---
title: Claude platform delivery surface
slug: index
level: 1
parent: ../index.md
related: [delivery-architecture.md, docs-roundtrip.md, ../storage-platforms/index.md, ../provenance/index.md]
tags: [claude, skills, mcp, plugins, delivery, collaboration]
status: draft
updated: 2026-09-25
---

# Claude platform delivery surface

> **TL;DR** Build one Python core (library + `adapt-rfp` CLI with JSON output). Wrap it twice: **Agent Skills** hold the workflow knowledge ("how to draft an EHCRP answer"), and a **remote MCP server** (FastMCP, Streamable HTTP, OAuth) holds data access and deterministic checks. Ship both as one **plugin**. Pilot in local Claude Code now. Claude web runs end to end once the MCP server is hosted and added as a custom connector. Claude Docs is the drafting surface. The final Google Doc stays a manual paste, because no official connector can edit an existing Google Doc.

## The question

How should adapt-rfp (DR-0003 M8 skills, M9 collaboration, M10 deployment) be exposed to Claude? The system has to work in Claude Code for the pilot (due 2026-10-13) and in claude.ai later ("claude web can operate the system end to end"). It also has to stay inspectable for a small team.

## The landscape (as of 2026-09-25)

| Surface | What it gives us | Runs where | Card |
|---|---|---|---|
| Agent Skills | `SKILL.md` instructions + scripts + references, loaded by progressive disclosure | Claude Code, claude.ai, API (no sync between them) | [agent-skills.md](agent-skills.md) |
| Plugins + marketplaces | One bundle of skills, commands, agents, hooks and MCP config; git-hosted catalog | Claude Code; claude.ai/Desktop via Team/Enterprise org sync | [claude-code-plugins.md](claude-code-plugins.md) |
| MCP servers / custom connectors | Tools, resources, prompts over stdio (local) or Streamable HTTP (remote) | Every Claude app (remote); Claude Code/Desktop (local) | [mcp-connectors.md](mcp-connectors.md) |
| FastMCP | Pythonic MCP server framework, fits the uv stack | Our server | [fastmcp.md](fastmcp.md) |
| Claude Docs | Living docs that Claude drafts, edits and comments on; tabs; export | claude.ai (beta since 2026-09-16), plus the Docs connector | [claude-docs.md](claude-docs.md) |
| Google Drive connector | Search and read Docs as Markdown; create new files | claude.ai, Claude Code | [google-drive-connector.md](google-drive-connector.md) |
| Projects | Shared knowledge + instructions, RAG when large | claude.ai | [claude-projects.md](claude-projects.md) |
| API: Citations | Sentence- or block-level grounding of claims | API only | [citations.md](citations.md) |
| API: other features | Structured outputs, Files, caching, Batch, memory, context editing, code execution, web search | API only | [api-features.md](api-features.md) |
| Agent SDK / headless | Claude Code's agent loop as a Python library; `claude -p` | Our machines or CI | [agent-sdk.md](agent-sdk.md) |

## Recommendation

1. **Core first, surfaces thin.** Every capability lives in `src/adapt_rfp/` and is reachable as `adapt-rfp <verb> --json`. Skills and MCP tools call it; they never re-implement it. This keeps QA deterministic (DR-0003) and testable without an LLM.
2. **Skills = procedure, MCP = data + actions.** Skills say *when* and *in what order* (draft → check → annotate). MCP tools do the reading, writing and checking, so the same tool calls work from claude.ai, where the sandbox can't see our repo.
3. **One plugin, one marketplace, in this repo.** `plugins/adapt-rfp/` holds `skills/` and `.mcp.json`. Claude Code installs it from git. On a Team/Enterprise plan the same repo syncs into claude.ai.
4. **Claude Docs for iteration, humans for the final paste.** Claude reads and edits Claude Docs through the Docs connector, and harvesting edited text back into `library/` goes through a adapt-rfp MCP tool. The Drive connector can *read* the final Google Doc for a last QA pass.
5. **Keep canonical state in git.** Claude Docs has no version history. Project knowledge and memory are caches, never the source of truth (DR-0005).

See [delivery-architecture.md](delivery-architecture.md) for the split and the phases, and [docs-roundtrip.md](docs-roundtrip.md) for the collaboration loop.

## Phased path

| Phase | When | Surface | Exit criterion |
|---|---|---|---|
| P0 Pilot | now → 2026-10-13 | Claude Code, project skills in `.claude/skills/`, local CLI, manual Claude Docs paste | One EHCRP answer drafted and checked |
| P1 Package | after pilot | Plugin + repo marketplace; optional local stdio MCP | A colleague installs it with one command |
| P2 Web read | M10 decision | Hosted FastMCP (read + check tools), custom connector, skills uploaded or org-provisioned | Claude web drafts and checks without a laptop |
| P3 Web write | later | Write tools (propose variant → git branch/PR), Docs harvest, Agent SDK batch jobs | Round trip closes from claude.ai |

## Open questions

- Which Claude plan does Hyphae use? Org-wide skill and plugin distribution and org connectors need Team or Enterprise. *(unverified for Hyphae)*
- Sources disagree on whether Claude Docs exports to Google Docs (see [claude-docs.md](claude-docs.md)).
- Where the MCP server is hosted and how it gets to the private repo is an M10 question. See [../storage-platforms/index.md](../storage-platforms/index.md).

## Children

- Level 2: [delivery-architecture.md](delivery-architecture.md) · [docs-roundtrip.md](docs-roundtrip.md)
- Level 3: [agent-skills.md](agent-skills.md) · [claude-code-plugins.md](claude-code-plugins.md) · [mcp-connectors.md](mcp-connectors.md) · [fastmcp.md](fastmcp.md) · [claude-docs.md](claude-docs.md) · [google-drive-connector.md](google-drive-connector.md) · [claude-projects.md](claude-projects.md) · [citations.md](citations.md) · [api-features.md](api-features.md) · [agent-sdk.md](agent-sdk.md)

Parent: [../index.md](../index.md)
