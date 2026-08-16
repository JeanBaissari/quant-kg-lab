---
name: statsmodels-glm
description: "Use when fitting generalized linear models with statsmodels \u2014 GLM\
  \ families/links/varfuncs, GEE with covariance structures, GLMGam, robust covariance\
  \ (HC0\u2013HC3/cluster), and Tweedie models."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: statsmodels/statsmodels
source_commit: 179d1f4df4164c94c69256fc9436d578a1beb163
extraction_date: 2026-08-12
graph:
  nodes: 11616
  edges: 33529
  community_count: 638
  graph_hash: 22b3083cca514704
tags:
- statsmodels
- glm
- gee
- families
- robust-covariance
related_skills:
- statsmodels
- statsmodels-core
- statsmodels-diagnostics
- scikit-learn-linear-model
- pandas-core
---

# statsmodels.genmod

Generalized linear models: `GLM` with the family/link/varfunc triad (Gaussian,
Poisson, Binomial, Gamma, NegativeBinomial, Tweedie), `GEE` for clustered/correlated
data with covariance structures, `GLMGam` for additive terms, and robust covariance
for valid inference under heteroskedasticity.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `GLM` | `genmod/generalized_linear_model.py:L66` | GLM model — family + link via the formula or arrays API |
| `GLMResults` | `genmod/generalized_linear_model.py:L1750` | Fitted GLM — params, bse, pvalues, conf_int, summary |
| `Family` | `genmod/families/family.py:L24` | Distribution family base — deviance, resid_dev, loglike |
| `Poisson` | `genmod/families/family.py:L379` | Count family — log link default |
| `Binomial` | `genmod/families/family.py` | Binary family — logit/probit/cloglog links |
| `Gamma` | `genmod/families/family.py` | Positive-skew family — inverse link default |
| `NegativeBinomial` | `genmod/families/family.py` | Overdispersed count family |
| `Tweedie` | `genmod/families/family.py` | Power-variance family — p in (1, 2) |
| `Link` | `genmod/families/links.py:L23` | Link-function base — identity, log, logit, inverse_power |
| `GEE` | `genmod/generalized_estimating_equations.py:L488` | Generalized estimating equations — clustered/correlated data |
| `GEEResults` | `genmod/generalized_estimating_equations.py:L1885` | GEE fit results |
| `NominalGEE` | `genmod/generalized_estimating_equations.py:L2797` | Nominal-category GEE |
| `OrdinalGEE` | `genmod/generalized_estimating_equations.py:L2467` | Ordinal-category GEE |
| `CovStruct` | `genmod/cov_struct.py:L29` | Working covariance structure base |
| `Stationary` | `genmod/cov_struct.py:L596` | Stationary autocorrelation structure |
| `GLMGam` | `gam/generalized_additive_model.py` | GAM — smooth additive terms |
| `GLMInfluence` | `stats/outliers_influence.py:L1456` | Influence/diagnostics for GLM fits |

## Common Patterns

- **GLM fit**:
  ```python
  import statsmodels.api as sm
  model = sm.GLM(y, X, family=sm.families.Poisson())
  res = model.fit(cov_type="HC1")
  res.summary()   # params, z, pvalues, conf_int
  ```
- **Family choice**: Poisson (counts), Binomial (0/1 or proportions), Gamma
  (positive continuous), NegativeBinomial (overdispersed counts), Tweedie
  (compound-Poisson-like losses with mass at zero).
- **Link choice**: logit for probabilities, log for counts/positive, identity for
  continuous — pick per the response's support.
- **Clustered data**: `GEE(y, X, groups=panel_id, cov_struct=sm.cov_struct.Exchangeable())`
  — valid inference when observations are correlated within panels.
- **Robust covariance**: `res = model.fit(cov_type="HC0"|"HC1"|"HC3"|"cluster")` —
  heteroskedasticity-robust standard errors; cluster for within-group correlation.
- **Additive terms**: `GLMGam` with `splines` — smooth nonlinear terms without
  explicit basis construction.

## Pitfalls

- **Family/link mismatch**: e.g. identity link with Poisson can produce negative
  predicted counts — validate predictions against the response support.
- **Overdispersion**: plain Poisson understates standard errors when variance >
  mean — use NegativeBinomial or `GLM(family=NegativeBinomial())`.
- **GEE needs groups**: without `groups=`, GEE is not identified — pass the panel
  identifier explicitly.
- **cov_type consistency**: HC1 (n/(n-k)) is the common default; HC3 is more
  conservative for small samples; pick once and document.
- **Tweedie power**: `var_power` in (1, 2) is the compound-Poisson region — outside
  that the fit is numerically fragile.
- **Formula vs arrays**: `sm.GLM.from_formula(...)` needs a DataFrame with
  `add_constant` handled by the formula — mixing APIs changes the design matrix.

## Provenance

Graph: `knowledge_graphs/statsmodels/.graphify/graph.json` — 11616 nodes · 33529 edges ·
638 communities · graphify @ pin, backend opencode, description coverage 43%.

## Verification Checklist

- [ ] `sm.GLM(y, X, family=sm.families.Poisson()).fit()` runs
- [ ] `GEE(y, X, groups=g, cov_struct=sm.cov_struct.Exchangeable()).fit()` runs
- [ ] QR rows cite `genmod/**` files resolvable in the statsmodels graph
