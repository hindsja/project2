# Final technical verification

Run: 2026-11-23T16:52:14.535355+00:00. Actor: Codex (GPT-6). This is automated evidence, not a human AI-off or partner check.

| Check | Observed result |
|---|---|
| Public repository at [20010a6](https://github.com/hindsja/project2/commit/20010a6ecbe0ac1931e631964e01b989f9f9c2ee) | Fresh download has the repaired folders; all 19 original tests pass |
| Public download cold run | PASS: fresh folder, site-packages disabled, server, base result, changed constraint and export |
| Final local tests | **21 passed**; [actual test log](../outputs/final-tests.txt) |
| Final local cold run | PASS; [record](../outputs/automated-cold-run.json) |
| Base finance, stresses, chronological results and approved config | Exactly unchanged from public source results |
| Original November 17 prediction and before/after snapshots | SHA-256 matches preserved public files; not overwritten |
| README and memo openings | AI announcement and education/ownership statement present |
| Visual browser review | NOT COMPLETED: browser host unavailable; native browser URL verification failed and control stopped |
| Final publishing / Brightspace | Not performed; final local package awaits upload |

## Corrections

Mandate checks now read weights in explicit ticker order, so an equivalent dictionary cannot accidentally change which holding is evaluated as BIL. Missing-data requests return an actionable error instead of disconnecting, without exposing local paths. The browser hides old results after a failed recalculation. The memo's allocation range is readable and its displayed policy numbers follow the evaluated configuration. Final documentation distinguishes the repaired public version from the newer local package.

These changes do not improve or change the estimated financial outcome. No claim is made that the short retrospective diagnostic proves future performance or that the AI-off requirement is complete. Videos, transcripts, student review and the final manifest entries remain human completion items.

Reproduce from the project root:

```text
python -m unittest discover -s tests -v
python tools/cold_run.py
python app.py --export
```

The machine-readable [verification record](../outputs/final-verification.json) records the interpreter and file hashes. The historical analysis cutoff remains September 30, 2026; the November 23 date is verification, not new market data.
