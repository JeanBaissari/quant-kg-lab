# Edge Audit — backtrader

**Date**: 2026-07-29

## Summary

- Total edges: 6863
- EXTRACTED: 5412 (78.9%)
- INFERRED: 1451 (21.1%)
- AMBIGUOUS: 0

## Top INFERRED Nodes

- `MetaParams`: 243 inferred edges
- `LineSingle`: 95 inferred edges
- `DataBase`: 70 inferred edges
- `PandasMarketCalendar`: 68 inferred edges
- `LineRoot`: 60 inferred edges
- `CommInfoBase`: 54 inferred edges
- `SignalStrategy`: 50 inferred edges
- `Strategy`: 50 inferred edges
- `LineMultiple`: 49 inferred edges
- `TimeFrame`: 48 inferred edges
- `LineActions`: 48 inferred edges
- `LineIterator`: 47 inferred edges
- `Timer`: 46 inferred edges
- `TradingCalendar`: 45 inferred edges
- `TradingCalendarBase`: 45 inferred edges
- `WriterFile`: 44 inferred edges
- `Position`: 43 inferred edges
- `StrategyBase`: 42 inferred edges
- `LineSeriesStub`: 42 inferred edges
- `ItemCollection`: 35 inferred edges

## Cross-Module Suspicious Edges

- `cerebro.py` ↔ `tradingcal.py`: 132
- `linebuffer.py` ↔ `lineroot.py`: 99
- `cerebro.py` ↔ `strategy.py`: 88
- `strategy.py` ↔ `lineiterator.py`: 70
- `stores` ↔ `metabase.py`: 59
- `brokers` ↔ `order.py`: 54
- `lineseries.py` ↔ `linebuffer.py`: 48
- `lineseries.py` ↔ `lineroot.py`: 48
- `feed.py` ↔ `dataseries.py`: 46
- `feed.py` ↔ `resamplerfilter.py`: 46
- `cerebro.py` ↔ `metabase.py`: 44
- `cerebro.py` ↔ `timer.py`: 44
- `cerebro.py` ↔ `writer.py`: 44
- `brokers` ↔ `comminfo.py`: 43
- `brokers` ↔ `position.py`: 43
- `strategy.py` ↔ `lineroot.py`: 35
- `strategy.py` ↔ `lineseries.py`: 35
- `strategy.py` ↔ `metabase.py`: 35
- `strategy.py` ↔ `trade.py`: 35
- `order.py` ↔ `metabase.py`: 32
