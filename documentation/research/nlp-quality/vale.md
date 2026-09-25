---
title: Vale
slug: vale
level: 3
parent: index.md
related: [proselint.md, abbreviation-detection.md, spacy-rule-matching.md, check-catalog.md]
tags: [prose-lint, style, cli, glossary]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M3, M7, M8]
license: MIT
maturity: mature
inspectability: high
sources:
  - title: vale-cli/vale GitHub repository (license, release v3.22.0 2026-09-17)
    url: https://github.com/vale-cli/vale
    accessed: 2026-09-25
  - title: Vale docs, checks
    url: https://docs.vale.sh/checks/
    accessed: 2026-09-25
  - title: Vale docs, conditional check
    url: https://docs.vale.sh/checks/conditional.md
    accessed: 2026-09-25
  - title: Vale docs, vocabularies
    url: https://docs.vale.sh/keys/vocab.md
    accessed: 2026-09-25
---

# Vale

> **TL;DR** **Adopt.** Vale is a fast, markup-aware prose linter written in Go. Its rules are YAML files, so adapt-rfp can **generate a "Hyphae" style from the glossary and entity registry** and version it in git. It is the most inspectable way to enforce canonical names, forbidden variants, and acronym definitions.

## What it is

A single-binary CLI (MIT; repo `vale-cli/vale`, v3.22.0 released 2026-09-17, active) that lints Markdown, HTML, AsciiDoc, and more. It understands markup scopes, so it skips code and can target headings or body text. Rules `extend` one of these check types: `existence`, `substitution`, `occurrence`, `repetition`, `consistency`, `conditional`, `capitalization`, `metric`, `readability`, `spelling`, `sequence`, `script`. Community packages (Microsoft, Google, write-good, proselint, alex ports) install via `vale sync`.

## Why it matters for adapt-rfp

- **Vocabularies.** `config/vocabularies/<name>/accept.txt` entries feed `Vale.Terms` as a substitution rule, which enforces exact spelling and casing. `reject.txt` entries feed `Vale.Avoid` as an existence rule and flag every occurrence. The docs say to keep canonical forms in accept and unwanted variants in reject. This maps one-to-one onto glossary `canonical` and `aliases_forbidden` fields: "Resources Conservation District" and "Hispanic Counsel" go in reject, their canonical forms in accept.
- **`conditional`** handles "acronym used without definition". The documented example flags `\b([A-Z]{3,5})\b` unless a `Full Name (ACR)` pattern defines it, with an exceptions list.
- **`substitution`** can enforce a single expansion. A generated rule maps `Urban Thermal Comfort Index` → `Universal Thermal Climate Index`.
- **`existence`** with a token list gives a quick hype/booster check (see [lexicons](hedge-booster-lexicon.md)).
- **`consistency`** flags a document that uses both variants of a pair (e.g., "stormwater"/"storm water").

## How it would fit

- M3 exports `styles/Hyphae/*.yml` and `vocabularies/Hyphae/{accept,reject}.txt` from the glossary YAML. The generated files can be committed or rebuilt, per DR-0005.
- M7 runs `vale --output=JSON draft.md` and maps each alert (`Check`, `Line`, `Span`, `Message`, `Severity`) into the adapt-rfp report.
- M8: a skill can run Vale directly. Colleagues can also use the VS Code / Obsidian integrations *(integration availability unverified)*.
- Target-specific rules (context leakage) are awkward in Vale because they depend on per-draft metadata. Keep those in spaCy ([spaCy rules](spacy-rule-matching.md)), or generate a per-target Vale config at run time.

## Strengths

- Rules are plain text, diffable, reviewable by non-programmers, and testable with fixture files.
- Fast, deterministic, no model, no network.
- Output is line/column spans with rule ids, which is exactly the "explain the finding" requirement.

## Weaknesses / risks

- Regex/token level only. It has no POS or dependency parsing, so grammar agreement ("one of the … facility") is out of reach.
- Acronym collision *across* a library needs cross-document state. Vale lints files one at a time, so use [Schwartz-Hearst extraction](abbreviation-detection.md) for library-wide checks.
- A Go binary, not a Python dependency. Install via a release binary or package manager, then call it as a subprocess. Claude web cannot run it unless hosted (M10).

## Verdict rationale

It has the highest inspectability-to-effort ratio of anything in this survey. It directly catches three of the DR-0002 defects (name misspellings, UTCI expansion, boosters) with rules generated from data we must curate anyway.

Parent: [NLP quality checks](index.md)
