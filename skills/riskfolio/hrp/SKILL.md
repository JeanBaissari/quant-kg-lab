---
name: riskfolio-hrp
description: "Use when building hierarchical portfolio strategies with Riskfolio-Lib — HCPortfolio, HRP/HERC, DBHT clustering, and codependence measures."
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
---

# riskfolio.hrp

Hierarchical portfolio construction: `HCPortfolio` with HRP/HERC variants,
DBHT clustering, and codependence (correlation) inputs — no covariance
inversion needed, robust to ill-conditioned matrices.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `HCPortfolio` | `src/HCPortfolio.py` | Hierarchical clustering portfolio — HRP/HERC optimization |
| `HCPortfolio.optimization()` | `src/HCPortfolio.py` | Solves the hierarchical portfolio given model/linkage/codependence |
| `DBHT.py` | `src/DBHT.py` | Directed Bubble Hierarchical Tree clustering |
| `PlotFunctions.py` | `src/PlotFunctions.py` | Frontier/cluster plotting helpers |

## Common Patterns

- **HRP**: `port = rp.HCPortfolio(returns=Y); w = port.optimization(model='HRP',
  codependence='pearson', linkage='single')` — the standard no-inversion construction.
- **HERC**: `model='HERC'` with `rm='CVaR'` — hierarchical equal risk contribution.
- **Codependence options**: pearson/spearman/abs_pearson/distance — pick per data
  distribution.

## Pitfalls

- **Codependence vs covariance**: HRP consumes a codependence matrix — don't pass a raw
  covariance without the right flag.
- **Clustering stability**: linkage choice changes allocations; compare 'single' vs 'ward'.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] `HCPortfolio(returns=Y).optimization(model='HRP')` runs on a 20-asset universe
