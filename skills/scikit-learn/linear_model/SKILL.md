---
name: scikit-learn-linear-model
description: "Use when working with scikit-learn linear models \u2014 regression (LinearRegression,\
  \ Ridge, Lasso, ElasticNet), classification (LogisticRegression, SGDClassifier),\
  \ and robust alternatives (Huber, RANSAC, Quantile). Covers loss functions, regularization,\
  \ and solver selection."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-07-29
graph:
  nodes: 8450
  edges: 28094
  community_count: 367
  graph_hash: 9ce80bbf4dcf8c7c
tags:
- scikit-learn
- machine-learning
- linear-models
- regression
- classification
- regularization
related_skills:
- scikit-learn-metrics
- scikit-learn-model-selection
- scikit-learn-preprocessing
target_version: '1.9.0 (dev: after 1.9.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `scikit-learn` ahead of the latest PyPI release (1.9.0 (dev: after 1.9.0)). Some APIs may not exist in your installed version.

# scikit-learn Linear Models

Extracted from scikit-learn knowledge graph. Source: `sklearn.linear_model` module.

## Quick Reference
### Ordinary Least Squares & Regularized Regression

| Class | Purpose | Key Params | Graph Node |
|-----|-------|----------|----------|
| `LinearRegression` | Ordinary least squares | `fit_intercept`, `n_jobs` | linear_model/_base.py:L519 |
| `Ridge` | L2-regularized linear regression | `alpha`, `solver`, `fit_intercept` | linear_model/_ridge.py:L1022 |
| `RidgeCV` | Ridge with built-in CV for alpha | `alphas`, `cv`, `scoring`, `store_cv_values` | linear_model/_ridge.py:L2658 |
| `RidgeClassifier` | Ridge for classification | `alpha`, `solver`, `class_weight` | linear_model/_ridge.py:L1389 |
| `RidgeClassifierCV` | RidgeClassifier with CV | `alphas`, `cv`, `class_weight` | linear_model/_ridge.py:L2869 |
| `Lasso` | L1-regularized (sparse) regression | `alpha`, `max_iter`, `tol`, `selection` | linear_model/_coordinate_descent.py:L1365 |
| `LassoCV` | Lasso with built-in CV | `eps`, `n_alphas`, `cv`, `max_iter` | linear_model/_coordinate_descent.py:L2066 |
| `ElasticNet` | L1 + L2 regularization | `alpha`, `l1_ratio`, `max_iter` | linear_model/_coordinate_descent.py:L920 |
| `ElasticNetCV` | ElasticNet with CV | `l1_ratio`, `eps`, `n_alphas`, `cv` | linear_model/_coordinate_descent.py:L2320 |
| `Lars` | Least Angle Regression | `n_nonzero_coefs`, `fit_intercept` | linear_model/_least_angle.py:L925 |
| `LarsCV` | Lars with CV | `max_n_alphas`, `cv` | linear_model/_least_angle.py:L1520 |
| `LassoLars` | Lasso via LARS algorithm | `alpha`, `max_iter`, `fit_intercept` | linear_model/_least_angle.py:L1215 |
| `LassoLarsCV` | LassoLars with CV | `max_n_alphas`, `cv` | linear_model/_least_angle.py:L1836 |
| `MultiTaskLasso` | Lasso for multi-output regression | `alpha`, `max_iter`, `tol` | linear_model/_coordinate_descent.py:L2904 |
| `MultiTaskElasticNet` | ElasticNet for multi-output | `alpha`, `l1_ratio`, `max_iter` | linear_model/_coordinate_descent.py:L2602 |
| `OrthogonalMatchingPursuit` | Greedy feature selection (OMP) | `n_nonzero_coefs`, `tol`, `fit_intercept` | linear_model/_omp.py:L658 |
| `BayesianRidge` | Bayesian regression with ARD | `alpha_1`, `lambda_1`, `max_iter` | linear_model/_bayes.py:L26 |
| `ARDRegression` | Automatic Relevance Determination | `alpha_1`, `lambda_1`, `threshold_lambda` | linear_model/_bayes.py:L467 |

### Robust & Quantile Regression

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `HuberRegressor` | Huber loss (outlier-robust L2/L1) | `epsilon`, `max_iter`, `alpha` | linear_model/_huber.py:L129 |
| `QuantileRegressor` | Conditional quantile regression | `quantile`, `alpha`, `solver` | linear_model/_quantile.py:L20 |
| `RANSACRegressor` | RANSAC outlier-robust regression | `estimator`, `min_samples`, `residual_threshold` | linear_model/_ransac.py:L81 |
| `TheilSenRegressor` | Theil-Sen median-based estimator | `fit_intercept`, `max_subpopulation` | linear_model/_theil_sen.py:L207 |

