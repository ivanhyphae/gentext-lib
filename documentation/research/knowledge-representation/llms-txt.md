---
title: llms.txt
slug: llms-txt
level: 3
parent: index.md
related: [agent-skills-progressive-disclosure.md, llm-wiki-pattern.md, retrieval-design.md]
tags: [progressive-disclosure, convention, index]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M2, M8]
license: n/a (open proposal)
maturity: emerging
inspectability: high
sources:
  - title: The /llms.txt file (llmstxt.org)
    url: https://llmstxt.org/
    accessed: 2026-09-25
---

# llms.txt

> **TL;DR** llms.txt is a Markdown convention for an LLM-oriented index file: an H1, a blockquote summary, then H2 sections that list `[name](url): notes`. Adopt its *shape* for `library/index.md` and every type index. There is no need to publish it on the web.

## What it is
Jeremy Howard proposed llms.txt on 2024-09-03. The site lists a v2 update dated 2026-08-10 *(date as shown on the site; contents of v2 not reviewed in detail)*. The format, in order: an H1 with the project name (the only required element), a blockquote summary, optional prose, then zero or more H2 sections containing Markdown link lists of the form `[name](url): optional notes`. An `Optional` section, by convention, holds secondary material that can be skipped. Sites are also encouraged to serve `.md` versions of pages. The site reports that Mintlify, GitBook and others generate llms.txt automatically, and that major AI labs publish llms.txt files for their docs ([llmstxt.org](https://llmstxt.org/), accessed 2026-09-25).

## Why it matters for gentext
It is the smallest possible "level 0" of a progressive-disclosure wiki. It is readable by Claude, by humans, and by a 20-line generator. It also matches DR-0005's `library/index.md` → type index → chunk layout.

## How it would fit
- `gentext index --md` regenerates `library/index.md` and `library/<type>/index.md` from frontmatter (`title`, `summary`, `variants[].words`).
- Example entry: `- [UTCI microclimate modeling](method/utci-modeling.md): heat-exposure modeling method; variants 60/150/300 words`.
- An `## Optional` section lists deprecated or low-confidence chunks.

## Strengths
- Trivial to generate and diff, with no tooling lock-in.
- Serves as a readable table of contents for colleagues too.

## Weaknesses / risks
- It is a convention, not a validated standard, and it has no metadata beyond link notes. Filtering still needs the frontmatter and the derived index.
- A flat index gets long past a few hundred entries. That is why we split it by type.

## Verdict rationale
Adopt, because it costs almost nothing, fits every access path (Claude Code, Claude web via MCP, humans), and keeps the root index honest.

Up: [knowledge representation](index.md)
