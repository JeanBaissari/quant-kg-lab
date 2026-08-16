---
name: riskfolio-risk-measures
description: "Use when working with Riskfolio-Lib risk measures and risk contribution\
  \ \u2014 Sharpe_Risk, Risk_Contribution, CVaR/CDaR/MAD/LPM families, and matrix\
  \ helpers."
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
- risk-measures
- tails
related_skills:
- riskfolio
- riskfolio-portfolio
- scipy-stats
target_version: '7.3.0 (dev: after 7.3.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `riskfolio` ahead of the latest PyPI release (7.3.0 (dev: after 7.3.0)). Some APIs may not exist in your installed version.

# riskfolio.risk_measures

Risk analytics surface: portfolio risk measures (MV, CVaR, CDaR, EVaR, MAD,
LPM), risk contribution decomposition, and the matrix estimators
(duplication/commutation, covariance/coskewness families).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `RiskFunctions.py:L1` | `src/RiskFunctions.py:L1` | Risk-measure implementations used by the optimizer |
| `Sharpe_Risk()` | `src/RiskFunctions.py:L2025` | Sharpe-based risk/objective calculator |
| `Risk_Margin()` | `src/RiskFunctions.py:L2688` | Marginal risk per asset |
| `Risk_Contribution()` | `src/RiskFunctions.py:L2426` | Per-asset risk contribution decomposition |
| `CVaR_Hist()` | `src/RiskFunctions.py:L356` | Historical CVaR estimator |
| `LPM()` | `src/RiskFunctions.py:L438` | Lower partial moment risk |
| `MAD()` / `SemiDeviation()` | `src/RiskFunctions.py:L71` | Mean-absolute-deviation and semi-deviation risks |
| `cppfunctions.py:L1` | `external/cppfunctions.py:L1` | Python wrappers for the C++ matrix kernels (duplication, commutation, covariance families) |
| `semi_covariance_matrix()` | `external/cppfunctions.py:L148` | Downside covariance kernel |
| `coskewness_matrix()` | `external/cppfunctions.py:L193` | Third-moment matrix — skew-aware optimization |
| `cokurtosis_matrix()` | `external/cppfunctions.py:L283` | Fourth-moment matrix — tail-aware optimization |

## Common Patterns

- **Risk decomposition**: `Risk_Contribution(w, cov)` — per-asset contribution to total
  risk; the input to risk-parity work.
- **Tail measures**: `CVaR_Hist(returns, alpha)` — historical CVaR; combine with
  `rm='CVaR'` in the optimizer for tail-aware portfolios.
- **Downside-focused**: `SemiDeviation`/`LPM` — penalize only below-target returns;
  match to the strategy's return objective.
- **Higher moments**: `coskewness_matrix` / `cokurtosis_matrix` — feed `rm='SKEW'` /
  `rm='KURT'` models for non-Gaussian universes.
- **Risk-budget report**: combine `Risk_Contribution` + `Risk_Margin` per asset into a
  table — where the risk actually lives before rebalancing.
- **Cross-measure validation**: compute MV, CVaR, and MAD on the same portfolio and compare
  orderings — tail-focused measures rank assets differently than variance.

## Pitfalls

- **C++ kernels**: the fast matrix functions live in the excluded C++ bindings —
  `external/cppfunctions.py:L1` is the Python API surface.
- **Sample size**: coskewness/cokurtosis estimators need long histories; short samples
  produce unstable matrices.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] `Risk_Contribution(w, cov)` decomposes to ~sum(w)
