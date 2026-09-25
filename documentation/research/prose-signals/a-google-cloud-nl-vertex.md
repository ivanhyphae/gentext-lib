---
title: Google Cloud Natural Language API and Gemini (Agent Platform, formerly Vertex AI)
slug: a-google-cloud-nl-vertex
level: 3
parent: index.md
related: [commercial-apis.md, ../llm-evaluation/judge-reliability.md, ../llm-evaluation/rubric-judging.md, ../nlp-quality/spacy-rule-matching.md]
tags: [google-cloud, gemini, llm-judge, cross-family, syntax, entities]
status: draft
updated: 2026-09-25
kind: service
verdict: trial
fit: [M4, M7]
license: proprietary (GCP terms)
maturity: mature
inspectability: medium
sources:
  - title: Cloud Natural Language API REST reference (v1/v1beta2/v2 methods; v2 lacks analyzeSyntax)
    url: https://docs.cloud.google.com/natural-language/docs/reference/rest
    accessed: 2026-09-25
  - title: Natural Language API basics (syntax tokens, POS, dependencyEdge, beginOffset)
    url: https://docs.cloud.google.com/natural-language/docs/basics
    accessed: 2026-09-25
  - title: Natural Language API data usage FAQ ("does not store any customer data")
    url: https://docs.cloud.google.com/natural-language/docs/data_usage
    accessed: 2026-09-25
  - title: Cloud Natural Language pricing
    url: https://cloud.google.com/natural-language/pricing
    accessed: 2026-09-25
  - title: Gemini Enterprise Agent Platform (formerly Vertex AI) product page
    url: https://cloud.google.com/products/gemini-enterprise-agent-platform
    accessed: 2026-09-25
  - title: Gemini Developer API pricing (model ids and per-M-token prices, batch −50%)
    url: https://ai.google.dev/gemini-api/docs/pricing
    accessed: 2026-09-25
  - title: Panickssery et al., LLM evaluators recognize and favor their own generations (arXiv 2404.13076)
    url: https://arxiv.org/abs/2404.13076
    accessed: 2026-09-25
---

# Google Cloud Natural Language API and Gemini (Agent Platform, formerly Vertex AI)

> **TL;DR** **Trial Gemini, hold the NL API.** Hyphae already uses Google Cloud, so Gemini is the easiest *different-family* judge to add. Running our rubric and finding schema through Gemini as a second opinion directly targets Claude's self-preference bias when Claude judges Claude-drafted text. The classic Natural Language API is span-accurate and has a strong no-storage policy, but it adds little over local spaCy, and `analyzeSyntax` exists only in v1.

## Natural Language API

- **Methods:** v1 and v1beta2 have `analyzeEntities`, `analyzeEntitySentiment`, `analyzeSentiment`, `analyzeSyntax`, `annotateText`, `classifyText` and `moderateText`. **v2 drops `analyzeSyntax` and entity sentiment.**
- **Signal:** tokens with `beginOffset`, POS (tense, number, person…), lemma, dependency edges; entities with salience; document and sentence sentiment; content categories; moderation categories.
- **Data:** "Google processes it in memory and does not store any customer data". Only metadata is logged.
- **Pricing:** per 1,000-character unit per feature, with a monthly free tier. Exact rates were not rendered in our fetch *(check the pricing page)*.
- **Fit:** spaCy already gives us the same parse locally and deterministically ([spacy-rule-matching](../nlp-quality/spacy-rule-matching.md)). The only reason to call the NL API would be `classifyText` as a cheap topic label for chunks in M4. Hold.

## Gemini as a second-opinion judge

- **Platform:** Vertex AI was renamed **Gemini Enterprise Agent Platform** in April 2026 (Cloud Next). Existing endpoints (`aiplatform.googleapis.com`) and SDKs keep working. Gemini is also reachable through the simpler Gemini Developer API.
- **Models and price** (Developer API list, 2026-09-25): `gemini-3.5-flash` $1.50/$9.00 per M tokens; `gemini-3.8-flash` $0.75/$3.75 introductory until 2026-12-31, doubling on 2027-01-01; `gemini-3.1-pro-preview` $2/$12; `gemini-3.5-flash-lite` $0.30/$2.50. The batch discount is 50%. Agent Platform pricing may differ slightly *(the page did not render for us)*.
- **Why:** LLM judges favour their own family's output ([2404.13076](https://arxiv.org/abs/2404.13076)). Rubric judges were >50% more likely to wrongly pass their own family's failures ([judge-reliability](../llm-evaluation/judge-reliability.md)). A Gemini pass using the *same* checklist and quote-first JSON schema ([rubric-judging](../llm-evaluation/rubric-judging.md)) gives us disagreement cases worth a human look. It does not replace the human gold set.
- **Holistic prompts that work here:** "Quote each sentence that could appear unchanged in any firm's proposal (generic)". "Quote sentences whose claims have no concrete noun, number, or place". "Estimate reading grade and name the three sentences that drive it up". Each answer is a quote plus a rubric line, which we verify by exact-match anchoring before it reaches Claude.

## How it would fit

M7 stage 3 gets `judge_second_opinion(text, rubric_id, model="gemini-3.5-flash")` on the MCP server. It uses a service-account key already in Hyphae's GCP project and structured-output JSON. Findings whose quotes don't match the text are dropped. Claude sees findings tagged `source: gemini`, and agreement between the two families raises confidence.

## Strengths

- Different model family, existing billing and IAM, cheap Flash tier, and batch mode for library-wide sweeps.

## Weaknesses / risks

- Model ids churn fast (six Flash variants listed), so pin versions.
- A second judge doubles the prompt-maintenance surface. Both families share some biases (verbosity, leniency).

## Verdict rationale

Trial Gemini on the post-pilot calibration set: compare Claude-only and Claude+Gemini agreement against human labels. Hold the NL API.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
