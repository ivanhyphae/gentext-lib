---
title: Supabase (Postgres + pgvector + Auth + Edge Functions)
slug: supabase
level: 3
parent: index.md
related: [comparison.md, claude-web-access.md, remote-mcp-hosting.md, sqlite-fts5-vec.md]
tags: [postgres, pgvector, hosted, auth, mcp, phase-2]
status: draft
updated: 2026-09-25
kind: platform
verdict: assess
fit: [M2, M3, M5, M8, M10]
license: Apache-2.0 (platform OSS); hosted service commercial
maturity: mature
inspectability: medium
sources:
  - title: Supabase billing docs
    url: https://supabase.com/docs/guides/platform/billing-on-supabase
    accessed: 2026-09-25
  - title: Supabase pricing summary (secondary)
    url: https://uibakery.io/blog/supabase-pricing
    accessed: 2026-09-25
  - title: Supabase MCP server docs
    url: https://supabase.com/docs/guides/ai-tools/mcp
    accessed: 2026-09-25
  - title: Supabase remote MCP server announcement
    url: https://supabase.com/blog/remote-mcp-server
    accessed: 2026-09-25
  - title: Deploy MCP servers on Supabase (BYO MCP)
    url: https://supabase.com/docs/guides/ai-tools/byo-mcp
    accessed: 2026-09-25
  - title: Building an MCP server with mcp-lite on Edge Functions
    url: https://supabase.com/docs/guides/functions/examples/mcp-server-mcp-lite
    accessed: 2026-09-25
  - title: Hybrid search
    url: https://supabase.com/docs/guides/ai/hybrid-search
    accessed: 2026-09-25
  - title: Automatic embeddings
    url: https://supabase.com/docs/guides/ai/automatic-embeddings
    accessed: 2026-09-25
---

# Supabase (Postgres + pgvector + Auth + Edge Functions)

> **TL;DR** **Assess now, trial in phase 2.** Supabase is the strongest hosted option: Postgres with pgvector and hybrid search, Auth (it can act as the OAuth 2.1 server for an MCP endpoint), Storage, Edge Functions that can host our MCP server, and an official remote MCP server. Use it as a **derived, git-synced mirror**, not as the canonical store, and only once multi-user or always-on needs appear.

## What it is
A managed Postgres platform. Relevant pieces:
- **pgvector** (HNSW, `halfvec`) and **hybrid search** (tsvector + pgvector with reciprocal-rank fusion, documented recipe).
- **Automatic embeddings**: triggers plus pgmq, pg_net, and pg_cron call an Edge Function to (re)embed changed rows.
- **Auth**, with row-level security, and it can serve as the OAuth 2.1 authorization server for an MCP endpoint (`withOAuthProtectedResource` / `withSupabase` helpers), so each tool call runs as the signed-in user.
- **Edge Functions** (Deno/TypeScript). An official guide deploys an MCP server with `mcp-lite`.
- **Official MCP server** at `https://mcp.supabase.com/mcp` (OAuth), with tool groups for database, debugging, dev, edge functions, docs, branching, and storage. It supports read-only mode and project scoping.

**Pricing (2026-09, secondary sources; verify on supabase.com/pricing):** Free: 500 MB DB, 1 GB storage, 2 active projects, paused after 7 days inactive, no backups. Pro: $25/month per project with 8 GB DB and $10 compute credit. Team: $599/month.

## Why it matters for gentext
It's the one vendor that covers the whole phase-2 checklist: a shared live index, per-user auth tied to `sensitivity`/`owner` via RLS, file storage for source PDFs/DOCX (if DR-0004 permits), and a place to host the MCP server next to the data.

## How it would fit
- **One-way sync**: CI on push to `main` upserts chunks, variants, facts, and requirements into Postgres and re-embeds changed rows. Git stays canonical (DR-0005).
- Our MCP server (on Edge Functions, or Python elsewhere) queries Postgres. Writes still go out as PRs.
- The official Supabase MCP stays a **developer** tool against a dev project. Their docs warn about prompt injection through row content, and against connecting it to production.

## Strengths
- Postgres is open and inspectable (psql, Studio, `pg_dump`), and there's little lock-in. The same schema runs on Neon or self-hosted Postgres.
- Auth, storage, functions, and vectors in one bill, with good docs.

## Weaknesses / risks
- **Confidentiality**: a hosted copy of library text. Sync only chunks whose sensitivity allows it.
- The free tier pauses and has no backups, so real use means Pro ($25/month). That's fine, but it's a recurring cost.
- Edge Functions are TypeScript/Deno, while our code is Python (DR-0006). Either keep the MCP server in Python elsewhere, or maintain a thin TS layer.
- Two systems plus a sync job is less elegant than one repo.

## Verdict rationale
**Yes to Supabase, but later**, when a trigger in [index.md](index.md) fires. Before that it adds cost, a sync path, and a hosted copy of sensitive text without solving a problem we have.

Parent: [index.md](index.md)
