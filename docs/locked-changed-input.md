# Locked Changed-Input Record

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

### Immutable prediction evidence — verified after execution

- Prediction commit: [d4b657f9f6be3dc352fcf2cbb08c73c5eab3ed84](https://github.com/hindsja/project2/commit/d4b657f9f6be3dc352fcf2cbb08c73c5eab3ed84).
- Immutable prediction file: [record at the pre-run commit](https://github.com/hindsja/project2/blob/d4b657f9f6be3dc352fcf2cbb08c73c5eab3ed84/docs/locked-changed-input.md).
- Immutable configuration: [final-changed-config.json at that commit](https://github.com/hindsja/project2/blob/d4b657f9f6be3dc352fcf2cbb08c73c5eab3ed84/final-changed-config.json).
- GitHub committer timestamp: November 23, 2026, 8:36:50 PM EST / November 24, 2026, 01:36:50 UTC.
- Verification scope: after execution, the assistant downloaded the immutable record and configuration. The prediction matched the local pre-run record and the published configuration matched the saved changed-run configuration. The commit timestamp precedes both saved run timestamps. This is retrospective chronology verification, not an independent observation of the student's AI-off activity or of the file's availability before execution.

### Part B — actual result and post-run explanation

The student reported personally running both commands. The assistant read the saved files afterward and did not execute this changed-input experiment. The original prediction was supplied in chat, and the post-run interpretation below includes AI assistance; neither is represented as verified AI-off work.

| Evidence | Recorded value |
|---|---|
| Before command | `python app.py --snapshot final-before` (the instructions used the existing `.venv-lab15` Python executable) |
| After command | `python app.py --config final-changed-config.json --snapshot final-after` |
| Before run | 2026-11-24T01:39:23.571687+00:00 / November 23, 2026, 8:39:23 PM EST |
| After run | 2026-11-24T01:39:33.942975+00:00 / November 23, 2026, 8:39:33 PM EST |
| Before evidence | [JSON](../outputs/snapshots/final-before/results.json), [readable output](../outputs/snapshots/final-before/decision-output.md) |
| After evidence | [JSON](../outputs/snapshots/final-after/results.json), [readable output](../outputs/snapshots/final-after/decision-output.md) |
| Configuration comparison | Only `max_volatility` changes, from 0.15 to 0.20 |

| Measure | Before: 15% ceiling | After: 20% ceiling |
|---|---:|---:|
| EWY / QQQM / VOO / FNDX / BIL weights | 0% / 0% / 35% / 5% / 60% | 0% / 0% / 35% / 5% / 60% |
| Estimated annual net return | 6.5696% | 6.5696% |
| Estimated annualized volatility | 4.8995% | 4.8995% |
| One-way turnover | 25.00% | 25.00% |
| Transition trading cost | 0.0500% | 0.0500% |
| Mandate verdict | PASS | PASS |
| Committee decision | PILOT | PILOT |

#### Student's post-run response, preserved verbatim

> my prediction was right because the estimated volatility was not at its maximum allowable so it had no need to change because it was already optimized. based on the results my recomendation is still pilot/the same as the initial..

This response followed the assistant's explanation that the optimizer minimizes volatility subject to the return target and other constraints. It is not described as an unaided diagnosis.

#### Edited interpretation — AI-assisted, with the original prediction preserved

The prediction was **partly supported**. The PILOT recommendation remained unchanged, and the conditional prediction that weights would stay the same when the original volatility ceiling was not reached matched the result. The explicit prediction that estimated volatility would increase did **not** occur: it remained 4.8995%.

The original 15% ceiling was not binding because the selected portfolio's estimated volatility was already about 4.90%. The optimizer minimizes estimated volatility while meeting the 6.5% estimated net-return target and the other mandate constraints. It does not maximize return by using the entire risk allowance. Raising only the ceiling to 20% did not make the existing minimum-volatility feasible allocation less desirable. Any portfolios newly admitted by a higher volatility ceiling would have higher volatility than the selected portfolio. Thus weights, estimated return, turnover and the decision stayed unchanged.

The student's final recommendation remains **PILOT**, as initially proposed: a 5–10% simulated sleeve and 0% live allocation, with the existing monitoring and stop rules. No model correction was needed for this result. The misconception in the initial rationale concerned the optimization objective, not a demonstrated software failure.

**Limitation:** this experiment confirms behavior when a nonbinding upper risk limit is relaxed; it does not establish robustness when a binding constraint changes or validate expected returns. Other stresses remain separate evidence. The pre-run prediction's chat involvement and the post-run AI assistance remain disclosed; a successful commit/run sequence alone does not certify the required AI-off prediction phase.
