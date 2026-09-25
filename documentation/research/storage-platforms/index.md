---
title: Storage and platforms
slug: index
level: 1
parent: ../index.md
related: [comparison.md, claude-web-access.md, ../../decision-record/0005-canonical-store-plain-text.md, ../../decision-record/0003-module-decomposition.md]
tags: [storage, deployment, mcp, memory, m10]
status: draft
updated: 2026-09-25
---

# Storage and platforms

> **TL;DR** Keep the private git repo of Markdown and YAML as the only canonical store (DR-0005). Rebuild a single SQLite file (FTS5 plus sqlite-vec) as the derived index. Reach it from Claude web first through Claude Code on the web (no server), then through a thin remote MCP server. Use Supabase only later, as a *derived* hosted mirror, and only if we need multi-user writes or always-on hosted search. Don't use Notion as the store. Don't adopt a third-party "memory" product: the library already is the memory.

## The question

Where do canonical chunks, registries, and solicitation models live? Where do the derived indexes (metadata, full text, embeddings) live? And what lets Claude web run the whole system end to end (README target)? The lens is **powerful, elegant, inspectable**, for a small team, with confidential sources (DR-0004).

A fact that shapes every choice: **the corpus is small.** The pilot will yield about 15–25 chunks. A mature library is likely hundreds to a few thousand chunks with variants. Brute-force vector search over 10k vectors takes milliseconds on one CPU, so we need no ANN index, no vector-DB service, and no scaling story. What we do need is reviewability, provenance, and reachability from Claude web.

## Landscape

| Layer | Options | Page |
|---|---|---|
| Canonical store | git + Markdown/YAML (Obsidian as an optional viewer); Dolt; Notion; Airtable/Grist; Postgres | [comparison.md](comparison.md) |
| Derived index | SQLite + FTS5 + sqlite-vec; DuckDB + vss; LanceDB; Postgres + pgvector; hosted vector DBs | [comparison.md](comparison.md) |
| Claude web access | Claude Code on the web; remote MCP on Cloudflare / FastMCP Horizon / Fly / Render / Supabase Edge | [claude-web-access.md](claude-web-access.md) |
| Agent memory | Anthropic memory tool and Managed Agents memory stores; mem0; Zep/Graphiti; Letta; Supermemory | [claude-web-access.md](claude-web-access.md) |

### Cards (level 3)

- [git-markdown-vault.md](git-markdown-vault.md): git + Markdown/YAML as canonical. **adopt**
- [sqlite-fts5-vec.md](sqlite-fts5-vec.md): SQLite, FTS5, sqlite-vec as the derived index. **adopt**
- [duckdb-vss.md](duckdb-vss.md): DuckDB + vss for analytics. **assess**
- [lancedb.md](lancedb.md): embedded vector + FTS store. **assess**
- [dolt.md](dolt.md): version-controlled SQL database. **hold**
- [supabase.md](supabase.md): Postgres + pgvector + Auth + Edge + MCP. **assess**, becoming **trial** in phase 2
- [notion.md](notion.md): Notion as DB/CMS. **hold** as canonical store
- [hosted-vector-dbs.md](hosted-vector-dbs.md): Turbopuffer, Pinecone, Qdrant. **hold**
- [claude-code-web.md](claude-code-web.md): Claude Code on the web over the git repo. **trial**
- [remote-mcp-hosting.md](remote-mcp-hosting.md): where to host our MCP server. **trial**
- [cloud-run-mcp.md](cloud-run-mcp.md): Google Cloud Run, the chosen host (DR-0009). **adopt**
- [claude-memory-stores.md](claude-memory-stores.md): Anthropic memory tool and Managed Agents memory stores. **assess**
- [agent-memory-services.md](agent-memory-services.md): mem0, Zep/Graphiti, Letta, Supermemory. **hold**

## Recommendation, phased

**Phase 0: pilot (now to the 2026-10-13 deadline).** Use git and a local derived SQLite index (`adapt-rfp index rebuild`). Claude Code runs locally, and teammates can use Claude Code on the web against the same private GitHub repo. Nothing is hosted and no new vendor sees confidential text. Claude web chat only receives pasted or exported artifacts.

**Phase 1: Claude web end to end (after the pilot).** Build one **remote MCP server** in Python with FastMCP, matching DR-0006. It serves read tools (`find_copy`, `get_chunk`, `get_requirements`, `check_draft`) from a repo checkout plus a SQLite index built at deploy time. Write tools (`propose_chunk`, `harvest_edit`) open a **branch/PR** on the repo instead of mutating state, which keeps every change reviewable. Host it on FastMCP Horizon (free personal tier) or on Fly/Render/Cloud Run, with OAuth so it works as a claude.ai custom connector. Redeploy on push to `main`.

**Phase 2: production, only if triggered.** Adopt **Supabase** (Postgres + pgvector + Auth + Storage + Edge Functions) when any of these become true: several non-technical people need to write concurrently, reads must be always-on and low-latency beyond what a redeploy-on-push container gives, or we need per-user row-level permissions tied to the `sensitivity` field. Even then, sync one way, **git → Supabase**. Postgres is an index and a serving layer, and moving canonicity into it would need a new DR superseding DR-0005.

### Direct answers

- **Should we use Supabase?** Not for the pilot. It's the best candidate for phase 2 because it bundles Postgres + pgvector + hybrid search, Auth, Edge Functions that can host an MCP server, and an official MCP server. Adopt it when a trigger above fires, as a derived mirror. See [supabase.md](supabase.md).
- **Should we use Notion?** Not as the store. Rich-text properties cap at 2,000 characters per request, the API allows 3 req/s on non-Business plans, and there is a Markdown *read* endpoint but no Markdown write. Notion history is also not diffable the way git is. Notion could later be a one-way *published catalog* for colleagues who live there. See [notion.md](notion.md).
- **Third-party memory?** Hold. Those products extract "facts about the user" from chat. Our memory is the curated library, with provenance. If we move to Anthropic Managed Agents, its Markdown memory stores are the natural fit. See [claude-web-access.md](claude-web-access.md).

## Date sensitivity

Pricing, free tiers, and beta status on these pages were checked on 2026-09-25 and go stale quickly. Re-verify before any purchase or DR.

Parent: [../index.md](../index.md)
