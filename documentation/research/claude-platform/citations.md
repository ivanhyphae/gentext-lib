---
title: Claude API Citations
slug: citations
level: 3
parent: index.md
related: [api-features.md, ../provenance/index.md, delivery-architecture.md]
tags: [api, citations, provenance, grounding]
status: draft
updated: 2026-09-25
kind: service
verdict: trial
fit: [M6, M7, M3]
license: proprietary (Anthropic API)
maturity: mature
inspectability: high
sources:
  - title: Citations
    url: https://platform.claude.com/docs/en/build-with-claude/citations
    accessed: 2026-09-25
  - title: Search results
    url: https://platform.claude.com/docs/en/build-with-claude/search-results
    accessed: 2026-09-25
---

# Claude API Citations

> **TL;DR** Citations are GA on the Claude API for all active models. With `citations: {enabled: true}` on documents, Claude's answer is interleaved with citation blocks that point to exact character ranges, PDF pages or custom content-block indices. `cited_text` is free of output tokens. **Trial** for M6 compose and M7 provenance checks in API or batch pipelines. The feature isn't available inside claude.ai chat.

## What it is

- **Document types.** Plain text, chunked into sentences, cited by `char_location`. PDF, cited by `page_location`. **Custom content**, meaning our own blocks with no further chunking, cited by `content_block_location` (0-indexed, exclusive end).
- **Search result blocks** give the same kind of citations for RAG results returned from tools.
- **Cost.** `cited_text` doesn't count toward output tokens, or toward input tokens when passed back.
- **Incompatible with structured outputs.** Enabling both returns HTTP 400.
- ZDR eligible. Available on Claude API, Claude Platform on AWS, Bedrock, Google Cloud and Foundry.

## Why it matters for gentext

AGENTS.md: "any factual claim in generated text must trace to a library chunk or fact with provenance". Citations make the model *emit* that trace in a machine-checkable form. There is no need to parse `[chunk:id]` tags out of prose.

## How it would fit

- **M6 compose (API path).** Send each candidate chunk variant as a custom-content document (one block per sentence or fact), with `title` = chunk id and `context` = metadata. The draft comes back with block-index citations, which map straight to chunk and fact ids, forming the "inline provenance map" of DR-0003.
- **M7 provenance check.** Sentences with numbers, names or dates and no citation get flagged. This is a deterministic post-check on the citation structure.
- **Claude web path.** Not available there. The `check_draft` tool does a lexical/embedding alignment instead (see [../provenance/index.md](../provenance/index.md)).

## Strengths

- Exact, auditable spans with no hallucinated quotes, since `cited_text` comes from the source.
- Custom content lets our chunk boundaries define citation granularity.

## Weaknesses / risks

- API-only. It doesn't help conversations in claude.ai or Claude Docs.
- Can't combine with structured outputs, so JSON reports and cited prose need separate calls.
- A citation shows that support *exists*, not that the paraphrase is faithful. The LLM judge in M7 is still needed.

## Verdict rationale

This is the strongest built-in provenance mechanism, and it fits M6/M7 in headless pipelines ([agent-sdk.md](agent-sdk.md)). **Trial** in P3, where compose runs through the API.

Parent: [index.md](index.md)
