---
name: scikit-learn-metrics
description: Use when working with scikit-learn metrics, scoring functions, pairwise
  distances, or clustering evaluation. Covers accuracy_score, f1_score, classification_report,
  roc_auc_score, silhouette_score, and pairwise distance metrics.
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
  graph_hash: 75a69cbf83913826
tags:
- scikit-learn
- machine-learning
- metrics
- scoring
- classification
- regression
- clustering
related_skills:
- scikit-learn-model-selection
- scikit-learn-preprocessing
---

# scikit-learn Metrics

Extracted from scikit-learn knowledge graph. Source: `sklearn.metrics` module.

## Quick Reference
### Classification Metrics

| Function | Purpose | Graph Node | Key Params |
|----------|---------|-----------|------------|
| `accuracy_score` | Fraction of correct predictions | metrics/_classification.py:L357 | `normalize`, `sample_weight` |
| `precision_score` | Ratio tp / (tp + fp) | metrics/_classification.py:L2527 | `average`, `pos_label`, `zero_division` |
| `recall_score` | Ratio tp / (tp + fn) | metrics/_classification.py:L2710 | `average`, `pos_label`, `zero_division` |
| `f1_score` | Harmonic mean of precision and recall | metrics/_classification.py:L1461 | `average`, `pos_label` |
| `fbeta_score` | Weighted harmonic mean (beta param) | metrics/_classification.py:L1656 | `beta`, `average` |
| `classification_report` | Text summary of precision, recall, f1 | metrics/_classification.py:L2996 | `target_names`, `output_dict` |
| `confusion_matrix` | Compute confusion matrix | metrics/_classification.py:L443 | `labels`, `normalize` |
| `roc_auc_score` | Area under ROC curve | metrics/_ranking.py:L513 | `average`, `multi_class`, `max_fpr` |
| `log_loss` | Logistic / cross-entropy loss | metrics/_classification.py:L3347 | `eps`, `normalize`, `sample_weight` |
| `balanced_accuracy_score` | Class-balanced accuracy | metrics/_classification.py:L2884 | `adjusted`, `sample_weight` |
| `matthews_corrcoef` | MCC (phi coefficient) | metrics/_classification.py:L1252 | `sample_weight` |
| `cohen_kappa_score` | Inter-rater agreement | metrics/_classification.py:L888 | `labels`, `weights`, `sample_weight` |
| `hamming_loss` | Fraction of wrong labels | metrics/_classification.py:L3230 | `sample_weight` |
| `jaccard_score` | Intersection over union | metrics/_classification.py:L1058 | `average`, `pos_label`, `sample_weight` |
| `brier_score_loss` | Brier score for probabilities | metrics/_classification.py:L3739 | `pos_label`, `sample_weight` |
| `zero_one_loss` | Fraction of misclassifications | metrics/_classification.py:L1362 | `normalize`, `sample_weight` |
| `top_k_accuracy_score` | Top-k accuracy | metrics/_ranking.py:L2086 | `k`, `normalize`, `sample_weight` |

### Regression Metrics

| Function | Purpose | Graph Node |
|----------|---------|-----------|
| `r2_score` | Coefficient of determination | metrics/_regression.py:L1179 |
| `mean_squared_error` | MSE (L2 loss) | metrics/_regression.py:L551 |
| `root_mean_squared_error` | RMSE (sqrt of MSE) | metrics/_regression.py:L642 |
| `mean_absolute_error` | MAE (L1 loss) | metrics/_regression.py:L257 |
| `mean_absolute_percentage_error` | MAPE | metrics/_regression.py:L447 |
| `explained_variance_score` | Explained variance | metrics/_regression.py:L1033 |
| `max_error` | Maximum residual error | metrics/_regression.py:L1348 |
| `mean_squared_log_error` | Mean squared log error | metrics/_regression.py:L730 |
| `mean_gamma_deviance` | Gamma deviance (for GammaRegressor) | metrics/_regression.py:L1565 |
| `mean_poisson_deviance` | Poisson deviance (for PoissonRegressor) | metrics/_regression.py:L1522 |
| `mean_tweedie_deviance` | Tweedie deviance | — |
| `d2_tweedie_score` | D² Tweedie score | metrics/_regression.py:L1613 |

### Clustering Metrics

| Function | Purpose | Graph Node |
|----------|---------|-----------|
| `silhouette_score` | Silhouette coefficient | metrics/cluster/_unsupervised.py:L59 |
| `adjusted_rand_score` | Adjusted Rand index | metrics/cluster/_supervised.py:L360 |
| `normalized_mutual_info_score` | NMI | metrics/cluster/_supervised.py:L1084 |
| `calinski_harabasz_score` | Variance ratio criterion | metrics/cluster/_unsupervised.py:L333 |
| `davies_bouldin_score` | Davies-Bouldin index | metrics/cluster/_unsupervised.py:L413 |

### Pairwise Distances

| Function | Purpose | Graph Node |
|----------|---------|-----------|
| `pairwise_distances` | Compute distance matrix between vectors | metrics/pairwise.py:L2311 |
| `cosine_similarity` | Cosine similarity kernel | metrics/pairwise.py:L1705 |
| `euclidean_distances` | Euclidean distance matrix | metrics/pairwise.py:L268 |

### Scorer Utilities

| Function | Purpose | Graph Node |
|----------|---------|-----------|
| `make_scorer` | Build a scorer from a metric function | metrics/_scorer.py:L674 |
| `get_scorer` | Get scorer by name from registry | metrics/_scorer.py:L478 |

> Note: mean_tweedie_deviance exists in the library but is absent from the committed graph (extraction gap).

## Common Patterns

```python
# Regression diagnostics on out-of-sample return predictions
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import make_scorer, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

rng = np.random.default_rng(0)
X = rng.normal(size=(300, 5))
y = 0.5 * X[:, 0] - 0.2 * X[:, 2] + rng.normal(scale=0.4, size=300)
y_pred = Ridge(alpha=1.0).fit(X, y).predict(X)
print(r2_score(y, y_pred), mean_squared_error(y, y_pred))

# Custom scorer: directional hit rate (sign agreement with the target)
def hit_rate(y_true, y_pred):
    return float(np.mean(np.sign(y_true) == np.sign(y_pred)))

hit_scorer = make_scorer(hit_rate)
tscv = TimeSeriesSplit(n_splits=5)
scores = cross_val_score(Ridge(), X, y, cv=tscv, scoring=hit_scorer)
print(scores, scores.mean())
```

## Pitfalls
1. **`average` parameter for multiclass**: `precision_score` / `recall_score` / `f1_score` default to `average='binary'` — fails on multiclass. Use `'macro'`, `'micro'`, or `'weighted'`.
2. **`roc_auc_score` on multiclass**: Requires `multi_class='ovr'` or `'ovo'` and probability estimates.
3. **`zero_division` behavior**: By default returns 0 and warns for undefined precision. Set `zero_division=1` to suppress.
4. **Clustering metrics require labels**: `adjusted_rand_score` and `normalized_mutual_info_score` need ground-truth labels, not raw data.
5. **`r2_score` can be negative**: R² < 0 means the model is worse than a constant mean predictor.

## Verification Checklist

- [ ] Correct `average` parameter for multiclass/multilabel
- [ ] Scoring metric matches business objective (e.g., `f1` vs `roc_auc` vs `recall`)
- [ ] Probability calibration checked before `brier_score_loss` or `log_loss`
- [ ] `sample_weight` propagated when using weighted datasets

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `pairwise.py:L1` (39), `_classification.py:L1` (31), `_ranking.py:L1` (22) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
