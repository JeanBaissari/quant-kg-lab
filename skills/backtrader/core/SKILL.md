---
name: backtrader-core
description: "Use when building event-driven backtests with backtrader \u2014 Cerebro,\
  \ Strategy, DataFeed, Broker, Order, and Trade."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: mementum/backtrader
source_commit: b853d7c90b6721476eb5a5ea3135224e33db1f14
extraction_date: 2026-07-29
graph:
  nodes: 2680
  edges: 4964
  community_count: 206
  graph_hash: 58f821144ba4d073
tags:
- backtrader
- core
related_skills: []
target_version: 1.9.78.123 (untagged, on release day)
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `backtrader` at its pinned commit — an abandoned release line. Target version: 1.9.78.123 (untagged, on release day). Verify against your installed version before use.

# backtrader Core (`backtrader`)

The event-driven backtesting engine. `Cerebro` is the central orchestrator — you add data feeds, register a strategy, configure brokers/commissions, add analyzers, and call `run()`. Every time-series in backtrader is a `Line` (a circular buffer), groups of lines form `LineSeries`, and the strategy receives new bar data via `next()`.

## Quick Reference
| Class / Component | Source File | Purpose | Key Params |
|-------------------|-------------|---------|------------|
| `Cerebro` | `cerebro.py:L60` | Backtesting engine / orchestration | `stdstats`, `runonce`, `preload` |
| `Strategy` | `strategy.py:L107` | User trading logic base class | `next()`, `__init__()`, `notify_order()` |
| `MetaParams` | `metabase.py:L203` | Metaclass for declarative parameter system | `params = (('period', 14),)` |
| `LineRoot` | `lineroot.py:L61` | Root of time-series hierarchy | line operations (`+`, `-`, `*`, `/`) |
| `LineBuffer` | `linebuffer.py:L50` | Circular buffer for time-series data | underlying array storage |
| `LineSeries` | `lineseries.py:L444` | Named group of lines (open, high, low, close) | `.lines` attribute |
| `DataBase` | `feed.py:L599` | Abstract data feed base class | `dataname`, `fromdate`, `todate` |
| `GenericCSVData` | `backtrader/feeds/csvgeneric.py:L32` | CSV data feed with column mapping | `dtformat`, `timeframe` |
| `YahooFinanceCSV` | `feeds/yahoo.py:L192` | Yahoo Finance CSV loader | pre-configured OHLCV columns |
| `BackBroker` | `brokers/bbroker.py:L36` | Default broker backend | `cash`, `commission` |
| `CommInfoBase` | `comminfo.py:L30` | Commission scheme base | `commission`, `margin`, `stocklike` |
| `Order` | `order.py:L528` | Order object (created, submitted, accepted, completed) | `.buy()`, `.sell()`, `.close()` |
| `Position` | `position.py:L28` | Current position tracking | `.size`, `.price`, `.pnl` |
| `Trade` | `trade.py:L94` | Completed trade tracking | `.pnl`, `.pnlcomm`, `.bars` |
| `SignalStrategy` | `strategy.py:L1524` | Strategy driven by signals | `signal`, `sigtype` |
| `Sizer` | `sizer.py:L29` | Position sizing strategy | `FixedSize`, `PercentSizer` |

## Key Methods & Attributes (graph degree centrality)

| Method / Attribute | Prevalence | Description |
|--------------------|------------|-------------|
| `MetaParams` metaclass | 247 edges | God node — parameter system underpins everything | `metabase.py:L203` |

| `LineRoot` operations | 110 edges | Time-series math (+, -, *, /, >, <) | `lineroot.py:L61` |

| `Strategy.next()` | core | Called on each bar — main trading logic |
| `Strategy.__init__()` | core | Pre-compute indicators, set up data |
| `Strategy.buy()` / `sell()` | core | Submit orders to broker |
| `Strategy.notify_order()` | core | Order status changes callback |
| `Strategy.notify_trade()` | core | Trade open/close callback |
| `LineBuffer.buflen()` | 65 edges | Get buffer length (required bars available) |
| `LineIterator` | 69 edges | Iteration over time-series data | `lineiterator.py:L148` |

| `DataBase._load()` | 72 edges | Load next bar from data source |
| `BackBroker` execution | 59 edges | Order matching and execution | `brokers/bbroker.py:L36` |

