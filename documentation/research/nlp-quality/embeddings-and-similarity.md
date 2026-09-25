---
title: Embeddings and similarity
slug: embeddings-and-similarity
level: 2
parent: index.md
related: [sentence-embeddings.md, nli-claim-support.md, minhash-lsh.md, bertscore.md, keyphrase-extraction.md, check-catalog.md]
tags: [embeddings, similarity, nli, rubric, redundancy, M1, M4, M6, M7]
status: draft
updated: 2026-09-25
---

# Embeddings and similarity

> **TL;DR** Use embeddings for **retrieval and ranking, not verdicts**. Rubric matching should return the best-matching draft sentence per evidence expectation, with its score, and let a human or LLM judge decide. Use lexical MinHash before embeddings for forks. Use an NLI or MiniCheck model, not cosine similarity, when the question is "is this claim supported?". Start with a local open model (bge-small / gte-modernbert / Qwen3-Embedding-0.6B via sentence-transformers). Adopt Voyage 4 if the team wants the model Anthropic's docs feature, or if Claude-web operation needs a hosted API.

## Three different similarity questions

| Question | Right tool | Why not the others |
|---|---|---|
| "Is this the same text (forked, lightly edited, shortened)?" | MinHash/LSH Jaccard and containment ([card](minhash-lsh.md)) | Deterministic, explainable (shared shingles), cheap. Embeddings call paraphrases "the same" too. |
| "Is this about the same thing?" (retrieval, rubric evidence, redundancy) | Bi-encoder sentence embeddings + cosine ([card](sentence-embeddings.md)), optionally a reranker | Lexical methods miss paraphrase |
| "Does source A support claim B?" | NLI / fact-checking models ([card](nli-claim-support.md)) | Cosine is symmetric and topical. "Reduces heat by 5°C" and "reduces heat by 15°C" embed almost identically. |

## Model choice (checked 2026-09-25)

| Option | License | Notes |
|---|---|---|
| `BAAI/bge-small-en-v1.5` | MIT | small, CPU-fast, English; good default for CI |
| `Alibaba-NLP/gte-modernbert-base` | Apache-2.0 | ModernBERT backbone, longer context |
| `nomic-ai/nomic-embed-text-v1.5` | Apache-2.0 | needs task prefixes (`search_query:` / `search_document:`) |
| `Qwen/Qwen3-Embedding-0.6B` | Apache-2.0 | instruction-aware, multilingual |
| `BAAI/bge-m3` | MIT | dense + sparse + multi-vector in one model |
| `google/embeddinggemma-300m` | Gemma terms | not OSI; check terms before use |
| `voyageai/voyage-4-nano` | Apache-2.0 (per Anthropic docs and HF tag) | open-weight sibling of the Voyage API models |
| Voyage API `voyage-4` / `-large` / `-lite` | commercial API | 32k context, Matryoshka dims 256–2048, `input_type` query/document; `voyage-context-4` for context-aware chunk embeddings; `rerank-2.5` |
| OpenAI `text-embedding-3-*` | commercial API | viable; no advantage for this project *(pricing unverified)* |

Anthropic has no embedding model of its own. Its docs say Voyage AI "has a wide variety of options and capabilities" and use Voyage for the rest of the guide, while telling readers to "assess a variety of embeddings vendors". So Voyage is the featured choice, not a requirement.

**Recommendation.** Pin one local model for deterministic CI (bge-small or gte-modernbert). Allow an optional Voyage backend behind the same interface. Store `model@revision` with every vector and treat vectors as derived data (DR-0005). Don't pick by MTEB rank alone. Build a 30–50 pair eval from the pilot (fork pairs, long/short variants, rubric-evidence hits and misses) and choose on that.

## Rubric descriptor matching (E1)

Rubric bands are written as judgments ("*High: application includes community voices… quotes or stories demonstrating…*"). Raw cosine between a whole answer and a whole band text is weak evidence: every answer on heat and parks is "similar" to every band. Instead:

1. In M5, **decompose each High descriptor into evidence expectations**: short, concrete statements (e.g., "includes a direct quote from a resident", "names a community partner and their role", "cites a local heat-health statistic").
2. Map each expectation to a **deterministic detector** where one exists (quote detector L12, partner registry match, fact-type match). Use embeddings only for the rest ("a story of lived experience").
3. For embedding-only expectations, score each draft sentence against the expectation (asymmetric: expectation = query, sentence = document). Report the top 3 with scores.
4. **Calibrate per model.** Cosine scales differ between models (bge scores are compressed high, for example). Set thresholds from the pilot eval set, not from folklore, and report "no sentence above τ" as a *gap candidate*, not a failure.
5. Optionally, a cross-encoder reranker (Voyage rerank-2.5, or an open bge-reranker *(license unverified)*) re-scores the top-k for sharper separation.

This keeps the check inspectable: the reviewer sees the expectation, the best sentence, and the score.

## Cross-answer redundancy (E2)

Embed every sentence of every answer in one application. Pairs from *different* answers with cosine ≥ τ_high (calibrate, likely about 0.85 for bge-class models) mean "the same point made twice". Also run MinHash on 5-word shingles to catch literal copy. Report them as clusters. Redundancy can be deliberate (reviewers read answers in isolation), so this is a warning.

## Near-duplicates and variants (M1)

- Forks (Ambrose Memorial vs Ambrose Center, ~99% identical): MinHash Jaccard ≥ 0.9 at the paragraph level, then diff the few non-matching paragraphs. This is how M1 isolates the differing pre-app sections.
- Shortened variants: *containment* (|A∩B|/|B|) is high while Jaccard is low. datasketch's LSH Ensemble indexes containment directly. Confirm with embedding cosine and record `shortened-from`.
- Paraphrased adaptations: MinHash is low, cosine is high. Candidate `adapted-for` lineage for human confirmation.

## Claim support (E4)

With the M6 provenance map (sentence → chunk/fact ids), run a claim checker per sentence against *only its cited sources*. This is a much easier problem than open fact-checking. MiniCheck-Flan-T5-Large (MIT, 770M) runs on CPU/GPU locally. AlignScore handles long contexts by chunking (~350 tokens). Low support → "claim drifted from source". Numbers are checked deterministically first (L11). NLI models are unreliable on exact numeric mismatch *(general finding; verify on our eval)*.

## Pitfalls

- Embedding similarity rewards topic overlap, not quality or truth.
- Thresholds are not portable across models. Recalibrate when the model changes.
- Boilerplate dominates similarity: strip headers and templates before embedding.
- Hosted APIs send library text off-machine. Chunk `sensitivity` tags (DR-0004) must gate which chunks can go to Voyage/OpenAI.

## Sources

- Anthropic, Embeddings guide: https://platform.claude.com/docs/en/build-with-claude/embeddings (accessed 2026-09-25)
- Hugging Face model API license tags for the models above, e.g. https://huggingface.co/api/models/BAAI/bge-small-en-v1.5 (accessed 2026-09-25)
- datasketch README (LSH Ensemble, v2.0 scheme change): https://github.com/ekzhu/datasketch (accessed 2026-09-25)
- MiniCheck README: https://github.com/Liyan06/MiniCheck (accessed 2026-09-25)
- AlignScore README: https://github.com/yuh-zha/AlignScore (accessed 2026-09-25)

Parent: [NLP quality checks](index.md)
