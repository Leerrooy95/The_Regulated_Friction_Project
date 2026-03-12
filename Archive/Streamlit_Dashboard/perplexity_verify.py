"""
Perplexity API integration for live web verification of pending signals.

Uses the OpenAI-compatible SDK pointed at the Perplexity API endpoint.
Perplexity has web search built-in — no extra tool config needed.
API key is read from the PERPLEXITY_API_KEY environment variable.
"""

import logging
import os
import time
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# SDK import – deferred so the rest of the dashboard still works when
# openai is not installed (e.g. local dev without the dependency).
# ---------------------------------------------------------------------------
try:
    from openai import OpenAI  # type: ignore[import-untyped]
    _HAS_OPENAI = True
except ImportError:
    _HAS_OPENAI = False

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
_MODEL_ID = "sonar-pro"
_BASE_URL = "https://api.perplexity.ai"
_MAX_RETRIES = 3
_BASE_BACKOFF = 2  # seconds; doubles on each retry


def _get_client():
    """Return a configured OpenAI client pointed at Perplexity, or ``None``."""
    if not _HAS_OPENAI:
        logger.warning("openai package is not installed – verification disabled")
        return None
    api_key = os.environ.get("PERPLEXITY_API_KEY", "")
    if not api_key:
        logger.warning("PERPLEXITY_API_KEY not set – verification disabled")
        return None
    return OpenAI(api_key=api_key, base_url=_BASE_URL)


# ---------------------------------------------------------------------------
# Core verification function
# ---------------------------------------------------------------------------

def verify_pending_signals(queries: list[str]) -> list[dict]:
    """Verify a list of pending-signal queries via Perplexity (web search built-in).

    Parameters
    ----------
    queries : list[str]
        Plain-text search queries (typically the ``verification_query``
        values from the LLM extraction).

    Returns
    -------
    list[dict]
        One dict per query with the keys expected by the dashboard:
        ``query``, ``date``, ``description``, ``source``, ``status``,
        and ``citations`` (list of source URLs from Perplexity).
        Status is one of ``"verified"``, ``"unverified"``, or ``"error"``.
    """
    client = _get_client()
    if client is None:
        return [_error_result(q, "Perplexity client unavailable") for q in queries]

    results: list[dict] = []
    for query in queries:
        result = _verify_single(client, query)
        results.append(result)
    return results


def _verify_single(client, query: str, *, _retries: int = 0) -> dict:
    """Call Perplexity for a single query, retrying on rate-limit errors."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a fact-checking assistant for The Regulated Friction Project, "
                "an OSINT research project. Search the web and return "
                "a concise summary (2-3 sentences) of what you found, "
                "including the most recent date mentioned and the primary source URL. "
                "CRITICAL DISAMBIGUATION: 'DOGE' means Department of Government Efficiency "
                "(federal restructuring led by Elon Musk), NOT Dogecoin cryptocurrency. "
                "'Board of Peace' is a Trump-created organization for Gaza reconstruction "
                "(EO 14375), NOT a generic peace group. 'Schedule Policy/Career' is federal "
                "employee reclassification to at-will, replacing 'Schedule F'. "
                "Interpret all entities in their geopolitical/institutional context. "
                "If no relevant results are found, say so clearly."
            ),
        },
        {"role": "user", "content": query},
    ]
    try:
        response = client.chat.completions.create(
            model=_MODEL_ID,
            messages=messages,
        )

        description = response.choices[0].message.content or ""

        # Perplexity may include citations in the response object
        source = ""
        citations: list[str] = []
        if hasattr(response, "citations") and response.citations:
            citations = list(response.citations)
            source = citations[0] if citations else ""

        return {
            "query": query,
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "description": description.strip(),
            "source": source,
            "status": "verified" if description.strip() else "unverified",
            "citations": citations,
        }

    except Exception as exc:  # noqa: BLE001
        err_msg = str(exc).lower()
        # Retry on rate-limit / resource-exhausted errors
        if ("429" in err_msg or "rate" in err_msg) and _retries < _MAX_RETRIES:
            wait = _BASE_BACKOFF * (2 ** _retries)
            logger.info("Rate-limited on %r – retrying in %ss", query, wait)
            time.sleep(wait)
            return _verify_single(client, query, _retries=_retries + 1)
        logger.exception("Perplexity verification failed for %r", query)
        return _error_result(query, str(exc))


def _error_result(query: str, message: str) -> dict:
    """Return a standard error-result dict."""
    return {
        "query": query,
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "description": f"Verification error: {message}",
        "source": "",
        "status": "error",
        "citations": [],
    }
