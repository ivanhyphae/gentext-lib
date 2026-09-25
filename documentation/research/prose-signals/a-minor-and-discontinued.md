---
title: Minor, discontinued and API-less writing tools
slug: a-minor-and-discontinued
level: 3
parent: index.md
related: [commercial-apis.md, a-sapling.md, a-languagetool-api.md, ../nlp-quality/readability-descriptives.md]
tags: [prowritingaid, quillbot, hemingway, ginger, textgears, perspective, wqrm]
status: draft
updated: 2026-09-25
kind: service
verdict: hold
fit: [M4, M7]
license: various (proprietary; WQRM paper CC-BY 4.0)
maturity: legacy
inspectability: low
sources:
  - title: ProWritingAid Help Center, Do you offer an API? (sunset; updated 2024-10-24)
    url: https://help.prowritingaid.com/article/126-do-you-offer-an-api-for-building-integrations
    accessed: 2026-09-25
  - title: TextGears API documentation
    url: https://textgears.com/api
    accessed: 2026-09-25
  - title: LinkGo FAQ, Does QuillBot have an API? (third-party; no official public API)
    url: https://linkgo.dev/faq/quillbot-have-an-api-for-integration
    accessed: 2026-09-25
  - title: Perspective API home page (sunsetting; ends after 2026)
    url: https://www.perspectiveapi.com/
    accessed: 2026-09-25
  - title: Chakrabarty, Laban, Wu, AI-Slop to AI-Polish? Edit-based writing rewards (arXiv 2504.07532)
    url: https://arxiv.org/abs/2504.07532
    accessed: 2026-09-25
---

# Minor, discontinued and API-less writing tools

> **TL;DR** **Hold on all of these.** ProWritingAid has no API (sunset in 2024). QuillBot, Hemingway and Ginger have no official public developer API that we could find. TextGears has a small span-level grammar and readability API but adds nothing over Sapling or LanguageTool. Perspective API shuts down on 2026-12-31 and is out of scope anyway. The most interesting "newcomer" is not a vendor: an open **writing-quality reward model** (WQRM, Salesforce) that we could run ourselves if LLM judges prove too noisy.

## Status table (2026-09-25)

| Tool | API status | Note |
|---|---|---|
| **ProWritingAid** | **Discontinued**: "we no longer offer an API" (help page updated 2024-10-24) | Old SDKs remain on GitHub, dead |
| **QuillBot** | No official public API (third-party FAQ; the only "API" hits are UI-scraping hacks) | Don't scrape, it breaks their terms |
| **Hemingway Editor** | No developer API found *(absence unverified)* | Its signals (grade level, adverbs, passive voice, hard sentences) are easy to rebuild with textstat + spaCy ([readability-descriptives](../nlp-quality/readability-descriptives.md)) |
| **Ginger** | No developer API found *(absence unverified)* | — |
| **TextGears** | Active REST API: `/grammar`, `/spelling`, `/readability`, `/analyze`, `/detect`, `/summarize`. Errors carry `offset`, `length`, `type`, `better[]`. 11 languages; servers in US, Estonia, Singapore | Our probe with the legacy `DEMO_KEY` returned "Invalid API key". Pricing and retention not verified |
| **Perspective API** (Jigsaw) | **Sunsetting**: "service is officially ending after 2026"; no new quota requests after Feb 2026 | Toxicity is irrelevant to proposal prose |

## Newcomers: "writing quality scoring"

We found no 2025–26 commercial API that scores holistic writing quality *with spans* beyond the vendors on the [comparison page](commercial-apis.md). "Slop detector" sites are browser-side cliché word lists (e.g. a 758-entry list), which our own lexicon does better and inspectably.

The research signal is more useful. Chakrabarty, Laban and Wu (arXiv 2504.07532, CC-BY) report that most frontier LLMs scored **near chance** on a 4,729-judgment Writing Quality benchmark. Their edit-trained **WQRM** reached 74%, and WQRM-selected revisions were preferred by professional writers in 66% of cases (72% when score gaps were larger). They say they release datasets and models *(model licence and weights availability not checked)*. Two implications:

1. It is a caution for the rubric pass: holistic "is this good writing?" judgments from LLMs are weak, so keep to checklist items with quotes ([judge-reliability](../llm-evaluation/judge-reliability.md)).
2. It is a possible later **build** option: a self-hosted reward model to rank candidate rewrites of a paragraph. Assess after the pilot, if the critic/reviser loop needs a tiebreaker.

## Verdict rationale

Hold. Nothing here beats the Sapling / LanguageTool / own-checks combination. Recheck TextGears only if Sapling's terms turn out to be unacceptable.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
