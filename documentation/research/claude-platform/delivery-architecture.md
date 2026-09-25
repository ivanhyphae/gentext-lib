---
title: "Skills vs MCP vs CLI: delivery architecture"
slug: delivery-architecture
level: 2
parent: index.md
related: [agent-skills.md, claude-code-plugins.md, mcp-connectors.md, fastmcp.md, agent-sdk.md, docs-roundtrip.md]
tags: [architecture, skills, mcp, cli, plugins, deployment]
status: draft
updated: 2026-09-25
---

# Skills vs MCP vs CLI: delivery architecture

> **TL;DR** Use three layers over one core. The **CLI** is the deterministic engine. **Skills** carry the procedure and pointers into the library. A **remote MCP server** exposes the engine and data to every Claude surface. Skills alone can't reach a private repo from claude.ai, and an MCP server alone doesn't teach Claude the drafting method. The two are bundled as one plugin.

## Why three layers

Each surface has a hard limit that pushes a capability into a particular layer:

| Constraint (verified 2026-09-25) | Consequence |
|---|---|
| Skills on claude.ai run in a sandbox VM with "full, partial, or no network access" by settings; on the API, no network and no package installs ([Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)) | A skill on the web can't count on cloning our repo or calling a database. Data access must come from MCP. |
| Custom skills don't sync between Claude Code, claude.ai and the API (same source) | Keep skills as files in git and publish them to each surface from there. |
| claude.ai connects to MCP servers from Anthropic's cloud, so the server must be publicly reachable ([custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)) | Local stdio servers work only in Claude Code/Desktop. The web target needs a hosted HTTPS server. |
| claude.ai tool results are capped at ~150,000 chars with a 240 s timeout; Claude Code defaults to 25,000 tokens ([Build an MCP server](https://claude.com/docs/connectors/building)) | Tools return compact JSON and paginate. Long jobs (ingest, embedding) run offline, not inside a tool call. |
| claude.ai org plugin sync rejects plugins with a top-level `bin/` ([host a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace)) | Put executables under `scripts/` and reference them as `${CLAUDE_PLUGIN_ROOT}/scripts/...`. |

## What goes where

| Capability (DR-0003) | Core/CLI | MCP tool / resource | Skill |
|---|---|---|---|
| M0/M1 ingest, segment | `gentext ingest`, `gentext segment` | none in P2 (confidential sources stay local, DR-0004) | `ingest-source` (Claude Code only) |
| M2 library lookup | `gentext find` | `search_chunks`, `get_chunk`; resources `chunk://{id}`, `library://index` | `find-copy`: how to choose variants, when to stop |
| M3 facts, glossary | `gentext facts`, `gentext glossary` | `lookup_fact`, `resolve_entity`, `glossary_check` | referenced from drafting skills |
| M5 solicitation | `gentext solicitation` | `get_requirements`, `compliance_matrix`; resource `solicitation://ehcrp/r2` | `model-solicitation` (LLM-assisted extraction → human review) |
| M6 compose | `gentext compose --plan` (retrieval + fit) | `draft_context` returns chunks + limits + provenance scaffold | `draft-answer`: the method, the voice, the placeholder rule |
| M7 QA | `gentext check` (word limits, leakage, glossary, provenance) | `check_draft` → report JSON | `check-draft`: run the check, then judge rubric coverage |
| M9 harvest | `gentext harvest` | `propose_variant` writes a branch/PR, never `main` | `harvest-edits` |

Rules of thumb:

- **CLI** holds anything deterministic, anything that needs the full repo, and anything slow. It must run without an LLM (DR-0003).
- **MCP tools** are small, typed verbs over the CLI's functions (call the Python API in-process, not a subprocess). Use tool annotations: `readOnlyHint` on reads, `destructiveHint` on writes. Use **resources** for addressable text such as chunks and solicitation YAML, and **prompts** for canned entry points ("draft EHCRP Q3"). Claude supports tools, prompts, resources and text/binary content. It does not support resource subscriptions or sampling (same source).
- **Skills** hold judgment and sequence: which tool first, how to treat `[[NEEDS SOURCE]]`, the truthfulness rules from AGENTS.md, and when to hand back to a human. Keep each SKILL.md short and link to reference files (progressive disclosure: ~100 tokens of metadata per skill, body under 5k tokens).
- **Pure-stdlib check scripts** (word counts, a leakage regex over a supplied name list) can also ship inside a skill's `scripts/`. They then run in claude.ai's sandbox with no network. This is a cheap fallback before the MCP server exists. *(Design option, not tested.)*

## Packaging

```
plugins/gentext/
  .claude-plugin/plugin.json      name, version, userConfig (server URL)
  skills/{find-copy,draft-answer,check-draft,harvest-edits}/SKILL.md
  .mcp.json                       P1: stdio `uv run gentext-mcp`; P2: {"type":"http","url":"https://…/mcp"}
  scripts/                        helpers (no top-level bin/)
.claude-plugin/marketplace.json   repo-local catalog
```

- **Claude Code:** `/plugin marketplace add <org>/gentext-lib`, then `/plugin install gentext@<marketplace>`. Or register it for the repo with `--scope project` and commit `.claude/settings.json` ([host a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace)).
- **claude.ai (Team/Enterprise):** Organization settings → Plugins & skills → sync a private GitHub repo. Plugins then appear in web chat, Desktop, Cowork and Claude Code ([manage plugins](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)).
- **claude.ai (Pro/Max):** upload each skill as a zip under Customize → Skills and add the MCP URL as a custom connector.

## Phases

1. **P0 pilot (Claude Code, local).** Put skills in `.claude/skills/`, call the CLI through Bash, and paste into Claude Docs by hand. No server. This is the fastest path to 2026-10-13, and everything stays in git.
2. **P1 plugin.** Move the skills into the plugin and add a local **stdio** FastMCP server (`uv run`). The tool contracts get settled while debugging is still local.
3. **P2 hosted, read-mostly.** Deploy the same FastMCP app over Streamable HTTP with OAuth (or an org static header). Sync a read-only clone of the repo plus a rebuilt index (M10). Add it as a custom connector. Now Claude web can find, draft and check.
4. **P3 write + automation.** Add `propose_variant` / `record_edit` tools that open git branches or PRs, so humans still review. Use the Agent SDK or `claude -p` in CI for nightly ingest and QA, and the Batch API for bulk characterization ([agent-sdk.md](agent-sdk.md), [api-features.md](api-features.md)).

## Alternatives considered

- **Skills only.** Elegant, but on the web they can't reach the library. Uploading the library inside a skill zip copies canonical data into a surface with no sync. Rejected past P0.
- **MCP only.** Works everywhere, but Claude has no drafting method, and tool descriptions are a poor place for a long procedure. Rejected.
- **Projects as the delivery surface.** Useful as a stopgap knowledge store, but read-only and stale ([claude-projects.md](claude-projects.md)).
- **API app (our own UI).** Most control (Citations, structured outputs), but it gives up claude.ai and Claude Docs, which the README targets. Keep it for batch jobs only.

## Inspectability

Everything declarative lives in git: skills, plugin manifest, MCP tool schemas, marketplace. The server logs every tool call with its arguments. Writes go through PRs. The one weak spot is claude.ai itself: conversation transcripts and Claude Docs have no version history or compliance-API logging ([Claude Docs help](https://support.claude.com/en/articles/16923645-get-started-with-claude-docs)). Lineage therefore has to be recorded by our tools at harvest time.

## Sources

All accessed 2026-09-25: [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Build an MCP server for Claude](https://claude.com/docs/connectors/building) · [Custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) · [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) · [Host a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace) · [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

Parent: [index.md](index.md)
