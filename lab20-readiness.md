# Lab 20 — Project 2 Readiness

**Status:** technical package prepared; required human/partner evidence remains unresolved.
**Preparation date:** November 16, 2026, America/Indianapolis. Run logs use UTC timestamps.
AI assistance: Codex (GPT-6) prepared the app, analyses, tests and this evidence structure. No partner interaction or AI-off prediction is represented as completed.

## D — Can a stranger reach the decision, and does it survive a changed input?

The repository contains a Python web app, a one-command README, frozen data, readable decision output, a matching decision memo and validation evidence.
The base decision is **pilot in a 5–10% simulated sleeve, with 0% live allocation**. The base constrained weights are 35% VOO / 5% FNDX / 60% BIL.
Estimated annual net return is 6.57%, volatility 4.90%, and one-way transition turnover 25.00%. These are historical estimates as of September 30, 2026.
Automated stress runs include both feasible cases and rejection cases. They do not replace the student's locked changed-input test.

## R — Readiness manifest

| Item | Location | Actual status |
|---|---|---|
| Python app | [app.py](../app.py), [engine.py](../engine.py), [interface](../static/index.html) | Implemented; HTTP and financial tests run |
| One-command instructions | [README](../README.md) | `python app.py`; frozen data, no dependencies |
| Visible decision output | [decision-output.md](../outputs/decision-output.md), [results.json](../outputs/results.json) | Generated from actual execution |
| Committee memo | [decision-memo.md](decision-memo.md) | Same base numbers, cutoff and conditions as output |
| Mandate and data | [mandate.md](mandate.md), [data-card.md](data-card.md) | Approved hypothetical mandate; disclosed modeling assumptions |
| Validation and AI record | [validation-and-ai-use.md](validation-and-ai-use.md) | Technical checks recorded; student review pending |
| Locked Changed-Input Record | [locked-changed-input.md](locked-changed-input.md) | Student prediction supplied in chat; AI-off status, prior GitHub commit and result pending |
| Videos 1–3 and transcripts | [submission manifest](submission-manifest.md) | Not recorded or linked |
| GitHub publication | [submission guide](../SUBMIT.md) | No repository URL supplied; local preparation only |

## I — Partner's cold-run note

**Not yet performed.** The automated fresh-folder check below is not a substitute.

| Required observation | Partner's actual record |
|---|---|
| Run date/time | Pending partner run |
| Command entered | Pending partner run |
| First failure, or explicit clean result | Pending partner run |
| Elapsed time | Pending partner run |
| Location of result | Pending partner run |
| Control moved and mandate verdict observed | Pending partner run |

The instruction was to send only the repository link and provide no coaching. No claim is made that this happened. The reciprocal run of the partner's repository is also not recorded.

### Separate AI-run technical check

The actual fresh-folder execution is saved in [automated-cold-run.json](../outputs/automated-cold-run.json).
It copies the project into a new temporary folder, disables installed site-packages, starts the Python server, reads the base result, changes a fund cap through the API and exports readable output.
This establishes technical reproducibility in the tested environment; it does not establish that the README is sufficient for an uncoached human.

## V — Predicted changed input, committed before running

Canonical record: [locked-changed-input.md](locked-changed-input.md), also linked from [validation-and-ai-use.md](validation-and-ai-use.md).

**Status:** the student selected a return-target increase from 6.5% to 8.0%, predicting higher estimated volatility, changed fund weights and an unchanged PILOT recommendation. The risk ceiling stays at 15%. The AI-off phase is not verified; the pre-run GitHub commit, before/after test and interpretation remain pending. The 8% test has not been run by the assistant.
No automated stress result is relabeled as that prediction.

## Explain the code — six minutes, AI off

The relevant block is `portfolio_metrics()` followed by `mandate_checks()` and `optimize()` in [engine.py](../engine.py).
**Actual explanation:** not yet recorded.
**Partner's actual question and student's answer:** not yet supplied.
**Any line requiring later help:** not yet identified.

## E — Fix the first failure and rerun

**Status:** awaiting the partner's cold run. There is no basis yet to claim either a partner-discovered fix or a clean partner run.

| Required evidence | Actual record |
|---|---|
| First partner failure, or clean-run statement | Pending |
| Fix and pushed commit, if needed | Pending |
| Partner's rerun outcome | Pending |

## Decision line

**Pilot the process only in a 5–10% simulated sleeve with 0% live capital; reverse to reject if the point-in-time signal is unavailable or no allocation meets the mandate, and consider live adoption only after prospective monitoring meets the stated benchmark, risk and compliance conditions.**

This is AI-assisted analysis for the student's review, not a claim that the student has already defended it orally.

## Reflection

1. **What the partner's cold run revealed:** not yet available because the partner run has not occurred.
2. **What will remain untouched before the deadline:** the student's actual commitment has not been supplied.

## Unresolved items at preparation

GitHub publication; actual partner note and reciprocal cold run; AI-off prediction committed/pushed before the test; before/after evidence and interpretation; AI-off code explanation; partner-driven fix/rerun or clean-run record; personal reflection and final decision ownership. Project 2 videos/transcripts are also outstanding.

The [Lab 20 instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) allow truthful unresolved items. This document reports them and does not guarantee checkout credit or Project 2 readiness.
