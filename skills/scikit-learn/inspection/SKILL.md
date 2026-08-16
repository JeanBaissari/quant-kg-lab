---
name: scikit-learn-inspection
description: "Use when explaining fitted models in quant pipelines \u2014 permutation\
  \ importance, partial dependence, decision boundaries, and prediction-vs-decision\
  \ consistency checks via sklearn.inspection."
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
- model-interpretation
- permutation-importance
- partial-dependence
related_skills:
- scikit-learn-ensemble
- scikit-learn-feature-selection
- scikit-learn-model-selection
---

# scikit-learn Inspection (`sklearn.inspection`)

Model-explainability module for fitted quant models: `permutation_importance` ranks factors
by their effect on out-of-sample error, `partial_dependence` shows how a factor moves
predictions while others are marginalized, and `DecisionBoundaryDisplay` visualizes
`decision_function`/prediction surfaces. Reach for it when a factor model is a black box and
you need verifiable, factor-level evidence.

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `permutation_importance` | `inspection/_permutation_importance.py:L138` | Rank features by score drop when permuted on validation data | `scoring`, `n_repeats`, `random_state`, `n_jobs` |
| `partial_dependence` | `inspection/_partial_dependence.py:L370` | Average model prediction vs one/two features, others marginalized | `kind` ('average'/'individual'), `grid_resolution`, `percentiles` |
| `PartialDependenceDisplay` | `inspection/_plot/partial_dependence.py:L22` | Plot partial dependence from an estimator (`from_estimator`) | `features`, `kind`, `target`, `ice_ratio` |
| `DecisionBoundaryDisplay` | `inspection/_plot/decision_boundary.py:L151` | Plot the decision surface in 2D feature space | `response_method` ('decision_function'/'predict_proba'/'predict') |

## Common Patterns

```python
# Permutation importance on a held-out OOS slice (never permute inside train)
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import (DecisionBoundaryDisplay, PartialDependenceDisplay,
                                partial_dependence, permutation_importance)
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
X = rng.normal(size=(500, 6))
y = 1.5 * X[:, 0] - 0.8 * X[:, 2] + rng.normal(scale=0.5, size=500)
X_train, X_oos = X[:400], X[400:]
y_train, y_oos = y[:400], y[400:]

rf = RandomForestRegressor(n_estimators=200, max_depth=8, random_state=42).fit(X_train, y_train)
imp = permutation_importance(rf, X_oos, y_oos, n_repeats=10,
                             scoring="neg_mean_squared_error", random_state=42)
print(sorted(zip(range(6), imp.importances_mean), key=lambda t: -t[1]))

# Partial dependence: for a linear model the PDP slope equals the coefficient
ridge = Ridge(alpha=1.0).fit(X_train, y_train)
pd = partial_dependence(ridge, X_train, features=[0], kind="average")
print(pd.average.shape, ridge.coef_[0])
PartialDependenceDisplay.from_estimator(ridge, X_train, features=[0], kind="average")

# Decision boundary + prediction check: sign(decision_function) == predict
clf = Pipeline([("std", StandardScaler()),
                ("logit", LogisticRegression(max_iter=1000))])
clf.fit(X_train[:, :2], (y_train > 0).astype(int))
scores = clf.decision_function(X_train[:, :2])
print(np.mean(np.sign(scores) == clf.predict(X_train[:, :2])))
DecisionBoundaryDisplay.from_estimator(clf, X_train[:, :2], response_method="decision_function")
```

## Pitfalls
1. **Permutation importance leaks on time series**: Permuting features inside a temporally
   correlated window destroys the ordering the model saw. Score on a strict OOS slice
   (TimeSeriesSplit holdout), never on the training window, and fix `random_state`.
2. **PDP assumes feature independence**: Marginalizing over correlated momentum/vol factors
   produces points outside the observed joint distribution. Report PDPs per factor with the
   correlation caveat, or use `kind="individual"` lines to see spread.
3. **`kind="recursion"` is fast but biased**: It reuses the tree's internal split statistics,
   fails for multiclass and non-tree estimators, and over-weights correlated features.
   Prefer `kind="average"` for correctness.
4. **Grid resolution cost**: `grid_resolution` (default 100) × features grows the forward
   pass cost. Keep `percentiles=(5, 95)` and small grids on wide data.
5. **DecisionBoundaryDisplay is 2D-only**: Mesh grids live in the space of the features you
   pass. For >2 features project first (e.g. PCA) or pick the two most important factors.

## Verification Checklist
- [ ] `permutation_importance` scored on an OOS slice with `random_state` set
- [ ] `partial_dependence` used with `kind="average"` (or "individual") — not "recursion" — for correlated factors
- [ ] `PartialDependenceDisplay` built on training data only
- [ ] `response_method` matches the model (decision_function for linear classifiers)
- [ ] sign(`decision_function`) agreement with `predict` checked for classifiers

## Provenance
- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `PartialDependenceDisplay` (12), `DecisionBoundaryDisplay` (8) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
