---
title: LLM generation records
slug: llm-generation-records
level: 3
parent: index.md
related: [schema.md, prov-o.md, text-watermarking.md]
tags: [llm, provenance, prompts, telemetry, opentelemetry]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M6, M8, M9]
license: n/a (OTel semantic conventions Apache-2.0)
maturity: emerging
inspectability: high
sources:
  - title: OpenTelemetry Gen AI attribute registry
    url: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
    accessed: 2026-09-25
  - title: open-telemetry/semantic-conventions-genai
    url: https://github.com/open-telemetry/semantic-conventions-genai
    accessed: 2026-09-25
  - title: W3C PROV-O
    url: https://www.w3.org/TR/prov-o/
    accessed: 2026-09-25
---

# LLM generation records

> **TL;DR** Every LLM call whose output we keep gets a small YAML record: model, provider, time, operator, skill and prompt-template reference, input chunk ids with hashes, parameters, and output hash. Borrow field names from the **OpenTelemetry GenAI semantic conventions** (`gen_ai.provider.name`, `gen_ai.request.model`, …), which are still in development, not stable. Borrow the shape from PROV (Activity → used / wasAssociatedWith). **Adopt**, with one hard rule: never commit raw prompts that quote `projects/` material.

## What it is

The pattern is a provenance record for a generation *activity*:

| Field | PROV | OTel GenAI analogue |
|---|---|---|
| `agent: ai:claude-opus-5-5` | wasAssociatedWith (SoftwareAgent) | `gen_ai.request.model`, `gen_ai.provider.name` |
| `on_behalf_of: person:…` | actedOnBehalfOf | n/a |
| `at` | startedAtTime | span timestamps |
| `activity: shorten` | Activity type | `gen_ai.operation.name` (loosely) |
| `inputs[]` with sha256 | used | n/a |
| `prompt_ref`, `prompt_sha256` | used (Plan) | prompt content is opt-in in OTel |
| `params` | n/a | `gen_ai.request.*` (temperature, max tokens) |
| `output_sha256` | wasGeneratedBy (inverse) | n/a |

OTel's GenAI conventions are built for observability traces, not document provenance. Several practitioner write-ups note they were not yet stable in 2026 *(check status before pinning names)*.

## Why it matters for gentext

"AI wrote it" is not enough provenance. What matters is *which inputs* the model saw, because AGENTS.md requires every factual claim to trace to a chunk or fact. With input ids we can check that an AI-drafted sentence only restates facts that were present in its inputs, a deterministic M7 check.

## How it would fit

- M8 skills (`draft-answer`, `harvest-edits`) write the record automatically to `library/provenance/generations/`. The chunk's `authors[]` entry points to it via `via:`.
- Store the *template* (committed, versioned) plus a hash of the rendered prompt. If a rendered prompt contains only library text, it may be stored. If it touches `projects/`, store only the hash (DR-0004).
- Keep the raw model output hash, so a later diff shows how much humans changed. That makes "AI-drafted, lightly edited" measurable.
- Records for discarded generations are optional. They are useful for debugging, but noisy.

## Strengths
- Deterministic, declarative, no detection guesswork. Easy to review in a PR.
- Model ids and dates make "which model version wrote this?" answerable years later.

## Weaknesses / risks
- Only as complete as the tooling. Text generated in the Claude web UI and pasted in by hand has no record unless a human files one. The harvest skill should ask.
- Model ids alone don't pin behavior (providers update models, and system prompts change).
- A folder with a record per call can grow large. Compact it by keeping only records referenced by committed chunks.

## Verdict rationale

Adopt. This is the cheap and reliable half of AI provenance. Watermarks and detectors are the expensive and unreliable half.

Up: [provenance index](index.md)
