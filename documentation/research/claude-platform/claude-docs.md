---
title: Claude Docs
slug: claude-docs
level: 3
parent: index.md
related: [docs-roundtrip.md, google-drive-connector.md, claude-projects.md]
tags: [collaboration, claude-docs, artifacts, M9]
status: draft
updated: 2026-09-25
kind: product
verdict: trial
fit: [M9]
license: proprietary (Anthropic)
maturity: emerging
inspectability: medium
sources:
  - title: Get started with Claude Docs (Help Center)
    url: https://support.claude.com/en/articles/16923645-get-started-with-claude-docs
    accessed: 2026-09-25
  - title: Claude Cowork and chat are now one Claude (blog, 2026-09-16)
    url: https://claude.com/blog/cowork-is-now-claude
    accessed: 2026-09-25
  - title: Claude Docs connector guide (topic.index, topic.comments, topic.tabs, topic.sharing), read via the connector in this session
    url: https://claude.ai
    accessed: 2026-09-25
---

# Claude Docs

> **TL;DR** Claude Docs are living rich-text documents in claude.ai, stored under Artifacts. Claude drafts them, people co-edit and comment, and an @Claude comment gets Claude to revise. It launched in beta on 2026-09-16 on paid plans. A connector lets Claude (including Claude Code) create, read, edit and comment on docs programmatically. **Trial** as gentext's iteration surface. Don't treat it as a record, because it has no version history.

## What it is (verified 2026-09-25)

- **Availability.** Beta on Pro, Max, Team and Enterprise. On by default except on Enterprise, where an owner enables it. Not available to orgs using CMEK, ZDR or HIPAA configurations. No mobile editing.
- **Structure.** A doc holds **tabs**, which can be nested and ordered. Tabs contain prose, pipe tables, charts, diagrams, chips (dates, mentions, dropdowns) and uploads.
- **Collaboration.** Real-time co-editing. Anyone can comment. A comment addressed to Claude arrives as its own turn, and Claude replies in the thread and makes the edit. Changes are attributed to whoever made them. Claude can do only what the requesting user can do.
- **Programmatic access (Docs connector).** Create a doc with tabs in one `batch`. Read by outline, view or search. Edit with find-replace, block replace, insert and table-cell ops, guarded by content hash or revision. List, create and reply to comments. Limits: 1000 threads per doc, 100 comments per thread, 4 KB comment bodies.
- **Sharing.** Pro/Max: link sharing. Team/Enterprise: inside the org only. Roles are viewer or editor, with no comment-only tier.
- **Export.** The doc name menu → Export offers Word, PDF or Markdown, for the open tab only (connector guide). The Help Center also lists **Google Docs** as an export target. *Conflict: test before relying on it.* The connector's `export` tool gives Claude a Word or PDF file.
- **Gaps.** No version history, no File menu, a doc can't be put in a Project, no compliance-API logging, and charts don't auto-update.

## Why it matters for gentext

The README says "try working in claude docs", and DR-0003 open question 5 asks Claude Docs vs Google Docs. Claude Docs is the only surface where Claude can edit *existing* text in place and act on reviewer comments. Google Docs through the Drive connector is read-only for existing files ([google-drive-connector.md](google-drive-connector.md)).

## How it would fit

M9 surface: one doc per application, one tab per question, provenance as comments, a QA tab. See [docs-roundtrip.md](docs-roundtrip.md). Harvest goes through Claude reading the doc and then calling gentext tools, because our server can't read Docs directly.

## Strengths

- Claude and humans share one surface, and comment threads map naturally onto review.
- Programmatic, guarded edits (hash/revision checks) mean Claude doesn't overwrite human edits blindly.
- Tabs mirror the tabbed final Google Doc.

## Weaknesses / risks

- A two-week-old beta: behaviour and limits will change.
- No version history. Lineage must be captured in git at harvest time.
- Content lives in Anthropic's app, outside our repo, which weakens inspectability. It is not reachable by our own services.
- Org-internal sharing on Team/Enterprise may block partner reviewers (I-ReLab, CCRCD), who would need Export.

## Verdict rationale

**Trial** for the EHCRP pilot with a manual fallback (Export → Markdown). Promote it to adopt if the round trip works and the export and comment behaviour holds steady.

Parent: [index.md](index.md)
