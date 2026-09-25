---
title: Retrieval design
slug: retrieval-design
level: 2
parent: index.md
related: [hybrid-search-and-reranking.md, contextual-retrieval.md, llms-txt.md, agent-skills-progressive-disclosure.md, llm-wiki-pattern.md]
tags: [retrieval, bm25, embeddings, rerank, metadata]
status: draft
updated: 2026-09-25
---

# Retrieval design

> **TL;DR** Use a four-stage funnel, in which each stage is optional and inspectable: (1) navigate the progressive-disclosure indexes, (2) apply hard metadata filters, (3) run lexical BM25 via SQLite FTS5, (4) only when needed, add embedding similarity fused with BM25 and a reranker. Because our chunks are curated, the `summary` field does the job of Anthropic's "contextual" prefix without an extra LLM pass. Build all indexes from git with one command.

## What M6/M7 actually ask

| Query | Best mechanism |
|---|---|
| "Firm-experience chunks with a 150-word variant, about urban heat" | metadata filter (type, variant words, topics) |
| "Everything we have on Bay Point" | filter `places: [place:bay-point]`, then navigate the index |
| "Text similar to this rubric descriptor: *community voices… quotes or stories*" | embeddings + rerank |
| "Where do we mention 'hsCRP'?" | BM25 (exact token) |
| "Does this draft name any org or place not in the target context?" | registry lookup (aliases → canonical), deterministic |
| "Which facts back this sentence?" | provenance map + fact registry, deterministic |

Most queries are filters or exact lookups. Semantic search matters mainly for matching rubrics to chunks and for "find copy like this".

## The funnel

### 1. Navigation (progressive disclosure)
`library/index.md` → `library/<type>/index.md` → chunk. Each index lists `[title](path): summary` and is generated from frontmatter, never hand-maintained. A skill (`find-copy`) tells Claude to read the root index first. Claude can then answer many requests without any search engine, as in the [LLM-wiki pattern](llm-wiki-pattern.md) and [Agent Skills](agent-skills-progressive-disclosure.md). This works from Claude web as long as the files are reachable (via MCP or a synced project).

### 2. Metadata filters (hard constraints)
Filters apply before any ranking: `type`, `owner`, `sensitivity` (never return `internal` chunks for public drafts), `status ≥ reviewed`, `places`, `orgs`, `programs`, `topics`, `variants.words ≤ limit`. They are SQL `WHERE` clauses over the derived SQLite index. Filters prevent the worst failure, which is context leakage (the Fresno sentence), better than any ranker.

### 3. Lexical: FTS5 BM25
SQLite FTS5 ships a `bm25()` ranking function with per-column weights, so `title` and `summary` can be weighted above `body` ([sqlite.org](https://www.sqlite.org/fts5.html), accessed 2026-09-25). It needs no model and is fully explainable, which makes it strong on names, acronyms and figures. Query expansion comes from the glossary and entity aliases: a search for "CCRCD" also matches "Contra Costa Resource Conservation District".

### 4. Semantic: embeddings + fusion + rerank (add when needed)
- Embed `title + summary + body` for each chunk *variant*. Store the vectors in sqlite-vec (pre-v1) or a sidecar parquet/npz file. At a few thousand vectors, brute-force cosine similarity in numpy is fine.
- Fuse the embedding and BM25 rankings with reciprocal rank fusion (RRF, a standard method), then rerank the top ~30–50 with Voyage `rerank-2.5` or Cohere Rerank 4 ([hybrid-search-and-reranking.md](hybrid-search-and-reranking.md)).
- **Contextual prefix.** Anthropic's Contextual Retrieval prepends 50–100 tokens of LLM-written context to each chunk before embedding and BM25 indexing. That cut top-20 retrieval failures by 49% with BM25, and by 67% with reranking added ([contextual-retrieval.md](contextual-retrieval.md)). Our curated `summary`, `type`, `places` and `orgs` give the same context deterministically: prepend them to the text at index time.

### When to turn on stage 4
- The filtered candidate set regularly exceeds what Claude can read in one pass (roughly 50–100k tokens), or
- A small labelled eval (about 20 queries, e.g. "rubric descriptor → the chunks a human would pick") shows recall@10 below ~0.8 with stages 1–3 *(threshold is a suggestion, not a sourced benchmark)*.

Below that, Anthropic's guidance for knowledge bases under ~200k tokens applies: put the relevant material in the prompt and use prompt caching.

## Privacy and cost

- API embedding and rerank calls send text off the machine, so apply DR-0004 and send only chunks at an allowed `sensitivity`. Voyage lists 200M free tokens on most current models ([docs.voyageai.com](https://docs.voyageai.com/docs/pricing), accessed 2026-09-25). Our whole corpus is well under 1M tokens, so embedding cost is negligible. If text must not leave the machine, the fallback is the open-weight `voyage-4-nano` (Apache-2.0, listed in Anthropic's embeddings guide) or another local model, run in the same pipeline *(local quality not evaluated here)*.
- Rebuild is one command (`adapt-rfp index`), and the index is gitignored (DR-0005).

## Inspectability hooks

- Every retrieval result carries its *reason*: the filters matched, the BM25 score and the matched terms, the embedding rank and the rerank score.
- Log retrieval runs to `log.md`-style JSONL (per the LLM-wiki "log" idea) so humans can audit why a chunk was chosen.
- Keep the eval set in git and rerun it when the model or index changes.

## Entity and fact retrieval

Registries are small (tens to hundreds of entries). Load them whole into memory and match with exact and alias lookups plus fuzzy matching (e.g. rapidfuzz *(unverified here)*) to catch "Counsel". No vector search is needed.

Up: [knowledge representation](index.md)
