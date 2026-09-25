---
title: LLM-as-span-annotator (quoted spans, reason-first, validated offsets)
slug: s-llm-span-annotation
level: 3
parent: index.md
related: [span-feedback-schema.md, s-scarecrow-taxonomy.md, s-slop-measurement.md, ../llm-evaluation/adversarial-review-pass.md, ../llm-evaluation/claude-structured-outputs.md, ../provenance/span-anchoring.md]
tags: [llm-as-judge, span-annotation, structured-outputs, witness, factgenie]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M7]
license: factgenie MIT; technique n/a
maturity: emerging
inspectability: high
sources:
  - title: Kasner et al. Large Language Models as Span Annotators (arXiv 2504.08697)
    url: https://arxiv.org/html/2504.08697v2
    accessed: 2026-09-25
  - title: Semin, Dušek, Kasner. Strategies for Span Labeling with Large Language Models (arXiv 2601.16946)
    url: https://www.alphaxiv.org/abs/2601.16946
    accessed: 2026-09-25
  - title: ufal/factgenie (MIT; v1.2.1, 2026-01-15)
    url: https://github.com/ufal/factgenie
    accessed: 2026-09-25
  - title: Shaib et al. Measuring AI "Slop" in Text (zero-shot span extraction results)
    url: https://arxiv.org/html/2509.19163v2
    accessed: 2026-09-25
  - title: Chakrabarty et al. Can AI writing be salvaged? (LLM span detection precision)
    url: https://arxiv.org/html/2409.14509v5
    accessed: 2026-09-25
---

# LLM-as-span-annotator

> **TL;DR** **Adopt**, as the LLM layer of the span-feedback pipeline. Ask Claude for **quoted spans, not character offsets**, one taxonomy slice at a time, with the **reason written before the span** and a detailed guideline. A validator then locates each quote in the text (exact, then prefix/suffix disambiguation) and computes the offsets itself. It drops anything that doesn't match. This is the *witness* pattern from [llm-evaluation](../llm-evaluation/index.md), applied to style and slop. Expect only moderate agreement with humans (span precision around 0.2–0.5 in the literature), so these findings are suggestions for Claude or a human to accept or reject, not verdicts.

## Evidence

- **Kasner et al. 2025** compared LLMs with skilled annotators on data-to-text errors, MT errors and propaganda techniques. Findings:
  - Model-generated **character indices were unreliable** ("frequently generates indices that do not match"). The authors switched to JSON `{reason, text, type}` and heuristic string matching.
  - Putting `reason` **first** reduces post-hoc rationalisation.
  - Detailed guidelines matter: removing them hurt significantly. Few-shot examples did not consistently help, and sometimes hurt reasoning models.
  - Reasoning models beat instruction-tuned models of similar size. On D2T the best models (o3-mini, Claude 3.7, Gemini 2.0) reached human inter-annotator agreement. Propaganda was much harder (γ 0.16 vs 0.31 for humans).
  - Cost was about $3.60 per 1,000 outputs against about $500 for crowdworkers.
  - Related categories get confused, and repeated strings cause matching collisions.
- **Semin, Dušek & Kasner 2026** compared inline tagging, numeric indexing and content matching. Inline tagging is a dependable baseline, and constrained decoding (*LogitMatch*) fixes quote mismatches. The Claude API doesn't expose logits to us, so the validator does that job instead.
- **Shaib et al.**: zero-shot slop span extraction reached character-level precision of only 0.13–0.16, while **LAMP** 5-shot detection reached 0.46 precision (0.20 with the category required). Narrow, well-defined categories do much better than "find the slop".
- **factgenie** (MIT) is a self-hosted UI for collecting span annotations from humans and LLMs. It is useful for building our gold set, though Anthropic support isn't documented *(unverified)*.

## Recipe for adapt-rfp

1. **One pass per slice**: `slop.*`, `style.*`, `relevance/generic` (with M5 prompt and rubric), `fact.*` (with M3 facts; see [claim verification](../llm-evaluation/claim-verification.md)). Each pass gets its category definitions, "what not to flag" (humanizer's false-positive section, the M5 allowlist) and 2–3 examples drawn from LAMP or our gold set.
2. **Context in, not just the paragraph**: question prompt, target place, and the deterministic and statistical findings already found, so the LLM doesn't duplicate them. It may cite them as evidence.
3. **Output via strict tool use** ([structured outputs](../llm-evaluation/claude-structured-outputs.md)): `reason → quote → category → severity → suggestion`. Require quotes of at least 3 words, extended to the full clause where possible.
4. **Validate** in plain Python: exact match after whitespace/quote normalisation, then prefix/suffix, then fuzzy match with a threshold. On a miss, drop and log. The pilot Ambrose doc has about 1% duplicate sentences and 4% repeated 6-grams (probe, 2026-09-25), so disambiguation is needed. `category` must exist in the taxonomy, and `suggestion` must not add unsourced numbers or names: run the L11 number/entity extractor on it.
5. **Budget**: cap findings per paragraph (for example 5) and ask for the most consequential first. This counters nit-picking under "be strict" instructions.
6. **Calibrate** on a small gold set (about 30 paragraphs, 2 raters, including LAMP-style edits of our own drafts) per slice. Keep a category only when its precision is acceptable. The invalid-quote rate is a health metric.

## Strengths

- Covers what rules cannot: purple prose, unnecessary exposition, poor structure, off-prompt, genericness in context.
- Suggestions come in the same record, so Claude can revise from them.

## Weaknesses / risks

- Precision is moderate at best. Category confusion (cliché vs purple prose) is common. Merge near-synonyms, or accept `also:` labels.
- Claude annotating Claude has a self-preference risk. Occasionally use a different-family annotator ([Gemini card](a-google-cloud-nl-vertex.md)).
- Cost scales with passes. Use caching of the shared prefix ([caching](../llm-evaluation/claude-caching-batch-thinking.md)).

## Verdict rationale

This is the only practical way to get LAMP- and Shaib-style categories on our drafts. The quote-and-validate design keeps it inspectable. Adopt, with calibration gating each category.

Parent: [Prose signals](index.md) · Up: [Span-feedback schema](span-feedback-schema.md)
