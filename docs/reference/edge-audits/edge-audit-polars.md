# Edge Audit — polars

**Date**: 2026-08-13

## Summary

- Total edges: 16925
- EXTRACTED: 6604 (39.0%)
- INFERRED: 10321 (61.0%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `CompatLevel`: 525 inferred edges
- `sphinx_accessor`: 502 inferred edges
- `ModuleUpgradeRequiredError`: 455 inferred edges
- `ShapeError`: 433 inferred edges
- `QueryOptFlags`: 345 inferred edges
- `ComputeError`: 313 inferred edges
- `Schema`: 296 inferred edges
- `ArrowSchemaExportable`: 273 inferred edges
- `InvalidOperationError`: 269 inferred edges
- `PartitionBy`: 265 inferred edges
- `SeriesBuffers`: 253 inferred edges
- `ExprMetaNameSpace`: 228 inferred edges
- `ExprStringNameSpace`: 228 inferred edges
- `CustomUFuncWarning`: 227 inferred edges
- `OutOfBoundsError`: 227 inferred edges
- `ExprBinaryNameSpace`: 227 inferred edges
- `ExprCatNameSpace`: 227 inferred edges
- `ExprDateTimeNameSpace`: 227 inferred edges
- `ExprExtensionNameSpace`: 227 inferred edges
- `ExprNameNameSpace`: 227 inferred edges

## Cross-Module Suspicious Edges

- `frame.py` ↔ `exceptions.py`: 1337
- `series.py` ↔ `exceptions.py`: 753
- `frame.py` ↔ `group_by.py`: 489
- `expr.py` ↔ `exceptions.py`: 454
- `convert.py` ↔ `classes.py`: 320
- `frame.py` ↔ `protocol.py`: 261
- `frame.py` ↔ `partition.py`: 261
- `frame.py` ↔ `opt_flags.py`: 261
- `frame.py` ↔ `schema.py`: 261
- `frame.py` ↔ `_typing.py`: 261
- `series.py` ↔ `protocol.py`: 251
- `series.py` ↔ `_typing.py`: 251
- `series.py` ↔ `various.py`: 251
- `expr.py` ↔ `binary.py`: 227
- `expr.py` ↔ `categorical.py`: 227
- `expr.py` ↔ `datetime.py`: 227
- `expr.py` ↔ `ext.py`: 227
- `expr.py` ↔ `meta.py`: 227
- `expr.py` ↔ `name.py`: 227
- `expr.py` ↔ `string.py`: 227
