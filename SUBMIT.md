# Submission guide — Lab 20 first, Project 2 afterward

This is an operational guide, separate from the analytical deliverables. The user reports Lab 20 is due tomorrow, November 17, 2026. The exact closing time and Project 2 deadline have not been verified in Brightspace.

## 1. Put the project on GitHub

Recommended: make a dedicated Project 2 repository and upload the **contents of `project2/`**, keeping all subfolders intact. Its root should show `README.md`, `app.py`, `engine.py`, `reporting.py`, `config.json`, `requirements.txt`, `data/`, `static/`, `docs/`, `tests/`, `tools/`, and `outputs/`.

Do not upload only the ZIP: GitHub must show the individual Markdown/code/output files. Do not upload `__pycache__`, an environment, credentials or `.env`. No credentials are required by this app.

If using your existing course repository instead, upload the entire `project2` folder and direct your partner to its README. The run command is entered from that folder.

The archive `Project2-Lab20-package.zip` contains this prepared project for easy transfer. Extract it before uploading files. Nothing has been published to GitHub by the assistant; no repository URL was supplied.

## 2. Complete the Lab 20 activities

1. Give your partner **only the GitHub repository link**. They download/extract into their own folder and follow the README without coaching.
2. Have them write the real command, first failure or clean result, elapsed time and result location in `docs/lab20-readiness.md`. Swap and test their repository too.
3. **Close AI.** Choose a load-bearing input and new value whose result you have not already seen. Write your own prediction in `docs/locked-changed-input.md`, including old/new values and units, expected numerical direction and expected decision effect.
4. Commit and push the prediction **before running the change**. Copy the URL of that commit into the record afterward; do not rewrite the frozen prediction.
5. From the project folder, save the unchanged result with `python app.py --snapshot lab20-before`. Copy `config.json` to `changed-config.json`, edit only your selected input, then run `python app.py --config changed-config.json --snapshot lab20-after`. These snapshots refuse overwrites.
6. Under the prediction, record what actually happened, whether the decision changed, and why. Run `python tools/sync_record.py` to copy that actual record into the validation attachment. Push the config, both snapshot folders and updated documents. The snapshot JSON contains the exact settings and timestamp.
7. With AI closed, explain `portfolio_metrics()`, `mandate_checks()` and the relevant part of `optimize()` in `engine.py` to your partner. Answer their actual question; swap roles.
8. Fix the first failure your partner encountered, push it and have them rerun. If their first run was clean, explicitly record that no fix was needed. The AI's clean run cannot be substituted.
9. Review the decision line and write your own reflection: what the cold run revealed, and what you will not touch before the deadline.

If a step remains unresolved, record the actual issue truthfully. The lab permits unresolved items; it does not permit invented partner notes or backdated predictions.

## 3. What to submit for LAB 20

In the **Lab 20 checkout/submission field in Brightspace**, paste the actual **GitHub file links** below. The assignment requests links, not a new PDF or a local Windows path.

| Priority | File/link | Why |
|---|---|---|
| Main Lab 20 record | `docs/lab20-readiness.md` | Partner note, fix/clean-run evidence, decision line, reflection and unresolved items |
| Changed-input record | `docs/locked-changed-input.md` plus its pre-run commit link | Human prediction frozen before the test and actual result |
| App entry | `app.py` | Runnable Python web app |
| Financial logic | `engine.py` | Code producing the decision numbers |
| Run instructions | `README.md` | Stranger's one-command starting point |
| Visible result | `outputs/decision-output.md` | Numbers readable directly on GitHub |
| Before/after outputs | `outputs/snapshots/lab20-before/results.json` and `outputs/snapshots/lab20-after/results.json` | Evidence from your actual changed-input test |

The repository must also contain `reporting.py`, `static/`, `config.json` and `data/` so it runs. They do not each need a separately pasted checkout link unless the instructor requests it. Add a fix-commit link if a partner-discovered failure needed repair.

Open each submitted link and check that the instructor can access it. Submit individually. If the exact Brightspace field differs, follow its assignment header/instructions. The complete Project 2 videos are a readiness item, not listed among Lab 20's four floor items; record their unfinished status honestly.

## 4. What to submit for PROJECT 2 later

| Destination | Submission |
|---|---|
| GitHub repository | Complete runnable project, frozen data, readable results, tests and all final documentation |
| Project 2 Brightspace submission | Repository URL and completed manifest with GitHub file links |
| Brightspace file attachments | `docs/decision-memo.md` and `docs/validation-and-ai-use.md`; include `docs/locked-changed-input.md` so the linked record is available with the attachments |
| YouTube | Video 1 ≤3 minutes; Video 2 ≤5 minutes; Video 3 ≤5 minutes, opening with the app running live |
| Manifest/repository | Working YouTube links, titles/durations, timestamp indices, access confirmation and actual corrected transcripts |

Use `docs/submission-manifest.md` to assemble the final links. Use `VIDEO-GUIDE.md` for recording preparation. Do not submit fabricated transcripts or label the recording outline as a transcript. Edition A/B are not submitted for Project 2.

## Current completion status

The technical project, executed output and analysis are prepared locally. Automated tests and a fresh-folder run are recorded. The browser automation host was unavailable, so open the page yourself to check its appearance.

Still required: GitHub publication; the real partner run/fix record; your AI-off prediction and prior commit; your changed-input interpretation/code explanation/reflection; final review and ownership of the recommendation; videos/transcripts for Project 2; and the actual Brightspace submissions.

## Useful commands

```text
python app.py
python app.py --export
python -m unittest discover -s tests -v
```

The first opens the app server at http://127.0.0.1:8766. The second regenerates base output and memo; do not use it to overwrite a frozen changed-input record. The third runs the financial/timing/server tests.
