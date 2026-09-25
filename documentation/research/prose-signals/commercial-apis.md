---
title: Commercial writing-feedback APIs (build vs buy)
slug: commercial-apis
level: 2
parent: index.md
related: [a-grammarly.md, a-languagetool-api.md, a-sapling.md, a-writer.md, a-ai-detection-apis.md, a-google-cloud-nl-vertex.md, a-minor-and-discontinued.md, ../nlp-quality/languagetool.md, ../llm-evaluation/judge-reliability.md, ../nlp-quality/stylometry-ai-detection.md]
tags: [writing-feedback, grammar, ai-detection, build-vs-buy, api]
status: draft
updated: 2026-09-25
---

# Commercial writing-feedback APIs (build vs buy)

> **TL;DR** Mostly **build**, with narrow buys. No hosted API returns the holistic signal the maintainer wants ("generic", "AI slop", "reads at 4th grade", "big grammar problems") as **span-level findings**. Grammarly's API gives four document-level numbers, and only to Enterprise admins. LanguageTool and Sapling give good spans, but for grammar and spelling only. AI detectors give per-window "AI-likelihood" scores that are not quality and not provenance. The worthwhile buys: **Sapling** (trial: cheap, self-serve, sentence-offset grammar edits, plus a style-guide-compliance endpoint), **Gemini on Google Cloud** (trial as a *different-family* second-opinion judge, which counters self-preference bias), and optionally **Pangram** (assess: an advisory "reads as AI" heat map). Build "generic/slop/grade-level" ourselves from deterministic checks plus the Claude rubric pass.

## The question

Is "writing feedback" a domain we can rent, like Grammarly, so Claude gets real metrics and span-level issues it can correct against? We checked the 2026 status of the main vendors. A lot has changed since 2023: Grammarly killed its developer SDK (Jan 2024) and renamed its parent company Superhuman (Oct 2025). ProWritingAid shut its API (Oct 2024). Writer removed AI detection from its SDKs (June 2026). Perspective API ends on 2026-12-31. Superhuman bought GPTZero (June 2026).

## Comparison (accessed 2026-09-25; pricing goes stale fast)

| Service | Signal returned | Spans? | Small-team access & price | Data terms | Status | Card |
|---|---|---|---|---|---|---|
| **Grammarly APIs** (Superhuman) | Writing Score: `general_score` + engagement/correctness/delivery/clarity. AI Detection (beta): `average_confidence`, `ai_generated_percentage`. Plagiarism (beta) | **No**, document only | Enterprise/EDU admins only; quote-based | Uploaded file kept ≤24 h, score kept 30 d | Active; Text Editor SDK dead since 2024-01-10 | [a-grammarly](a-grammarly.md) |
| **LanguageTool API** | Grammar, spelling, some style; `rule.id`, category, `offset`/`length`, replacements | Yes | Free public API (20 req/min, 20 KB/request); paid Proofreading API plans; self-host (LGPL) | Paid API: "none of the texts … are stored", servers in Germany | Active (6.9-SNAPSHOT) | [a-languagetool-api](a-languagetool-api.md) |
| **Sapling** | Edits (grammar/spelling; `error_type`, `general_error_type`), tone, **style-guide compliance** (violations with offsets + rewrites), AI detector (doc/sentence/token) | Yes | Self-serve key; trial 50k chars/day; edits $0.025/1k chars, detector $0.005/1k | No-retention and on-prem on Enterprise; cloud default not stated | Active | [a-sapling](a-sapling.md) |
| **Writer** | Palmyra LLMs. Voice/Terms/Style Guide enforcement lives in the *app* | No checking API found | Tokens: Palmyra X5 $0.60/$6 per M | Enterprise | Active; AI-detect removed from SDK 3.0.0 | [a-writer](a-writer.md) |
| **Pangram / GPTZero / Originality.ai** | AI-likelihood: windows (Pangram), sentence highlights (GPTZero), sentence scores (Originality) | Yes (windows/sentences) | Pangram $0.05/100 words; GPTZero API tiers (unverified); Originality API from Enterprise $179/mo | GPTZero: API docs "not stored"; Pangram: zero-retention on enterprise | Active; GPTZero now Superhuman-owned | [a-ai-detection-apis](a-ai-detection-apis.md) |
| **Google Cloud NL API** | Syntax (tokens, POS, dependency, offsets; **v1 only**), entities, sentiment, classification, moderation | Yes | Per 1k-char units, free monthly tier | "Does not store any customer data" | Active | [a-google-cloud-nl-vertex](a-google-cloud-nl-vertex.md) |
| **Gemini (Agent Platform, formerly Vertex AI)** | Whatever our rubric asks for, as structured JSON | Yes, if the prompt asks for quotes | e.g. `gemini-3.5-flash` $1.50/$9 per M tokens, batch −50% | GCP terms; Hyphae already on GCP | Active; renamed Apr 2026 | [a-google-cloud-nl-vertex](a-google-cloud-nl-vertex.md) |
| ProWritingAid, QuillBot, Hemingway, Ginger, TextGears, Perspective | — | — | No usable API, discontinued, or marginal | — | See card | [a-minor-and-discontinued](a-minor-and-discontinued.md) |

