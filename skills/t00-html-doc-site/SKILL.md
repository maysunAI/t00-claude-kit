---
name: t00-html-doc-site
description: "Use whenever you make or change an HTML help page, manual, tutorial, guide or step list: split it into a multi-page mini site (left menu + site search + previous/next hit in the page + previous/next page) instead of one long page. Triggers: make html help, write a manual, beginner guide, tutorial page, turn the docs into a web page."
metadata:
  version: 1.0.0
  created: 2026-10-28
---

# Multi-page documentation site

## When
Any HTML meant to be read (help, manual, tutorial, beginner guide, startup steps, research report). Do not hand-write one long page.
Exceptions: tool UIs (forms, dashboards, app pages) are not documents; a one-screen start page may be a single page but still needs a "back" link.

## How (3 steps, do not hand-write the HTML skeleton)
1. Write a UTF-8 source file:
   ```
   @title Site title
   @back /|Back to tool        (optional; url|text)
   ## First page title
   <p>HTML fragment</p>
   ## Second page title
   ```
   Each `##` is one page. One page, one topic, one to three screens; split if longer.
2. Run a generator script on the source file and an output folder (a short script that renders a template; any static-site approach works).
3. Open index.html and click through it with browser automation: left menu, search for a word, click a result, previous/next hit, previous/next page, and the menu collapse at 390 px width.

## The generated site should have
- a fixed left menu with the current page highlighted, collapsible on phones, light/dark aware
- site-wide search (press `/`), results listing page and snippet, hit highlighting, floating previous / next hit
- previous page / next page at the bottom of each page
- plain static relative links so it opens by double-click and works on any host

## Writing for a total beginner
- page titles as a question or action ("How to start", "What is a magnet link")
- the first sentence says what problem the page solves; steps in an ordered list, one action per step
- put English keywords in parentheses to help search
- put known limits and untested items on their own page
