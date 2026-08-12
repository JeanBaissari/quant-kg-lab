# Edge Audit — optuna

**Date**: 2026-08-12

## Summary

- Total edges: 4010
- EXTRACTED: 3000 (74.8%)
- INFERRED: 1010 (25.2%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Study`: 187 inferred edges
- `BaseDistribution`: 183 inferred edges
- `StudyDirection`: 135 inferred edges
- `CategoricalDistribution`: 63 inferred edges
- `FloatDistribution`: 63 inferred edges
- `IntDistribution`: 60 inferred edges
- `FrozenStudy`: 58 inferred edges
- `TrialState`: 41 inferred edges
- `LazyRandomState`: 37 inferred edges
- `StudySummary`: 34 inferred edges
- `BaseImportanceEvaluator`: 14 inferred edges
- `BaseHeartbeat`: 13 inferred edges
- `ArtifactStore`: 12 inferred edges
- `SearchSpace`: 12 inferred edges
- `RandomSampler`: 10 inferred edges
- `ArtifactNotFound`: 8 inferred edges
- `ConditionalGPRegressor`: 8 inferred edges
- `GPRegressor`: 8 inferred edges
- `NSGAIIISampler`: 8 inferred edges
- `Multi-objective sampler using the NSGA-III algorithm.      NSGA-III stands for "`: 8 inferred edges

## Cross-Module Suspicious Edges

- `_trial.py` ↔ `distributions.py`: 84
- `_base.py` ↔ `distributions.py`: 43
- `_frozen.py` ↔ `distributions.py`: 36
- `study.py` ↔ `distributions.py`: 33
- `study.py` ↔ `_study_direction.py`: 33
- `study.py` ↔ `_study_summary.py`: 33
- `_rdb` ↔ `distributions.py`: 32
- `nsgaii` ↔ `study.py`: 30
- `_base.py` ↔ `_frozen.py`: 30
- `_base.py` ↔ `_study_direction.py`: 30
- `_rdb` ↔ `_study_direction.py`: 24
- `_trial.py` ↔ `study.py`: 21
- `acqf.py` ↔ `gp.py`: 16
- `_ped_anova` ↔ `distributions.py`: 16
- `_brute_force.py` ↔ `distributions.py`: 16
- `_transform.py` ↔ `distributions.py`: 16
- `_fixed.py` ↔ `distributions.py`: 16
- `terminator.py` ↔ `erroreval.py`: 15
- `matplotlib` ↔ `study.py`: 13
- `search_space.py` ↔ `distributions.py`: 12
