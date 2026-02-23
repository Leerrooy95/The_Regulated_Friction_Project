# Data Pipeline Fix - Quick Start Guide

## Problem Summary

Your data pipeline had a **disconnect** between:
1. **DigitalOcean Droplet** (runs Scrapy spiders daily)
2. **GitHub Repository** (storage)
3. **Streamlit Community Cloud** (dashboard)

### Root Causes Identified:
1. ❌ Spiders ran on Droplet but never pushed data to GitHub
2. ❌ Dashboard had **infinite caching** (`@st.cache_data` with no TTL)
3. ❌ Streamlit Community Cloud sleeps after 7 days of inactivity

---

## ✅ Solutions Implemented

### 1. Fixed Dashboard Caching Issue

**File Modified:** `dashboard/data_loader.py`

**Changes:**
- Added `ttl=3600` (1-hour cache) to all four data loaders:
  - `load_core_dataset()`
  - `load_backfill()`
  - `load_negative_windows()`
  - `load_eo_spider()`

**Result:** Dashboard will refresh data from GitHub every hour instead of caching indefinitely.

### 2. Created Droplet Push Script

**File Created:** `push_spider_data.sh`

**Features:**
- Automatically commits spider output files
- Pushes to GitHub with timestamps
- Handles errors gracefully
- Logs all operations to `/var/log/spider_push.log`

### 3. Created Automated Schedule

**File Created:** `crontab_template.txt`

**Schedule:**
- **2:00 AM UTC**: Run Federal Register spider
- **2:15 AM UTC**: Push data to GitHub (15 min after spider completes)
- **9:00 AM UTC every 6 days**: Ping dashboard to keep it awake

---

## 🚀 Quick Setup (5 Steps)

### Step 1: Update Push Script Path
Edit `push_spider_data.sh` line 19:
```bash
REPO_DIR="/home/yourusername/The_Regulated_Friction_Project"  # Change this!
```

### Step 2: Configure Git Authentication
Ensure your Droplet can push to GitHub:
```bash
# Option A: SSH key (recommended)
ssh-keygen -t ed25519 -C "your_email@example.com"
# Add ~/.ssh/id_ed25519.pub to GitHub: Settings > SSH Keys

# Option B: Personal access token
git config --global credential.helper store
# Next git push will prompt for token
```

### Step 3: Test Components
```bash
# Test spider
cd /your/repo/path
scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json"

# Test push script
./push_spider_data.sh

# Check logs
cat /var/log/spider_push.log
```

### Step 4: Install Crontab
```bash
# Edit crontab
crontab -e

# Add these lines (update REPO_DIR and DASHBOARD_URL first):
REPO_DIR=/your/repo/path
DASHBOARD_URL=https://your-app.streamlit.app

0 2 * * * cd $REPO_DIR && /usr/bin/python3 -m scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json" >> /var/log/spider_run.log 2>&1
15 2 * * * $REPO_DIR/push_spider_data.sh
0 9 */6 * * /usr/bin/curl -s -o /dev/null -w "%{http_code}\n" "$DASHBOARD_URL" >> /var/log/dashboard_ping.log 2>&1
```

### Step 5: Monitor
```bash
# Watch logs in real-time
tail -f /var/log/spider_run.log      # Spider execution
tail -f /var/log/spider_push.log     # Git pushes
tail -f /var/log/dashboard_ping.log  # Dashboard pings
```

---

## 📊 Data Flow Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    DigitalOcean Droplet                    │
│                                                            │
│  1. Cron triggers at 2:00 AM UTC                           │
│     ↓                                                      │
│  2. Scrapy spider runs (7 days of Federal Register data)   │
│     ↓                                                      │
│  3. JSON saved to: federal_register/Spider Output Files/   │
│     ↓                                                      │
│  4. Cron triggers push script at 2:15 AM UTC               │
│     ↓                                                      │
│  5. Git commit + push to GitHub                            │
└────────────────────────────┬───────────────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     GitHub      │
                    │   Repository    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Streamlit     │
                    │  Community      │
                    │     Cloud       │
                    │                 │
                    │  Cache: 1 hour  │
                    │  Ping: 6 days   │
                    └─────────────────┘
