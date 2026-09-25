---
title: FastMCP (Python)
slug: fastmcp
level: 3
parent: index.md
related: [mcp-connectors.md, delivery-architecture.md]
tags: [mcp, python, library, server]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M8, M10]
license: Apache-2.0
maturity: mature
inspectability: high
sources:
  - title: fastmcp on PyPI
    url: https://pypi.org/project/fastmcp/
    accessed: 2026-09-25
  - title: FastMCP docs
    url: https://gofastmcp.com/
    accessed: 2026-09-25
  - title: MCP Python SDK
    url: https://github.com/modelcontextprotocol/python-sdk
    accessed: 2026-09-25
---

# FastMCP (Python)

> **TL;DR** FastMCP is a decorator-based Python framework for MCP servers and clients. It defaults to Streamable HTTP and has built-in OAuth, and it fits the uv/Python ≥3.12 stack (DR-0006). **Adopt** for the gentext MCP server. One app serves stdio in Claude Code and HTTP for claude.ai.

## What it is

- Standalone project maintained by the Prefect team ([PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)). Apache-2.0. Latest release on PyPI is **4.0.10, released 2026-09-25**. It moves fast, so pin a version.
- FastMCP 1.0 was merged into the official MCP Python SDK in 2024 (`mcp.server.fastmcp`). The standalone package is the actively developed line (PyPI page).
- Features cited by the project and secondary sources: `@mcp.tool`, `@mcp.resource("chunk://{id}")`, `@mcp.prompt`; Streamable HTTP as the default HTTP transport; server-side OAuth and token validation (from 3.0); server composition; OpenTelemetry. Version-specific details are *(unverified against the 4.x docs)*.

## Why it matters for gentext

Tools can call `gentext` Python functions in-process. Type hints and Pydantic models become JSON schemas, which reuses our M2/M3/M5 models. The same module runs with `uv run gentext-mcp` over stdio (P1) and behind HTTPS (P2).

## How it would fit

```python
from fastmcp import FastMCP
from gentext import library, qa

mcp = FastMCP("gentext")

@mcp.tool(annotations={"readOnlyHint": True})
def search_chunks(query: str, type: str | None = None, limit: int = 10) -> list[library.ChunkHit]:
    """Find library chunks by meaning and metadata. Returns ids, titles, variant word counts."""
    return library.search(query, type=type, limit=limit)

@mcp.resource("chunk://{chunk_id}")
def chunk(chunk_id: str) -> str:
    return library.read_markdown(chunk_id)

@mcp.tool(annotations={"readOnlyHint": True})
def check_draft(text: str, solicitation: str, question_id: str) -> qa.Report:
    return qa.check(text, solicitation, question_id)
```

*(Illustrative sketch; confirm the decorator signatures against the pinned version.)*

## Strengths

- The least ceremony of any Python option, and it is idiomatic for a small team.
- Shows up in the tooling: Anthropic's `mcp-server-dev` plugin and the `mcp-builder` skill both target Python and FastMCP.
- Easy to test: call the functions directly in pytest, and use the MCP Inspector for protocol checks.

## Weaknesses / risks

- Rapid major versions (3.x → 4.x within 2026) mean API churn. Pin it and read release notes before upgrading.
- Some FastMCP features, such as sampling and subscriptions, aren't supported by Claude's client ([mcp-connectors.md](mcp-connectors.md)). Don't depend on them.
- The alternative is the official SDK's bundled `mcp.server.fastmcp`: slower moving, fewer features. It's a reasonable fallback if churn hurts.

## Verdict rationale

It matches the stack and has the shortest path from our library functions to typed tools. Its code is all Python we can read.

Parent: [index.md](index.md)
