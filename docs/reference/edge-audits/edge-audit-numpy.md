# Edge Audit — numpy

**Date**: 2026-07-29

## Summary

- Total edges: 30581
- EXTRACTED: 28378 (92.8%)
- INFERRED: 2203 (7.2%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `AxisError`: 414 inferred edges
- `Benchmark`: 205 inferred edges
- `ABCPolyBase`: 178 inferred edges
- `ComplexWarning`: 168 inferred edges
- `CommaDecimalPointLocale`: 114 inferred edges
- `MaskedArray`: 107 inferred edges
- `MAError`: 69 inferred edges
- `LineSplitter`: 49 inferred edges
- `NameValidator`: 49 inferred edges
- `StringConverter`: 49 inferred edges
- `VisibleDeprecationWarning`: 48 inferred edges
- `ndindex`: 47 inferred edges
- `AxisConcatenator`: 45 inferred edges
- `ConversionWarning`: 44 inferred edges
- `ConverterError`: 44 inferred edges
- `errstate`: 31 inferred edges
- `DummyArray`: 28 inferred edges
- `DTypePromotionError`: 25 inferred edges
- `DataSource`: 25 inferred edges
- `ConverterLockError`: 25 inferred edges

## Cross-Module Suspicious Edges

- `_core` ↔ `exceptions.py`: 418
- `matrixlib` ↔ `linalg`: 192
- `lib` ↔ `exceptions.py`: 155
- `ma` ↔ `lib`: 62
- `linalg` ↔ `exceptions.py`: 61
- `_core` ↔ `lib`: 28
- `ma` ↔ `exceptions.py`: 24
- `lib` ↔ `matrixlib`: 14
- `random` ↔ `exceptions.py`: 12
- `lib` ↔ `ma`: 10
- `matlib.py` ↔ `matrixlib`: 8
- `benchmarks` ↔ `_core`: 7
- `__init__.py` ↔ `_pytesttester.py`: 6
- `matrixlib` ↔ `ma`: 4
- `ma` ↔ `_core`: 4
- `core` ↔ `_core`: 2
- `f2py` ↔ `exceptions.py`: 2
- `f2py` ↔ `_pytesttester.py`: 2
- `polynomial` ↔ `_pytesttester.py`: 2
- `random` ↔ `_pytesttester.py`: 2
