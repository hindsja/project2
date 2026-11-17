"""Auditable portfolio calculations. Fractions internally; percentage points only where named.

The 5-percentage-point grid is intentionally small enough to inspect and explain.
This is an educational historical process review, not a live trading system.
"""
import calendar
import csv
import hashlib
import itertools
import json
import math
import statistics
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TICKERS = ('EWY', 'QQQM', 'VOO', 'FNDX', 'BIL')
EPS = 1e-10


def month_end(label):
    day = date.fromisoformat(label)
    return date(day.year, day.month, calendar.monthrange(day.year, day.month)[1])


def previous_month(label):
    return (date.fromisoformat(label + '-01') - timedelta(days=1)).strftime('%Y-%m')


def load_config(path=None):
    config = json.loads(Path(path or ROOT / 'config.json').read_text(encoding='utf-8'))
    validate_config(config)
    return config


def validate_config(config):
    expected = {'decision_date', 'window_months', 'target_return', 'max_volatility', 'max_weight',
                'min_bil', 'max_turnover', 'cost_bps', 'equity_return_cap', 'equity_shift_pp',
                'extra_lag_days', 'use_signal', 'signal_rise_pp', 'defensive_min_bil',
                'max_signal_age_days', 'current_weights'}
    if set(config) != expected:
        raise ValueError('Configuration keys must match config.json exactly.')
    cutoff = date.fromisoformat(config['decision_date'])
    if cutoff != month_end(cutoff.isoformat()):
        raise ValueError('Decision date must be a completed calendar month-end.')
    ranges = {'target_return': (-.10, .30), 'max_volatility': (.001, 1),
              'max_weight': (0, 1), 'min_bil': (0, 1), 'max_turnover': (0, 1),
              'cost_bps': (0, 1000), 'equity_return_cap': (0, .30),
              'equity_shift_pp': (-20, 20), 'signal_rise_pp': (.01, 5),
              'defensive_min_bil': (0, 1)}
    for name, (low, high) in ranges.items():
        value = config[name]
        if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or not low <= value <= high:
            raise ValueError(f'{name} must be finite and between {low} and {high}.')
    for name, low, high in [('window_months', 12, 60), ('extra_lag_days', 0, 120),
                             ('max_signal_age_days', 1, 365)]:
        value = config[name]
        if type(value) is not int or not low <= value <= high:
            raise ValueError(f'{name} must be an integer between {low} and {high}.')
    if type(config['use_signal']) is not bool:
        raise ValueError('use_signal must be true or false.')
    weights = config['current_weights']
    if set(weights) != set(TICKERS) or any(type(x) not in (float, int) or not math.isfinite(x) or x < 0 for x in weights.values()):
        raise ValueError('Current weights must cover all five tickers with finite nonnegative weights.')
    if abs(sum(weights.values()) - 1) > EPS:
        raise ValueError('Current weights must sum to one.')


def load_prices(path=None):
    with Path(path or ROOT / 'data/prices.csv').open(newline='', encoding='utf-8-sig') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ['Date', *TICKERS]:
            raise ValueError('Unexpected price headers.')
        rows = list(reader)
    dates, matrix = [], []
    for row in rows:
        observed = month_end(row['Date'])
        if dates:
            expected = (dates[-1].replace(day=28) + timedelta(days=4)).replace(day=1)
            if observed.replace(day=1) != expected:
                raise ValueError('Price months must be consecutive, unique and increasing.')
        values = [float(row[t]) for t in TICKERS]
        if any(not math.isfinite(x) or x <= 0 for x in values):
            raise ValueError('Missing, nonfinite or nonpositive adjusted price.')
        dates.append(observed)
        matrix.append(values)
    if len(matrix) < 13:
        raise ValueError('At least thirteen monthly prices are required.')
    returns = [[new[i] / old[i] - 1 for i in range(5)] for old, new in zip(matrix, matrix[1:])]
    return dates, matrix, returns


def load_signal_rows(path=None):
    with Path(path or ROOT / 'data/unrate_vintages.csv').open(newline='', encoding='utf-8-sig') as handle:
        rows = list(csv.DictReader(handle))
    seen = set()
    identifiers = set()
    for row in rows:
        if row['series name'] != 'UNRATE' or row['row'] in identifiers:
            raise ValueError('Signal requires UNRATE and unique row identifiers.')
        identifiers.add(row['row'])
        observed = month_end(row['month measured'] + '-01')
        published = date.fromisoformat(row['published on'])
        value = float(row['value'])
        if published <= observed or not math.isfinite(value) or not 0 < value < 100:
            raise ValueError('Invalid unemployment value or publication date.')
        key = (row['month measured'], row['published on'])
        if key in seen:
            raise ValueError('Duplicate or conflicting signal publication.')
        seen.add(key)
    return rows


