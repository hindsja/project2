"""Financial invariants, timing counterexamples and HTTP behavior; standard library only."""
import copy
import csv
import io
import json
import math
import statistics
import sys
import tempfile
import threading
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from http.server import ThreadingHTTPServer

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import engine
import reporting
from app import handler_for


class FinancialTests(unittest.TestCase):
    def setUp(self):
        self.config = engine.load_config()

    def test_grid_complete_and_fully_invested(self):
        grid = engine.grid()
        self.assertEqual(len(grid), math.comb(24, 4))
        self.assertEqual(len(grid), len(set(grid)))
        self.assertTrue(all(abs(sum(w)-1) < 1e-12 and min(w) >= 0 for w in grid))

    def test_covariance_and_return_known_answer(self):
        estimates = {'returns': [.08, .04, 0, 0, 0],
                     'covariance': [[.04, .01, 0, 0, 0], [.01, .01, 0, 0, 0],
                                    [0]*5, [0]*5, [0]*5]}
        config = dict(self.config, current_weights=dict(zip(engine.TICKERS, [.5, .5, 0, 0, 0])))
        metrics = engine.portfolio_metrics([.5, .5, 0, 0, 0], estimates, config)
        self.assertAlmostEqual(metrics['gross_return'], .06)
        self.assertAlmostEqual(metrics['volatility'], math.sqrt(.0175))
        self.assertEqual(metrics['cost'], 0)

    def test_turnover_and_cost_count_both_sides(self):
        estimates = {'returns': [.08]*5, 'covariance': [[0]*5 for _ in range(5)]}
        result = engine.portfolio_metrics([0, 0, .35, .25, .4], estimates, self.config)
        self.assertAlmostEqual(result['turnover'], .25)
        self.assertAlmostEqual(result['cost'], .0005)
        self.assertAlmostEqual(result['net_return'], .0795)

    def test_month_labels_are_end_of_month(self):
        dates, prices, returns = engine.load_prices()
        self.assertEqual(dates[0], date(2021, 9, 30))
        self.assertEqual(dates[-1], date(2026, 9, 30))
        self.assertEqual((len(prices), len(returns)), (61, 60))

    def test_snapshot_prices_match_originals_and_raw_bil(self):
        original = list(csv.DictReader((engine.ROOT/'data/lab15_prices_original.csv').read_text().splitlines()))
        joined = list(csv.DictReader((engine.ROOT/'data/prices.csv').read_text().splitlines()))
        raw = json.loads((engine.ROOT/'data/bil_source.json').read_text())['chart']['result'][0]
        for old, new, bil in zip(original, joined, raw['indicators']['adjclose'][0]['adjclose']):
            for t in engine.TICKERS[:4]:
                self.assertEqual(old[t], new[t])
            self.assertAlmostEqual(float(new['BIL']), bil, places=7)

    def test_estimates_independent_portfolio_series(self):
        estimates = engine.estimate(self.config)
        _, _, returns = engine.load_prices()
        weights = [.1, .1, .3, .2, .3]
        portfolio_series = [sum(w*x for w,x in zip(weights,row)) for row in returns[-36:]]
        measured = engine.portfolio_metrics(weights, estimates, self.config)
        self.assertAlmostEqual(measured['volatility'], statistics.stdev(portfolio_series)*math.sqrt(12), places=12)
        for i in range(5):
            self.assertAlmostEqual(estimates['raw_returns'][i], sum(row[i] for row in returns[-36:])/3, places=12)

    def test_future_releases_cannot_change_prior_signal(self):
        rows = engine.load_signal_rows()
        prior = engine.unemployment_signal(self.config, rows)
        modified = copy.deepcopy(rows)
        for row in modified:
            if row['published on'] > self.config['decision_date']:
                row['value'] = '80.0'
        after = engine.unemployment_signal(self.config, modified)
        self.assertEqual(prior, after)
        self.assertIn(31, prior['excluded_future_rows'])
        self.assertEqual(prior['selected_rows'][-1]['month measured'], '2026-08')

    def test_missing_october_stops_signal(self):
        config = dict(self.config, decision_date='2025-12-31')
        result = engine.analyze(config)
        self.assertFalse(result['signal']['available'])
        self.assertIsNone(result['portfolios'][2])
        self.assertEqual(result['decision'], 'REJECT')

    def test_publication_lag_excludes_by_effective_date(self):
        config = dict(self.config, extra_lag_days=45)
        signal = engine.unemployment_signal(config)
        self.assertEqual(signal['selected_rows'][-1]['month measured'], '2026-07')
        self.assertTrue(signal['available'])

    def test_base_feasibility_and_baseline_failure(self):
        result = engine.analyze(self.config)
        p = result['portfolios'][2]
        self.assertEqual(p['weights'], {'EWY':0.0,'QQQM':0.0,'VOO':.35,'FNDX':.05,'BIL':.6})
        self.assertTrue(all(check['passed'] for check in p['checks']))
        self.assertEqual(result['portfolios'][0]['failed_rules'], ['Annual one-way turnover limit'])
        self.assertTrue(result['portfolios'][1]['passed'])

    def test_infeasible_constraints_do_not_relax(self):
        result = engine.analyze(dict(self.config, max_weight=.30))
        self.assertEqual(result['decision'], 'REJECT')
        self.assertEqual(result['feasible_count'], 0)
        self.assertIsNone(result['portfolios'][2])

    def test_invalid_config_rejected(self):
        for changes in [{'cost_bps': float('nan')}, {'window_months': 2}, {'extra_lag_days': -1},
                        {'max_weight': 2}, {'use_signal': 'false'}, {'decision_date':'2026-09-01'}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                engine.validate_config(dict(self.config, **changes))

    def test_duplicate_price_month_rejected(self):
        content = (engine.ROOT/'data/prices.csv').read_text().splitlines()
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)/'invalid.csv'
            target.write_text('\n'.join(content[:3]+[content[2]]+content[3:]))
            with self.assertRaises(ValueError):
                engine.load_prices(target)

    def test_future_prices_do_not_change_first_rebalance(self):
        original = engine.load_prices()
        changed = copy.deepcopy(original)
        for i, day in enumerate(changed[0][1:]):
            if day >= date(2026, 1, 31):
                changed[2][i][0] += .1
        before = engine.walk_forward(self.config)
        with patch.object(engine, 'load_prices', return_value=changed):
            after = engine.walk_forward(self.config)
        self.assertEqual(before['trades'][:3], after['trades'][:3])
        self.assertEqual(len(before['results'][0]['wealth']), 25)

    def test_snapshots_preserve_inputs_and_refuse_overwrite(self):
        report = engine.full_report(self.config)
        with tempfile.TemporaryDirectory() as folder, patch.object(reporting, 'ROOT', Path(folder)):
            target = reporting.save_report(report, snapshot='automated-check')
            saved = json.loads((target/'results.json').read_text())
            self.assertEqual(saved['config'], self.config)
            self.assertIn('(../../../docs/data-card.md)', (target/'decision-output.md').read_text())
            with self.assertRaises(FileExistsError):
                reporting.save_report(report, snapshot='automated-check')

    def test_stale_signal_blocks_new_allocation(self):
        result = engine.analyze(dict(self.config, extra_lag_days=120))
        self.assertFalse(result['signal']['available'])
        self.assertEqual(result['decision'], 'REJECT')


class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), handler_for(engine.load_config()))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_home_and_health(self):
        with urlopen(self.base) as response:
            self.assertIn(b'A portfolio you can question.', response.read())
        with urlopen(self.base+'/api/health') as response:
            self.assertEqual(json.load(response)['status'], 'ok')

    def test_interactive_change_recalculates_verdict(self):
        config = engine.load_config()
        config['max_weight'] = .30
        request = Request(self.base+'/api/analyze', data=json.dumps(config).encode(), headers={'Content-Type':'application/json'})
        with urlopen(request) as response:
            result = json.load(response)
        self.assertEqual(result['decision'], 'REJECT')

    def test_bad_inputs_and_unknown_paths(self):
        request = Request(self.base+'/api/analyze', data=b'{"cost_bps": -5}')
        with self.assertRaises(HTTPError) as error:
            urlopen(request)
        self.assertEqual(error.exception.code, 400)
        with self.assertRaises(HTTPError) as error:
            urlopen(self.base+'/../config.json')
        self.assertEqual(error.exception.code, 404)


if __name__ == '__main__':
    unittest.main()
