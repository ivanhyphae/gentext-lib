---
title: Notion as database / CMS
slug: notion
level: 3
parent: index.md
related: [comparison.md, git-markdown-vault.md, claude-web-access.md]
tags: [cms, database, saas, mcp, collaboration]
status: draft
updated: 2026-09-25
kind: product
verdict: hold
fit: [M2, M9]
license: proprietary SaaS
maturity: mature
inspectability: low
sources:
  - title: Notion API request limits
    url: https://developers.notion.com/reference/request-limits
    accessed: 2026-09-25
  - title: Retrieve a page as markdown
    url: https://developers.notion.com/reference/retrieve-page-markdown
    accessed: 2026-09-25
  - title: Notion's hosted MCP server, an inside look
    url: https://www.notion.com/blog/notions-hosted-mcp-server-an-inside-look
    accessed: 2026-09-25
  - title: Official Notion MCP server repository
    url: https://github.com/makenotion/notion-mcp-server
    accessed: 2026-09-25
  - title: Notion MCP deep dive (secondary)
    url: https://www.stackone.com/blog/notion-mcp-deep-dive/
    accessed: 2026-09-25
---

# Notion as database / CMS

> **TL;DR** **Hold** as the canonical store. Notion is the friendliest editing and browsing UI and has a good hosted MCP server, but its API is built around blocks with small per-request limits, it can read Markdown but not write it, and it offers no diffable history. That clashes with provenance and inspectability. If the team lives in Notion, consider a later **one-way published catalog** from git into a Notion database.

## What it is
A block-based docs and databases workspace. Its API models databases as **data sources** (API version 2025-09-03, a breaking migration). A **hosted MCP server** (`mcp.notion.com`, OAuth) exposes search, fetch, create and update pages, data-source queries, views, and comments. It works with page content as token-efficient "enhanced Markdown".

## Why it matters for adapt-rfp
Colleagues could browse and filter chunks by type, place, or funder in a familiar UI, and Claude web can already reach Notion through its connector.

## Limits that matter (verified 2026-09-25)
- **Rate**: 180 req/min per connection (about 3/s) on most plans, 600/min on Business/Enterprise, plus a shared per-workspace limit.
- **Size**: rich-text values are capped at **2,000 characters** per request object, with 100-element block arrays, 1,000 blocks and 500 KB per request. A 350-word chunk must be split across several rich-text objects.
- **Markdown**: `GET /v1/pages/{id}/markdown` exists (truncates beyond about 20k blocks). **There is no Markdown write endpoint**, so writes go through the block API. (The hosted MCP can replace page content in Markdown; secondary source.)
- **MCP**: page-level operations, no block-level editing, no database deletion. Data-source query power depends on the plan. It's built for interactive OAuth and doesn't take bearer tokens (secondary source).

## How it would fit (if at all)
Phase 2+: CI publishes `library/` into a Notion database (title, type, summary, variants as child blocks, link back to the git path). It's read-only by convention, and edits come back through the M9 harvest path, never by syncing Notion → git automatically.

## Strengths
- Best-in-class UI for non-technical colleagues, plus comments.
- Mature hosted MCP; Claude web connector available.

## Weaknesses / risks
- **Inspectability is low**: history isn't exportable as diffs, and the data lives in the vendor's block model.
- Two-way sync with git is fragile (block-to-Markdown round-trips lose structure).
- Rate limits hurt bulk rebuilds, and vendor lock-in is high.
- DR-0004: another SaaS holding library text.

## Verdict rationale
Notion is a good *window* on the library and a bad *foundation* for it. Decide later, and only if colleagues actually ask to browse there. Claude Docs already covers iterative editing (M9).

Parent: [index.md](index.md)
