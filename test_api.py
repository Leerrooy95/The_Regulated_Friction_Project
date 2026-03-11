"""
test_api.py — Regulated Friction Project: Llama-4-Scout Extraction Pipeline
===========================================================================
Sends the intel.txt mission brief to Llama-4-Scout-17B-16E-Instruct for
clinical entity extraction and friction/compliance scoring.

Usage:
    python test_api.py                    # Full run, saves to output/
    python test_api.py --dry-run          # Print token estimate, don't call API
    python test_api.py --intel custom.txt # Use a different intel file
"""

import os
import sys
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()

# ─── CONFIG ───────────────────────────────────────────────────────────────────
ENDPOINT     = "https://models.github.ai/inference"
MODEL        = "Llama-4-Scout-17B-16E-Instruct"
TOKEN        = os.environ.get("MODEL_API_KEY")
TEMPERATURE  = 0.1          # Low temp for deterministic extraction
MAX_TOKENS   = 16384        # Scout supports up to 16K output — enough for full JSON
TOP_P        = 0.9          # Slight nucleus sampling to avoid degenerate loops
OUTPUT_DIR   = Path("output")
INTEL_FILE   = "intel.txt"

# ─── SYSTEM PROMPT ────────────────────────────────────────────────────────────

# This is SEPARATE from the intel data. Keep it focused on the extraction task.

# The intel.txt goes in the UserMessage where the model allocates attention for

# content analysis. The system message defines HOW to analyze, not WHAT.


