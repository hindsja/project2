# Validation and AI use

**Analysis cutoff:** September 30, 2026. **Preparation:** November 16, 2026, America/Indianapolis; execution logs use UTC.
AI assistance: Codex (GPT-6), as exposed in this session, implemented and checked the technical package. No independent student execution, partner review or final sign-off is claimed.

## Evidence and actual checks

| Area | Method | Evidence |
|---|---|---|
| Prices | Preserve Lab 15 equity values; join BIL by month; require positive finite values, exact dates and matching coverage | [provenance](../data/provenance.json), `test_snapshot_prices_match_originals_and_raw_bil` |
| Return/covariance arithmetic | Known-answer two-asset fixture; independently compute volatility of the weighted monthly portfolio return series | `test_covariance_and_return_known_answer`, `test_estimates_independent_portfolio_series` |
| Trading costs | 25% sold plus 25% bought at 10 bps per side costs 0.05% of capital | `test_turnover_and_cost_count_both_sides` |
| Grid integrity | 10,626 unique nonnegative five-fund weights, each summing to one | `test_grid_complete_and_fully_invested` |
| Mandate | Base constrained portfolio passes; equal weight fails turnover; infeasible fund caps reject rather than relax | Financial tests and [saved output](../outputs/decision-output.md) |
| Timing leakage | Change future publications radically and verify prior signal unchanged; change later prices and verify first rebalance unchanged | Timing counterexample tests |
| Missing data | October 2025 gap blocks December signal; duplicate months and malformed settings are rejected | Missing-month and input tests |
| UI/server calculation path | HTTP home/health; POST changed constraint yields REJECT; invalid payload returns 400 | HTTP tests |
| Fresh-folder reproducibility | New copied folder, disabled site-packages, start server, read outputs, change control via API, export | [automated cold run](../outputs/automated-cold-run.json) |

Exact executed test names, counts, interpreter and completion timestamp are recorded in [test-results.txt](../outputs/test-results.txt) and [verification.json](../outputs/verification.json).
These are AI-run tests. They provide arithmetic/invariant/counterexample evidence, not independent human endorsement or proof that the financial assumptions are true.

## Baselines and stress tests

Equal weight allocates 20% to each fund. The second baseline/benchmark is 60% VOO / 40% BIL. Each is evaluated against the same mandate and starting holdings; equal weight is not silently exempted from turnover.

The constrained search minimizes estimated volatility on a 5-point grid, subject to the target return, risk, weight, BIL and turnover rules. [Actual results](../outputs/results.json) preserve every base verdict, eligible signal row, scenario and chronological trade log.

Stress dimensions are equity estimates, 36 versus 60 months, trading costs, risk/position constraints, publication lag and removal of the macro rule. Infeasible scenarios produce no new allocation. These automated scenarios are not the human changed-input record.

The 24-month historical diagnostic uses annual September rebalances, 36 trailing monthly returns, subsequent monthly performance, drifted holdings, and costs on both buys and sells. Baselines implement their transparent allocation rules even when infeasible and record failed checks. A missing signal or infeasible constrained search retains holdings and records a block. Monthly drift warnings do not assume unapproved off-cycle trades.

## Locked Changed-Input Record

The canonical record is [locked-changed-input.md](locked-changed-input.md), submitted with this file. The student supplied the 6.5%-to-8.0% target change and predicted higher estimated volatility, different weights and an unchanged PILOT decision. **The pre-run public commit was verified and the assistant ran both cases on November 17, 2026.** Estimated volatility increased from 4.8995% to 7.8972%, allocations changed, and PILOT remained. Exact outputs, commit link, timestamps and AI-assisted interpretation are preserved in that record and its appendix. The AI-off phase is not verified; student review and explanation remain pending.

Before final Project 2 submission, that linked record must contain the actual completed evidence. The shared record also supplies the changed-input evidence for [Lab 20](lab20-readiness.md); there are no competing versions of the prediction.

## Material AI contributions and dispositions

