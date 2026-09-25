---
title: Check catalog
slug: check-catalog
level: 2
parent: index.md
related: [embeddings-and-similarity.md, vale.md, spacy-rule-matching.md, abbreviation-detection.md, rapidfuzz.md, hedge-booster-lexicon.md, minhash-lsh.md]
tags: [qa, checks, M7, catalog]
status: draft
updated: 2026-09-25
---

# Check catalog

> **TL;DR** This page lists about 20 concrete checks, grouped by stage. For each one it gives the mechanism, the registry it depends on (glossary, entity registry, gazetteer, M5 solicitation), its false-positive profile, and the pilot defect it catches. Roughly 70% of the checks are deterministic and need only Vale, spaCy, rapidfuzz, and a few hundred lines of Python.

## Design principles

1. **The registries are the rules.** Most checks are compiled from M3 (glossary, entity registry, place gazetteer) and M5 (limits, rubric). Editing a YAML entry changes the check, so nobody hand-writes rules twice. Vale styles can be generated from the glossary.
2. **Each finding carries its evidence:** `check_id`, `severity`, char span, matched text, suggestion, and `because` (the registry entry id, lexicon name, or model plus score).
3. **Precision over recall for errors, recall over precision for warnings.** Grammar and hype checks are warnings. Name, acronym, leakage, and limit checks can be errors.
4. **Deterministic first.** A check with a model inside (embeddings, NLI) must pin the model name and revision in the report so results can be reproduced.

## Stage 0: structural (M5-driven)

| id | Check | Mechanism | Pilot link |
|---|---|---|---|
| S1 | Word/char limit | Count words the way the funder does (state the rule in M5: hyphenated words, numbers). Report `limit - count`. | 250/300/350 limits |
| S2 | Placeholder left | regex `\[\[NEEDS SOURCE:.*?\]\]`, `TODO`, `XX` | truthfulness rule |
| S3 | Required elements | M5 question lists required named items (partners, dollar figures); presence check | compliance matrix |

## Stage 1: deterministic lexical

| id | Check | Mechanism | FP profile | Pilot defect |
|---|---|---|---|---|
| L1 | Canonical term / forbidden variant | Vale vocab `accept.txt` (→ `Vale.Terms`) + `reject.txt` (→ `Vale.Avoid`), generated from glossary + entity aliases ([Vale](vale.md)) | low | "Counsel", "Resources Conservation District" |
| L2 | Acronym expansion matches glossary | Extract (short, long) pairs with Schwartz-Hearst; compare each long form to glossary; flag >1 distinct expansion per acronym within a draft *or across the library* ([abbreviation detection](abbreviation-detection.md)) | low | UTCI collision |
| L3 | Acronym defined before use | Vale `conditional` rule, exceptions from glossary "no-expansion-needed" list | medium (headers, tables) | general |
| L4 | Org-name near-miss | PhraseMatcher over canonical names and aliases (exact), then [rapidfuzz](rapidfuzz.md) on noun chunks and NER ORG spans not matched exactly (token_sort_ratio ≥ 90, not equal) | medium; tune per registry | "Council/Counsel" |
| L5 | **Context leakage** | EntityRuler built from a gazetteer of places, orgs, funders, and programs, each tagged with `scope`. Compare to the draft's target (`places: [bay-point, contra-costa]`, `funder: lci`). Off-target entity → error. NER GPE/ORG not in gazetteer → "unknown entity" warning ([spaCy rules](spacy-rule-matching.md)) | low for gazetteer hits | "for Fresno County" |
| L6 | Funder-vocabulary misuse | Funder terms (EHCRP values) allowed only in drafts targeting that funder | low | DR-0003 terminology |
| L7 | Grammar patterns | spaCy Matcher: "one of the (ADJ)* NN" singular; article/number agreement; doubled words. LanguageTool as a broad secondary pass ([LanguageTool](languagetool.md)) | medium (mass nouns like "staff") | "one of the primary recreational facility" |
| L8 | Hype and boosters | Lexicon match with categories (novelty, importance, scale…), density per 100 words, and exemptions for quoted text ([lexicons](hedge-booster-lexicon.md)) | medium; always a warning | "unprecedented", "cutting-edge" |
| L9 | Passive voice | spaCy dependency labels `nsubjpass`/`auxpass` (en_core_web models); report a ratio, flag sentences with a passive verb and no agent | medium | style |
| L10 | Weasel/cliché/typography | proselint or Vale packages (write-good, proselint styles) | medium | style |
| L11 | Numbers and facts | Extract numbers, %, $, dates, census tract ids (regex + spaCy `CARDINAL/MONEY/PERCENT/DATE`). Each must resolve to an M3 fact id in the provenance map | low | fact registry |
| L12 | Rubric evidence: quotes | Detect quotation spans ≥ 5 words attributed with a speech verb (said, shared, told, noted) within the sentence. The count is the evidence | low | Harm Reduction Q1 "quotes or stories" |

