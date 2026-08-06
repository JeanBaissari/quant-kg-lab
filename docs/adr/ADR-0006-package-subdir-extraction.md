# ADR-0006: Package-subdir from-scratch re-extraction

**Type**: ADR
**ADR**: ADR-0006
**Status**: accepted
**Date**: 2026-08-06
**Last Verified**: 2026-08-06

## Context

The committed graphs were extracted once, months earlier, from **whole upstream repos** — dragging
in tests, benchmarks, R/JVM packages, and docs. graphify also hard-errors on non-code corpus files
without a backend, and the graphs were only 2/10 semantically described.

## Decision

Re-extract every library **from scratch** at its pinned commit, targeting the **importable package
subdir** (e.g. `numpy/`, `python-package/xgboost/`, `talib/`) with the ADR-0002 noise excludes plus
non-code excludes (`*.pyf/*.f/*.h/*.rst/*.csv/…`). Codified in `scripts/rebuild_graph.sh` and
`graphs.lock` (pinned commits). Semantic **descriptions** are a separate, deferred pass (ADR-0003).

## Consequences

- 10 clean graphs, ~55K nodes total (vs ~133K noisy); god nodes are real API.
- `graphs.lock` node/edge counts and skill-frontmatter graph stats updated to the fresh graphs.
- The old sklearn/optuna descriptions are dropped; all 10 will be described uniformly in the bulk pass.

## Alternatives considered

- Post-hoc pruning of the old graphs — kept the stale edges/clustering; rejected for a true from-scratch rebuild.
- Whole-repo extraction with heavier excludes — still noisier than package-subdir targeting.

*Last verified against the repo: 2026-08-06.*
