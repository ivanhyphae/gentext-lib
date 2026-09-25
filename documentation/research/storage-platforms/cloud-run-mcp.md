---
title: Google Cloud Run for the gentext MCP server
slug: cloud-run-mcp
level: 3
parent: index.md
related: [remote-mcp-hosting.md, ../claude-platform/fastmcp.md, ../claude-platform/mcp-connectors.md]
tags: [mcp, hosting, google-cloud]
status: draft
updated: 2026-09-25
kind: platform
verdict: adopt
fit: [M8, M10]
license: proprietary (managed service)
maturity: mature
inspectability: high
sources:
  - title: Host MCP servers on Cloud Run (Google Cloud docs)
    url: https://docs.cloud.google.com/run/docs/host-mcp-servers
    accessed: 2026-09-25
---

# Google Cloud Run for the gentext MCP server

> **TL;DR** **Adopt** (DR-0009). Hyphae already uses Google Cloud, and Cloud Run officially hosts remote MCP servers over Streamable HTTP (and SSE; not stdio), naming FastMCP as a supported SDK. The one thing to solve is auth: Cloud Run defaults to IAM, while claude.ai connectors expect OAuth.

## What it is
A managed container runtime that scales to zero. Google's docs have a dedicated guide for MCP servers: "Cloud Run supports hosting MCP servers with streamable HTTP transport, but not MCP servers with stdio transport."

## Why it fits gentext
- It's the team's existing cloud: no new vendor, billing, or admin.
- Our server is small and mostly stateless (read, search, check tools over a baked-in SQLite index). That suits scale-to-zero containers.
- Container builds are reproducible and inspectable (Dockerfile + `uv.lock`).

## Auth options (from the guide)
- **IAM invoker (default):** every request needs the Cloud Run Invoker role.
- **`gcloud run services proxy`:** a local proxy that injects the caller's identity. Good for Claude Code on a laptop.
- **OIDC ID tokens:** for service-to-service calls.
- **claude.ai custom connector:** needs OAuth on a public URL. Likely pattern: allow unauthenticated invocation at the Cloud Run level and enforce OAuth in the app (e.g., a FastMCP auth provider backed by Google OAuth, restricted to the Hyphae domain). *(Approach unverified; confirm when implementing.)*

## Risks / to check at build time
- The guide doesn't cover scale-to-zero cold starts, pricing, or session affinity for stateful MCP sessions. Design tools to be stateless.
- The index must be rebuilt and redeployed when the library changes (CI on push to `main`).

## Sources
- Google Cloud, *Host MCP servers on Cloud Run*: https://docs.cloud.google.com/run/docs/host-mcp-servers (accessed 2026-09-25)
