---
title: Claude structured outputs and strict tool use
slug: claude-structured-outputs
level: 3
parent: index.md
related: [rubric-judging.md, anthropic-citations-api.md, claude-caching-batch-thinking.md, adversarial-review-pass.md]
tags: [claude, structured-outputs, json-schema, tool-use]
status: draft
updated: 2026-09-25
kind: service
verdict: adopt
fit: [M7, M8]
license: proprietary API
maturity: mature
inspectability: high
sources:
  - title: "Claude docs: Structured outputs"
    url: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
    accessed: 2026-09-25
  - title: "Claude docs: Citations (incompatibility note)"
    url: https://platform.claude.com/docs/en/build-with-claude/citations
    accessed: 2026-09-25
---

# Claude structured outputs and strict tool use

> **TL;DR** `output_config.format` (JSON Schema) or `strict: true` tool definitions constrain decoding, so the verdict JSON always parses and matches the schema. **Adopt** them for every judge, panel, skeptic, and adjudicator call. Numeric and length constraints aren't enforced by the schema, and citations can't be used at the same time. Our deterministic validator covers both gaps.

## What it is

Per the [docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), accessed 2026-09-25:
- **GA** on the Claude API, AWS, Bedrock, Google Cloud, and Foundry, for current Opus, Sonnet, Haiku 4.5, and Fable/Mythos models.
- **JSON outputs** via `output_config.format`. The old beta `output_format` is deprecated. Python SDK `messages.parse()` accepts Pydantic models.
- **Strict tool use** via `"strict": true` on a tool: the tool name and input match the schema.
- The schema is compiled to a grammar that restricts token generation. Compiled grammars are cached for 24h. Changing the schema invalidates the prompt cache.
- **Not supported**: recursive schemas, numeric constraints (`minimum`/`maximum`), string `minLength`/`maxLength`, and external `$ref`. `additionalProperties: false` is required on objects. `enum`, `anyOf`, and internal `$ref` are supported.
- **Incompatible with Citations** in the same request: that returns a 400 ([citations docs](https://platform.claude.com/docs/en/build-with-claude/citations)).

## Why it matters for gentext

Inspectability needs findings that are *data*: diffable, validatable, renderable into Claude Docs comments, and comparable across runs. Free-text critique can't be validated or counted. A schema also enforces the reasoning order that reduces rationalisation: evidence fields come before verdict fields ([judge-reliability](judge-reliability.md)).

## How it would fit

- One Pydantic model per role in `src/gentext/qa/llm/schemas.py` (planned): `PanelVerdict`, `SkepticFindings`, `Rebuttal`, `Adjudication`, `ClaimList`.
- Field order encodes the procedure: `items[] {rubric_ref(enum), quote{exact,prefix,suffix}|null, status(enum)}` → `band(enum)` → `points_low`, `points_high`.
- `rubric_ref` is generated as an **enum from the M5 YAML** for that question, so the judge can't cite a rubric line that doesn't exist. This is enforced at decode time.
- Post-validation in Python covers what the schema can't: quote occurs verbatim in the draft, points within the band range, string lengths.
- Tool-use variant: expose `report_finding(...)` as a strict tool if we later want the skeptic to emit findings incrementally while thinking.

## Strengths

- Zero parse failures. The schema doubles as documentation of the judge's contract.
- Dynamic enums (rubric ids, sentence ids, fact ids) cut out a whole class of hallucinated references.
- Pydantic models are reused by the renderer, tests, and Inspect scorers.

## Weaknesses / risks

- Constrained decoding can hide low confidence. A forced `status` enum gets filled even when the model is unsure, so include `unsure` as an allowed value.
- The schema adds to input tokens and must stay stable to keep the cache warm.
- It can't be combined with Citations, so the verification step uses a different call shape ([anthropic-citations-api](anthropic-citations-api.md)).
- Batch API compatibility is not stated in the page excerpt we read *(unverified; expected to work since it is a Messages parameter)*.

## Verdict rationale

**Adopt.** It is the cheapest large win for inspectability, and it turns the "every critique quotes a span and cites a rubric line" rule into a contract checked by the machine.

Parent: [LLM evaluation](index.md)
