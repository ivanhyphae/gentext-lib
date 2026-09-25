---
title: LanguageTool
slug: languagetool
level: 3
parent: index.md
related: [spacy-rule-matching.md, vale.md, proselint.md]
tags: [grammar, spelling, prose-lint, self-hosted, java]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M7]
license: LGPL-2.1 (core); language_tool_python wrapper GPL-3.0
maturity: mature
inspectability: medium
sources:
  - title: languagetool-org/languagetool GitHub repository (license, activity)
    url: https://github.com/languagetool-org/languagetool
    accessed: 2026-09-25
  - title: LanguageTool (Wikipedia; 6.8 stable May 2026, n-gram data size)
    url: https://en.wikipedia.org/wiki/LanguageTool
    accessed: 2026-09-25
  - title: Self-host LanguageTool guide (2026; Docker, Java 17)
    url: https://wiki.ethanppl.com/blog/2026/05/11/self-host-language-tools
    accessed: 2026-09-25
  - title: meyayl/docker-languagetool image
    url: https://github.com/meyayl/docker-languagetool
    accessed: 2026-09-25
  - title: language_tool_python on PyPI (3.4.0, GPL-3.0-only)
    url: https://pypi.org/project/language-tool-python/
    accessed: 2026-09-25
  - title: Public API probe, api.languagetool.org/v2/check (reported version 6.9-SNAPSHOT)
    url: https://api.languagetool.org/v2/check
    accessed: 2026-09-25
---

# LanguageTool

> **TL;DR** **Trial.** LanguageTool is the strongest open-source rule-based grammar and spelling checker, and it is self-hostable via Docker (Java 17+, optional ~8 GB n-gram data). Use it as a *broad secondary* grammar pass. In our probe it **did not catch** the pilot's "one of the … facility" error, so the specific pilot regressions need custom spaCy rules.

## What it is

A Java grammar, style, and spell checker with thousands of XML pattern rules per language. The core is LGPL-2.1, and the repo was actively committed as of 2026-09-25. Wikipedia lists 6.8 (May 2026) as the latest stable release. The public API reported `6.9-SNAPSHOT` on our probe date. It exposes an HTTP API (`/v2/check`) and can run locally as a server (default port 8010 in common Docker images). Optional n-gram data (~8 GB for English) improves confusion-pair detection (their/there, affect/effect). Some rules are Premium-only on the hosted service, and the API response says so ("You might be missing errors only the Premium version can find").

## Probe (2026-09-25, public API, synthetic sentences)

| Sentence | LanguageTool matches |
|---|---|
| "She is one of the best student in the class." | none |
| "It is one of the primary recreational facility in the area." | none |
| "Our team is one of the leader in the field." | none |
| "…This cutting-edge tool offers unprecedented precision." | none |

A local spaCy Matcher rule caught the first two ([spaCy rules](spacy-rule-matching.md)). So LanguageTool (free tier, without n-grams) is **not sufficient** for the DR-0002 grammar regression. Premium or n-gram behaviour is untested.

## Why it matters for adapt-rfp

It catches the long tail of generic errors (agreement, commonly confused words, punctuation, doubled words) that we don't want to write rules for. Custom XML rules and a disabled-rules list can adapt it to our style.

## How it would fit

- M7 posts draft text to a **self-hosted** LanguageTool container. Pilot text should not go to the public API: DR-0004 treats sources as confidential, and the public API has rate limits.
- Call the HTTP API directly with `httpx`. Avoid a hard dependency on `language_tool_python`, which is GPL-3.0-only. A GPL dependency is a licensing question for a private repo that might be distributed later. Calling a server over HTTP avoids linking.
- Map `rule.id`, `offset`, `length`, `message`, and `replacements` into the adapt-rfp report as `L7.lt.<rule_id>`, severity warning.

## Strengths

- Broad, mature, multilingual coverage. Rule ids make findings explainable and suppressible.
- Self-hostable. No model downloads beyond optional n-grams.

## Weaknesses / risks

- Missed the pilot's actual grammar defect in our probe.
- Java service plus multi-GB data is extra infrastructure for a small team. Claude web would need it hosted (M10).
- Hosted-service rules differ from open-source rules, so results are not identical across deployments.

## Verdict rationale

Trial it as a secondary pass once the deterministic spaCy/Vale checks exist. Keep it only if, on real drafts, it catches issues the custom rules miss at an acceptable false-positive rate.

Parent: [NLP quality checks](index.md)
