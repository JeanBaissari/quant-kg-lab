---
name: scikit-learn-tree
description: Use when working with scikit-learn Decision Trees — classification, regression, visualization, and export. Covers core classes, methods, and quant-relevant patterns.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_version: main
extraction_date: 2026-07-29
graph_hash: 18753_nodes_49978_edges
metadata:
  hermes:
    tags: [scikit-learn, machine-learning, decision-tree, cart, visualization]
    related_skills: [scikit-learn-ensemble, scikit-learn-model-selection, scikit-learn-metrics]
---

# scikit-learn Decision Trees

Extracted from scikit-learn knowledge graph. Source: `sklearn.tree` module.
Communities: 176 ("Decision Trees"), 0 ("Linear Models + DecisionTreeClassifier/Regressor").

## Quick Reference

| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `DecisionTreeClassifier` | `tree/_classes.py` | CART classification tree | `criterion` ('gini'/'entropy'), `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features`, `class_weight` |
| `DecisionTreeRegressor` | `tree/_classes.py` | CART regression tree | `criterion` ('squared_error'/'friedman_mse'/'absolute_error'), `max_depth`, `min_samples_split`, `min_samples_leaf` |
| `ExtraTreeClassifier` | `tree/_classes.py` | Extremely randomized classification tree | `max_features`, `max_depth`, `min_samples_split` |
| `ExtraTreeRegressor` | `tree/_classes.py` | Extremely randomized regression tree | `max_features`, `max_depth`, `min_samples_split` |
| `BaseDecisionTree` | `tree/_classes.py` | Abstract base for all tree classes | — |
| `export_graphviz` | `tree/_export.py` | Export tree to Graphviz DOT format | `decision_tree`, `feature_names`, `class_names`, `filled`, `rounded` |
| `plot_tree` | `tree/_export.py` | Render tree inline (matplotlib) | `decision_tree`, `feature_names`, `class_names`, `filled`, `fontsize` |
| `export_text` | `tree/_export.py` | Export tree as plain text | `decision_tree`, `feature_names`, `spacing`, `decimals` |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.fit(X, y)` | 11 nodes | Train the decision tree |
| `.predict(X)` | 9 nodes | Predict class/value |
| `.predict_proba(X)` | 3 nodes | Class probabilities |
| `.predict_log_proba(X)` | 3 nodes | Log-probabilities (more stable) |
| `.apply(X)` | 2 nodes | Return leaf index for each sample |
| `.decision_path(X)` | 2 nodes | Return sparse matrix of decision paths |
| `.feature_importances_` | — | Normalized total reduction of criterion (Gini importance) |
| `.get_depth()` | — | Maximum depth of the tree |
| `.get_n_leaves()` | — | Number of leaves |
| `.cost_complexity_pruning_path()` | — | Get alpha values and impurities for pruning |

## Common Patterns

```python
# Decision Tree Regression — interpretable quant baseline
from sklearn.tree import DecisionTreeRegressor, plot_tree
dt = DecisionTreeRegressor(
    max_depth=5,
    min_samples_leaf=20,    # prevent overfitting on small nodes
    min_samples_split=50,
    random_state=42
)
dt.fit(X_train, y_train)

# Inspect tree structure
print(f"Depth: {dt.get_depth()}, Leaves: {dt.get_n_leaves()}")
importances = dt.feature_importances_
leaf_indices = dt.apply(X_test)  # which leaf each sample falls into

# Cost-complexity pruning — find optimal alpha
path = dt.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas

# Classification with class weights for imbalanced quant data
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(
    max_depth=4,
    class_weight='balanced',
    min_samples_leaf=10,
    random_state=42
)
dtc.fit(X_train, y_train)
probas = dtc.predict_proba(X_test)  # shape (n_samples, n_classes)

# Visualize
from sklearn.tree import export_graphviz
export_graphviz(dtc, feature_names=feature_names, filled=True, rounded=True,
                out_file='tree.dot')
# Or inline
plot_tree(dtc, feature_names=feature_names, filled=True)
```

## Pitfalls

1. **Overfitting**: Decision trees can perfectly memorize training data. Always constrain with `max_depth`, `min_samples_leaf`, or cost-complexity pruning.
2. **Instability**: Small data perturbations can produce entirely different trees. For quant applications, ensemble methods (RF, GBDT) are typically preferred.
3. **Feature importance bias**: Gini importance favors high-cardinality features and continuous features over categorical ones. Use permutation importance from `sklearn.inspection` for unbiased estimates.
4. **`predict_proba` smoothing**: Class probabilities are computed as the fraction of samples in each leaf — no smoothing. Small leaves produce extreme probabilities (0 or 1).
5. **Memory with deep trees**: A fully-grown tree on large data can have millions of nodes. Set `max_leaf_nodes` to bound memory.
6. **`decision_path` output**: Returns a sparse CSR matrix — use `.toarray()` or `.nonzero()` to extract paths per sample.

## References

- `references/api.md` — Full API surface from knowledge graph
- Communities 176, 0: 779 total graph nodes (412 code, 367 rationale)
- Source files: `sklearn/tree/_classes.py` (33 nodes), `_export.py` (26), `_reingold_tilford.py` (18)
