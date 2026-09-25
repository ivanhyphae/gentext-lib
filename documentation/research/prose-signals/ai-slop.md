---
title: AI slop and LLM-text quality (landscape and recommendation)
slug: ai-slop
level: 2
parent: index.md
related: [span-feedback-schema.md, s-slop-measurement.md, s-edit-based-rewards-lamp.md, s-slop-lexicons.md, s-ai-detectors.md, s-scarecrow-taxonomy.md, s-llm-span-annotation.md, s-writing-critic-models.md, holistic-metrics.md, m-genericness.md, ../llm-evaluation/adversarial-review-pass.md, ../nlp-quality/stylometry-ai-detection.md]
tags: [ai-slop, llm-text-quality, taxonomy, lexicon, reward-model, ai-detection, M4, M7]
status: draft
updated: 2026-09-25
---

# AI slop and LLM-text quality

> **TL;DR** "Slop" is not one property. Research now splits it into **fixable span-level categories**: low density, irrelevance, templated structure, clichés, purple prose, unnecessary exposition, poor sentence structure, and lack of specificity. The field agrees on two things. Nobody, human or LLM, is reliable at a binary "this is slop" call. Experts *do* converge on the spans and on edits. So gentext should run a **three-layer slop pass**: curated lexicon/pattern detectors, statistical proxies plus an open reward model (WQRM), and a quote-validated Claude span annotator using the LAMP/Shaib taxonomy. All three emit one [span-feedback record](span-feedback-schema.md) that Claude revises from. AI-text *detectors* stay on hold: they answer "who wrote it", which provenance already records, not "is it good".

## The question

The maintainer wants tools that tell Claude "this is generic", "this is AI slop", "big grammar problems" or "style problems" over paragraphs and sections, with metrics and **spans that can feed correction**, deterministic or not. The earlier [NLP-quality](../nlp-quality/index.md) pass put AI detection on hold and pointed to the `humanizer` skill for AI tells. This page asks what else research offers now.

## What the research says (2024–2026)

| Finding | Source | Consequence |
|---|---|---|
| Slop = 3 themes / 7 codes: density, relevance; factuality, bias; structure, coherence, tone | [Shaib et al.](s-slop-measurement.md) | our top-level category tree |
| Binary slop labels: poor human agreement; GPT-5 et al. κ≈0; span precision 0.13–0.16 zero-shot | Shaib et al. | never ask "is this slop?"; ask per-category, span-first |
| Expert writers agree on 7 idiosyncrasies; the most common are awkward wording 28%, structure 20%, exposition 18%, cliché 17% | [LAMP, CHI 2025](s-edit-based-rewards-lamp.md) | the style/slop leaves; edit triple *(span, category, rewrite)* |
| Writer-edited > LLM-edited > raw; LLM edits already help | LAMP | a critic → targeted-edit loop is worth building |
| Frontier LLMs are near chance on writing-quality pairs; an edit-trained 400M model reaches 74% | [WQRM](s-edit-based-rewards-lamp.md) | an open local scorer is a useful second opinion |
| Slop phrases can be 1,000× over-represented vs human text; lists are model- and genre-specific | [Antislop, slop-forensics](s-slop-lexicons.md) | lexicons work but must be domain-tuned |
| LLMs as span annotators: moderate agreement, offsets unreliable, reason-first helps, guidelines essential | [Kasner et al.](s-llm-span-annotation.md) | quote, not offsets; validator computes positions |
| Scarecrow/FRANK/MQM converge on span + category + severity + explanation (+ antecedent) | [taxonomies](s-scarecrow-taxonomy.md) | the record shape; MQM severity weights |
| Detectors: Pangram near-zero FPR in NBER tests, but FPR 0–100% by tool on edited non-native academic text | [detectors](s-ai-detectors.md) | not a quality target for polished drafts |

## Signal families for "AI slop" in proposals

