# Sync Debug Report

## Summary

The `sync_to_do_space.yml` workflow was failing with **zero jobs created** because the YAML file had a fatal parse error. None of the three `aws s3 sync` commands were executing.

---

## Root Causes Identified

### 1. YAML Indentation Error (Critical — Caused Total Failure)

The `run:` key was indented with **7 spaces** instead of **8 spaces**, putting it at a different YAML nesting level than `env:`.

```yaml
# BROKEN — run: at 7 spaces, env: at 8 spaces
      - name: Sync AI Context to DO Space
        env:                          # ← 8 spaces
          AWS_ACCESS_KEY_ID: ...
     
       run: |                         # ← 7 spaces (WRONG)
```

GitHub Actions could not parse the workflow file at all. The error:

```
while parsing a block collection
  in "sync_to_do_space.yml", line 18, column 7
expected <block end>, but found '<block mapping start>'
  in "sync_to_do_space.yml", line 27, column 8
```

**Result:** Both workflow runs (IDs `22534686788` and `22534571927`) show `conclusion: failure` with `total_jobs: 0`. The workflow never ran a single step.

### 2. Wrong Folder Target

The third sync command referenced `./Control_Proof` instead of `./Run_Correlations_Yourself`.

- `Control_Proof/` contains raw correlation CSVs (master data)
- `Run_Correlations_Yourself/` contains the CSVs **plus** the README explaining them and the reproducible analysis script — this is what the AI Agent needs for context

### 3. All Syncs in a Single Step

All three `aws s3 sync` commands were in one `run:` block. If any command failed, the remaining commands would also fail (shell exits on first error). Splitting into separate steps ensures independent execution.

### 4. Missing `--delete` Flag

Without `--delete`, files removed from the repository would persist in the DO Space indefinitely. For a strict one-way mirror (as required by the OPSEC rules), `--delete` ensures the Space is an exact replica of what's in the repo.

### 5. Missing `--exclude` for Runtime Artifacts

The `output/.api_budget.json` file is a runtime artifact (already in `.gitignore`) that should not be synced to the Space, but if it were ever committed accidentally, the old sync would push it.

---

## Fix Applied

```yaml
# Each folder gets its own isolated step with proper indentation
- name: Sync AI Context Index to DO Space
  env:
    AWS_ACCESS_KEY_ID: ${{ secrets.SPACES_ACCESS_KEY }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.SPACES_SECRET_KEY }}
    AWS_DEFAULT_REGION: sfo3
  run: |
    aws s3 sync ./_AI_CONTEXT_INDEX s3://regulated-friction-space/_AI_CONTEXT_INDEX/ \
      --endpoint-url https://sfo3.digitaloceanspaces.com \
      --delete

- name: Sync Output Intel to DO Space
  env: ...
  run: |
    aws s3 sync ./output s3://regulated-friction-space/output/ \
      --endpoint-url https://sfo3.digitaloceanspaces.com \
      --delete \
      --exclude ".api_budget.json"

- name: Sync Correlation Data to DO Space
  env: ...
  run: |
    aws s3 sync ./Run_Correlations_Yourself s3://regulated-friction-space/Run_Correlations_Yourself/ \
      --endpoint-url https://sfo3.digitaloceanspaces.com \
      --delete
```

### What Changed

| Before | After | Why |
|--------|-------|-----|
| `run:` at 7 spaces | `run:` at 8 spaces | Fixes YAML parse error |
| 1 step, 3 commands | 3 separate steps | Failure isolation |
| `./Control_Proof` | `./Run_Correlations_Yourself` | Correct folder with CSVs + README |
| No `--delete` | `--delete` on all | True one-way mirror |
| No `--exclude` | `--exclude ".api_budget.json"` | Prevents leaking runtime artifacts |

---

## Verification

After this fix, re-run the workflow via the **"Run workflow"** button on the Actions tab and confirm that all three folders appear in the DO Space:

```
regulated-friction-space/
├── _AI_CONTEXT_INDEX/
│   ├── 00_START_HERE.md
│   ├── 01_CORE_THEORY.md
│   ├── ... (10 index files)
│   ├── Node_Dossiers/
│   └── sources/
├── output/
│   ├── daily_intelligence.json
│   ├── latest_scrape.json
│   ├── *_extracted.json
│   ├── *_summary.txt
│   └── archive/
└── Run_Correlations_Yourself/
    ├── README.md
    ├── historical_backfill_2017_2024.csv
    ├── negative_windows.csv
    └── run_original_analysis.py
```
