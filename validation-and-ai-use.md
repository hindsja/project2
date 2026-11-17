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

The canonical record is [locked-changed-input.md](locked-changed-input.md), submitted with this file. The student supplied the 6.5%-to-8.0% target change and predicted higher estimated volatility, different weights and an unchanged PILOT decision. **The AI-off phase is not verified; the prior GitHub commit, actual result and interpretation remain pending.** The assistant has not run the 8% case.

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
- Visual browser QA could not run: the connected browser/native computer host was unavailable. HTTP behavior and browser JavaScript syntax are checked separately; human visual review remains outstanding.
- No GitHub upload, partner cold run, human AI-off explanation/prediction, YouTube video, transcript or Brightspace submission has occurred in this preparation session.

## Course references

[Project 2](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md),
[AI Boundary Card](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/AI-BOUNDARY-CARD.md),
[student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md),
[Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md).
Project 2 has no Edition A checkpoint; the lab's explicitly AI-off activities still apply. Brightspace controls actual deadlines and final submission fields.

<!-- LOCKED-RECORD-APPENDIX -->

## Appendix — Locked Changed-Input Record

**Status: prediction supplied; pre-run GitHub commit and test pending.** The prediction below records the student's choices and clarification from the conversation. The 8% case has not been run by the assistant.

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

**GitHub commit link containing Part A, pushed before the run:** not yet available.
**Commit timestamp:** not yet available.

The commit that first freezes Part A is the evidence of ordering. Its link may be added after that commit exists without changing Part A. A local file timestamp or an AI-written prediction is not substituted for the required record.

## Part B — Actual result, after the prediction commit

| Required field | Actual record |
|---|---|
| Before output link | Not yet generated for this human test |
| After output link | Not yet generated for this human test |
| Changed config and run command | `changed-config.json` prepared with target `0.08`; `python app.py --config changed-config.json --snapshot lab20-after` has NOT been executed. Run only after the prediction is committed and pushed. |
| Actual before/after decision numbers | Not yet observed for this human test |
| Decision changed or unchanged | Not yet observed |
| Why the result matched/differed, or why nothing changed | Student interpretation pending |
| Follow-up fix if needed | Not yet applicable |

## Distinction from other evidence

The repository's stress suite and automated tests were AI-assisted and ran during preparation. They are not this record. The student must select and predict a new test before observing its result. The prepared app supports separately saved configurations and non-overwriting snapshots; operational instructions are in the README and SUBMIT guide.
