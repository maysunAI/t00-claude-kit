# Permissions: what to allow, ask and deny

Official reference: [Configure permissions](https://code.claude.com/docs/en/permissions) and [Settings](https://code.claude.com/docs/en/settings). Put the rules in `.claude/settings.json` (shared) or `.claude/settings.local.json` (only you).

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Bash(git status)",
      "Bash(git diff *)"
    ],
    "ask": [
      "Bash(git push *)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  }
}
```

Habits that worked for us:
1. Allow read-only commands you run all day (status, diff, lint, tests); `/fewer-permission-prompts` can propose a list from your own transcripts.
2. Keep outward-facing actions on "ask": pushing, posting, sending mail, deploying, deleting data.
3. Deny reading secret files. Claude then cannot paste a token into a document by accident. A rule in CLAUDE.md is only a request; a `deny` rule is enforced.
4. Review `.claude/settings.local.json` now and then: every "Yes, and don't ask again" you clicked is saved there as an allow rule.
5. Settings are strict JSON: no comments, no trailing commas. A broken file is reported at the next start; run `claude doctor` to see what was dropped.
