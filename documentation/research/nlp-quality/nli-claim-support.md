---
title: NLI claim support (SummaC, AlignScore, MiniCheck)
slug: nli-claim-support
level: 3
parent: index.md
related: [embeddings-and-similarity.md, sentence-embeddings.md, bertscore.md]
tags: [nli, factual-consistency, grounding, fact-checking, provenance]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M3, M6, M7]
license: MiniCheck code Apache-2.0, Flan-T5 checkpoint MIT, Bespoke-MiniCheck-7B non-commercial; AlignScore MIT; SummaC Apache-2.0
maturity: emerging
inspectability: medium
sources:
  - title: Liyan06/MiniCheck README (EMNLP 2024)
    url: https://github.com/Liyan06/MiniCheck
    accessed: 2026-09-25
  - title: Tang, Laban & Durrett (2024), MiniCheck, arXiv 2404.10774
    url: https://arxiv.org/abs/2404.10774
    accessed: 2026-09-25
  - title: bespokelabs/Bespoke-MiniCheck-7B model card (non-commercial license)
    url: https://huggingface.co/bespokelabs/Bespoke-MiniCheck-7B
    accessed: 2026-09-25
  - title: lytang/MiniCheck-Flan-T5-Large model (HF license tag MIT)
    url: https://huggingface.co/lytang/MiniCheck-Flan-T5-Large
    accessed: 2026-09-25
  - title: LLM-AggreFact leaderboard
    url: https://llm-aggrefact.github.io/
    accessed: 2026-09-25
  - title: yuh-zha/AlignScore README (MIT; last push 2024-03)
    url: https://github.com/yuh-zha/AlignScore
    accessed: 2026-09-25
  - title: Laban et al. (2022), SummaC, TACL 10:163-177
    url: https://aclanthology.org/2022.tacl-1.10/
    accessed: 2026-09-25
  - title: tingofurro/summac GitHub (Apache-2.0; PyPI 0.0.4, 2023-10)
    url: https://github.com/tingofurro/summac
    accessed: 2026-09-25
---

# NLI claim support (SummaC, AlignScore, MiniCheck)

> **TL;DR** **Trial.** Small fact-checking and NLI models score whether a *sentence* is supported by a *source text*. With gentext's provenance map (sentence → cited chunk/fact), this becomes a narrow, local check: "did adaptation drift from the source?". Start with **MiniCheck-Flan-T5-Large** (770M, MIT checkpoint). Keep numbers and names on deterministic checks, and treat model scores as warnings with evidence.

## What it is

| Tool | Idea | Size / license | Status |
|---|---|---|---|
| **SummaC** (Laban et al., TACL 2022) | Split the document and summary into sentences, run a sentence-level NLI model over pairs, then aggregate. `SummaC_ZS` uses max/mean with no parameters. `SummaC_Conv` learns a histogram convolution (74.4% balanced accuracy on the SummaC benchmark). | code Apache-2.0 | PyPI 0.0.4 (2023). Quiet. |
| **AlignScore** (Zha et al., ACL 2023) | RoBERTa trained on a unified "alignment" objective across 7 task types. Long contexts are split into ~350-token chunks and claims into sentences. The score is the max over chunks, averaged over sentences. | base 125M / large 355M; MIT | Last push 2024-03. Pinned to old PyTorch (1.12.1 noted). |
| **MiniCheck** (Tang, Laban, Durrett, EMNLP 2024) | Fact-checker trained on synthetic hard examples. `MiniCheck(document, sentence) → [0,1]`. The authors say Flan-T5 "reaches GPT-4 performance" on LLM-AggreFact. | RoBERTa/DeBERTa/Flan-T5 (~770M), code Apache-2.0, Flan-T5 checkpoint MIT (HF tag); **Bespoke-MiniCheck-7B is non-commercial** | pip from git. PyPI `minicheck` 0.4.0 (2026-07) exists *(ownership not verified)*. |
| Plain NLI cross-encoders | e.g. `cross-encoder/nli-deberta-v3-base` (Apache-2.0) or `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (MIT), via sentence-transformers | small | Baseline. |

LLM-AggreFact is the shared benchmark and leaderboard for grounded fact-checking. It includes LLM judges (Claude among them), so it allows a cost/accuracy comparison against a Claude-based check.

## Why it matters for gentext

AGENTS.md: *"Any factual claim in generated text must trace to a library chunk or fact."* The provenance map proves a claim was *linked*. It does not prove the adapted sentence still *says what the source says*. M6 adaptation (shortening, re-voicing for Bay Point) is exactly where drift happens, for example "13–20% lower hsCRP" becoming "20% lower", or "planned" becoming "completed".

## How it would fit

- M7 check E4: for each draft sentence with provenance ids, score `support = checker(concat(cited sources), sentence)`. MiniCheck's README says to split multi-sentence claims into sentences.
- Below the threshold → warning "claim may not be supported by <chunk id>", showing both texts.
- Sentences *without* provenance but with checkable content (numbers, named entities) → deterministic L11 error first. Model scoring is secondary.
- Pin the model name and revision in the report. Run on CPU in CI for the 770M models *(latency on our hardware not measured)*.

## Strengths

- A narrow task (claim vs *cited* source) plays to these models' strengths.
- Local, cheap, and reproducible compared with an LLM judge. Outputs are a score plus the evidence pair.

## Weaknesses / risks

- Scores are opaque. NLI models are known to be weak on numeric and negation subtleties *(general literature finding; verify on our eval)*, which is why numbers stay deterministic.
- Research code: AlignScore and SummaC are effectively unmaintained, and their dependency pins conflict with current PyTorch. MiniCheck is the most current.
- The license trap: the strongest checkpoint (Bespoke-7B) is non-commercial. Hyphae is a commercial firm.
- Out-of-domain prose (grant narratives) is unlike the training data. Calibrate on 30–50 pilot sentence/source pairs.

## Verdict rationale

This is the right technique for adaptation drift, and inspectable enough when paired with evidence display. Trial MiniCheck-Flan-T5 on pilot pairs before building on it, and compare it against a Claude judge prompt (another topic).

Parent: [NLP quality checks](index.md)
