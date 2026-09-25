---
title: Critic–reviser loops (Self-Refine, Constitutional-style critique)
slug: critic-reviser-loop
level: 3
parent: index.md
related: [adversarial-review-pass.md, claim-verification.md, multi-agent-debate.md]
tags: [self-refine, critique, constitutional-ai, revision, red-team]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M6, M7]
license: n/a (technique)
maturity: mature
inspectability: medium
sources:
  - title: "Self-Refine: Iterative Refinement with Self-Feedback (Madaan et al., 2023)"
    url: https://arxiv.org/abs/2303.17651
    accessed: 2026-09-25
  - title: "Constitutional AI: Harmlessness from AI Feedback (Bai et al., 2022)"
    url: https://arxiv.org/abs/2212.08073
    accessed: 2026-09-25
  - title: "Large Language Models Cannot Self-Correct Reasoning Yet (Huang et al., 2023/ICLR 2024)"
    url: https://arxiv.org/abs/2310.01798
    accessed: 2026-09-25
---

# Critic–reviser loops (Self-Refine, Constitutional-style critique)

> **TL;DR** Generate, critique against explicit principles, revise, repeat. **Trial** it in bounded form only: at most two rounds, a critique grounded in rubric items and registry facts, a reviser that may only swap library variants or registry facts, and deterministic re-checks each round. Without external signal, self-correction can make things worse.

## What it is

- **Self-Refine**: the same LLM drafts, critiques its own draft, and revises it iteratively. Across 7 tasks, humans and metrics preferred the output by about 20% over one-shot generation ([arXiv 2303.17651](https://arxiv.org/abs/2303.17651)).
- **Constitutional-style critique**: the model critiques and revises against a written list of principles, the "constitution" ([arXiv 2212.08073](https://arxiv.org/abs/2212.08073)). For us the constitution is Appendix F's checklist items plus AGENTS.md truthfulness rules: no invented facts, visible placeholders, and no context leakage.
- **The counter-evidence**: on reasoning tasks, *intrinsic* self-correction (no external feedback) doesn't help and sometimes degrades output. Earlier gains relied on oracle labels ([arXiv 2310.01798](https://arxiv.org/abs/2310.01798)).

## Why it matters for adapt-rfp

Writers want suggestions, not just a grade. A critic–reviser loop turns the findings from the [adversarial pass](adversarial-review-pass.md) into a candidate revision. The danger is specific to proposals: a reviser "improving" specificity will happily invent a resident quote or a tree count. The loop has to be fenced.

## How it would fit

```
findings (upheld) ─► reviser(constrained) ─► draft'
                                   │
         deterministic M7 checks + claim verification + quote validator
                                   │
                  stop if upheld findings don't decrease, or round = 2
```

- **External signal, not introspection.** Critiques come from the skeptic and panel, anchored to quotes and rubric ids. Verification comes from M3 and deterministic checks. This is the setting where Huang et al.'s negative result does *not* apply, because the feedback isn't intrinsic.
- **Reviser allowed actions** (structured output): `replace_sentence(sentence_id, with: chunk_variant_id | fact_id | placeholder)`, `delete_sentence`, `reorder`. Free prose is allowed only as connective tissue under 15 words per edit, and it is flagged `llm-authored` in provenance.
- Any new claim not resolvable to M3 becomes `{>>TK source: …<<}`, never a fabricated number or quote.
- Output is a **diff plus rationale per edit** (finding id → edit), shown for human acceptance. Nothing is committed to `library/` automatically.

## Strengths

- Turns critique into concrete, reviewable edits.
- Reuses library length variants, which is what the library is for.
- Measurable: upheld findings per round and deterministic check deltas.

## Weaknesses / risks

- Fabrication pressure: the fix for "voices absent" is real community quotes, which only humans or partners can supply. The loop must output a request, not a quote.
- Convergence to bland: repeated revision can sand off voice. Track M4 specificity metrics each round.
- Self-preference: the reviser's output is scored by a same-family judge. Keep humans as the final judge ([judge-reliability](judge-reliability.md)).
- Cost multiplies with rounds. The cap of two keeps it bounded.

## Verdict rationale

**Trial**, behind a flag, after the review pass itself is calibrated. The critique half is already part of the adopted pipeline. The *auto-revise* half has to earn trust by showing that its edits get accepted by writers.

Parent: [LLM evaluation](index.md)
