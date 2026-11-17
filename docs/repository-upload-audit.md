# Repository upload audit — November 17, 2026

Repository: [hindsja/project2](https://github.com/hindsja/project2).
Inspected immutable upload: [ca88b2520a0c83c1908c9853b3756db0dffe3768](https://github.com/hindsja/project2/commit/ca88b2520a0c83c1908c9853b3756db0dffe3768).
Actor: assistant inspection and execution; this is **not** the required partner cold run.

## Finding

All **33 prepared files' contents** were present and matched the local prepared files byte for byte at inspection. No prepared data or code content was missing. However, **22 files were uploaded at the root instead of their six subfolders**, and `.gitignore` was uploaded as `download`.

The app therefore could not run from the uploaded structure. A downloaded copy executed with `python app.py --export` exited with code 1 because `data/prices.csv` did not exist. The interface at `static/index.html`, documentation links and test/tool paths were also misplaced.

| Required folder | Files that must be inside it |
|---|---|
| `data/` | `bil_source.json`, `lab15_prices_original.csv`, `prices.csv`, `provenance.json`, `unrate_vintages.csv` |
| `docs/` | `data-card.md`, `decision-memo.md`, `lab20-readiness.md`, `locked-changed-input.md`, `mandate.md`, `submission-manifest.md`, `validation-and-ai-use.md`; plus this new audit |
| `outputs/` | `automated-cold-run.json`, `decision-output.md`, `results.json`, `test-results.txt`, `verification.json`; plus new audit/test evidence and `snapshots/` |
| `static/` | `index.html` |
| `tests/` | `test_engine.py` |
| `tools/` | `cold_run.py`, `prepare_data.py`, `sync_record.py` |

Keep `app.py`, `engine.py`, `reporting.py`, both configuration JSON files, `requirements.txt`, README and guides at the repository root. Rename the file `download` to `.gitignore` or upload the correctly named local version; this file is useful but is not the cause of the runtime failure.

## Verified repair

The assistant reconstructed the correct directories from the **downloaded committed files**, without changing the calculation code. In that corrected copy:

- `python app.py --export` exited successfully.
- All 19 financial, date-filtering, snapshot and HTTP tests passed.
- The prediction's Part A was checked against the frozen GitHub file and remains unchanged.
- The actual before/after configurations differ only in `target_return`.

Evidence: [structured audit](../outputs/repository-upload-audit.json), [tests on the restored uploaded source](../outputs/repository-restoration-tests.txt), and [locked comparison](locked-changed-input.md).

**Publication status:** corrected paths and new results are prepared locally; no corrected upload or partner rerun has yet been verified. This audit does not claim that the public repository is repaired.

## Prediction and ordering

The original [root-level prediction](https://github.com/hindsja/project2/blob/ca88b2520a0c83c1908c9853b3756db0dffe3768/locked-changed-input.md) is preserved by commit `ca88b25`, timestamped **21:54:49 UTC**. Public availability was confirmed before the assistant's baseline and 8% runs at **21:57:57 UTC**, November 17, 2026.

The file's location mistake does not erase this prediction evidence. The record continues to disclose that it was supplied/clarified in AI chat, rather than claiming an independently verified AI-off phase.

## Still absent as course evidence

The actual partner note, code explanation/question, personal reflection and final review were not supplied. Three Project 2 recordings and actual transcripts do not exist in the prepared/uploaded package. These are unfinished activities, not accidentally omitted technical files.
