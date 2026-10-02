# 16_Project_2025 — Project 2025 Policy-Mapping

**What this folder answers**: of the 30 chapter directives in Project 2025's *Mandate for Leadership*, how many were actually executed in 2025–2026, how many were attempted and then blocked or reversed, how many produced the *opposite* of what the chapter asked for, and how many simply never happened?

**Current status**: complete. All 30 chapters researched, 125 dated and sourced findings, four correction rounds behind it (two external reviews plus two self-caught follow-ups — see `RESEARCH_PROGRESS.md` for the full history if you want it).

---

## Start here, by what you want to do

| I want to... | Open this |
|---|---|
| See the headline numbers and a one-line verdict per chapter | **`00_Project_2025_Hit_Rate.md`** |
| Look up, sort, or filter the underlying findings | **`project_2025_mapping.csv`** |
| Read the original Project 2025 chapter summaries this was built from | `Project_2025_Mandate_for_Leadership_Chapter-by-Chapter_Policy.md` |
| Read general background on Project 2025 itself (origins, status, four pillars) | `Project_2025_Overview_of_the_Heritage_Foundation.md` |
| Understand the methodology, or pick up unfinished research | `RESEARCH_PROGRESS.md` |
| See exactly which rows were removed in cleanup, and why | `_pass1_superseded_rows_removed.csv` |
| See the follow-up analysis of Heritage's next family-policy report (SR323, Jan 2026) | **`Heritage_2026_Successor_Documents/README.md`** |

Most people only need the first two.

Note: `Heritage_2026_Successor_Documents/` tracks a separate, later Heritage Foundation report (Special Report No. 323, Jan 2026) — not a continuation of the Mandate for Leadership's 30 chapters tracked above. It lives here because it's the same institution's next major policy document and uses the same method.

---

## The headline numbers

As of the current version, across all 30 chapters:

| Outcome | Rows | Meaning |
|---|---:|---|
| `VERIFIED` | 55 | Confirmed, not currently blocked or reversed |
| `PARTIALLY VERIFIED` | 31 | Confirmed but unresolved, forward-looking, or only partially executed |
| `ATTEMPTED — BLOCKED/REVERSED` | 26 | Actually attempted, then blocked by a court, Congress, or public backlash |
| `AFFIRMATIVELY CONTRADICTED` | 8 | The real-world outcome was the *opposite* of the chapter's ask — not just unmet, inverted |
| `NO MATCH FOUND` | 5 | Genuinely nothing found after real research |
| **Total** | **125** | |

Read that as: **21% of tracked sub-directives were fought to a standstill**, and another **6% produced the reverse of what the chapter asked for**. Only 4% are honest blanks. Full chapter-by-chapter detail and the reasoning behind every number is in `00_Project_2025_Hit_Rate.md`.

This is **not** the same question independent trackers like the Center for Progressive Reform/Governing for Impact (~53%) or project2025.observer (~48%) answer — they measure what fraction of the full Project 2025 agenda has been implemented, across far more actions than this file tracks. This folder instead focuses on the *texture* behind specific directives: which attempts were contested, how, by whom, and which produced an outcome nobody asked for.

---

## How `project_2025_mapping.csv` is laid out

One row per chapter sub-directive with a dated, sourced finding. Columns:

| Column | Contents |
|---|---|
| `Chapter_Num` | Integer 1–30, used to sort the file — always sorted by this, so row order has no other meaning |
| `Date` | When the event happened (or a range, for multi-stage events) |
| `Chapter` | Chapter number, department name, and original Project 2025 author(s) |
| `Directive` | The specific sub-directive this row addresses (chapters have several) |
| `Repo_Event` | What actually happened — dense, factual, named officials/courts/dollar figures |
| `Verification_Status` | One of the five outcomes above, plus a short source citation |
| `Why_No_Match` | Filled in only for the 5 genuine `NO MATCH FOUND` rows, explaining why nothing turned up (needed Congress and didn't pass, achieved informally via a different mechanism, not addressed either way, or unknowable from public sources) |
| `Pass` | `1` = sourced from this repo's own `_AI_CONTEXT_INDEX/` corpus; `2` = from live web research done specifically for this file |
| `Repo_Source_File` | Citation detail — which repo file, or which outlets, back this row |

Every `Repo_Event` and `Verification_Status` is backed by real, named, dated sources — never fabricated. Rows sourced from live web research are explicitly marked `[web research — not repo corpus]` in `Repo_Source_File` so it's always clear which claims trace back to this repository's existing documentation versus independent research done for this analysis.

---

## Method, briefly

1. **Pass 1** checked each chapter directive against events already documented in this repo's `_AI_CONTEXT_INDEX/`. Chapters with nothing there got flagged for follow-up.
2. **Pass 2** did full live web research on every flagged chapter, explicitly searching not just for "was this done" but for the blindspot a repo-only pass can't see: directives that were *attempted and then blocked or reversed*.
3. **Pass 3** was cleanup after review — both external (an independent model audit, a GitHub Copilot PR review) and self-caught. It added the `AFFIRMATIVELY CONTRADICTED` category, removed 21 stale duplicate placeholder rows left behind by how Pass 1/2 were built, fixed two rows where a status update wasn't matched by an update to the surrounding text, corrected two factual errors that surfaced along the way, and reverted one retag that turned out not to meet this file's own stated definition of its category once someone checked it against the definition rather than against "does it match the other rows."

Full round-by-round detail — including the two mistakes that were caught and fixed in public — is in `00_Project_2025_Hit_Rate.md`'s Correction Log and `RESEARCH_PROGRESS.md`'s Session Log. Nothing here was swept under the rug; the corrections are as visible as the findings.

---

## If you want to extend this

`RESEARCH_PROGRESS.md` has the full methodology, including the exact rules for adding a new row (what counts as each status, how to cite sources, and a rule added specifically to stop the duplicate-placeholder bug from recurring). The short version: web-search for the directive, explicitly check for a blocked/reversed or contradicted outcome before concluding "verified," cite real sources, and if you're updating an existing row's status, update its `Date` and `Repo_Event` text in the same edit — don't leave them saying something the new status contradicts.
