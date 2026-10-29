---
name: t00-acceptance-criteria
description: "Read when writing acceptance criteria (what counts as done and correct). Write testable yes/no clauses in Given-When-Then, about 5 per feature, covering the normal path, errors, edge cases and permissions, and say how each is verified (automated test / browser automation / human eyes / real device). Applies to new features and isolation rules such as 'user A must not see user B data'."
metadata:
  version: 1.0.0
  created: 2026-10-05
---

# Writing acceptance criteria

## Industry practice (web search, 2026-10-05)
- Good criteria are clear, specific and testable: two people reading them reach the same pass/fail verdict.
- Given-When-Then: Given = state before, When = user action, Then = observable change.
- Every clause must answer "how do I test this?". Rewrite "should be fast" as "opens in under 3 s on a normal network".
- About 5 per group; more means several features, so split them.
- Cover the normal path, error states, edge cases and permission rules. Each clause is independent with a clear yes/no. Describe the outcome, not the implementation.

## Our additions (mistakes we made)
1. Add "verification" to each clause: automated test / Playwright at two viewports (392 and 1400) / human eyes / real device. If you cannot verify it, write "not verified".
2. For "A cannot see B" requirements (multi-user, language isolation) always write the reverse case: actually log in as B and try.
3. Make numbers concrete: no horizontal overflow means scrollWidth <= clientWidth; after deploy, curl each URL and expect 200.
4. Anything automatable goes into a test script kept in the project and re-run after each change.
5. Put the criteria in the project's REQUIREMENTS.md and mirror them in the tested / untested list in OVERVIEW.md.

## Template
```
Feature: <name>
Acceptance criteria (max 5):
1. Given <state> When <action> Then <result>   Verify: <automated / Playwright / eyes / device / not verified>
2. (error) Given ... When ... Then ...
3. (edge) ...
4. (permission) Given users A and B When B logs in Then B cannot see A's data   Verify: automated test with two sessions
```

## Example: multi-user app
1. Given user A has favourites When B logs in Then B's favourites are empty. Verify: automated.
2. Given B changes their own settings When A refreshes Then A's settings are unchanged. Verify: automated.
3. Given a shared group library When any member edits an item Then the history shows who, when, old and new value. Verify: automated.
4. Given the Japanese UI When any page opens Then the text has no Chinese-only characters and never redirects to the Chinese site. Verify: scripted text scrape plus a spot check.
5. Given a visitor who is not logged in When requesting another user's data endpoint Then the response is 401. Verify: automated.

## Sources
- https://nulab.com/learn/software-development/acceptance-criteria/
- https://www.parallelhq.com/blog/given-when-then-acceptance-criteria
- https://testomat.io/blog/clear-acceptance-criteria-for-user-stories-bdd-way/
