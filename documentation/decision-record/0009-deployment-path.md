# 0009. Deployment path: Claude Code clone as MVP, small MCP server on Google Cloud Run next

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
- README target: Claude web operates the system end to end.
- Research (`documentation/research/storage-platforms/`, `claude-platform/`): Claude Code (local or on the web) can clone the repo and run the CLI and skills with no server. Claude.ai custom connectors need a remote MCP server (Streamable HTTP) reachable over the internet with OAuth.
- Hyphae already uses **Google Cloud**. Cloud Run officially supports hosting remote MCP servers over Streamable HTTP (and SSE), not stdio, and names FastMCP as an option (https://docs.cloud.google.com/run/docs/host-mcp-servers, accessed 2026-09-25).

## Decision
1. **MVP:** Claude Code clones the repo and runs the `gentext` CLI + skills directly. This covers the pilot (to 2026-10-13).
2. **Next:** a small Python **FastMCP** server in a container on **Google Cloud Run**, exposing read, search, and check tools over the same core library. The library index is baked into the image at build time or pulled from the repo on start. Write tools open GitHub PRs and never mutate canonical data directly.
3. Supabase, other hosts, and agent-memory products are out of scope unless a later DR brings them back.

## Consequences
- One cloud vendor, already billed and administered by the team. Cloud Run scales to zero, so an idle server costs close to nothing *(pricing to confirm at build time)*.
- **Auth mismatch to solve:** Cloud Run's default auth is IAM invoker (fine for `gcloud run services proxy` from Claude Code), but claude.ai connectors need OAuth. Likely approach: allow unauthenticated invocation at the Cloud Run level and enforce OAuth inside the app (FastMCP auth provider, e.g. Google OAuth restricted to the Hyphae domain). Confirm in the implementation DR.
- Stateful MCP sessions on an autoscaling service: prefer stateless tool calls. Check session-affinity needs when implementing.

## Alternatives considered
- Prefect Horizon / Fly / Render (research suggestions): viable, but they add a vendor the team doesn't already use.
- Supabase edge functions: a second platform with no gain at our scale.

## Revisions
