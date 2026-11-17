# Fix the GitHub upload and add the Lab 20 results

Your first upload preserved all prepared file contents, but flattened the folders. The app needs the correct structure.

1. Extract **`Lab20-GitHub-repair.zip`**. This archive's top level is the repository top level; it has no outer `project2` wrapper.
2. Open [the repository upload page](https://github.com/hindsja/project2/upload/main).
3. From the extracted folder, drag the **six whole folders** `data`, `docs`, `outputs`, `static`, `tests`, and `tools` into GitHub's upload area. Drag the root-level files too so the updated README and guides replace the older versions. Do not select all nested files individually; that caused the flattened structure.
4. Check that the upload list includes paths such as **`data/prices.csv`**, **`static/index.html`**, **`docs/locked-changed-input.md`**, and **`outputs/snapshots/lab20-after/results.json`**.
5. Commit with a message such as `Restore project folders and add locked 8-percent test results`.
6. Open the repository root. It should show those six folders. Download/extract a fresh ZIP and follow the README, or have your partner perform the required cold run from it.

The existing root-level `download` file is the `.gitignore` content under the wrong name. Upload `.gitignore` with its correct name. It may be hidden by your file browser; the app does not depend on it to run.

The older misplaced files at the root can be removed after the correct copies are present and checked, to avoid confusing duplicate records. Do not delete the repository or reset its history: the original prediction commit must remain accessible.

## Lab 20 links after the repair is published

- [Main Lab 20 record](https://github.com/hindsja/project2/blob/main/docs/lab20-readiness.md)
- [Prediction and actual comparison](https://github.com/hindsja/project2/blob/main/docs/locked-changed-input.md)
- [Original pre-run prediction commit](https://github.com/hindsja/project2/commit/ca88b2520a0c83c1908c9853b3756db0dffe3768)
- [Before output](https://github.com/hindsja/project2/blob/main/outputs/snapshots/lab20-before/results.json)
- [After output](https://github.com/hindsja/project2/blob/main/outputs/snapshots/lab20-after/results.json)
- [App](https://github.com/hindsja/project2/blob/main/app.py) and [financial code](https://github.com/hindsja/project2/blob/main/engine.py)
- [README](https://github.com/hindsja/project2/blob/main/README.md)

The new-path links above are intended destinations and will not work until the repair is committed. Open them before submitting.

The before/after test is complete and the prediction matched. Partner activities, personal review/reflection and the disclosed AI-off limitation remain. Use the truthful status in the lab record; the technical repair alone does not complete those activities.
