---
name: pymc-model
description: "Use when declaring PyMC Bayesian models — Model context, priors/observed/free_rv registries, deterministic nodes, modelcontext, and the data layer (Minibatch, ConstantData)."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pymc-devs/pymc
source_commit: 47bdf54a27a4246498994de700e8d55e99eb2d49
extraction_date: 2026-08-13
graph:
  nodes: 4067
  edges: 11144
  community_count: 135
  graph_hash: f7ea65eb6c16067f
tags:
- pymc
- model
- bayesian
- priors
related_skills:
- pymc
- pymc-sampling
- pymc-distributions
- numpy-core
---

# pymc.model

The model-declaration layer: `pm.Model()` is the context container for priors,
observed/latent variables, and deterministic transforms. Everything else hangs
off the model context.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Model` | `model/core.py` | The Bayesian model container — the `with pm.Model():` context |
| `modelcontext()` | `model/core.py:L131` | Get/set the current model context |
| `ModelManager` | `model/core.py:L102` | Context-stack manager for nested models |
| `BaseModel` | `model/core.py:L362` | Base class with enter/exit + registry hooks |
| `ValueGradFunction` | `model/core.py:L143` | Objective/gradient function wrapper for sampling |
| `MinibatchOp` | `data.py:L92` | Minibatch data node — stochastic subsampling of data |
| `MinibatchRandomVariable` | `variational/minibatch_rv.py:L28` | Random variable over a minibatch |
| `SplineWrapper` | `distributions/dist_math.py:L249` | Spline interpolation helper for priors |
| `PointFunc` | `pytensorf.py:L612` | Pytensor function wrapper around a point |

## Common Patterns

- **The canonical model**:
  ```python
  import pymc as pm
  with pm.Model() as m:
      mu = pm.Normal("mu", mu=0, sigma=1)
      sigma = pm.HalfCauchy("sigma", beta=1)
      obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
  ```
- **Deterministic nodes**: `pm.Deterministic("ret", pm.math.exp(mu))` — track derived
  quantities in the trace without extra parameters.
- **Minibatch for large data**: `pm.Minibatch(y, batch_size=500)` — scalable
  likelihood subsampling.
- **Context discipline**: always use `with pm.Model()` — `modelcontext()` resolves the
  active model for `pm.sample()` and friends.
- **Model reuse**: keep the model handle `m`; re-enter `with m:` to sample or extend.

## Pitfalls

- **Missing context**: creating variables outside `with pm.Model():` raises — the model
  context is mandatory.
- **Registry collisions**: reusing a variable name in the same model raises — name
  variables uniquely (or use `name` suffixes).
- **Minibatch randomness**: MinibatchOp introduces stochasticity — fix the RNG or batch
  order for reproducible priors.
- **Deterministic ≠ free_rv**: deterministics are not sampled parameters — they have no
  prior and no NUTS step.
- **Observed shape**: observed data must match the prior's shape after broadcasting —
  shape errors surface late (at sampling), so check `m.rvs_to_values` early.

## Provenance

Graph: `knowledge_graphs/pymc/.graphify/graph.json` — 4067 nodes · 11144 edges ·
135 communities · graphify @ 47bdf54a27a4, backend opencode, description coverage 82.9%.

## Verification Checklist

- [ ] `with pm.Model(): pm.Normal("x")` registers one free_rv
- [ ] `modelcontext()` returns the active model inside the context
- [ ] QR rows cite `model/core.py`/`data.py` files resolvable in the pymc graph
