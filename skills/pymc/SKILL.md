---
name: pymc
description: "Use when working with pymc \u2014 the Bayesian-modelling entry point.\
  \ Router indexing the pymc sub-skills; load the sub-skill for the modelling stage\
  \ you need."
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
  graph_hash: abe838c4f6662d33
tags:
- pymc
- router
- bayesian
- probabilistic
related_skills:
- pymc-model
- pymc-sampling
- pymc-distributions
- numpy-core
- statsmodels-tsa
- quant-volatility-modelling
target_version: '6.3.0 (dev: after 6.3.0, before 6.3.1)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `pymc` ahead of the latest PyPI release (6.3.0 (dev: after 6.3.0, before 6.3.1)). Some APIs may not exist in your installed version.

# pymc

Probabilistic programming / Bayesian modelling: declare a `Model` with priors + likelihood,
sample the posterior (NUTS/HMC), and forecast via posterior predictive draws — the
uncertainty-quantification layer of the stack.

## Sub-skills

| Skill | Scope |
|-------|-------|
| [model](model/SKILL.md) | Model container, modelcontext, deterministic/observed variables |
| [sampling](sampling/SKILL.md) | sample/sample_posterior_predictive/prior predictive, NUTS tuning, arviz |
| [distributions](distributions/SKILL.md) | continuous/discrete/multivariate/timeseries priors, transforms |

## Common Patterns

- **Quant usage**: Bayesian volatility (GARCH11/AR priors), regime detection with
  mixture priors, parameter uncertainty in portfolio models.
- **Model → sample → predict**: `with pm.Model(): ...` → `pm.sample()` →
  `pm.sample_posterior_predictive()`.
- **Diagnostics**: `az.summary(trace)` — rhat < 1.01, ess > 400 per parameter.

## Provenance

Graph: `knowledge_graphs/pymc/.graphify/graph.json` — 4067 nodes · 11144 edges ·
135 communities · graphify @ 47bdf54a27a4, backend opencode, description coverage 82.9%,
8 curated M2b entries (ADR-0008).

## Verification Checklist

- [ ] Router links resolve to the 3 module skills
- [ ] `related_skills` names resolve to real skills