def unemployment_signal(config, rows=None):
    """Only use the latest eligible vintage for each month; never bridge a missing month."""
    cutoff = date.fromisoformat(config['decision_date'])
    rows = rows if rows is not None else load_signal_rows()
    selected = {}
    excluded = []
    for row in rows:
        available = date.fromisoformat(row['published on']) + timedelta(days=config['extra_lag_days'])
        if available > cutoff:
            excluded.append(int(row['row']))
            continue
        month = row['month measured']
        if month not in selected or row['published on'] > selected[month]['published on']:
            selected[month] = row
    result = {'available': False, 'reason': '', 'rise_pp': None, 'defensive': False,
              'selected_rows': [], 'excluded_future_rows': excluded}
    if not selected:
        result['reason'] = 'No unemployment release is available by the cutoff.'
        return result
    latest = max(selected)
    prior = previous_month(latest)
    if prior not in selected:
        result['reason'] = 'The two newest required measured months are not consecutive; no filling is allowed.'
        return result
    if (cutoff - month_end(latest + '-01')).days > config['max_signal_age_days']:
        result['reason'] = 'Latest knowable observation exceeds the allowed data age.'
        return result
    chosen = [selected[prior], selected[latest]]
    rise = float(chosen[1]['value']) - float(chosen[0]['value'])
    result.update(available=True, rise_pp=rise,
                  defensive=rise + EPS >= config['signal_rise_pp'], selected_rows=chosen,
                  reason='Use latest published vintages; change measured in percentage points, not percent.')
    return result


def estimate(config, prices=None):
    dates, _, returns = prices or load_prices()
    cutoff = date.fromisoformat(config['decision_date'])
    if cutoff not in dates:
        raise ValueError('Decision date is outside the frozen price snapshot.')
    end = dates.index(cutoff)
    count = config['window_months']
    if end < count:
        raise ValueError(f'Only {end} monthly returns are available; {count} requested.')
    sample = returns[end-count:end]
    columns = list(zip(*sample))
    means = [statistics.mean(column) for column in columns]
    raw = [value * 12 for value in means]
    # The 10% equity ceiling is an explicit conservative modeling assumption, not a forecast.
    adjusted = [min(value, config['equity_return_cap']) + config['equity_shift_pp'] / 100
                if i < 4 else value for i, value in enumerate(raw)]
    covariance = [[12 * sum((r[i]-means[i]) * (r[j]-means[j]) for r in sample)/(count-1)
                   for j in range(5)] for i in range(5)]
    return {'raw_returns': raw, 'returns': adjusted, 'covariance': covariance,
            'start': dates[end-count].isoformat(), 'end': dates[end].isoformat(), 'months': count}


def one_way_turnover(weights, current):
    """Half the sum of absolute weight changes: 25% sold + 25% bought = 25% turnover."""
    return sum(abs(weights[i] - current[i]) for i in range(5)) / 2


def portfolio_metrics(weights, estimates, config):
    current = [config['current_weights'][t] for t in TICKERS]
    turnover = one_way_turnover(weights, current)
    # Cost is charged on BOTH buys and sells; bps is cost per dollar traded on each side.
    cost = 2 * turnover * config['cost_bps'] / 10000
    gross = sum(w * mu for w, mu in zip(weights, estimates['returns']))
    variance = sum(weights[i] * weights[j] * estimates['covariance'][i][j]
                   for i in range(5) for j in range(5))
    if variance < -EPS:
        raise ValueError('Covariance produced negative portfolio variance.')
    return {'weights': dict(zip(TICKERS, weights)), 'gross_return': gross,
            'net_return': gross - cost, 'volatility': math.sqrt(max(variance, 0)),
            'turnover': turnover, 'cost': cost}


