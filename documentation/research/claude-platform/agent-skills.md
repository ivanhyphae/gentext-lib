---
title: Agent Skills
slug: agent-skills
level: 3
parent: index.md
related: [claude-code-plugins.md, delivery-architecture.md, mcp-connectors.md]
tags: [skills, SKILL.md, progressive-disclosure]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M8, M6, M7]
license: n/a (format); Anthropic example skills in anthropics/skills
maturity: mature
inspectability: high
sources:
  - title: Agent Skills overview
    url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
    accessed: 2026-09-25
  - title: Use skills in Claude (Help Center)
    url: https://support.claude.com/en/articles/12512180-using-skills-in-claude
    accessed: 2026-09-25
  - title: Provision and manage skills for your organization
    url: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
    accessed: 2026-09-25
---

# Agent Skills

> **TL;DR** A skill is a folder: `SKILL.md` (YAML `name` + `description`, then instructions) plus optional reference files and scripts, loaded only when relevant. It is the right home for adapt-rfp's *procedures*: how to draft, check and harvest. **Adopt**, but give it data through MCP, because skills on the web run in a sandbox that can't see our repo.

## What it is

- **Format.** `SKILL.md` with frontmatter. `name` is ≤64 chars, lowercase/digits/hyphens, and may not contain "anthropic" or "claude". `description` is ≤1024 chars and must say what the skill does *and when to use it*. Everything else is Markdown and files.
- **Progressive disclosure.** Level 1 is metadata, always loaded, about 100 tokens per skill. Level 2 is the SKILL.md body, loaded on trigger, under 5k tokens recommended. Level 3 is bundled files, read on demand. Scripts run through bash and only their output enters context.
- **Surfaces.** Claude Code (`~/.claude/skills/`, `.claude/skills/`, or plugins; full network). claude.ai (zip upload under Customize → Skills; needs code execution; network full, partial or none by settings). API (`/v1/skills`, workspace-wide; runs in the code-execution container with **no network, no package installs**).
- **No sync.** Skills uploaded to one surface don't appear on the others.
- **Sharing on claude.ai.** The platform overview says custom skills are per user and can't be centrally managed. Newer Help Center articles describe Team/Enterprise **org provisioning** (Organization settings → Plugins & skills, on by default for all users), publishing to an org library, and direct sharing with colleagues. *Treat the Help Center as current and confirm in our admin console.*

## Why it matters for adapt-rfp

The README asks for "anthropic format skills". The format also mirrors our wiki: a short top file, then deeper references, the same progressive disclosure DR-0005 uses for the library. The existing `humanizer` skill can be chained into `check-draft`.

## How it would fit

- Skills: `find-copy`, `draft-answer`, `check-draft`, `model-solicitation`, `harvest-edits`, `ingest-source` (Claude Code only).
- Each SKILL.md states the workflow, the truthfulness rules (no invented facts, `{>>TK …<<}`), which MCP tools or CLI verbs to call, and where to stop for human review.
- `references/` holds the voice guide, a glossary summary and a funder-values crib. `scripts/` holds stdlib-only checks that also run in the claude.ai sandbox.
- Source of truth is `plugins/adapt-rfp/skills/` in git, published to each surface from there.

## Strengths

- Plain text, diffable and reviewable: very high inspectability.
- Costs almost no context until triggered, so many skills can coexist.
- The same file works in Claude Code, claude.ai, the API and the Agent SDK.

## Weaknesses / risks

- Triggering depends on how well the `description` is written. Test with evals (the `skill-creator` skill supports this).
- Runtime differs by surface (network, packages). Scripts must degrade gracefully.
- Skills aren't covered by ZDR, and a malicious skill can exfiltrate data. Only use our own or Anthropic's.
- Upload on claude.ai is manual per surface unless it is org-provisioned or plugin-synced.

## Verdict rationale

This is the native, most inspectable way to put method into Claude. It can't reach data by itself, so it pairs with [mcp-connectors.md](mcp-connectors.md) and ships through [claude-code-plugins.md](claude-code-plugins.md).

Parent: [index.md](index.md)
