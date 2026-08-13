---
name: pymc-distributions
description: "Use when choosing PyMC prior distributions \u2014 continuous/discrete/multivariate\
  \ families, timeseries priors (RandomWalk/AR/GARCH11), transforms, and distribution\
  \ registration."
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
- distributions
- priors
- timeseries
related_skills:
- pymc
- pymc-model
- pymc-sampling
- numpy-core
- statsmodels-tsa
- quant-volatility-modelling
---

# pymc.distributions

Prior/likelihood families: continuous (Normal, StudentT, HalfCauchy, LogNormal, Beta,
Gamma...), discrete (Bernoulli, Binomial, Poisson...), multivariate (MvNormal, Dirichlet,
LKJ...), timeseries (RandomWalk, AR, GARCH11), plus transforms and custom-distribution
registration.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Distribution` | `distributions/distribution.py:L465` | Base class — logp/support_point/registration machinery |
| `Continuous` | `distributions/distribution.py:L714` | Base for continuous families |
| `Discrete` | `distributions/distribution.py:L704` | Base for discrete families |
| `Uniform` | `distributions/continuous.py:L249` | Uniform prior — bounded ignorance |
| `Normal` | `distributions/continuous.py` | Gaussian prior — mu/sigma parametrization |
| `HalfCauchy` | `distributions/continuous.py` | Heavy-tailed positive prior — the default for scale params |
| `StudentT` | `distributions/continuous.py` | Fat-tailed prior — nu degrees of freedom |
| `LogNormal` | `distributions/continuous.py` | Positive skewed prior |
| `Beta` | `distributions/continuous.py` | [0,1] prior — proportions, hit rates |
| `Gamma` | `distributions/continuous.py` | Positive prior — rates, variances |
| `Bernoulli` | `distributions/discrete.py` | Binary prior — event probability |
| `Binomial` | `distributions/discrete.py` | Count prior — n trials, p success |
| `Poisson` | `distributions/discrete.py` | Count prior — arrivals |
| `NegativeBinomial` | `distributions/discrete.py` | Overdispersed count prior |
| `MvNormal` | `distributions/multivariate.py` | Multivariate Gaussian — mu/cov |
| `Dirichlet` | `distributions/multivariate.py` | Simplex prior — weight vectors, regime probabilities |
| `LKJCholeskyCov` | `distributions/multivariate.py` | Correlation/covariance prior — LKJ-distributed (curated M2b) |
| `OrderedMultinomial` | `distributions/multivariate.py` | Ordered categorical model (curated M2b) |
| `RandomWalk` | `distributions/timeseries.py:L122` | Gaussian random-walk prior — level/regime drift |
| `PredefinedRandomWalk` | `distributions/timeseries.py:L282` | Random walk with a fixed innovation schedule |
| `GARCH11` | `distributions/timeseries.py` | GARCH(1,1) volatility prior — Bayesian vol modelling |
| `AR` | `distributions/timeseries.py` | Autoregressive prior — lag structure |
| `CustomDist` | `distributions/custom.py` | Custom distribution builder (curated M2b) |
| `Truncated` | `distributions/truncated.py` | Truncated distribution wrapper (curated M2b) |
| `moment()` | `distributions/moments/means.py` | Expected-value computation for a distribution |
| `support_point()` | `distributions/distribution.py` | Representative start point for samplers/optimizers |
| `change_dist_size()` | `distributions/shape_utils.py` | Resize a distribution's shape (curated M2b) |
| `ZeroSumTransform` | `distributions/transforms.py:L644` | Zero-sum constraint transform |

## Common Patterns

- **Quant priors**:
  - Scale params: `pm.HalfCauchy("sigma", beta=1)` — never a flat Normal on sigma.
  - Returns mean: `pm.Normal("mu", mu=0, sigma=0.1)` — tight, prior-regularized.
  - Fat tails: `pm.StudentT("ret", nu=5, mu=mu, sigma=sigma, observed=returns)`.
  - Regime weights: `pm.Dirichlet("w", a=np.ones(k))`.
- **Volatility prior**: `GARCH11("vol", ...)` — Bayesian alternative to arch's
  frequentist fits; posterior covers parameter uncertainty.
- **Regime drift**: `RandomWalk("level", sigma=0.01)` — time-varying level with a
  shrinkage prior on innovation.
- **Custom families**: `pm.CustomDist("x", ...)` for non-builtin likelihoods.
- **Transform discipline**: unbounded samplers operate on transformed space — priors
  with support constraints (HalfCauchy, Beta) get automatic transforms.

## Pitfalls

- **Improper priors**: unbounded flat priors (e.g. `pm.Flat`) on scale parameters
  make sampling diverge — use HalfCauchy/HalfNormal.
- **Posterior sensitivity**: prior tails matter — test with
  `sample_prior_predictive` before fitting.
- **MvNormal covariance**: pass `chol`/`cov` correctly — a non-PSD covariance
  silently corrupts the likelihood.
- **Timeseries priors need ordered data**: RandomWalk/AR assume sequential observations —
  shuffle-free input.
- **Discrete + NUTS**: discrete priors switch sampling to non-NUTS steps — keep the
  discrete surface small or marginalize.
- **Named collisions**: `pm.Normal("x")` twice in one model raises — unique names or
  `name=` suffixing.

## Provenance

Graph: `knowledge_graphs/pymc/.graphify/graph.json` — 4067 nodes · 11144 edges ·
135 communities · graphify @ 47bdf54a27a4, backend opencode, description coverage 82.9%,
8 curated M2b entries (ADR-0008).

## Verification Checklist

- [ ] `pm.Normal("x", mu=0, sigma=1)` / `pm.HalfCauchy("s", beta=1)` register priors
- [ ] `pm.GARCH11` / `pm.RandomWalk` register timeseries priors
- [ ] QR rows cite `distributions/**` files resolvable in the pymc graph