def mandate_checks(metrics, config, signal):
    weights = list(metrics['weights'].values())
    reserve = config['min_bil']
    if config['use_signal'] and signal['available'] and signal['defensive']:
        reserve = max(reserve, config['defensive_min_bil'])
    checks = [
        ('Fully invested', abs(sum(weights)-1) <= EPS, sum(weights), 1),
        ('Long-only; no leverage', min(weights) >= -EPS, min(weights), 0),
        ('Estimated net return target', metrics['net_return'] + EPS >= config['target_return'], metrics['net_return'], config['target_return']),
        ('Estimated volatility limit', metrics['volatility'] <= config['max_volatility'] + EPS, metrics['volatility'], config['max_volatility']),
        ('Single-fund limit', max(weights) <= config['max_weight'] + EPS, max(weights), config['max_weight']),
        ('Treasury-bill minimum', weights[4] + EPS >= reserve, weights[4], reserve),
        ('Annual one-way turnover limit', metrics['turnover'] <= config['max_turnover'] + EPS, metrics['turnover'], config['max_turnover']),
        ('Point-in-time signal available', not config['use_signal'] or signal['available'], None, None),
    ]
    return [{'rule': name, 'passed': bool(ok), 'value': value, 'limit': limit} for name, ok, value, limit in checks]


@lru_cache(maxsize=1)
def grid():
    # Stars-and-bars: 10,626 possible 5-point portfolios across five funds.
    result = []
    for cuts in itertools.combinations(range(24), 4):
        boundaries = (-1, *cuts, 24)
        result.append(tuple((boundaries[i+1]-boundaries[i]-1)/20 for i in range(5)))
    return tuple(result)


def evaluate(weights, estimates, config, signal, name):
    metrics = portfolio_metrics(weights, estimates, config)
    checks = mandate_checks(metrics, config, signal)
    return dict(metrics, name=name, checks=checks, passed=all(c['passed'] for c in checks),
                failed_rules=[c['rule'] for c in checks if not c['passed']])


def optimize(estimates, config, signal):
    if config['use_signal'] and not signal['available']:
        return None, 0
    reserve = max(config['min_bil'], config['defensive_min_bil']
                  if config['use_signal'] and signal['defensive'] else config['min_bil'])
    best, feasible = None, 0
    current = [config['current_weights'][t] for t in TICKERS]
    for weights in grid():
        if max(weights) > config['max_weight'] + EPS or weights[4] + EPS < reserve:
            continue
        if one_way_turnover(weights, current) > config['max_turnover'] + EPS:
            continue
        metrics = portfolio_metrics(weights, estimates, config)
        if metrics['net_return'] + EPS < config['target_return'] or metrics['volatility'] > config['max_volatility'] + EPS:
            continue
        feasible += 1
        key = (metrics['volatility'], metrics['turnover'], weights)
        if best is None or key < best[0]:
            best = (key, weights)
    return (evaluate(best[1], estimates, config, signal, 'Constrained portfolio') if best else None), feasible


def analyze(config, prices=None):
    validate_config(config)
    estimates = estimate(config, prices)
    signal = unemployment_signal(config)
    baseline = evaluate((0, 0, .6, 0, .4), estimates, config, signal, '60/40 benchmark')
    equal = evaluate((.2,) * 5, estimates, config, signal, 'Equal weight')
    selected, feasible = optimize(estimates, config, signal)
    decision = 'PILOT' if selected else 'REJECT'
    condition = ('Pilot only in a 5-10% shadow sleeve, with 0% live allocation; reverse to reject if the '
                 'signal is unavailable or no allocation meets the mandate. Consider live adoption only after '
                 '12 prospective monthly observations, net return at least the benchmark, realized annualized '
                 'volatility at most 15%, and no mandate breach at an annual rebalance.') if selected else (
                 'Reject a new allocation under these inputs; reconsider only when valid data and a portfolio '
                 'meeting every mandate rule are available. Do not override limits to force a result.')
    return {'config': config, 'estimates': estimates, 'signal': signal, 'portfolios': [equal, baseline, selected],
            'feasible_count': feasible, 'decision': decision, 'decision_line': condition,
            'live_allocation_range': [0, 0], 'shadow_allocation_range': [.05, .10] if selected else [0, 0]}


def stress_suite(config):
    scenarios = [
        ('Base', {}), ('Equity estimates -3 percentage points', {'equity_shift_pp': -3.0}),
        ('60-month estimation window', {'window_months': 60}),
        ('Trading cost 100 bps per side', {'cost_bps': 100.0}),
        ('Volatility ceiling 4%', {'max_volatility': .04}),
        ('Single-fund ceiling 30%', {'max_weight': .30}),
        ('Release availability +45 days', {'extra_lag_days': 45}),
        ('Signal disabled (diagnostic only)', {'use_signal': False}),
    ]
    results = []
    for name, changes in scenarios:
        case = analyze(dict(config, **changes))
        results.append({'scenario': name, 'changes': changes, 'decision': case['decision'],
                        'portfolio': case['portfolios'][2], 'signal': case['signal']})
    return results


