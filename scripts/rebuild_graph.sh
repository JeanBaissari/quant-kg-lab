#!/usr/bin/env bash
#
# rebuild_graph.sh — reproducibly rebuild one library's knowledge graph.
#
# Usage:   scripts/rebuild_graph.sh <library>
# Example: scripts/rebuild_graph.sh pandas
#
# Reads the pinned upstream commit from /graphs.lock, clones the source at that
# commit, runs the graphify pipeline with the noise filter from docs/GRAPH_SPEC.md,
# and regenerates graph.json + GRAPH_REPORT.md + labels + edge audit.
#
# Requirements (this cannot run in a network-less sandbox):
#   - graphify CLI:  npm install -g @sentropic/graphify
#   - network access to clone the upstream repo
#   - the claude-cli backend available to graphify (for real descriptions)
#
set -euo pipefail

LIB="${1:-}"
if [[ -z "$LIB" ]]; then
  echo "usage: scripts/rebuild_graph.sh <library>" >&2
  exit 2
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK="$REPO_ROOT/graphs.lock"
KG_DIR="$REPO_ROOT/knowledge_graphs/$LIB"
GRAPHIFY_DIR="$KG_DIR/.graphify"
SRC_DIR="$KG_DIR/repo"

# --- Preconditions -----------------------------------------------------------
command -v graphify >/dev/null 2>&1 || {
  echo "ERROR: graphify not found. Install with: npm install -g @sentropic/graphify" >&2
  exit 1
}
[[ -f "$LOCK" ]] || { echo "ERROR: missing $LOCK" >&2; exit 1; }

# --- Resolve repo + commit from graphs.lock (stdlib python, no jq needed) -----
read -r REPO COMMIT < <(python3 - "$LOCK" "$LIB" <<'PY'
import json, sys
lock, lib = sys.argv[1], sys.argv[2]
data = json.load(open(lock))["libraries"]
if lib not in data:
    sys.stderr.write(f"ERROR: '{lib}' not in graphs.lock. Known: {', '.join(sorted(data))}\n"); sys.exit(1)
print(data[lib]["repo"], data[lib]["commit"])
PY
)
echo ">> $LIB  repo=$REPO  commit=$COMMIT"

# --- Clone (or update) upstream at the pinned commit -------------------------
mkdir -p "$KG_DIR"
if [[ ! -d "$SRC_DIR/.git" ]]; then
  echo ">> cloning https://github.com/$REPO into $SRC_DIR"
  git clone --filter=blob:none "https://github.com/$REPO" "$SRC_DIR"
fi
git -C "$SRC_DIR" fetch --depth 1 origin "$COMMIT" || git -C "$SRC_DIR" fetch origin
git -C "$SRC_DIR" checkout --quiet "$COMMIT"
echo ">> checked out $(git -C "$SRC_DIR" rev-parse --short HEAD)"

# --- Noise filter (docs/GRAPH_SPEC.md §6) ------------------------------------
# graphify reads .graphifyignore for path excludes. Symbol-level excludes
# (__Pyx_*, *JNI*, raw TA_* C entry points) are pruned in a post-pass; see
# GRAPH_SPEC §6 for the ta-lib exception.
cat > "$SRC_DIR/.graphifyignore" <<'IGNORE'
tests/
test_*
*_test.py
conftest.py
asv_bench/
benchmarks/
bench/
doc/
docs/
examples/
.github/
setup.py
versioneer*
_vendor/
third_party/
vendored/
IGNORE

# --- Extract → merge descriptions → cluster → audit --------------------------
pushd "$SRC_DIR" >/dev/null
echo ">> graphify extract (backend=claude-cli)"
graphify extract --backend claude-cli
echo ">> merging descriptions"
python3 "$REPO_ROOT/scripts/merge_descriptions.py" "$LIB" || true
echo ">> graphify cluster-only"
graphify cluster-only .
popd >/dev/null

# graphify writes into $SRC_DIR/.graphify — publish the three committed artifacts up one level.
mkdir -p "$GRAPHIFY_DIR"
for f in graph.json GRAPH_REPORT.md .graphify_labels.json; do
  [[ -f "$SRC_DIR/.graphify/$f" ]] && cp "$SRC_DIR/.graphify/$f" "$GRAPHIFY_DIR/$f"
done

echo ">> edge audit"
python3 "$REPO_ROOT/scripts/audit_edges.py" "$LIB" || true

# --- Quality-gate reminder (docs/GRAPH_SPEC.md §5) ---------------------------
cat <<GATE

── Verify against the Quality Gate (docs/GRAPH_SPEC.md §5) before committing ──
  [ ] real community labels (no "Community N", no {"None":"Tests"})
  [ ] >=80% of retained public-API code nodes have SEMANTIC descriptions (not AST stubs)
  [ ] top-20 god nodes contain no test/benchmark/__Pyx_*/JNI symbols
  [ ] built_from_commit == $COMMIT (matches graphs.lock)
  [ ] docs/edge-audit-$LIB.md regenerated
GATE
echo ">> done: $GRAPHIFY_DIR"
