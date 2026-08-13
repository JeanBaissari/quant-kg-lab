---
name: arch-volatility
description: "Use when modelling conditional volatility with arch — ARCH/GARCH/EGARCH fits, conditional_volatility, and forecast()."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: bashtage/arch
source_commit: 704bb70e48372e3ccccdde7da379811657ad0224
extraction_date: 2026-08-12
graph:
  nodes: 1367
  edges: 3900
  community_count: 135
  graph_hash: 5b23bf9efa5ee1d1
tags:
- arch
- volatility
- garch
related_skills:
- arch
- arch-unitroot
- arch-bootstrap
- pandas-core
---

# arch.volatility

ARCH-family conditional volatility modelling: `arch_model()` (or explicit
`GARCH`/`EGARCH`/`GJR`/`ARCH` classes) fits a mean + volatility specification;
the results object exposes `conditional_volatility`, `params`, and `forecast()`.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `ARCHModel` | `univariate/base.py:L177` | Base model class — `arch_model(y)` returns an ARCH-family model; `fit()` runs the optimizer |
| `ARCHModelFixedResult` | `univariate/base.py:L1137` | Results when parameters are fixed rather than estimated |
| `VolatilityProcess` | `univariate/volatility.py:L202` | Base class for ARCH-family volatility processes |
| `GARCH` | `univariate/volatility.py:L970` | GARCH(p,q) volatility process — the workhorse spec |
| `EGARCH` | `univariate/volatility.py:L2536` | Exponential GARCH — asymmetric leverage effects |
| `Distribution` | `univariate/distribution.py:L40` | Base class for residual distributions (Normal, StudentT, SkewStudentT) |

## Common Patterns

- **Standard fit**: `am = arch_model(returns, vol='GARCH', p=1, q=1); res = am.fit(update_freq=0)` —
  `res.params`, `res.conditional_volatility`, `res.aic`.
- **Leverage/EGARCH**: `arch_model(returns, vol='EGARCH')` — asymmetric vol response.
- **Forecast**: `res.forecast(horizon=10)` → `forecast.variance` (annualize: `sqrt(252)`).
- **Model selection**: fit GARCH(1,1) / GARCH(2,2) / EGARCH and compare AIC/BIC.

## Pitfalls

- **Scale**: arch warns on tiny/large scales (DataScaleWarning) — multiply returns by 100
  for stable estimation.
- **Convergence**: `fit()` can stall — pass `disp='off'`, try `update_freq=0`; warnings
  (ConvergenceWarning) mean the optimizer stopped early.
- **Annualization**: `conditional_volatility` is per-period; scale by `sqrt(periods_per_year)`.

## Provenance

Graph: `knowledge_graphs/arch/.graphify/graph.json` — 1367 nodes · 3900 edges ·
135 communities · graphify @ 704bb70e4837, backend opencode, description coverage 94.3%.

## Verification Checklist

- [ ] `arch_model(returns, vol='GARCH').fit(update_freq=0)` runs and forecasts
- [ ] QR rows cite `source_file:line` resolving in the arch graph
