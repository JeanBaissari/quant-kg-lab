---
name: scikit-learn-gaussian-process
description: "Use when working with scikit-learn Gaussian Processes — GPC, GPR, and kernel functions. Covers core classes, methods, and quant-relevant patterns."
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
tags: [scikit-learn, machine-learning, gaussian-process, gp, bayesian, uncertainty, kernels]
related_skills: [scikit-learn-model-selection, scikit-learn-metrics, scikit-learn-preprocessing]
---

# scikit-learn Gaussian Processes

Extracted from scikit-learn knowledge graph. Source: `sklearn.gaussian_process` module.
Communities: 30 ("Gaussian Processes GPC"), 58 ("Gaussian Processes"), 160 ("Gaussian Processes GPR"), 116, 216, 544.

## Quick Reference

| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `GaussianProcessClassifier` | `gaussian_process/_gpc.py` | GP classification with Laplace approximation | `kernel`, `optimizer`, `n_restarts_optimizer`, `max_iter_predict` |
| `GaussianProcessRegressor` | `gaussian_process/_gpr.py` | GP regression with exact inference | `kernel`, `alpha` (noise level), `optimizer`, `n_restarts_optimizer`, `normalize_y` |
| `RBF` | `gaussian_process/kernels.py` | Radial Basis Function (squared exponential) kernel | `length_scale`, `length_scale_bounds` |
| `Matern` | `gaussian_process/kernels.py` | Matérn covariance kernel | `length_scale`, `nu` (0.5/1.5/2.5/∞), `length_scale_bounds` |
| `RationalQuadratic` | `gaussian_process/kernels.py` | Rational Quadratic kernel (scale mixture of RBF) | `length_scale`, `alpha` (scale mixture), `length_scale_bounds`, `alpha_bounds` |
| `ExpSineSquared` | `gaussian_process/kernels.py` | Periodic kernel | `length_scale`, `periodicity`, `length_scale_bounds`, `periodicity_bounds` |
| `DotProduct` | `gaussian_process/kernels.py` | Linear (dot product) kernel | `sigma_0` (inhomogeneity), `sigma_0_bounds` |
| `ConstantKernel` | `gaussian_process/kernels.py` | Constant kernel (amplitude scaling) | `constant_value`, `constant_value_bounds` |
| `WhiteKernel` | `gaussian_process/kernels.py` | White noise kernel | `noise_level`, `noise_level_bounds` |
| `Sum(k1, k2)` | `gaussian_process/kernels.py` | Sum of two kernels (OR combination) | — |
| `Product(k1, k2)` | `gaussian_process/kernels.py` | Product of two kernels (AND combination) | — |
| `Exponentiation(kernel, exponent)` | `gaussian_process/kernels.py` | Exponentiate a kernel | `kernel`, `exponent` |
| `Kernel` | `gaussian_process/kernels.py` | Abstract base for all kernels | — |
| `Hyperparameter` | `gaussian_process/kernels.py` | Descriptor for kernel hyperparameters | `name`, `value_type`, `bounds`, `n_elements`, `fixed` |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.__call__(X, Y)` | 13 nodes | Compute kernel matrix K(X, Y) |
| `.__repr__()` | 12 nodes | String representation |
| `.diag(X)` | 11 nodes | Diagonal of K(X, X) |
| `.__init__()` | 14 nodes | Kernel/GP constructors |
| `.is_stationary()` | 6 nodes | Whether kernel is stationary |
| `.get_params()` | 4 nodes | Get kernel hyperparameters |
| `.bounds` | 4 nodes | Log-transformed bounds on theta |
| `.fit(X, y)` | 3 nodes | Fit GP (optimize hyperparameters) |
| `.predict(X)` | 3 nodes | Predictive mean |
| `.log_marginal_likelihood()` | 3 nodes | LML (for hyperparameter optimization) |
| `.sample_y(X)` | — | Draw samples from posterior (GPR only) |
| `.predict_proba(X)` | — | Class probabilities (GPC only) |

## Common Patterns

```python
# GPR with custom kernel — quant-style uncertainty estimation
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel

# Kernel: amplitude * RBF(length_scale) + noise
kernel = ConstantKernel(1.0) * RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
gpr = GaussianProcessRegressor(
    kernel=kernel,
    alpha=0.0,               # additional noise on training targets
    optimizer='fmin_l_bfgs_b',
    n_restarts_optimizer=5,  # avoid local optima
    normalize_y=True,
    random_state=42
)
gpr.fit(X_train, y_train)

# Predict with uncertainty
y_pred, y_std = gpr.predict(X_test, return_std=True)
# 95% confidence interval
ci_lower = y_pred - 1.96 * y_std
ci_upper = y_pred + 1.96 * y_std

# Sample from posterior
y_samples = gpr.sample_y(X_test, n_samples=100)

# Inspect learned kernel
print(gpr.kernel_)  # e.g., 2.34**2 * RBF(length_scale=1.45) + WhiteKernel(noise_level=0.01)
print(f"LML: {gpr.log_marginal_likelihood_value_:.2f}")

# Composite kernels for quant data
from sklearn.gaussian_process.kernels import Matern, ExpSineSquared, Sum, Product

# Trend + seasonal + noise
kernel = (
    ConstantKernel() * Matern(length_scale=10, nu=1.5) +       # smooth trend
    ConstantKernel() * ExpSineSquared(periodicity=30, length_scale=5) +  # monthly cycle
    WhiteKernel(noise_level=0.5)                                 # observation noise
)

# GPC for probabilistic classification
from sklearn.gaussian_process import GaussianProcessClassifier
gpc = GaussianProcessClassifier(kernel=RBF(1.0), random_state=42)
gpc.fit(X_train, y_train)
probas = gpc.predict_proba(X_test)
```

## Pitfalls

1. **O(n³) complexity**: Exact GP inference scales cubically with n_samples. Beyond ~5000 samples, use sparse approximations or switch to `GradientBoostingRegressor`/`RandomForestRegressor`.
2. **Kernel initial values**: Poor initial `length_scale` prevents convergence. Use `length_scale_bounds=(1e-3, 1e3)` for robustness and enable `n_restarts_optimizer`.
3. **Cholesky failure**: Ill-conditioned kernel matrices cause `LinAlgError`. Increase `alpha` (adds noise to diagonal) or tighten kernel bounds.
4. **GPC is approximate**: Uses Laplace approximation — uncertainty estimates are approximate for non-Gaussian likelihoods. For rigorous Bayesian classification, consider `pymc` or `stan`.
5. **`normalize_y=True`**: Centers y to zero mean, which improves numerical stability. But predictions are on the centered scale — scikit-learn handles this transparently.
6. **`return_std` vs `return_cov`**: Use `return_std` for diagonal uncertainty, `return_cov` for full predictive covariance matrix (O(n_test³) memory).
7. **`predict_proba` in GPC**: Uses Monte Carlo sampling of the latent function — `max_iter_predict` controls number of samples.