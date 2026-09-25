---
title: Converter comparison (hands-on on the pilot)
slug: converter-comparison
level: 2
parent: index.md
related: [pandoc.md, docling.md, markitdown.md, pymupdf4llm.md, pdfplumber.md, google-docs-tabs.md]
tags: [ingest, conversion, docx, pdf, benchmark]
status: draft
updated: 2026-09-25
---

# Converter comparison (hands-on on the pilot)

> **TL;DR** On the pilot DOCX, pandoc, MarkItDown and Docling recover the heading tree about equally well. pandoc is the only one that keeps comments and suggestions, and Docling is the only one that promotes the tab-like `Title` paragraphs to headings by default. On the guidelines PDF, pymupdf4llm and Docling both produce headings and a correct score table. MarkItDown's PDF output is flat text. The Appendix F rubric is bulleted prose, so `pdftotext` + regex is enough for M5.

## Setup

- Date: 2026-09-25, on the dev machine (Linux, CPU only). Tools ran in throwaway venvs under `/tmp/claude-1000/…/scratchpad`. Nothing was installed in the repo.
- Versions: pandoc 3.9 (via `pypandoc-binary` 1.17; upstream latest is 3.11), MarkItDown 0.1.8, Docling 2.130.0 / docling-core 2.99.0, pymupdf4llm 1.28.2, pdfplumber 0.11.10, poppler `pdftotext`.
- Inputs: `Ambrose Memorial Park EHCRP.docx` (about 15k words, 9 H1 / 15 H2 / 49 H3 / 47 H4 / 9 H5 paragraph styles, 7 `Title` paragraphs, 4 tables, 5 drawings, 7 comments, 11 section breaks); `2026 URBAN GREENING … CONCEPT PROPOSAL.docx` (about 2.2k words, **no paragraph styles**, 34 checkbox glyphs); `Round-2-Final-Guidelines.pdf` (58 pages, tagged PDF, produced by Word).
- Only counts and structural observations are recorded here, not source text (confidentiality, AGENTS.md).

## DOCX results (Ambrose)

| | pandoc → gfm | MarkItDown | Docling |
|---|---|---|---|
| Time | 0.7 s | 2.2 s | 4.9 s |
| Words out | 16.6k | 16.3k | 16.3k |
| Headings (#/##/###/####) | 8/15/44/47 (+H5) | 7/14/39/45 | 7 `#` (Title) + 9/15/43/47 shifted down one level |
| `Title` paragraphs | plain text; `docx+styles` → `custom-style="Title"` div | plain text | `TitleItem` → `#` |
| Tables | 2 as HTML `<table>` (multi-paragraph cells), rest pipe | all pipe tables (cells flattened) | 4 `TableItem`s, pipe in MD, full grid in JSON |
| Images | extracted to files (`--extract-media`) | 3 inline refs | 5 `PictureItem`s |
| Comments / suggestions | kept with `--track-changes=all` (7 comments, 1 deletion) | dropped | dropped *(not seen in output)* |
| Structured output | pandoc JSON AST | none | DoclingDocument JSON |

All three converters show the same source defects, and M0/M1 has to clean them up:
- The Google-inserted **table of contents** comes out as link lists (a blockquote in pandoc).
- Some **empty headings** (`# ` with no text).
- **One heading split over two heading paragraphs**, because the author pressed Enter inside a heading.
- **Direct formatting inside headings** (`**<u>…</u>**`), which has to be stripped before headings can be matched.

## DOCX results (Urban Greening form)

Every converter produced **zero headings**, because the document uses no heading styles. The checkboxes survive as ☐/☒ characters in all of them. They are text glyphs, not Word content controls (the file has 0 `w:sdt` and 0 `w14:checkbox` elements), so a checked/unchecked state parser only needs a regex. Segmentation here needs rules: numbered question patterns, bold lead-ins, and the form's own question list.

## PDF results (guidelines)

| | pdftotext -layout | pdfplumber | pymupdf4llm | Docling (pp. 40–50) | MarkItDown |
|---|---|---|---|---|---|
| Time | <1 s | 0.8 s (8 pp. tables) | 11.6 s | 122 s on CPU (first run, includes model load) | 7.5 s |
| Headings | none | none | 76, multi-level | yes, but **all at `##`** | none |
| Score overview table | aligned columns | 17×6 grid (spurious empty cols) | correct 2-col pipe table | correct 17×2 table | flat text |
| Rubric pages | clean bullets | 1-column "tables" (bordered boxes) | bullets + bold bands | bullets | flat text |
| Notes | page breaks = `\f` | good for table cell geometry | ran OCR on 4 pages automatically (Tesseract) | downloads OCR/layout models | pdfminer text |

The main PDF finding is that **Appendix F rubric bands are bulleted text, not tables.** Each question has the form `Question N. … [Points available: X; Limit: Y words]`, followed by `High (a-b points): …`, `Medium …`, `Low …`. A deterministic parser can read these from `pdftotext` output after joining wrapped lines. Brackets sometimes wrap across lines, so raw-line regex undercounts them. The PDF is also **tagged**, so its structure tree offers another route to headings *(not tested)*.

## Takeaways for M0/M1

1. **Adopt pandoc for DOCX.** It keeps the most information (styles, comments, media), it is deterministic, and its AST is inspectable. Add a Lua filter that (a) promotes `custom-style="Title"` to a tab boundary, (b) drops the TOC and empty headings, (c) merges consecutive same-level headings, and (d) strips inline formatting from headings.
2. **Trial Docling** as the structural model for segmentation (typed items + heading breadcrumbs) and as a cross-check. Its heavier install (1.6 GB venv vs about 0.5 GB for everything else) is acceptable for a dev tool but not for Claude web.
3. **PDF solicitations:** `pdftotext -layout` for the text layer, pdfplumber for real tables, pymupdf4llm when Markdown headings help (mind the AGPL). Claude PDF reading only for LLM-assisted extraction that humans verify.
4. **MarkItDown** is fine for quick previews. It is not suitable as the canonical converter because it drops comments and flattens tables.

## Sources

- pandoc releases, https://github.com/jgm/pandoc/releases (accessed 2026-09-25)
- PyPI JSON for docling, markitdown, pymupdf4llm, pdfplumber, pypandoc-binary, https://pypi.org/ (accessed 2026-09-25)
- Hands-on runs, 2026-09-25 (scratch outputs not retained in repo).

Up: [index.md](index.md)
