---
name: scikit-learn-metrics
description: Use when working with scikit-learn metrics, scoring functions, pairwise distances, or clustering evaluation. Covers accuracy_score, f1_score, classification_report, roc_auc_score, silhouette_score, and pairwise distance metrics.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_version: main
extraction_date: 2026-07-29
graph_hash: 18753_nodes_49978_edges
graph_stats:
  nodes: 18753
  edges: 49978
  communities: [35, 94, 105, 123, 125, 133, 315, 346, 347, 363, 382, 415, 515]
metadata:
  hermes:
    tags: [scikit-learn, machine-learning, metrics, scoring, classification, regression, clustering]
    related_skills: [scikit-learn-model-selection, scikit-learn-preprocessing]
---

# scikit-learn Metrics

Extracted from scikit-learn knowledge graph. Source: `sklearn.metrics` module.

## Quick Reference

### Classification Metrics

| Function | Purpose | Key Params |
|----------|---------|------------|
| `accuracy_score` | Fraction of correct predictions | `normalize`, `sample_weight` |
| `precision_score` | Ratio tp / (tp + fp) | `average`, `pos_label`, `zero_division` |
| `recall_score` | Ratio tp / (tp + fn) | `average`, `pos_label`, `zero_division` |
| `f1_score` | Harmonic mean of precision and recall | `average`, `pos_label` |
| `fbeta_score` | Weighted harmonic mean (beta param) | `beta`, `average` |
| `classification_report` | Text summary of precision, recall, f1 | `target_names`, `output_dict` |
| `confusion_matrix` | Compute confusion matrix | `labels`, `normalize` |
| `roc_auc_score` | Area under ROC curve | `average`, `multi_class`, `max_fpr` |
| `log_loss` | Logistic / cross-entropy loss | `eps`, `normalize`, `sample_weight` |
| `balanced_accuracy_score` | Class-balanced accuracy | `adjusted`, `sample_weight` |
| `matthews_corrcoef` | MCC (phi coefficient) | `sample_weight` |
| `cohen_kappa_score` | Inter-rater agreement | `labels`, `weights`, `sample_weight` |
| `hamming_loss` | Fraction of wrong labels | `sample_weight` |
| `jaccard_score` | Intersection over union | `average`, `pos_label`, `sample_weight` |
| `brier_score_loss` | Brier score for probabilities | `pos_label`, `sample_weight` |
| `zero_one_loss` | Fraction of misclassifications | `normalize`, `sample_weight` |
| `top_k_accuracy_score` | Top-k accuracy | `k`, `normalize`, `sample_weight` |

### Regression Metrics

| Function | Purpose |
|----------|---------|
| `r2_score` | Coefficient of determination |
| `mean_squared_error` | MSE (L2 loss) |
| `root_mean_squared_error` | RMSE (sqrt of MSE) |
| `mean_absolute_error` | MAE (L1 loss) |
| `mean_absolute_percentage_error` | MAPE |
| `explained_variance_score` | Explained variance |
| `max_error` | Maximum residual error |
| `mean_squared_log_error` | Mean squared log error |
| `mean_gamma_deviance` | Gamma deviance (for GammaRegressor) |
| `mean_poisson_deviance` | Poisson deviance (for PoissonRegressor) |
| `mean_tweedie_deviance` | Tweedie deviance |
| `d2_tweedie_score` | D² Tweedie score |

### Clustering Metrics

| Function | Purpose |
|----------|---------|
| `silhouette_score` | Silhouette coefficient |
| `adjusted_rand_score` | Adjusted Rand index |
| `normalized_mutual_info_score` | NMI |
| `calinski_harabasz_score` | Variance ratio criterion |
| `davies_bouldin_score` | Davies-Bouldin index |

### Pairwise Distances

| Function | Purpose |
|----------|---------|
| `pairwise_distances` | Compute distance matrix between vectors |
| `cosine_similarity` | Cosine similarity kernel |
| `euclidean_distances` | Euclidean distance matrix |

### Scorer Utilities

| Function | Purpose |
|----------|---------|
| `make_scorer` | Build a scorer from a metric function |
| `get_scorer` | Get scorer by name from registry |

## Common Pitfalls

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

## References

- `references/api.md` — Full API surface from knowledge graph
- `references/examples.md` — Extracted from scikit-learn examples/