| `Cerebro.run()` | core | Run the backtest loop |
| `Cerebro.adddata()` | core | Add data feed to engine |
| `Cerebro.addstrategy()` | core | Register strategy class |
| `Cerebro.broker.setcash()` | core | Set initial cash |
| `Cerebro.broker.setcommission()` | core | Set commission scheme |

## Architecture Overview

```
Cerebro (orchestrator)
  │
  ├─ Data Feeds (DataBase → GenericCSV, YahooFinance, IB, Oanda, VC)
  │    ├─ LineBuffer: circular buffer per bar (open, high, low, close, volume, openinterest)
  │    ├─ DataSeries: extends LineBuffer with datetime index
  │    └─ Resample/Replay filters: change timeframe
  │
  ├─ Strategy (user-defined)
  │    ├─ __init__(): declare indicators, register observers
  │    ├─ next(): called per bar — decision logic
  │    ├─ notify_order(): order status updates
  │    ├─ notify_trade(): trade open/close
  │    ├─ buy() / sell() / close(): submit orders
  │    └─ Params: (('period', 14), ('stake', 10)) — MetaParams metaclass
  │
  ├─ Broker (BackBroker)
  │    ├─ Order execution: Market, Limit, Stop, StopLimit, StopTrail
  │    ├─ Commission: CommInfoBase → Fixed, Percentage, PerShare
  │    ├─ Sizers: FixedSize, PercentSizer, AllInSizer
  │    ├─ Margin: short selling, futures
  │    └─ Position tracking: .size, .price, .pnl
  │
  ├─ Lines & Time-Series
  │    ├─ LineRoot → operations: l1 + l2, l1 > l2, l1(0), l1(-1)
  │    ├─ LineSingle → scalar from a single data source
  │    ├─ LineMultiple → operations across multiple sources
  │    └─ LineBuffer → circular buffer of N bars
  │
  ├─ Indicators (built-in, built on Line operations)
  │    ├─ MovingAverageBase → SMA, EMA, WMA, DEMA, TEMA, HMA, DicksonMA
  │    ├─ BasicOps → SumN, Highest, Lowest, ApplyN, ReduceN
  │    ├─ CrossOver/CrossUp/CrossDown → signal detection
  │    └─ Oscillators → RSI, MACD, Stochastic, ATR, ...
  │
  └─ Observers (real-time monitoring during backtest)
       ├─ Broker, Trades, BuySell, DrawDown, TimeReturn
       └─ Plotting: matplotlib integration
```

## Common Patterns

### Pattern 1: Basic SMA crossover strategy
```python
import backtrader as bt

class SmaCross(bt.Strategy):
    params = (('fast', 10), ('slow', 30))

    def __init__(self):
        self.fast_ma = bt.indicators.SMA(self.data.close, period=self.p.fast)
        self.slow_ma = bt.indicators.SMA(self.data.close, period=self.p.slow)
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)

    def next(self):
        if self.crossover > 0:       # fast crosses above slow
            self.buy()
        elif self.crossover < 0:     # fast crosses below slow
            self.close()

cerebro = bt.Cerebro()
cerebro.adddata(bt.feeds.YahooFinanceCSV(dataname='AAPL.csv'))
cerebro.addstrategy(SmaCross)
cerebro.broker.setcash(10000)
cerebro.broker.setcommission(commission=0.001)
cerebro.run()
cerebro.plot()
```

### Pattern 2: Multiple data feeds and timeframes
```python
class MultiTFStrategy(bt.Strategy):
    def __init__(self):
        # self.datas[0] = daily, self.datas[1] = weekly
        self.daily_sma = bt.indicators.SMA(self.datas[0].close, period=20)
        self.weekly_sma = bt.indicators.SMA(self.datas[1].close, period=10)

    def next(self):
        if self.daily_sma > self.weekly_sma:
            self.buy(data=self.datas[0])

cerebro = bt.Cerebro()
cerebro.adddata(daily_data)
cerebro.adddata(weekly_data)
```

### Pattern 3: Custom commission scheme
```python
class MyCommission(bt.CommInfoBase):
    params = (('commission', 0.002), ('percabs', True))

    def _getcommission(self, size, price, pseudoexec):
        return abs(size) * price * self.p.commission

cerebro.broker.addcommissioninfo(MyCommission())
```

