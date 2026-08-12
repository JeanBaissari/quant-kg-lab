#!/bin/bash
# quant-kg-lab setup — verify prerequisites and install dependencies.
# It deliberately does NOT clone anything: per-library clones/rebuilds are
# pin-based via scripts/rebuild_graph.sh <lib> (commit from graphs.lock).
set -euo pipefail

usage() {
    cat <<'EOF'
quant-kg-lab setup — prerequisites + dependencies (no cloning)

Usage: scripts/setup.sh [--help]

Steps:
  1. verify python3 is available
  2. run scripts/install_graphify.sh if present (else print the npm instruction)
  3. pip install -r requirements.txt
  4. print per-library rebuild instructions (scripts/rebuild_graph.sh <lib>)

Library clones/rebuilds are NOT done here: each library is rebuilt from the
commit pinned in graphs.lock via scripts/rebuild_graph.sh <lib>.
EOF
}

if [ "$#" -gt 0 ]; then
    case "$1" in
        --help|-h|help) usage; exit 0 ;;
        *) echo "ERROR: unknown argument: $1" >&2; usage; exit 1 ;;
    esac
fi

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== quant-kg-lab setup ==="

# 1. python3
if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 required but not found on PATH" >&2
    exit 1
fi
echo "[1/4] python3: $(python3 --version)"

# 2. graphify CLI (external, npm)
if [ -f "scripts/install_graphify.sh" ]; then
    echo "[2/4] running scripts/install_graphify.sh"
    bash scripts/install_graphify.sh
else
    echo "[2/4] scripts/install_graphify.sh not present — install the graphify CLI manually:"
    echo "      npm install -g @sentropic/graphify"
fi

# 3. Python dependencies (target libraries for skill validation)
echo "[3/4] python3 -m pip install -r requirements.txt"
echo "      (TA-Lib first needs its C library: apt install ta-lib / brew install ta-lib)"
python3 -m pip install -r requirements.txt

# 4. Pin-based rebuild instructions (graphs.lock, not branch clones)
echo "[4/4] rebuild each library's knowledge graph from its pinned commit:"
python3 - <<'PY'
import json
libraries = json.load(open("graphs.lock"))["libraries"]
for lib in libraries:
    commit = libraries[lib].get("commit", "?")[:12]
    print(f"      scripts/rebuild_graph.sh {lib}   # {commit}")
PY

echo ""
echo "=== setup complete ==="
echo "Next: scripts/rebuild_graph.sh <lib> — pins live in graphs.lock"