SYSTEM_PROMPT = """You are the lead Intelligence Officer for The Regulated Friction Project.

## YOUR ANALYTICAL FRAMEWORK

The Regulated Friction Project documents statistically significant correlations between high-visibility "friction" events (document releases, scandals, media cycles) and institutional "compliance" events (policy shifts, financial moves, regulatory changes).

Core statistical baseline:
- Pearson r = 0.6196 at 2-week lag (actual median: 7 days) (p = 0.0004, n = 28)
- 93% response rate across 66 historical backfill pairs (2017-2024)
- Median lag: +7 days
- Convergence Model: Calendar anchors independently drive friction, policy, and financial events into the same window

## CRITICAL ENTITY DISAMBIGUATION

You MUST interpret these terms in their correct context. Misidentification will corrupt downstream analysis:

- "DOGE" = Department of Government Efficiency — the federal government restructuring initiative led by Elon Musk, focused on workforce reductions, agency restructuring, and Schedule Policy/Career reclassification of federal employees. This is NOT the Dogecoin cryptocurrency. Track: layoffs, RIFs, agency closures, NTEU lawsuits, federal court injunctions.
- "Board of Peace" = A specific Trump-created international organization for Gaza reconstruction, established via Executive Order 14375 with IOIA diplomatic immunity. Chairman: Trump (lifetime tenure, sole authority). NOT a generic peace organization. Track: membership, capital pledges, reconstruction contracts, legal challenges, ISF troop deployments.
- "Schedule Policy/Career" (Schedule P/C) = Reclassification of ~50,000 federal career positions to at-will employment, replacing the legacy "Schedule F" executive order. Implementation date: March 9, 2026.
- "MGX" = UAE sovereign technology investment fund chaired by Sheikh Tahnoon bin Zayed Al Nahyan (UAE national security adviser). Core positions: TikTok (15%), Stargate equity, World Liberty Financial (49% via Aryam Investment 1), G42 AI chips.
- "1789 Capital" = Investment vehicle founded by Omeed Malik. Investments: Tucker Carlson Network, Anduril, Neuralink, xAI, SpaceX, Cerebras. Functions as bridge between Gulf capital, media narrative, and defense tech.
- "QXO" = Public holding company. Affinity Partners (Kushner) sole public holding. Apollo $3B credit pipeline. Completed $11B Beacon Roofing acquisition.
- "Affinity Partners" = Jared Kushner's investment firm. $5.4B AUM including $2B from Saudi PIF. Kushner serves as Board of Peace Senior Adviser.
- "Savvy Games" = Saudi PIF subsidiary for gaming investments (Scopely, Niantic, ESL FACEIT, SNK).
- "Sanabil Investments" = Saudi PIF subsidiary investing in 40+ US VC/PE firms including a16z, Founders Fund, and Valar Ventures.
- "Operation Epic Fury" = US-Israel military operation against Iran that began February 28, 2026. Also "Lion's Roar" (Israel).
- "CRINK" = Analytical framework for China-Russia-Iran-North Korea coordination bloc. Not an official organization.

## YOUR TASK

1. Parse the provided intel document
2. Classify each event as FRICTION or COMPLIANCE (or ANCHOR / PENDING)
3. Extract all named entities (persons, organizations, dollar amounts, dates)
4. Identify CONVERGENCE_NODES: any entity appearing in 3+ distinct domains (e.g., tech + finance + governance + defense)
5. Score each event's dashboard relevance tier
6. Flag any signals that may update or invalidate existing predictions

## REQUIRED OUTPUT FORMAT

Return a single valid JSON object with this exact structure. No markdown, no backticks, no commentary — raw JSON only:

{
  "extraction_metadata": {
    "model": "Llama-4-Scout-17B-16E-Instruct",
    "timestamp": "<ISO 8601>",
    "intel_source": "intel.txt",
    "events_processed": <int>,
    "convergence_nodes_found": <int>
  },
  "pending_signals": [
    {
      "event": "<description>",
      "deadline": "<YYYY-MM-DD or quarter>",
      "monitoring_priority": "HIGH | MEDIUM | LOW",
      "web_verification_needed": <true|false>,
      "verification_query": "<search query if web needed>"
    }
  ],
  "events": [
    {
      "event_id": "<FRIC|COMP|ANCH|PEND>_YYYYMMDD_<short_slug>",
      "date": "<YYYY-MM-DD>",
      "date_end": "<YYYY-MM-DD or null if single-day>",
      "event_type": "FRICTION | COMPLIANCE | ANCHOR | PENDING",
      "category": "<one of: Document_Release, Financial_Exposé, Executive_Order, Military_Action, Capital_Flow, Territorial, Congressional, International_Summit, Enforcement_Change, Media_Flashbang, Corporate_Leadership, SEC_Filing, Credit_Pipeline, Immunity_Grant, Military_Authorization>",
      "actors": ["<primary>", "<secondary>", "..."],
      "dollar_amount": <number or null>,
      "description": "<one-line clinical summary, max 200 chars>",
      "lag_from_nearest_friction": null,
      "source_type": "Government_Filing | News_Report | SEC_EDGAR | Congressional_Record | Court_Document",
      "confidence": "HIGH | MEDIUM | LOW",
      "dashboard_relevance": "TIER_1_CRITICAL | TIER_2_MODERATE | TIER_3_CONTEXTUAL",
      "convergence_node_flags": ["<entity names appearing in 3+ domains>"],
      "prediction_impact": "<null or description of which prediction this updates>"
    }
  ],
  "convergence_nodes": [
    {
      "entity": "<name>",
      "domains": ["<domain1>", "<domain2>", "..."],
      "domain_count": <int>,
      "key_persons": ["<name>"],
      "total_dollar_exposure": <number or null>,
      "assessment": "<one-line significance>"
    }
  ],
  "active_window_summary": {
    "window_start": "2026-02-08",
    "window_end": "2026-02-21",
    "total_friction_events": <int>,
    "total_compliance_events": <int>,
    "density_vs_baseline": "<multiplier, e.g. 4.67x>",
    "highest_single_day": "<date>",
    "highest_single_day_count": <int>
  },
  "model_notes": "<any caveats, ambiguities, or flags the model wants to raise>"
}

CRITICAL RULES:
- Output ONLY the JSON object. No text before or after.
- Every dollar_amount must be a raw integer (no $ signs, no commas, no "B" or "M" suffixes). Conversion guide: "Billion" = multiply by 1000000000, "Million" = multiply by 1000000. Examples: "$3.5 billion" → 3500000000, "$500M" → 500000000, "$17B" → 17000000000, "three and a half billion" → 3500000000. When in doubt, round to nearest million.
- Dates in ISO 8601: YYYY-MM-DD.
- If a field is unknown, use null — never fabricate data.
- Convergence nodes MUST appear in 3+ distinct domains to qualify. Entities with fewer than 3 domains should be EXCLUDED from the convergence_nodes array.
- Do NOT editorialize or add opinions. Clinical extraction only.

ARRAY FORMAT RULES (critical for downstream parsing):
- The "domains" array in convergence_nodes must contain SEPARATE strings for each domain. WRONG: ["A, B, C"]. RIGHT: ["A", "B", "C"]. Each domain is ONE string in the array. domain_count must equal the actual length of the domains array.
- The "actors" array in events must contain SEPARATE strings for each actor. WRONG: ["SEC / CFTC", "Board of Peace / 40+ countries"]. RIGHT: ["SEC", "CFTC", "Board of Peace", "40+ countries"].

CROSS-REFERENCE RULES (critical for dashboard):
- lag_from_nearest_friction: ALWAYS output null for this field. Do not attempt to calculate date math. The system will handle this post-generation.
- convergence_node_flags: For each event, check if ANY actor in the event also appears in the convergence_nodes entity list. If yes, list those entity names. Example: if an event's actors include "Apollo" and Apollo is a convergence node, then convergence_node_flags should include "Apollo Global Management". NEVER leave empty if actors overlap with convergence nodes.

COMPLETENESS RULES:
- Extract EVERY friction and compliance event from the intel. The intel contains labeled sections (FRICTION_EVENT, COMPLIANCE_EVENT, PENDING). Each labeled item must appear as a separate entry in the appropriate output array.
- ALL items in Section 6 (PENDING / TRACKING) must appear in the pending_signals array. Do not stop at 3.
- Actor Granularity: If an event involves an umbrella organization (e.g., "Board of Peace"), you MUST also list any specific individuals, funds, or companies explicitly mentioned as being involved in that specific event (e.g., add "Apollo Global Management" or "Jared Kushner" to the actors array if the text places them at the event). Do not guess or infer; only extract what is in the text.
"""

