# Edge Audit — vectorbt

**Date**: 2026-07-29

## Summary

- Total edges: 13588
- EXTRACTED: 8019 (59.0%)
- INFERRED: 5569 (41.0%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Config`: 539 inferred edges
- `ArrayWrapper`: 497 inferred edges
- `Wrapping`: 410 inferred edges
- `PlotsBuilderMixin`: 279 inferred edges
- `StatsBuilderMixin`: 279 inferred edges
- `MappedArray`: 219 inferred edges
- `Drawdowns`: 212 inferred edges
- `Configured`: 202 inferred edges
- `RepEval`: 174 inferred edges
- `Ranges`: 165 inferred edges
- `QSAdapter`: 137 inferred edges
- `BaseAccessor`: 112 inferred edges
- `RustSupport`: 112 inferred edges
- `Orders`: 100 inferred edges
- `Bar`: 95 inferred edges
- `Box`: 95 inferred edges
- `Gauge`: 95 inferred edges
- `Heatmap`: 95 inferred edges
- `Histogram`: 95 inferred edges
- `Scatter`: 95 inferred edges

## Cross-Module Suspicious Edges

- `test_plotting.py` ↔ `generic`: 752
- `generic` ↔ `base`: 414
- `portfolio` ↔ `generic`: 250
- `portfolio` ↔ `utils`: 208
- `test_plotting.py` ↔ `utils`: 188
- `portfolio` ↔ `base`: 181
- `generic` ↔ `utils`: 177
- `records` ↔ `base`: 168
- `records` ↔ `utils`: 150
- `records` ↔ `generic`: 148
- `returns` ↔ `base`: 120
- `signals` ↔ `utils`: 116
- `generic` ↔ `records`: 106
- `indicators` ↔ `base`: 93
- `base` ↔ `utils`: 83
- `portfolio` ↔ `returns`: 76
- `returns` ↔ `utils`: 66
- `indicators` ↔ `generic`: 62
- `indicators` ↔ `utils`: 62
- `returns` ↔ `generic`: 60
