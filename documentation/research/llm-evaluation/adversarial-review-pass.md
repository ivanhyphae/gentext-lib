---
title: Adversarial review pass design
slug: adversarial-review-pass
level: 2
parent: index.md
related: [judge-reliability.md, panel-simulation.md, critic-reviser-loop.md, multi-agent-debate.md, claim-verification.md, rubric-judging.md, claude-structured-outputs.md, ../provenance/span-anchoring.md]
tags: [adversarial-review, red-team, llm-as-judge, grant-narrative, inspectability]
status: draft
updated: 2026-09-25
---

# Adversarial review pass design

> **TL;DR** This is a five-stage pass over one narrative answer: claim verification, rubric panel, skeptic, rebuttal, and deterministic validation. It emits `findings.jsonl`. Every finding carries a verbatim quote, a rubric line id, a category, and a status after rebuttal, and anything that fails the verbatim check is dropped. The pass proposes; people dispose. It never rewrites canonical text and never promises a score.

## Inputs (all from the repo, all versioned)

| Input | Source | Why |
|---|---|---|
| Draft answer + sentence ids + provenance map | M6 | Critiques anchor to sentences; claims map to chunk/fact ids |
| Question record | M5 YAML | Prompt, word limit, points, **band descriptors split into checklist items** with stable ids |
| Facts cited by the draft (+ nearby registry entries) | M3 | Ground truth for claim verification |
| Deterministic QA report | M7 | So the LLM doesn't re-litigate word counts or leakage, and can cite them |
| Sibling answers in the same application | M6 | Cross-section consistency (partners, numbers, timeline) |
| Funder values glossary | M5 | EHCRP's four values, used as the panel's vocabulary |

Some things are excluded on purpose: the drafter's prompt, library marketing summaries, and any "this is a strong draft" framing. The judge sees what a reviewer would see, plus the registry.

Example checklist decomposition for **EHCRP HR Q1** (Appendix F): `specific-community` (names the heat-vulnerable community), `exposure` (how exposure occurs), `harms` (what harms result), `data` (relevant data present), `integration` (data and lived experience combined to show *who* and *why*), `voices` (community quotes or stories), and `not-generic` (would not apply equally to many communities). The *Medium* descriptor supplies the negative test for `not-generic`.

## Stages

### 1. Claim verification (grounding before judging)
Split the draft into atomic claims, FActScore-style. Resolve each claim against M3: numbers, dates, and names are matched deterministically first. The LLM checks support only for the remainder, using the [Citations API](anthropic-citations-api.md) with registry facts supplied as documents so the support pointer is exact. Statuses are `supported`, `contradicted`, `unsourced`, and `needs-human`. Unsourced claims become `[[NEEDS SOURCE]]` suggestions, never fixes. See [claim-verification](claim-verification.md).

### 2. Panel (constructive scoring)
Three personas score independently in fresh contexts. Each persona prompt says whose priorities it weighs, and all three read the same Appendix F text; see [panel-simulation](panel-simulation.md). For each checklist item the persona marks `met / partial / absent` and **must quote** the span it relied on, or write `absent` with no quote. Only then does it pick a band and points inside the band's range. Asking for evidence first and verdict second is the ordering shown to reduce cue-anchored rationalisation ([arXiv 2605.23970](https://arxiv.org/abs/2605.23970), accessed 2026-09-25).

### 3. Skeptic (adversarial)
A single "skeptical reviewer" gets the panel output. Its job is the **strongest honest case for scoring one band lower**. It is limited to a closed set of categories:

`generic` · `unsupported-claim` · `missing-evidence-type` · `inconsistent-with:<section>` · `overclaim/booster` · `context-leak` · `unclear-sequence` · `jargon` · `does-not-answer-prompt`

It has to produce at least one finding per checklist item that the panel marked `met`, or state "no credible objection". That forces coverage without forcing invention. It also runs the **place-swap probe**: "List sentences that would remain true if *Bay Point* were replaced by *another Contra Costa community*." Those sentences are candidate `generic` findings.

### 4. Rebuttal (debate-lite)
A defender answers each skeptic finding, but may only cite draft spans or M3 fact ids, not new prose. An adjudicator, as a fresh context, rules `upheld / rejected / partially` with a one-line reason. This is the useful core of [debate](multi-agent-debate.md) without open-ended rounds. It prunes false positives, which matters because judges are lenient in some settings and nit-picky under "be strict" instructions (see [judge-reliability](judge-reliability.md)).

