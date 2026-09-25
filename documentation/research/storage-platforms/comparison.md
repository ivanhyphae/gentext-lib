---
title: Canonical stores and derived indexes compared
slug: comparison
level: 2
parent: index.md
related: [claude-web-access.md, git-markdown-vault.md, sqlite-fts5-vec.md, supabase.md, notion.md]
tags: [storage, index, vector-search, comparison]
status: draft
updated: 2026-09-25
---

# Canonical stores and derived indexes compared

> **TL;DR** For the canonical layer, only git + plain text meets all three of powerful, elegant, and inspectable for a small team. Dolt comes closest but costs a server and an unfamiliar workflow. For the derived index, one SQLite file with FTS5 and sqlite-vec covers metadata, keyword, and vector search for a corpus this size. Postgres + pgvector (Supabase) is the upgrade path once hosting and multi-user access matter.

## Requirements distilled from DR-0002/3/5

1. **Diffable prose history** with attribution (who changed which sentence, and why).
2. **Rich metadata** in frontmatter: type, owner, voice, facts[], sources[], variants[], lineage, sensitivity.
3. **Queries**: filter by metadata, keyword/BM25, semantic nearest-neighbor, and hybrid.
4. **Rebuildable**: every index is derived from the repo by one command (DR-0005).
5. **Confidentiality**: nothing leaves our control unless its `sensitivity` tag allows it (DR-0004).
6. **Reachable from Claude web** eventually (see [claude-web-access.md](claude-web-access.md)).

Scale: at most a few thousand chunks. That makes ANN indexes, sharding, and dedicated vector services unnecessary.

## Canonical store options

| Option | History / diff | Metadata | Non-technical editing | Inspectability | Lock-in | Verdict |
|---|---|---|---|---|---|---|
| **git + Markdown/YAML** ([card](git-markdown-vault.md)) | Line-level diffs, blame, PR review | YAML frontmatter, schema-validated in CI | Weak directly. Use Claude Docs round-trip (M9), or Obsidian as a viewer/editor | High | None | **adopt** |
| Dolt ([card](dolt.md)) | Cell-level diff, branch, merge in SQL | Tables | Weak (SQL or DoltHub UI) | High, though prose diffs are cell-sized blobs | Low (OSS, MySQL wire) | hold |
| Postgres/Supabase as source of truth ([card](supabase.md)) | Only if we build audit tables | Tables + JSONB | Via a custom UI or Studio | Medium | Low–medium | hold as canonical |
| Notion ([card](notion.md)) | Page history, not diffable via the API | Database properties | Excellent | Low–medium | High | hold |
| Airtable | Revision history per record | Fields | Excellent | Medium | High | hold |
| Grist | Action history; the document is a SQLite file | Tables + Python formulas | Good | Medium–high (OSS `grist-core`, Apache-2.0) | Low | assess only for registries |

Notes:
- **Airtable**: 5 req/s per base, 50 req/s per token, 30 s back-off after a 429; official MCP server since Feb 2026 (secondary source). A spreadsheet model is a poor fit for long prose with variants.
- **Grist** is the one table tool that stays inspectable: open source, self-hostable, SQLite underneath, REST and SQL endpoint. It could host the *fact and entity registries* for non-technical editing if YAML proves too hostile. That would split the canonical store in two, so treat it as a later option.
- **Obsidian** is not a store. It's a free (commercial licence optional since Feb 2025) editor/viewer for the same Markdown folder, with wikilinks and properties UI. That makes it a zero-cost browsing surface for colleagues who can pull the repo.

## Derived index options

