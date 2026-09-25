---
title: mammoth (and python-docx)
slug: mammoth
level: 3
parent: index.md
related: [pandoc.md, markitdown.md]
tags: [docx, html, style-map]
status: draft
updated: 2026-09-25
kind: library
verdict: hold
fit: [M0]
license: BSD-2-Clause
maturity: mature
inspectability: high
sources:
  - title: python-mammoth README
    url: https://github.com/mwilliamson/python-mammoth
    accessed: 2026-09-25
  - title: mammoth on PyPI (1.12.2, 2026-09-12)
    url: https://pypi.org/project/mammoth/
    accessed: 2026-09-25
  - title: python-docx on PyPI (1.2.0, 2025-06-16, MIT)
    url: https://pypi.org/project/python-docx/
    accessed: 2026-09-25
---

# mammoth (and python-docx)

> **TL;DR** **Hold.** mammoth's explicit **style map** (`p[style-name='Title'] => h1:fresh`) is an elegant, inspectable way to map Word styles to semantic HTML. But its Markdown output is deprecated, and pandoc already does the same job with `docx+styles` and a filter. Keep python-docx or the stdlib `zipfile` for targeted XML probes (checkbox state, section breaks), not for conversion.

## What it is
- **mammoth:** DOCX → clean HTML driven by a user style map. It ignores visual formatting on purpose. Comments are off by default and enabled by mapping `comment-reference`. Images are inlined as base64 or written out, and table formatting is dropped. The README says Markdown support is deprecated and recommends HTML followed by a separate converter.
- **python-docx:** a reader/writer for the DOCX object model (paragraphs, runs, styles, tables). MIT. The last release was 2025-06-16, so maintenance is slow.

## Why it matters for adapt-rfp
- A checked-in style map file would document exactly how each source style becomes structure. That kind of transparency is what the inspectability lens asks for.
- MarkItDown uses mammoth internally, so its behaviour explains MarkItDown's output.

## Weaknesses / risks
- HTML → Markdown needs a second tool (markdownify etc.), which adds another lossy hop.
- Unmapped styles produce warnings, not structure.

## Verdict rationale
The idea is right but it duplicates pandoc. Borrow the concept: keep our pandoc Lua filter's style mapping as a small declarative table.

Up: [index.md](index.md)
