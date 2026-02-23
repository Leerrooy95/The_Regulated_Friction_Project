#!/bin/bash
################################################################################
# push_spider_data.sh
################################################################################
# Purpose: Push daily Scrapy spider output from DigitalOcean Droplet to GitHub
#
# This script:
#   1. Stages spider output files
#   2. Commits with timestamp
#   3. Pushes to GitHub repository
#
# Expected to run via cron after spiders complete.
################################################################################

set -e  # Exit on error
set -u  # Exit on undefined variable

# ── Configuration ────────────────────────────────────────────────────────────
REPO_DIR="/path/to/The_Regulated_Friction_Project"  # UPDATE THIS PATH
SPIDER_OUTPUT_DIR="federal_register/Spider Output Files"
OUTPUT_DIR="output"
GIT_BRANCH="main"  # or your default branch

# Log file for debugging
LOG_FILE="/var/log/spider_push.log"

# ── Functions ────────────────────────────────────────────────────────────────
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

error_exit() {
    log "ERROR: $1"
    exit 1
}

# ── Main Script ──────────────────────────────────────────────────────────────
log "Starting spider data push script"

# Change to repository directory
cd "$REPO_DIR" || error_exit "Failed to change to repository directory: $REPO_DIR"
log "Changed to repository directory: $REPO_DIR"

# Ensure we're on the correct branch
git checkout "$GIT_BRANCH" || error_exit "Failed to checkout branch: $GIT_BRANCH"
log "Checked out branch: $GIT_BRANCH"

# Pull latest changes to avoid conflicts
git pull origin "$GIT_BRANCH" || error_exit "Failed to pull latest changes"
log "Pulled latest changes from origin/$GIT_BRANCH"

# Stage spider output files
if [ -d "$SPIDER_OUTPUT_DIR" ]; then
    git add "$SPIDER_OUTPUT_DIR"/*.json 2>/dev/null || true
    log "Staged files from $SPIDER_OUTPUT_DIR"
else
    log "WARNING: Spider output directory not found: $SPIDER_OUTPUT_DIR"
fi

# Stage LLM output files (if they exist)
if [ -d "$OUTPUT_DIR" ]; then
    git add "$OUTPUT_DIR"/*.json 2>/dev/null || true
    git add "$OUTPUT_DIR"/*.txt 2>/dev/null || true
    log "Staged files from $OUTPUT_DIR"
else
    log "WARNING: Output directory not found: $OUTPUT_DIR"
fi

# Check if there are changes to commit
if git diff --cached --quiet; then
    log "No changes to commit. Exiting."
    exit 0
fi

# Commit with timestamp
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')
git commit -m "Auto-update: Spider data push - $TIMESTAMP" || error_exit "Failed to commit changes"
log "Committed changes with timestamp: $TIMESTAMP"

# Push to GitHub
git push origin "$GIT_BRANCH" || error_exit "Failed to push to GitHub"
log "Successfully pushed to GitHub: origin/$GIT_BRANCH"

log "Spider data push completed successfully"
exit 0
