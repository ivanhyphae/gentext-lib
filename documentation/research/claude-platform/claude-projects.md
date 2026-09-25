---
title: Projects in claude.ai
slug: claude-projects
level: 3
parent: index.md
related: [agent-skills.md, mcp-connectors.md, google-drive-connector.md, claude-docs.md]
tags: [projects, knowledge, rag, claude-ai]
status: draft
updated: 2026-09-25
kind: product
verdict: trial
fit: [M2, M5, M8]
license: proprietary (Anthropic)
maturity: mature
inspectability: low
sources:
  - title: What are projects? (Help Center)
    url: https://support.claude.com/en/articles/9517075-what-are-projects
    accessed: 2026-09-25
  - title: Google Drive connector (project knowledge from Drive)
    url: https://claude.com/docs/connectors/google/drive
    accessed: 2026-09-25
---

# Projects in claude.ai

> **TL;DR** A Project is a claude.ai workspace with custom instructions and uploaded "project knowledge". Paid plans switch to RAG automatically when knowledge outgrows context, and Team/Enterprise can share projects. **Trial** as a zero-infrastructure stopgap: upload `library/index.md`, reviewed chunks and the EHCRP solicitation YAML so colleagues on the web can draft before the MCP server exists. Never make it canonical.

## What it is

- Available to all users (Free is limited to 5 projects). Holds files, text and code, plus custom instructions.
- Paid plans: RAG turns on automatically near context limits, "expanding capacity by up to 10x".
- Team/Enterprise: share with specific members or the whole org, with view or edit permission.
- Drive files can be added as knowledge only in **private** projects, and they refresh periodically.
- Claude Docs **can't** be put into a Project, though chats can (Docs connector guide).
- A new Projects version for Claude Code (cloud threads, project library) is rolling out to Pro/Max *(beta; details unverified)*.

## Why it matters for gentext

It is the lightest way to get the library in front of Claude web in the pilot window: no hosting, no OAuth. Custom instructions can carry the AGENTS.md truthfulness rules.

## How it would fit

- P0/P1 on the web: a shared "EHCRP Round 2" project. Knowledge = exported library Markdown (reviewed, shareable-tagged chunks only), glossary, solicitation YAML. Instructions = "cite chunk ids; use `[[NEEDS SOURCE]]`".
- A script (`gentext export-project`) builds the upload bundle from git, so the copy stays reproducible.
- Superseded in P2 by the MCP connector plus skills. The project may then stay as a place for instructions and chat history.

## Strengths

- Nothing to operate, and colleagues already know the UI.
- RAG copes with a library of hundreds of chunks.

## Weaknesses / risks

- **Low inspectability.** We can't see what RAG retrieved, and there's no per-call log.
- Read-only for Claude: no write-back, no checks, no provenance enforcement.
- Stale copies: every library change needs a re-upload, which is exactly the forked-copy problem DR-0002 found.
- Shared projects can't take Drive files, and confidentiality depends on who has access to the project.

## Verdict rationale

**Trial** only as a bridge for web users during the pilot. The MCP route is strictly better once hosted.

Parent: [index.md](index.md)
