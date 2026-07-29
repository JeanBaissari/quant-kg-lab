#!/bin/bash
# quant-kg-lab setup — clone repos and regenerate knowledge graphs
set -e

echo "=== quant-kg-lab setup ==="

# Check prerequisites
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 required"; exit 1; }
command -v git >/dev/null 2>&1 || { echo "ERROR: git required"; exit 1; }
command -v graphify >/dev/null 2>&1 || { echo "WARN: graphify not found — npm install -g @sentropic/graphify"; }

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "Project root: $PROJECT_ROOT"

# Clone repos if not present
if [ ! -d "knowledge_graphs/scikit-learn/repo" ]; then
    echo "Cloning scikit-learn..."
    git clone --depth 1 --branch main \
        https://github.com/scikit-learn/scikit-learn.git \
        knowledge_graphs/scikit-learn/repo
fi

if [ ! -d "knowledge_graphs/optuna/repo" ]; then
    echo "Cloning optuna..."
    git clone --depth 1 --branch master \
        https://github.com/optuna/optuna.git \
        knowledge_graphs/optuna/repo
fi

# Verify graph artifacts
echo ""
echo "=== Verification ==="
for lib in scikit-learn optuna; do
    graph="knowledge_graphs/$lib/.graphify/graph.json"
    if [ -f "$graph" ]; then
        size=$(du -sh "$graph" | cut -f1)
        nodes=$(python3 -c "import json; g=json.load(open('$graph')); print(len(g.get('nodes',[])))")
        echo "  $lib: $nodes nodes ($size)"
    else
        echo "  $lib: MISSING — run extraction first"
    fi
done

echo ""
echo "Skills: $(find skills -name 'SKILL.md' | wc -l)"
echo "Scripts: $(ls scripts/*.py 2>/dev/null | wc -l)"
echo ""
echo "=== Setup complete ==="
echo "Next: python scripts/query_graph.py sklearn 'BaseEstimator'"