| Contribution | Current disposition | Evidence or reason | Student review |
|---|---|---|---|
| Five-fund app concept including a Treasury-bill fund | Accepted by user in conversation | Builds on existing Lab 15 work and adds a defensive sleeve | Concept approved |
| Seven-year hypothetical mandate and numerical limits | Accepted by user in conversation | Explicit proposal and user approval before implementation | Mandate approved |
| Conservative 10% equity estimate ceiling | Implemented as a disclosed AI proposal | Historical mean sensitivity and stress tests; not a proven forecast | Final acceptance/reason pending |
| UNRATE threshold, freshness and defensive-floor rules | Implemented as disclosed AI proposals | Vintage filter, future-row counterexample and missing-month failure | Final acceptance/reason pending |
| Python search, turnover and covariance code | Implemented and AI-tested | Known-answer/invariant checks and saved execution logs | Student code explanation pending |
| Pilot recommendation rather than adoption | AI-assisted draft | Thin return buffer; short retrospective history; no established signal advantage | Final analyst decision pending |
| Memo, data card, README and submission structure | AI-assisted drafts | Numbers generated from the same report; sources and limitations linked | Final review pending |

The user approved the concept and mandate; no additional personal disposition or learning history has been inferred. There was no parameter search to optimize signal backtest performance. The choices were nevertheless made after the historical period, so model-selection bias remains.

## Source boundaries and limitations

- Equity price provenance is inherited from Lab 15. BIL's raw response is saved. UNRATE vintages and source audit are inherited from Lab 17. See [data card](data-card.md).
- No independent second-vendor price reconciliation is claimed. Prices are retrospective adjusted snapshots; only UNRATE has vintage filtering.
- The chronological diagnostic is not a prospective or untouched test; two rebalances and 24 returns cannot establish predictive value.
- No tax model, broker execution, full liquidity stress, underlying ETF issuer concentration audit, seven-year withdrawal simulation or intramonth drawdown measurement is claimed.
- The common month-end implementation convention approximates execution; monthly bars do not support exact next-session fill prices.
- Visual browser QA remains outstanding. On November 23 the browser host was unavailable, and native control stopped because the current Chrome URL could not be established reliably. HTTP checks passed; this is not a visual UI check.
- The user's initial public GitHub upload was inspected at commit `ca88b2520a0c83c1908c9853b3756db0dffe3768`: all prepared file contents were present, but six subfolders were flattened and `.gitignore` was named `download`. A raw-download run failed on the missing `data/prices.csv` path. The repaired folders and post-prediction outputs were verified in public commit `20010a6ecbe0ac1931e631964e01b989f9f9c2ee` on November 23; the downloaded repository passed all 19 original tests and its cold run. November 23 refinements are local until uploaded. See [repository audit](repository-upload-audit.md).
- No partner cold run, verified human AI-off explanation/prediction phase, YouTube video, actual transcript or Brightspace submission is claimed.

## Course references

[Project 2](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md),
[AI Boundary Card](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/AI-BOUNDARY-CARD.md),
[student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md),
[Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md).
Project 2 has no Edition A checkpoint; the lab's explicitly AI-off activities still apply. Brightspace controls actual deadlines and final submission fields.


## November 23 final preparation

Codex (GPT-6) inspected the public repository, the current Project 2 brief, checklist, AI Boundary Card and Lab 13 follow-on instructions. The public repaired repository passed 19 tests and a fresh-folder check. Final local changes correct order-dependent BIL checks, expose missing-data HTTP errors without local paths, hide obsolete browser results after failed recalculation, and fix memo range/parameter formatting. These are implementation corrections; the base financial model, mandate, frozen prices and original prediction/snapshots are preserved.

The final run results and hashes are in [final verification](final-verification.md) and [machine-readable evidence](../outputs/final-verification.json). Tests are AI-run. The browser visual check, human review/AI dispositions, AI-off evidence and actual videos are not asserted complete. No model version more specific than GPT-6 is exposed.

Lab 13 explicitly permits the student's own client mandate after the common Meridian exercise, with AI open. See [mandate](mandate.md) for the source and unresolved client question. This explains the different benchmark/objective; no instructor approval or earlier submission date is invented.

