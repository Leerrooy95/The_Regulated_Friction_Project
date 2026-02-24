# DigitalOcean Droplet Setup Guide

This guide explains how to set up automated spider runs and data pushes from your DigitalOcean Droplet to keep the Streamlit Community Cloud dashboard up-to-date.

## Prerequisites

1. Repository cloned on your Droplet
2. Python environment with Scrapy installed
3. Git configured with GitHub credentials (SSH keys or token)
4. Streamlit dashboard deployed on Streamlit Community Cloud

## Step 1: Update the Push Script

Edit `push_spider_data.sh` and update the following variable:

```bash
REPO_DIR="/path/to/The_Regulated_Friction_Project"  # Change this to your actual path
```

For example:
```bash
REPO_DIR="/home/yourusername/The_Regulated_Friction_Project"
```

## Step 2: Test the Scripts Manually

Before setting up cron, test each component:

### Test the spider:
```bash
cd /path/to/The_Regulated_Friction_Project
scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json"
```

**Note**: The `-o` flag appends to the existing JSON file. The `push_spider_data.sh` script automatically merges multiple JSON arrays using `merge_spider_output.py` to maintain a single valid JSON array.

### Test the merge script (optional manual test):
```bash
python3 merge_spider_output.py "federal_register/Spider Output Files/items_federal_register_eo_1.json"
```

### Test the push script:
```bash
./push_spider_data.sh
```

Check the log file for any errors:
```bash
cat /var/log/spider_push.log
```

## Step 3: Set Up Crontab

Open your crontab:
```bash
crontab -e
```

Add the following lines:

```cron
# ============================================================================
# The Regulated Friction Project - Automated Data Pipeline
# ============================================================================

# Set shell and path
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Repository location (update this!)
REPO_DIR=/path/to/The_Regulated_Friction_Project

# Streamlit dashboard URL (update this!)
DASHBOARD_URL=https://your-app-name.streamlit.app

# ── Daily Spider Run at 2 AM UTC ──
# Runs the Federal Register spider and saves output to JSON file
0 2 * * * cd $REPO_DIR && /usr/bin/python3 -m scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json" >> /var/log/spider_run.log 2>&1

# ── Push Data to GitHub at 2:15 AM UTC ──
# Waits 15 minutes after spider completes, then pushes data to GitHub
15 2 * * * $REPO_DIR/push_spider_data.sh

# ── Keep Dashboard Awake (Ping every 6 days at 9 AM UTC) ──
# Prevents Streamlit Community Cloud from sleeping after 7 days
0 9 */6 * * /usr/bin/curl -s -o /dev/null -w "%{http_code}\n" "$DASHBOARD_URL" >> /var/log/dashboard_ping.log 2>&1

# ============================================================================
```

## Step 4: Customize the Schedule

The cron schedule above runs:
- **Spider**: Daily at 2 AM UTC
- **Push**: Daily at 2:15 AM UTC (15 minutes after spider)
- **Dashboard ping**: Every 6 days at 9 AM UTC

### To change the schedule:

**Run spider more frequently (every 6 hours):**
```cron
0 */6 * * * cd $REPO_DIR && /usr/bin/python3 -m scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json" >> /var/log/spider_run.log 2>&1
15 */6 * * * $REPO_DIR/push_spider_data.sh
```

**Run spider at a different time (e.g., 6 AM EST = 11 AM UTC):**
```cron
0 11 * * * cd $REPO_DIR && /usr/bin/python3 -m scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json" >> /var/log/spider_run.log 2>&1
15 11 * * * $REPO_DIR/push_spider_data.sh
```

**Ping dashboard more frequently (every 3 days):**
```cron
0 9 */3 * * /usr/bin/curl -s -o /dev/null -w "%{http_code}\n" "$DASHBOARD_URL" >> /var/log/dashboard_ping.log 2>&1
```

## Step 5: Verify Cron Jobs

Check that your cron jobs are installed:
```bash
crontab -l
```

Monitor the logs to ensure everything is working:
```bash
# Spider execution log
tail -f /var/log/spider_run.log

# Push script log
tail -f /var/log/spider_push.log

# Dashboard ping log
tail -f /var/log/dashboard_ping.log
```

## Step 6: Dashboard Cache Configuration

The dashboard has been updated to refresh data every hour. If you want to change the cache duration:

Edit `dashboard/data_loader.py` and modify the `ttl` parameter:

```python
@st.cache_data(ttl=3600)  # 3600 seconds = 1 hour
```

Common TTL values:
- `ttl=1800` - 30 minutes
- `ttl=3600` - 1 hour (current setting)
- `ttl=7200` - 2 hours
- `ttl=21600` - 6 hours

## Troubleshooting

### Spider not running:
1. Check Python path: `which python3`
2. Verify Scrapy is installed: `python3 -m scrapy version`
3. Check log: `cat /var/log/spider_run.log`

### Push failing:
1. Check Git credentials: `git config --list`
2. Test manual push: `cd $REPO_DIR && git push`
3. Check log: `cat /var/log/spider_push.log`

### Dashboard not updating:
1. Verify files are pushed to GitHub: Check repository commits
2. Force cache clear by restarting Streamlit app from Community Cloud dashboard
3. Wait up to 1 hour for cache to expire (based on TTL setting)

### Dashboard sleeping:
1. Verify ping is running: `grep "dashboard_ping" /var/log/cron.log`
2. Check ping log: `cat /var/log/dashboard_ping.log`
3. Ensure dashboard URL is correct in crontab

## Security Notes

1. **Git Credentials**: Use SSH keys or personal access tokens for authentication
2. **Log Files**: Logs may contain sensitive information - secure with proper permissions
3. **Cron Environment**: Cron runs with limited environment variables - use absolute paths

## Optional: Email Notifications

To receive email notifications on cron job failures, add this to the top of your crontab:

```cron
MAILTO=your-email@example.com
```

Cron will email you if any job produces output to stderr (errors).

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    DigitalOcean Droplet                         │
│                                                                 │
│  ┌─────────────┐      ┌──────────────┐      ┌──────────────┐  │
│  │   Cron      │─────▶│    Scrapy    │─────▶│  Push Script │  │
│  │  Schedule   │      │   Spiders    │      │    (Git)     │  │
│  └─────────────┘      └──────────────┘      └──────┬───────┘  │
│                                                     │           │
└─────────────────────────────────────────────────────┼───────────┘
                                                      │
                                                      ▼
                                              ┌───────────────┐
                                              │    GitHub     │
                                              │  Repository   │
                                              └───────┬───────┘
                                                      │
                                                      ▼
                                              ┌───────────────┐
                                              │   Streamlit   │
                                              │  Community    │
                                              │     Cloud     │
                                              └───────────────┘
```

## Dashboard URL

To find your Streamlit dashboard URL:
1. Go to https://share.streamlit.io/
2. Log in with your account
3. Find your app in the dashboard
4. The URL will be in the format: `https://your-app-name.streamlit.app`
