---
title: Sentence embeddings (sentence-transformers, Voyage)
slug: sentence-embeddings
level: 3
parent: index.md
related: [embeddings-and-similarity.md, nli-claim-support.md, minhash-lsh.md, keyphrase-extraction.md]
tags: [embeddings, sentence-transformers, voyage, retrieval, similarity]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M1, M2, M4, M6, M7]
license: Apache-2.0 (sentence-transformers); model licenses vary; Voyage API commercial
maturity: mature
inspectability: medium
sources:
  - title: huggingface/sentence-transformers GitHub repository (Apache-2.0; v6.1.0, 2026-09-18)
    url: https://github.com/huggingface/sentence-transformers
    accessed: 2026-09-25
  - title: Anthropic docs, Embeddings (Voyage recommendation; Voyage 4 model table)
    url: https://platform.claude.com/docs/en/build-with-claude/embeddings
    accessed: 2026-09-25
  - title: voyageai Python package on PyPI (0.5.0, 2026-07-10, MIT)
    url: https://pypi.org/project/voyageai/
    accessed: 2026-09-25
  - title: Hugging Face model cards (license tags), e.g. BAAI/bge-small-en-v1.5, Alibaba-NLP/gte-modernbert-base, nomic-ai/nomic-embed-text-v1.5, Qwen/Qwen3-Embedding-0.6B, voyageai/voyage-4-nano
    url: https://huggingface.co/BAAI/bge-small-en-v1.5
    accessed: 2026-09-25
  - title: MTEB leaderboard
    url: https://huggingface.co/spaces/mteb/leaderboard
    accessed: 2026-09-25
---

# Sentence embeddings (sentence-transformers, Voyage)

> **TL;DR** **Adopt.** Use **sentence-transformers** (Apache-2.0, v6.1.0 on 2026-09-18) as the local embedding and cross-encoder runtime, with a small pinned open model for CI. Put **Voyage 4** (the provider Anthropic's embeddings guide features; the guide itself says to compare vendors) behind the same interface as an optional hosted backend. Embeddings power retrieval (M6), rubric-evidence ranking, redundancy, and paraphrase-level lineage.

## What it is

- **sentence-transformers.** The standard Python library for bi-encoder embeddings (`SentenceTransformer.encode`), cross-encoder rerankers (`CrossEncoder`), and sparse encoders, plus fine-tuning. It loads most open models on the Hugging Face Hub.
- **Open models** (license tags checked on HF 2026-09-25): `bge-small-en-v1.5` (MIT), `bge-m3` (MIT), `gte-modernbert-base` (Apache-2.0), `nomic-embed-text-v1.5` (Apache-2.0, needs task prefixes), `Qwen3-Embedding-0.6B` (Apache-2.0), `voyage-4-nano` (Apache-2.0), `embeddinggemma-300m` (Gemma terms, not OSI).
- **Voyage API.** `voyage-4-large`, `voyage-4`, and `voyage-4-lite`: 32k context, 1024-d default with 256/512/2048 Matryoshka options, `int8`/binary quantization, and `input_type="query"|"document"` (which prepends a retrieval prompt). `voyage-context-4` embeds chunks with document context (120k). `rerank-2.5` is the reranker. Anthropic states it "does not offer its own embedding model".

## Why it matters for gentext

| Use | Module | Notes |
|---|---|---|
| Retrieve candidate chunks for a question | M6 | query = question + rubric expectation; documents = chunk variants |
| Rubric evidence ranking (E1) | M7 | top-k sentences per expectation, with scores ([deep dive](embeddings-and-similarity.md)) |
| Cross-answer redundancy (E2) | M7 | sentence-pair cosine across answers |
| Paraphrase lineage (`adapted-for`) | M1 | complements [MinHash](minhash-lsh.md) |
| Topic facets | M2/M4 | clustering, [KeyBERT](keyphrase-extraction.md) |

## How it would fit

- One interface: `Embedder.encode(texts, kind="query"|"doc") -> np.ndarray`, with backends `st:<hf-id>@<revision>` and `voyage:<model>`. Every vector store row keeps `model@revision`, dimensions, and normalization.
- Vectors are derived, rebuildable, and never committed (AGENTS.md). DR-0005 describes the store as SQLite/DuckDB plus a vector index.
- **Sensitivity gate.** Chunks tagged above a threshold (DR-0004) are embedded only locally.
- Choose the model with a small pilot eval set (fork pairs, variant pairs, rubric hits and misses), not by leaderboard rank.

## Strengths

- Mature, fast, well documented. CPU is fine for small models at our corpus size.
- Same library covers rerankers and NLI cross-encoders ([NLI card](nli-claim-support.md)).
- The Voyage option aligns with Anthropic guidance and suits Claude-web operation (no local GPU).

## Weaknesses / risks

- Scores are not explanations. Always surface the matched text next to the score.
- Similarity is topical. It does not measure truth, quality, or rubric satisfaction on its own.
- Model changes shift score distributions. Recalibrate thresholds, and re-embed everything on change.
- Hosted APIs mean cost and data egress *(Voyage pricing not checked; see their pricing page)*.

## Verdict rationale

Embeddings are unavoidable for semantic retrieval and rubric evidence. sentence-transformers is the obvious runtime, and a pluggable Voyage backend keeps the Anthropic-aligned option open.

Parent: [NLP quality checks](index.md)
