# Edge Audit — ta

**Date**: 2026-08-13

## Summary

- Total edges: 1207
- EXTRACTED: 658 (54.5%)
- INFERRED: 549 (45.5%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `IndicatorMixin`: 255 inferred edges
- `.. module:: wrapper    :synopsis: Wrapper of Indicators.  .. moduleauthor:: Dari`: 42 inferred edges
- `Add volatility technical analysis features to dataframe.      Args:         df (`: 42 inferred edges
- `Add trend technical analysis features to dataframe.      Args:         df (panda`: 42 inferred edges
- `Add trend technical analysis features to dataframe.      Args:         df (panda`: 42 inferred edges
- `Add others analysis features to dataframe.      Args:         df (pandas.core.fr`: 42 inferred edges
- `Add all technical analysis features to dataframe.      Args:         df (pandas.`: 42 inferred edges
- `Add volume technical analysis features to dataframe.      Args:         df (pand`: 42 inferred edges
- `AwesomeOscillatorIndicator`: 8 inferred edges
- `KAMAIndicator`: 8 inferred edges
- `PercentagePriceOscillator`: 8 inferred edges
- `PercentageVolumeOscillator`: 8 inferred edges
- `ROCIndicator`: 8 inferred edges
- `RSIIndicator`: 8 inferred edges
- `StochasticOscillator`: 8 inferred edges
- `StochRSIIndicator`: 8 inferred edges
- `TSIIndicator`: 8 inferred edges
- `UltimateOscillator`: 8 inferred edges
- `WilliamsRIndicator`: 8 inferred edges
- `CumulativeReturnIndicator`: 8 inferred edges

## Cross-Module Suspicious Edges

- `wrapper.py` ↔ `trend.py`: 98
- `trend.py` ↔ `utils.py`: 91
- `wrapper.py` ↔ `momentum.py`: 77
- `wrapper.py` ↔ `volume.py`: 63
- `momentum.py` ↔ `utils.py`: 59
- `volatility.py` ↔ `utils.py`: 53
- `volume.py` ↔ `utils.py`: 39
- `wrapper.py` ↔ `volatility.py`: 35
- `wrapper.py` ↔ `others.py`: 21
- `others.py` ↔ `utils.py`: 13
