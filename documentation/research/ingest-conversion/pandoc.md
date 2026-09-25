---
title: pandoc
slug: pandoc
level: 3
parent: index.md
related: [converter-comparison.md, docling.md, mammoth.md, heading-chunking.md]
tags: [docx, markdown, converter, cli, ast]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M0, M1, M9]
license: GPL-2.0-or-later
maturity: mature
inspectability: high
sources:
  - title: Pandoc User's Guide (--track-changes)
    url: https://pandoc.org/MANUAL.html
    accessed: 2026-09-25
  - title: pandoc releases (3.11, 2026-08-29)
    url: https://github.com/jgm/pandoc/releases
    accessed: 2026-09-25
  - title: pypandoc-binary on PyPI (1.17, bundles pandoc 3.9)
    url: https://pypi.org/project/pypandoc-binary/
    accessed: 2026-09-25
---

# pandoc

> **TL;DR** **Adopt** as the M0 DOCX→Markdown converter. It is deterministic, fast, and ships as a single binary. Its JSON AST is fully inspectable, and it is the only tool we tested that keeps Word comments and suggestions. Use `-f docx+styles --track-changes=all` with a Lua filter for adapt-rfp-specific cleanup.

## What it is
A universal document converter written in Haskell. It reads DOCX into an AST and writes GFM, CommonMark, HTML, JSON and others. Lua filters can transform the AST in between.

## Why it matters for adapt-rfp
- **Structure:** Word `Heading N` styles become `#…######`. With the `styles` extension, other paragraph styles (e.g. Google's `Title`, `Subtitle`) are kept as `custom-style` divs, so a filter can turn them into tab or section boundaries. *(Behaviour observed on the pilot. The extension text was not located in the fetched manual excerpt.)*
- **Comments and suggestions:** `--track-changes=all` wraps insertions, deletions and comments in spans with `insertion`, `deletion`, `comment-start` and `comment-end` classes (manual). These are useful context for M1 and the M9 harvest.
- **Tables:** GFM output falls back to raw HTML `<table>` when cells hold multiple blocks, so nothing is lost. The trade-off is less readable Markdown.
- **Media:** `--extract-media=DIR` writes images to files, which the manifest can hash.

## How it would fit
`adapt-rfp ingest file.docx` → `pandoc -f docx+styles --track-changes=all -t json` → Lua/Python pass (drop the TOC and empty headings, merge split headings, strip inline formatting from headings, mark tab boundaries) → `gfm` Markdown + manifest entry (sha256 of the source, pandoc version). Keep the JSON as the derived intermediate for M1.

## Strengths
- About 0.7 s for a 15k-word document. No models, no network.
- Available in the `uv` world via `pypandoc-binary` (MIT wrapper), so no system package is needed.
- The same tool can write DOCX back out for M9 or submission drafts.

## Weaknesses / risks
- GPL licence. That is fine as a CLI subprocess, but think before linking it into anything distributed.
- No layout or PDF input (pandoc cannot read PDF).
- Heading hygiene (split and empty headings) is our job.

## Verdict rationale
It has the best information retention and the most inspectable intermediate of anything we tried, at the lowest operational cost.

Up: [index.md](index.md)
