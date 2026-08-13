---
name: pymc-sampling
description: "Use when sampling PyMC models \u2014 pm.sample()/sample_posterior_predictive()/sample_prior_predictive(),\
  \ NUTS/HMC step selection and tuning, backends, and arviz diagnostics (rhat/ess/summary)."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pymc-devs/pymc
source_commit: 47bdf54a27a4246498994de700e8d55e99eb2d49
extraction_date: 2026-08-13
graph:
  nodes: 4067
  edges: 11144
  community_count: 156
  graph_hash: f7ea65eb6c16067f
tags:
- pymc
- sampling
- nuts
- mcmc
- diagnostics
related_skills:
- pymc
- pymc-model
- pymc-distributions
- numpy-core
---

# pymc.sampling

The sampling surface: `pm.sample()` runs MCMC (NUTS by default) and returns an
InferenceData trace; `sample_posterior_predictive` / `sample_prior_predictive` draw
data from the posterior/prior; backends persist the trace.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `sample()` | `sampling/mcmc.py` | Run MCMC — draws/tune/chains/cores, step-method auto-assignment |
| `sample_prior_predictive()` | `sampling/forward.py:L485` | Draw from the prior → data (prior predictive check) |
| `sample_posterior_predictive()` | `sampling/forward.py:L607` | Draw new data from the posterior — forecasts/backtests |
| `draw()` | `sampling/forward.py:L397` | Draw from a random variable directly |
| `vectorize_over_posterior()` | `sampling/forward.py:L1337` | Vectorize a function over posterior draws |
| `assign_step_methods()` | `sampling/mcmc.py:L256` | Auto-pick step methods per variable (NUTS for continuous) |
| `instantiate_steppers()` | `sampling/mcmc.py:L183` | Build the step-method stack |
| `get_default_tune_steps()` | `sampling/mcmc.py:L127` | Default tuning length |
| `MultiTrace` | `backends/base.py:L323` | Trace container across chains |
| `NDArray` | `backends/ndarray.py:L27` | In-memory trace backend |
| `dict_to_dataset()` | `backends/arviz.py:L70` | Trace → arviz InferenceData conversion |
| `find_observations()` | `backends/arviz.py:L137` | Locate observed data in the trace for PPC |
| `requires` | `backends/arviz.py:L51` | Arviz import guard/version check |
| `SamplingError` | `exceptions.py:L31` | Sampling failure error |
| `SamplingIteratorCallback` | `sampling/mcmc.py:L144` | Per-iteration callback hook |

## Common Patterns

- **Standard run**:
  ```python
  with m:
      trace = pm.sample(draws=2000, tune=1000, chains=4, cores=4, random_seed=42)
  ```
- **Forecast distribution**:
  ```python
  with m:
      ppc = pm.sample_posterior_predictive(trace)
  ```
  — the Bayesian forecast/backtest distribution (mean + uncertainty band).
- **Prior sanity**: `pm.sample_prior_predictive(500)` BEFORE seeing data — the
  prior-predictive check.
- **Diagnostics**: `az.summary(trace)` — require `r_hat < 1.01`, `ess_bulk > 400`,
  and no divergences.
- **Reproducibility**: always pass `random_seed` — MCMC is stochastic otherwise.
- **Backend persistence**: `pm.sample(..., trace_backend=NDArray)` for in-memory,
  or the zarr backend for long traces.

## Pitfalls

- **Divergences**: `trace.sample_stats["diverging"].sum()` > 0 → the geometry is
  pathological — reparametrize (centered → non-centered), raise tune, or adapt the
  mass matrix.
- **rhat on short chains**: rhat < 1.01 needs enough warmup — tune ≥ 1000 for
  posteriors with strong correlations.
- **PPC ≠ forecast**: posterior predictive draws reuse observed covariates — for true
  out-of-sample forecasting, extend the model's data axis and predict forward.
- **NUTS on discrete vars**: discrete variables get their own step method (Metropolis/
  categorical Gibbs) — mixing slows convergence; marginalize or reparametrize where
  possible.
- **cores vs reproducibility**: parallel chains with `cores>1` need `random_seed` per
  chain to be reproducible — pass a list of seeds.

## Provenance

Graph: `knowledge_graphs/pymc/.graphify/graph.json` — 4067 nodes · 11144 edges ·
135 communities · graphify @ 47bdf54a27a4, backend opencode, description coverage 82.9%.

## Verification Checklist

- [ ] `pm.sample(draws=200, tune=200, chains=2, random_seed=1)` returns an InferenceData
- [ ] `pm.sample_posterior_predictive(trace)` returns predictions
- [ ] `az.summary(trace)` shows rhat/ess columns
- [ ] QR rows cite `sampling/*.py`/`backends/*.py` files resolvable in the pymc graph
