---
title: proselint (with write-good and alex)
slug: proselint
level: 3
parent: index.md
related: [vale.md, hedge-booster-lexicon.md, languagetool.md]
tags: [prose-lint, style, python]
status: draft
updated: 2026-09-25
kind: library
verdict: assess
fit: [M7]
license: BSD-3-Clause (proselint); MIT (write-good, alex)
maturity: mature
inspectability: high
sources:
  - title: amperser/proselint GitHub repository
    url: https://github.com/amperser/proselint
    accessed: 2026-09-25
  - title: proselint on PyPI (0.16.0, 2025-11-14)
    url: https://pypi.org/project/proselint/
    accessed: 2026-09-25
  - title: btford/write-good GitHub repository (last push 2025-03-10)
    url: https://github.com/btford/write-good
    accessed: 2026-09-25
  - title: get-alex/alex GitHub repository (last push 2024-11-27)
    url: https://github.com/get-alex/alex
    accessed: 2026-09-25
  - title: Vale package ports (vale-cli/proselint, vale-cli/write-good, vale-cli/alex)
    url: https://github.com/vale-cli/proselint
    accessed: 2026-09-25
---

# proselint (with write-good and alex)

> **TL;DR** **Assess.** proselint is a maintained Python linter with 60+ curated usage checks (hedging, weasel words, clichés, jargon, corporate speak, typography). It is useful as a library of *ideas and word lists*. For gentext, run its checks through Vale's packaged ports, or borrow its lists into our lexicons, rather than adding a second linter engine. write-good and alex are Node tools with slowing maintenance. Use them only via Vale ports.

## What it is

- **proselint**: BSD-3-Clause Python CLI and library. v0.16.0 was released 2025-11-14, with repo commits as of 2026-09-04. Checks are grouped as uncomparables, weasel words, clichés, malapropisms, hedging, mixed metaphors, oxymorons, skunked terms, jargon, corporate speak, bureaucratese, typography, redundancy, and sensitivity. JSON config (`proselint.json`) enables or disables checks per module or per file glob. The Python API (`LintFile(...).lint()`) returns structured results with positions.
- **write-good** (MIT, Node): flags passive voice, weasel words, "so" at sentence start, adverbs, clichés, and wordy phrases. Last push 2025-03.
- **alex** (MIT, Node): flags insensitive or inconsiderate language. Last push 2024-11.

## Why it matters for gentext

- Funders discount inflated, vague prose. proselint's `hedging`, `weasel_words`, `corporate_speak`, and `cliches` overlap with what reviewers penalize.
- Its lists are curated by editors, which gives better precision than ad-hoc word lists.
- It does **not** directly target the DR-0002 boosters ("unprecedented", "cutting-edge"). Those need the [hype/booster lexicon](hedge-booster-lexicon.md) *(based on the check categories; not exhaustively verified)*.

## How it would fit

- Preferred: add Vale packages (`proselint`, `write-good`, `alex` ports) to `.vale.ini` so there is one engine, one output format, and one suppression mechanism.
- Alternative: call proselint's Python API from M7 if a check isn't ported. Map results to `L10.proselint.<check>`.

## Strengths

- Curated, low-noise checks. Python-native, permissive license.
- Configurable per check.

## Weaknesses / risks

- Generic English usage, not grant-writing-specific.
- Passive-voice and adverb flags (write-good) are noisy in technical prose. Report them as ratios, not errors.
- Two engines (Vale + proselint) would duplicate findings.

## Verdict rationale

Valuable content, but redundant as an engine next to Vale. Assess whether the Vale ports cover what we want. Otherwise, mine proselint's lists into our own lexicons.

Parent: [NLP quality checks](index.md)
