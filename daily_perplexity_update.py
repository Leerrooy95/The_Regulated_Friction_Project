"""
daily_perplexity_update.py (Standalone Version)
================================================
Perplexity-only intelligence pipeline. No Llama Scout dependency.
Loads tracked entities and signals from intelligence_config.json.

Uses Perplexity (sonar-pro) to:
1. Check status of each active signal
2. Scan breaking news across all tracked entities
3. Generate prioritized daily summary
4. Save daily_intelligence.json for dashboard consumption

Requires PERPLEXITY_API_KEY environment variable.
"""

import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# SDK import – deferred so the script still gives a helpful error when
# openai is not installed.
# ---------------------------------------------------------------------------
try:
    from openai import OpenAI  # type: ignore[import-untyped]
except ImportError:
    logger.error("openai package is not installed. Run: pip install openai")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
_MODEL_ID = "sonar-pro"
_BASE_URL = "https://api.perplexity.ai"
_MAX_RETRIES = 3
_BASE_BACKOFF = 2  # seconds; doubles on each retry
_DAILY_API_BUDGET = 50  # max API calls per 24-hour period
CONFIG_FILE = Path("intelligence_config.json")
OUTPUT_DIR = Path("output")
BUDGET_FILE = OUTPUT_DIR / ".api_budget.json"

# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

SIGNAL_STATUS_PROMPT = """You are a real-time intelligence analyst. Today is {today}.

Check the CURRENT STATUS of this signal: {signal}

Search terms to use: {search_terms}

Return a JSON object with:
- "status": "CONFIRMED" (event happened), "ACTIVE" (ongoing/developing), "MONITORING" (no new developments), or "RESOLVED"
- "headline": One-line current status
- "summary": 2-3 sentences on what's happening RIGHT NOW
- "event_type": "KINETIC" (military/strikes), "REGULATORY", "FINANCIAL", "POLITICAL", or "INTELLIGENCE"
- "imminence": "ONGOING" (happening now), "IMMINENT" (within 24h), "NEAR_TERM" (this week), or "MONITORING"
- "sources": Array of source references
- "timestamp": Today's date

Be specific about what HAS HAPPENED vs what MIGHT happen."""

BREAKING_NEWS_PROMPT = """You are a real-time intelligence analyst. Today is {today}.

Search for breaking news in the LAST 24 HOURS related to these entities:
{entities}

Framework context: {framework_context}

For each significant finding, return a JSON object with:
- "headline": One-line summary of what HAPPENED (not predictions)
- "summary": 2-3 sentences on the event
- "event_type": "KINETIC", "REGULATORY", "FINANCIAL", "POLITICAL", or "INTELLIGENCE"
- "imminence": "ONGOING", "IMMINENT", "NEAR_TERM", or "MONITORING"
- "priority": "HIGH", "MEDIUM", or "LOW"
- "framework_relevance": How this connects to friction/compliance patterns
- "sources": Source references
- "timestamp": When it occurred

Return as JSON array. Focus on CONFIRMED events, not speculation. If something happened, say it happened."""

DAILY_SUMMARY_PROMPT = """You are the intelligence analyst for The Regulated Friction Project.

Today: {today}

## SIGNAL STATUS UPDATES
{signal_updates}

## BREAKING NEWS
{breaking_news}

## FRAMEWORK CONTEXT
{framework_context}

Generate a daily intelligence summary with:

1. **top_3_developments**: The three most important items TODAY. Each MUST have:
   - "headline": What HAPPENED (past tense for confirmed events)
   - "summary": 2-3 sentence explanation
   - "event_type": "KINETIC", "REGULATORY", "FINANCIAL", "POLITICAL", or "INTELLIGENCE"
   - "imminence": "ONGOING", "IMMINENT", "NEAR_TERM", or "MONITORING"
   - "source": Primary source
   - "timestamp": Date

2. **new_alerts**: Breaking developments. Each MUST have:
   - "headline": What happened
   - "alert_type": Category
   - "event_type": Same options as above
   - "imminence": Same options as above
   - "relevance": Framework connection
   - "priority": "HIGH", "MEDIUM", "LOW"
   - "timestamp": Date

3. **signal_updates**: Status changes on tracked signals

4. **priority_watchlist**: 3-5 items to monitor next 24 hours

Use PAST TENSE for confirmed events. "US struck Iran" not "US may strike Iran".
Use PRESENT TENSE for ongoing situations. "Negotiations are underway" not "negotiations may occur".

Return as JSON object."""


