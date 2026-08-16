---
name: scikit-learn-neural-network
description: "Use when working with scikit-learn Neural Networks \u2014 MLPClassifier,\
  \ MLPRegressor, and Bernoulli RBM. Covers core classes, methods, and quant-relevant\
  \ patterns."
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
- neural-network
- mlp
- deep-learning
- classification
- regression
related_skills:
- scikit-learn-model-selection
- scikit-learn-metrics
- scikit-learn-preprocessing
---

# scikit-learn Neural Networks

Extracted from scikit-learn knowledge graph. Source: `sklearn.neural_network` module.
Communities: 81 ("Neural Networks"), 136, 386.

## Quick Reference
| Class/Function | Source File | Purpose | Key Params |
|---------------|-------------|---------|------------|
| `MLPClassifier` | `neural_network/_multilayer_perceptron.py:L879` | Multi-layer Perceptron classifier | `hidden_layer_sizes`, `activation` ('relu'/'tanh'/'logistic'), `alpha`, `batch_size`, `learning_rate`, `max_iter`, `early_stopping` |
| `MLPRegressor` | `neural_network/_multilayer_perceptron.py:L1386` | Multi-layer Perceptron regressor | `hidden_layer_sizes`, `activation`, `alpha`, `batch_size`, `learning_rate`, `max_iter`, `early_stopping` |
| `BernoulliRBM` | `neural_network/_rbm.py:L25` | Restricted Boltzmann Machine (unsupervised) | `n_components`, `learning_rate`, `batch_size`, `n_iter` |
| `BaseMultilayerPerceptron` | `neural_network/_multilayer_perceptron.py:L58` | Abstract base for MLP | — |

### Key Methods (from graph node analysis)

| Method | Prevalence | Description |
|--------|-----------|-------------|
| `.fit(X, y)` | 2 nodes | Train the neural network via backpropagation |
| `.predict(X)` | 1 node | Predict class/value |
| `.predict_proba(X)` | — | Class probabilities (MLPClassifier) |
| `.predict_log_proba(X)` | — | Log-probabilities |
| `.partial_fit(X, y)` | 2 nodes | Online/incremental training (supports `classes` param) |
| `._fit()` | 2 nodes | Internal fit loop (LBFGS or SGD) |
| `._score()` | 2 nodes | Internal scoring (loss or accuracy) |
| `.loss_curve_` | — | Training loss at each iteration |
| `.validation_scores_` | — | Validation scores per iteration (if `early_stopping=True`) |
| `.coefs_` | — | Weight matrices (list of arrays per layer) |
| `.intercepts_` | — | Bias vectors (list of arrays per layer) |

## Common Patterns

```python
# MLP Regression for non-linear quant modeling
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

mlp = make_pipeline(
    StandardScaler(),  # CRITICAL: MLP requires scaled input
    MLPRegressor(
        hidden_layer_sizes=(64, 32),  # two hidden layers
        activation='relu',
        solver='adam',
        alpha=0.001,           # L2 regularization
        batch_size='auto',     # min(200, n_samples)
        learning_rate='adaptive',
        learning_rate_init=0.001,
        max_iter=500,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=20,
        random_state=42,
    )
)
mlp.fit(X_train, y_train)

# Monitor convergence
import matplotlib.pyplot as plt
plt.plot(mlp.named_steps['mlpregressor'].loss_curve_)
plt.title('Training Loss')

# MLP Classification with probability output
from sklearn.neural_network import MLPClassifier
mlpc = make_pipeline(
    StandardScaler(),
    MLPClassifier(
        hidden_layer_sizes=(100, 50),
        activation='relu',
        solver='adam',
        alpha=0.0001,
        max_iter=300,
        early_stopping=True,
        random_state=42
    )
)
mlpc.fit(X_train, y_train)
probas = mlpc.predict_proba(X_test)

# Incremental learning with partial_fit
mlp_inc = MLPRegressor(hidden_layer_sizes=(32,), warm_start=False, max_iter=1)
for batch_X, batch_y in data_batches:
    mlp_inc.partial_fit(batch_X, batch_y)
```

## Pitfalls

1. **Scale sensitivity**: MLP neurons use dot products — unscaled inputs cause vanishing/exploding gradients. Always `StandardScaler` (or `MinMaxScaler` for bounded activations like logistic).
2. **Solver choice**: `adam` works well for most problems. `lbfgs` converges faster on small datasets but uses more memory. `sgd` is slow but allows `partial_fit`.
3. **Overfitting**: MLPs are universal approximators. Use `alpha` (L2), `early_stopping`, and small-ish hidden layers. Monitor `validation_scores_`.
4. **Non-convex optimization**: Different random seeds produce different local minima. For reproducible quant work, always set `random_state`.
5. **Warm start**: `warm_start=True` allows reusing the previous solution when `fit` is called again — useful for progressive training or hyperparameter search.
6. **Classification with `partial_fit`**: You must pass `classes` parameter on the first call so the model knows all possible labels.

## Provenance

- Knowledge graph: scikit-learn, 8450 nodes, 28094 edges, 401 communities
- God nodes: `SGDOptimizer` (32), `BaseMultilayerPerceptron` (31), `AdamOptimizer` (30) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 6f8b95aa2234, backend opencode, description coverage 81%
