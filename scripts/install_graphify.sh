#!/usr/bin/env bash
#
# install_graphify.sh — isolated npm install of @sentropic/graphify@0.17.1.
#
# Installs into <repo>/.graphify-cli/ (gitignored) and prints the GRAPHIFY_CLI
# export line to stdout:
#     export GRAPHIFY_CLI="<repo>/.graphify-cli/node_modules/@sentropic/graphify/dist/cli.js"
# Idempotent: re-running skips the npm step. Follows the isolated-install recipe
# in scripts/rebuild_graph.sh header (a plain `npm i -g` can leave a broken
# package when $HOME already has a node_modules).
#
# Usage:   eval "$(bash scripts/install_graphify.sh)"
# Example: "$GRAPHIFY_CLI" --version
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLI_DIR="$REPO_ROOT/.graphify-cli"
CLI_JS="$CLI_DIR/node_modules/@sentropic/graphify/dist/cli.js"
VERSION="0.17.1"

if [[ ! -f "$CLI_JS" ]]; then
  mkdir -p "$CLI_DIR"
  if [[ ! -f "$CLI_DIR/package.json" ]]; then
    printf '{"name":"graphify-cli-install","version":"1.0.0","private":true}\n' > "$CLI_DIR/package.json"
  fi
  (cd "$CLI_DIR" && npm i "@sentropic/graphify@$VERSION" --no-audit --no-fund 1>&2)
fi

echo "export GRAPHIFY_CLI=\"$CLI_JS\""