| Option | Keyword | Vector | Runs where | Maturity (2026-09) | Fit |
|---|---|---|---|---|---|
| **SQLite + FTS5 + sqlite-vec** ([card](sqlite-fts5-vec.md)) | FTS5 BM25 | brute-force KNN (stable 0.1.9); ANN in 0.1.10 alpha | anywhere, one file | FTS5 mature; sqlite-vec pre-1.0 but active | **adopt** |
| DuckDB + vss ([card](duckdb-vss.md)) | `fts` extension | HNSW (persistence experimental) | embedded | Core mature; vss persistence flagged experimental | assess (analytics) |
| LanceDB ([card](lancedb.md)) | Tantivy/native FTS | IVF/HNSW, hybrid + rerank | embedded or cloud | Apache-2.0, VC-backed, fast-moving | assess |
| Postgres + pgvector ([card](supabase.md)) | `tsvector` + GIN | HNSW/IVFFlat, `halfvec` | hosted (Supabase/Neon) | Mature | phase 2 |
| Turso / libSQL | FTS5 | native vector functions | hosted SQLite, embedded replicas | libSQL production; Rust "Turso Database" rewrite beta (v0.6.x) | assess, if we want hosted SQLite |
| Neon | as Postgres | pgvector | serverless Postgres | Databricks-owned; free 0.5 GB/project, usage-based | alternative to Supabase for DB only |
| Hosted vector DBs ([card](hosted-vector-dbs.md)) | varies | ANN | SaaS | Mature | hold |

### Why SQLite first
- It's one file, and you can inspect it with `sqlite3`, Datasette, or any SQL client. Deleting it and rebuilding is safe by construction.
- Every runtime we might use has it: Python stdlib, Claude Code cloud VMs, any container host. The whole index can ship *inside* the MCP server image.
- FTS5 gives BM25 ranking, and brute-force cosine search over a few thousand embeddings is instant. That means hybrid search is one SQL query plus reciprocal-rank fusion in Python.
- SQLite now has an official ANN extension, **vec1** (v0.7, IVFADC; its own page says "testing is insufficient"). We don't need ANN, but it's a hedge if sqlite-vec stalls.

### When to move to Postgres
When the index has to be *shared and live*: several writers, a hosted MCP server that shouldn't redeploy per change, or row-level security keyed on `sensitivity`/`owner`. Supabase supports hybrid search in Postgres (tsvector + pgvector with RRF) and has an "automatic embeddings" pattern using pgmq, pg_net, and pg_cron. The same schema works on Neon if we only want the database.

## Scoring against the lens

| | Powerful | Elegant | Inspectable | Small-team cost |
|---|---|---|---|---|
| git + SQLite (phase 0–1) | enough for the corpus size | one repo, one file, one rebuild command | highest | ~$0 |
| git + Supabase mirror (phase 2) | multi-user, auth, always-on | two systems plus a sync job | high (Postgres is inspectable; the sync adds a moving part) | $0 → $25/mo Pro |
| Notion/Airtable canonical | great UI | API friction for long prose | low | per-seat |
| Dolt canonical | branching data | unfamiliar workflow | high | server ops |

## Sources

- SQLite FTS5: https://sqlite.org/fts5.html (accessed 2026-09-25)
- SQLite vec1: https://sqlite.org/vec1 (accessed 2026-09-25)
- sqlite-vec releases: https://github.com/asg017/sqlite-vec/releases (accessed 2026-09-25)
- DuckDB vss: https://duckdb.org/docs/current/core_extensions/vss (accessed 2026-09-25)
- LanceDB docs: https://docs.lancedb.com/ (accessed 2026-09-25)
- Supabase hybrid search: https://supabase.com/docs/guides/ai/hybrid-search (accessed 2026-09-25)
- Supabase automatic embeddings: https://supabase.com/docs/guides/ai/automatic-embeddings (accessed 2026-09-25)
- Turso/libSQL: https://docs.turso.tech/libsql ; https://turso.tech/vector (accessed 2026-09-25)
- Neon pricing after Databricks (secondary): https://agentdeals.dev/vendor/neon (accessed 2026-09-25) *(unverified against neon.com)*
- Airtable API limits: https://support.airtable.com/docs/managing-api-call-limits-in-airtable (accessed 2026-09-25)
- Airtable MCP launch date (secondary): https://www.scalekit.com/blog/airtable-mcp-vs-api (accessed 2026-09-25) *(unverified)*
- Grist self-hosting: https://www.getgrist.com/product/self-hosted/ (accessed 2026-09-25)
- Obsidian free for work: https://obsidian.md/blog/free-for-work/ (accessed 2026-09-25)

Parent: [index.md](index.md)
