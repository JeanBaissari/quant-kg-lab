# Edge Audit — imbalanced-learn

**Date**: 2026-08-13

## Summary

- Total edges: 865
- EXTRACTED: 705 (81.5%)
- INFERRED: 160 (18.5%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `InputTags`: 24 inferred edges
- `BaseSampler`: 20 inferred edges
- `ValueDifferenceMetric`: 18 inferred edges
- `Pipeline`: 17 inferred edges
- `SamplerTags`: 16 inferred edges
- `Tags`: 16 inferred edges
- `ArraysTransformer`: 15 inferred edges
- `SamplerMixin`: 10 inferred edges
- `The :mod:`imblearn.under_sampling.prototype_selection` submodule contains method`: 10 inferred edges
- `FunctionSampler`: 9 inferred edges
- `EditedNearestNeighbours`: 5 inferred edges
- `TomekLinks`: 5 inferred edges
- `Base class for sampling`: 4 inferred edges
- `Base method defined in each sampler to defined the sampling         strategy.`: 4 inferred edges
- `Base class for sampling algorithms.      Warning: This class should not be used`: 4 inferred edges
- `Check inputs and statistics of the sampler.          You should use ``fit_resamp`: 4 inferred edges
- `Resample the dataset.          Parameters         ----------         X : {array-`: 4 inferred edges
- `Return True if the given estimator is a sampler, False otherwise.      Parameter`: 4 inferred edges
- `Construct a sampler from calling an arbitrary callable.      Read more in the :r`: 4 inferred edges
- `Check inputs and statistics of the sampler.          You should use ``fit_resamp`: 4 inferred edges

## Cross-Module Suspicious Edges

- `base.py` ↔ `_tags.py`: 45
- `_smote` ↔ `pairwise.py`: 18
- `base.py` ↔ `_validation.py`: 15
- `_easy_ensemble.py` ↔ `pipeline.py`: 7
- `_bagging.py` ↔ `pipeline.py`: 6
- `testing.py` ↔ `base.py`: 6
- `__init__.py` ↔ `base.py`: 5
- `_smote_enn.py` ↔ `base.py`: 4
- `_smote_tomek.py` ↔ `base.py`: 4
- `_test_common` ↔ `pipeline.py`: 4
- `__init__.py` ↔ `_smote_enn.py`: 1
- `__init__.py` ↔ `_smote_tomek.py`: 1
- `__init__.py` ↔ `_bagging.py`: 1
- `__init__.py` ↔ `_easy_ensemble.py`: 1
- `__init__.py` ↔ `_forest.py`: 1
- `__init__.py` ↔ `_weight_boosting.py`: 1
- `__init__.py` ↔ `_generator.py`: 1
- `__init__.py` ↔ `_split.py`: 1
- `__init__.py` ↔ `_adasyn.py`: 1
- `__init__.py` ↔ `_random_over_sampler.py`: 1