def walk_forward(config, use_signal=True):
    """24-month chronological diagnostic; estimates precede each return, not an unseen holdout.

    Rebalance at September month-end once per year. Missing signals/no feasible mix stop
    new orders and retain existing holdings; monitoring still records the issue.
    """
    dates, matrix, returns = load_prices()
    start = dates.index(date(2024, 9, 30))
    end = dates.index(date(2026, 9, 30))
    names = ('Constrained', 'Equal weight', '60/40 benchmark')
    holdings = {name: [0, 0, .6, 0, .4] for name in names}
    wealth = {name: 1.0 for name in names}
    history = {name: [1.0] for name in names}
    monthly = {name: [] for name in names}
    trades, monitoring = [], []
    costs = {name: 0.0 for name in names}
    for k in range(start, end):
        decision_date = dates[k].isoformat()
        signal_config = dict(config, decision_date=decision_date, use_signal=use_signal, window_months=36)
        signal = unemployment_signal(signal_config)
        if use_signal and not signal['available']:
            monitoring.append({'date': decision_date, 'event': 'Signal unavailable: block new orders, retain holdings', 'reason': signal['reason']})
        for name in names:
            cost = 0.0
            if k in (start, start + 12):
                local = dict(signal_config, current_weights=dict(zip(TICKERS, holdings[name])))
                estimates = estimate(local, (dates, matrix, returns))
                if name == 'Constrained':
                    chosen, _ = optimize(estimates, local, signal)
                    target = list(chosen['weights'].values()) if chosen else None
                else:
                    target = [.2]*5 if name == 'Equal weight' else [0, 0, .6, 0, .4]
                    chosen = evaluate(target, estimates, local, signal, name)
                # Baselines execute their stated rules even when failing; breaches are exposed.
                if target is not None:
                    turn = one_way_turnover(target, holdings[name])
                    cost = 2 * turn * config['cost_bps'] / 10000
                    holdings[name] = target
                trades.append({'date': decision_date, 'portfolio': name, 'weights': dict(zip(TICKERS, holdings[name])),
                               'executed': target is not None, 'cost': cost,
                               'passed': chosen['passed'] if chosen else False,
                               'failed_rules': chosen['failed_rules'] if chosen else ['No feasible allocation / unavailable signal']})
            r = sum(w * x for w, x in zip(holdings[name], returns[k]))
            net = (1-cost) * (1+r) - 1
            wealth[name] *= 1+net
            costs[name] += cost
            monthly[name].append(net)
            history[name].append(wealth[name])
            holdings[name] = [w * (1+x)/(1+r) for w, x in zip(holdings[name], returns[k])]
            if max(holdings[name]) > config['max_weight'] + EPS or holdings[name][4] < config['min_bil']-EPS:
                monitoring.append({'date': dates[k+1].isoformat(), 'portfolio': name,
                                   'event': 'Drift outside weight limits: flag for committee; no unscheduled trade assumed'})
    summaries = []
    for name in names:
        peak, drawdown = 1.0, 0.0
        for value in history[name]:
            peak = max(peak, value)
            drawdown = min(drawdown, value/peak-1)
        summaries.append({'name': name, 'total_return': wealth[name]-1,
                          'cagr': wealth[name]**(12/len(monthly[name]))-1,
                          'volatility': statistics.stdev(monthly[name])*math.sqrt(12),
                          'max_drawdown': drawdown, 'sum_trade_cost_fractions': costs[name],
                          'wealth': history[name]})
    return {'start': dates[start].isoformat(), 'end': dates[end].isoformat(), 'months': end-start,
            'signal_enabled': use_signal, 'results': summaries, 'trades': trades, 'monitoring': monitoring,
            'limitations': 'Retrospective 24-month chronological diagnostic, not an untouched holdout. Rule selected after data existed. Only two annual rebalances; revised adjusted-price snapshots. No taxes. Baselines execute even when mandate fails; failures are recorded.'}


def fingerprint():
    paths = ['data/prices.csv', 'data/unrate_vintages.csv', 'config.json', 'engine.py']
    return {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in paths}


def full_report(config=None):
    config = config or load_config()
    result = analyze(config)
    result.update(stresses=stress_suite(config), walk_forward=walk_forward(config),
                  without_signal=walk_forward(config, use_signal=False), fingerprints=fingerprint())
    return result
