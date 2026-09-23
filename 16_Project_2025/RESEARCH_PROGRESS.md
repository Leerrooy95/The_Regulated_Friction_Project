# Project 2025 Mapping — Research Progress Checkpoint

**Purpose of this file**: This is a resumability checkpoint, not a finished deliverable. If this work gets interrupted (session ends, usage limit, etc.), a fresh session should read this file first, then `project_2025_mapping.csv`, to see exactly what is done, what is in progress, and what is left — without redoing completed chapters or re-researching from scratch.

**How to resume**: Open `project_2025_mapping.csv`, find the chapters marked `PENDING` below, and continue the same methodology (see "Methodology" section) starting from the first `PENDING` chapter. Update this file's status table and the "Session Log" at the bottom after every batch of chapters completed, then commit + push both files together.

---

## Why this file exists (context for a resuming session)

The original `project_2025_mapping.csv` (v1) only checked Project 2025 chapter directives against events already documented inside this repository's own `_AI_CONTEXT_INDEX/` corpus. That produced a lot of honest "NO REPO MATCH" rows for chapters this repo was never built to track (Education, EPA, HHS, Energy, etc.).

The repo owner then ran independent web-research passes on three of those chapters (Ch.12 Energy, Ch.13 EPA, Ch.14 HHS) and found something the repo-only pass missed: **several Project 2025 directives were attempted, and then blocked, reversed, or left contested by courts/litigation** — not just "implemented" or "no match." That is a third outcome category the original methodology didn't have a slot for. This surfaced a new verification-status value:

- `ATTEMPTED — BLOCKED/REVERSED` — the administration took the action the chapter called for, and a court (or other check) blocked, vacated, enjoined, or reversed it, in whole or part, as of the source's research date.

This file tracks finishing that same web-research pass (methodology below) across the remaining chapters that still show `NO REPO MATCH` in the CSV, so the final CSV has three honest outcome buckets for every chapter: **executed**, **attempted-but-blocked**, or **no corresponding action found even after web research**.

---

## Methodology (apply identically to every remaining chapter)

For each chapter, using the chapter's directive text from `Project_2025_Mandate_for_Leadership_Chapter-by-Chapter_Policy.md` as the target:

1. Web-search for concrete actions taken by the named agency/official matching the directive, dated as precisely as possible.
2. **Explicitly search for the blindspot**: litigation, injunctions, vacaturs, congressional blocks, agency reversals, or walk-backs of any action found in step 1. An implemented policy that was later struck down is not the same as one that stuck — both need their own row.
3. Only include rows backed by identifiable, real sources (outlet name + approximate date). No fabricated citations.
4. Use verification statuses consistent with the existing convention:
   - `VERIFIED` — action confirmed by multiple/credible sources, not currently blocked
   - `ATTEMPTED — BLOCKED/REVERSED` — action taken, then blocked/vacated/enjoined/reversed (cite the court/mechanism)
   - `PARTIALLY VERIFIED` — action or pledge confirmed but outcome/completion is unresolved, forward-looking, or only partially executed
   - `NO REPO MATCH` → for chapters where even web research turns up nothing concrete, relabel as `NO MATCH FOUND (web-researched)` to distinguish "we checked the web and found nothing" from the original pass's "we only checked the repo."
5. Repo_Source_File column for new rows should read: `Ch.N — <Department> (<Author>) [web research — not repo corpus]`, matching the convention already used for Ch.12/13/14.
6. Append new rows to `project_2025_mapping.csv` (do not renumber/reorder existing rows — always append).
7. After finishing a chapter (or a batch), update the status table below and re-run the Python CSV validation (`csv.reader`, check column-count consistency) before committing.

---

## Chapter Status Tracker

