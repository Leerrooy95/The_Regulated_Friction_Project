# OPSEC Security Audit

## Architecture Review

The dead-drop pipeline follows a sound security model:

```
GitHub Actions → (one-way push) → DO Space → (read-only) → Mistral Nemo Agent
                                                              ↓
                                              Streamlit Dashboard (isolated Droplet)
```

### What's Working Well

| Area | Status | Notes |
|------|--------|-------|
| Credential management | ✅ Secure | All secrets in GitHub Actions Secrets, no hardcoded keys |
| One-way data flow | ✅ Enforced | `aws s3 sync` push-only, no pull commands |
| Agent isolation | ✅ Good | Agent has no GitHub PAT, reads only from Space |
| Droplet isolation | ✅ Good | Streamlit Droplet has no connection to Agent backend |
| `.gitignore` coverage | ✅ Good | `.env`, `.api_budget.json`, `Research_Documents/` excluded |
| XSRF protection | ✅ Enabled | `enableXsrfProtection = true` in Streamlit config |

---

## Recommendations

### Priority 1: DO Space Bucket Policy (Action Required)

Verify that the DigitalOcean Space has proper ACL restrictions:

```
1. The Spaces Access Key used by GitHub Actions should have WRITE-ONLY scope
   (or read+write if you need sync --delete to check existing objects)
2. The Mistral Nemo Agent's access should be READ-ONLY
3. No public access should be enabled on the bucket
```

**How to verify:**
- In the DigitalOcean console → Spaces → `regulated-friction-space` → Settings
- Ensure "File Listing" is **disabled** (prevents directory enumeration by unauthorized parties)
- Ensure CDN is **disabled** unless you explicitly need it (CDN makes objects publicly cacheable)

### Priority 2: Scope GitHub Actions Permissions

Add explicit permissions to the sync workflow to follow the principle of least privilege:

```yaml
jobs:
  sync-to-space:
    runs-on: ubuntu-latest
    permissions:
      contents: read  # Only needs to read repo files, never write
```

This is already effectively the case (the workflow doesn't use `GITHUB_TOKEN` for writes), but making it explicit prevents future mistakes.

### Priority 3: Pin the Checkout Action

The workflow uses `actions/checkout@v4`, which auto-updates to the latest v4.x. For supply-chain security, consider pinning to a specific SHA:

```yaml
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1
```

This prevents a compromised `actions/checkout` release from injecting code into your pipeline. However, this trades security for convenience (you must manually update the SHA for patches).

### Priority 4: Rotate Spaces Keys Periodically

DigitalOcean Spaces keys don't expire. Set a calendar reminder to rotate them every 90 days:

1. Generate a new key in DO console
2. Update `SPACES_ACCESS_KEY` and `SPACES_SECRET_KEY` in GitHub Actions Secrets
3. Delete the old key in DO console

### Priority 5: Verify No Sensitive Data in Synced Folders

The three synced folders should contain only OSINT data intended for the AI Agent. Periodically audit:

- `_AI_CONTEXT_INDEX/` — Public analysis and dossiers. ✅ Safe to sync.
- `output/` — LLM-generated intelligence summaries, spider scrapes. ✅ Safe to sync, but `--exclude ".api_budget.json"` is applied.
- `Run_Correlations_Yourself/` — Reproducible analysis scripts and CSVs. ✅ Safe to sync.

**Note:** If you ever add files to these folders that contain personal notes, API logs, or research drafts, add `--exclude` patterns to the sync commands.

### Priority 6: Monitor for Stale Data

The `--delete` flag removes files from the Space that no longer exist in the repo. This is correct for a one-way mirror. However, be aware:

- If the daily pipeline fails to run, the Space will still have the last successful sync
- Consider adding a "last sync timestamp" file so the Agent knows data freshness:

```yaml
- name: Write sync timestamp
  run: echo "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > /tmp/last_sync.txt

- name: Upload sync timestamp
  env: ...
  run: |
    aws s3 cp /tmp/last_sync.txt s3://regulated-friction-space/last_sync.txt \
      --endpoint-url https://sfo3.digitaloceanspaces.com
```

---

## Security Grade: A-

The architecture is well-designed with proper separation of concerns. The main gap was the broken YAML (now fixed). The recommendations above are incremental hardening steps, not critical vulnerabilities.
