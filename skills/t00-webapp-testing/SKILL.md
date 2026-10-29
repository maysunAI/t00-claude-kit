---
name: t00-webapp-testing
description: "Fixed way to verify that a web change really works live: two viewports (phone 392 / desktop 1400) for horizontal overflow, console JS errors, click through the key flow after login, save screenshots into the project folder. Use when the user says: test it, verify, it looks wrong on mobile, check it live, Playwright, screenshot. Also curl every binary asset (images) after deploying."
metadata:
  version: 1.0.0
  created: 2026-10-04
  source: https://github.com/anthropics/skills/tree/main/skills/webapp-testing
---

# Web verification (live first)

## What to measure at each viewport
- scrollWidth vs clientWidth (scrollWidth > clientWidth means horizontal overflow)
- number of console errors and the first five
- a screenshot saved to a full absolute path inside the project folder

## Rules (each one is a past mistake)
1. Screenshot paths must be full absolute paths in the project's own folder, never relative, never the repo root.
2. For dynamic pages wait for networkidle before reading the DOM.
3. Never touch real user data: create your own test rows and delete only those. Never run an unfiltered DELETE on a table (a real incident wiped 44 user-added links).
4. Passing locally does not mean it works live: after deploy run the check against the real URL; for new or changed binary assets curl each key URL and expect 200.
5. Real-device behaviour (drag feel, microphone, orientation lock) cannot be tested by a script: report "not tested: ..." instead of "verified".
6. A shared browser may be in use by another session: open a new tab and close it when done.

## When you need interaction
Write a small Playwright script: launch(headless=True), new_page(viewport=...), goto, wait_for_load_state('networkidle'), then select by id or text.