### Pattern 4: Position sizing with percent of equity
```python
cerebro.addsizer(bt.sizers.PercentSizer, percents=90)  # use 90% of equity
```

### Pattern 5: Order management with stop-loss
```python
class StopLossStrategy(bt.Strategy):
    def __init__(self):
        self.order = None

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.sell(exectype=bt.Order.Stop, price=order.executed.price * 0.95)

    def next(self):
        if self.order:
            return  # wait for pending order
        if self.data.close[0] > self.data.close[-1]:
            self.order = self.buy()
```

## Pitfalls

1. **`next()` is called on every bar regardless of indicator readiness**: Indicators need `period` bars before producing values. The first `period-1` calls to `next()` will have `NaN` indicator values. Use `if len(self) < self.p.period: return` to skip early bars, or rely on the automatic `_minperiod` from `MetaParams`.

2. **`self.datas[0]` vs `self.data`**: `self.data` and `self.datas[0]` point to the same object, but `self.data.close` is shorthand for `self.datas[0].close`. When using multiple data feeds, always use explicit `self.datas[i]` indexing — `self.data` only refers to the first.

3. **Line indexing: `[0]` = current bar, `[-1]` = previous bar**: Unlike pandas where `[-1]` is the last element, backtrader line indexing uses negative offsets for lookback. `self.data.close[0]` is the current bar's close; `self.data.close[-1]` is yesterday's close. This is the #1 source of bugs for pandas users.

4. **Order execution is not immediate**: `self.buy()` submits an order that executes on the NEXT bar at the open by default. The position only appears in `self.position` on the following `next()` call. Use `self.buy(exectype=bt.Order.Close)` to execute at the current bar's close.

5. **`cheat-on-open` is order-sensitive**: When using `cerebro = bt.Cerebro(cheat_on_open=True)`, `next_open()` is called BEFORE the broker processes orders. This allows looking at orders that will execute, but confusingly means `self.position` reflects the state BEFORE the open fill.

6. **`runonce=True` (default) batches indicator computation**: With `runonce`, all indicator values are computed in one shot before the strategy loop. This is much faster but means `next()` sees all indicator values already computed — you cannot use `next()` to dynamically change indicator parameters per bar. Set `runonce=False` for per-bar indicator recalculation.

7. **Data feed datetime mismatch**: `fromdate`/`todate` use the data feed's timezone. Yahoo Finance CSV data is UTC; setting `fromdate=datetime(2020,1,1)` without `tzinfo=pytz.utc` may miss bars due to timezone mismatch.

## Cross-Library Bridges

| Source | Target | Relationship | Description |
|--------|--------|-------------|-------------|
| `backtrader.Cerebro` | `vectorbt.Portfolio` | equivalent | Both are backtesting engines |
| `backtrader.Strategy.next` | `vectorbt.SignalFactory` | equivalent | Strategy logic ≈ signal generation |
| `backtrader.DataFeed` | `pandas.DataFrame` | wraps | bt data feeds can be constructed from DataFrames |
| `backtrader.indicators` | `ta-lib.SMA/RSI` | bridges | `backtrader.talib` module wraps ta-lib |
| `backtrader.LineBuffer` | `numpy.ndarray` | backed_by | Line uses numpy array for underlying storage |
| `backtrader.Cerebro` | `optuna.Study` | optimized_by | HPO tunes strategy parameters via optuna integration |

## Verification Checklist

- [ ] `cerebro.run()` executes without error
- [ ] Initial cash set via `cerebro.broker.setcash(100000)`
- [ ] Commission configured via `cerebro.broker.setcommission(commission=0.001)`
- [ ] Strategy's `next()` called for each bar in data feed
- [ ] Indicator values accessible in `next()` after minimum period
- [ ] `self.buy()` returns an Order object; check `order.status` in `notify_order()`
- [ ] Final portfolio value accessible via `cerebro.broker.getvalue()`
- [ ] Plot renders: `cerebro.plot()` shows OHLCV, indicators, trades

## Provenance

- Knowledge graph: backtrader, 2680 nodes, 4964 edges, 206 communities
- God nodes: `MetaParams` (260), `LineRoot` (119), `LineSingle` (111) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b853d7c90b67, backend opencode, description coverage 84%
