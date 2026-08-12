# Edge Audit — optuna

**Date**: 2026-08-12

## Summary

- Total edges: 4252
- EXTRACTED: 3194 (75.1%)
- INFERRED: 1058 (24.9%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `BaseDistribution`: 194 inferred edges
- `Study`: 193 inferred edges
- `StudyDirection`: 137 inferred edges
- `FloatDistribution`: 76 inferred edges
- `CategoricalDistribution`: 71 inferred edges
- `IntDistribution`: 66 inferred edges
- `FrozenStudy`: 60 inferred edges
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
- `pytest_samplers.py` ↔ `distributions.py`: 24
- `_trial.py` ↔ `study.py`: 21
- `acqf.py` ↔ `gp.py`: 16
- `_ped_anova` ↔ `distributions.py`: 16
- `_brute_force.py` ↔ `distributions.py`: 16
- `_transform.py` ↔ `distributions.py`: 16
- `_fixed.py` ↔ `distributions.py`: 16
- `terminator.py` ↔ `erroreval.py`: 15
- `matplotlib` ↔ `study.py`: 13