## Stage 2: statistical

| id | Check | Mechanism | Use |
|---|---|---|---|
| T1 | Readability band | textstat / TextDescriptives (Flesch-Kincaid grade, sentence length mean/sd) | target band per funder; warning only ([readability](readability-descriptives.md)) |
| T2 | Repetition | TextDescriptives quality metrics (duplicate n-gram fractions) | catches pasted-twice paragraphs |
| T3 | Source overlap / lineage | MinHash Jaccard of draft paragraphs vs library chunks; containment for shortened variants ([MinHash](minhash-lsh.md)) | confirms provenance map; flags unattributed reuse |
| T4 | Keyphrase coverage | YAKE/KeyBERT keyphrases of the question prompt vs the answer ([keyphrases](keyphrase-extraction.md)) | cheap "did we answer the prompt" signal |

## Stage 3: embedding and model checks

See [Embeddings and similarity](embeddings-and-similarity.md) for thresholds and models.

| id | Check | Mechanism | Pilot link |
|---|---|---|---|
| E1 | Rubric evidence retrieval | Split each "High" descriptor into evidence expectations (M5). For each, the top-k draft sentences by cosine. Report the best sentence and its score, not a verdict | "community voices… stories" |
| E2 | Cross-answer redundancy | Sentence embeddings across all answers in one application; pairs above the threshold → "said twice" | redundancy |
| E3 | Semantic near-duplicate | Paraphrase-level forks that MinHash misses | forked docs |
| E4 | Claim support | For each factual sentence, run NLI/MiniCheck against the cited chunk or fact text ([NLI](nli-claim-support.md)) | provenance truthfulness |

## Not recommended as checks

- Stylometric or AI-text detection as a gate ([card](stylometry-ai-detection.md)).
- BERTScore as a quality score ([card](bertscore.md)). It measures similarity to a reference, and we rarely have a gold reference.

## Report shape

```yaml
draft: drafts/ehcrp-r2/harm-reduction-q1.md
target: {funder: lci, program: ehcrp, round: 2, places: [bay-point, contra-costa-county]}
tools: {spacy: 3.8.x, en_core_web_sm: 3.8.0, vale: 3.22.0, embed: voyage-4@2026-01}
findings:
  - check: L5.context-leakage
    severity: error
    span: [1832, 1846]
    text: "Fresno County"
    because: gazetteer:place/fresno-county (scope != target.places)
    suggest: "Remove or replace with Contra Costa County / Bay Point"
metrics: {words: 262, limit: 250, fk_grade: 15.8, passive_ratio: 0.21, hype_per_100w: 1.9}
```

A Markdown renderer turns this into annotated text for humans and Claude Docs (M9).

## Build order for the pilot slice

S1, S2 → L1, L2, L4, L5 (all four DR-0002 name, acronym, and leakage defects) → L7, L8, L12 → T3 → E1. That sequence covers every DR-0002 regression with only E1 needing a model.

## Sources

Tool facts on this page are cited on the linked level-3 cards. The key primary sources:

- Vale vocabularies and conditional check: https://docs.vale.sh/keys/vocab.md, https://docs.vale.sh/checks/conditional.md (accessed 2026-09-25)
- spaCy rule-based matching: https://spacy.io/usage/rule-based-matching (accessed 2026-09-25)
- TextDescriptives quality component: https://hlasse.github.io/TextDescriptives/quality.html (accessed 2026-09-25)
- The local probes (spaCy Matcher, Schwartz-Hearst, rapidfuzz, LanguageTool public API) were run on 2026-09-25 with synthetic sentences. Results are on the [spaCy](spacy-rule-matching.md), [abbreviation](abbreviation-detection.md), [rapidfuzz](rapidfuzz.md), and [LanguageTool](languagetool.md) cards.

Parent: [NLP quality checks](index.md)
