# Where things live (Claude Code file locations)

Checked against the official docs on 2026-10-29: [Settings](https://code.claude.com/docs/en/settings) and [Memory](https://code.claude.com/docs/en/memory). Windows: `~` means `%USERPROFILE%`.

| What | User (all projects) | Project (shared, commit it) | Project (only you) |
|---|---|---|---|
| Settings and permissions | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| Instructions (CLAUDE.md) | `~/.claude/CLAUDE.md` | `./CLAUDE.md` or `./.claude/CLAUDE.md` | `./CLAUDE.local.md` (gitignore it) |
| Topic rules | `~/.claude/rules/*.md` | `.claude/rules/*.md` | - |
| Skills | `~/.claude/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` | - |
| Slash commands | `~/.claude/commands/<name>.md` | `.claude/commands/<name>.md` | - |
| Auto memory (Claude writes it) | `~/.claude/projects/<project>/memory/` | - | - |

Notes:
- More specific settings win: managed > command line > project local > project shared > user. Lists such as `permissions.allow` are merged, not replaced.
- CLAUDE.md files in the folders above your working directory load at launch; files in sub-folders load when Claude touches a file there.
- Custom commands have been merged into skills: for new work prefer `.claude/skills/<name>/SKILL.md`; `.claude/commands/<name>.md` still works.
- The auto-memory folder is per git repository and machine-local (not shared across machines). Change it with the `autoMemoryDirectory` setting.
- Run `/status` to see which settings files loaded, `/memory` to browse memory files, `/doctor` to audit CLAUDE.md, rules, skills and commands.

## Where we keep things in our own workspace (example, adapt it)

- One workspace root `T00/` holds dozens of projects `PJxx_name/`. The root `CLAUDE.md` imports a shared rules file with `@AI00_Common/CLAUDE.md`.
- Shared rules: `AI00_Common/rules/R##_*.md`, one topic per file; the CLAUDE.md lists when to read which one.
- Skills the whole workspace uses: `T00/.claude/skills/`. Commands: `AI00_Common/.claude/commands/`.
- Each project has its own `CLAUDE.md` (project rules, one line per change: what was done, what was not tested), `OVERVIEW.md`, `REQUIREMENTS.md`.
- Secrets live only in `PJxx/secrets/*.env` (gitignored); documents say "see secrets/xxx.env" and never contain the value.
- Screenshots and one-off files: a single `temp/` folder, or the project's own folder when they document that project (always full absolute paths).