## What each kind of signal is actually good for

- **Grammar/spelling spans** (LanguageTool, Sapling, TextGears) are a commodity. They fix the "big grammar problems" complaint only partly: in our probes neither the default nor the `picky` level of free LanguageTool flagged "In today's fast-paced world, our innovative team leverages cutting-edge solutions to deliver unparalleled value." It caught only *Their are* → *there* (see [a-languagetool-api](a-languagetool-api.md)). The earlier probe also missed "one of the … facility" ([languagetool](../nlp-quality/languagetool.md)).
- **Holistic scores** (Grammarly Writing Score) are the closest product to "is this good writing?". They come back as four numbers with no spans, so Claude has nothing to anchor a revision to, and access is gated behind Enterprise.
- **AI-detector scores** answer "does this read as machine-written?", which is a proxy for "generic/slop". They are not a provenance record. Independent 2026 work found commercial detectors flag 9–15% of unmodified human abstracts and 38–80% of lightly AI-polished ones ([arXiv 2608.11256](https://arxiv.org/abs/2608.11256)). Our own provenance record ([provenance](../provenance/index.md)) beats any detector on "who wrote this".
- **LLM judges from another family** are the only rented signal that can explain *why* a passage is generic, with a quote. That is what Claude can act on.

## Build vs buy recommendation

1. **Build the core** (already planned in [check-catalog](../nlp-quality/check-catalog.md)): readability/grade level (textstat), the hype/booster lexicon, Vale rules for clichés, spaCy agreement rules, plus the Claude rubric pass with quoted findings. These cover "generic", "4th grade" and "slop" inspectably and at no per-call cost.
2. **Trial Sapling** as the rented grammar layer instead of hosting LanguageTool: offsets, error categories, pay-per-character, no Java server to run for Claude web. Keep self-hosted LanguageTool as the fallback. Test the style-guide-compliance endpoint against our Vale rules.
3. **Trial Gemini as a second-opinion judge** on the same rubric and schema, for the self-preference problem in [judge-reliability](../llm-evaluation/judge-reliability.md). Use it on a sample, not every call.
4. **Assess Pangram** (or Sapling's detector, which is cheaper and already on the same key) as an *advisory* "reads-as-AI" heat map in M7 reports. Never use it as a gate or as authorship evidence.
5. **Hold** Grammarly (no spans, Enterprise-only), Writer (no checking API), Originality.ai, and the Google NL API (spaCy already does this locally).

## How it plugs into the MCP server

One adapter per vendor behind a `check_prose(text, checks=[…])` tool ([fastmcp](../claude-platform/fastmcp.md)). Each adapter normalises to the adapt-rfp finding shape: `{source, rule_id, category, start, end, quote, message, suggestions[], severity, confidence}`.

- Offsets: Sapling's edit `start`/`end` are **relative to the sentence**, so the document offset is `sentence_start + start`. LanguageTool uses `offset`/`length`. Pangram uses window `start_index`/`end_index`. GPTZero returns sentence text, which we re-anchor with a text-quote selector ([web-annotation-selectors](../provenance/web-annotation-selectors.md)).
- Document-level scores (Grammarly, detector totals) become one finding with `start=end=null`.
- Cache by `(vendor, model_version, sha256(text))` so re-runs are free and diffable. Log vendor model versions: Sapling and Pangram change their detector models without notice.
- Send only promoted library or draft prose, never `projects/` raw sources with contact data (AGENTS.md, DR-0004).

**Rough pilot cost:** 10,000 words is about 55k characters. That comes to about $1.40 for Sapling edits, $0.30 for Sapling detection, $5 for Pangram, and a few cents for a Gemini Flash judge pass.

Parent: [Prose signals](index.md)
