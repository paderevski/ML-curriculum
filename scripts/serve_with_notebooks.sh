#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

python3 scripts/export_notebooks.py
python3 scripts/generate_notebook_metadata.py

bundle exec jekyll serve --config _config.yml,_config.local.yml "$@"
