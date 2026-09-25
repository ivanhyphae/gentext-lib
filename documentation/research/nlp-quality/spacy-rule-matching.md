---
title: spaCy rule matching and gazetteers
slug: spacy-rule-matching
level: 3
parent: index.md
related: [rapidfuzz.md, abbreviation-detection.md, vale.md, languagetool.md, check-catalog.md]
tags: [spacy, ner, entity-ruler, phrase-matcher, context-leakage, grammar, passive-voice]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M3, M4, M7]
license: MIT (spaCy and en_core_web models)
maturity: mature
inspectability: high
sources:
  - title: explosion/spaCy GitHub repository (MIT; release v3.8.16, 2026-08-24)
    url: https://github.com/explosion/spaCy
    accessed: 2026-09-25
  - title: spaCy rule-based matching guide (Matcher, PhraseMatcher, EntityRuler)
    url: https://spacy.io/usage/rule-based-matching
    accessed: 2026-09-25
  - title: Local probe with spaCy 3.8 + en_core_web_sm 3.8.0 (synthetic sentences), scratchpad, not committed
    url: https://github.com/explosion/spacy-models/releases/tag/en_core_web_sm-3.8.0
    accessed: 2026-09-25
---

# spaCy rule matching and gazetteers

> **TL;DR** **Adopt.** spaCy (MIT, v3.8.16 on 2026-08-24) is the programmable core of M4/M7. It provides the **PhraseMatcher/EntityRuler** built from the entity registry and place gazetteer (canonical names and context leakage), token **Matcher** patterns for pilot grammar errors, **dependency labels** for passive voice, and statistical **NER** to surface unknown orgs and places for review.

## What it is

An industrial NLP library: tokenizer, POS tagger, dependency parser, NER, and rule components. `Matcher` matches token-attribute patterns (LOWER, POS, TAG, DEP, OP quantifiers). `PhraseMatcher` does fast exact matching over thousands of phrases (optionally on `LOWER`). `EntityRuler` adds pattern-based entities with custom labels and `id`s, and can run before or after the statistical NER.

## Why it matters for adapt-rfp

| Pilot defect | spaCy mechanism |
|---|---|
| "…for Fresno County" in a Bay Point draft | EntityRuler over the M3 gazetteer: every place, org, funder, and program gets a pattern with `id: place/fresno-county`. After matching, compare each `ent.ent_id_` with the draft target's allowlist. Off-target means leakage. |
| "Council"/"Counsel" | PhraseMatcher on canonical names *and* known bad aliases (bad alias → error). Unmatched ORG spans go to [rapidfuzz](rapidfuzz.md). |
| "one of the primary recreational facility" | Matcher pattern (below) |
| passive voice | tokens with `dep_ in {"nsubjpass","auxpass"}` (English models); flag if no `agent` child |
| unknown entities | statistical NER `ORG/GPE/LOC` not covered by the gazetteer → "add to registry or fix" |

**Grammar probe (local, 2026-09-25).** The pattern `one of the|our|its|their` + `(ADJ|ADV|NOUN|PROPN)*` + singular `NN/NNP` + non-noun caught:

- "one of the primary recreational facility in…" ✔
- "one of the best student here" ✔
- no hit on "…recreational facilities…" ✔
- **false positive** on "one of the city park staff." (mass/collective noun)

In the same probe, LanguageTool's public API missed all three errors ([card](languagetool.md)). Keep a mass-noun exception list (staff, equipment, infrastructure, data).

## How it would fit

- `adapt-rfp.nlp.pipeline(target)` builds `en_core_web_sm` (or `_md`/`_trf` if accuracy matters) + EntityRuler from `library/registry/*.yaml` + custom Matchers, cached per registry hash.
- Each finding records `pattern_id`, token span, and registry id. That meets the inspectability bar.
- The gazetteer carries `scope` metadata (`place: fresno-county`, `region: central-valley`), so the leakage rule is "entity scope ∉ target scope". Places *near* the target (e.g., Pittsburg, Concord) can be allowlisted per chunk.
- The same pipeline gives M4 its tokens, sentences, and POS ratios. TextDescriptives and scispaCy plug in as components.

## Strengths

- Deterministic rules plus optional statistics in one pipeline. Findings are explainable down to the token.
- Very fast on CPU. Models are MIT-licensed and small (`sm` ≈ 12 MB *(size unverified)*).
- Rich ecosystem (scispaCy, TextDescriptives, spacy-llm).

## Weaknesses / risks

- The statistical NER misses or mislabels local names (e.g., "Bay Point Garden Club"). The gazetteer must carry the load, and NER is only a safety net.
- Tagger errors propagate into grammar rules. Grammar findings stay warnings.
- Rule sprawl: keep patterns in data files with fixtures (the DR-0002 defects as tests).

## Verdict rationale

Required for leakage and grammar checks, and it hosts most other deterministic checks. Low cost, high inspectability.

Parent: [NLP quality checks](index.md)
