---
name: quant-explainability
description: "Use when explaining a fitted quant model — choosing the right SHAP explainer, global and local attribution views, interaction analysis, and the sanity checks that make explanations trustworthy."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [shap-explainers, shap-plots, shap-maskers, xgboost-core, lightgbm-core, scikit-learn-ensemble, quant-factor-importance]
tags: [quantitative-finance, explainability, shap, feature-importance, model-interpretation, workflow]
related_skills: [shap-explainers, shap-plots, shap-maskers, xgboost-core, lightgbm-core, scikit-learn-ensemble, quant-factor-importance]
target_version: cross-lib
---

# Quant Explainability (model → explainer → global attribution → local drill-down → trust)

Explainability answers "which features drive this model's predictions, globally and for
specific rows?" — the bridge between a fitted black box and the factor thesis an analyst can
defend. SHAP gives exact per-feature attributions when the model is a tree ensemble.

## Steps

1. **Fix the masker & background first** — `shap-maskers`: the masker defines what
   "absent" means — decide it once per model version:
   ```python
   masker = shap.maskers.Tabular(X_train, max_samples=100, clustering="correlation")
   ```
2. **Choose the explainer** — `shap-explainers`: `TreeExplainer` (exact, fast — the default
   for xgboost/lightgbm/sklearn trees), `LinearExplainer` for linear models,
   `KernelExplainer` only for non-tree models.
   ```python
   explainer = shap.TreeExplainer(model, masker)
   exp = explainer(X_test)
   ```
3. **Verify additivity** — `shap-explainers`: `explainer.assert_additivity()` — if values
   don't sum to predictions, the explanation is broken (model/version mismatch).
4. **Global view** — `shap-plots`: `shap.beeswarm(exp)` — feature importance + direction
   in one plot; `shap.bar_plot(exp)` for the headline numbers.
5. **Local drill-down** — `shap-plots`: `shap.waterfall_plot(exp[0])` for single rows;
   `shap.decision_plot(...)` to compare many rows on one additive scale.
6. **Interactions** — `shap-explainers`: `TreeExplainer(model).shap_interaction_values(X)`
   + `shap.dependence_plot("f_a", ..., interaction_index="f_b")` — which feature pairs
   co-drive predictions.
7. **Sanity vs factor thesis** — `quant-factor-importance`: compare SHAP ordering with
   permutation importance and the factor thesis — a model whose top SHAP features are
   unexpected deserves a look, not trust.

## Pitfalls

1. **Explainers are not interchangeable**: TreeExplainer ≠ KernelExplainer values — pin the
   explainer per model and document it; mixing variants across reports breaks comparisons.
2. **Background leakage**: fit the background on the training set, not the explained rows.
3. **Tree limit**: boosted ensembles with early stopping need `tree_limit` matching the
   deployed model, or the explanation is for a different model than the one trading.
4. **Correlated features**: Independent masking marginalizes independently — Partition
   masking (via clustering) matches tree behavior; report which contract you used.
5. **Additivity is mandatory**: if `assert_additivity()` fails, stop — the SHAP values are
   not trustworthy and likely the model/masker combo is wrong.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| masking | `shap-maskers` | background + clustering |
| explainer | `shap-explainers` | TreeExplainer (explains) |
| verification | `shap-explainers` | assert_additivity |
| global | `shap-plots` | beeswarm/bar |
| local | `shap-plots` | waterfall/decision |
| interactions | `shap-explainers` | shap_interaction_values |
| cross-check | `quant-factor-importance` | permutation vs SHAP ordering |
| models | `xgboost-core`, `lightgbm-core`, `scikit-learn-ensemble` | explainable model surface |
