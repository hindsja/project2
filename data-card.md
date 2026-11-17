# Data card — Prices and point-in-time unemployment signal

**Historical decision cutoff:** September 30, 2026, after that day's releases and market close. A decision using that month's prices is implemented for the following month's returns; monthly data do not model intraday execution.

## Frozen prices

| Field | Definition |
|---|---|
| Universe | EWY, QQQM, VOO, FNDX, BIL |
| Source | Yahoo Finance chart API adjusted-close monthly bars; endpoints below |
| Units | USD adjusted prices; monthly simple returns in decimal fractions |
| Coverage | 61 price observations, September 2021–September 2026; 60 returns |
| Snapshot dates | Equity file October 21, 2026; BIL November 16, 2026 |
| Timing | CSV first-of-month labels designate the monthly bar, not prices available on that first day; engine converts to month-end |
| Adjustments | Provider-adjusted for splits/distributions; historical values may be revised |
| Validation | Exact months, positive finite prices, unique consecutive dates, matching currencies/coverage for BIL join; no gap filling |
| Evidence | `data/lab15_prices_original.csv`, `data/bil_source.json`, `data/prices.csv`, `data/provenance.json` |

The equity file is preserved from Lab 15, not newly independently retrieved in this project. Its source was recorded in that lab. The BIL source JSON was retrieved and checked during this project. These are retrospective snapshots; they do not establish point-in-time price vintages. Selection of these surviving funds is not a survivorship-free market-wide study.

Source endpoints use `period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true`:
[EWY](https://query2.finance.yahoo.com/v8/finance/chart/EWY?period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true),
[QQQM](https://query2.finance.yahoo.com/v8/finance/chart/QQQM?period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true),
[VOO](https://query2.finance.yahoo.com/v8/finance/chart/VOO?period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true),
[FNDX](https://query2.finance.yahoo.com/v8/finance/chart/FNDX?period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true),
[BIL](https://query1.finance.yahoo.com/v8/finance/chart/BIL?period1=1630454400&period2=1790812800&interval=1mo&events=history&includeAdjustedClose=true).

BIL's issuer describes exposure to publicly issued U.S. Treasury bills with one to three months remaining maturity: [State Street BIL](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil), checked November 16, 2026. This verifies the defensive sleeve's instrument category, not future price stability or returns.

## UNRATE publication-vintage signal

| Field | Definition |
|---|---|
| Primary origin | U.S. Bureau of Labor Statistics, Current Population Survey |
| Archive | [ALFRED UNRATE](https://alfred.stlouisfed.org/series?seid=UNRATE) |
| Measure | Seasonally adjusted unemployment rate, percent of the civilian labor force, monthly |
| Local snapshot | Preserved Lab 17 CSV downloaded October 28, 2026 |
| Coverage | July 2024–September 2026; 26 measured months across 27 calendar months, 31 first-release/changed-value records |
| Publication field | ALFRED vintage date when a value first appeared or changed; unchanged carry-forward copies omitted |
| Rule units | Difference of rates in **percentage points**; 4.2% to 4.3% is +0.1 percentage point |
| Availability | Publication date plus configured extra lag must be on/before decision date |
| Revision handling | Keep latest eligible publication for each measured month |
| Missingness | No imputation; latest and previous calendar month must both be available |
| Freshness | Latest measured month-end must be within 100 days of the decision |
| Decision use | A rise of at least 0.10 percentage point raises minimum BIL to 40% at an annual decision |
| Failure | Stop new constrained orders if signal unavailable; keep and monitor existing holdings |

October 2025 is absent from the source table; the [BLS revised-release explanation](https://www.bls.gov/bls/2025-lapse-revised-release-dates.htm) states the household survey was not collected for that reference month. September 2025's delayed publication is November 20. At December 31, the November observation cannot be paired with missing October, so the signal is unavailable. The engine tests this explicitly.

At September 30, 2026, the September observation published October 2 is excluded. The app displays the exact eligible months, vintage dates and source-row IDs used. The Lab 17 relative-change signal is deliberately replaced here with a percentage-point difference to avoid confusing a relative percentage change with a change in unemployment-rate points.

See [ALFRED help](https://alfred.stlouisfed.org/help) for vintage semantics. Source assertions above are inherited from the documented Lab 17 audit; this project reuses and tests the local vintage rows rather than claiming a new independent download of every vintage.

## Limits on interpretation

This small macro series has not demonstrated causal or predictive value for these funds. The model/rule were designed after the historical period existed. The chronological diagnostic checks implementation timing, not true prospective performance. Fund overlap, Korea exposure/currency risk within EWY, covariance shifts, falling bill yields, trading spreads, taxes and intramonth losses remain relevant. No live data feed or automatic broker execution exists.