<!-- LOCKED-RECORD-APPENDIX -->

## Appendix — Locked Changed-Input Record

**Status: pre-run GitHub publication verified; before/after test completed by the assistant on November 17, 2026.** Part A is preserved unchanged from the published prediction. The AI-off limitation described there remains; this run does not retroactively establish an AI-off activity.

## Part A — Student-supplied prediction

Recorded by the assistant on **2026-11-17 at 21:47:28 UTC (16:47:28 America/Indianapolis)**, before the test. This is the recording time, not an independently verified time of original authorship.

Authorship/context: the student selected the higher target and supplied the expected direction and decision effect in chat. AI clarified the distinction between the fixed risk ceiling and estimated portfolio volatility; the student confirmed that estimated volatility was intended and clarified that the recommendation should remain unchanged. Completion of the assignment's AI-off prediction phase is not independently verified and is not claimed here.

| Required field | Actual record |
|---|---|
| Date/time and time zone before the run | Recorded 2026-11-17 21:47:28 UTC / 16:47:28 America/Indianapolis; original authorship time not separately supplied |
| Configuration key and financial meaning | `target_return`: minimum estimated annual return after modeled trading costs |
| Old value and units | 6.5% annually (`0.065` in the configuration) |
| New value and units | 8.0% annually (`0.08` in the configuration) |
| Expected direction of decision numbers | Estimated portfolio volatility increases and fund allocations change; specific weights and numerical changes were not predicted |
| Expected effect on decision | The recommendation remains PILOT |
| Student's reason for that expectation | The student expects greater estimated volatility to accompany the higher return target. No separate reason for the unchanged PILOT decision was supplied. |

Only the return target changes. The 15% risk ceiling and all other settings remain fixed.

## Immutable prediction evidence