### 5. Deterministic validation (the inspectability gate)
Plain Python, no LLM:
- `quote.exact` must occur in the draft (after whitespace normalisation), with `prefix`/`suffix` used to disambiguate. This is the TextQuoteSelector shape from [span anchoring](../provenance/span-anchoring.md).
- `rubric_ref` must exist in the M5 YAML.
- `fact_id` references must exist in M3.
- Points must fall inside the chosen band's range.

Failures are **dropped and logged** as `invalid_findings`. The invalid rate is itself a judge-health metric.

## Output schema (sketch)

```yaml
run: {id, date, model, effort, prompt_hashes, rubric_version, draft_sha}
panel:
  - persona: equity-reviewer
    items: [{rubric_ref: EHCRP-R2/HR-Q1/high/voices, status: absent, quote: null}]
    band: medium
    points: 4
findings:
  - id: F7
    stage: skeptic
    category: generic
    rubric_ref: EHCRP-R2/HR-Q1/medium/not-generic
    quote: {exact: "...", prefix: "...", suffix: "..."}
    rationale: "Sentence is true of any hot inland suburb."
    suggestion: "Use the Bay Point bus-stop shade gap (fact F-0123) instead"   # advisory
    rebuttal: {status: upheld, reason: "no local specific in span"}
invalid_findings: [...]
```

Structured outputs enforce the shape ([claude-structured-outputs](claude-structured-outputs.md)). Constraints that JSON Schema can't express there, such as `minLength` and numeric ranges, are enforced in stage 5.

The run is rendered in two places. A Markdown report groups findings by rubric item, so a reviewer sees "Voices: absent (3/3 personas)". The same findings also go to M9 as span comments.

## Revision policy

- Default: **a human revises**, working from the findings.
- Optional bounded [critic-reviser loop](critic-reviser-loop.md): at most two rounds. The reviser may only swap in library chunk variants or registry facts, and every round re-runs the deterministic checks and stage 5. Stop when the upheld findings no longer decrease. Research shows intrinsic self-correction without external signal can degrade output ([arXiv 2310.01798](https://arxiv.org/abs/2310.01798), accessed 2026-09-25). Here the external signal is the registry and the validator.

## Cross-section consistency

Stage 3 also receives sibling answers and checks them pairwise: partner names and roles, dollar amounts, durations (Early tier: 30 months), counts, and the named community. Deterministic entity/fact diffing in M7 catches most of this. The LLM adds semantic contradictions, such as Q1 saying seniors are most exposed while Q2 designs only for youth.

## Guarding against rewarding generic fluent text

1. **Checklist, not impression.** Fluency earns no checklist item.
2. **Quote-or-absent.** Generic text yields quotes that the skeptic's `generic` category and the place-swap probe then target.
3. **Deterministic specificity signals from M4**, passed to the judge and reported alongside: local named entities, numbers resolving to M3, and funder-value terms per 100 words, plus booster count.
4. **Gold-set decoys.** Hand-write a fluent, on-topic, place-free HR Q1 answer. It must score Low or Medium on `not-generic` and `voices`, or the judge prompt fails calibration.
5. **Perturbation tests**, modelled on structured-perturbation grant review ([arXiv 2603.08281](https://arxiv.org/abs/2603.08281), accessed 2026-09-25): delete the community quote, swap the place name, pad with boosters. Scores must move in the expected direction.
6. **Length held fixed** by word limits, and variants compared at equal length. This counters verbosity bias.

## Cost envelope (estimate)

One question costs about 6–8 calls, each with about 8–12k input tokens (mostly a cached shared prefix) and about 1–2k output tokens. On Opus 5.5 that is roughly **$0.30–$1 per question per pass**, and the whole narrative (7 questions) comes to a few dollars. Batch mode halves it for calibration sweeps. See [claude-caching-batch-thinking](claude-caching-batch-thinking.md) for prices. *Estimate, not measured.*

Sources: inline links above; EHCRP Round 2 Final Guidelines, Appendix F (local `projects/`, not committed).

Parent: [LLM evaluation](index.md)
