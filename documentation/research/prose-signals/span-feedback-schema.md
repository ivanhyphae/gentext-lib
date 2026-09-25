---
title: Span-feedback schema (one finding format for deterministic, statistical and LLM detectors)
slug: span-feedback-schema
level: 2
parent: index.md
related: [ai-slop.md, s-scarecrow-taxonomy.md, s-llm-span-annotation.md, m-norming-presentation.md, ../llm-evaluation/adversarial-review-pass.md, ../nlp-quality/check-catalog.md, ../provenance/span-anchoring.md, ../llm-evaluation/claude-structured-outputs.md]
tags: [schema, findings, span-annotation, witness, M4, M7, M8]
status: draft
updated: 2026-09-25
---

# Span-feedback schema

> **TL;DR** Every detector, whether a Vale rule, a percentile metric, WQRM or a Claude annotator, emits the same **finding** record. It has a TextQuoteSelector anchor (`exact` / `prefix` / `suffix` plus a computed offset hint), a **dotted category** from one taxonomy, an MQM-style **severity**, **evidence** (metric vs norm, lexicon entry, rubric line, fact id, or the LLM's reason), a **suggestion** with constraints, the **detector** that produced it, and a lifecycle **status**. LLM findings are witnesses: a validator must find the quote, or the finding is dropped. The format is a superset of the [adversarial-pass findings](../llm-evaluation/adversarial-review-pass.md) and the [check-catalog report](../nlp-quality/check-catalog.md#report-shape), so nothing already designed has to change.

## Design rules

1. **Span first, score second.** Paragraph metrics still anchor to a paragraph and name their worst spans ([norming](m-norming-presentation.md)).
2. **LLMs quote; code locates.** Offsets are always computed by the validator, never trusted from a model ([evidence](s-llm-span-annotation.md)).
3. **One taxonomy, many sources.** `category` is ours. Source-native labels (LAMP, Shaib, Scarecrow, humanizer pattern) go in `also`.
4. **Evidence is typed.** A reader can tell at a glance whether a finding rests on a rule, a number or an opinion.
5. **Suggestions carry constraints.** The default is `no-new-facts`. A fix that needs a fact becomes `add-source`, which produces a `[[NEEDS SOURCE: …]]` placeholder (AGENTS.md).
6. **Advisory by default.** Only `fact.*`, `context.*` and structural checks may reach `critical`. Style and slop top out at `major`.

## Record (YAML, one per finding, stored in `findings.jsonl`)

```yaml
id: F-0031                         # stable within a run
run: R-2026-09-25-hrq1-03          # run header holds draft_sha, tool versions, prompt hashes
detector:
  id: lex.contrast                 # dotted; family.kind
  kind: deterministic              # deterministic | statistical | model | llm
  version: gentext-lex@0.1 / slop-score-regex@2026-09
  model: null                      # e.g. claude-opus-5-5, Salesforce/WQRM-PRE@<rev>
category: slop.contrast            # from the taxonomy below
also: [humanizer:9, wikipedia:negative-parallelism]
severity: minor                    # info | minor | major | critical  (weights 0/1/5/25)
confidence: 1.0                    # 1.0 for rules; calibrated precision for model/llm
scope: sentence                    # span | sentence | paragraph | section | document
anchor:
  exact: "not only on physical construction, but"
  prefix: "infrastructure depends "
  suffix: " also on the relational"
  start: 13435                     # computed by validator (here: offset in the pilot DOCX text extract)
  end: 13473
  sentence_id: S2.4
related_anchor: null               # Scarecrow antecedent: the other span for redundancy/contradiction
evidence:
  type: pattern                    # pattern | lexicon | metric | rubric | fact | reason
  rule: RE_NOT_BUT
  metric: null                     # {name, value, percentile, reference, direction}
  rubric_ref: null                 # EHCRP-R2/HR-Q1/medium/not-generic
  fact_id: null
  rationale: "Negative-parallelism frame; states the positive claim indirectly."
suggestion:
  action: rewrite                  # delete | replace | rewrite | tighten | make-specific | add-source | move | none
  replacement: null                # only for deterministic replace
  instruction: "State what the project does directly; drop the 'not only' frame."
  constraints: [no-new-facts, keep-funder-terms]
status: open                       # open | accepted | rejected | fixed | stale | invalid
resolution: null                   # {by, reason, round} when closed
```

`severity` is defined by consequence, not by taste:

| Severity | Meaning | Examples |
|---|---|---|
| critical | wrong or harmful to submit | contradicted fact, context leak ("…for Fresno County"), limit exceeded |
| major | a reviewer would likely mark it down | unanchored generic claim in a place-specific question; unsourced number; off-prompt paragraph |
| minor | weakens the prose; fix if cheap | cliché, negative parallelism, purple phrase, poor sentence structure |
| info | a signal, not a problem by itself | single AI-vocab word, paragraph WQRM at p30, detector window |

A paragraph **burden** (Σ weights per 100 words, MQM-style) may be reported as a trend. It is never a gate.

## Category taxonomy (v0)

| Category | Meaning | Maps from | Typical detectors |
|---|---|---|---|
| `slop.density` | many words, little content | Shaib density; LAMP exposition | idea density, LLM |
| `slop.exposition` | restating, wind-ups, announcing | LAMP unnecessary exposition; humanizer 28–29 | LLM, patterns |
| `slop.cliche` | stock phrase, AI vocabulary cluster | LAMP cliché; humanizer 7, 32; Wikipedia | lexicon, LLM |
| `slop.purple` | ornate, figurative, inflated | LAMP purple prose; humanizer 1 | LLM, lexicon |
| `slop.contrast` / `slop.tricolon` / `slop.typography` | rhetorical tics, em-dash density | humanizer 9, 10, 14; Slop Score | regex |
| `slop.template` | repeated sentence shapes | Shaib structure/templatedness | templates-per-token |
| `slop.tone` | sales language, booster, chatbot residue | Shaib tone; humanizer 4, 20–22; L8 | lexicon, LLM |
| `specificity.generic` | could apply to any community | LAMP lack of specificity; M5 rubric | anchors, place-swap, LLM |
| `relevance.off-prompt` | does not answer the question | Shaib relevance; Scarecrow off-prompt | E1/T4, LLM |
| `style.structure` | tangled, stacked or weakly linked sentences | LAMP poor structure; Scarecrow incoherent | readability, LLM |
| `style.word-choice` | awkward, vague, jargon | LAMP awkward; Scarecrow jargon | LLM, Vale |
| `style.redundant` | said twice (needs `related_anchor`) | Scarecrow redundant | MinHash, embeddings |
| `grammar.*` | agreement, tense, missing word | LAMP tense; Scarecrow grammar | LanguageTool, spaCy, CoLA |
| `fact.entity` / `fact.circumstance` / `fact.number` / `fact.out-of-source` / `fact.self-contradiction` | factual errors | FRANK; Scarecrow | M3 lookup, NLI, LLM |
| `context.leak` / `context.term` | wrong place/org; glossary variant | check catalog L1–L6 | gazetteer, Vale |

The adversarial skeptic's categories map to these as follows: `generic`→`specificity.generic`, `overclaim/booster`→`slop.tone`, `unsupported-claim`→`fact.out-of-source`, `context-leak`→`context.leak`, `jargon`→`style.word-choice`, `does-not-answer-prompt`→`relevance.off-prompt`.

## Two more examples

Statistical, paragraph scope, normed:

```yaml
detector: {id: model.wqrm, kind: model, model: Salesforce/WQRM-PRE@2025-04-15}
category: slop.density
severity: info
scope: paragraph
anchor: {exact: "<first 12 words of P3>", prefix: "", suffix: "", start: 2210, end: 3004}
evidence: {type: metric, metric: {name: wqrm, value: 5.3, percentile: 8, reference: firm-exemplar@3f2c, direction: low_is_bad}}
suggestion: {action: none, instruction: "Low polish vs firm corpus; see span findings in P3."}
```

LLM annotator (witness), with a rubric reference:

```yaml
detector: {id: llm.annotate.specificity, kind: llm, model: claude-opus-5-5, version: prompt@a91e}
category: specificity.generic
also: [lamp:lack-of-specificity]
severity: major
confidence: 0.62                       # calibrated precision of this slice on the gold set
anchor: {exact: "…", prefix: "…", suffix: "…"}   # offsets filled by validator
evidence: {type: reason, rubric_ref: EHCRP-R2/HR-Q1/medium/not-generic,
           rationale: "True of any hot inland suburb; no Bay Point anchor."}
suggestion: {action: make-specific, constraints: [no-new-facts],
             instruction: "Use a Bay Point fact from M3 (e.g., bus-stop shade gap) or insert [[NEEDS SOURCE: …]]."}
```

## Validator (plain Python, runs after every detector)

- `anchor.exact` is found in the draft at `draft_sha` after normalisation. `prefix`/`suffix` break ties. Otherwise the finding becomes `status: invalid` and is logged.
- `category` exists. `severity` respects the cap for its family. `rubric_ref` and `fact_id` resolve in M5/M3.
- LLM `suggestion.replacement` or `instruction` introduces no number, name or date absent from the draft plus the M3 facts supplied.
- Overlapping findings from different detectors on the same category **merge** into one record with `detector: [..]` listed. Agreement raises the displayed priority, not the severity.

## Revision contract (how Claude uses it)

1. The M8 `check-draft` tool returns open findings grouped by paragraph and sorted by severity, plus paragraph metrics.
2. Claude rewrites **only anchored spans**, cites finding ids in its edit note, and may mark a finding `rejected` with a reason. Rejections are calibration data.
3. All detectors re-run on the new draft. A finding becomes `fixed` when its anchor is gone *and* the same detector no longer fires there. It becomes `stale` when the anchor is gone but the detector fires elsewhere nearby, which means the problem moved.
4. Stop after two rounds, or when major findings don't decrease. A human approves the final text (DR-0007).

## Rendering

The same records become Claude Docs comments or Markdown annotations anchored like [provenance spans](../provenance/span-anchoring.md). Comment text: `[category · severity] rationale → instruction (detector)`.

Parent: [Prose signals](index.md) · Up: [AI slop](ai-slop.md)
