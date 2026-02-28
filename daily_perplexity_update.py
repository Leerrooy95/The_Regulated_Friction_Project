"""
daily_perplexity_update.py
==========================
Runs after Llama Scout extraction in the daily GitHub Actions pipeline.
Uses Perplexity (sonar-pro) to:
1. Verify all HIGH priority pending signals
2. Search for breaking news relevant to framework entities
3. Prioritize today's most important developments
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
OUTPUT_DIR = Path("output")

# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

BREAKING_NEWS_PROMPT = """You are monitoring breaking news for The Regulated Friction Project.

Today's date: {today}

Search for any breaking news in the last 24 hours related to these entities:
{entities}

Focus areas:
- Executive orders, policy changes, regulatory actions
- Corporate leadership changes, SEC filings, major deals
- International developments (Iran, Cuba, Israel/Gaza, Taiwan)
- DOJ/FBI actions, congressional hearings
- Schedule F/Schedule P/C implementation

For each relevant finding, return:
- headline: One-line summary
- source: Primary source URL
- timestamp: When reported
- framework_relevance: How this connects to friction/compliance patterns
- priority: HIGH/MEDIUM/LOW

Return as JSON array. If no relevant news found, return empty array."""

DAILY_PRIORITY_PROMPT = """You are the intelligence analyst for The Regulated Friction Project.

Today's date: {today}

## VERIFIED SIGNALS
{verified_signals}

## BREAKING NEWS
{breaking_news}

## UPCOMING DEADLINES (next 7 days)
{upcoming_deadlines}

## YOUR TASK

Analyze all inputs and determine:

1. **top_3_developments**: Array of the three most important items for TODAY. Each object MUST have these keys:
   - "headline": One-line title
   - "summary": 2-3 sentence explanation
   - "source": Primary source or reference
   - "timestamp": Date string (e.g. "2026-02-28")
   - "event_type": One of: "KINETIC" (military action, strikes, conflict), "REGULATORY" (filings, deadlines, court actions), "FINANCIAL" (deals, capital movements), "POLITICAL" (appointments, policy), "INTELLIGENCE" (threat assessments, signals, warnings, intelligence reports)
   - "imminence": One of: "IMMINENT" (within 24 hours), "NEAR_TERM" (within 7 days), "MONITORING" (ongoing)

2. **verification_updates**: Array of pending signals that are now resolved or have new information. Each object MUST have:
   - "signal": Name of the signal
   - "status": One of "verified", "unverified", or "pending"
   - "result": Description of current status
   - "new_sources": Source references (string)

3. **new_alerts**: Array of breaking news that introduces NEW friction or compliance events. Each object MUST have:
   - "headline": One-line title
   - "alert_type": Category of alert
   - "event_type": One of: "KINETIC", "REGULATORY", "FINANCIAL", "POLITICAL", "INTELLIGENCE"
   - "imminence": One of: "IMMINENT", "NEAR_TERM", "MONITORING"
   - "relevance": Framework relevance explanation
   - "timestamp": Date string
   - "priority": "HIGH", "MEDIUM", or "LOW"

4. **priority_watchlist**: Array of 3-5 plain text strings describing items to monitor in the next 24 hours

Return as JSON object with these four keys. Use EXACTLY the field names specified above."""


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
# Core pipeline functions
# ---------------------------------------------------------------------------

def load_latest_extraction() -> dict | None:
    """Find and load the most recent *_extracted.json from output/."""
    if not OUTPUT_DIR.exists():
        logger.warning("output/ directory not found")
        return None

    extraction_files = sorted(
        OUTPUT_DIR.glob("*_extracted.json"),
        key=lambda p: p.name,
        reverse=True,
    )
    if not extraction_files:
        logger.warning("No *_extracted.json files found in output/")
        return None

    latest = extraction_files[0]
    logger.info("Loading latest extraction: %s", latest.name)
    try:
        with open(latest, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as exc:
        logger.error("Failed to load %s: %s", latest, exc)
        return None


def verify_pending_signals(client, pending_signals: list) -> tuple[list, int]:
    """Call Perplexity to verify each HIGH priority signal.

    Re-uses the same verification approach as ``perplexity_verify.py`` but
    returns a richer structure for the daily intelligence file.
    """
    results = []
    api_calls = 0
    for sig in pending_signals:
        query = sig.get("verification_query", sig.get("event", ""))
        if not query:
            continue
        try:
            raw = _call_perplexity(client, f"Verify this signal as of today: {query}")
            api_calls += 1
            description = raw.strip()
            status = "verified" if description and "no relevant" not in description.lower() else "unverified"
            results.append({
                "signal": sig.get("event", query),
                "original_deadline": sig.get("deadline"),
                "status": status,
                "result": description[:500],
                "source": "",
            })
        except Exception:  # noqa: BLE001
            results.append({
                "signal": sig.get("event", query),
                "original_deadline": sig.get("deadline"),
                "status": "error",
                "result": "Verification failed",
                "source": "",
            })
    return results, api_calls


def scan_for_breaking_news(client, entities: list) -> tuple[list, int]:
    """Query Perplexity for breaking news on key entities."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    prompt = BREAKING_NEWS_PROMPT.format(
        today=today,
        entities="\n".join(f"- {e}" for e in entities),
    )
    try:
        raw = _call_perplexity(client, prompt)
        parsed = _parse_json(raw)
        if isinstance(parsed, list):
            return parsed, 1
        return [], 1
    except Exception:  # noqa: BLE001
        logger.warning("Breaking news scan failed")
        return [], 1


