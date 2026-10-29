---
name: t00-skill-writer
description: "Fixed procedure for writing a new skill or improving one: decide whether it is worth writing, how to split it (entry SKILL.md plus on-demand sub-files), how to write trigger words in the description, keep it small, validate, and package a zip for the claude.ai web/mobile app. Use when the user says: write a skill, turn this into a skill, learn the official skills then write ours, the skill is too big, the skill did not trigger."
metadata:
  version: 1.0.0
  created: 2026-10-04
  source: https://github.com/anthropics/skills (structure of skill-creator, frontend-design, webapp-testing, claude-api)
---

# Writing a skill

## 0. Is it worth writing?
Worth it: the same kind of task done 2+ times with fixed steps; a pitfall that can become a checklist; a reusable script.
Not worth it: one-off work; something already covered by rules or commands; a pile of links (links cannot be searched or triggered, so put the key points into the body).
Take only what is useful from official skills; do not copy a whole package.

## 1. Structure (learned from the official skills)
- One skill = one folder, entry file SKILL.md, front matter has `name` (same as the folder) and `description`.
- Simple: a single SKILL.md. Complex: the entry holds routing and key rules only; details go to a references/ folder, repeatable actions to scripts/, and the body says when to read which file. (An official skill with a 100 KB entry is the counter-example: it loads fully on every trigger.)
- Treat scripts as black boxes: the body says "run --help first, do not read the source".

## 2. Writing the description (it decides whether the skill triggers)
- One paragraph: what it does plus the words users really say.
- Also say when NOT to trigger.
- Keep it under about 600 characters.

## 3. Size
Entry SKILL.md target <= 5 KB, hard limit 12 KB; split into references beyond that.

## 4. Validate and package
- Check: name equals folder, description present and contains trigger words, size, referenced files exist, no secret-looking strings.
- For the phone app: zip the folder and upload it in claude.ai under Settings, Capabilities, Skills. Scripts cannot run on the phone, so SKILL.md must stand on its own.

## 5. After writing
1. Run a real task and see whether it triggers as intended.
2. Note the skill name in the project docs.
3. Never put keys or passwords in a skill (paths yes, values no).
