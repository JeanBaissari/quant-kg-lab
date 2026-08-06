# ADR-0002: Graph noise-filter policy

**Type**: ADR
**ADR**: ADR-0002
**Status**: accepted
**Date**: 2026-08-06
**Last Verified**: 2026-08-06

## Context

The original whole-repo extractions ranked extraction noise as top "god nodes" — `__Pyx_AddTraceback`,
`XGBoostJNI`, `Benchmark`, `AxisError`, test files — so queries and bridges pointed at test/benchmark
and binding-internal nodes rather than the public API.

## Decision

Define a **noise-filter policy** ([`docs/specs/GRAPH_SPEC.md`](../specs/GRAPH_SPEC.md) §6): exclude
`tests/`, benchmarks, examples, docs, vendored, and C/JNI binding internals (`__Pyx_*`, `*JNI*`),
with an explicit **ta-lib exception** (its public API *is* the Cython wrapper). Applied at extraction
time via `--exclude` and by targeting the package subdir (see ADR-0006).

## Consequences

- God nodes reflect real public API (`BaseEstimator`, `DataFrame`, `Study`, …).
- Graphs shrank ~2× (e.g. xgboost 7708→1632) with higher signal.
- The description budget dropped accordingly (fewer, higher-value nodes).

## Alternatives considered

- Post-hoc prune of the committed graphs — rejected in favour of clean re-extraction (ADR-0006),
  though the same filter is reused for god-node *display* in generators.

*Last verified against the repo: 2026-08-06.*
