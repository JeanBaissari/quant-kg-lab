---
name: pyportfolioopt-risk-models
description: "Use when estimating a covariance/risk model with PyPortfolioOpt — sample_cov, shrunk covariance (Ledoit-Wolf), risk_matrix, and matrix repair."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: robertmartin8/PyPortfolioOpt
source_commit: a6638d2e06dae6f444fd022cfd4b3c528902a85b
extraction_date: 2026-08-12
graph:
  nodes: 342
  edges: 512
  community_count: 16
  graph_hash: 50f7a3628b7218f1
tags:
- pyportfolioopt
- risk
- covariance
related_skills:
- pyportfolioopt
- pyportfolioopt-efficient-frontier
---

# pypfopt.risk_models

Covariance and risk estimation for portfolio optimization: sample covariance,
shrinkage estimators (`CovarianceShrinkage` — Ledoit-Wolf and friends), and
`risk_matrix()` as the dispatch surface.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `risk_matrix()` | `risk_models.py` | Computes a covariance matrix using the specified risk-model method |
| `CovarianceShrinkage` | `risk_models.py` | Estimates a shrunk covariance matrix (Ledoit-Wolf and related methods) |
| `fix_nonpositive_semidefinite()` | `risk_models.py` | Repairs a covariance matrix that is not positive semidefinite |
| `sample_cov` | `risk_models.py` | Sample covariance of asset returns (annualized) |

## Common Patterns

- **Standard pipeline**: `S = risk_models.risk_matrix(prices)` — the default (sample
  covariance, annualized) is fine for liquid, long-history assets.
- **Shrinkage for noisy estimates**: `CovarianceShrinkage(prices).ledoit_wolf()` — shrinks
  toward a structured target; preferred for many-asset, short-history universes.
- **PSD repair**: `fix_nonpositive_semidefinite(S)` before feeding cvxpy-based optimizers.

## Pitfalls

- **NaN prices**: interpolate/forward-fill before `risk_matrix`; NaN rows silently corrupt
  the estimator.
- **Non-PSD covariance**: sample covariance from fewer observations than assets is singular —
  shrink or repair, or the optimizer's solver fails.

## Provenance

Graph: `knowledge_graphs/pyportfolioopt/.graphify/graph.json` — 342 nodes · 512 edges ·
16 communities · graphify @ a6638d2e06da, backend opencode, description coverage 91.3%.

## Verification Checklist

- [ ] `risk_matrix(prices)` returns a symmetric annualized covariance
- [ ] `CovarianceShrinkage(prices).ledoit_wolf()` is PSD on a 20-asset sample
