# ADR-0003: graphify assistant-mode (no-API-key) pipeline

**Type**: ADR
**ADR**: ADR-0003
**Status**: accepted
**Date**: 2026-08-06
**Last Verified**: 2026-08-06

## Context

Re-extraction was believed to require a paid LLM backend ("credits"). Investigation of graphify
(`github.com/rhanka/graphify`) showed otherwise: code extraction is a **local tree-sitter AST +
Louvain** pass (no LLM), and node descriptions run in **assistant mode** — graphify emits
`batch-NNN.md` prompts, the host assistant writes `batch-NNN.json`, and `graphify describe` ingests
them, with **no API key** at any step.

## Decision

Standardize the rebuild on: `graphify extract <pkg> --no-description --no-label --exclude …`
(local, free) then the assistant-mode `describe`/`label` loop. `scripts/rebuild_graph.sh` carries
the working invocation. Full every-node description coverage may instead use a direct backend
(`--backend openai|anthropic`) on the user's own key when bulk speed is wanted.

## Consequences

- Graphs are re-runnable from scratch locally with zero marginal cost.
- Proven end-to-end: ta-lib Python API re-extracted and 10/10 nodes described via the loop.
- Install caveat: `npm i -g` can leave a broken package under `$HOME`; install isolated and use `GRAPHIFY_CLI`.

## Alternatives considered

- Direct paid API backend for everything — deferred to an opt-in bulk path; not required for correctness.

*Last verified against the repo: 2026-08-06.*
