---
title: Reaching the system from Claude web, and the "memory" question
slug: claude-web-access
level: 2
parent: index.md
related: [comparison.md, claude-code-web.md, remote-mcp-hosting.md, claude-memory-stores.md, agent-memory-services.md, supabase.md]
tags: [mcp, deployment, claude-web, memory, m8, m10]
status: draft
updated: 2026-09-25
---

# Reaching the system from Claude web, and the "memory" question

> **TL;DR** Claude web can reach our system in two ways. **Claude Code on the web** clones the private GitHub repo into a cloud VM and runs our CLIs and skills, with no server of ours. A **remote MCP server** added as a claude.ai custom connector gives chat and Claude Docs sessions typed tools. Do the first now and the second after the pilot, with writes returning as git PRs. The README's "third-party memory system" is not needed: our curated library *is* the memory. Anthropic's Markdown-file memory stores are the only memory product that matches our model.

## Path A: Claude Code on the web (zero infrastructure)

At claude.ai/code, each session gets an isolated VM with the repo cloned, authenticated through the Claude GitHub App. It's in research preview for Pro, Max, and Team, and for Enterprise premium seats. Skills in the repo, the `uv` CLIs, and a SQLite index rebuilt at session start all just work, and results come back as commits/PRs. This already meets "Claude web operates the system end to end" for technical users. See [claude-code-web.md](claude-code-web.md).

Limits: it's a coding surface, not the chat/Docs surface where drafting happens, and network access is restricted by default. Embedding APIs may need allow-listing *(unverified detail; check environment settings)*.

## Path B: our own remote MCP server (custom connector)

Custom connectors on claude.ai (Pro, Max, Team, Enterprise) need a **publicly reachable** Streamable-HTTP MCP endpoint. Claude connects from Anthropic's cloud, so a server behind a VPN won't work. OAuth is supported, including Dynamic Client Registration. On Team/Enterprise, an Owner adds the connector under Organization settings → Connectors.

Proposed server shape (M8):
- **Read tools**: `find_copy(query, type?, place?, max_words?)`, `get_chunk(id, variant?)`, `get_facts(ids)`, `get_requirements(solicitation, question?)`, `check_draft(text, solicitation, question)` (runs the M7 deterministic checks).
- **Write tools** that don't mutate canonical data directly: `propose_chunk`, `harvest_edit(doc_text, lineage)` → create a branch and PR through the GitHub API. Humans merge, CI validates the schema, and a push to `main` triggers a redeploy that rebuilds the index.
- **Sensitivity filter at the edge**: the server only loads chunks whose `sensitivity` allows hosted use. `projects/` never ships (DR-0004).

Hosting options are compared in [remote-mcp-hosting.md](remote-mcp-hosting.md). In short: **FastMCP + Prefect Horizon** is the shortest path for a Python codebase (free personal tier, GitHub-driven redeploys, built-in OAuth). **Fly.io / Render / Cloud Run** are generic container hosts. **Cloudflare Workers** fits best if we write the server in TypeScript, which we won't. **Supabase Edge Functions** make sense in phase 2, when Supabase already holds the mirror.

Why not just use vendor MCP servers (GitHub, Supabase, Notion)? They expose *their* primitives (files, SQL, pages), not ours (chunks, variants, requirements, checks). Claude would have to rediscover the schema in every session, and the Supabase docs themselves warn against pointing their MCP at production data because of prompt-injection risk. They're useful as developer tools, not as the product surface. Also, the GitHub remote MCP server has had a history of claude.ai connector auth incompatibility (issue #549, closed as stale). Check current status before relying on it.

## The memory question

"Memory systems" fall into three families:

| Family | Examples | What it stores | Fit |
|---|---|---|---|
| Extracted conversational memory | mem0, Supermemory, Zep (hosted) | LLM-extracted facts/preferences from chats, vector + graph | Poor. Opaque extraction, and it duplicates our fact registry without provenance |
| Temporal knowledge graph | Graphiti (OSS core of Zep) | entities/relations with validity windows | Interesting for M3 facts with validity, but `graph-keeper` (RDF in git) is more inspectable |
| File-based agent memory | Anthropic memory tool, Managed Agents memory stores, Letta MemFS/Context Repositories | Markdown files the agent reads/writes, often versioned | Good. Same shape as our library |

Cards: [claude-memory-stores.md](claude-memory-stores.md), [agent-memory-services.md](agent-memory-services.md).

The trend matters here: Anthropic (memory stores, Apr 2026 beta, immutable versions) and Letta (git-backed Context Repositories, Feb 2026) both moved toward **versioned Markdown files**, not vector blobs. That's the architecture DR-0005 already picked. So "use a third-party memory system for production" should become **"let agents keep *working* memory (session notes, user preferences, open tasks) in a file-based store, while the curated library stays in git."** Never let an extraction service write library content.

## Recommended sequence

1. **Pilot**: Path A only. Write a `SessionStart` script that runs `uv sync && gentext index rebuild`.
2. **After the pilot**: a Path B server with read tools, then check tools, then PR-based write tools. Record it in a deployment DR (M10).
3. **Production**: if the triggers in [index.md](index.md) fire, add the Supabase mirror behind the same MCP tool contract, so clients don't change.

## Sources

- Claude Code on the web: https://code.claude.com/docs/en/claude-code-on-the-web (accessed 2026-09-25)
- Custom connectors via remote MCP: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp (accessed 2026-09-25)
- Building custom connectors: https://support.anthropic.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers (accessed 2026-09-25)
- Supabase MCP security guidance: https://supabase.com/docs/guides/ai-tools/mcp (accessed 2026-09-25)
- GitHub MCP / claude.ai issue: https://github.com/github/github-mcp-server/issues/549 (accessed 2026-09-25)
- Managed Agents memory: https://platform.claude.com/docs/en/managed-agents/memory (accessed 2026-09-25)
- Letta Context Repositories: https://www.letta.com/blog/context-repositories/ (accessed 2026-09-25)

Parent: [index.md](index.md)
