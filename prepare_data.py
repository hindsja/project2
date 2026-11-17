"""Join the preserved Lab 15 prices to the downloaded BIL response, without filling gaps."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = ROOT / 'data/bil_source.json'
    response = json.loads(source.read_text(encoding='utf-8'))['chart']['result'][0]
    if response['meta']['currency'] != 'USD':
        raise ValueError('BIL must be priced in USD.')
    dates = response['timestamp']
    values = response['indicators']['adjclose'][0]['adjclose']
    if len(dates) != len(values):
        raise ValueError('BIL timestamps and prices differ in length.')
    bil = {}
    for timestamp, value in zip(dates, values):
        month = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-01')
        if month in bil or value is None or value <= 0:
            raise ValueError('Missing or duplicate BIL month.')
        bil[month] = value
    with (ROOT / 'data/lab15_prices_original.csv').open(newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    if set(bil) != {row['Date'] for row in rows} or len(rows) != 61:
        raise ValueError('Expected matching 61-month histories.')
    target = ROOT / 'data/prices.csv'
    with target.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=['Date', 'EWY', 'QQQM', 'VOO', 'FNDX', 'BIL'])
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(row, BIL=f"{bil[row['Date']]:.8f}"))
    metadata = {
        'price_period': '2021-09 through 2026-09; month labels denote MONTH-END observations',
        'equity_snapshot_download': '2026-10-21 (preserved Lab 15 file)',
        'bil_snapshot_download': '2026-11-16',
        'bil_source': 'https://query1.finance.yahoo.com/v8/finance/chart/BIL?period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true',
        'signal_snapshot_download': '2026-10-28 (preserved Lab 17 file)',
        'limitations': 'Adjusted prices are retrospective snapshots, not archived historical price vintages. Only UNRATE has publication-vintage filtering. Returns include provider distribution/split adjustments; do not subtract fund expense ratios again.',
        'sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in [target, source, ROOT / 'data/lab15_prices_original.csv', ROOT / 'data/unrate_vintages.csv']},
    }
    (ROOT / 'data/provenance.json').write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    print('Prepared 61 complete monthly prices for five funds; no prices filled.')


if __name__ == '__main__':
    main()
