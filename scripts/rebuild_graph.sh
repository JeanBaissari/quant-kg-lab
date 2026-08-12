#!/usr/bin/env bash
#
# rebuild_graph.sh — reproducibly re-extract one library's knowledge graph FROM SCRATCH.
#
# Verified working pipeline (graphify 0.17.1, github.com/rhanka/graphify):
#   code extraction is a LOCAL tree-sitter AST pass + Louvain clustering — NO LLM,
#   NO API key, NO credits. Node descriptions use graphify's assistant mode, which
#   emits batch prompt files an assistant (Claude Code) answers — still no API key.
#
# Usage:   scripts/rebuild_graph.sh <library>
# Example: scripts/rebuild_graph.sh pandas
#
# Requirements:
#   - graphify CLI. If `graphify` is on PATH it is used; otherwise set GRAPHIFY_CLI
#     to the path of dist/cli.js. Install cleanly (the plain `npm i -g` can leave a
#     broken package if $HOME already has a node_modules — install isolated):
#        d=$(mktemp -d); (cd "$d" && npm init -y >/dev/null && \
#           npm i @sentropic/graphify@0.17.1 --no-audit --no-fund)
#        export GRAPHIFY_CLI="$d/node_modules/@sentropic/graphify/dist/cli.js"
#   - network access to clone upstream (github reachable).
#
set -euo pipefail

LIB="${1:-}"
[[ -z "$LIB" ]] && { echo "usage: scripts/rebuild_graph.sh <library>" >&2; exit 2; }

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK="$REPO_ROOT/graphs.lock"
KG="$REPO_ROOT/knowledge_graphs/$LIB"
SRC="$KG/repo"

# graphify invocation: prefer PATH binary, else GRAPHIFY_CLI (node dist/cli.js)
if command -v graphify >/dev/null 2>&1; then GFY=(graphify)
elif [[ -n "${GRAPHIFY_CLI:-}" && -f "${GRAPHIFY_CLI}" ]]; then GFY=(node "$GRAPHIFY_CLI")
else echo "ERROR: graphify not found. Set GRAPHIFY_CLI to dist/cli.js (see header)." >&2; exit 1; fi

# The importable package subdir inside each upstream repo (the real API surface —
# extracting the whole repo drags in tests/benchmarks/docs and errors on non-code).
pkg_subdir() { case "$1" in
  scikit-learn) echo sklearn;; ta-lib) echo talib;;
  xgboost) echo python-package/xgboost;; lightgbm) echo python-package/lightgbm;;
  *) echo "$1";; esac; }

read -r REPO COMMIT < <(python3 - "$LOCK" "$LIB" <<'PY'
import json,sys
d=json.load(open(sys.argv[1]))["libraries"]; lib=sys.argv[2]
if lib not in d: sys.stderr.write("unknown lib\n"); sys.exit(1)
print(d[lib]["repo"], d[lib]["commit"])
PY
)

# 1. clone upstream at the pinned commit
if [[ ! -d "$SRC/.git" ]]; then
  echo ">> cloning $REPO"
  git clone --quiet --filter=blob:none "https://github.com/$REPO" "$SRC"
fi
git -C "$SRC" fetch --quiet --depth 1 origin "$COMMIT" 2>/dev/null || git -C "$SRC" fetch --quiet origin
git -C "$SRC" checkout --quiet "$COMMIT"
PKG="$SRC/$(pkg_subdir "$LIB")"
echo ">> extracting $LIB from $PKG @ ${COMMIT:0:12}"

# 2. LOCAL AST + Louvain extraction (no LLM). Exclude tests/benchmarks + non-code.
#    NOTE (QKG_018 F1/F2): graphify's glob excludes are root-anchored, so also pass
#    the segment form 'tests/' (matches nested test dirs — statsmodels F1) and
#    corpus-extension excludes ('.m'/'.txt'/'.html' etc. hard-abort without a
#    semantic backend — statsmodels F2).
WS="$KG/.graphify"; mkdir -p "$WS"
"${GFY[@]}" extract "$PKG" --out "$KG" --no-description --no-label \
  --exclude 'tests/**' --exclude 'tests/' --exclude 'test_*' --exclude '*_test.py' \
  --exclude 'benchmarks/**' --exclude 'asv_bench/**' --exclude 'examples/**' \
  --exclude 'samples/**' --exclude 'docs/**' --exclude 'doc/' \
  --exclude '*.pyx' --exclude '*.pxi' --exclude '*.pxd' --exclude '*.pyi' --exclude '*.typed' \
  --exclude '*.m' --exclude '*.mat' --exclude '*.do' --exclude '*.R' --exclude '*.f90' \
  --exclude '*.txt' --exclude '*.html'

# 3. Descriptions + labels via assistant mode (emits batch prompts; NO API key).
#    An assistant (Claude Code) fills each .graphify/description-instructions/batch-NNN.json,
#    then re-run `graphify describe` to ingest. Same flow for `graphify label`.
echo ">> emitting description batches (assistant mode — answer them, then re-run describe to ingest)"
"${GFY[@]}" describe "$KG" || true

cat <<DONE

>> structural graph written: $WS/graph.json
>> NEXT: answer .graphify/description-instructions/batch-*.json (assistant mode, no API key),
   then: ${GFY[*]} describe "$KG"   # ingests → real descriptions
   Verify against the Quality Gate in docs/GRAPH_SPEC.md §5.
DONE
