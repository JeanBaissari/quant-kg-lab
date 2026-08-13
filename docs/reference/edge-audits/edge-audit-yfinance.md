# Edge Audit — yfinance

**Date**: 2026-08-13

## Summary

- Total edges: 1584
- EXTRACTED: 1181 (74.6%)
- INFERRED: 403 (25.4%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `YfData`: 102 inferred edges
- `YFDataException`: 88 inferred edges
- `YFException`: 57 inferred edges
- `YFRateLimitError`: 37 inferred edges
- `Domain`: 22 inferred edges
- `WebSocket`: 20 inferred edges
- `YFEarningsDateMissing`: 19 inferred edges
- `Search`: 18 inferred edges
- `frozendict`: 17 inferred edges
- `YFNotImplementedError`: 16 inferred edges
- `TickerBase`: 7 inferred edges
- `Returns a DataFrame with the recommendations         Columns: period  strongBuy`: 5 inferred edges
- `Valuation measures (market cap, P/E, P/S, P/B, EV/EBITDA, ...).          Returns`: 5 inferred edges
- `Keys:   current  low  high  mean  median`: 5 inferred edges
- `Index:      0q  +1q  0y  +1y         Columns:    numberOfAnalysts  avg  low  hig`: 5 inferred edges
- `Index:      0q  +1q  0y  +1y         Columns:    numberOfAnalysts  avg  low  hig`: 5 inferred edges
- `Index:      pd.DatetimeIndex         Columns:    epsEstimate  epsActual  epsDiff`: 5 inferred edges
- `Index:      0q  +1q  0y  +1y         Columns:    current  7daysAgo  30daysAgo  6`: 5 inferred edges
- `Index:      0q  +1q  0y  +1y         Columns:    upLast7days  upLast30days  down`: 5 inferred edges
- `Index:      0q  +1q  0y  +1y +5y -5y         Columns:    stock  industry  sector`: 5 inferred edges

## Cross-Module Suspicious Edges

- `base.py` ↔ `exceptions.py`: 57
- `data.py` ↔ `exceptions.py`: 45
- `base.py` ↔ `data.py`: 19
- `base.py` ↔ `live.py`: 19
- `calendars.py` ↔ `data.py`: 19
- `calendars.py` ↔ `exceptions.py`: 19
- `funds.py` ↔ `data.py`: 19
- `funds.py` ↔ `exceptions.py`: 19
- `lookup.py` ↔ `data.py`: 18
- `lookup.py` ↔ `exceptions.py`: 18
- `utils.py` ↔ `exceptions.py`: 16
- `utils.py` ↔ `search.py`: 16
- `data.py` ↔ `utils.py`: 15
- `history.py` ↔ `exceptions.py`: 15
- `query.py` ↔ `exceptions.py`: 13
- `industry.py` ↔ `domain.py`: 11
- `sector.py` ↔ `domain.py`: 11
- `search.py` ↔ `data.py`: 10
- `search.py` ↔ `exceptions.py`: 10
- `fundamentals.py` ↔ `exceptions.py`: 6
