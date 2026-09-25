---
title: Research wiki conventions
slug: conventions
level: 0
parent: index.md
tags: [meta]
status: stable
updated: 2026-09-25
---

# Research wiki conventions

> **TL;DR** The research is a pyramid. Read `index.md` (level 0) first, then a topic `index.md` (level 1), then comparison pages (level 2), then individual tool or technique cards (level 3). Every page opens with a TL;DR so a reader, human or LLM, can stop at any depth.

## Levels

| Level | What | Length | Example |
|---|---|---|---|
| 0 | Root index + cross-topic synthesis | 1–2 screens | `index.md` |
| 1 | Topic overview: the question, the landscape, a recommendation, links down | ≤ ~800 words | `storage-platforms/index.md` |
| 2 | Comparison or deep-dive across several options | ≤ ~1200 words | `storage-platforms/comparison.md` |
| 3 | Card for one tool, library, algorithm, or technique | ≤ ~600 words | `nlp-quality/vale.md` |

## Frontmatter

```yaml
---
title: Vale
slug: vale                       # filename without .md
level: 3
parent: index.md                 # relative path to the page one level up
related: [proselint.md, ../llm-evaluation/rubric-judging.md]   # relative paths
tags: [prose-lint, style, cli]
status: draft                    # draft | reviewed | stable
updated: 2026-09-25
# level-3 cards only:
kind: library                    # library | service | platform | algorithm | technique | standard | product
verdict: adopt                   # adopt | trial | assess | hold  (Thoughtworks-radar style)
fit: [M7]                        # adapt-rfp modules it serves (see decision-record/0003)
license: MIT
maturity: mature                 # experimental | emerging | mature | legacy
inspectability: high             # high | medium | low: can we see, diff, and audit what it does/stores?
sources:
  - title: Vale documentation
    url: https://vale.sh/docs/
    accessed: 2026-09-25
---
```

## Page body

1. `# Title`
2. `> **TL;DR** …` (1–3 sentences, including the verdict for cards)
3. Body. Suggested card sections: *What it is · Why it matters for adapt-rfp · How it would fit (module, interface) · Strengths · Weaknesses / risks · Verdict rationale · Sources*.
4. Link only with relative Markdown links. Every page links to its `parent`. Level-1 pages link to all their children.

## Evidence standards

- Claims about tools (features, licenses, pricing, maintenance status) must cite a source URL with an access date. Mark anything unverified as *(unverified)*.
- Prefer primary sources (docs, repos, papers) over blog posts.
- State the date sensitivity: pricing and "is it maintained" go stale fast.

## Evaluation lens

Rate options against the project's three adjectives, **powerful, elegant, inspectable**, and against its constraints: small team, a private git repo as the canonical store (DR-0005), Claude as the main LLM, and operation from Claude web as a target.
