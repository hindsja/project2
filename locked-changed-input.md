# Locked Changed-Input Record

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