# ─── HELPERS ──────────────────────────────────────────────────────────────────

def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for English text."""
    return len(text) // 4


def normalize_dollar_amount(value) -> int | float | None:
    """
    Normalize dollar amounts that the model may output in non-numeric formats.
    Handles: "$3B", "3.5 billion", "$500M", "500000000", 3000000000, "$17,000,000,000"
    Returns raw numeric value or None if unparseable.
    """
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return value

    # Convert to string and clean
    s = str(value).strip().replace(",", "").replace("$", "").replace("+", "")

    # Handle word multipliers
    multipliers = {
        "trillion": 1_000_000_000_000,
        "billion": 1_000_000_000,
        "million": 1_000_000,
        "thousand": 1_000,
        "T": 1_000_000_000_000,
        "B": 1_000_000_000,
        "M": 1_000_000,
        "K": 1_000,
    }

    for suffix, mult in multipliers.items():
        if s.lower().endswith(suffix.lower()):
            num_part = s[:len(s) - len(suffix)].strip()
            try:
                return int(float(num_part) * mult)
            except ValueError:
                continue

    # Try direct numeric parse
    try:
        return int(float(s))
    except ValueError:
        return None


def normalize_event_dollars(data: dict) -> tuple[dict, int]:
    """
    Walk through all events and convergence_nodes, normalizing dollar_amount
    and total_dollar_exposure fields. Returns (cleaned_data, fix_count).
    """
    fixes = 0

    for event in data.get("events", []):
        original = event.get("dollar_amount")
        if original is not None and not isinstance(original, (int, float)):
            normalized = normalize_dollar_amount(original)
            if normalized is not None:
                event["dollar_amount"] = normalized
                fixes += 1

    for node in data.get("convergence_nodes", []):
        original = node.get("total_dollar_exposure")
        if original is not None and not isinstance(original, (int, float)):
            normalized = normalize_dollar_amount(original)
            if normalized is not None:
                node["total_dollar_exposure"] = normalized
                fixes += 1

    return data, fixes


# ─── POST-PROCESSING ENGINE ──────────────────────────────────────────────────
# Catches structural issues the Scout model may produce despite prompt rules.
# Each function is idempotent — safe to run multiple times on the same data.

def fix_domain_arrays(data: dict) -> tuple[dict, int]:
    """
    Fix convergence_nodes where domains are comma-separated strings inside
    a single array element instead of separate strings.
    E.g., ["A, B, C"] → ["A", "B", "C"]
    Also recomputes domain_count to match actual array length.
    """
    fixes = 0
    for node in data.get("convergence_nodes", []):
        domains = node.get("domains", [])
        if not domains:
            continue

        # Check if any element contains commas (the bug pattern)
        needs_split = any("," in d for d in domains)
        if needs_split:
            new_domains = []
            for d in domains:
                # Split on comma, strip whitespace, remove parens/dollar junk for cleaner labels
                parts = [p.strip() for p in d.split(",") if p.strip()]
                new_domains.extend(parts)

            # Deduplicate while preserving order
            seen = set()
            deduped = []
            for d in new_domains:
                key = d.lower()
                if key not in seen:
                    seen.add(key)
                    deduped.append(d)

            node["domains"] = deduped
            node["domain_count"] = len(deduped)
            fixes += 1
        else:
            # Even if no comma fix needed, ensure domain_count is accurate
            node["domain_count"] = len(domains)

    return data, fixes


def fix_convergence_threshold(data: dict) -> tuple[dict, int]:
    """
    Remove convergence_nodes with fewer than 3 domains.
    The Scout sometimes includes entities with 1-2 domains despite the 3+ rule.
    """
    original_nodes = data.get("convergence_nodes", [])
    valid_nodes = [n for n in original_nodes if n.get("domain_count", 0) >= 3]
    removed = len(original_nodes) - len(valid_nodes)
    data["convergence_nodes"] = valid_nodes

    # Update metadata count
    meta = data.get("extraction_metadata", {})
    meta["convergence_nodes_found"] = len(valid_nodes)

    return data, removed


def calculate_friction_lags(data: dict) -> tuple[dict, int]:
    """
    For each COMPLIANCE event, calculate calendar days from the nearest
    prior FRICTION event. Sets lag_from_nearest_friction on compliance events.
    """
    from datetime import date

    events = data.get("events", [])
    fixes = 0

    # Collect friction dates
    friction_dates = []
    for evt in events:
        if evt.get("event_type") == "FRICTION" and evt.get("date"):
            try:
                friction_dates.append(date.fromisoformat(evt["date"]))
            except ValueError:
                continue

    if not friction_dates:
        return data, fixes

    friction_dates.sort()

    # Calculate lags for compliance events
    for evt in events:
        if evt.get("event_type") != "COMPLIANCE":
            continue
        if not evt.get("date"):
            continue

        try:
            comp_date = date.fromisoformat(evt["date"])
        except ValueError:
            continue

        # Find nearest prior friction date
        prior = [fd for fd in friction_dates if fd <= comp_date]
        if prior:
            lag = (comp_date - prior[-1]).days
            evt["lag_from_nearest_friction"] = lag
            fixes += 1
        else:
            # No prior friction event — use nearest overall
            nearest = min(friction_dates, key=lambda fd: abs((comp_date - fd).days))
            lag = (comp_date - nearest).days
            evt["lag_from_nearest_friction"] = lag
            fixes += 1

    return data, fixes


def fix_actor_arrays(data: dict) -> tuple[dict, int]:
    """
    Fix events where actors are slash-separated or comma-separated strings
    inside a single array element instead of separate strings.
    E.g., ["PIF / Mubadala / Silver Lake"] → ["PIF", "Mubadala", "Silver Lake"]
    Also handles: ["Board of Peace / 40+ countries"] → ["Board of Peace", "40+ countries"]
    """
    fixes = 0
    for evt in data.get("events", []):
        actors = evt.get("actors", [])
        if not actors:
            continue

        needs_split = any(" / " in a or (", " in a and len(a) > 40) for a in actors)
        if needs_split:
            new_actors = []
            for a in actors:
                if " / " in a:
                    parts = [p.strip() for p in a.split(" / ") if p.strip()]
                    new_actors.extend(parts)
                elif ", " in a and len(a) > 40:
                    parts = [p.strip() for p in a.split(", ") if p.strip()]
                    new_actors.extend(parts)
                else:
                    new_actors.append(a)

            # Deduplicate preserving order
            seen = set()
            deduped = []
            for a in new_actors:
                if a.lower() not in seen:
                    seen.add(a.lower())
                    deduped.append(a)

            evt["actors"] = deduped
            fixes += 1

    return data, fixes


def backfill_convergence_flags(data: dict) -> tuple[dict, int]:
    """
    For each event, check if any actor name overlaps with convergence_nodes
    entity names. Populate convergence_node_flags accordingly.
    Uses fuzzy matching — if an actor string contains a node entity name
    (or vice versa), it counts as a match.
    """
    nodes = data.get("convergence_nodes", [])
    events = data.get("events", [])
    fixes = 0

    if not nodes:
        return data, fixes

    # Build lookup: lowercase entity name → original entity name
    node_names = {}
    for node in nodes:
        entity = node.get("entity", "")
        if entity:
            # Store both full name and short forms for fuzzy matching
            node_names[entity.lower()] = entity
            # Also store key words for partial matching
            # e.g., "Apollo Global Management" → also match "Apollo"
            for word in entity.split():
                if len(word) > 3 and word.lower() not in {"the", "and", "for", "inc", "llc", "ltd"}:
                    node_names[word.lower()] = entity

    for evt in events:
        actors = evt.get("actors", [])
        flags = set()

        for actor in actors:
            actor_lower = actor.lower()
            for key, entity in node_names.items():
                # Bidirectional containment check
                if key in actor_lower or actor_lower in key:
                    flags.add(entity)

        if flags:
            # Merge with any existing flags (don't overwrite)
            existing = set(evt.get("convergence_node_flags", []))
            combined = existing | flags
            evt["convergence_node_flags"] = sorted(combined)
            if combined - existing:
                fixes += 1

    return data, fixes


def post_process(data: dict) -> tuple[dict, dict]:
    """
    Run all post-processing fixes in sequence.
    Returns (cleaned_data, fix_report).
    """
    report = {}

    data, n = fix_domain_arrays(data)
    report["domain_arrays_fixed"] = n

    data, n = fix_convergence_threshold(data)
    report["sub_threshold_nodes_removed"] = n

    data, n = fix_actor_arrays(data)
    report["actor_arrays_fixed"] = n

    data, n = calculate_friction_lags(data)
    report["lags_calculated"] = n

    data, n = backfill_convergence_flags(data)
    report["convergence_flags_backfilled"] = n

    return data, report


def extract_json(raw: str) -> dict | None:
    """
    Extract JSON from model output, handling common LLM formatting issues:
    - Markdown code fences (```json ... ```)
    - Leading/trailing whitespace or commentary
    - BOM characters
    """
    # Strip markdown fences
    cleaned = re.sub(r'^```(?:json)?\s*', '', raw.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r'```\s*$', '', cleaned.strip(), flags=re.MULTILINE)
    cleaned = cleaned.strip()

    # Try direct parse
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Try to find JSON object boundaries
    start = cleaned.find('{')
    end = cleaned.rfind('}')
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(cleaned[start:end + 1])
        except json.JSONDecodeError:
            pass

    return None


def save_output(data: dict | None, raw: str, run_id: str):
    """Save both parsed JSON and raw response for debugging."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Always save raw response
    raw_path = OUTPUT_DIR / f"{run_id}_raw.txt"
    raw_path.write_text(raw, encoding="utf-8")
    print(f"  Raw response saved: {raw_path}")

    # Save parsed JSON if valid
    if data is not None:
        json_path = OUTPUT_DIR / f"{run_id}_extracted.json"
        json_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        print(f"  Parsed JSON saved:  {json_path}")

        # Save a lightweight summary for quick review
        summary_path = OUTPUT_DIR / f"{run_id}_summary.txt"
        meta = data.get("extraction_metadata", {})
        events = data.get("events", [])
        nodes = data.get("convergence_nodes", [])
        window = data.get("active_window_summary", {})
        pending = data.get("pending_signals", [])

        lines = [
            f"=== EXTRACTION SUMMARY — {run_id} ===",
            f"Events processed:       {meta.get('events_processed', len(events))}",
            f"Convergence nodes:      {meta.get('convergence_nodes_found', len(nodes))}",
            f"Active window:          {window.get('window_start', '?')} to {window.get('window_end', '?')}",
            f"Friction events:        {window.get('total_friction_events', '?')}",
            f"Compliance events:      {window.get('total_compliance_events', '?')}",
            f"Density vs baseline:    {window.get('density_vs_baseline', '?')}",
            f"Pending signals:        {len(pending)}",
            "",
            "--- CONVERGENCE NODES ---",
        ]
        for node in nodes:
            lines.append(
                f"  {node.get('entity', '?')} — {node.get('domain_count', '?')} domains: "
                f"{', '.join(node.get('domains', []))}"
            )

        lines.extend(["", "--- TIER 1 CRITICAL EVENTS ---"])
        for evt in events:
            if evt.get("dashboard_relevance") == "TIER_1_CRITICAL":
                lines.append(
                    f"  [{evt.get('event_type', '?')}] {evt.get('date', '?')} — "
                    f"{evt.get('description', '?')[:100]}"
                )

        if data.get("model_notes"):
            lines.extend(["", "--- MODEL NOTES ---", data["model_notes"]])

        summary_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"  Summary saved:        {summary_path}")
    else:
        print("  ⚠ JSON parsing FAILED — check raw output for issues")


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    # Parse args
    dry_run = "--dry-run" in sys.argv
    intel_file = INTEL_FILE
    for i, arg in enumerate(sys.argv):
        if arg == "--intel" and i + 1 < len(sys.argv):
            intel_file = sys.argv[i + 1]

    # Validate environment
    if not TOKEN:
        print("ERROR: MODEL_API_KEY not found in environment. Set it in .env or export it.")
        sys.exit(1)

    if not Path(intel_file).exists():
        print(f"ERROR: Intel file not found: {intel_file}")
        sys.exit(1)

    # Read intel
    intel_data = Path(intel_file).read_text(encoding="utf-8")

    # Token estimates
    system_tokens = estimate_tokens(SYSTEM_PROMPT)
    intel_tokens = estimate_tokens(intel_data)
    total_input = system_tokens + intel_tokens

    print(f"=== Regulated Friction Project — Llama Scout Extraction ===")
    print(f"Model:          {MODEL}")
    print(f"Intel file:     {intel_file}")
    print(f"Temperature:    {TEMPERATURE}")
    print(f"Max tokens out: {MAX_TOKENS}")
    print(f"")
    print(f"Token estimates (approximate):")
    print(f"  System prompt:  ~{system_tokens:,} tokens")
    print(f"  Intel data:     ~{intel_tokens:,} tokens")
    print(f"  Total input:    ~{total_input:,} tokens")
    print(f"  Output budget:  ~{MAX_TOKENS:,} tokens")
    print(f"  Total capacity: ~{total_input + MAX_TOKENS:,} tokens")
    print()

    if total_input > 100_000:
        print("⚠ WARNING: Input exceeds 100K tokens. Consider trimming intel.txt or")
        print("  removing redundant context. Scout handles 512K but quality degrades.")
        print()

    if dry_run:
        print("--dry-run flag set. Exiting without API call.")
        return

    # Build messages
    messages = [
        SystemMessage(SYSTEM_PROMPT),
        UserMessage(intel_data),
    ]

    # Call API
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    print(f"Calling {MODEL}...")
    print(f"Run ID: {run_id}")
    print()

    try:
        client = ChatCompletionsClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(TOKEN),
        )

        response = client.complete(
            messages=messages,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            max_tokens=MAX_TOKENS,
            model=MODEL,
        )

        raw_content = response.choices[0].message.content
        finish_reason = response.choices[0].finish_reason

        print(f"Response received.")
        print(f"  Finish reason: {finish_reason}")
        print(f"  Response length: {len(raw_content):,} chars (~{estimate_tokens(raw_content):,} tokens)")

        if finish_reason == "length":
            print("  ⚠ WARNING: Response was TRUNCATED (hit max_tokens).")
            print("    Increase MAX_TOKENS or simplify the extraction schema.")

        # Parse and save
        print()
        print("Parsing JSON...")
        parsed = extract_json(raw_content)

        # Normalize dollar amounts before saving
        dollar_fixes = 0
        if parsed:
            parsed, dollar_fixes = normalize_event_dollars(parsed)
            if dollar_fixes:
                print(f"  💰 Normalized {dollar_fixes} dollar amount(s) from string→numeric")

        # Run post-processing engine
        pp_report = {}
        if parsed:
            parsed, pp_report = post_process(parsed)
            print(f"  🔧 Post-processing complete:")
            if pp_report.get("domain_arrays_fixed"):
                print(f"     • Split {pp_report['domain_arrays_fixed']} comma-joined domain array(s)")
            if pp_report.get("sub_threshold_nodes_removed"):
                print(f"     • Removed {pp_report['sub_threshold_nodes_removed']} node(s) below 3-domain threshold")
            if pp_report.get("actor_arrays_fixed"):
                print(f"     • Split {pp_report['actor_arrays_fixed']} slash/comma-joined actor array(s)")
            if pp_report.get("lags_calculated"):
                print(f"     • Calculated lag for {pp_report['lags_calculated']} compliance event(s)")
            if pp_report.get("convergence_flags_backfilled"):
                print(f"     • Backfilled convergence flags on {pp_report['convergence_flags_backfilled']} event(s)")
            if not any(pp_report.values()):
                print(f"     • No fixes needed — model output was clean")

        save_output(parsed, raw_content, run_id)

        # Quick validation
        if parsed:
            events = parsed.get("events", [])
            nodes = parsed.get("convergence_nodes", [])
            pending = parsed.get("pending_signals", [])
            print()
            print(f"✅ Extraction successful:")
            print(f"   {len(events)} events extracted")
            print(f"   {len(nodes)} convergence nodes (3+ domains)")
            print(f"   {len(pending)} pending signals tracked")

            # Check for common issues
            empty_actors = sum(1 for e in events if not e.get("actors"))
            null_dates = sum(1 for e in events if not e.get("date"))
            if empty_actors:
                print(f"   ⚠ {empty_actors} events have empty actor lists")
            if null_dates:
                print(f"   ⚠ {null_dates} events have null dates")

            # Validate dollar amounts are numeric
            bad_dollars = []
            for e in events:
                amt = e.get("dollar_amount")
                if amt is not None and not isinstance(amt, (int, float)):
                    bad_dollars.append(e.get("event_id", "unknown"))
            if bad_dollars:
                print(f"   ⚠ Non-numeric dollar_amount in: {', '.join(bad_dollars)}")

            # Check lag coverage for compliance events
            comp_events = [e for e in events if e.get("event_type") == "COMPLIANCE"]
            comp_no_lag = sum(1 for e in comp_events
                             if e.get("lag_from_nearest_friction") is None)
            if comp_no_lag:
                print(f"   ⚠ {comp_no_lag}/{len(comp_events)} compliance events still missing lag")
            elif comp_events:
                lags = [e["lag_from_nearest_friction"] for e in comp_events]
                print(f"   ✓ Lag range: {min(lags)}–{max(lags)} days (median ~{sorted(lags)[len(lags)//2]})")

            # Check convergence flag coverage
            events_with_flags = sum(1 for e in events
                                    if e.get("convergence_node_flags"))
            print(f"   ✓ {events_with_flags}/{len(events)} events linked to convergence nodes")

        print()
        print(f"Done. Check output/ directory for results.")

    except Exception as exc:
        print(f"ERROR: API call failed.")
        print(f"  Type: {type(exc).__name__}")
        print(f"  Detail: {exc}")
        print()
        print("Common fixes:")
        print("  - Check MODEL_API_KEY is valid and has model access")
        print("  - Verify endpoint: https://models.github.ai/inference")
        print("  - Check rate limits on your GitHub Models access tier")
        sys.exit(1)


if __name__ == "__main__":
    main()
