---
name: scikit-learn-cluster
description: "Use when working with scikit-learn Clustering \u2014 KMeans, DBSCAN,\
  \ HDBSCAN, Agglomerative, MeanShift, Spectral, Birch, OPTICS, and biclustering.\
  \ Covers core classes, methods, and quant-relevant patterns."
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
- clustering
- kmeans
- dbscan
- unsupervised
- quant
related_skills:
- scikit-learn-model-selection
- scikit-learn-metrics
- scikit-learn-preprocessing
---

# scikit-learn Clustering

Extracted from scikit-learn knowledge graph. Source: `sklearn.cluster` module.
Communities: 37 ("Clustering KMeans"), 48 ("Clustering DBSCAN/MeanShift/Spectral"), 147 ("BisectingKMeans"), 935–945 (DBSCAN subcommunities), 966 (KMeans).

## Quick Reference
| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `KMeans` | `cluster/_kmeans.py` | k-means clustering (Lloyd/Elkan) | `n_clusters`, `init`, `n_init`, `max_iter`, `algorithm` ('lloyd'/'elkan'), `random_state` |
| `MiniBatchKMeans` | `cluster/_kmeans.py` | Mini-batch k-means (scalable) | `n_clusters`, `batch_size`, `max_iter`, `random_state` |
| `BisectingKMeans` | `cluster/_bisect_k_means.py` | Hierarchical divisive k-means | `n_clusters`, `bisecting_strategy` ('biggest_inertia'/'largest_cluster'), `random_state` |
| `DBSCAN` | `cluster/_dbscan.py` | Density-based spatial clustering | `eps`, `min_samples`, `metric`, `algorithm` |
| `HDBSCAN` | `cluster/_hdbscan/hdbscan.py` | Hierarchical DBSCAN (variable density) | `min_cluster_size`, `min_samples`, `cluster_selection_epsilon`, `metric` |
| `MeanShift` | `cluster/_mean_shift.py` | Mean shift clustering (density modes) | `bandwidth`, `cluster_all`, `max_iter` |
| `SpectralClustering` | `cluster/_spectral.py` | Spectral clustering (graph Laplacian) | `n_clusters`, `affinity`, `gamma`, `assign_labels` ('kmeans'/'discretize') |
| `AgglomerativeClustering` | `cluster/_agglomerative.py` | Hierarchical agglomerative clustering | `n_clusters`, `linkage` ('ward'/'complete'/'average'/'single'), `metric`, `distance_threshold` |
| `OPTICS` | `cluster/_optics.py` | Ordering Points To Identify Clustering Structure | `min_samples`, `xi`, `min_cluster_size`, `metric` |
| `Birch` | `cluster/_birch.py` | Balanced Iterative Reducing and Clustering | `threshold`, `branching_factor`, `n_clusters` |
| `SpectralBiclustering` | `cluster/_bicluster.py` | Spectral co-clustering (checkerboard) | `n_clusters`, `method` ('bistochastic'/'scale'/'log'), `n_components` |
| `SpectralCoclustering` | `cluster/_bicluster.py` | Spectral co-clustering (diagonal) | `n_clusters`, `svd_method` ('randomized'/'arpack'), `n_svd_vecs` |
| `AffinityPropagation` | `cluster/_affinity_propagation.py` | Affinity propagation (exemplar-based) | `damping`, `max_iter`, `convergence_iter`, `preference` |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.fit(X)` | 7 nodes | Fit the clustering model |
| `.fit_predict(X)` | 3 nodes | Fit and return labels (single call) |
| `.predict(X)` | 3 nodes | Predict closest cluster for new data |
| `.__init__()` | 11 nodes | Class constructors |
| `.transform(X)` | — | Transform X to cluster-distance space (KMeans, Birch) |
| `.labels_` | — | Cluster labels for training data |
| `.cluster_centers_` | — | Centroid coordinates (KMeans, MeanShift) |
| `.inertia_` | — | Sum of squared distances to centroids (KMeans) |
| `.core_sample_indices_` | — | Core samples (DBSCAN, OPTICS) |
| `.components_` | — | Exemplars (AffinityPropagation, MeanShift) |
| `.children_` | — | Merge tree (AgglomerativeClustering) |

## Common Patterns

```python
# KMeans — fast, scalable baseline for quant regime discovery
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

kmeans = make_pipeline(
    StandardScaler(),
    KMeans(n_clusters=5, n_init='auto', random_state=42, algorithm='elkan')
)
labels = kmeans.fit_predict(X)
inertias = []
for k in range(1, 15):
    km = KMeans(n_clusters=k, n_init='auto', random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
# Elbow method: knee in inertias vs k plot

# DBSCAN — density-based, handles arbitrary shapes + noise
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=10, metric='euclidean', n_jobs=-1)
labels = db.fit_predict(X)
n_noise = (labels == -1).sum()  # -1 = unclustered noise points
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

# HDBSCAN — variable-density, no eps needed
from sklearn.cluster import HDBSCAN
hdb = HDBSCAN(min_cluster_size=15, min_samples=5, metric='euclidean')
labels = hdb.fit_predict(X)
# Access cluster hierarchy
hdb.condensed_tree_  # cluster tree
hdb.single_linkage_tree_  # dendrogram data

# Agglomerative clustering — get full dendrogram
from sklearn.cluster import AgglomerativeClustering
agg = AgglomerativeClustering(
    n_clusters=None, distance_threshold=0, linkage='ward'
)
agg.fit(X)
# agg.children_ contains merge steps for dendrogram

# MiniBatchKMeans for large quant datasets
from sklearn.cluster import MiniBatchKMeans
mbk = MiniBatchKMeans(n_clusters=50, batch_size=1000, random_state=42)
mbk.fit(X_large)  # streams data in batches

# Spectral biclustering for quant factor discovery
from sklearn.cluster import SpectralCoclustering
scc = SpectralCoclustering(n_clusters=4, random_state=42)
scc.fit(X)  # X is features × samples or returns × assets
row_labels = scc.row_labels_
col_labels = scc.column_labels_
```

## Pitfalls

1. **Scale sensitivity**: KMeans, DBSCAN, MeanShift, and SpectralClustering are all distance-based — standardize features first.
2. **KMeans `n_init`**: Old default was 10 with `init='k-means++'`. New default is `'auto'` which uses 1 for efficiency. For quant work, set `n_init=10` explicitly to ensure quality.
3. **DBSCAN `eps` selection**: Use `kneighbors_graph` or nearest-neighbor distance plot to find the elbow. No silver bullet.
4. **DBSCAN memory**: Constructs full pairwise distance matrix for `algorithm='brute'` — use `'ball_tree'` or `'kd_tree'` for large n.
5. **`fit_predict` vs `fit` then `predict`**: KMeans and DBSCAN support both, but DBSCAN's `predict` is approximate and memory-intensive — prefer `fit_predict`.
6. **Birch `threshold`**: Very sensitive; too small = many subclusters/memory blowup, too large = coarse clusters. Tune empirically.
7. **Spectral `affinity='rbf'`**: Requires `gamma` tuning. Try `affinity='nearest_neighbors'` for an automatic alternative.

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `MiniBatchKMeans` (33), `KMeans` (31), `_BaseKMeans` (29) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
