---
name: riskfolio-hrp
description: "Use when building hierarchical portfolio strategies with Riskfolio-Lib\
  \ \u2014 HCPortfolio, HRP/HERC, DBHT clustering, and codependence measures."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: dcajasn/Riskfolio-Lib
source_commit: 632a9e48fbaf2b9f8e83864a492332364b6ed32c
extraction_date: 2026-08-12
graph:
  nodes: 426
  edges: 599
  community_count: 29
  graph_hash: dc57c0d4aa45a96d
tags:
- riskfolio
- hrp
- hierarchical
related_skills:
- riskfolio
- riskfolio-portfolio
- scipy
target_version: '7.3.0 (dev: after 7.3.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `riskfolio` ahead of the latest PyPI release (7.3.0 (dev: after 7.3.0)). Some APIs may not exist in your installed version.

# riskfolio.hrp

Hierarchical portfolio construction: `HCPortfolio` with HRP/HERC variants,
DBHT clustering, and codependence (correlation) inputs — no covariance
inversion needed, robust to ill-conditioned matrices.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `HCPortfolio` | `src/HCPortfolio.py:L26` | Hierarchical clustering portfolio — HRP/HERC optimization |
| `HCPortfolio.optimization()` | `src/HCPortfolio.py:L760` | Solves the hierarchical portfolio given model/linkage/codependence |
| `HCPortfolio.returns()` | `src/HCPortfolio.py:L110` | Accessor for the returns matrix |
| `HCPortfolio.kappa()` | `src/HCPortfolio.py:L129` | Codependence matrix — pearson/spearman/abs_pearson/distance |
| `HCPortfolio.kappa_g()` | `src/HCPortfolio.py:L149` | Generalised codependence (higher-moment aware) |
| `HCPortfolio.p_em()` | `src/HCPortfolio.py:L169` | Expected-mimicking portfolios per cluster |
| `HCPortfolio.p_esm()` | `src/HCPortfolio.py:L184` | Expected-shortfall-mimicking portfolios per cluster |
| `HCPortfolio._hierarchical_clustering()` | `src/HCPortfolio.py:L341` | Linkage clustering over the codependence matrix |
| `HCPortfolio._recursive_bisection()` | `src/HCPortfolio.py:L414` | Top-down weight bisection (HRP core) |
| `DBHT.py:L1` | `src/DBHT.py:L1` | Directed Bubble Hierarchical Tree clustering |
| `PlotFunctions.py:L1` | `src/PlotFunctions.py:L1` | Frontier/cluster plotting helpers |

## Common Patterns

- **HRP**: `port = rp.HCPortfolio(returns=Y); w = port.optimization(model='HRP',
  codependence='pearson', linkage='single')` — the standard no-inversion construction.
- **HERC**: `model='HERC'` with `rm='CVaR'` — hierarchical equal risk contribution.
- **Codependence options**: pearson/spearman/abs_pearson/distance — pick per data
  distribution.
- **Tail-aware clusters**: `p_esm()` — expected-shortfall-mimicking portfolios per cluster
  when returns are fat-tailed; `p_em()` for the mean-mimicking baseline.
- **Linkage choice**: single/complete/average/ward change the dendrogram structure —
  compare weight stability across linkages before committing.
- **Stability check**: perturb the returns window and re-optimize — HRP weights should
  move less than MV weights under the same perturbation.

## Pitfalls

- **Codependence vs covariance**: HRP consumes a codependence matrix — don't pass a raw
  covariance without the right flag.
- **Clustering stability**: linkage choice changes allocations; compare 'single' vs 'ward'.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] `HCPortfolio(returns=Y).optimization(model='HRP')` runs on a 20-asset universe
