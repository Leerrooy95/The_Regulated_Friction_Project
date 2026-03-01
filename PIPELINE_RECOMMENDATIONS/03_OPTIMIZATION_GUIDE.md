# Optimization Guide

## 1. Sync Reliability

### Current Improvement: Isolated Steps

Each folder now syncs in its own step. If one fails (e.g., a transient network error), the others still succeed, and GitHub Actions clearly shows which step failed.

### Future Improvement: Retry Logic

For resilience against transient S3/Spaces API errors, add retry logic:

```yaml
- name: Sync AI Context Index to DO Space
  env: ...
  run: |
    for i in 1 2 3; do
      aws s3 sync ./_AI_CONTEXT_INDEX s3://regulated-friction-space/_AI_CONTEXT_INDEX/ \
        --endpoint-url https://sfo3.digitaloceanspaces.com \
        --delete && break
      echo "Attempt $i failed, retrying in 10s..."
      sleep 10
    done
```

---

## 2. Data Freshness for the AI Agent

The Mistral Nemo Agent reads from the DO Space but has no way to know when data was last updated. Consider adding a manifest file:

```yaml
- name: Generate sync manifest
  run: |
    echo '{
      "synced_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
      "folders": ["_AI_CONTEXT_INDEX", "output", "Run_Correlations_Yourself"],
      "pipeline_run": "${{ github.run_id }}",
      "commit": "${{ github.sha }}"
    }' > /tmp/sync_manifest.json

- name: Upload manifest
  env: ...
  run: |
    aws s3 cp /tmp/sync_manifest.json s3://regulated-friction-space/sync_manifest.json \
      --endpoint-url https://sfo3.digitaloceanspaces.com
```

The Agent's Knowledge Base can then reference `sync_manifest.json` to tell users how fresh the data is.

---

## 3. Workflow Trigger Refinement

The current trigger watches the "Daily Intelligence Pipeline" workflow:

```yaml
on:
  workflow_run:
    workflows: ["Daily Intelligence Pipeline"]
    types: [completed]
```

This correctly chains the sync after the daily pipeline. The `if:` condition also correctly checks for `success` before running. No changes needed here.

**Note:** If you rename the `daily_pipeline.yaml` workflow's `name:` field, this trigger will silently stop matching. Keep the names in sync.

---

## 4. Consider Syncing `Control_Proof/` Too

The current sync sends `Run_Correlations_Yourself/` which contains the analysis README and key CSVs. However, the analysis script (`run_original_analysis.py`) references data from `Control_Proof/`:

```python
# From Run_Correlations_Yourself/run_original_analysis.py
# References: Control_Proof/master_reflexive_correlation_data.csv
```

If you want the Agent to have complete context for understanding the correlations, consider adding a fourth sync step:

```yaml
- name: Sync Control Proof Data to DO Space
  env: ...
  run: |
    aws s3 sync ./Control_Proof s3://regulated-friction-space/Control_Proof/ \
      --endpoint-url https://sfo3.digitaloceanspaces.com \
      --delete
```

---

## 5. Dashboard Streamlit Config

The `dashboard/.streamlit/config.toml` has `enableXsrfProtection = true` which is correct. One note:

- If `enableCORS = false` is also set, Streamlit may override it when XSRF protection is enabled. If you see CORS warnings in the Streamlit logs, remove the `enableCORS` line entirely and let Streamlit manage it automatically.

---

## 6. Git Workflow Hygiene

The daily pipeline uses `git pull --rebase` before pushing, which is good practice for avoiding merge conflicts. However:

- If two pipelines run simultaneously (unlikely but possible with manual dispatch), the rebase could fail
- Consider adding a concurrency group to prevent overlapping runs:

```yaml
# In daily_pipeline.yaml
concurrency:
  group: daily-pipeline
  cancel-in-progress: false
```

---

## 7. Output Archive Growth

The `output/archive/` folder grows daily with `_extracted.json`, `_summary.txt`, and `_raw.txt` files. Over months, this could become large. Consider:

1. **Periodic cleanup**: Add a step to the daily pipeline that removes archive files older than 30 days
2. **Exclude archive from sync**: If the Agent only needs current intel, add `--exclude "archive/*"` to the output sync command

---

## Quick Reference: Verified Commands

| Action | Command |
|--------|---------|
| Validate workflow YAML | `python -c "import yaml; yaml.safe_load(open('.github/workflows/sync_to_do_space.yml'))"` |
| Validate dashboard syntax | `python -m py_compile dashboard/app.py && python -m py_compile dashboard/data_loader.py && python -m py_compile dashboard/constants.py` |
| Test correlation data exists | `test -f Run_Correlations_Yourself/historical_backfill_2017_2024.csv && test -f Run_Correlations_Yourself/negative_windows.csv` |
| Manual sync trigger | GitHub → Actions → "Sync AI Context to Drop Box" → "Run workflow" |
