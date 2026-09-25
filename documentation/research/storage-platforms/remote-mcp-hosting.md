---
title: Hosting a remote MCP server for Claude web
slug: remote-mcp-hosting
level: 3
parent: index.md
related: [claude-web-access.md, claude-code-web.md, supabase.md, sqlite-fts5-vec.md]
tags: [mcp, hosting, oauth, deployment, m8]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M8, M10]
license: varies (FastMCP Apache-2.0; hosts commercial)
maturity: emerging
inspectability: medium
sources:
  - title: Custom connectors using remote MCP (Claude Help Center)
    url: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
    accessed: 2026-09-25
  - title: FastMCP, Prefect Horizon deployment
    url: https://gofastmcp.com/deployment/prefect-horizon
    accessed: 2026-09-25
  - title: Prefect Horizon
    url: https://www.prefect.io/horizon
    accessed: 2026-09-25
  - title: Cloudflare, Build a remote MCP server
    url: https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/
    accessed: 2026-09-25
  - title: Supabase, Deploy MCP servers
    url: https://supabase.com/docs/guides/ai-tools/byo-mcp
    accessed: 2026-09-25
  - title: Fly.io pricing update (effective 2026-10-01)
    url: https://fly.io/pricing-update/
    accessed: 2026-09-25
  - title: Render free tier
    url: https://render.com/docs/free
    accessed: 2026-09-25
---

# Hosting a remote MCP server for Claude web

> **TL;DR** **Trial after the pilot.** Write the server in Python with FastMCP. Bake the repo checkout and SQLite index into the deploy, and route writes to GitHub PRs. Host first on **FastMCP/Prefect Horizon** (free for personal servers, redeploys on push, built-in OAuth). **Fly.io or Render** are portable container fallbacks. Cloudflare Workers and Supabase Edge Functions are TypeScript-first, so choose them only if we already live there.

## Requirements from Claude
A custom connector (Pro/Max/Team/Enterprise) needs a **publicly reachable** Streamable-HTTP endpoint, because Claude connects from Anthropic's cloud. OAuth is supported (client ID/secret in Advanced settings; DCR supported). On Team/Enterprise, an Owner adds it under Organization settings → Connectors. An unauthenticated server is fine for testing only, and serving private library text requires auth.

## Options (2026-09)

| Host | Language | Auth | Cost | Notes |
|---|---|---|---|---|
| **Prefect Horizon** (formerly FastMCP Cloud) | Python (FastMCP) | built-in OAuth | free personal tier; pay for production compute | connect GitHub repo → deploy in about 60 s, redeploy on push to `main`, PR previews. Whether its OAuth works cleanly with claude.ai is *unverified*; test it |
| **Fly.io** | any container | our own (e.g. GitHub/Google OAuth via FastMCP auth providers) | pay-as-you-go; stopped Machines still bill rootfs; memory $6/GB-mo from 2026-10-01 | scale-to-zero possible; volumes available |
| **Render** | any container | our own | free web service sleeps after 15 min idle, about 1 min cold start | cold starts may time out connector calls *(unverified)*; paid tier avoids that |
| **Cloudflare Workers** | TypeScript (Python Workers exist but aren't the documented MCP path) | Cloudflare Access or third-party OAuth via `workers-oauth-provider` | generous free tier | use `createMcpHandler()`. `McpAgent` and the quick-deploy templates are **deprecated** for new servers |
| **Supabase Edge Functions** | TypeScript/Deno (`mcp-lite`) | Supabase Auth as OAuth 2.1 server | included with Supabase plan | best when data is already in Supabase (phase 2) |
| Google Cloud Run *(not researched in depth)* | any container | our own | scale-to-zero | option if Hyphae's Google Workspace/GCP is the home |

## How it would fit
- `src/adapt_rfp/mcp_server.py` (FastMCP) imports the same library code as the CLIs, so there's a single implementation.
- Build step: `adapt-rfp index rebuild --sensitivity-max=<hosted>` → `index.db` baked into the image. Data is read-only at runtime.
- Write tools use a GitHub App token scoped to the repo to open PRs, and never push to `main`.
- Log every tool call (tool, args, chunk ids returned) for inspectability.

## Strengths
- One Python codebase serves CLI, skills, and MCP.
- Stateless and read-only at runtime, so it's safe, cheap, and easy to reason about.

## Weaknesses / risks
- **Hosting confidential text** (even filtered) on a third party. Needs a sensitivity policy (DR-0004).
- OAuth setup is the fiddliest part, and connector compatibility bugs have happened (e.g. the GitHub MCP issue). Budget a day for it.
- Index freshness depends on the redeploy. Fine for a library that changes a few times a week.

## Verdict rationale
It's the smallest server that makes Claude web chat and Claude Docs sessions first-class users of the library, and it doesn't touch canonicity.

Parent: [index.md](index.md)
