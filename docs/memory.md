# Memory: what to put where

Official reference: [How Claude remembers your project](https://code.claude.com/docs/en/memory).

Two systems, both loaded at the start of every session and treated as context, not as enforced configuration:

1. CLAUDE.md files: instructions you write (build and test commands, conventions, layout, "always / never" rules). Keep them short; move multi-step procedures into a skill.
2. Auto memory: notes Claude writes itself from your corrections and preferences, in `~/.claude/projects/<project>/memory/`. Plain markdown; browse, edit or delete it with `/memory`.

## The format we use for memory files

One fact per file, with front matter, and one index line per file in `MEMORY.md`:

```markdown
---
name: verify-production-not-just-local
description: After deploying, curl the real URL; a passing local test does not prove the live site works
metadata:
  type: feedback
---

After changing a binary asset (image etc.) always curl the production URL and expect 200.
**Why:** a page passed local browser tests but the live image 404ed.
**How to apply:** after every deploy, request each changed file on the real domain; if one 404s, check its sibling files too.
```

`MEMORY.md` (the index, no front matter):

```markdown
- [Verify production](verify-production-not-just-local.md) - curl the real URL after deploy, local tests are not enough
```

Types we use: `user` (who the user is), `feedback` (how to work, with the reason), `project` (ongoing facts not visible in the code), `reference` (where to find things).

Rules of thumb:
- Do not store what the repository already records (code layout, git history, CLAUDE.md contents).
- Store the reason (**Why**) with every feedback item, so the rule can be judged in a new situation.
- Update or delete a memory that turned out wrong instead of adding a contradicting one.
- Never store secrets in memory files.
