# Edge Audit — backtrader

**Date**: 2026-07-29

## Summary

- Total edges: 4964
- EXTRACTED: 3433 (69.2%)
- INFERRED: 1531 (30.8%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `MetaParams`: 256 inferred edges
- `LineSingle`: 106 inferred edges
- `PandasMarketCalendar`: 73 inferred edges
- `DataBase`: 70 inferred edges
- `LineRoot`: 69 inferred edges
- `LineMultiple`: 58 inferred edges
- `CommInfoBase`: 54 inferred edges
- `SignalStrategy`: 54 inferred edges
- `Strategy`: 54 inferred edges
- `Timer`: 50 inferred edges
- `TradingCalendar`: 49 inferred edges
- `TradingCalendarBase`: 49 inferred edges
- `TimeFrame`: 49 inferred edges
- `LineActions`: 49 inferred edges
- `LineIterator`: 49 inferred edges
- `WriterFile`: 48 inferred edges
- `StrategyBase`: 44 inferred edges
- `LineSeriesStub`: 44 inferred edges
- `Position`: 43 inferred edges
- `ItemCollection`: 37 inferred edges

## Cross-Module Suspicious Edges

- `cerebro.py` ↔ `tradingcal.py`: 144
- `linebuffer.py` ↔ `lineroot.py`: 126
- `cerebro.py` ↔ `strategy.py`: 96
- `strategy.py` ↔ `lineiterator.py`: 74
- `bbroker.py` ↔ `order.py`: 54
- `cerebro.py` ↔ `metabase.py`: 48
- `cerebro.py` ↔ `timer.py`: 48
- `cerebro.py` ↔ `writer.py`: 48
- `feed.py` ↔ `dataseries.py`: 48
- `feed.py` ↔ `resamplerfilter.py`: 48
- `lineseries.py` ↔ `linebuffer.py`: 48
- `lineseries.py` ↔ `lineroot.py`: 48
- `ibstore.py` ↔ `metabase.py`: 37
- `strategy.py` ↔ `lineroot.py`: 37
- `strategy.py` ↔ `lineseries.py`: 37
- `strategy.py` ↔ `metabase.py`: 37
- `strategy.py` ↔ `trade.py`: 37
- `order.py` ↔ `metabase.py`: 32
- `feed.py` ↔ `tradingcal.py`: 24
- `resamplerfilter.py` ↔ `dataseries.py`: 24