**GitHub commit containing Part A, published before the run:** [ca88b2520a0c83c1908c9853b3756db0dffe3768](https://github.com/hindsja/project2/commit/ca88b2520a0c83c1908c9853b3756db0dffe3768).
**Immutable prediction file:** [locked-changed-input.md at that commit](https://github.com/hindsja/project2/blob/ca88b2520a0c83c1908c9853b3756db0dffe3768/locked-changed-input.md). The initial upload put this file at the repository root; the corrected package places the live record under `docs/`.
**Commit timestamp:** 2026-11-17 21:54:49 UTC (16:54:49 America/Indianapolis).
**Public availability verified before testing:** the public commit/file were downloaded and inspected before the 21:57:57 UTC runs. The downloaded prediction and calculation/configuration files matched the local prepared files byte for byte. See [repository audit](repository-upload-audit.md).

The commit that first freezes Part A is the evidence of ordering. Its link may be added after that commit exists without changing Part A. A local file timestamp or an AI-written prediction is not substituted for the required record.

## Part B — Actual result, after the prediction commit

| Required field | Actual record |
|---|---|
| Before output link | [Before JSON](../outputs/snapshots/lab20-before/results.json), [readable before output](../outputs/snapshots/lab20-before/decision-output.md); run 2026-11-17 21:57:57.019354 UTC |
| After output link | [After JSON](../outputs/snapshots/lab20-after/results.json), [readable after output](../outputs/snapshots/lab20-after/decision-output.md); run 2026-11-17 21:57:57.586671 UTC |
| Changed config and run command | `python app.py --snapshot lab20-before`; then `python app.py --config changed-config.json --snapshot lab20-after`. Only `target_return` changes from `0.065` to `0.08`. |
| Actual before/after decision numbers | Estimated net return 6.5696% → 8.0081%; volatility 4.8995% → 7.8972%; weights and costs below |
| Decision changed or unchanged | Unchanged: PILOT. All constrained-portfolio mandate checks pass in both cases. |
| Why the result matched/differed, or why nothing changed | AI-assisted interpretation below explains the match. Student review/own explanation has not been claimed. |
| Follow-up fix if needed | No model fix was needed for this test. A separate repository upload-layout failure was found by the assistant; the corrected structure is prepared locally and requires publication/recheck. |

### Before/after comparison

| Measure | 6.5% target | 8.0% target |
|---|---:|---:|
| EWY weight | 0% | 0% |
| QQQM weight | 0% | 0% |
| VOO weight | 35% | 55% |
| FNDX weight | 5% | 10% |
| BIL weight | 60% | 35% |
| Estimated annual net return | 6.5696% | 8.0081% |
| Estimated annual volatility | 4.8995% | 7.8972% |
| Risk ceiling (unchanged input) | 15% | 15% |
| One-way turnover from 60% VOO / 40% BIL | 25% | 10% |
| Modeled transition trading cost | 0.0500% of capital | 0.0200% of capital |
| Mandate verdict | PASS | PASS |
| Recommendation | PILOT | PILOT |

### AI-assisted interpretation for student review

The result matches the student's stated directions: stock-fund exposure rises from 40% to 65%, BIL falls from 60% to 35%, and estimated volatility increases by 2.9977 percentage points. The optimizer needs more of the higher-return equity estimates to clear the higher target. Risk remains below the unchanged 15% ceiling and the other constraints still pass, so the research recommendation stays PILOT with 0% live capital.

Turnover falls because BOTH cases measure trades from the same assumed starting portfolio, 60% VOO / 40% BIL. The new allocation is closer to that starting mix. It is not a trade measured from the original optimized 35% VOO / 5% FNDX / 60% BIL allocation.

The 8% case clears its target by only 0.0081 percentage point (about 0.81 basis point). That small buffer reinforces the existing caution; a passing estimate does not establish a dependable 8% future return. The 6.5% mandate remains the base policy; 8% is the locked scenario, not an unrecorded replacement of the approved policy.

## Distinction from other evidence

The repository's stress suite and automated tests were AI-assisted and ran during preparation. They are not this record. The student must select and predict a new test before observing its result. The prepared app supports separately saved configurations and non-overwriting snapshots; operational instructions are in the README and SUBMIT guide.

## Additional pre-run record — 20% volatility ceiling (chat-supplied)

**Status: prediction and reason supplied by the student in chat; mechanically transcribed by Codex before execution.** The assistant supplied neutral blank-field choices and entered the selected configuration. This record does not certify an AI-off prediction phase. No changed-scenario result has been generated by the assistant. The earlier November 17 evidence remains unchanged.

### Part A — prediction before execution

- Transcription timestamp: 2026-11-23T19:27:03.527346-05:00 (America/Indianapolis). This is not a verified time of independent authorship.
- Input: `max_volatility`, the allowed annualized portfolio-volatility ceiling.
- Old value: `0.15` (15% annualized volatility).
- New value: `0.20` (20% annualized volatility).
- Configuration: [final-changed-config.json](../final-changed-config.json). All other settings match the base configuration.
- Actual AI-off authorship circumstances/time: not supplied or verified.

Student prediction, preserved verbatim:

> I predict estimated portfolio volatility will increase, portfolio weights will change if current volatility is reached, stay the same if not, committee decision wil remain pilot

Student financial reason, preserved verbatim:

> the financial reason is that an increase in allowable max volatility will allow allocations to be altered increasing volatility as expected returns increases until it hits its optimal value no longer increasing returns rapidly/increasing volatility too much....

These statements are the student's untested prediction, not a verified description of the optimizer. Their substantive accuracy has not been evaluated here before the frozen experiment.

### Immutable evidence — complete after publication

- Prediction GitHub commit URL: PENDING publication.
- Commit timestamp: PENDING publication.

### Part B — complete after running with AI closed

- Actual commands and run timestamps: PENDING.
- Before output link: PENDING.
- After output link: PENDING.
- Before / after weights: PENDING.
- Before / after estimated net return: PENDING.
- Before / after estimated volatility: PENDING.
- Before / after turnover: PENDING.
- Before / after committee decision: PENDING.
- Student explanation of agreement/difference: PENDING.
- Failure or limitation and follow-up: PENDING.

Expected output paths, not yet claimed to exist: `outputs/snapshots/final-before/` and `outputs/snapshots/final-after/`. Preserve any failed run and use new labels if those folders already exist.