```

---

## 🔧 Customization Options

### Change Spider Schedule

**Run every 6 hours:**
```cron
0 */6 * * * cd $REPO_DIR && python3 -m scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json" >> /var/log/spider_run.log 2>&1
15 */6 * * * $REPO_DIR/push_spider_data.sh
```

**Run at specific time (e.g., 6 AM EST = 11 AM UTC):**
```cron
0 11 * * * cd $REPO_DIR && python3 -m scrapy crawl federal_register_eo -o "federal_register/Spider Output Files/items_federal_register_eo_1.json" >> /var/log/spider_run.log 2>&1
15 11 * * * $REPO_DIR/push_spider_data.sh
```

### Change Dashboard Cache TTL

Edit `dashboard/data_loader.py`:
```python
@st.cache_data(ttl=1800)  # 30 minutes
@st.cache_data(ttl=3600)  # 1 hour (current)
@st.cache_data(ttl=7200)  # 2 hours
```

### Change Dashboard Ping Frequency

```cron
0 9 */3 * * curl -s "$DASHBOARD_URL" >> /var/log/dashboard_ping.log 2>&1  # Every 3 days
0 9 */6 * * curl -s "$DASHBOARD_URL" >> /var/log/dashboard_ping.log 2>&1  # Every 6 days (current)
```

---

## 🐛 Troubleshooting

### Problem: Spider not running
```bash
# Check Python path
which python3

# Verify Scrapy installed
python3 -m scrapy version

# Check log
cat /var/log/spider_run.log
```

### Problem: Push failing
```bash
# Check Git config
git config --list

# Test manual push
cd $REPO_DIR && git push

# Check log
cat /var/log/spider_push.log
```

### Problem: Dashboard not updating
1. Check GitHub commits (data should be pushed daily)
2. Wait up to 1 hour for cache to expire
3. Force restart dashboard from Streamlit Community Cloud

### Problem: Dashboard sleeping
```bash
# Check ping log
cat /var/log/dashboard_ping.log

# Should see HTTP 200 responses
# If getting 404, verify DASHBOARD_URL is correct
```

---

## 📝 Files Modified/Created

| File | Type | Purpose |
|------|------|---------|
| `dashboard/data_loader.py` | Modified | Added 1-hour cache TTL to all loaders |
| `push_spider_data.sh` | New | Automated Git push script for Droplet |
| `DROPLET_SETUP.md` | New | Comprehensive setup guide |
| `crontab_template.txt` | New | Ready-to-use cron schedule |
| `QUICK_START.md` | New | This file - quick reference |
| `_AI_CONTEXT_INDEX/08_KEY_DATASETS.md` | Modified | Added data pipeline documentation |

---

## 📚 Additional Documentation

- **Full Setup Guide**: `DROPLET_SETUP.md`
- **Crontab Template**: `crontab_template.txt`
- **Data Sources**: `_AI_CONTEXT_INDEX/08_KEY_DATASETS.md`

---

## ✨ What's Fixed

| Issue | Status | Solution |
|-------|--------|----------|
| Dashboard showing old data | ✅ Fixed | Added 1-hour cache TTL |
| Spider data not in GitHub | ✅ Fixed | Automated push script + cron |
| Dashboard goes to sleep | ✅ Fixed | Auto-ping every 6 days |
| Manual data updates required | ✅ Fixed | Fully automated pipeline |

---

## 🎯 Next Steps

1. ✅ **Review this guide**
2. ⏳ **Update `push_spider_data.sh` with your repo path**
3. ⏳ **Test spider and push script manually**
4. ⏳ **Install crontab on your Droplet**
5. ⏳ **Monitor logs for 24 hours**
6. ✅ **Done! Your pipeline is automated**

---

**Questions?** Check `DROPLET_SETUP.md` for detailed troubleshooting and advanced configuration options.
