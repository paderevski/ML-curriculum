#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

python3 scripts/export_notebooks.py
python3 scripts/generate_notebook_metadata.py

bundle exec jekyll serve --config _config.yml,_config.local.yml "$@" 2> >(awk '
	/^To use retry middleware with Faraday v2\.0\+, install `faraday-retry` gem$/ { next }
	/^Deprecation Warning \[import\]: Sass @import rules are deprecated/ { suppress=1; next }
	suppress && /root stylesheet$/ { suppress=0; next }
	suppress { next }
	{ print }
' >&2)