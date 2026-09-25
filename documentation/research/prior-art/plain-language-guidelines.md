---
title: Plain language guidelines
slug: plain-language-guidelines
level: 3
parent: proposal-management-practice.md
related: [visiblethread.md, funder-ai-policies.md]
tags: [style, plain-language, federal, standard]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M4, M7]
license: public domain (US) / CC0
maturity: mature
inspectability: high
sources:
  - title: Digital.gov, Principles of plain language
    url: https://digital.gov/guides/plain-language/principles
    accessed: 2026-09-25
  - title: Digital.gov, Requirements for plain writing (Plain Writing Act)
    url: https://digital.gov/resources/plain-writing-act
    accessed: 2026-09-25
  - title: Center for Plain Language, The Federal Plain Language Guidelines Are Missing
    url: https://centerforplainlanguage.org/the-federal-plain-language-guidelines-are-missing/
    accessed: 2026-09-25
  - title: GSA/plainlanguage.gov GitHub repository (archived 2025-12-29)
    url: https://github.com/GSA/plainlanguage.gov
    accessed: 2026-09-25
---

# Plain language guidelines

> **TL;DR** The Federal Plain Language Guidelines, written to implement the Plain Writing Act of 2010, are the most authoritative free style standard for writing to US public agencies. plainlanguage.gov has been retired. Its content now sits in an **archived, public-domain GitHub repo**, with a shorter guide on Digital.gov. **Adopt** it as the base of gentext's style rules, alongside the `humanizer` skill for AI-tells.

## What it is

- **Plain Writing Act of 2010**: requires federal agencies to use "clear, concise, well-organized" writing in public-facing documents. It binds agencies, not applicants, but it describes what agency reviewers are trained to value.
- **Federal Plain Language Guidelines (FPLG)**: PLAIN's long-standing manual. The Center for Plain Language reports that when plainlanguage.gov was taken down, the guidelines "quietly disappeared" and the link redirects to Digital.gov guides.
- **Digital.gov principles** (current): write for your audience, use topic sentences, use active voice, organize information (summary first), use tables and lists where they help.
- **Archive**: the `GSA/plainlanguage.gov` repo was archived read-only on 2025-12-29 and is public domain in the US (CC0 for contributions). We can vendor or cite rules from it.

## Why it matters for gentext

- California state grants (the pilot) are not bound by the federal act. But reviewers at agencies and CBOs reward the same things: short sentences, concrete nouns, active verbs, and summary first.
- It gives M7 style checks an **external, citable authority**, so they aren't just our taste. That helps when colleagues disagree with a flag.
- One specific rule matters twice: *use "must", not "shall"*. It is a style rule for our prose and, per APMP guidance, a signal when shredding requirements in M5 (shall = must).

## How it would fit

- M4: sentence length distribution, passive-voice rate, and readability. The FPLG gives targets to parameterize, e.g., flag sentences over a threshold *(pick thresholds empirically; FPLG numeric guidance unverified here)*.
- M7 `style` check: rules as data (YAML or a Vale style) with a `source:` field pointing to the FPLG section in the archived repo.
- Pair with the existing `humanizer` skill (Wikipedia "Signs of AI writing") for AI-tells. The two overlap on filler and inflated claims.

## Strengths

- Authoritative, free, public domain, stable (archived).
- Rules are concrete enough to automate.

## Weaknesses / risks

- The canonical text is now in an archive, not a living site. Future federal guidance may move again.
- Readability formulas are crude for technical content (UTCI modeling). Use them as flags, not gates.

## Verdict rationale

**Adopt** as the documented basis for style rules. It is cheap, citable, and inspectable.

Up: [Proposal management practice](proposal-management-practice.md)