| Chapter | Department | Status | Notes |
|---|---|---|---|
| Ch.1 | White House Office | DONE (v1, repo-only, adjacent) | Structural/loyalty chapter; unlikely to have a single discrete event even with web research — left as-is unless a resuming session finds something concrete |
| Ch.2 | Executive Office of the President (OMB) | DONE (v1, repo-only) | Vought/OMB — repo-sourced, adequate |
| Ch.3 | Central Personnel Agencies (Schedule F) | DONE (v1, repo-only) | Strongest match in the repo; no further work needed |
| Ch.4 | Department of Defense | DONE (v1, repo-only) | Hegseth purge covered; DEI/transgender/COVID-discharge sub-items still unmatched — low priority for a re-pass |
| Ch.5 | Department of Homeland Security | DONE (v1, repo-only) | Noem firing + SAVE Act covered |
| Ch.6 | Department of State | **PENDING** | Not yet web-researched |
| Ch.7 | Intelligence Community | **PENDING** | Not yet web-researched (Ratcliffe/CIA lead worth checking) |
| Ch.8 | Media Agencies (USAGM/CPB) | **PENDING** | Not yet web-researched |
| Ch.9 | USAID | DONE (v1, repo-only) | Strong match; no further work needed |
| Ch.10 | Department of Agriculture | **PENDING** | Not yet web-researched |
| Ch.11 | Department of Education | **PENDING** | Not yet web-researched — high priority, one of P2025's most consequential chapters |
| Ch.12 | Department of Energy | DONE (v2, web-researched) | Includes a confirmed ATTEMPTED — BLOCKED/REVERSED row (DOE grant terminations ruled unconstitutional) |
| Ch.13 | Environmental Protection Agency | DONE (v2, web-researched) | Endangerment finding repeal executed but under active litigation (unresolved, not yet blocked) |
| Ch.14 | Health and Human Services | DONE (v2, web-researched) | Includes a confirmed ATTEMPTED — BLOCKED/REVERSED row (mifepristone access restriction stayed by SCOTUS) |
| Ch.15 | Housing and Urban Development | **PENDING** | Not yet web-researched |
| Ch.16 | Department of the Interior | **PENDING** | Not yet web-researched |
| Ch.17 | Department of Justice | DONE (v1, repo-only) | Strong match; no further work needed |
| Ch.18 | Department of Labor | **PENDING** | Not yet web-researched |
| Ch.19 | Department of Transportation | **PENDING** | Not yet web-researched |
| Ch.20 | Department of Veterans Affairs | **PENDING** | Not yet web-researched |
| Ch.21 | Department of Commerce (NOAA) | **PENDING** | Not yet web-researched |
| Ch.22 | Department of the Treasury | **PENDING** | Not yet web-researched — note: tax-bracket legislation may overlap with H.R.1/"One Big Beautiful Bill Act" already found for Ch.14; check for a shared reference |
| Ch.23 | Export-Import Bank | **PENDING** | Not yet web-researched |
| Ch.24 | Federal Reserve | **PENDING** | Not yet web-researched |
| Ch.25 | Small Business Administration | **PENDING** | Not yet web-researched |
| Ch.26 | Trade | DONE (v1, repo-only) | Section 122/IEEPA covered; could add a web-researched blocked/reversed angle later (low priority) |
| Ch.27 | SEC & CFPB | **PENDING** | Not yet web-researched |
| Ch.28 | Federal Communications Commission | DONE (v1, repo-only) | Covered; could add a web-researched Section 230/TikTok-litigation angle later (low priority) |
| Ch.29 | Federal Election Commission | **PENDING** | Not yet web-researched |
| Ch.30 | Federal Trade Commission | **PENDING** | Not yet web-researched |

**Remaining chapter count as of this checkpoint: 15 pending** (Ch.6, 7, 8, 10, 11, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27, 29, 30 — 18 listed above as PENDING; count precisely from the table, not this line, if they diverge).

---

## Session Log

- **Session 1** (mapping v1): Built initial repo-only CSV (47 rows), Hit Rate doc, PR #197 opened.
- **Session 2** (mapping v2, this checkpoint): User identified the blocked/reversed blindspot and independently web-researched Ch.12, Ch.13, Ch.14 (added rows 49–63). This session merged that expanded CSV into the repo copy, added this checkpoint file, and is dispatching research passes for the remaining PENDING chapters. *(Update this line with what was actually completed before ending the session.)*