### SGD-Based Models

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `SGDClassifier` | Linear classifier via SGD | `loss`, `penalty`, `alpha`, `max_iter`, `learning_rate` | linear_model/_stochastic_gradient.py:L958 |
| `SGDRegressor` | Linear regression via SGD | `loss`, `penalty`, `alpha`, `max_iter` | linear_model/_stochastic_gradient.py:L1802 |
| `SGDOneClassSVM` | One-class classification via SGD | `nu`, `fit_intercept`, `max_iter` | linear_model/_stochastic_gradient.py:L2125 |
| `Perceptron` | Classic perceptron (SGD with hinge) | `penalty`, `alpha`, `max_iter`, `eta0` | linear_model/_perceptron.py:L10 |
| `PassiveAggressiveClassifier` | Online passive-aggressive classifier | `C`, `max_iter`, `tol`, `loss` | linear_model/_passive_aggressive.py:L22 |
| `PassiveAggressiveRegressor` | Online passive-aggressive regressor | `C`, `max_iter`, `tol`, `loss` | linear_model/_passive_aggressive.py:L348 |

### Generalized Linear Models (GLM)

| Class | Purpose | Key Params | externals/array_api_compat/common/_typing.py:L39 |
|-------|---------|------------|
| `LogisticRegression` | Logistic / multinomial classification | `penalty`, `C`, `solver`, `multi_class`, `max_iter` | linear_model/_logistic.py:L1001 |
| `LogisticRegressionCV` | LogisticRegression with CV for C | `Cs`, `cv`, `scoring`, `penalty`, `solver` | linear_model/_logistic.py:L1692 |
| `PoissonRegressor` | GLM with Poisson distribution (counts) | `alpha`, `fit_intercept`, `max_iter` | linear_model/_glm/glm.py:L575 |
| `GammaRegressor` | GLM with Gamma distribution (positive) | `alpha`, `fit_intercept`, `max_iter` | linear_model/_glm/glm.py:L763 |
| `TweedieRegressor` | GLM with Tweedie distribution | `power`, `alpha`, `fit_intercept`, `max_iter` | linear_model/_glm/glm.py:L944 |

## Common Patterns

```python
# L2 shrinkage with built-in CV: RidgeCV picks alpha on the validation path
import numpy as np
from sklearn.linear_model import LassoCV, LogisticRegression, Ridge, RidgeCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(size=(600, 10))
y = 0.8 * X[:, 0] - 0.4 * X[:, 3] + rng.normal(scale=0.3, size=600)

ridge_cv = RidgeCV(alphas=np.logspace(-3, 3, 20), cv=5).fit(X, y)
print(ridge_cv.alpha_, ridge_cv.coef_[:5])

# L1 path: LassoCV drives most factor coefficients to zero
lasso_cv = LassoCV(alphas=np.logspace(-3, 1, 50), cv=5, random_state=42).fit(X, y)
print(np.count_nonzero(lasso_cv.coef_), lasso_cv.alpha_)

# Directional classification (return sign) with a scaled pipeline
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)
clf = Pipeline([("std", StandardScaler()),
                ("logit", LogisticRegression(penalty="l2", C=1.0, max_iter=1000))])
clf.fit(Xtr, (ytr > 0).astype(int))
print(clf.score(Xte, (yte > 0).astype(int)))
```

## Pitfalls
1. **Feature scaling matters**: `LinearRegression` (with OLS solver) and `Ridge` don't strictly require scaling, but `SGD*`, `Perceptron`, `PassiveAggressive*`, and regularized models converge faster/more reliably with standardized features. Always scale for `LogisticRegression`.
2. **`LogisticRegression` `penalty` + `solver` compatibility**: Not all solver/penalty pairs work. Use `solver='lbfgs'` with `penalty='l2'` or `None` for most cases. `penalty='l1'` requires `solver='liblinear'` or `'saga'`.
3. **`SGDClassifier` `loss` parameter**: The default `loss='hinge'` gives a linear SVM. Use `loss='log_loss'` for logistic regression equivalent, `loss='modified_huber'` for probability estimates with outlier tolerance.
4. **GLMs require appropriate targets**: `PoissonRegressor` expects count data (non-negative integers). `GammaRegressor` expects strictly positive continuous targets. `TweedieRegressor` with `power` between 1-2 bridges Poisson and Gamma.
5. **`RANSACRegressor` randomness**: `min_samples` and `residual_threshold` heavily influence results. Set `random_state` for reproducibility.
6. **`Lasso` coordinate descent `selection='random'`**: Faster convergence with less structure-dependent bias, but non-deterministic without `random_state`. Default `'cyclic'` is deterministic but can be slower.

## Verification Checklist

- [ ] Features standardized for regularized/SGD/LogisticRegression models
- [ ] Correct `solver` + `penalty` combination for `LogisticRegression`
- [ ] GLM target values in valid range (positive, integer, etc.)
- [ ] `max_iter` increased if convergence warning appears
- [ ] `random_state` set for reproducible results
- [ ] Model calibrated if probability estimates needed from SGDClassifier

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `LinearModelLoss` (70), `NewtonCholeskySolver` (50), `NewtonCDGramSolver` (48) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
