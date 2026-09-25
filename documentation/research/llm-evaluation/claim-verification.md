---
title: Claim extraction and verification against the fact registry
slug: claim-verification
level: 3
parent: index.md
related: [anthropic-citations-api.md, adversarial-review-pass.md, critic-reviser-loop.md, ../provenance/index.md]
tags: [factuality, hallucination, fact-checking, factscore, safe, chain-of-verification]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M3, M7]
license: n/a (technique; FActScore code MIT per repo, unverified)
maturity: mature
inspectability: high
sources:
  - title: "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (Min et al., EMNLP 2023)"
    url: https://arxiv.org/abs/2305.14251
    accessed: 2026-09-25
  - title: "Long-form factuality in large language models (SAFE; Wei et al., 2024)"
    url: https://arxiv.org/abs/2403.18802
    accessed: 2026-09-25
  - title: "Chain-of-Verification Reduces Hallucination in Large Language Models (Dhuliawala et al., 2023)"
    url: https://arxiv.org/abs/2309.11495
    accessed: 2026-09-25
  - title: Ragas faithfulness metric
    url: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
    accessed: 2026-09-25
---

# Claim extraction and verification against the fact registry

> **TL;DR** Split the draft into atomic claims and check each one against a trusted source. Report supported, contradicted, and unsourced claims per sentence. **Adopt.** Our trusted source is the curated M3 fact registry, not web search, which makes this more reliable than the published methods. Match deterministically first; use the LLM only for paraphrased support.

## What it is

- **FActScore**: breaks a generation into atomic facts and computes the share supported by a knowledge source. An automated estimator stayed within 2% error of human FActScores ([arXiv 2305.14251](https://arxiv.org/abs/2305.14251)).
- **SAFE**: an LLM splits a response into facts and checks each with multi-step Google Search. It agreed with 72% of crowd annotations, won 76% of disagreements, and was about 20× cheaper ([arXiv 2403.18802](https://arxiv.org/abs/2403.18802)).
- **Chain-of-Verification (CoVe)**: draft → plan verification questions → answer them *independently* of the draft → revise. This reduced hallucination on list, QA, and long-form tasks ([arXiv 2309.11495](https://arxiv.org/abs/2309.11495)).
- **Ragas faithfulness** is the same ratio (supported claims ÷ all claims) applied to RAG context ([docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)).

## Why it matters for gentext

AGENTS.md: "Never invent facts… Any factual claim in generated text must trace to a library chunk or fact with provenance." DR-0002 lists repeatable facts: census tracts 06013313203 and 06013314105, CHAT 3.55, "21–35 days over 100°F by the 2090s", Green Heart "13–20% lower hsCRP", and $4,217,818. A reused number that drifted ("20–35 days") or lost its source is exactly the defect this catches.

## How it would fit (M7, stage 1 of the [adversarial pass](adversarial-review-pass.md))

1. **Extract** (LLM, structured output): `claims[] = {id, sentence_id, text, type: number|date|name|causal|outcome|evaluative, quote}`. Evaluative claims ("strong partnership") are tagged and skipped. They belong to the rubric judge.
2. **Resolve deterministically**: normalise numbers, units, and ranges, then match against M3 `facts[].value`. Match names against the entity registry, including aliases, which catches "Council/Counsel". Use the provenance map from M6 when the sentence already cites a fact id.
3. **Verify the remainder** (LLM): pass candidate facts as documents with [Citations](anthropic-citations-api.md) enabled and ask whether claim X is supported, contradicted, or not addressed. Keep the returned `cited_text` as proof.
4. **CoVe-style independence**: the verifier sees only the claim and the candidate facts, *not* the surrounding draft, so fluent context can't carry an unsupported claim.
5. **Report**: per-claim status, with `unsourced` claims turned into suggested `[[NEEDS SOURCE: …]]` placeholders. Also report a draft-level *supported fraction* (FActScore-style) as a trend metric, not a gate.

**Hallucination detection** comes for free: any `number`, `date`, or `name` claim with no registry match and no provenance is a hallucination candidate. Invented community quotes (the pressure point for HR Q1 "voices") are caught the same way. Quotes must resolve to a registry entry holding the consented source, or they're flagged.

**Cross-section consistency** is a join. The same fact id or entity appearing with different values across answers is a contradiction, found without an LLM.

## Strengths

- Registry-grounded, so it is far more reliable than open-web SAFE. Most checks are string or number matches.
- Every verdict carries a pointer: a fact id or a cited span.
- Also feeds M3 curation: frequently `unsourced` claims show which facts the registry is missing.

## Weaknesses / risks

- Atomic-claim extraction is imperfect. It splits too finely or merges, and misses implicit claims.
- Paraphrase and causal claims ("shade reduces exposure") need an evidence standard the registry may not hold yet.
- Only as good as the registry. A wrong registry fact passes. Validity windows in M3 help.

## Verdict rationale

**Adopt.** This is the most direct implementation of the project's truthfulness rule. It is mostly deterministic, and it produces exactly the per-claim audit trail funders' claims need.

Parent: [LLM evaluation](index.md)
