# Edge Audit — arch

**Date**: 2026-08-13

## Summary

- Total edges: 3895
- EXTRACTED: 1714 (44.0%)
- INFERRED: 2181 (56.0%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `AbstractDocStringInheritor`: 246 inferred edges
- `Normal`: 171 inferred edges
- `ConstantVariance`: 111 inferred edges
- `VolatilityProcess`: 111 inferred edges
- `Distribution`: 108 inferred edges
- `ConvergenceWarning`: 72 inferred edges
- `DataScaleWarning`: 72 inferred edges
- `StartingValueWarning`: 72 inferred edges
- `WaldTestStatistic`: 72 inferred edges
- `Substitution`: 67 inferred edges
- `InitialValueWarning`: 63 inferred edges
- `ValueWarning`: 63 inferred edges
- `DocStringInheritor`: 60 inferred edges
- `InfeasibleTestException`: 55 inferred edges
- `InvalidLengthWarning`: 55 inferred edges
- `PerformanceWarning`: 55 inferred edges
- `CovarianceEstimator`: 43 inferred edges
- `APARCH`: 39 inferred edges
- `ARCH`: 39 inferred edges
- `EGARCH`: 39 inferred edges

## Cross-Module Suspicious Edges

- `mean.py` ↔ `volatility.py`: 280
- `base.py` ↔ `exceptions.py`: 250
- `mean.py` ↔ `distribution.py`: 175
- `unitroot.py` ↔ `exceptions.py`: 165
- `base.py` ↔ `distribution.py`: 144
- `base.py` ↔ `volatility.py`: 144
- `volatility.py` ↔ `exceptions.py`: 126
- `multiple_comparison.py` ↔ `base.py`: 78
- `base.py` ↔ `testing.py`: 72
- `mean.py` ↔ `recursions_python.py`: 70
- `cointegration.py` ↔ `kernel.py`: 66
- `cointegration.py` ↔ `_phillips_ouliaris.py`: 66
- `cointegration.py` ↔ `_decorators.py`: 66
- `volatility.py` ↔ `distribution.py`: 63
- `volatility.py` ↔ `array.py`: 63
- `unitroot.py` ↔ `array.py`: 55
- `distribution.py` ↔ `array.py`: 36
- `mean.py` ↔ `array.py`: 35
- `base.py` ↔ `array.py`: 34
- `kernel.py` ↔ `array.py`: 34
