---
title: git + Markdown/YAML vault
slug: git-markdown-vault
level: 3
parent: index.md
related: [comparison.md, sqlite-fts5-vec.md, claude-code-web.md, dolt.md, ../../decision-record/0005-canonical-store-plain-text.md]
tags: [canonical-store, git, markdown, yaml, obsidian]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M2, M3, M5, M10]
license: n/a (git GPL-2.0; Obsidian proprietary, free for work)
maturity: mature
inspectability: high
sources:
  - title: Obsidian is now free for work
    url: https://obsidian.md/blog/free-for-work/
    accessed: 2026-09-25
  - title: Letta, Context Repositories (git-based agent memory)
    url: https://www.letta.com/blog/context-repositories/
    accessed: 2026-09-25
  - title: Claude Managed Agents memory (versioned Markdown stores)
    url: https://platform.claude.com/docs/en/managed-agents/memory
    accessed: 2026-09-25
---

# git + Markdown/YAML vault

> **TL;DR** **Adopt.** A private git repo with one Markdown file per chunk (YAML frontmatter) and YAML registries is the canonical store. It's the most inspectable option available, LLMs read it natively, it costs nothing, and the agent-memory field is converging on the same design.

## What it is
A folder tree (`library/`, `solicitations/`, `library/glossary/`) under git. Chunks are `.md` with frontmatter, and facts, entities, and solicitations are `.yaml`. It's "Obsidian-style" in that the same folder opens as an Obsidian vault with wikilinks and a properties UI, but nothing depends on Obsidian.

## Why it matters for adapt-rfp
- **Provenance and lineage for free**: `git log -p` and `git blame` show who changed which sentence, and PRs are the review gate for "promoted into library".
- **Progressive disclosure**: `library/index.md` → type index → chunk, which is how Claude navigates best (DR-0005).
- **Portable**: any future store (SQLite, Supabase, a memory store) is a projection of the repo.
- **Converging design**: Anthropic's Managed Agents memory stores (Markdown files with immutable versions, Apr 2026 beta) and Letta's git-backed Context Repositories (Feb 2026) both choose files plus versioning for agent memory.

## How it would fit
- JSON Schema (or Pydantic) for frontmatter, validated by a pre-commit hook and CI.
- `adapt-rfp index rebuild` projects the repo into [SQLite](sqlite-fts5-vec.md).
- Claude reaches it locally, through [Claude Code on the web](claude-code-web.md), or through our [MCP server](remote-mcp-hosting.md), whose writes become PRs.

## Strengths
- Maximal inspectability, diffable prose, trivial backup, no vendor.
- Works offline, and every tool (grep, Vale, spaCy) reads it directly.

## Weaknesses / risks
- **Concurrent non-technical editing** is weak. We mitigate with the Claude Docs round-trip (M9), Obsidian for viewing, and PR-producing MCP write tools.
- **No query engine**: needs the derived index for search.
- Schema drift without validation. Solve it with CI.
- Merge conflicts on the same chunk. Keep chunks small, one file each.

## Verdict rationale
It's the only option that fully satisfies "inspectable" at zero cost and still leaves every hosted option open as a derived layer. The known weakness (multi-writer editing) has a planned mitigation (M9) and a phase-2 escape hatch ([supabase.md](supabase.md)).

Parent: [index.md](index.md)
