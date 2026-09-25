---
title: LLM wiki pattern (Karpathy)
slug: llm-wiki-pattern
level: 3
parent: index.md
related: [llms-txt.md, agent-skills-progressive-disclosure.md, obsidian-and-renderers.md]
tags: [progressive-disclosure, wiki, pattern]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M1, M2, M7]
license: n/a (pattern described in a public gist)
maturity: emerging
inspectability: high
sources:
  - title: llm-wiki (Andrej Karpathy, GitHub gist)
    url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    accessed: 2026-09-25
  - title: How to Build Karpathy's LLM Wiki (Starmorph blog; secondary)
    url: https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide
    accessed: 2026-09-25
---

# LLM wiki pattern (Karpathy)

> **TL;DR** Raw sources stay immutable. An LLM maintains a wiki of interlinked Markdown pages from them, guided by a schema file, with an `index.md` catalog and an append-only `log.md`, and runs ingest, query and lint operations. This is almost exactly gentext's shape. Adopt the index/log/lint ideas, but keep the human ratification gate that the gist leaves light.

## What it is
Karpathy's gist (secondary sources date it April 2026) describes three layers: **raw sources** (immutable), **the wiki** (LLM-written Markdown pages: entities, concepts, syntheses) and **the schema** (a `CLAUDE.md`-style file of conventions). Two special files are **`index.md`**, a catalog of every page with one-line summaries, and **`log.md`**, an append-only record of ingests, queries and maintenance. The operations are **ingest** (read a source, write or update pages and cross-links), **query** (answer from the wiki and file useful answers back as pages) and **lint** (find contradictions, stale claims, orphans and missing links). The gist says the index "works surprisingly well" at about 100 sources and hundreds of pages without embeddings, and that local BM25/vector tools are optional add-ons ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), accessed 2026-09-25).

## Why it matters for gentext
| LLM wiki | gentext |
|---|---|
| `raw/` | `projects/` (local, confidential; DR-0004) |
| wiki pages | `library/` chunks + registries |
| schema file | `AGENTS.md` + pydantic/LinkML schema |
| ingest | M0 + M1 (candidates, human-promoted) |
| lint | M7 checks on the library itself (orphans, stale facts, alias collisions) |
| `log.md` | an audit log of promotions, edits harvested from Docs, retrieval runs |

It is independent evidence that index-first navigation is viable at our scale.

## Strengths
- No infrastructure, with every artifact diffable.
- Lint as a first-class operation fits the defect catalogue in DR-0002.

## Weaknesses / risks
- The gist lets the LLM write pages directly. Our truthfulness rules require human promotion and provenance, so the LLM proposes and a human disposes (the same rule graph-keeper follows).
- The wiki is synthesis-oriented. We need *reusable prose* with length variants, which is a stricter unit than a wiki page.

## Verdict rationale
Adopt the pattern (index, log, lint, schema file), with our ratification gate added.

Up: [knowledge representation](index.md)
