---
title: Claude Code plugins and marketplaces
slug: claude-code-plugins
level: 3
parent: index.md
related: [agent-skills.md, mcp-connectors.md, delivery-architecture.md]
tags: [plugins, marketplace, distribution, hooks]
status: draft
updated: 2026-09-25
kind: platform
verdict: adopt
fit: [M8]
license: n/a (format)
maturity: mature
inspectability: high
sources:
  - title: Plugin manifest reference
    url: https://code.claude.com/docs/en/plugins-reference
    accessed: 2026-09-25
  - title: Host and maintain a marketplace
    url: https://code.claude.com/docs/en/plugins/host-marketplace
    accessed: 2026-09-25
  - title: Manage plugins for your organization (Help Center)
    url: https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization
    accessed: 2026-09-25
---

# Claude Code plugins and marketplaces

> **TL;DR** A plugin bundles skills, commands, agents, hooks and MCP server configs under `.claude-plugin/plugin.json`. A marketplace is a git-hosted `marketplace.json` catalog. On Team/Enterprise the same private repo syncs into claude.ai, Desktop and Cowork. **Adopt** as the single package for adapt-rfp's Claude surface.

## What it is

- **Layout** (defaults): `.claude-plugin/plugin.json` (optional manifest), `skills/<name>/SKILL.md`, `commands/` (legacy; prefer skills), `agents/`, `hooks/hooks.json`, `.mcp.json`, `.lsp.json`, `output-styles/`, `monitors/`, `bin/` (put on PATH in Claude Code), `settings.json`.
- **Manifest** fields include `name`, `version`, `mcpServers` (path, inline map, `.mcpb` bundle or URL) and `userConfig`, which prompts the user for values such as a server URL or token. Paths must start with `./`. `${CLAUDE_PLUGIN_ROOT}` resolves to the installed location.
- **Marketplace.** Users run `/plugin marketplace add owner/repo` (or a git URL, a hosted `marketplace.json` URL, or a shared directory), then `/plugin install name@marketplace`. `--scope project` writes `.claude/settings.json` so everyone in a repo gets it. Private repos use the user's own git credentials. Auto-update is off by default. Bump `version` or omit it to track commits.
- **claude.ai org sync** (Team/Enterprise). Organization settings → Plugins & skills connects a private GitHub/GitLab repo, or accepts a zip upload (≤200 MB). Plugins then appear in web chat, Desktop chat, Cowork and Claude Code. Restrictions: the repo must be private or internal, and **no top-level `bin/`**.
- `claude plugin validate .` checks the manifest and catalog.

## Why it matters for adapt-rfp

It is the one artifact that carries skills plus the MCP connection to every surface we target, and it versions them together. Hooks can enforce working agreements mechanically, for example a PreToolUse hook that blocks writes under `projects/` (DR-0004).

## How it would fit

```
.claude-plugin/marketplace.json          { "name": "hyphae", "plugins": [{ "name": "adapt-rfp", "source": "./plugins/adapt-rfp" }] }
plugins/adapt-rfp/.claude-plugin/plugin.json
plugins/adapt-rfp/skills/...
plugins/adapt-rfp/.mcp.json                 P1 stdio → P2 http URL (via userConfig)
plugins/adapt-rfp/hooks/hooks.json          guard projects/, run `adapt-rfp check` after draft writes
```

The sibling `hyphae_ai_skills` repo could become a second plugin in the same `hyphae` marketplace.

## Strengths

- Declarative and git-native: reviewable in PRs, and versioned.
- One install gives a colleague the whole toolkit. Org sync removes per-user uploads on claude.ai.
- The same package loads in the Agent SDK by local path ([agent-sdk.md](agent-sdk.md)).

## Weaknesses / risks

- On claude.ai, hooks and stdio MCP servers can't run on the user's machine. Only remote MCP servers are useful there. *(Inferred from connectors running in Anthropic's cloud; confirm per component.)*
- Org distribution needs Team/Enterprise. On Pro/Max, skills and connectors are added by hand.
- Version-bump discipline: a pinned `version` with no bump means users don't get updates.

## Verdict rationale

Plugins are Anthropic's own packaging and distribution path for exactly this bundle. They cost little, are inspectable, and scale from one laptop to the org.

Parent: [index.md](index.md)
