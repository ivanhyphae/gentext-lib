---
title: NLP quality checks for proposal prose
slug: index
level: 1
parent: ../index.md
related: [check-catalog.md, embeddings-and-similarity.md]
tags: [nlp, qa, prose-lint, embeddings, M4, M7]
status: draft
updated: 2026-09-25
---

# NLP quality checks for proposal prose

> **TL;DR** Most of the pilot's real defects can be caught with **deterministic, explainable checks**: a glossary-driven Vale style, spaCy rule matchers over an entity/place gazetteer, Schwartz-Hearst acronym extraction, rapidfuzz near-miss names, a hype/booster lexicon, and MinHash for forks. Embeddings (sentence-transformers locally, or Voyage, which Anthropic's docs point to) come next, for rubric-evidence retrieval and redundancy. NLI claim checkers (MiniCheck, AlignScore) come after that, to test claim support. Treat stylometry and AI-text detection as **hold**.

## The question

Which classical NLP and embedding techniques should gentext's M4 (Characterize) and M7 (QA) modules use to check composed drafts? The checks must run **without an LLM**, be reproducible in CI, and explain each finding (rule id, span, the glossary or registry entry it came from). They must also catch every DR-0002 defect as a regression test.

## Landscape in one paragraph

**Prose linters** (Vale, proselint, LanguageTool, write-good, alex) apply rules to text. Vale stands out because its rules are YAML files we can version next to the glossary. **Text descriptives** (textstat, TextDescriptives) produce numbers such as readability, sentence length, and repetition, which are good for targets and trends but weak as pass/fail gates. **spaCy pipelines** (tokenization, POS, dependencies, NER, PhraseMatcher, EntityRuler) are the programmable core for names, places, grammar patterns, and passive voice. **Fuzzy and near-duplicate matching** (rapidfuzz, MinHash/LSH via datasketch, SimHash) handle misspellings and forked documents. **Embeddings** (sentence-transformers, bge/gte/nomic/Qwen3, Voyage 4) handle semantics: retrieval, rubric similarity, and redundancy. **NLI-based consistency models** (SummaC, AlignScore, MiniCheck) ask whether a sentence is supported by a source. **Stylometry and AI detectors** are unreliable and biased, so they are not suitable as gates.

## Recommended check pipeline (deterministic → statistical → embedding)

| Stage | Checks | Tools | Output |
|---|---|---|---|
| 0. Structural | word/char limits per question; `{>>TK …<<}` placeholders left; required sections | plain Python + M5 YAML | hard pass/fail |
| 1. Deterministic lexical | glossary terms and forbidden variants; acronym defined-once and matches glossary; canonical org names; **context leakage** (off-target places/orgs/funders); grammar patterns; hype/booster lexicon; passive voice; typography | Vale (vocab + custom styles), spaCy PhraseMatcher/EntityRuler/Matcher, Schwartz-Hearst, rapidfuzz, LanguageTool (secondary) | findings with rule id + span + registry ref |
| 2. Statistical | readability, sentence-length spread, repetition fractions, lexical overlap with sources, near-duplicate/lineage against library | textstat / TextDescriptives, datasketch MinHash | metrics vs targets; warnings |
| 3. Embedding / model | rubric descriptor → evidence retrieval; cross-answer redundancy; semantic near-duplicates; claim support against cited chunk/fact | sentence-transformers or Voyage; MiniCheck / AlignScore | scored findings with evidence sentence pairs |
| 4. LLM judge | rubric band judgment, tone | (out of scope here) | consumes stages 0–3 as evidence |

Each stage writes into one machine-readable report (see [check catalog](check-catalog.md#report-shape)). Later stages never override earlier deterministic failures.

## Pilot defect → technique

| DR-0002 defect | Primary check (deterministic) | Backstop |
|---|---|---|
| UTCI expanded two ways | Schwartz-Hearst pairs vs glossary; Vale `conditional` + `substitution` | embedding none needed |
| "Council/Counsel", "Resource(s) Conservation District" | Vale vocab `accept`/`reject`; PhraseMatcher on registry aliases | rapidfuzz near-miss (≥90 token-sort) |
| "…for Fresno County" in a Bay Point draft | gazetteer EntityRuler + target allowlist (places/orgs/funders) | spaCy NER GPE/ORG not in registry → review |
| "one of the primary recreational facility" | spaCy Matcher "one of the + singular noun" | LanguageTool (missed it in our probe) |
| "unprecedented precision", "cutting-edge" | hype/booster lexicon (NIH hype adjectives + Hyland boosters) | proselint/write-good weasel checks |
| Rubric wants community quotes/stories | quote detector (quotation marks + attribution verb) | embedding match to rubric "High" descriptor |
| Forked near-identical docs | MinHash/LSH over shingles | embedding cosine for paraphrase forks |
| Long vs "SHORTENED" variants | MinHash containment (LSH Ensemble) + embedding similarity → `shortened-from` | |
| Claims unsupported by fact registry | number/entity extraction → M3 lookup | MiniCheck against source chunk |
| Same point repeated across answers | sentence-embedding cross-answer similarity | MinHash on sentence shingles |

## Children

Level 2:
- [Check catalog](check-catalog.md): every proposed check, how it works, its false-positive profile, and the report shape.
- [Embeddings and similarity](embeddings-and-similarity.md): model choice, rubric matching, redundancy, NLI, and thresholds.

Level 3 cards:
- [Vale](vale.md): adopt
- [LanguageTool](languagetool.md): trial
- [proselint (with write-good, alex)](proselint.md): assess
- [spaCy rule matching and gazetteers](spacy-rule-matching.md): adopt
- [Abbreviation detection (Schwartz-Hearst)](abbreviation-detection.md): adopt
- [RapidFuzz](rapidfuzz.md): adopt
- [Hedge and booster lexicons](hedge-booster-lexicon.md): adopt
- [Readability and text descriptives](readability-descriptives.md): trial
- [MinHash / LSH near-duplicates](minhash-lsh.md): adopt
- [Keyphrase extraction (YAKE, KeyBERT)](keyphrase-extraction.md): assess
- [Sentence embeddings](sentence-embeddings.md): adopt
- [NLI claim support (SummaC, AlignScore, MiniCheck)](nli-claim-support.md): trial
- [BERTScore](bertscore.md): hold
- [Stylometry and AI-text detection](stylometry-ai-detection.md): hold

## Caveats

- Maintenance and license facts were checked on 2026-09-25 (GitHub and PyPI). They go stale. The YAKE license in particular is inconsistent across sources (see its card).
- Probes used synthetic sentences only. No pilot source text was sent to external services beyond the defect fragments already quoted in DR-0002.

Parent: [Research index](../index.md)
