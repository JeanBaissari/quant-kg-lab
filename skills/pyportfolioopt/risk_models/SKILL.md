---
name: pyportfolioopt-risk-models
description: "Use when estimating a covariance/risk model with PyPortfolioOpt \u2014\
  \ sample_cov, shrunk covariance (Ledoit-Wolf), risk_matrix, and matrix repair."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: robertmartin8/PyPortfolioOpt
source_commit: a6638d2e06dae6f444fd022cfd4b3c528902a85b
extraction_date: 2026-08-12
graph:
  nodes: 342
  edges: 522
  community_count: 16
  graph_hash: e238a0e0014fb438
tags:
- pyportfolioopt
- risk
- covariance
related_skills:
- pyportfolioopt
- pyportfolioopt-efficient-frontier
target_version: '1.6.0 (dev: after 1.6.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `pyportfolioopt` ahead of the latest PyPI release (1.6.0 (dev: after 1.6.0)). Some APIs may not exist in your installed version.

# pypfopt.risk_models

Covariance and risk estimation for portfolio optimization: sample covariance,
shrinkage estimators (`CovarianceShrinkage` — Ledoit-Wolf and friends), and
`risk_matrix()` as the dispatch surface.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `risk_matrix()` | `risk_models.py:L116` | Computes a covariance matrix using the specified risk-model method |
| `CovarianceShrinkage` | `risk_models.py:L412` | Estimates a shrunk covariance matrix (Ledoit-Wolf and related methods) |
| `fix_nonpositive_semidefinite()` | `risk_models.py:L57` | Repairs a covariance matrix that is not positive semidefinite |
| `sample_cov()` | `risk_models.py:L172` | Sample covariance of asset returns (annualized) |
| `semicovariance()` | `risk_models.py:L206` | Downside-only covariance — penalizes negative co-movements |
| `exp_cov()` | `risk_models.py:L281` | Exponentially weighted covariance — recent returns weighted more |
| `min_cov_determinant()` | `risk_models.py:L330` | Minimum-covariance-determinant robust estimate |
| `cov_to_corr()` / `corr_to_cov()` | `risk_models.py:L366` | Convert between covariance and correlation matrices |
| `CovarianceShrinkage.shrunk_covariance()` | `risk_models.py:L484` | Shrinkage estimate (default Ledoit-Wolf single-factor) |
| `CovarianceShrinkage.ledoit_wolf()` | `risk_models.py:L509` | Ledoit-Wolf shrinkage to a single-factor target |
| `CovarianceShrinkage.oracle_approximating()` | `risk_models.py:L657` | Oracle-approximating shrinkage — optimal asymptotically |
| `_is_positive_semidefinite()` | `risk_models.py:L33` | PSD check — pre-flight before feeding cvxpy |

## Common Patterns

- **Standard pipeline**: `S = risk_models.risk_matrix(prices)` — the default (sample
  covariance, annualized) is fine for liquid, long-history assets.
- **Shrinkage for noisy estimates**: `CovarianceShrinkage(prices).ledoit_wolf()` — shrinks
  toward a structured target; preferred for many-asset, short-history universes.
- **PSD repair**: `fix_nonpositive_semidefinite(S)` before feeding cvxpy-based optimizers.
- **Downside risk**: `semicovariance(prices)` — covariance of returns below the mean;
  pairs naturally with `EfficientSemivariance`.
- **Recency weighting**: `exp_cov(prices, span=60)` — recent regime weighted more than
  `sample_cov`; use for fast-moving factor books.
- **Correlation views**: `cov_to_corr(S)` for clustering/risk-parity work; `corr_to_cov`
  to rebuild S from a shrunk correlation + diagonal variances.

## Pitfalls

- **NaN prices**: interpolate/forward-fill before `risk_matrix`; NaN rows silently corrupt
  the estimator.
- **Non-PSD covariance**: sample covariance from fewer observations than assets is singular —
  shrink or repair, or the optimizer's solver fails.
- **Annualization**: sample_cov/exp_cov annualize by default — if you feed `frequency`
  wrong, Sharpe/vol estimates in `portfolio_performance` are off by sqrt(252).
- **OAS vs LW**: `oracle_approximating()` is asymptotically optimal but can be unstable on
  very short samples — default to `ledoit_wolf()` unless the universe is long.

## Provenance

Graph: `knowledge_graphs/pyportfolioopt/.graphify/graph.json` — 342 nodes · 512 edges ·
16 communities · graphify @ a6638d2e06da, backend opencode, description coverage 91.3%.

## Verification Checklist

- [ ] `risk_matrix(prices)` returns a symmetric annualized covariance
- [ ] `CovarianceShrinkage(prices).ledoit_wolf()` is PSD on a 20-asset sample
