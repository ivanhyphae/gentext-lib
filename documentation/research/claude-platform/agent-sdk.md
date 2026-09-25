---
title: Claude Agent SDK and headless Claude Code
slug: agent-sdk
level: 3
parent: index.md
related: [api-features.md, claude-code-plugins.md, delivery-architecture.md]
tags: [agent-sdk, headless, automation, ci, managed-agents]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M0, M1, M7, M10]
license: Anthropic Commercial Terms (SDK); see repo LICENSE
maturity: mature
inspectability: high
sources:
  - title: Agent SDK overview
    url: https://code.claude.com/docs/en/agent-sdk/overview
    accessed: 2026-09-25
  - title: claude-agent-sdk-python (GitHub)
    url: https://github.com/anthropics/claude-agent-sdk-python
    accessed: 2026-09-25
---

# Claude Agent SDK and headless Claude Code

> **TL;DR** The Agent SDK runs Claude Code's agent loop as a Python or TypeScript library, with built-in tools, hooks, subagents, MCP, permissions and sessions. It loads skills and plugins from `.claude/` or a local path. `claude -p --output-format json` gives the same loop from a shell. **Trial** for unattended gentext jobs (ingest, nightly QA, harvest PRs) that reuse the *same* skills and MCP server as interactive use.

## What it is

- Python and TypeScript SDKs (repos `anthropics/claude-agent-sdk-python` and `-typescript`) wrap the Claude Code binary.
- **Capabilities:** built-in tools (files, bash, web), hooks, subagents, MCP, permissions, sessions (resume and fork). Skills, commands and memory load automatically from the project's `.claude/` and `~/.claude/`. Plugins load by local path.
- **Auth:** API key. Anthropic doesn't allow third-party products to offer claude.ai login or rate limits through the SDK unless approved. For internal jobs we use an API key.
- **Alternatives** from the same page: the Client SDK (write the loop yourself, or use the beta tool runner), and **Managed Agents**, a hosted harness where sessions run in an Anthropic-managed or self-hosted sandbox, configured through the API.

## Why it matters for gentext

The P3 pipelines (ingest new sources, re-run QA across drafts, open harvest PRs) are agentic. They read files, run the CLI and judge output, and they should behave exactly like a colleague's Claude Code session. With the SDK, one plugin serves both interactive and batch use, so skills don't drift.

## How it would fit

- `scripts/nightly_qa.py`: an SDK `query()` with `plugins=[{"type": "local", "path": "plugins/gentext"}]`, allowed tools restricted to Read/Bash(`gentext *`), a hook that blocks `projects/` reads, and output parsed to a report committed in a PR. *(Option names illustrative; check the Python reference.)*
- CI: `claude -p "run check-draft on drafts/ehcrp/*.md" --output-format json` in GitHub Actions.
- M10: Managed Agents is an option if we don't want to host a runner. *(assess later)*

## Strengths

- One agent definition for humans and robots, from the same git-tracked skills and plugin.
- Hooks and permissions give hard guardrails that prompts can't.
- Transcripts and tool calls are loggable by us.

## Weaknesses / risks

- Needs API billing and key management separate from claude.ai seats.
- Heavier than a plain API call for simple batch classification. Use [api-features.md](api-features.md) (Batch + structured outputs) there.
- The SDK tracks Claude Code releases closely, so pin versions in CI.

## Verdict rationale

**Trial** once the plugin exists (P1+). It is the most coherent way to automate without forking the method into separate code.

Parent: [index.md](index.md)
