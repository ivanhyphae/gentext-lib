---
title: Prompt caching, Batch API, and thinking for judge passes
slug: claude-caching-batch-thinking
level: 3
parent: index.md
related: [claude-structured-outputs.md, adversarial-review-pass.md, inspect-ai.md, judge-reliability.md]
tags: [claude, cost, prompt-caching, batch, extended-thinking, reproducibility]
status: draft
updated: 2026-09-25
kind: service
verdict: adopt
fit: [M7, M10]
license: proprietary API
maturity: mature
inspectability: medium
sources:
  - title: "Claude docs: Pricing"
    url: https://platform.claude.com/docs/en/about-claude/pricing
    accessed: 2026-09-25
  - title: "Claude docs: Prompt caching"
    url: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
    accessed: 2026-09-25
  - title: "Claude docs: Batch processing"
    url: https://platform.claude.com/docs/en/build-with-claude/batch-processing
    accessed: 2026-09-25
  - title: "Claude docs: Thinking"
    url: https://platform.claude.com/docs/en/build-with-claude/thinking
    accessed: 2026-09-25
  - title: "Claude docs: Extended thinking (manual mode, migration)"
    url: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
    accessed: 2026-09-25
---

# Prompt caching, Batch API, and thinking for judge passes

> **TL;DR** Put the stable material first: persona instructions, rubric, facts, sibling answers. Cache that prefix and put the draft last. Use the Batch API (50% off, stacks with caching) for calibration sweeps, and interactive calls when writers are waiting. Leave adaptive thinking on for the skeptic and adjudicator. Thinking text is only a *summary*, so every rationale that matters must be in the visible JSON. **Adopt.** Prices are as of 2026-09-25 and go stale quickly.

## What it is (facts as of 2026-09-25)

**Prices** per MTok ([pricing](https://platform.claude.com/docs/en/about-claude/pricing)):

| Model | Input | Output | Cache hit | Batch in/out |
|---|---|---|---|---|
| Opus 5.5 | $4 | $20 | $0.20 (0.05×) | $2 / $10 |
| Sonnet 5 | $2 | $10 | $0.20 | $1 / $5 |
| Haiku 4.5 | $1 | $5 | $0.10 | $0.50 / $2.50 |

- Claude 4.7+ uses a tokenizer that produces about 30% more tokens for the same text.

**Prompt caching** ([docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)):
- Writes cost 1.25× base (5-minute TTL) or 2× (1-hour TTL).
- Up to 4 breakpoints.
- The minimum cacheable prefix is 512 tokens on Opus 5.5 and 4,096 on Haiku 4.5. Shorter prefixes silently don't cache.
- Multipliers "stack with… the Batch API discount".

**Batch** ([docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing)):
- 50% off input and output.
- Most batches finish in under an hour, and a batch expires if not done in 24h.
- Limit of 100,000 requests or 256 MB per batch; results are kept 29 days.
- Cache hits in batches are best-effort (30–98%). The docs suggest the 1-hour TTL.

**Thinking** ([docs](https://platform.claude.com/docs/en/build-with-claude/thinking)):
- On Opus 5.5 and Sonnet 5, adaptive thinking is on by default. Depth is steered with `output_config.effort`.
- `budget_tokens` manual mode returns 400 on 4.7+ ([extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)).
- The thinking text is "never the raw chain of thought", only a summary. `display` defaults to `"omitted"` on current models.
- Thinking tokens are billed as output.
- Changing effort or thinking settings invalidates cache breakpoints.

## Why it matters for gentext

A review pass is the same large prefix (Appendix F excerpt, checklist, facts, personas) with small changing tails (the draft). That is the ideal caching shape. Calibration (gold set × k runs × prompt variants) is exactly the non-urgent bulk work Batch is for.

## How it would fit

- **Prefix layout**, from most stable to least:
  1. tool/schema;
  2. system: role and procedure;
  3. solicitation question + checklist + few-shot anchors *(breakpoint)*;
  4. facts + sibling answers *(breakpoint)*;
  5. the draft, uncached.
- **Model tiering (proposal)**:
  - Haiku 4.5: claim extraction and deterministic-adjacent tasks.
  - Sonnet 5: panel personas.
  - Opus 5.5: skeptic and adjudicator.
  - Using a different tier from the drafter gives some judge/drafter separation.
- **Reproducibility record**: model id, effort, thinking display, schema hash, prompt hashes, rubric version, draft sha, and the `usage` block. The same inputs give comparable, not identical, outputs, so run k = 3 for calibration.
- **Cost estimate** (not measured): one question costs about $0.30–$1 per full pass on the interactive API, and about half that in batch.

## Strengths

- Large, documented savings. Batch and cache discounts stack.
- Thinking improves hard adjudications without us writing chain-of-thought prompts.

## Weaknesses / risks

- Thinking is opaque (summaries only), so it doesn't count toward inspectability. Require rationale fields in the output.
- Cache invalidates on any change to the schema, effort, or prefix, so a prompt edit mid-run spoils the savings.
- The 24h batch window is risky near the 2026-10-13 deadline. Keep interactive calls as the default for live drafting.
- Prices and model lineup change quickly. Re-check before budgeting.

## Verdict rationale

**Adopt.** These are configuration choices, not dependencies, and they make repeated rubric passes cheap enough to run on every draft.

Parent: [LLM evaluation](index.md)
