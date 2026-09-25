#!/usr/bin/env bash
# Setup script for Claude Code cloud environments (paste into the environment's "Setup script" box,
# or run manually: bash scripts/cloud-setup.sh). Idempotent.
set -euo pipefail

# uv (manages Python 3.12 + the repo-local .venv; DR-0006)
if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

# Optional: poppler's pdftotext gives better PDF text than the pypdf fallback.
if ! command -v pdftotext >/dev/null 2>&1 && command -v apt-get >/dev/null 2>&1; then
  (sudo -n apt-get install -y -qq poppler-utils || apt-get install -y -qq poppler-utils) >/dev/null 2>&1 || \
    echo "poppler-utils not installed; PDF extraction will use pypdf"
fi

cd "$(dirname "$0")/.."
uv sync
uv run pytest -q
echo "adapt-rfp ready. Start at documentation/status.md. No API key here: use the sub-agent backends."
