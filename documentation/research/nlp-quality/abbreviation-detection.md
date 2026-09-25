---
title: Abbreviation detection (Schwartz-Hearst)
slug: abbreviation-detection
level: 3
parent: index.md
related: [vale.md, spacy-rule-matching.md, rapidfuzz.md]
tags: [acronyms, glossary, schwartz-hearst, scispacy]
status: draft
updated: 2026-09-25
kind: algorithm
verdict: adopt
fit: [M3, M4, M7]
license: Apache-2.0 (scispaCy); MIT (abbreviations package)
maturity: mature
inspectability: high
sources:
  - title: Schwartz & Hearst (2003), A simple algorithm for identifying abbreviation definitions in biomedical text, PSB
    url: https://psb.stanford.edu/psb-online/proceedings/psb03/schwartz.pdf
    accessed: 2026-09-25
  - title: allenai/scispacy README (AbbreviationDetector; v0.6.2, 2025-10-01)
    url: https://github.com/allenai/scispacy
    accessed: 2026-09-25
  - title: abbreviations on PyPI (0.2.5, 2019-12-30)
    url: https://pypi.org/project/abbreviations/
    accessed: 2026-09-25
---

# Abbreviation detection (Schwartz-Hearst)

> **TL;DR** **Adopt.** The Schwartz-Hearst algorithm extracts `Long Form (SF)` definition pairs with simple, auditable heuristics. Run it over every draft *and the whole library* and compare each pair with the glossary. This is the primary check for the **UTCI collision** ("Universal Thermal Climate Index" vs "Urban Thermal Comfort Index").

## What it is

A 2003 algorithm. It finds a short form in parentheses (or a long form in parentheses after an acronym), then scans backwards from the end of the candidate long form to match the short form's characters in order, where the first character must start a word. It needs no training and has no model. Implementations:

- **scispaCy `AbbreviationDetector`** (Apache-2.0, v0.6.2 2025-10-01): a spaCy component. `nlp.add_pipe("abbreviation_detector")` exposes `doc._.abbreviations`, with `span._.long_form` on each short form. It also propagates the definition to later bare uses of the short form in the doc. It is tuned for biomedical text but works on general English.
- **`abbreviations` package** (MIT, 0.2.5, last release 2019): a pure-Python `schwartz_hearst.extract_abbreviation_definition_pairs()`. It is unmaintained and emits a Python 3.12 `SyntaxWarning`.
- Writing our own is about 60 lines, and many copies are public. This may be the most inspectable option.

## Local probe (2026-09-25)

Synthetic text: "Universal Thermal Climate Index (UTCI) … Urban Thermal Comfort Index (UTCI)". The `abbreviations` package returned `{'UTCI': 'Urban Thermal Comfort Index'}`. It **collapsed to a single expansion and hid the collision**. Collision detection must therefore keep *all* pairs, with offsets, and not a dict keyed by short form. scispaCy was not probed locally.

## How it would fit

1. M4: for each chunk and draft, extract a list of `(short, long, offset)`.
2. M3: the glossary entry `UTCI: {expansion: Universal Thermal Climate Index, source: …}`.
3. M7 check L2 errors:
   - `long` differs from the glossary expansion (normalize case, hyphens, and plurals first; use [rapidfuzz](rapidfuzz.md) ≥ 95 to tolerate "Climate-Index"-style noise).
   - More than one distinct `long` per `short` within a draft, or across `library/` (library-wide audit).
   - A short form in the draft with no glossary entry (warning: "add to glossary").
4. Vale `conditional` covers "used before defined" inside a single file ([Vale](vale.md)).

## Strengths

- Deterministic, fast, explainable ("found 'Urban Thermal Comfort Index (UTCI)' at char 1204").
- Published precision was high on the original biomedical test sets *(figures not re-verified here)*.
- Doubles as a glossary bootstrapper: harvest pairs from the pilot to seed `library/glossary/`.

## Weaknesses / risks

- Misses definitions not in the parenthetical pattern ("UTCI, or the Universal…", "UTCI stands for…"). Add a couple of Matcher patterns.
- Does not detect a *wrong* expansion that is never written out. That case is covered only if the glossary states the expansion and the draft expands it somewhere.
- scispaCy pins specific spaCy versions and pulls heavy dependencies *(verify compatibility with spaCy 3.8 before adopting)*. A vendored implementation avoids this.

## Verdict rationale

It is small, classical, and targets a real pilot defect. Adopt the algorithm, and prefer a vendored implementation with a fixture test for the UTCI case.

Parent: [NLP quality checks](index.md)
