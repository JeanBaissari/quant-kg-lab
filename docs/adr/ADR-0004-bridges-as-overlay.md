# ADR-0004: Cross-library bridges as a precise overlay graph

**Type**: ADR
**ADR**: ADR-0004
**Status**: accepted
**Date**: 2026-08-06
**Last Verified**: 2026-08-06

## Context

The v1 bridge injector substring-matched labels and "resolved" 28/29 bridges to **noise** —
benchmark files, docstring fragments, Cython trampolines, even the xgboost R package. The bridges
were meaningless and never written as real edges.

## Decision

Resolve each curated bridge to a **clean** node (exact-label, code-only, noise-excluded) and write a
real **cross-library overlay graph** at `knowledge_graphs/_cross_library/.graphify/graph.json`
(`scripts/inject_cross_edges_v2.py --apply`). Endpoints that only exist as Cython/internal nodes are
honestly left unresolved. Retire v1 (`cross-library-bridges.json` + `inject_cross_edges.py`).

## Consequences

- 16/19 bridges resolve to real classes; the overlay is queryable via `query_graph.py _cross_library`.
- `docs/reference/cross-library-bridges.json` and `unified-index.md` reflect real edges.

## Alternatives considered

- Keep reporting-only JSON — rejected: a bridge you cannot traverse is documentation theatre.

*Last verified against the repo: 2026-08-06.*
