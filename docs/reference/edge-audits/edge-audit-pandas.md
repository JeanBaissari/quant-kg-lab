# Edge Audit — pandas

**Date**: 2026-07-29

## Summary

- Total edges: 69899
- EXTRACTED: 54636 (78.2%)
- INFERRED: 15263 (21.8%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `StringDtype`: 1007 inferred edges
- `WriteBuffer`: 736 inferred edges
- `DataFrame`: 658 inferred edges
- `Series`: 500 inferred edges
- `Accessor`: 467 inferred edges
- `ReadBuffer`: 463 inferred edges
- `MultiIndex`: 425 inferred edges
- `OpsMixin`: 401 inferred edges
- `SequenceNotStr`: 362 inferred edges
- `RangeIndex`: 356 inferred edges
- `ArrowExtensionArray`: 321 inferred edges
- `ExtensionArray`: 317 inferred edges
- `FrozenList`: 315 inferred edges
- `ArrowArrayExportable`: 295 inferred edges
- `ArrowStreamExportable`: 295 inferred edges
- `NDArrayBackedExtensionArray`: 293 inferred edges
- `BaseIndexer`: 287 inferred edges
- `Resampler`: 248 inferred edges
- `WriteExcelBuffer`: 235 inferred edges
- `NumpyExtensionArray`: 210 inferred edges

## Cross-Module Suspicious Edges

- `core` ↔ `io`: 1711
- `core` ↔ `_typing.py`: 1555
- `io` ↔ `core`: 1005
- `io` ↔ `_typing.py`: 953
- `core` ↔ `benchmarks`: 302
- `tests` ↔ `core`: 256
- `errors` ↔ `_config`: 84
- `tests` ↔ `io`: 61
- `_testing` ↔ `core`: 47
- `_typing.py` ↔ `core`: 36
- `api` ↔ `core`: 20
- `tests` ↔ `benchmarks`: 19
- `tests` ↔ `tseries`: 16
- `benchmarks` ↔ `plotting`: 13
- `_typing.py` ↔ `tseries`: 11
- `tseries` ↔ `core`: 10
- `_typing.py` ↔ `io`: 9
- `api` ↔ `io`: 6
- `tests` ↔ `plotting`: 3
- `_testing` ↔ `_typing.py`: 3
