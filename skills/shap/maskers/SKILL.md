---
name: shap-maskers
description: "Use when shaping model inputs for SHAP \u2014 Tabular/Image/Partition/Composite\
  \ maskers, background datasets, and how masking defines what SHAP values mean."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: shap/shap
source_commit: df974a1966294b9c7acebb1373fd6dc5445d1d3d
extraction_date: 2026-08-12
graph:
  nodes: 1277
  edges: 1752
  community_count: 108
  graph_hash: 56d741979f6b195b
tags:
- shap
- maskers
- background-data
- explainability
related_skills:
- shap
- shap-explainers
- shap-plots
- scikit-learn-ensemble
- xgboost-core
- lightgbm-core
target_version: '0.52.0 (dev: after 0.52.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `shap` ahead of the latest PyPI release (0.52.0 (dev: after 0.52.0)). Some APIs may not exist in your installed version.

# shap.maskers

Maskers tell an explainer how to hide (mask) parts of the input — and what
"absent" means. The choice of masker + background data defines the exact
counterfactual being evaluated, so it determines the meaning of every SHAP
value you report.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `Masker` | `maskers/_masker.py:L14` | Base masker — `__call__(mask, *args)` applies a mask to inputs |
| `Tabular` | `maskers/_tabular.py:L19` | Tabular masker — Independent (marginalize) or Partition (tree-correlated) masking |
| `Image` | `maskers/_image.py:L16` | Image masker — blur/inpaint masked regions |
| `Composite` | `maskers/_composite.py:L10` | Composite masker — different maskers for different input groups |
| `OutputComposite` | `maskers/_output_composite.py:L5` | Maps the masker to the model output (e.g. softmax outputs) |
| `Fixed` | `maskers/_fixed.py:L11` | No-op masker — fixed reference input |
| `FixedComposite` | `maskers/_fixed_composite.py:L7` | Fixed masker over a composite structure |
| `joint_clustering()` | `maskers/_composite.py:L133` | Build a clustering for Partition masking from data |
| `Masker.save()` / `.load()` | `maskers/_masker.py:L14` | Persist maskers (e.g. for a model card) |

## Common Patterns

- **Tree models**: `masker = shap.maskers.Tabular(X, max_samples=100, clustering="correlation")` —
  Partition masking with a correlation clustering matches how tree models split.
- **Independent masking**: default `Tabular(X)` — features are marginalized
  independently; the classic SHAP interventional assumption.
- **Partition clustering**: `masker.clustering` — pass to TreeExplainer for
  dependent-feature SHAP; `joint_clustering()` builds it from data.
- **Background sampling**: keep `max_samples` small (100–1000 rows); the
  background distribution, not its size, matters.
- **Multi-input models**: `Composite` maskers — one masker per model input
  (e.g. numeric features + text/categorical).
- **Image models**: `shap.maskers.Image("blur(128,128)")` — inpaint masked
  image regions instead of dropping pixels.

## Pitfalls

- **Background leakage**: fitting the background on the training set then
  explaining test rows is correct; fitting it on the explained rows leaks
  information into the base value.
- **Independent vs Partition**: results differ systematically for correlated
  features (e.g. momentum factors) — Partition matches tree behavior,
  Independent matches the interventional contract. Report which you used.
- **max_samples too large**: sampling cost scales with background size —
  large backgrounds slow Kernel/Partition explainers quadratically-ish.
- **Composite order**: maskers must be listed in the same order as the model's
  inputs — a mismatch silently explains the wrong tensor.
- **Image masker shapes**: `blur(w,h)` argument order matters — verify against
  the input tensor shape.

## Provenance

Graph: `knowledge_graphs/shap/.graphify/graph.json` — 1277 nodes · 1752 edges ·
108 communities · graphify @ df974a196629, backend opencode, description coverage 80.1%;
122 curated nodes cover the Cython/C++ core (ADR-0008).

## Verification Checklist

- [ ] `shap.maskers.Tabular(X, max_samples=100)` feeds a TreeExplainer
- [ ] `masker.clustering` populated when `clustering="correlation"` is set
- [ ] QR rows cite `maskers/*.py` files resolvable in the shap graph
