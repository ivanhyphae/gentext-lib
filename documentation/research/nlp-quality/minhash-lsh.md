---
title: MinHash / LSH near-duplicate detection
slug: minhash-lsh
level: 3
parent: index.md
related: [embeddings-and-similarity.md, sentence-embeddings.md, rapidfuzz.md]
tags: [near-duplicate, minhash, lsh, simhash, lineage, dedup]
status: draft
updated: 2026-09-25
kind: algorithm
verdict: adopt
fit: [M1, M2, M7]
license: MIT (datasketch, simhash); Apache-2.0 (text-dedup)
maturity: mature
inspectability: high
sources:
  - title: ekzhu/datasketch GitHub README (MIT; v2.0.0, 2026-07-05)
    url: https://github.com/ekzhu/datasketch
    accessed: 2026-09-25
  - title: ChenghaoMou/text-dedup GitHub repository (Apache-2.0; PyPI 0.4.1, 2025-12-28)
    url: https://github.com/ChenghaoMou/text-dedup
    accessed: 2026-09-25
  - title: 1e0ng/simhash GitHub repository (MIT; last push 2022-03)
    url: https://github.com/1e0ng/simhash
    accessed: 2026-09-25
  - title: Broder (1997), On the resemblance and containment of documents
    url: https://doi.org/10.1109/SEQUEN.1997.666900
    accessed: 2026-09-25
---

# MinHash / LSH near-duplicate detection

> **TL;DR** **Adopt.** Shingle text into word n-grams and estimate Jaccard similarity (and containment) with MinHash, indexed by LSH for sub-linear lookup. **datasketch** (MIT, v2.0.0 on 2026-07-05) provides MinHash, MinHashLSH, and LSH Ensemble. This is how M1 collapses the forked Ambrose documents and links long/shortened variants, with explainable "shared shingles" evidence.

## What it is

- **Shingling + Jaccard.** Represent each paragraph as its set of *k*-word shingles (k=3–5). Jaccard |A∩B|/|A∪B| measures resemblance. *Containment* |A∩B|/|A| measures "A is mostly inside B" (Broder 1997).
- **MinHash** approximates Jaccard with a fixed-size signature (e.g., 128 permutations). **LSH** buckets signatures so that only likely matches are compared.
- **datasketch** provides MinHash and weighted MinHash, MinHashLSH (threshold queries), LSH Forest (top-k), LSH Ensemble (containment queries), HyperLogLog, and optional Redis/Cassandra storage. **v2.0.0 changed the default permutation scheme to `affine32`**, which fixes an over-estimation bias, halves memory, and speeds updates about 4×. Signatures persisted under 1.x must be rebuilt or loaded with `scheme="legacy"`.
- **SimHash** (Charikar) is a bitwise fingerprint whose Hamming distance tracks cosine over features. The `simhash` package (MIT) has had no commits since 2022.
- **text-dedup** (Apache-2.0) is a toolkit of scripts for MinHash, SimHash, suffix-array exact substring, and Bloom filters, aimed at dataset-scale dedup. It is overkill for our corpus but good reference code.

## Why it matters for adapt-rfp

| Pilot situation | Signal |
|---|---|
| Ambrose Memorial vs Ambrose Center Park docs (~99% identical) | Paragraph-level Jaccard ≈ 1 for most pairs. The few low-scoring paragraphs *are* the diff (title, 2a, Q5, 6a, a Modeling paragraph). |
| Long vs "SHORTENED VERSION" method paragraphs | High containment of short in long, moderate Jaccard. Propose `shortened-from`. |
| Boilerplate reused across proposals | Library-wide LSH hits show where a chunk already exists, so there is no duplicate chunk. |
| Draft QA (T3) | Each draft paragraph should match its provenance chunk. High overlap with an *uncited* chunk means unattributed reuse and a possible leakage risk. |

## How it would fit

- M1: `dedup.index(chunks)` builds a MinHashLSH (threshold ~0.8) plus an LSH Ensemble for containment. Candidates go to human review with a word-level diff (`difflib`), so the evidence is visible.
- The index is derived data, rebuildable from `library/` (DR-0005). Record the datasketch version and scheme.
- For a corpus of our size (hundreds to thousands of paragraphs), exact Jaccard on shingle sets is also fast. MinHash matters only as the library grows. Start exact, and keep the API the same.

## Strengths

- Deterministic (seeded), explainable, language-agnostic, CPU-cheap.
- Containment is a natural fit for the "shortened variant" relation.

## Weaknesses / risks

- Blind to paraphrase. Adaptations that reword everything need [embeddings](embeddings-and-similarity.md).
- Sensitive to normalization (smart quotes, list bullets, whitespace). Normalize before shingling.
- The 2.0 scheme change means stale persisted signatures silently differ. Pin the version.

## Verdict rationale

Classical, inspectable, and directly aligned with DR-0002 lesson 2 (reuse by forking) and lesson 3 (length variants).

Parent: [NLP quality checks](index.md)
