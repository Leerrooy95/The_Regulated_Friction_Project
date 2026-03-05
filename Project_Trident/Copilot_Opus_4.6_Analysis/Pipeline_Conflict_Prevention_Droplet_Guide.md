# Pipeline Conflict Prevention — DigitalOcean Droplet Guide

**Date:** March 5, 2026  
**Context:** The GitHub Actions daily pipeline (`daily_pipeline.yaml`) was failing with merge conflicts when the Droplet (or another agent) pushed changes to `output/` files on `main` while the pipeline was running.

---

## What Changed in the Pipeline

The "Commit and Push Updates" step was updated to:

1. **Use `git merge --strategy-option=ours` instead of `git pull --rebase`** — this auto-resolves conflicts in `output/` files by keeping the runner's freshly generated data (the latest scrape/intelligence), while still incorporating non-conflicting remote changes.
2. **Retry logic** — if the push is rejected (because the remote moved again during the merge), the pipeline retries up to 5 times with increasing backoff.
3. **Llama Scout resilience** — the Llama Scout extraction step now uses `continue-on-error: true`, so if the GitHub Models API is temporarily unavailable, the spider + Perplexity data still gets committed.

---

## What You Should Do on the Droplet

No mandatory changes are needed — the pipeline will now handle conflicts automatically. However, to minimize unnecessary merge commits and keep the git history clean, consider these optional best practices:

### 1. Avoid Pushing to `output/` From the Droplet During Pipeline Hours

The pipeline runs daily at **8:00 AM UTC**. If the Droplet's cron jobs or scripts push to `output/` files around the same time, conflicts are more likely.

**Recommendation:** Schedule any Droplet pushes to `output/` at least 1–2 hours away from the pipeline window (e.g., before 6:00 AM UTC or after 10:00 AM UTC).

```bash
# Example: if you have a cron job on the Droplet that pushes output
# Move it to 6:00 AM UTC (2 hours before pipeline)
0 6 * * * cd /path/to/repo && git add output/ && git commit -m "Droplet update" && git push origin main
```

### 2. Pull Before Pushing From the Droplet

Always pull the latest `main` before pushing from the Droplet to reduce the chance of stale conflicts:

```bash
cd /path/to/The_Regulated_Friction_Project
git pull origin main
# ... make changes ...
git add .
git commit -m "Droplet update"
git push origin main
```

### 3. Consider Using a Lock File or Branch (Advanced)

If the Droplet and pipeline ever need to write to the same files simultaneously at scale, consider:

- **Branch-based isolation:** Have the Droplet push to a `droplet/updates` branch, and merge it into `main` via a scheduled PR.
- **File-based coordination:** Write a timestamp lock file (e.g., `output/.pipeline_lock`) that the Droplet checks before pushing.

For now, the timing separation (point 1) should be sufficient.

---

## Summary

| Scenario | Before (old pipeline) | After (updated pipeline) |
|---|---|---|
| Droplet pushes to `output/` during pipeline run | ❌ Merge conflict → pipeline fails | ✅ Auto-resolved, runner data wins |
| Llama Scout API is unavailable | ❌ Pipeline fails, nothing committed | ✅ Spider + Perplexity data still committed |
| Push rejected by race condition | ❌ Single attempt, fails | ✅ Retries up to 5 times |

No action required on the Droplet for these fixes to take effect. The pipeline handles everything autonomously now.
