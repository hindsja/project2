AI announcement: Codex (GPT-6) assisted with app implementation, data processing, validation and drafting. Sources, assumptions and actual checks are documented.

The submitting analyst is responsible for reviewing the analysis and owning the final decision. Education, not investment advice.

# ETF Portfolio Committee Dashboard

**Decision: pilot in a simulated sleeve; allocate 0% of live capital.** The base result is 35% VOO / 5% FNDX / 60% BIL inside the shadow sleeve, with 6.57% estimated net annual return and 4.90% estimated volatility. Stop new orders if data are unavailable or no portfolio meets the mandate. These are historical estimates as of **September 30, 2026**, not current recommendations.

## Run the app

Requires **Python 3.10 or later** and a modern browser. No packages, account, API key or network access are needed after downloading the repository.

1. Download this repository's ZIP from GitHub's **Code → Download ZIP**, then extract it. Do not run inside the ZIP.
2. Open a terminal **in the folder containing this README, `app.py` and `config.json`**. If the project is inside a larger course repository, enter its `project2` folder first.
3. Run this one command:

```text
python app.py
```

4. Open **http://127.0.0.1:8766** in a browser. Leave the terminal running. Change a control and select **Recalculate portfolio**; inspect the mandate verdict.

If Windows does not recognize `python`, try `py -3 app.py`. On macOS/Linux, try `python3 app.py`. If port 8766 is occupied, use `python app.py --port 8767` and open the printed address. If Python is not installed, install Python 3.10+ from [python.org](https://www.python.org/downloads/). Ctrl+C stops the app.

**Read without running anything:** [saved decision output](outputs/decision-output.md), [committee memo](docs/decision-memo.md), [validation](docs/validation-and-ai-use.md).

## What the app decides

For a hypothetical seven-year investor with no withdrawals, compare equal weight, 60% VOO / 40% BIL, and the lowest-estimated-volatility feasible allocation on a 5-percentage-point grid. Each has its own pass/fail verdict and failed rules. No feasible portfolio means **REJECT**, never an automatic relaxation of the limits.

The approved mandate is a 6.5% estimated net return target, 15% estimated volatility ceiling, 60% single-fund ceiling, 10% BIL floor, 25% annual one-way turnover limit, long-only and no borrowing. Rebalance annually; monitor monthly. The assumed starting portfolio is 60% VOO / 40% BIL. See [mandate and assumptions](docs/mandate.md).

EWY, QQQM, VOO and FNDX are equity funds; BIL holds short-maturity U.S. Treasury bills. An ETF share is not an insured bank deposit. Fund allocations do not measure underlying issuer concentration or eliminate overlapping equity exposures.

## Point-in-time evidence

The unemployment risk rule admits only publications available by the decision date and retains the latest eligible vintage per measured month. A rise of at least 0.10 percentage point raises the BIL floor to 40%. Missing consecutive months or observations older than 100 days block new orders. See the [data card](docs/data-card.md). This rule is experimental; it has not demonstrated predictive value.

The four equity price series are preserved Lab 15 inputs downloaded October 21, 2026; BIL was downloaded November 16, 2026. Prices cover September 2021–September 2026. UNRATE vintages are preserved Lab 17 inputs downloaded October 28, 2026. Monthly date labels are converted to month-end before estimation. Prices are retrospective adjusted-close snapshots, not archived price vintages.

## Reproduce and inspect

```text
python app.py --export
python -m unittest discover -s tests -v
python tools/cold_run.py
```

`--export` rewrites the base output and generated committee memo from `config.json`. Keep personal records in their separate files. Starting or interacting with the web app does not change saved files. Downloading a scenario saves its JSON through your browser.

| File | Purpose |
|---|---|
| `engine.py` | Date filtering, return/covariance estimates, turnover/costs, mandate checks, search, stresses and chronological diagnostic |
| `app.py` | Local Python HTTP server and export/snapshot command |
| `reporting.py` | Consistent saved output and decision memo |
| `config.json` | Explicit base settings and assumed starting weights |
| `static/index.html` | Offline browser interface |
| `data/` | Frozen inputs, raw BIL response and provenance hashes |
| `outputs/results.json` | Full numbers, trade logs, checks, stresses and fingerprints |
| `docs/lab20-readiness.md` | Partner cold-run note and Lab 20 evidence status |
| `docs/locked-changed-input.md` | Human-only prediction and subsequent result; still pending |
| `SUBMIT.md` | What to upload and what to submit for each assignment |

## Locked changed-input workflow

The automated stress suite is **not** the required human-authored record. Close AI before choosing a new input/value and writing the prediction in `docs/locked-changed-input.md`. Record the old/new values, units, expected numerical direction and decision effect. Commit and push that prediction **before** running the changed case; preserve its commit link. Do not claim a prediction for a scenario whose result you have already seen.

Then save the unchanged output, make a copy of `config.json` named `changed-config.json`, edit only the chosen input, and run:

```text
python app.py --snapshot lab20-before
python app.py --config changed-config.json --snapshot lab20-after
```

These commands create `outputs/snapshots/lab20-before/` and `outputs/snapshots/lab20-after/`; existing snapshot names are refused. Record and interpret the actual result below the prediction, run `python tools/sync_record.py` to embed that record in the validation attachment, then commit/push the changed config, both outputs and completed documents. If a rerun needs a new label, use a new name rather than deleting evidence. The embedded config in each JSON is the authoritative scenario input.

## Limitations and completion status

The 24-month chronological diagnostic is retrospective, with only two annual rebalances; it is not an untouched holdout. Baselines execute their fixed rules even when they fail the mandate; failures are exposed in trade logs. The constrained process retains existing holdings when new orders are blocked. Weight drift is monitored, not automatically traded away. Annualized volatility is not a maximum-loss guarantee. The equity-return ceiling, signal threshold, starting weights and transaction costs are modeling assumptions, not proven forecasts.

The student AI-off prediction, partner cold run/code explanation, final analyst review, GitHub publication and three recorded videos/transcripts are **not claimed complete**. See [Lab 20](docs/lab20-readiness.md) and [submission guide](SUBMIT.md). The final recommendation can remain a truthful pilot or reject.
