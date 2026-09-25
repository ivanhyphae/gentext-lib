---
title: Claude Code on the web (over the git repo)
slug: claude-code-web
level: 3
parent: index.md
related: [claude-web-access.md, git-markdown-vault.md, remote-mcp-hosting.md]
tags: [claude-web, deployment, zero-infra, skills]
status: draft
updated: 2026-09-25
kind: product
verdict: trial
fit: [M8, M10]
license: proprietary (included with paid Claude plans)
maturity: emerging
inspectability: high
sources:
  - title: Use Claude Code in the cloud (docs)
    url: https://code.claude.com/docs/en/claude-code-on-the-web
    accessed: 2026-09-25
---

# Claude Code on the web (over the git repo)

> **TL;DR** **Trial now.** Claude Code on the web (claude.ai/code) runs sessions in Anthropic-managed VMs with our private GitHub repo cloned. Our skills and `uv` CLIs run there unchanged, and results come back as commits/PRs. It's the zero-infrastructure way to operate the whole system from a browser during the pilot.

## What it is
Cloud sessions of Claude Code started from claude.ai/code, or with `claude --cloud "…"` from the terminal. Each session gets an isolated VM with the repo cloned and limited network access by default. Repos connect through the Claude GitHub App. It's a research preview for Pro, Max, and Team, and for Enterprise premium / Chat+Claude Code seats (per docs, Aug 2026).

## Why it matters for adapt-rfp
The README target is "Claude web can operate the system end to end." For technical team members this works on day one: ingest → segment → draft → check, with every change landing as a reviewable PR. There's no server, no OAuth, and no hosted database.

## How it would fit
- A repo-level setup hook runs `uv sync && adapt-rfp index rebuild`, so every session starts with a fresh SQLite index.
- Skills in `skills/` (M8) load as project skills.
- Confidential `projects/` sources aren't in the repo (DR-0004), so cloud sessions only see promoted library text. That's a feature. Ingesting new raw sources stays a local-machine task.

## Strengths
- Zero infra and zero new vendors, and the same environment as local Claude Code.
- High inspectability: session transcripts plus git history.

## Weaknesses / risks
- It's a coding surface, not the chat or Claude Docs surface where colleagues draft. Non-technical users won't live here.
- Research preview: features, limits, and availability may change.
- Restricted network by default. Embedding API calls may need allow-listing *(unverified specifics)*.
- The index is rebuilt per session. That costs seconds now and could need embedding caching as the corpus grows (commit a cache, or fetch it from storage).

## Verdict rationale
It delivers the end-to-end target for the pilot at no cost and defers the MCP server until we know which tools people actually call.

Parent: [index.md](index.md)
