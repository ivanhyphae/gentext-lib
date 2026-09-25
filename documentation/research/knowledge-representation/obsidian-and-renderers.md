---
title: Obsidian, Bases/Dataview, Quartz, MkDocs/Zensical
slug: obsidian-and-renderers
level: 3
parent: index.md
related: [llm-wiki-pattern.md, frontmatter-schema-validation.md]
tags: [viewer, wikilinks, static-site, obsidian]
status: draft
updated: 2026-09-25
kind: product
verdict: trial
fit: [M2, M9]
license: Obsidian proprietary (free); Quartz MIT (unverified); Material for MkDocs MIT
maturity: mature
inspectability: high
sources:
  - title: Quartz 5 homepage
    url: https://quartz.jzhao.xyz/
    accessed: 2026-09-25
  - title: Dataview vs Datacore vs Obsidian Bases (Obsidian Rocks; secondary)
    url: https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/
    accessed: 2026-09-25
  - title: Material for MkDocs blog (maintenance mode announcement)
    url: https://squidfunk.github.io/mkdocs-material/blog/
    accessed: 2026-09-25
  - title: Zensical upcoming changes
    url: https://zensical.org/upcoming-changes/
    accessed: 2026-09-25
---

# Obsidian, Bases/Dataview, Quartz, MkDocs/Zensical

> **TL;DR** Trial Obsidian as an optional *viewer and editor* over `library/`, since it reads Markdown and YAML frontmatter natively. Bases gives no-code tables over properties. Use standard Markdown links, not `[[wikilinks]]`, so that GitHub, Claude and the generators all resolve them. Hold on a published site: Quartz 5 or Zensical only if colleagues need a browsable web view.

## What they are
- **Obsidian**: a local Markdown vault editor with backlinks and a graph view. Frontmatter appears as "properties".
- **Bases** (core plugin) vs **Dataview** (community plugin): Bases gives visual table views over YAML properties with no code. Dataview adds DQL and JavaScript queries and inline `key:: value` fields. Both read the same notes and can coexist ([obsidian.rocks](https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/), accessed 2026-09-25; secondary).
- **Quartz**: a static site generator for Obsidian-style vaults, with wikilinks, transclusions, backlinks, a graph view and full-text search. The homepage announces Quartz 5 with a date of 2026-09-20 ([quartz.jzhao.xyz](https://quartz.jzhao.xyz/), accessed 2026-09-25). v5 is days old, so expect churn.
- **Material for MkDocs** entered maintenance mode (announced 2025-11-05; 9.7.0 was the last feature release). New work moved to **Zensical**, from the same team, which reads `mkdocs.yml`. Critical fixes are reported to continue until 2027-05-05 (secondary sources; see [Zensical](https://zensical.org/upcoming-changes/), accessed 2026-09-25).

## Why it matters for adapt-rfp
Non-technical colleagues need to browse the library without git. Obsidian over a synced checkout gives them tables ("all `project-case` chunks, sensitivity, last_reviewed"), backlinks (which chunks cite `fact:…`) and a graph picture at no build cost.

## How it would fit
- The repo root, or `library/`, doubles as a vault. `.obsidian/` is gitignored, or only a shared minimal config is committed.
- A few committed `.base` views: chunks by type, stale facts, chunks awaiting review *(file format not examined)*.
- Editing in Obsidian is allowed, but validation (pre-commit/CI) still gates merges.
- Publishing, if ever: Quartz, or Zensical plus a custom frontmatter table. Never publish chunks marked `internal`.

## Strengths
- Zero conversion, so the canonical files are what people see.
- Bases and Dataview make frontmatter visibly useful, which motivates good metadata.

## Weaknesses / risks
- `[[wikilinks]]` are Obsidian dialect and break on GitHub and in plain tooling. Configure Obsidian to write relative Markdown links.
- Obsidian is proprietary, and sync between users is outside git (Obsidian Sync or git plugins). Concurrency is the DR-0005 weak spot.
- Generator churn: Quartz v5 is brand new, and MkDocs Material is winding down.

## Verdict rationale
Trial Obsidian as a viewer (cheap and reversible). Hold on static-site publishing until there is a reader who needs it.

Up: [knowledge representation](index.md)
