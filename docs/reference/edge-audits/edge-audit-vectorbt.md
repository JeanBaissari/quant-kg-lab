# Edge Audit — vectorbt

**Date**: 2026-08-12

## Summary

- Total edges: 9212
- EXTRACTED: 4481 (48.6%)
- INFERRED: 4731 (51.4%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `Config`: 544 inferred edges
- `ArrayWrapper`: 502 inferred edges
- `Wrapping`: 414 inferred edges
- `PlotsBuilderMixin`: 283 inferred edges
- `StatsBuilderMixin`: 283 inferred edges
- `Configured`: 233 inferred edges
- `MappedArray`: 223 inferred edges
- `Drawdowns`: 215 inferred edges
- `RepEval`: 176 inferred edges
- `Ranges`: 168 inferred edges
- `QSAdapter`: 138 inferred edges
- `BaseAccessor`: 114 inferred edges
- `RustSupport`: 112 inferred edges
- `Orders`: 101 inferred edges
- `BaseDFAccessor`: 83 inferred edges
- `BaseSRAccessor`: 83 inferred edges
- `EntryTrades`: 83 inferred edges
- `ExitTrades`: 83 inferred edges
- `Positions`: 83 inferred edges
- `Trades`: 83 inferred edges

## Cross-Module Suspicious Edges

- `accessors.py` ↔ `array_wrapper.py`: 382
- `base.py` ↔ `trades.py`: 308
- `accessors.py` ↔ `splitters.py`: 292
- `base.py` ↔ `array_wrapper.py`: 276
- `accessors.py` ↔ `config.py`: 181
- `base.py` ↔ `config.py`: 174
- `base.py` ↔ `plots_builder.py`: 138
- `base.py` ↔ `stats_builder.py`: 138
- `accessors.py` ↔ `drawdowns.py`: 133
- `accessors.py` ↔ `ranges.py`: 121
- `accessors.py` ↔ `mapped_array.py`: 121
- `dispatch.py` ↔ `_engine.py`: 112
- `mapped_array.py` ↔ `array_wrapper.py`: 78
- `mapped_array.py` ↔ `config.py`: 78
- `base.py` ↔ `drawdowns.py`: 77
- `base.py` ↔ `logs.py`: 77
- `base.py` ↔ `orders.py`: 77
- `base.py` ↔ `qs_adapter.py`: 77
- `base.py` ↔ `template.py`: 77
- `accessors.py` ↔ `plots_builder.py`: 73
