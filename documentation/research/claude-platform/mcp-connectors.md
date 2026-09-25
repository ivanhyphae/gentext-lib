---
title: MCP servers and custom connectors
slug: mcp-connectors
level: 3
parent: index.md
related: [fastmcp.md, claude-code-plugins.md, delivery-architecture.md, ../storage-platforms/index.md]
tags: [mcp, connectors, remote, oauth, streamable-http]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M8, M10, M2, M5, M7]
license: MCP spec open (modelcontextprotocol.io)
maturity: mature
inspectability: medium
sources:
  - title: Build an MCP server for Claude
    url: https://claude.com/docs/connectors/building
    accessed: 2026-09-25
  - title: Get started with custom connectors using remote MCP
    url: https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp
    accessed: 2026-09-25
  - title: Claude Code MCP
    url: https://code.claude.com/docs/en/mcp
    accessed: 2026-09-25
---

# MCP servers and custom connectors

> **TL;DR** An MCP server exposes **tools** (actions), **resources** (addressable content) and **prompts** (templates). Locally that runs over stdio in Claude Code/Desktop; remotely over Streamable HTTP, which claude.ai reaches from Anthropic's cloud as a *custom connector*. **Adopt.** A hosted gentext MCP server is the only way Claude web can reach our library and checks.

## What it is

- **Transports.** stdio (a local process), Streamable HTTP (recommended for remote), and legacy SSE (being deprecated). Claude Code also accepts WebSocket.
- **Claude's client supports** tools, prompts, resources, text and image tool results, and text and binary resources. It **doesn't** support resource subscriptions, sampling, or draft capabilities. Optional **MCP Apps** render interactive UI in the conversation.
- **Limits.** On claude.ai and Desktop, results are capped at ~150,000 characters and tool calls time out at 240 s. Claude Code caps results at 25,000 tokens by default (`MAX_MCP_OUTPUT_TOKENS`, `MCP_TOOL_TIMEOUT`).
- **Auth.** OAuth 2.0 per user (MCP auth specs 2025-03-26, 2025-06-18 and 2025-11-25; Dynamic Client Registration or a pre-registered client; callback `https://claude.ai/api/mcp/auth_callback`), a static org credential sent as a header, or none. Enterprise Managed Auth (SSO) is available.
- **Reachability.** claude.ai connects from Anthropic's cloud, so the server must be public HTTPS, or allow-list Anthropic's IP ranges.
- **Adding it.** Pro/Max users add a URL themselves. On Team/Enterprise an Owner adds it and each member authenticates. The free plan allows one custom connector. Connectors added on claude.ai also show up in Claude Code when logged in with that account.
- **Claude Code scopes:** local (`~/.claude.json`), project (`.mcp.json`, committed) and user.

## Why it matters for gentext

Skills on the web can't see our repo ([agent-skills.md](agent-skills.md)). MCP is the bridge. The same server also serves Claude Code, the Agent SDK and the API's MCP connector (beta), so one implementation covers every surface.

## How it would fit

- **Tools:** `search_chunks`, `get_chunk`, `lookup_fact`, `glossary_check`, `get_requirements`, `compliance_matrix`, `draft_context`, `check_draft` (all `readOnlyHint`); later `propose_variant` (writes a branch/PR, `destructiveHint: false`, and it asks for confirmation).
- **Resources:** `library://index`, `chunk://{id}`, `solicitation://{funder}/{program}/{round}`, so Claude can attach canonical text, not paraphrase.
- **Prompts:** `draft-question`, `qa-pass`. These are thin, and the method lives in skills.
- Responses are compact JSON with ids for provenance. Paginate search. Never return raw `projects/` sources (DR-0004).

## Strengths

- Works across every Claude surface. It's an open standard, not tied to Claude.
- Typed schemas plus server-side logging make every call auditable.
- It matches DR-0003: deterministic tools that the LLM orchestrates.

## Weaknesses / risks

- Hosting, OAuth and uptime are new operational burdens (M10).
- Prompt injection from tool results. Our content is ours, but pasted solicitation text is external.
- Tool descriptions compete for context. Keep the tool list small, since Claude Code's tool search helps only there.
- Inspectability is **medium**: the server is ours and logged, but claude.ai-side call history lives only in chat transcripts.

## Verdict rationale

This is the required path to the README's "claude web end to end" target. Build it after the pilot, starting with a stdio server in P1 and the same code over HTTP in P2. Implement it with [fastmcp.md](fastmcp.md).

Parent: [index.md](index.md)
