---
title: Apps Script tab-aware exporter
slug: apps-script-tab-export
level: 3
parent: index.md
related: [google-docs-tabs.md, pandoc.md]
tags: [google-docs, apps-script, tabs, export]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M0, M9]
license: n/a (our own script)
maturity: emerging
inspectability: medium
sources:
  - title: Apps Script, work with tabs
    url: https://developers.google.com/apps-script/guides/docs/tabs
    accessed: 2026-09-25
  - title: Google Docs Tab Exporter gist (per-tab export URL + HTML→MD)
    url: https://gist.github.com/alxzndr1/710ede4f71ba9a759cebc4b97454555a
    accessed: 2026-09-25
  - title: Exporting individual tabs from Google Docs as PDFs (Google Workspace DevRel)
    url: https://dev.to/googleworkspace/exporting-individual-tabs-from-google-docs-as-pdfs-2903
    accessed: 2026-09-25
---

# Apps Script tab-aware exporter

> **TL;DR** **Trial.** This is a small bound or standalone Apps Script that walks `getTabs()`/`getChildTabs()` and writes **one JSON (or Markdown) file per tab** to a Drive folder. Each file carries the tab id, title, path and paragraph heading levels. It is the lowest-friction way for non-developers to hand adapt-rfp a tab-faithful snapshot without an OAuth app.

## What it is
`DocumentApp` exposes `Document.getTabs()`, `Tab.getChildTabs()` and `Tab.asDocumentTab().getBody()` (Apps Script docs, updated 2026-09-03). Walking each body's paragraphs gives `getHeading()` (e.g. `HEADING2`), text and list nesting. That is enough for heading-based segmentation. Community exporters instead fetch `…/export?format=html&tab={tabId}` and convert the HTML. That URL parameter is **undocumented** and "could change" (Google DevRel post, 2025-10-28).

## Why it matters for adapt-rfp
- It keeps the one thing DOCX export loses, **tab identity**, so manifest locators can be `gdoc:{docId}#tab={tabId}`.
- The team works in Google Docs, and a custom menu item ("Export to adapt-rfp") fits their workflow.

## How it would fit
Recommended output: `{docId, revisionId?, exportedAt, tabs:[{tabId, title, path, paragraphs:[{heading, text, listLevel}]}]}` as JSON, not home-made Markdown. adapt-rfp then renders Markdown deterministically in Python. The JSON is the inspectable artifact that gets committed to the derived area.

## Weaknesses / risks
- The script lives in Google, outside git. Keep its source in the repo and push it with `clasp`.
- Apps Script quotas and runtime limits apply to large documents *(limits not re-checked)*.
- Tables, images and comments need extra code (comments come from the Drive API).

## Verdict rationale
It is cheap and gives us tab ids. Compare it against Docs API route A in [google-docs-tabs.md](google-docs-tabs.md), and keep whichever the team will actually run.

Up: [index.md](index.md)
