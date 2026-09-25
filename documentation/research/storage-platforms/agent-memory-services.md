---
title: Third-party agent memory services (mem0, Zep/Graphiti, Letta, Supermemory)
slug: agent-memory-services
level: 3
parent: index.md
related: [claude-web-access.md, claude-memory-stores.md, git-markdown-vault.md]
tags: [memory, agents, knowledge-graph, saas]
status: draft
updated: 2026-09-25
kind: service
verdict: hold
fit: [M3, M8]
license: mem0 Apache-2.0 (OSS) + SaaS; Graphiti Apache-2.0 (unverified) + Zep SaaS; Letta Apache-2.0 (unverified) + cloud; Supermemory OSS repo + SaaS
maturity: emerging
inspectability: low
sources:
  - title: Mem0 pricing
    url: https://mem0.ai/pricing
    accessed: 2026-09-25
  - title: Mem0 alternatives and pricing (secondary)
    url: https://atlan.com/know/mem0-alternatives/
    accessed: 2026-09-25
  - title: Graphiti docs
    url: https://help.getzep.com/graphiti/getting-started/welcome
    accessed: 2026-09-25
  - title: Zep temporal knowledge graph paper
    url: https://arxiv.org/abs/2501.13956
    accessed: 2026-09-25
  - title: Letta memory blocks
    url: https://docs.letta.com/guides/core-concepts/memory/memory-blocks
    accessed: 2026-09-25
  - title: Letta Context Repositories
    url: https://www.letta.com/blog/context-repositories/
    accessed: 2026-09-25
  - title: Supermemory pricing
    url: https://supermemory.ai/pricing/
    accessed: 2026-09-25
  - title: Supermemory repository
    url: https://github.com/supermemoryai/supermemory
    accessed: 2026-09-25
---

# Third-party agent memory services (mem0, Zep/Graphiti, Letta, Supermemory)

> **TL;DR** **Hold.** These products mostly *extract* memories from conversations with an LLM and retrieve them by vector/graph search. That's opaque, lossy, and provenance-free, which is the opposite of a curated, citable proposal library. Graphiti's temporal facts are the one idea worth borrowing for M3, and our git/RDF path can express it more inspectably.

## What they are (2026-09)
- **mem0**: memory layer that extracts, dedupes, and retrieves user/agent memories. Apache-2.0 OSS plus managed platform. 2026 pricing (secondary): Hobby free (10k memories), Starter $19/mo, Pro $249/mo (**graph memory only on Pro**), Enterprise custom.
- **Zep / Graphiti**: Graphiti is an OSS temporal knowledge-graph framework (20k+ stars per vendor). Facts carry validity windows, and the graph updates incrementally from "episodes". Zep is the hosted platform built on it.
- **Letta** (ex-MemGPT): stateful-agent framework. "Memory blocks" are pinned in the prompt, and Letta Filesystem handles documents. Since Feb 2026 Letta Code uses **Context Repositories**, git-backed memory files with auto-commits. (Letta API server agents don't use the local repo.)
- **Supermemory**: memory/context API, consumer app, and an open-source MCP server. Free, Pro $19/mo, Scale $399/mo, plus metered usage (secondary).

## Why it matters for gentext
The README says "consider a third-party memory system for production." Checked against our needs:
- **Library chunks and facts** need human curation, provenance, and variants. Auto-extracted memories can't supply these, and AGENTS.md forbids unsourced claims.
- **Working memory** (who prefers which voice, what reviewers flagged last round) is a real but small need. File-based stores ([claude-memory-stores.md](claude-memory-stores.md)) or a `notes/` folder cover it.
- **Temporal facts** ("CHAT score as of 2026 release") are useful. Graphiti's validity-window model is a good pattern for M3's `validity window` field.

## Strengths
- Turnkey cross-session recall for chat apps, with MCP servers available.
- Graphiti: a principled temporal model with academic write-up.

## Weaknesses / risks
- **Low inspectability**: LLM-extracted memories, embeddings, and graph edges we didn't author.
- Sends confidential content to another vendor (DR-0004).
- Prompt-injection writes into memory then persist as "trusted" context.
- Pricing and tiers churn (mem0 retired a tier in July 2026).

## Verdict rationale
They solve conversational personalization, not curated, citable content reuse. Revisit only if we build a chat product that needs per-user recall at scale. Even then, prefer file-based memory.

Parent: [index.md](index.md)
