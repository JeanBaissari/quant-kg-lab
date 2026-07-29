---
name: scikit-learn-model-selection
description: Use when working with scikit-learn model selection, cross-validation, hyperparameter tuning, or GridSearchCV/RandomizedSearchCV workflows. Covers train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV, and validation curve analysis.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: scikit-learn/scikit-learn
source_version: main
extraction_date: 2026-07-29
graph_hash: TBD
metadata:
  hermes:
    tags: [scikit-learn, machine-learning, model-selection, cross-validation, hyperparameter-tuning]
    related_skills: [scikit-learn-metrics, scikit-learn-preprocessing, optuna-samplers]
---

# scikit-learn Model Selection

Extracted from scikit-learn knowledge graph. Source: `sklearn.model_selection` module.

## Quick Reference

| Function/Class | Purpose | Key Params |
|---------------|---------|------------|
| `train_test_split` | Split arrays into train/test | `test_size`, `random_state`, `stratify` |
| `cross_val_score` | Evaluate score by CV | `cv`, `scoring`, `n_jobs` |
| `GridSearchCV` | Exhaustive param search | `param_grid`, `cv`, `scoring`, `n_jobs` |
| `RandomizedSearchCV` | Randomized param search | `param_distributions`, `n_iter`, `cv` |
| `cross_validate` | Evaluate multiple metrics | `cv`, `scoring` (dict), `return_train_score` |

## Common Pitfalls

1. **Data leakage in CV**: Always split before scaling. Use `Pipeline` to chain preprocessing + estimator.
2. **GridSearchCV score vs production**: `best_score_` is mean CV score, not holdout/test score.
3. **n_jobs interaction**: `n_jobs=-1` uses all cores but can conflict with BLAS threading.

## Verification Checklist

- [ ] Preprocessing inside Pipeline, not before CV split
- [ ] `scoring` metric matches business objective
- [ ] `random_state` set for reproducibility

## References

- `references/api.md` — Full API surface from knowledge graph
- `references/examples.md` — Extracted from scikit-learn examples/
