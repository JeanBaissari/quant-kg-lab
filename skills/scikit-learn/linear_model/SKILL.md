---
name: scikit-learn-linear-model
description: "Use when working with scikit-learn linear models — regression (LinearRegression, Ridge, Lasso, ElasticNet), classification (LogisticRegression, SGDClassifier), and robust alternatives (Huber, RANSAC, Quantile). Covers loss functions, regularization, and solver selection."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-07-29
graph:
  nodes: 18753
  edges: 49978
  community_count: 1149
  graph_hash: e4761fba3e257880
tags: [scikit-learn, machine-learning, linear-models, regression, classification, regularization]
related_skills: [scikit-learn-metrics, scikit-learn-model-selection, scikit-learn-preprocessing]
---

# scikit-learn Linear Models

Extracted from scikit-learn knowledge graph. Source: `sklearn.linear_model` module.

## Quick Reference

### Ordinary Least Squares & Regularized Regression

| Class | Purpose | Key Params |
|-------|---------|------------|
| `LinearRegression` | Ordinary least squares | `fit_intercept`, `n_jobs` |
| `Ridge` | L2-regularized linear regression | `alpha`, `solver`, `fit_intercept` |
| `RidgeCV` | Ridge with built-in CV for alpha | `alphas`, `cv`, `scoring`, `store_cv_values` |
| `RidgeClassifier` | Ridge for classification | `alpha`, `solver`, `class_weight` |
| `RidgeClassifierCV` | RidgeClassifier with CV | `alphas`, `cv`, `class_weight` |
| `Lasso` | L1-regularized (sparse) regression | `alpha`, `max_iter`, `tol`, `selection` |
| `LassoCV` | Lasso with built-in CV | `eps`, `n_alphas`, `cv`, `max_iter` |
| `ElasticNet` | L1 + L2 regularization | `alpha`, `l1_ratio`, `max_iter` |
| `ElasticNetCV` | ElasticNet with CV | `l1_ratio`, `eps`, `n_alphas`, `cv` |
| `Lars` | Least Angle Regression | `n_nonzero_coefs`, `fit_intercept` |
| `LarsCV` | Lars with CV | `max_n_alphas`, `cv` |
| `LassoLars` | Lasso via LARS algorithm | `alpha`, `max_iter`, `fit_intercept` |
| `LassoLarsCV` | LassoLars with CV | `max_n_alphas`, `cv` |
| `MultiTaskLasso` | Lasso for multi-output regression | `alpha`, `max_iter`, `tol` |
| `MultiTaskElasticNet` | ElasticNet for multi-output | `alpha`, `l1_ratio`, `max_iter` |
| `OrthogonalMatchingPursuit` | Greedy feature selection (OMP) | `n_nonzero_coefs`, `tol`, `fit_intercept` |
| `BayesianRidge` | Bayesian regression with ARD | `alpha_1`, `lambda_1`, `max_iter` |
| `ARDRegression` | Automatic Relevance Determination | `alpha_1`, `lambda_1`, `threshold_lambda` |

### Robust & Quantile Regression

| Class | Purpose | Key Params |
|-------|---------|------------|
| `HuberRegressor` | Huber loss (outlier-robust L2/L1) | `epsilon`, `max_iter`, `alpha` |
| `QuantileRegressor` | Conditional quantile regression | `quantile`, `alpha`, `solver` |
| `RANSACRegressor` | RANSAC outlier-robust regression | `estimator`, `min_samples`, `residual_threshold` |
| `TheilSenRegressor` | Theil-Sen median-based estimator | `fit_intercept`, `max_subpopulation` |

### SGD-Based Models

| Class | Purpose | Key Params |
|-------|---------|------------|
| `SGDClassifier` | Linear classifier via SGD | `loss`, `penalty`, `alpha`, `max_iter`, `learning_rate` |
| `SGDRegressor` | Linear regression via SGD | `loss`, `penalty`, `alpha`, `max_iter` |
| `SGDOneClassSVM` | One-class classification via SGD | `nu`, `fit_intercept`, `max_iter` |
| `Perceptron` | Classic perceptron (SGD with hinge) | `penalty`, `alpha`, `max_iter`, `eta0` |
| `PassiveAggressiveClassifier` | Online passive-aggressive classifier | `C`, `max_iter`, `tol`, `loss` |
| `PassiveAggressiveRegressor` | Online passive-aggressive regressor | `C`, `max_iter`, `tol`, `loss` |

### Generalized Linear Models (GLM)

| Class | Purpose | Key Params |
|-------|---------|------------|
| `LogisticRegression` | Logistic / multinomial classification | `penalty`, `C`, `solver`, `multi_class`, `max_iter` |
| `LogisticRegressionCV` | LogisticRegression with CV for C | `Cs`, `cv`, `scoring`, `penalty`, `solver` |
| `PoissonRegressor` | GLM with Poisson distribution (counts) | `alpha`, `fit_intercept`, `max_iter` |
| `GammaRegressor` | GLM with Gamma distribution (positive) | `alpha`, `fit_intercept`, `max_iter` |
| `TweedieRegressor` | GLM with Tweedie distribution | `power`, `alpha`, `fit_intercept`, `max_iter` |

## Common Pitfalls

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