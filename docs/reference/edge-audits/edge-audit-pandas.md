# Edge Audit — pandas

**Date**: 2026-07-29

## Summary

- Total edges: 40707
- EXTRACTED: 17144 (42.1%)
- INFERRED: 23563 (57.9%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `DatetimeTZDtype`: 1682 inferred edges
- `CategoricalDtype`: 1456 inferred edges
- `PeriodDtype`: 1069 inferred edges
- `StringDtype`: 1012 inferred edges
- `ArrowDtype`: 999 inferred edges
- `IntervalDtype`: 846 inferred edges
- `WriteBuffer`: 773 inferred edges
- `DataFrame`: 697 inferred edges
- `Series`: 511 inferred edges
- `ReadBuffer`: 480 inferred edges
- `Accessor`: 478 inferred edges
- `MultiIndex`: 432 inferred edges
- `BaseMaskedDtype`: 418 inferred edges
- `OpsMixin`: 404 inferred edges
- `SequenceNotStr`: 371 inferred edges
- `RangeIndex`: 365 inferred edges
- `SparseDtype`: 347 inferred edges
- `FrozenList`: 320 inferred edges
- `ArrowExtensionArray`: 319 inferred edges
- `ExtensionArray`: 314 inferred edges

## Cross-Module Suspicious Edges

- `indexes` ↔ `dtypes`: 1509
- `arrays` ↔ `dtypes`: 960
- `frame.py` ↔ `dtypes`: 845
- `frame.py` ↔ `_typing.py`: 845
- `indexes` ↔ `arrays`: 822
- `frame.py` ↔ `formats`: 676
- `internals` ↔ `dtypes`: 565
- `frame.py` ↔ `stata.py`: 507
- `pytables.py` ↔ `dtypes`: 486
- `generic.py` ↔ `formats`: 472
- `series.py` ↔ `_typing.py`: 396
- `window` ↔ `indexers`: 371
- `generic.py` ↔ `_typing.py`: 354
- `indexes` ↔ `formats`: 354
- `frame.py` ↔ `arrays`: 338
- `frame.py` ↔ `interchange`: 338
- `formats` ↔ `_typing.py`: 326
- `pytables.py` ↔ `computation`: 324
- `dtypes` ↔ `arrays`: 276
- `indexing.py` ↔ `dtypes`: 256
