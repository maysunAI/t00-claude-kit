---
description: After a deploy, verify the live site (hash, status codes, browser click-through) instead of trusting local tests
---

Verify the deploy of the change we just made. Do not mark it done until each step has evidence.

1. Syntax-check what you uploaded before uploading it (for example `node --check` on every JS file, and on each inline script block of an HTML file).
2. Back up the live files first; after upload compare a hash of the live file with the local one.
3. Request every changed URL on the real domain and expect HTTP 200, including images and scripts. If one fails, check its sibling files too.
4. Open the live page in a browser tool at two widths (about 390 and 1400 px): no horizontal overflow, no console errors, click the main buttons of the feature.
5. Never touch real user data while testing: create your own test rows and delete only those.
6. Write the result in the project's notes: what was deployed, what was verified, what was NOT tested (real devices, mobile, long flows).
