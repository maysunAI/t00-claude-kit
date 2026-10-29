---
name: t00-change-checklist
description: "Read before writing or changing code, or before answering 'do we have feature X?'. Split the request into a numbered list (missed items are the most common failure), read ALL related code and design notes first, then check each item off and verify it live. Use when the user says: build, change, add a feature, do we have, you missed something."
metadata:
  version: 1.0.0
  created: 2026-10-29
---

# Change checklist: before and after touching code

## Why this exists (real incidents, 2026-10-28/29)
- Incident 1: asked "does project A have review history?", the assistant ran one keyword search and answered "no, we need to add it". The project already had a review_history table, several forgetting curves and 263 card packs. Cause: it concluded from a fragment.
- Incident 2: a "review filter" built on 10/28 disappeared when the review screen was rewritten; the old entry point became dead code. Cause: no list of old features to compare against.
- Incident 3: one request contained several small asks and the assistant merged them into one answer, dropping one.

## What peers do (web search, 2026-10-29)
- Spec-driven development: GitHub Spec Kit (Specify, Plan, Tasks, Implement) and AWS Kiro (requirements.md / design.md / tasks.md, acceptance criteria in EARS syntax). Implicit requirements become checkable clauses.
- Japanese dev community (Zenn etc.): AGENTS.md / CLAUDE.md as the AI's "external brain" (layout, conventions, exact test commands); NOTES.md for progress on long tasks.
- No measured data on "how often AI drops requirements" was found. These are practices, not evidence.

## Do this every time
1. Split: turn the user's message into numbered items R1..Rn, one action per line, never merged.
2. Read: before changing a feature read (a) all related functions in the file, (b) the project's CLAUDE.md / OVERVIEW / REQUIREMENTS entries about it, (c) grep every call site (is it dead code?). To answer "do we have X?" list the files and lines you actually read; for a negative answer search at least two synonyms.
3. Old-feature list: before rewriting or replacing a screen, list what the old one did. The new one must map each item; anything dropped is stated explicitly.
4. Change in small steps; run a syntax check (for example node --check) after each.
5. Verify: before delivering, mark R1..Rn as done / pending / failed with evidence (command output, screenshot path). Anything you did not click through is "not tested".
6. Live check: after deploy, compare the file hash with local and click the key buttons with a browser automation tool.
7. Record: one line in the project's CLAUDE.md: what was done, what was not tested.
