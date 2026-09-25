---
title: Multi-agent debate
slug: multi-agent-debate
level: 3
parent: index.md
related: [adversarial-review-pass.md, panel-simulation.md, critic-reviser-loop.md, judge-reliability.md]
tags: [debate, multi-agent, adversarial-review, oversight]
status: draft
updated: 2026-09-25
kind: technique
verdict: assess
fit: [M7]
license: n/a (technique)
maturity: emerging
inspectability: medium
sources:
  - title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate (Du et al., 2023)"
    url: https://arxiv.org/abs/2305.14325
    accessed: 2026-09-25
  - title: "Debating with More Persuasive LLMs Leads to More Truthful Answers (Khan et al., ICML 2024)"
    url: https://arxiv.org/abs/2402.06782
    accessed: 2026-09-25
  - title: "Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning (Wu et al., 2025)"
    url: https://arxiv.org/abs/2511.07784
    accessed: 2026-09-25
---

# Multi-agent debate

> **TL;DR** Several LLM instances argue positions over rounds, and a judge (or consensus) decides. There is evidence that it helps factuality and that a weaker judge can pick the truthful side. Majority conformity and cost are real problems. **Assess**: adopt only "rebuttal-lite", one round where a defender answers each critique with draft spans or registry facts and a fresh adjudicator rules.

## What it is

- **Consensus debate**: multiple instances propose answers, read each other's, and revise over rounds toward agreement. This improved reasoning and factual validity over single-model baselines ([arXiv 2305.14325](https://arxiv.org/abs/2305.14325)).
- **Adversarial debate for oversight**: two expert debaters argue opposite answers and a non-expert judge chooses. Judges reached 76% (model) and 88% (human) accuracy versus 48% and 60% baselines, and more persuasive debaters *helped* truthfulness ([arXiv 2402.06782](https://arxiv.org/abs/2402.06782)).
- **Caveats**: in controlled logic puzzles, "majority pressure suppresses independent correction". Reasoning strength and diversity of agents mattered more than debate structure ([arXiv 2511.07784](https://arxiv.org/abs/2511.07784)).

## Why it matters for gentext

The skeptic in the [adversarial pass](adversarial-review-pass.md) produces false positives: nit-picks, and objections already answered elsewhere in the draft. Some adjudication is needed, or writers drown. The Khan et al. set-up maps well: the debaters have evidence (the draft and registry), and the judge only has to check whether cited evidence supports the claim.

## How it would fit ("rebuttal-lite")

1. Skeptic finding F: `{quote, rubric_ref, category, rationale}`.
2. Defender reply: `{concede | contest, evidence: [sentence_id | fact_id], argument ≤ 60 words}`. It may not introduce new text.
3. Adjudicator (fresh context; sees F, the reply, and the cited evidence only): `{upheld | rejected | partial, reason}`.
4. Deterministic validation checks that every cited sentence or fact id exists.

This keeps debate *evidence-bound* and one round deep, so the transcript stays short enough for a human to audit.

## Strengths

- Prunes weak critiques, which keeps the signal-to-noise acceptable for writers.
- Each ruling has a short, inspectable rationale tied to evidence ids.
- Structurally resists "the critic said so" authority.

## Weaknesses / risks

- All agents are one model family, so debate diversity is low, and the diversity finding in [arXiv 2511.07784](https://arxiv.org/abs/2511.07784) suggests that limits the gains.
- Conformity: multi-round, consensus-style debate converges on the majority whether or not it is right. Avoid it.
- A persuasive defender can talk the adjudicator out of real gaps. Mitigate by letting only *evidence ids* count, not rhetoric, and by auditing rejected findings on the gold set.
- Cost grows with rounds and agents.

## Verdict rationale

Full multi-round debate is **assess**: interesting, but not worth the complexity or opacity for 250-word answers. The one-round, evidence-bound rebuttal is part of the recommended pipeline and is measured in calibration (rejected-but-human-upheld rate).

Parent: [LLM evaluation](index.md)
