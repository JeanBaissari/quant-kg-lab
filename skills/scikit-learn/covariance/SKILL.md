---
name: scikit-learn-covariance
description: "Use when estimating return covariance for portfolio risk \u2014 empirical,\
  \ shrunk (Ledoit-Wolf), and robust (MCD) estimators in sklearn.covariance."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-08-06
graph:
  nodes: 8450
  edges: 28094
  community_count: 367
  graph_hash: 75a69cbf83913826
tags:
- scikit-learn
- machine-learning
- covariance
- risk-modeling
- portfolio
- shrinkage
related_skills:
- scikit-learn-decomposition
- scikit-learn-preprocessing
target_version: '1.9.0 (dev: after 1.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scikit-learn` ahead of the latest PyPI release (1.9.0 (dev: after 1.9.0)). Some APIs may not exist in your installed version.

# scikit-learn Covariance (`sklearn.covariance`)

Covariance estimators for risk modeling: `EmpiricalCovariance` (sample covariance),
`LedoitWolf`/`ShrunkCovariance` (shrinkage toward a structured target for small samples),
`MinCovDet` (robust MCD estimator for contaminated return series), and `GraphicalLasso`
(sparse precision for factor-graph structure). Reach for it when portfolio volatility,
correlation structure, or outlier-aware risk matters.

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `EmpiricalCovariance` | `covariance/_empirical_covariance.py:L132` | Unbiased sample covariance | `store_precision`, `assume_centered` |
| `ShrunkCovariance` | `covariance/_shrunk_covariance.py:L168` | Shrink sample covariance toward identity/target | `shrinkage` (0..1) |
| `LedoitWolf` | `covariance/_shrunk_covariance.py:L486` | Analytically optimal shrinkage intensity | `store_precision`, `assume_centered`, `block_size` |
| `MinCovDet` | `covariance/_robust_covariance.py:L621` | Robust covariance via minimum determinant (MCD) | `support_fraction`, `random_state`, `assume_centered` |
| `EllipticEnvelope` | `covariance/_elliptic_envelope.py:L15` | Outlier detection from robust covariance | `contamination`, `random_state`, `support_fraction` |
| `GraphicalLasso` | `covariance/_graph_lasso.py:L399` | Sparse precision (inverse covariance) | `alpha`, `max_iter`, `mode` |
| `empirical_covariance` | `covariance/_empirical_covariance.py:L76` | Functional form of the sample estimator | `assume_centered` |
| `shrunk_covariance` | `covariance/_shrunk_covariance.py:L118` | Functional form of shrinkage | `shrinkage`, `covariance_` |
| `log_likelihood` | `covariance/_empirical_covariance.py:L39` | Gaussian log-likelihood of data under a (cov, precision) pair | `emp_cov`, `precision_` |

## Common Patterns

```python
# Small-sample portfolio covariance: shrink when T < N
import numpy as np
from sklearn.covariance import (EllipticEnvelope, EmpiricalCovariance, GraphicalLasso,
                                LedoitWolf, MinCovDet, log_likelihood)

rng = np.random.default_rng(0)
T, N = 120, 40  # 120 days of returns, 40 assets: T < N regime
returns = rng.normal(0, 0.01, size=(T, N))

emp = EmpiricalCovariance().fit(returns)
lw = LedoitWolf().fit(returns)
print(np.linalg.cond(emp.covariance_), np.linalg.cond(lw.covariance_))
print(log_likelihood(lw.covariance_, lw.precision_),
      log_likelihood(emp.covariance_, emp.precision_))

# Min-variance weights from the shrunk covariance
w = np.linalg.solve(lw.covariance_, np.ones(N))
w /= w.sum()
print(w[:5])

# Robust covariance: 5% contaminated returns
contam = returns.copy()
for _ in range(10):
    i, j = rng.integers(0, T), rng.integers(0, N)
    contam[i, j] *= 20.0
mcd = MinCovDet(random_state=42).fit(contam)
print(np.linalg.cond(mcd.covariance_))
env = EllipticEnvelope(contamination=0.1, random_state=42).fit(contam)
print(env.predict(contam[:10]))

# Sparse precision via GraphicalLasso for sector structure
gl = GraphicalLasso(alpha=0.05, max_iter=200).fit(contam)
print(np.count_nonzero(gl.precision_) / gl.precision_.size)
```

## Pitfalls
1. **Sample covariance is singular when T < N**: `EmpiricalCovariance` becomes ill-conditioned
   or rank-deficient with more assets than return samples. Use `LedoitWolf` — it shrinks toward
   a well-conditioned target with an analytically optimal intensity.
2. **`assume_centered` double-centering**: Default `False` estimates the mean from data. If you
   pre-center returns yourself, set `assume_centered=True`, or the mean is subtracted twice.
3. **MCD breaks down past ~50% contamination**: `MinCovDet` and `EllipticEnvelope` assume a
   majority of clean observations; `support_fraction` below 0.5 is unreliable. Set
   `contamination` to the real outlier rate, and `random_state` for reproducibility.
4. **GraphicalLasso is expensive and alpha-sensitive**: Cost scales O(p³). Too small an `alpha`
   gives a dense, noisy precision; too large over-sparsifies and biases the structure. Use
   `GraphicalLassoCV` to select it.
5. **Precision ≠ covariance**: `GraphicalLasso`/estimators' `precision_` is the inverse —
   zeros there mean *conditional* independence (partial correlations), not zero covariance.
   Interpret `covariance_` for marginal structure, `precision_` for direct links.

## Verification Checklist
- [ ] Shrinkage (`LedoitWolf`) used when `n_samples < n_features`
- [ ] `assume_centered` matches how the data was (not) centered
- [ ] `random_state` set on `MinCovDet` / `EllipticEnvelope`
- [ ] `contamination` reflects the real outlier rate before robust fits
- [ ] `log_likelihood` compared across candidate estimators on OOS returns
- [ ] `GraphicalLasso` alpha selected by CV (not a single arbitrary value)

## Provenance
- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `EmpiricalCovariance` (22), `MinCovDet` (17), `EllipticEnvelope` (14) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
