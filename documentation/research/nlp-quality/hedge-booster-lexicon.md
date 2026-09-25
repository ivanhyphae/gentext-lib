---
title: Hedge and booster lexicons
slug: hedge-booster-lexicon
level: 3
parent: index.md
related: [vale.md, proselint.md, check-catalog.md]
tags: [style, hype, boosters, hedges, metadiscourse, lexicon]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M7]
license: n/a (our own lexicon; seeded from published research, lists re-typed not copied wholesale)
maturity: mature
inspectability: high
sources:
  - title: Millar, Batalo & Budgell (2022), Trends in the Use of Promotional Language (Hype) in Abstracts of Successful NIH Grant Applications, 1985-2020, JAMA Netw Open
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9412227/
    accessed: 2026-09-25
  - title: Millar et al. (2022), Hype in NIH Funding Opportunity Announcements, 1992-2020, JAMA Netw Open 5(11):e2243221
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9679874/
    accessed: 2026-09-25
  - title: Hyland (2005), Metadiscourse: Exploring Interaction in Writing (Continuum), book listing
    url: https://books.google.com/books/about/Metadiscourse.html?id=KDDLXQKxhbEC
    accessed: 2026-09-25
  - title: Hype or not? Formalizing automatic promotional language detection in biomedical research (arXiv 2509.24638)
    url: https://arxiv.org/abs/2509.24638
    accessed: 2026-09-25
---

# Hedge and booster lexicons

> **TL;DR** **Adopt.** Keep a versioned YAML lexicon of *hype adjectives* and *boosters/hedges*, seeded from the NIH grant-hype studies (139 adjectives in 8 categories) and Hyland's metadiscourse model. Report density per 100 words plus each hit with its category. This catches "unprecedented precision" and "cutting-edge" deterministically, as warnings.

## What it is

- **Hyland's metadiscourse model** divides interactional markers into *hedges* (perhaps, may, tend to), *boosters* (in fact, definitely, clearly, demonstrate), *attitude markers* (surprisingly, remarkable), *self-mention*, and *engagement markers*. Hyland (2005) gives the reference lists. We have not reproduced them here; consult the book, and build our own list rather than copying it.
- **NIH hype studies** (Millar, Batalo, Budgell, JAMA Network Open 2022). They identified **139 hype adjective forms in 8 categories**: importance (crucial, key, vital), novelty (innovative, unique, *unprecedented*, groundbreaking), rigor (robust, rigorous), scale (comprehensive, vast), utility (actionable, scalable, sustainable), quality (renowned, skilled), attitude (remarkable, exciting), and problem (dire, alarming, unmet). In successful NIH abstracts, 130 of these rose by 7,690 words per million from 1985 to 2020. By 2020 about 97% of abstracts contained at least one hype term.
- Grant-specific additions from our own copy: *cutting-edge, state-of-the-art, world-class, first-of-its-kind, revolutionary, transformative*. These are our assumptions, not from the cited studies.

## Why it matters for gentext

Reviewers read many applications. Hype is so common in successful grants that it cannot simply be "bad", but *unsupported* boosters (a superlative with no number or citation nearby) weaken credibility. The check should therefore:

1. Flag each hit with its category.
2. Look for **support**: a number, a fact id from the provenance map, or a citation within the same sentence. Unsupported hits get severity *warning*. Supported hits get *info*.
3. Report density (hits per 100 words) against a target band per funder.

Hedges matter in the other direction: overly hedged capability statements ("may potentially help") undersell. Track them as a separate ratio.

## How it would fit

- `library/lexicons/hype.yaml`: `{term, lemma, category, source: nih-hype-2022|hyland-2005|hyphae}`. Matching uses a spaCy PhraseMatcher on `LEMMA` (plural and inflection safe) with a POS filter (e.g., "key" only as ADJ).
- The same YAML can be exported to a Vale `existence` rule for editor-time feedback ([Vale](vale.md)).
- M4 stores densities per chunk, so the library can be searched for "low-hype variant".

## Strengths

- Transparent: every hit is a named word with a category and a citation for why it's on the list.
- Grounded in grant-specific research, not general style advice.

## Weaknesses / risks

- Context-blind. "Key" in "key informant interviews" is not hype. POS filters, a phrase allowlist, and the warning-only severity all help.
- Lexicons are English-only and need upkeep.
- Learned hype classifiers exist (arXiv 2509.24638), but they trade inspectability for recall. Assess them later.

## Verdict rationale

A cheap, explainable, research-grounded check aimed directly at a DR-0002 defect.

Parent: [NLP quality checks](index.md)
