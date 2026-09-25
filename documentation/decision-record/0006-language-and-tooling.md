# 0006. Python + uv with a repo-local .venv; no system Python packages

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
- The dev machine is **Arch Linux**. System Python (currently 3.14) is marked **externally managed** (PEP 668, `/usr/lib/python3.14/EXTERNALLY-MANAGED`), so `pip install` into it is refused. Arch expects system-wide Python packages to come from pacman (`python-*`).
- Arch is **rolling**. When pacman bumps the system Python minor version, every venv built on `/usr/bin/python` breaks.
- The maintainer uses `uv` and `uv tool install` for global CLIs. That doesn't give a *project* a reproducible environment.
- The sibling `hyphae_ai_skills` repo uses uv. The research picks Python-native tools (spaCy, datasketch, WQRM/transformers, FastMCP).
- The machine has a 16 GB NVIDIA GPU (CUDA in `/opt/cuda`) and podman.

## Decision
1. **The project environment is a repo-local `.venv`, managed only by uv.** `pyproject.toml` + `uv.lock` are committed; `.venv/` is gitignored. `uv sync` rebuilds it. `uv run <cmd>` runs inside it with no activation step, which also suits agents.
2. **The interpreter is uv-managed, pinned in `.python-version` (3.12)**, not the pacman Python. This keeps the venv independent of Arch's Python upgrades. 3.12 has the widest wheel coverage for the ML/NLP stack. Revisit when spaCy/torch wheels are routine for newer versions.
3. **Never** use `pip install --user`, `--break-system-packages`, or pacman `python-*` packages for project dependencies.
4. **Non-Python tools come through Python wheels where possible**, so they're versioned and locked with the project:
   - pandoc via `pypandoc-binary` (verified: bundles pandoc 3.9 inside `.venv`).
   - Vale via the `vale` PyPI wrapper (verified: `uvx --from vale vale --version` → 3.22.0). Add it as a dependency when M7 needs it.
   - LanguageTool, if used, runs as a **podman** container, not a Java install.
5. **Heavy dependencies go in dependency groups**, installed on demand (`uv sync --group nlp`, `--group models`). `nlp` holds spaCy + model wheel, textstat, rapidfuzz, datasketch. `models` holds torch (CUDA index configured in `pyproject.toml`), transformers, sentence-transformers. The base install stays small for Cloud Run (DR-0009).
6. Package `gentext` under `src/`, CLI entry point `gentext`. Tests use `pytest` (`uv run pytest`). The DR-0002 QC defects are the first fixtures.
7. Global, personal CLIs stay with `uv tool install`, and the project never depends on them.

## Consequences
- A fresh clone (laptop, Claude Code on the web, Cloud Run image) needs only `uv` → `uv sync`.
- Disk: each group adds weight (torch + CUDA wheels run to several GB). That's acceptable locally, and the Cloud Run image excludes `models` unless needed.
- Agents must run Python as `uv run python …` / `uv run gentext …`, never bare `python3`. That's recorded in AGENTS.md.

## Alternatives considered
- pacman `python-*` packages: system-wide, not locked, versions set by Arch, and break with Python bumps.
- Conda/mamba: heavier, and redundant with uv.
- A venv on the system interpreter: breaks on Arch Python upgrades.

## Revisions
- 2026-09-25: Rewritten after the maintainer asked how Python packaging should work on Arch. The original proposal just said "Python ≥3.12, uv". Skeleton created: `pyproject.toml`, `.python-version`, `uv.lock`, `src/gentext/`.
