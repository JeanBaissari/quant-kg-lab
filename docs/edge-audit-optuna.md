# Edge Audit — optuna

**Date**: 2026-07-29

## Summary

- Total edges: 8405
- EXTRACTED: 7152 (85.1%)
- INFERRED: 1253 (14.9%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `BaseDistribution`: 200 inferred edges
- `Study`: 194 inferred edges
- `StudyDirection`: 148 inferred edges
- `FloatDistribution`: 82 inferred edges
- `CategoricalDistribution`: 77 inferred edges
- `IntDistribution`: 72 inferred edges
- `FrozenStudy`: 60 inferred edges
- `TrialState`: 44 inferred edges
- `LazyRandomState`: 43 inferred edges
- `StudySummary`: 33 inferred edges
- `ArtifactStore`: 14 inferred edges
- `BaseImportanceEvaluator`: 14 inferred edges
- `BaseHeartbeat`: 13 inferred edges
- `ArtifactNotFound`: 12 inferred edges
- `SearchSpace`: 12 inferred edges
- `RandomSampler`: 11 inferred edges
- `TestStudyDirectionModel`: 11 inferred edges
- `TestStudySystemAttributeModel`: 11 inferred edges
- `TestTrialHeartbeatModel`: 11 inferred edges
- `TestTrialIntermediateValueModel`: 11 inferred edges

## Cross-Module Suspicious Edges

- `trial` ↔ `distributions.py`: 134
- `storages` ↔ `study`: 129
- `storages_tests` ↔ `storages`: 93
- `samplers` ↔ `study`: 75
- `storages` ↔ `distributions.py`: 73
- `visualization` ↔ `study`: 63
- `samplers` ↔ `distributions.py`: 62
- `testing` ↔ `distributions.py`: 40
- `study` ↔ `distributions.py`: 32
- `samplers_tests` ↔ `distributions.py`: 25
- `visualization` ↔ `distributions.py`: 21
- `samplers_tests` ↔ `testing`: 20
- `trial` ↔ `study`: 20
- `importance` ↔ `distributions.py`: 19
- `importance_tests` ↔ `testing`: 16
- `_transform.py` ↔ `distributions.py`: 16
- `importance` ↔ `study`: 12
- `_gp` ↔ `distributions.py`: 12
- `pruners` ↔ `study`: 12
- `samplers_tests` ↔ `samplers`: 11
