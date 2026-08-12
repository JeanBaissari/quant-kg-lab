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
  community_count: 401
  graph_hash: fc25a6d284e9a3ed
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

| Function | Purpose | Key Params | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node | Graph Node |
|----------|---------|------------|
| `accuracy_score` | Fraction of correct predictions | `normalize`, `sample_weight` | metrics/_classification.py:L357 |
| `precision_score` | Ratio tp / (tp + fp) | `average`, `pos_label`, `zero_division` | metrics/_classification.py:L2527 |
| `recall_score` | Ratio tp / (tp + fn) | `average`, `pos_label`, `zero_division` | metrics/_classification.py:L2710 |
| `f1_score` | Harmonic mean of precision and recall | `average`, `pos_label` | metrics/_classification.py:L1461 |
| `fbeta_score` | Weighted harmonic mean (beta param) | `beta`, `average` | metrics/_classification.py:L1656 |
| `classification_report` | Text summary of precision, recall, f1 | `target_names`, `output_dict` | metrics/_classification.py:L2996 |
| `confusion_matrix` | Compute confusion matrix | `labels`, `normalize` | metrics/_classification.py:L443 |
| `roc_auc_score` | Area under ROC curve | `average`, `multi_class`, `max_fpr` | metrics/_ranking.py:L513 |
| `log_loss` | Logistic / cross-entropy loss | `eps`, `normalize`, `sample_weight` | metrics/_classification.py:L3347 |
| `balanced_accuracy_score` | Class-balanced accuracy | `adjusted`, `sample_weight` | metrics/_classification.py:L2884 |
| `matthews_corrcoef` | MCC (phi coefficient) | `sample_weight` | metrics/_classification.py:L1252 |
| `cohen_kappa_score` | Inter-rater agreement | `labels`, `weights`, `sample_weight` | metrics/_classification.py:L888 |
| `hamming_loss` | Fraction of wrong labels | `sample_weight` | metrics/_classification.py:L3230 |
| `jaccard_score` | Intersection over union | `average`, `pos_label`, `sample_weight` | metrics/_classification.py:L1058 |
| `brier_score_loss` | Brier score for probabilities | `pos_label`, `sample_weight` | metrics/_classification.py:L3739 |
| `zero_one_loss` | Fraction of misclassifications | `normalize`, `sample_weight` | metrics/_classification.py:L1362 |
| `top_k_accuracy_score` | Top-k accuracy | `k`, `normalize`, `sample_weight` | metrics/_ranking.py:L2086 |

### Regression Metrics

| Function | Purpose | covariance/_elliptic_envelope.py:L187 | covariance/_elliptic_envelope.py:L187 |
|----------|---------|
| `r2_score` | Coefficient of determination | metrics/_regression.py:L1179 | metrics/_regression.py:L1179 |
| `mean_squared_error` | MSE (L2 loss) | metrics/_regression.py:L551 | metrics/_regression.py:L551 |
| `root_mean_squared_error` | RMSE (sqrt of MSE) | metrics/_regression.py:L642 | metrics/_regression.py:L642 |
| `mean_absolute_error` | MAE (L1 loss) | metrics/_regression.py:L257 | metrics/_regression.py:L257 |
| `mean_absolute_percentage_error` | MAPE | metrics/_regression.py:L447 | metrics/_regression.py:L447 |
| `explained_variance_score` | Explained variance | metrics/_regression.py:L1033 | metrics/_regression.py:L1033 |
| `max_error` | Maximum residual error | metrics/_regression.py:L1348 | metrics/_regression.py:L1348 |
| `mean_squared_log_error` | Mean squared log error | metrics/_regression.py:L730 | metrics/_regression.py:L730 |
| `mean_gamma_deviance` | Gamma deviance (for GammaRegressor) | metrics/_regression.py:L1565 | metrics/_regression.py:L1565 |
| `mean_poisson_deviance` | Poisson deviance (for PoissonRegressor) | metrics/_regression.py:L1522 | metrics/_regression.py:L1522 |
| `mean_tweedie_deviance` | Tweedie deviance |
| `d2_tweedie_score` | D² Tweedie score | metrics/_regression.py:L1613 | metrics/_regression.py:L1613 |

### Clustering Metrics

| Function | Purpose | covariance/_elliptic_envelope.py:L187 | covariance/_elliptic_envelope.py:L187 |
|----------|---------|
| `silhouette_score` | Silhouette coefficient | metrics/cluster/_unsupervised.py:L59 | metrics/cluster/_unsupervised.py:L59 |
| `adjusted_rand_score` | Adjusted Rand index | metrics/cluster/_supervised.py:L360 | metrics/cluster/_supervised.py:L360 |
| `normalized_mutual_info_score` | NMI | metrics/cluster/_supervised.py:L1084 | metrics/cluster/_supervised.py:L1084 |
| `calinski_harabasz_score` | Variance ratio criterion | metrics/cluster/_unsupervised.py:L333 | metrics/cluster/_unsupervised.py:L333 |
| `davies_bouldin_score` | Davies-Bouldin index | metrics/cluster/_unsupervised.py:L413 | metrics/cluster/_unsupervised.py:L413 |

### Pairwise Distances

| Function | Purpose | covariance/_elliptic_envelope.py:L187 | covariance/_elliptic_envelope.py:L187 |
|----------|---------|
| `pairwise_distances` | Compute distance matrix between vectors | metrics/pairwise.py:L2311 | metrics/pairwise.py:L2311 |
| `cosine_similarity` | Cosine similarity kernel | metrics/pairwise.py:L1705 | metrics/pairwise.py:L1705 |
| `euclidean_distances` | Euclidean distance matrix | metrics/pairwise.py:L268 | metrics/pairwise.py:L268 |

### Scorer Utilities

| Function | Purpose | covariance/_elliptic_envelope.py:L187 | covariance/_elliptic_envelope.py:L187 |
|----------|---------|
| `make_scorer` | Build a scorer from a metric function | metrics/_scorer.py:L674 | metrics/_scorer.py:L674 |
| `get_scorer` | Get scorer by name from registry | metrics/_scorer.py:L478 | metrics/_scorer.py:L478 |

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
- God nodes: `pairwise.py` (39), `_classification.py` (31), `_ranking.py` (22) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
