"""
Gemini API integration with Google Search grounding for live web
verification of pending signals.

Uses the google-genai SDK (successor to deprecated google-generativeai).
API key is read from the GEMINI_API_KEY environment variable.
"""

import json
import logging
import os
import time
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# SDK import – deferred so the rest of the dashboard still works when
# google-genai is not installed (e.g. local dev without the dependency).
# ---------------------------------------------------------------------------
try:
    from google import genai  # type: ignore[import-untyped]
    _HAS_GENAI = True
except ImportError:
    _HAS_GENAI = False

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
_MODEL_ID = "gemini-2.0-flash"
_MAX_RETRIES = 3
_BASE_BACKOFF = 2  # seconds; doubles on each retry


def _get_client():
    """Return a configured genai Client, or *None* when unavailable."""
    if not _HAS_GENAI:
        logger.warning("google-genai is not installed – verification disabled")
        return None
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        logger.warning("GEMINI_API_KEY not set – verification disabled")
        return None
    return genai.Client(api_key=api_key)


# ---------------------------------------------------------------------------
# Core verification function
# ---------------------------------------------------------------------------

def verify_pending_signals(queries: list[str]) -> list[dict]:
    """Verify a list of pending-signal queries via Gemini + Google Search.

    Parameters
    ----------
    queries : list[str]
        Plain-text search queries (typically the ``verification_query``
        values from the LLM extraction).

    Returns
    -------
    list[dict]
        One dict per query with the keys expected by the dashboard:
        ``query``, ``date``, ``description``, ``source``, ``status``.
        Status is one of ``"verified"``, ``"unverified"``, or ``"error"``.
    """
    client = _get_client()
    if client is None:
        return [_error_result(q, "Gemini client unavailable") for q in queries]

    results: list[dict] = []
    for query in queries:
        result = _verify_single(client, query)
        results.append(result)
    return results


def _verify_single(client, query: str, *, _retries: int = 0) -> dict:
    """Call Gemini for a single query, retrying on rate-limit errors."""
    prompt = (
        f"Search the web for the latest information about: {query}\n\n"
        "Return a concise summary (2-3 sentences) of what you found, "
        "including the most recent date mentioned and the primary source. "
        "If no relevant results are found, say so clearly."
    )
    try:
        response = client.models.generate_content(
            model=_MODEL_ID,
            contents=prompt,
            config={"tools": [{"google_search": {}}]},
        )

        # Extract grounding metadata when available
        description = response.text or ""
        source = ""
        search_queries: list[str] = []
        if response.candidates:
            meta = response.candidates[0].grounding_metadata
            if meta:
                search_queries = list(meta.web_search_queries or [])
                chunks = meta.grounding_chunks or []
                if chunks:
                    first = chunks[0]
                    if hasattr(first, "web") and first.web:
                        source = getattr(first.web, "uri", "") or getattr(first.web, "url", "")

        return {
            "query": query,
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "description": description.strip(),
            "source": source,
            "status": "verified" if description.strip() else "unverified",
            "search_queries": search_queries,
        }

    except Exception as exc:  # noqa: BLE001
        err_msg = str(exc).lower()
        # Retry on rate-limit / resource-exhausted errors
        if ("429" in err_msg or "resource" in err_msg) and _retries < _MAX_RETRIES:
            wait = _BASE_BACKOFF * (2 ** _retries)
            logger.info("Rate-limited on %r – retrying in %ss", query, wait)
            time.sleep(wait)
            return _verify_single(client, query, _retries=_retries + 1)
        logger.exception("Gemini verification failed for %r", query)
        return _error_result(query, str(exc))


def _error_result(query: str, message: str) -> dict:
    """Return a standard error-result dict."""
    return {
        "query": query,
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "description": f"Verification error: {message}",
        "source": "",
        "status": "error",
        "search_queries": [],
    }
