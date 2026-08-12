---
name: scikit-learn-decomposition
description: "Use when working with scikit-learn matrix decomposition and dimensionality\
  \ reduction \u2014 PCA, NMF, TruncatedSVD, FactorAnalysis, FastICA, DictionaryLearning,\
  \ and LatentDirichletAllocation."
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
- decomposition
- dimensionality-reduction
- pca
- nmf
- svd
related_skills:
- scikit-learn-preprocessing
- scikit-learn-linear-model
---

# scikit-learn Decomposition

Extracted from scikit-learn knowledge graph. Source: `sklearn.decomposition` module.

## Quick Reference

### PCA Variants

| Class | Purpose | Key Params |
|-------|---------|------------|
| `PCA` | Principal Component Analysis (SVD) | `n_components`, `svd_solver`, `whiten`, `random_state` |
| `IncrementalPCA` | PCA on batches (out-of-core) | `n_components`, `batch_size`, `whiten` |
| `KernelPCA` | Non-linear PCA via kernel trick | `n_components`, `kernel`, `gamma`, `eigen_solver` |
| `SparsePCA` | Sparse principal components | `n_components`, `alpha`, `ridge_alpha`, `max_iter` |
| `MiniBatchSparsePCA` | Minibatch sparse PCA | `n_components`, `alpha`, `batch_size`, `max_iter` |

### Matrix Factorization

| Class | Purpose | Key Params |
|-------|---------|------------|
| `NMF` | Non-negative Matrix Factorization | `n_components`, `init`, `solver` ('mu'/'cd'), `max_iter` |
| `TruncatedSVD` | SVD for sparse matrices (LSA) | `n_components`, `algorithm` ('randomized'/'arpack'), `n_iter` |
| `DictionaryLearning` | Sparse dictionary learning | `n_components`, `alpha`, `max_iter`, `transform_algorithm` |
| `MiniBatchDictionaryLearning` | Minibatch dictionary learning | `n_components`, `alpha`, `batch_size`, `max_iter` |

### Other Decompositions

| Class | Purpose | Key Params |
|-------|---------|------------|
| `FactorAnalysis` | Gaussian factor analysis | `n_components`, `tol`, `max_iter`, `rotation` |
| `FastICA` | Independent Component Analysis | `n_components`, `algorithm` ('parallel'/'deflation'), `fun` |
| `LatentDirichletAllocation` | Topic modeling (LDA) | `n_components`, `doc_topic_prior`, `topic_word_prior`, `learning_method` |

## Common Pitfalls

1. **`PCA` `n_components` as float**: When `0 < n_components < 1`, it selects the number of components to explain that fraction of variance. When `n_components=None`, keeps all components (min(n_samples, n_features)).
2. **`TruncatedSVD` for sparse text**: Use for LSA on `TfidfVectorizer` output. Unlike `PCA`, it works directly on sparse matrices without densifying.
3. **`NMF` non-negativity constraint**: Input data must be non-negative. `NMF` cannot handle negative values — use `PCA` or `TruncatedSVD` instead.
4. **`IncrementalPCA` `batch_size`**: Larger batches use more memory but are faster. Must be at least `n_components`. For very large data, this is the only practical PCA option.
5. **`KernelPCA` kernel choice**: `kernel='rbf'` is most common but requires tuning `gamma`. `kernel='linear'` is equivalent to standard PCA. Memory scales as O(n²) — not suitable for >10k samples.
6. **`LatentDirichletAllocation` `learning_method='batch'`**: Expects all data at once, slower but more accurate. `'online'` is faster for large corpora with `batch_size` and `total_samples` params.
7. **`FastICA` sign ambiguity**: Components may be flipped in sign across runs. Use `random_state` for reproducibility, or ignore sign for downstream analysis.

## Verification Checklist

- [ ] `n_components` chosen appropriately (float for variance-based, int for absolute)
- [ ] Sparse matrices handled with `TruncatedSVD`, not `PCA`
- [ ] Non-negative data for `NMF` (scale or clip if needed)
- [ ] `random_state` set for reproducibility (PCA, KernelPCA, FastICA, LDA, SparsePCA)
- [ ] `max_iter` increased if convergence warning
- [ ] `whiten=True` used intentionally (decorrelates and normalizes components)
- [ ] KernelPCA memory budget checked for sample size