# ---------------------------------------------------------------------------
# Client setup
# ---------------------------------------------------------------------------

def _get_client():
    """Return a configured OpenAI client pointed at Perplexity, or ``None``."""
    api_key = os.environ.get("PERPLEXITY_API_KEY", "")
    if not api_key:
        logger.warning("PERPLEXITY_API_KEY not set – daily update disabled")
        return None
    return OpenAI(api_key=api_key, base_url=_BASE_URL)


def _call_perplexity(client, prompt: str, *, _retries: int = 0) -> str:
    """Send a single prompt to Perplexity sonar-pro with retry logic."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a real-time intelligence analyst. "
                "Always return valid JSON. No markdown fences, no commentary."
            ),
        },
        {"role": "user", "content": prompt},
    ]
    try:
        response = client.chat.completions.create(
            model=_MODEL_ID,
            messages=messages,
        )
        return response.choices[0].message.content or ""
    except Exception as exc:  # noqa: BLE001
        err_msg = str(exc).lower()
        if ("429" in err_msg or "rate" in err_msg) and _retries < _MAX_RETRIES:
            wait = _BASE_BACKOFF * (2 ** _retries)
            logger.info("Rate-limited – retrying in %ss", wait)
            time.sleep(wait)
            return _call_perplexity(client, prompt, _retries=_retries + 1)
        logger.exception("Perplexity call failed")
        raise


def _parse_json(text: str):
    """Best-effort JSON parse from LLM output."""
    import re as _re

    text = text.strip()
    # Strip markdown fences (with optional language identifier)
    text = _re.sub(r"^```(?:\w+)?\s*\n?", "", text)
    text = _re.sub(r"\n?```\s*$", "", text)
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to locate a JSON object or array
        for start_char, end_char in [("{", "}"), ("[", "]")]:
            start = text.find(start_char)
            end = text.rfind(end_char)
            if start != -1 and end != -1 and end > start:
                try:
                    return json.loads(text[start : end + 1])
                except json.JSONDecodeError:
                    continue
    return None


# ---------------------------------------------------------------------------
# API budget management — resets every 24 hours
# ---------------------------------------------------------------------------

def _load_budget() -> dict:
    """Load daily API budget tracker from disk."""
    if BUDGET_FILE.exists():
        try:
            with open(BUDGET_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"date": "", "calls": 0}


def _save_budget(budget: dict):
    """Persist the budget tracker."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(BUDGET_FILE, "w", encoding="utf-8") as f:
        json.dump(budget, f)


