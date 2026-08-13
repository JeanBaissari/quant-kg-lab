---
name: riskfolio-risk-measures
description: "Use when working with Riskfolio-Lib risk measures and risk contribution — Sharpe_Risk, Risk_Contribution, CVaR/CDaR/MAD/LPM families, and matrix helpers."
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
---

# riskfolio.risk_measures

Risk analytics surface: portfolio risk measures (MV, CVaR, CDaR, EVaR, MAD,
LPM), risk contribution decomposition, and the matrix estimators
(duplication/commutation, covariance/coskewness families).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `RiskFunctions.py` | `src/RiskFunctions.py` | Risk-measure implementations used by the optimizer |
| `Sharpe_Risk()` | `src/RiskFunctions.py` | Sharpe-based risk/objective calculator |
| `Risk_Margin()` | `src/RiskFunctions.py` | Marginal risk per asset |
| `Risk_Contribution()` | `src/RiskFunctions.py` | Per-asset risk contribution decomposition |
| `CVaR_Hist()` | `src/RiskFunctions.py` | Historical CVaR estimator |
| `LPM()` | `src/RiskFunctions.py` | Lower partial moment risk |
| `MAD()` / `SemiDeviation()` | `src/RiskFunctions.py` | Mean-absolute-deviation and semi-deviation risks |
| `cppfunctions.py` | `external/cppfunctions.py` | Python wrappers for the C++ matrix kernels (duplication, commutation, covariance families) |

## Common Patterns

- **Risk decomposition**: `Risk_Contribution(w, cov)` — which assets drive portfolio risk.
- **Tail-risk comparisons**: CVaR/CDaR vs MV across quantiles when selecting the objective.
- **Higher-moment matrices**: `covariance_matrix`, `coskewness_matrix`,
  `cokurtosis_matrix` from `cppfunctions.py` for 3rd/4th-moment optimizations.

## Pitfalls

- **C++ kernels**: the fast matrix functions live in the excluded C++ bindings —
  `external/cppfunctions.py` is the Python API surface.
- **Sample size**: coskewness/cokurtosis estimators need long histories; short samples
  produce unstable matrices.

## Provenance

Graph: `knowledge_graphs/riskfolio/.graphify/graph.json` — 426 nodes · 599 edges ·
29 communities · graphify @ 632a9e48fbaf, backend opencode.

## Verification Checklist

- [ ] `Risk_Contribution(w, cov)` decomposes to ~sum(w)