def prioritize_for_today(
    client,
    verified_signals: list,
    breaking_news: list,
    pending_signals: list,
) -> tuple[dict, int]:
    """Use Perplexity to rank and prioritize what matters TODAY."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Build upcoming deadlines from pending signals (they have deadline fields)
    upcoming = []
    for sig in pending_signals:
        deadline = sig.get("deadline") or sig.get("date")
        if deadline:
            upcoming.append(f"{sig.get('event', sig.get('description', ''))}: {deadline}")

    prompt = DAILY_PRIORITY_PROMPT.format(
        today=today,
        verified_signals=json.dumps(verified_signals, indent=2) if verified_signals else "None available",
        breaking_news=json.dumps(breaking_news, indent=2) if breaking_news else "None found",
        upcoming_deadlines="\n".join(upcoming) if upcoming else "None identified",
    )
    try:
        raw = _call_perplexity(client, prompt)
        parsed = _parse_json(raw)
        if isinstance(parsed, dict):
            return parsed, 1
        # If parsing fails, return structured empty result
        return {
            "top_3_developments": [],
            "verification_updates": [],
            "new_alerts": [],
            "priority_watchlist": [],
        }, 1
    except Exception:  # noqa: BLE001
        logger.warning("Prioritization failed")
        return {
            "top_3_developments": [],
            "verification_updates": [],
            "new_alerts": [],
            "priority_watchlist": [],
        }, 1


def save_daily_intelligence(data: dict):
    """Save to output/daily_intelligence.json (overwritten daily)."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / "daily_intelligence.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    logger.info("Daily intelligence saved to %s", output_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    client = _get_client()
    if client is None:
        logger.error("Cannot proceed without Perplexity API key")
        sys.exit(1)

    extraction = load_latest_extraction()
    if extraction is None:
        logger.error("No extraction data available — skipping daily update")
        sys.exit(1)

    pending = extraction.get("pending_signals", [])
    nodes = extraction.get("convergence_nodes", [])
    events = extraction.get("events", [])

    total_api_calls = 0

    # Step 1: Verify HIGH priority pending signals
    high_priority = [s for s in pending if s.get("monitoring_priority") == "HIGH"]
    logger.info("Verifying %d HIGH priority signals…", len(high_priority))
    verified, calls = verify_pending_signals(client, high_priority)
    total_api_calls += calls

    # Step 2: Scan for breaking news on key entities
    entity_names = [n["entity"] for n in nodes if n.get("entity")]
    logger.info("Scanning breaking news for %d entities…", len(entity_names))
    breaking, calls = scan_for_breaking_news(client, entity_names)
    total_api_calls += calls

    # Step 3: Have Perplexity prioritize for today
    logger.info("Generating daily prioritization…")
    daily_intel, calls = prioritize_for_today(client, verified, breaking, pending)
    total_api_calls += calls

    # Step 4: Assemble and save output
    daily_intel.setdefault("top_3_developments", [])
    daily_intel.setdefault("verification_updates", verified)
    daily_intel.setdefault("new_alerts", [])
    daily_intel.setdefault("priority_watchlist", [])

    output = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_by": f"Perplexity {_MODEL_ID}",
        **daily_intel,
        "entities_scanned": entity_names,
        "pending_signals_checked": len(high_priority),
        "api_calls_made": total_api_calls,
    }

    save_daily_intelligence(output)
    logger.info(
        "Done. %d signals checked, %d breaking items, %d API calls.",
        len(high_priority),
        len(breaking),
        total_api_calls,
    )


if __name__ == "__main__":
    main()