def _check_budget() -> tuple[dict, bool]:
    """Check if we have remaining API budget today.

    Resets the counter when the UTC date rolls over.
    Returns (budget_dict, is_within_budget).
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    budget = _load_budget()
    if budget.get("date") != today:
        budget = {"date": today, "calls": 0}
    return budget, budget["calls"] < _DAILY_API_BUDGET


def _record_api_call(budget: dict) -> dict:
    """Increment the call counter and persist."""
    budget["calls"] = budget.get("calls", 0) + 1
    _save_budget(budget)
    return budget


# ---------------------------------------------------------------------------
# Core pipeline functions
# ---------------------------------------------------------------------------

def load_config() -> dict:
    """Load intelligence configuration."""
    if not CONFIG_FILE.exists():
        logger.error("Config file not found: %s", CONFIG_FILE)
        sys.exit(1)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_entities(config: dict) -> list:
    """Flatten all tracked entities into a single list."""
    entities = []
    for category, items in config.get("tracked_entities", {}).items():
        entities.extend(items)
    return entities


def check_signal_status(client, signal: dict, today: str) -> dict:
    """Check current status of a tracked signal via Perplexity."""
    prompt = SIGNAL_STATUS_PROMPT.format(
        today=today,
        signal=signal.get("signal", ""),
        search_terms=", ".join(signal.get("search_terms", []))
    )
    try:
        raw = _call_perplexity(client, prompt)
        parsed = _parse_json(raw)
        if isinstance(parsed, dict):
            parsed["original_signal"] = signal.get("signal", "")
            parsed["category"] = signal.get("category", "")
            return parsed
    except Exception:  # noqa: BLE001
        logger.warning("Failed to check signal: %s", signal.get("signal", ""))
    return {
        "original_signal": signal.get("signal", ""),
        "status": "ERROR",
        "headline": "Check failed",
        "summary": "",
        "sources": []
    }


def scan_breaking_news(client, entities: list, framework_context: str, today: str) -> list:
    """Scan for breaking news across all entities."""
    prompt = BREAKING_NEWS_PROMPT.format(
        today=today,
        entities="\n".join(f"- {e}" for e in entities),
        framework_context=framework_context
    )
    try:
        raw = _call_perplexity(client, prompt)
        parsed = _parse_json(raw)
        if isinstance(parsed, list):
            return parsed
    except Exception:  # noqa: BLE001
        logger.warning("Breaking news scan failed")
    return []


def generate_daily_summary(client, signal_updates: list, breaking_news: list, framework_context: str, today: str) -> dict:
    """Generate prioritized daily summary."""
    prompt = DAILY_SUMMARY_PROMPT.format(
        today=today,
        signal_updates=json.dumps(signal_updates, indent=2) if signal_updates else "No updates",
        breaking_news=json.dumps(breaking_news, indent=2) if breaking_news else "No breaking news",
        framework_context=framework_context
    )
    try:
        raw = _call_perplexity(client, prompt)
        parsed = _parse_json(raw)
        if isinstance(parsed, dict):
            return parsed
    except Exception:  # noqa: BLE001
        logger.warning("Daily summary generation failed")
    return {
        "top_3_developments": [],
        "new_alerts": [],
        "signal_updates": [],
        "priority_watchlist": []
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    client = _get_client()
    if client is None:
        logger.error("Cannot proceed without Perplexity API key")
        sys.exit(1)

    config = load_config()
    entities = get_all_entities(config)
    active_signals = config.get("active_signals", [])
    framework_context = config.get("framework_context", "")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Budget gate — abort early if daily limit is reached
    budget, within_budget = _check_budget()
    if not within_budget:
        logger.warning(
            "Daily API budget exhausted (%d/%d calls). Skipping run.",
            budget["calls"], _DAILY_API_BUDGET,
        )
        sys.exit(0)
    logger.info("API budget: %d/%d calls used today", budget["calls"], _DAILY_API_BUDGET)

    total_api_calls = 0

    # Step 1: Check status of each active signal
    logger.info("Checking %d active signals...", len(active_signals))
    signal_updates = []
    for signal in active_signals:
        budget, ok = _check_budget()
        if not ok:
            logger.warning("Budget limit reached during signal checks")
            break
        result = check_signal_status(client, signal, today)
        signal_updates.append(result)
        total_api_calls += 1
        budget = _record_api_call(budget)

    # Step 2: Scan breaking news
    budget, ok = _check_budget()
    if ok:
        logger.info("Scanning breaking news for %d entities...", len(entities))
        breaking_news = scan_breaking_news(client, entities, framework_context, today)
        total_api_calls += 1
        budget = _record_api_call(budget)
    else:
        logger.warning("Budget limit reached — skipping breaking news scan")
        breaking_news = []

    # Step 3: Generate daily summary
    budget, ok = _check_budget()
    if ok:
        logger.info("Generating daily summary...")
        daily_summary = generate_daily_summary(client, signal_updates, breaking_news, framework_context, today)
        total_api_calls += 1
        budget = _record_api_call(budget)
    else:
        logger.warning("Budget limit reached — skipping summary generation")
        daily_summary = {
            "top_3_developments": [],
            "new_alerts": [],
            "signal_updates": [],
            "priority_watchlist": []
        }

    # Step 4: Assemble output
    output = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_by": "Perplexity sonar-pro (standalone)",
        "config_version": config.get("last_updated", "unknown"),
        **daily_summary,
        "signal_status": signal_updates,
        "entities_scanned": entities,
        "api_calls_made": total_api_calls,
        "daily_budget_used": budget.get("calls", 0),
        "daily_budget_limit": _DAILY_API_BUDGET
    }

    # Save
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / "daily_intelligence.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    logger.info("Daily intelligence saved to %s", output_path)
    logger.info(
        "Done. %d signals checked, %d breaking items, %d API calls. Budget: %d/%d.",
        len(active_signals),
        len(breaking_news),
        total_api_calls,
        budget.get("calls", 0),
        _DAILY_API_BUDGET,
    )


if __name__ == "__main__":
    main()
