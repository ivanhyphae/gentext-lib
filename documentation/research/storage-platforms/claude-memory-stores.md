---
title: Anthropic memory tool and Managed Agents memory stores
slug: claude-memory-stores
level: 3
parent: index.md
related: [claude-web-access.md, agent-memory-services.md, git-markdown-vault.md]
tags: [memory, anthropic, agents, managed-agents]
status: draft
updated: 2026-09-25
kind: service
verdict: assess
fit: [M6, M8, M9]
license: proprietary API
maturity: emerging
inspectability: high
sources:
  - title: Memory tool (Claude Platform docs)
    url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
    accessed: 2026-09-25
  - title: Using agent memory (Managed Agents)
    url: https://platform.claude.com/docs/en/managed-agents/memory
    accessed: 2026-09-25
  - title: Memory for Claude Managed Agents (blog)
    url: https://claude.com/blog/claude-managed-agents-memory
    accessed: 2026-09-25
---

# Anthropic memory tool and Managed Agents memory stores

> **TL;DR** **Assess.** These are the only "memory systems" that match our architecture: agent memory as a directory of Markdown files, versioned in the hosted variant. Use them for *working* memory (session notes, user and style preferences, open drafting tasks), never for canonical library content. They matter only if we build our own agent on the Claude API or Managed Agents. Claude web chat doesn't use them.

## What they are
1. **Memory tool** (`memory_20250818`, client-side). Claude issues `view`, `create`, `str_replace`, `insert`, `delete`, and `rename` on paths under `/memories`, and **our** code executes them against storage we choose. It's available on Claude 4+ models. SDK helpers: `BetaAbstractMemoryTool` and `BetaLocalFilesystemMemoryTool` (Python). We're responsible for path-traversal protection.
2. **Managed Agents memory stores** (beta header `agent-memory-2026-07-22`, public beta since April 2026). Workspace-scoped collections of text documents, mounted into the agent sandbox at `/mnt/memory/<slug>/`, read-only or read-write. Every change creates an **immutable memory version** (audit, point-in-time restore, redaction). Versions are retained 30 days (recent versions of live memories are kept) and can be exported via the API. Limits: 100 kB per memory, 10,000 memories per store, 8 stores per session. Edits support optimistic concurrency via `content_sha256` preconditions.

## Why it matters for adapt-rfp
The README asks for a production memory layer. This one has the same shape as DR-0005 (Markdown files and paths), is Claude-native, and is inspectable (list, read, and diff versions through the API or Console). A hosted adapt-rfp agent could mount:
- `adapt-rfp-library` **read-only**: a synced copy of promoted library chunks (git stays canonical),
- `adapt-rfp-working` **read-write**: drafting notes, reviewer feedback, per-person style preferences.

## Strengths
- File semantics, versioning, redaction, read-only mounts (a guard against prompt-injection writes, which the docs explicitly warn about).
- No embedding infrastructure, and no vendor outside Anthropic.

## Weaknesses / risks
- Beta. Retention and limits may change, and 30-day version history is shorter than git's.
- Only relevant if we run agents on the API or Managed Agents. Claude web chat with connectors doesn't mount these stores.
- A second copy of library text. Keep it read-only and one-way synced from git.

## Verdict rationale
It's the right answer *if* production means a hosted Claude agent. Until then, the git repo plus our MCP server covers the need. Revisit in the deployment DR.

Parent: [index.md](index.md)
