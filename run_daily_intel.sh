#!/bin/bash
################################################################################
# run_daily_intel.sh
################################################################################
# Eliminates the race condition between the GitHub Actions daily pipeline
# (8:00 AM UTC) and the DigitalOcean Droplet's Gradient agent.
#
# Instead of blindly running at a fixed time (the old 8:30 AM cron), this
# script polls the GitHub REST API until today's Daily Intelligence Pipeline
# workflow reports status=completed + conclusion=success, then pulls the
# fresh data and launches the agent.
#
# ── Data Flow ──
#   1. 8:00 AM UTC  – GitHub Action fires (spider + Perplexity + Llama Scout)
#   2. 8:05 AM UTC  – This script starts via cron, begins polling
#   3. ~8:10-8:25   – Pipeline finishes; script detects success via API
#   4. Script runs `git pull` → `python3 main.py`
#
# ── Required Environment ──
#   GITHUB_TOKEN  – A GitHub PAT (classic or fine-grained) with actions:read
#                   scope. For a private repo, the token also needs repo scope.
#                   Set it in the Droplet's environment or /etc/environment.
#
# ── Crontab Entry ──
#   5 8 * * *  GITHUB_TOKEN="ghp_XXXX" /path/to/run_daily_intel.sh >> /var/log/daily_intel.log 2>&1
#
# ── Dependencies ──
#   curl, jq, git, python3 (all standard on Ubuntu Droplets; install jq with
#   `apt-get install -y jq` if missing)
################################################################################

set -euo pipefail

# ── Configuration ────────────────────────────────────────────────────────────
GITHUB_OWNER="Leerrooy95"
GITHUB_REPO="The_Regulated_Friction_Project"
WORKFLOW_FILE="daily_pipeline.yaml"
GIT_BRANCH="main"

# Droplet paths — update REPO_DIR to match your clone location
REPO_DIR="${REPO_DIR:-/root/The_Regulated_Friction_Project}"

# Polling tuning
POLL_INTERVAL=60   # seconds between API checks (≈60 req over 60 min — well within 5,000/hr PAT limit)
MAX_WAIT=5400      # 90-minute hard ceiling (seconds)

# Derived
TODAY=$(date -u +"%Y-%m-%d")
API_BASE="https://api.github.com"
# Endpoint: list workflow runs for a specific workflow, filtered to today's
# successful runs on the main branch.  The `status` parameter accepts both
# run statuses (completed, in_progress …) and conclusions (success, failure …).
# Docs: https://docs.github.com/en/rest/actions/workflow-runs#list-workflow-runs-for-a-workflow
API_URL="${API_BASE}/repos/${GITHUB_OWNER}/${GITHUB_REPO}/actions/workflows/${WORKFLOW_FILE}/runs"

# ── Helpers ──────────────────────────────────────────────────────────────────
log() {
    echo "[$(date -u +'%Y-%m-%d %H:%M:%S UTC')] $*"
}

error_exit() {
    log "❌ ERROR: $1"
    exit 1
}

check_dependencies() {
    for cmd in curl jq git python3; do
        if ! command -v "$cmd" >/dev/null 2>&1; then
            error_exit "Required command not found: $cmd (install with: apt-get install -y $cmd)"
        fi
    done

    if [ -z "${GITHUB_TOKEN:-}" ]; then
        error_exit "GITHUB_TOKEN is not set. Create a PAT with 'actions:read' scope and export it."
    fi
}

# ── API Poller ───────────────────────────────────────────────────────────────
# Returns 0 when today's pipeline is done + successful; 1 otherwise.
check_pipeline_status() {
    local response http_code body

    # curl -s  = silent, -w = append HTTP code on a new line
    response=$(curl -s -w "\n%{http_code}" \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "${API_URL}?branch=${GIT_BRANCH}&status=success&per_page=1&created=%3E%3D${TODAY}")

    # Split body from HTTP code (last line)
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | sed '$d')

    # ── Handle rate-limiting / errors ──
    if [ "$http_code" -eq 403 ] || [ "$http_code" -eq 429 ]; then
        log "⚠️  Rate-limited (HTTP ${http_code}). Will back off and retry."
        return 1
    fi

    if [ "$http_code" -ne 200 ]; then
        log "⚠️  GitHub API returned HTTP ${http_code}"
        return 1
    fi

    # ── Parse response ──
    local total_count
    total_count=$(echo "$body" | jq -r '.total_count // 0')

    if [ "$total_count" -gt 0 ]; then
        local conclusion run_id created_at
        conclusion=$(echo "$body" | jq -r '.workflow_runs[0].conclusion // "null"')
        run_id=$(echo "$body"     | jq -r '.workflow_runs[0].id // "unknown"')
        created_at=$(echo "$body" | jq -r '.workflow_runs[0].created_at // "unknown"')

        if [ "$conclusion" = "success" ]; then
            log "✅ Pipeline run #${run_id} succeeded (created ${created_at})"
            return 0
        else
            log "⚠️  Latest run #${run_id} has conclusion='${conclusion}' — still waiting."
        fi
    fi

    return 1
}

# ── Main ─────────────────────────────────────────────────────────────────────
log "═══════════════════════════════════════════════════════════════"
log "🚀 Daily Intel Sync — Starting"
log "   Watching : ${GITHUB_OWNER}/${GITHUB_REPO} → ${WORKFLOW_FILE}"
log "   Date     : ${TODAY}"
log "   Max wait : ${MAX_WAIT}s ($((MAX_WAIT / 60)) min)"
log "   Repo dir : ${REPO_DIR}"
log "═══════════════════════════════════════════════════════════════"

check_dependencies

elapsed=0

while [ "$elapsed" -lt "$MAX_WAIT" ]; do
    log "⏳ Polling GitHub Actions API… (${elapsed}s / ${MAX_WAIT}s elapsed)"

    if check_pipeline_status; then
        log "🎯 Pipeline confirmed successful. Pulling latest data…"

        cd "$REPO_DIR" || error_exit "Cannot cd to ${REPO_DIR}"
        git checkout "$GIT_BRANCH"   || error_exit "git checkout ${GIT_BRANCH} failed"
        git pull origin "$GIT_BRANCH" || error_exit "git pull failed"

        log "📂 Repo updated. Running Gradient agent (main.py)…"
        python3 main.py

        log "✅ Daily intel run complete."
        exit 0
    fi

    log "💤 Not ready yet — sleeping ${POLL_INTERVAL}s…"
    sleep "$POLL_INTERVAL"
    elapsed=$((elapsed + POLL_INTERVAL))
done

error_exit "⏰ Timed out after ${MAX_WAIT}s ($((MAX_WAIT / 60)) min). The Daily Intelligence Pipeline did not report success for ${TODAY}. Check https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}/actions"
