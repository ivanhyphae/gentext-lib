---
title: Microsoft MarkItDown
slug: markitdown
level: 3
parent: index.md
related: [converter-comparison.md, mammoth.md, pandoc.md]
tags: [docx, pdf, markdown, converter, mcp]
status: draft
updated: 2026-09-25
kind: library
verdict: hold
fit: [M0]
license: MIT
maturity: emerging
inspectability: medium
sources:
  - title: microsoft/markitdown on GitHub
    url: https://github.com/microsoft/markitdown
    accessed: 2026-09-25
  - title: markitdown on PyPI (0.1.8, 2026-09-21)
    url: https://pypi.org/project/markitdown/
    accessed: 2026-09-25
---

# Microsoft MarkItDown

> **TL;DR** **Hold** as the canonical converter, but it is fine for quick previews. It makes one-line "anything to Markdown" conversions for LLM input. DOCX headings survive, but comments are dropped, tables are forced into pipe tables, and PDF output is flat text with no headings or tables.

## What it is
A Python utility and CLI from Microsoft (MIT) that converts PDF, DOCX, PPTX, XLSX, HTML, images, audio and more to Markdown. It also ships an MCP server (`markitdown-mcp`), opt-in plugins (e.g. LLM-vision OCR), and optional Azure Document Intelligence for PDFs (repo, accessed 2026-09-25). DOCX goes through mammoth to HTML and then to Markdown.

## Why it matters for adapt-rfp
It is the fastest way to give Claude a readable view of a file, and the MCP server could be handy in Claude Desktop sessions.

## Pilot results
- Ambrose DOCX: 2.2 s, about the same heading counts as pandoc. The TOC is emitted as `#` lines. Pipe tables flatten multi-paragraph cells. Comments are lost.
- Guidelines PDF: 7.5 s. **Zero headings, zero tables**; the score-overview table became loose lines.
- Urban Greening form: checkbox glyphs are kept, and there are no headings (as with every tool).

## Weaknesses / risks
- No structured intermediate (no AST or JSON), so there is nothing to audit beyond the Markdown.
- Pre-1.0 API. The docs warn it performs I/O with process privileges, so sanitize untrusted inputs.

## Verdict rationale
Convenient, but it loses information that M0 must keep (comments, table fidelity, PDF structure). pandoc and Docling each beat it on the axis they are strong on.

Up: [index.md](index.md)
