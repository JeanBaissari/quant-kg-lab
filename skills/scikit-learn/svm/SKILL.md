---
name: scikit-learn-svm
description: "Use when working with scikit-learn SVMs — SVC, SVR, LinearSVC, NuSVC, OneClassSVM. Covers core classes, kernel functions, and quant-relevant patterns."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_commit: 6f8b95aa2234102acc3804fc8c7a3e6bd0506bfb
extraction_date: 2026-07-29
graph:
  nodes: 8662
  edges: 29241
  community_count: 401
  graph_hash: e587e89627b31941
tags: [scikit-learn, machine-learning, svm, svc, svr, classification, regression]
related_skills: [scikit-learn-model-selection, scikit-learn-metrics, scikit-learn-preprocessing]
---

# scikit-learn Support Vector Machines

Extracted from scikit-learn knowledge graph. Source: `sklearn.svm` module.
Communities: 60 ("SVM Liblinear"), 72 ("SVM SVC SVR"), 83 ("SVM LinearSVC/NuSVC"), 102 ("SVM SVC"), 161 ("SVM Libsvm").

## Quick Reference

| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `SVC` | `svm/_classes.py` | C-Support Vector Classification | `C`, `kernel` ('linear'/'rbf'/'poly'/'sigmoid'), `gamma`, `degree`, `class_weight`, `probability` |
| `NuSVC` | `svm/_classes.py` | ν-Support Vector Classification | `nu` (0–1), `kernel`, `gamma`, `class_weight` |
| `SVR` | `svm/_classes.py` | ε-Support Vector Regression | `C`, `epsilon`, `kernel`, `gamma`, `degree` |
| `NuSVR` | `svm/_classes.py` | ν-Support Vector Regression | `nu`, `C`, `kernel`, `gamma` |
| `LinearSVC` | `svm/_classes.py` | Linear SVM (liblinear, scales better) | `C`, `loss` ('hinge'/'squared_hinge'), `penalty` ('l1'/'l2'), `dual`, `max_iter` |
| `LinearSVR` | `svm/_classes.py` | Linear SVM Regression (liblinear) | `C`, `epsilon`, `loss`, `dual`, `max_iter` |
| `OneClassSVM` | `svm/_classes.py` | Unsupervised outlier detection | `nu`, `kernel`, `gamma` |
| `BaseLibSVM` | `svm/_base.py` | Abstract base for libsvm wrappers | — |
| `BaseSVC` | `svm/_base.py` | Abstract base for SVC/NuSVC | — |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.fit(X, y)` | 4 nodes | Train the SVM (solves dual QP) |
| `.predict(X)` | 3 nodes | Predict class/value |
| `.decision_function(X)` | 2 nodes | Signed distance to hyperplane |
| `.__init__()` | 9 nodes | Class constructors |
| `.__sklearn_tags__()` | 4 nodes | Estimator tag introspection |
| `.support_vectors_` | — | Support vectors (kernel SVMs) |
| `.support_` | — | Indices of support vectors |
| `.n_support_` | — | Number of support vectors per class |
| `.dual_coef_` | — | Dual coefficients |
| `.coef_` | — | Weights (linear SVC/SVR) |
| `.intercept_` | — | Intercept term |

## Common Patterns

```python
# SVC with RBF kernel — powerful non-linear classifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

svc = make_pipeline(
    StandardScaler(),  # SVM is scale-sensitive
    SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
)
svc.fit(X_train, y_train)
probas = svc.predict_proba(X_test)
decisions = svc.decision_function(X_test)  # raw distances

# SVR for quant prediction — robust to outliers with epsilon tube
from sklearn.svm import SVR
svr = make_pipeline(
    StandardScaler(),
    SVR(kernel='rbf', C=10.0, epsilon=0.01, gamma='scale')
)
svr.fit(X_train, y_train)

# LinearSVC for large datasets — much faster than kernel SVC
from sklearn.svm import LinearSVC
lsvc = LinearSVC(C=1.0, loss='squared_hinge', dual=False, max_iter=10000)
lsvc.fit(X_train, y_train)
coefs = lsvc.coef_  # linear feature weights — interpretable

# OneClassSVM for anomaly/outlier detection in quant data
from sklearn.svm import OneClassSVM
ocsvm = OneClassSVM(nu=0.05, kernel='rbf', gamma='auto')
ocsvm.fit(X_train)  # no y — unsupervised
anomaly_scores = ocsvm.decision_function(X_test)
is_outlier = ocsvm.predict(X_test)  # 1=inlier, -1=outlier
```

## Pitfalls

1. **Scale sensitivity**: SVMs are not scale-invariant. Always standardize features (`StandardScaler`). Kernel RBF distances are dominated by large-scale features otherwise.
2. **Kernel selection**: RBF is the default and most flexible, but linear is orders of magnitude faster for high-dimensional data (n_features >> n_samples).
3. **C vs. nu**: C controls margin hardness (higher = less regularization). nu sets an upper bound on training errors and lower bound on support vectors. They cannot be used together.
4. **probability=True cost**: Computing Platt-scaled probabilities adds a 5-fold internal CV — `predict_proba` is ~5× slower than `predict`.
5. **Dual vs primal**: `dual=False` in `LinearSVC` uses primal optimization and is much faster for n_samples >> n_features. `dual=True` (default) is faster for n_features >> n_samples.
6. **Sparsity**: SVC/SVR support sparse input via `fit(X, y)` directly. LinearSVC *with* `dual=False` supports sparse. `dual=True` does not.
7. **Memory**: Kernel SVMs store all support vectors (can be thousands), consuming significant memory at prediction time.