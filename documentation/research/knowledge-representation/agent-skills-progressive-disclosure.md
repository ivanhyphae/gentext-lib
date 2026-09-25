---
title: Agent Skills progressive disclosure
slug: agent-skills-progressive-disclosure
level: 3
parent: index.md
related: [llms-txt.md, llm-wiki-pattern.md, retrieval-design.md]
tags: [progressive-disclosure, skills, anthropic]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M2, M8]
license: open standard (agentskills.io)
maturity: mature
inspectability: high
sources:
  - title: "Equipping agents for the real world with Agent Skills (Anthropic Engineering)"
    url: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
    accessed: 2026-09-25
---

# Agent Skills progressive disclosure

> **TL;DR** Agent Skills load in three tiers: frontmatter `name`/`description` at startup, the `SKILL.md` body when relevant, and bundled files on demand. Adopt the same tiering for the library (index summary, then chunk frontmatter and body, then variants and sources), and expose it through skills such as `find-copy`.

## What it is
Anthropic describes Agent Skills (post dated 2025-10-16) as folders with a `SKILL.md`. Level 1 is the YAML `name` and `description`, preloaded so Claude knows when a skill applies. Level 2 is the full `SKILL.md`, read when the skill is triggered. Level 3 and beyond are referenced files (e.g. `reference.md`) that Claude opens selectively, which makes the usable context "effectively unbounded". The post likens it to "a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix". An update dated 2025-12-18 says Agent Skills were published as an open standard at agentskills.io, supported across Claude.ai, Claude Code, the Agent SDK and the Developer Platform ([anthropic.com](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), accessed 2026-09-25).

## Why it matters for gentext
Claude is the main LLM, and skills are our planned M8 surface. If the library uses the same disclosure pattern as the skills that read it, Claude navigates it "natively": a short summary tells it whether to open a file, and a file tells it where the details live.

## How it would fit
| Skill tier | Library analogue |
|---|---|
| `description` | `summary` line in `library/index.md` / type index |
| `SKILL.md` body | chunk file: frontmatter + canonical variant |
| referenced files | other variants, source excerpts, fact records, lineage |

- A `find-copy` skill's `SKILL.md` says: read `library/index.md`, filter by type and place, open at most N chunks, and prefer an existing length variant.
- Registry lookups go through scripts bundled in the skill (deterministic), not through prose.

## Strengths
- A proven pattern, first-party for Claude, and it works identically in Claude Code and Claude web.
- Forces good `summary` writing, which also improves BM25 and embeddings ([retrieval-design.md](retrieval-design.md)).

## Weaknesses / risks
- It depends on filesystem or MCP access to the repo from Claude web (a deployment question, M10).
- Summaries drift from bodies unless they are regenerated or checked (add an M7 check).

## Verdict rationale
Adopt: it is the organizing principle for the M2 layout and the M8 skills.

Up: [knowledge representation](index.md)
