---
title: Dolt
slug: dolt
level: 3
parent: index.md
related: [comparison.md, git-markdown-vault.md]
tags: [canonical-store, version-control, sql]
status: draft
updated: 2026-09-25
kind: product
verdict: hold
fit: [M3, M10]
license: Apache-2.0
maturity: mature
inspectability: high
sources:
  - title: Dolt 2.0 (DoltHub blog)
    url: https://www.dolthub.com/blog/2026-05-11-dolt-2-dot-0/
    accessed: 2026-09-25
  - title: InfoQ, Dolt 2.0 release
    url: https://www.infoq.com/news/2026/07/dolt-version-control/
    accessed: 2026-09-25
  - title: Version-controlled vector indexes
    url: https://www.dolthub.com/blog/2025-06-23-vector-index-deep-dive/
    accessed: 2026-09-25
  - title: DoltgreSQL repository
    url: https://github.com/dolthub/doltgresql
    accessed: 2026-09-25
---

# Dolt

> **TL;DR** **Hold.** Dolt is "git for data", a MySQL-compatible SQL database with branch, diff, and merge at cell level, and version-controlled vector indexes (beta). It fits structured registries well, but it's worse than plain git for long prose, and it needs a server and a workflow the team doesn't know.

## What it is
An open-source (Apache-2.0) SQL database whose storage is a Merkle-DAG. `dolt commit`, `dolt diff`, `dolt branch`, and `dolt merge` work on tables. **Dolt 2.0** (May 2026) adds automatic storage cleanup and compression, and ships beta support for version-controlled vector indexes (the MariaDB `VECTOR` type, adopted Sept 2025). **DoltgreSQL** (a Postgres-compatible variant) is still beta. DoltHub offers GitHub-style hosting.

## Why it matters for adapt-rfp
The fact and entity registries (M3) are tabular, and cell-level diffs ("CHAT score 3.55 → 3.61, source updated") would be nicer than YAML line diffs. Versioned embeddings would make index history auditable.

## How it would fit
It would hold M3 registries, with chunks staying in git. That's a split canonical store, so it would need a DR superseding part of DR-0005.

## Strengths
- True data version control with SQL, and high inspectability.
- Mature core, active vendor.

## Weaknesses / risks
- Prose chunks become text cells, and a cell diff of a 300-word paragraph is worse than a line diff in a PR.
- Needs `dolt sql-server` or DoltHub for Claude web access, which is more ops than a repo.
- Vector support is beta, and DoltgreSQL is beta.
- Non-technical colleagues get no better editing than with git.

## Verdict rationale
Its strength (tabular versioning) covers our smallest, easiest data. YAML in git with schema validation does that job well enough, so we'd pay the extra system cost for little gain.

Parent: [index.md](index.md)
