---
name: empyrical-perf-attrib
description: "Use when decomposing portfolio performance into factor exposures — perf_attrib and compute_exposures for factor-model attribution of returns."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: Quantopian/empyrical
source_commit: 40f61b4f229df10898d46d08f7b1bdc543c0f99c
extraction_date: 2026-08-13
graph:
  nodes: 180
  edges: 258
  community_count: 23
  graph_hash: ce35d5e4b0a5c431
tags:
- empyrical
- perf-attrib
- factor-model
- attribution
related_skills:
- empyrical
- empyrical-stats
- pyfolio-tearsheets
- statsmodels-core
- pandas-core
---

# empyrical.perf_attrib

Factor-model performance attribution: decompose portfolio returns into factor
contributions + residual (alpha), the engine behind pyfolio's
`create_perf_attrib_tear_sheet`.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `perf_attrib()` | `perf_attrib.py:L5` | Decompose returns into factor + residual components over the sample |
| `compute_exposures()` | `perf_attrib.py:L120` | Portfolio exposure to each factor per period (from position weights) |
| `perf_attrib.py` | `perf_attrib.py:L1` | Module: returns, factor returns, exposures → attribution |
| `stats.py` | `stats.py:L1` | Metric primitives used by the attribution layer |

## Common Patterns

- **Attribution pipeline**:
  ```python
  from empyrical import perf_attrib
  res = perf_attrib(returns, factor_returns, factor_loadings)
  # res: factor_returns (per-factor contribution), residual_returns
  ```
- **Exposure computation**: `compute_exposures(positions, factor_loadings)` — position
  weights × factor loadings per period, the input side of the attribution.
- **pyfolio integration**: feed the attribution result into
  `pyfolio.create_perf_attrib_tear_sheet` for the visual decomposition.
- **Diagnostic**: residual returns should be roughly white — persistent residual
  autocorrelation means a missing factor.

## Pitfalls

- **Factor alignment**: returns and factor series must be same-frequency and
  aligned — empyrical uses the aligned window; mismatched calendars silently drop
  observations.
- **Loading convention**: factor_loadings orientation (period × factor vs asset ×
  factor) must match the positions layout — flip before calling.
- **Residual ≠ skill**: positive residual alpha in-sample is expected; only stable
  out-of-sample residual returns support a real edge.

## Provenance

Graph: `knowledge_graphs/empyrical/.graphify/graph.json` — 180 nodes · 258 edges ·
23 communities · graphify @ 40f61b4f229d, backend opencode, description coverage 93.3%.

## Verification Checklist

- [ ] `perf_attrib(returns, factor_returns, loadings)` runs on synthetic data
- [ ] QR rows cite `perf_attrib.py:L*` resolvable in the empyrical graph