| Layer | Detector | Catches | Output | Verdict |
|---|---|---|---|---|
| 1. Deterministic | Curated AI-vocabulary + stock-phrase lexicon (humanizer ids, Wikipedia, excess-vocab) with M5 allowlist | clichés, AI vocabulary, sales tone | span hits, cluster density | adopt |
| | Pattern regexes: negative parallelism ("not X but Y"), tricolon, em-dash density, "serves as", copula avoidance | rhetorical tics | span hits | adopt |
| | Hype/booster lexicon (existing L8) | overclaim | span hits | adopt (exists) |
| 2. Statistical | templates-per-token / POS compression, idea density, repetition | templated structure, low density | paragraph metric, percentile | trial |
| | Genericness: anchors, concreteness, portability, place-swap ([m-genericness](m-genericness.md)) | lack of specificity | sentence findings | trial/adopt (sibling) |
| | Flat surprisal ([m-perplexity](m-perplexity.md)) | stock phrasing | span locator | assess (sibling) |
| | WQRM paragraph score ([card](s-writing-critic-models.md)) | overall polish | paragraph score, percentile | trial |
| 3. LLM | Claude span annotator: LAMP + Shaib categories, M5 prompt for relevance | purple prose, exposition, structure, off-prompt, generic-in-context | quoted spans + fix | adopt |
| Hold | AI-text detectors (Binoculars, Pangram, GPTZero…) | "machine-like" style | window scores | hold / optional risk check |

## Hands-on probes (2026-09-25; details on cards)

- **Lexicons.** Pilot docs showed 0.24–0.27 curated AI-vocab hits per 100 words, against 18.7 in a synthetic slop paragraph. Slop Score's public word list mostly flagged legitimate program vocabulary (*resilience*, *stewardship*, *interventions*). Curation and an M5 allowlist are required.
- **Negative parallelism.** Four hits in the 15k-word Ambrose doc, one of them a false positive from the simplified regex.
- **WQRM.** Pilot paragraphs scored 5.3–8.5 (mean 6.9). Synthetic slop scored 4.3 and its concrete rewrite 6.7, and pairwise mode preferred the rewrite. It runs in seconds on local GPU.
- **Quote anchoring.** About 1% of sentences in the pilot doc occur more than once, so quotes need prefix/suffix.
- **Not run**: Binoculars (two 7B models exceed our GPU), commercial detectors (see [a-ai-detection-apis](a-ai-detection-apis.md)), the WritingBench critic, and the `diversity` template metrics.

## Recommendation

1. **Adopt the unified [span-feedback schema](span-feedback-schema.md)** as the contract for every slop, style, grammar, genericness and fact detector, deterministic, statistical or LLM. It extends the witness findings of the [adversarial pass](../llm-evaluation/adversarial-review-pass.md) and the metric records of [norming](m-norming-presentation.md) instead of competing with them.
2. **Build layer 1 first**: a `lex.*` Vale/spaCy style sharing pattern ids with `humanizer`, a 50–150-entry curated list, the M5 allowlist, and cluster-based severity. It is cheap, catches the most visible tells, and gives Claude immediate spans.
3. **Add the Claude span annotator** with one category slice per call, reason-first, quotes validated. Calibrate each category on about 30 gold paragraphs. Seed the gold set by having a human edit 10–15 Claude drafts LAMP-style (span, category, rewrite); those edits double as few-shot examples.
4. **Trial WQRM** as a paragraph percentile and a rewrite tie-breaker. Report it, never gate on it.
5. **Revision loop**: Claude receives findings sorted by severity, fixes spans in place, and the detectors re-run. A finding closes only when its detector stops firing *and* the claim, number and leakage checks still pass. Stop after two rounds, or when major findings stop decreasing ([critic-reviser loop](../llm-evaluation/critic-reviser-loop.md)).
6. **Keep detectors out of the loop.** If a funder is known to screen with a detector, a human may run one on final text as a risk heat map and fix the flagged windows *via the taxonomy*.

## Evaluation lens

- **Powerful**: the three layers cover surface tics, structure and density, and contextual genericness.
- **Elegant**: one schema for all of them, and Claude revises from one list.
- **Inspectable**: every finding quotes the draft, names its detector and evidence, and can be rejected with a reason. The only opaque components (WQRM, the LLM) are advisory and calibrated.

## Caveats

- Nearly all slop research uses creative writing, news or QA. Grant prose legitimately repeats funder terms and restates prompts. Expect false positives until the allowlist and gold set exist.
- Pattern lists age with each model release. Version them and re-derive them from our own drafts (slop-forensics method).
- Claims about vendors and licenses were checked on 2026-09-25 and will go stale.

Parent: [Prose signals](index.md)
