---
title: Claude API features for gentext pipelines
slug: api-features
level: 3
parent: index.md
related: [citations.md, agent-sdk.md, delivery-architecture.md]
tags: [api, structured-outputs, batch, caching, files, memory, code-execution, web-search]
status: draft
updated: 2026-09-25
kind: platform
verdict: assess
fit: [M1, M4, M5, M6, M7, M10]
license: proprietary (Anthropic API)
maturity: mature
inspectability: medium
sources:
  - title: Features overview
    url: https://platform.claude.com/docs/en/build-with-claude/overview
    accessed: 2026-09-25
  - title: Memory tool
    url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
    accessed: 2026-09-25
  - title: Citations (structured-outputs incompatibility)
    url: https://platform.claude.com/docs/en/build-with-claude/citations
    accessed: 2026-09-25
---

# Claude API features for gentext pipelines

> **TL;DR** Several API features pay off in *headless* gentext jobs: structured outputs (M1 classification, M5 extraction), Batch (50% off bulk runs), prompt caching (library and rubric prefixes), Files, and web search/fetch (solicitation research). The memory tool and context editing matter only for long agent runs. **Assess**: adopt each one when a P3 pipeline needs it. None of them is needed for the pilot.

## Feature table (status per the features overview, 2026-09-25)

| Feature | Status on Claude API | gentext use | Notes |
|---|---|---|---|
| Structured outputs (JSON outputs, strict tool use) | GA | M1 chunk-type classification; M5 rubric → YAML; M7 judge reports | Schema-guaranteed. **Not combinable with Citations.** Schemas cached ≤24 h |
| Batch processing | GA | Re-characterize the whole library; judge every chunk against a rubric | 50% cheaper, asynchronous. Not ZDR eligible |
| Prompt caching (5 min, 1 h, automatic) | GA | Cache the glossary, voice guide and solicitation model as a shared prefix | Big savings when many questions share one prefix |
| Files API | GA (API) | Upload solicitation PDFs once, reuse across calls | Not ZDR. Keep confidential sources out (DR-0004) |
| Code execution tool | GA | Required for API Skills. Could run M4 metrics in-sandbox | No network in the container. Free alongside web search/fetch |
| Web search / web fetch | GA | Check funder pages and deadlines for M5 | Cite sources; treat fetched text as untrusted |
| Agent Skills via API | GA (`/v1/skills`) | Same SKILL.md files in API jobs | Workspace-wide; not ZDR |
| MCP connector | Beta | Call our remote MCP server straight from the Messages API | Reuse the P2 server in batch jobs |
| Memory tool | GA (client-side) | Agent keeps progress notes across sessions | **We** store the files under `/memories`, so it can live in the repo or a DB and stays inspectable |
| Context editing / compaction | Beta | Long ingest or QA agent runs | Clears old tool results or summarizes |
| Tool search, programmatic tool calling | GA | Only if the tool count grows large | Probably unnecessary |

## Why it matters for gentext

DR-0003 puts LLM steps (classification, extraction, adaptation, judging) behind human review. The API gives those steps typed outputs and bulk pricing, which interactive chat can't provide. The README's "third party memory system" idea can be compared against the memory tool, which is our own storage and therefore inspectable.

## How it would fit

- `gentext classify --llm`: structured outputs + Batch + a cached glossary prefix, producing candidate metadata for human confirmation (M1).
- `gentext solicitation extract`: Files API PDF + structured outputs → draft YAML → human review (M5).
- `gentext judge`: rubric coverage with structured outputs, run separately from the Citations-enabled compose call.

## Strengths

- Deterministic shapes, predictable cost, and every call can be logged by our code, which keeps inspectability high where we own the loop.

## Weaknesses / risks

- API billing is separate from claude.ai seats. Adds a key-management burden.
- Several features aren't ZDR eligible (Batch, Files, Skills, code execution), which matters if sources are sensitive.
- Beta features (MCP connector, context editing) can change.

## Verdict rationale

**Assess.** Valuable building blocks for P3 automation, irrelevant to the Claude Code pilot. Revisit per feature when a pipeline is specified.

Parent: [index.md](index.md)
