---
title: LanguageTool hosted API (Premium / Proofreading API)
slug: a-languagetool-api
level: 3
parent: index.md
related: [commercial-apis.md, a-sapling.md, ../nlp-quality/languagetool.md, ../nlp-quality/vale.md]
tags: [grammar, spelling, api, hosted, gdpr]
status: draft
updated: 2026-09-25
kind: service
verdict: assess
fit: [M7]
license: proprietary service over LGPL-2.1 core
maturity: mature
inspectability: medium
sources:
  - title: LanguageTool, Public HTTP Proofreading API (free limits)
    url: https://dev.languagetool.org/public-http-api
    accessed: 2026-09-25
  - title: LanguageTool, Proofreading API plans (no text stored, servers in Germany, 60k chars/request)
    url: https://languagetool.org/proofreading-api
    accessed: 2026-09-25
  - title: LanguageTool HTTP API documentation
    url: https://languagetool.org/http-api/
    accessed: 2026-09-25
  - title: LanguageTool Forum, Disappointing API limits for Premium (Premium 80 req/min, 300k chars/min; via search summary)
    url: https://forum.languagetool.org/t/disappointing-api-limits-for-premium/8728
    accessed: 2026-09-25
  - title: Probe of api.languagetool.org/v2/check, default and picky levels (synthetic text)
    url: https://api.languagetool.org/v2/check
    accessed: 2026-09-25
---

# LanguageTool hosted API (Premium / Proofreading API)

> **TL;DR** **Assess.** The hosted API is the same engine as the self-hosted server covered in [languagetool](../nlp-quality/languagetool.md), plus Premium-only rules. It returns clean span findings (`offset`, `length`, `rule.id`, category, replacements). Its paid terms are good: texts are not stored, and servers are in Germany. It is a grammar and spelling signal only. Even at `level=picky` it flagged **none** of the generic/hype phrasing in our probe. Prefer Sapling for rented grammar, or self-host LanguageTool.

## What it offers

- **Free public API**: 20 requests/IP/minute, 75 KB/minute, 20 KB per request, and suggestions for at most 30 misspellings. No guarantees, and a backlink is required. Fine for probes, not production.
- **Premium API** (a Premium user's key): about 80 req/min, 300k chars/min, 60k chars/request, according to a forum thread *(not confirmed on an official page)*.
- **Proofreading API plans**: five tiers by call volume (100 to 10,000 calls; the page is inconsistent about per day vs per month), max 60,000 chars/request, custom rules and a personal dictionary. It states that "none of the texts you send to the API are stored" and that the service is hosted in Germany and GDPR-compliant. Prices are not visible in the fetched page *(unverified)*.
- **Self-host**: the LGPL core via Docker. See the existing card.

## Probe (2026-09-25, public API, synthetic text only)

Text: *"In today's fast-paced world, our innovative team leverages cutting-edge solutions to deliver unparalleled value. Their are many reasons why the community will benefit."*

| Level | Matches |
|---|---|
| default | `THEIR_IS` (CONFUSED_WORDS) at offset 113, length 5: "Did you mean 'there'?" |
| picky | same single match |

It reported version `6.9-SNAPSHOT`. It flagged no cliché, hype word or wordiness. "Generic" and "slop" signals have to come from our own lexicons and the LLM pass ([hedge-booster-lexicon](../nlp-quality/hedge-booster-lexicon.md), [vale](../nlp-quality/vale.md)).

## How it would fit

The same adapter as the self-hosted server: `offset`/`length` are already document-absolute. Map `rule.id` to `L7.lt.<rule_id>` and `rule.category.id` to the finding category. The only difference between hosted and self-hosted is the base URL plus `username`/`apiKey` parameters, so we can start hosted and switch later.

## Strengths

- Mature, rule-id explainability, ~30 languages, and strong privacy wording on the paid API.
- No infrastructure for us, which matters for Claude web (M10).

## Weaknesses / risks

- Grammar and spelling only. It misses the pilot's defect classes (see the parent card's probe).
- Hosted Premium rules differ from the open-source rules, so results vary by deployment.
- Pricing is opaque from the pages we could fetch.

## Verdict rationale

Assess. It is a reasonable fallback if Sapling underperforms. Otherwise self-hosted LanguageTool (trial, in the parent card) plus custom rules gives the same signal without a subscription.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
