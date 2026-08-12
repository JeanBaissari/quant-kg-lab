# Edge Audit — numpy

**Date**: 2026-08-12

## Summary

- Total edges: 13271
- EXTRACTED: 12560 (94.6%)
- INFERRED: 711 (5.4%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `ABCPolyBase`: 184 inferred edges
- `AxisConcatenator`: 45 inferred edges
- `MAError`: 45 inferred edges
- `MaskedArray`: 45 inferred edges
- `errstate`: 31 inferred edges
- `AxisError`: 31 inferred edges
- `ndindex`: 29 inferred edges
- `DTypePromotionError`: 27 inferred edges
- `DataSource`: 25 inferred edges
- `ConversionWarning`: 25 inferred edges
- `ConverterError`: 25 inferred edges
- `ConverterLockError`: 25 inferred edges
- `LineSplitter`: 25 inferred edges
- `NameValidator`: 25 inferred edges
- `StringConverter`: 25 inferred edges
- `matrix`: 22 inferred edges
- `PytestTester`: 21 inferred edges
- `RankWarning`: 19 inferred edges
- `looper`: 13 inferred edges
- `A sub-package for efficiently dealing with polynomials.  Within the documentatio`: 8 inferred edges

## Cross-Module Suspicious Edges

- `_npyio_impl.py` ↔ `_iotools.py`: 150
- `extras.py` ↔ `core.py`: 90
- `extras.py` ↔ `_index_tricks_impl.py`: 45
- `chebyshev.py` ↔ `_polybase.py`: 38
- `numeric.py` ↔ `_ufunc_config.py`: 31
- `numeric.py` ↔ `exceptions.py`: 31
- `hermite_e.py` ↔ `_polybase.py`: 30
- `hermite.py` ↔ `_polybase.py`: 30
- `laguerre.py` ↔ `_polybase.py`: 29
- `legendre.py` ↔ `_polybase.py`: 29
- `_internal.py` ↔ `exceptions.py`: 27
- `polynomial.py` ↔ `_polybase.py`: 26
- `_npyio_impl.py` ↔ `_datasource.py`: 25
- `__init__.py` ↔ `_pytesttester.py`: 21
- `_polynomial_impl.py` ↔ `exceptions.py`: 19
- `_arraypad_impl.py` ↔ `_index_tricks_impl.py`: 15
- `_shape_base_impl.py` ↔ `_index_tricks_impl.py`: 14
- `_shape_base_impl.py` ↔ `defmatrix.py`: 14
- `matlib.py` ↔ `defmatrix.py`: 8
- `__init__.py` ↔ `records.py`: 2
