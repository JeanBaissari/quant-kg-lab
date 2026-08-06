---
name: backtrader-analyzers
description: "Use when adding performance analyzers to a backtrader strategy — SharpeRatio, DrawDown, TradeAnalyzer, TimeReturn, and other Cerebro analyzers."
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
  graph_hash: c751b026be8cb4f0
tags: [backtrader, analyzers]
related_skills: []
---

# backtrader Analyzers (`backtrader.analyzers`)

Analyzers compute performance metrics asynchronously during a backtest. Unlike Strategy code — which runs per-bar — analyzers receive callbacks (`notify_trade`, `notify_order`, `notify_fund`) and aggregate results into a final analysis dictionary retrievable after `cerebro.run()`.

## Quick Reference

| Analyzer | Source File | Metric | Key Output Keys |
|----------|-------------|--------|-----------------|
| `SharpeRatio` | `backtrader/analyzers/sharpe.py` | Risk-adjusted return (annualized) | `sharperatio` |
| `SharpeRatio_A` | `backtrader/analyzers/sharpe.py` | Annualized Sharpe directly | `sharperatio` |
| `DrawDown` | `backtrader/analyzers/drawdown.py` | Drawdown statistics | `max.drawdown`, `max.drawdownperiod`, `max.moneydown` |
| `TimeDrawDown` | `backtrader/analyzers/drawdown.py` | Time-based drawdown | `max.drawdown`, `max.drawdownperiod` |
| `TradeAnalyzer` | `backtrader/analyzers/tradeanalyzer.py` | Trade-level statistics | `total.closed`, `won.total`, `lost.total`, `pnl.net.total` |
| `AnnualReturn` | `backtrader/analyzers/annualreturn.py` | Returns by calendar year | `{year: return_pct}` |
| `TimeReturn` | `backtrader/analyzers/timereturn.py` | Returns by time period | dict of `{datetime: return}` |
| `SQN` | `backtrader/analyzers/sqn.py` | System Quality Number (Van Tharp) | `sqn` |
| `Calmar` | `backtrader/analyzers/calmar.py` | Calmar Ratio (return / max drawdown) | `calmar` |
| `VWR` | `backtrader/analyzers/vwr.py` | Variability-Weighted Return | `vwr` |
| `Transactions` | `backtrader/analyzers/transactions.py` | Per-data transaction log | `{data_name: [transactions]}` |
| `PositionsValue` | `backtrader/analyzers/positions.py` | Position values over time | `{datetime: value}` |
| `GrossLeverage` | `backtrader/analyzers/leverage.py` | Gross leverage ratio | `gross_leverage` |
| `LogReturnsRolling` | `backtrader/analyzers/logreturnsrolling.py` | Rolling log returns | dict of rolling return arrays |
| `PeriodStats` | `backtrader/analyzers/periodstats.py` | Stats for given timeframe | `average`, `stddev`, `positive`, `negative` |
| `PyFolio` | `backtrader/analyzers/pyfolio.py` | PyFolio-compatible output | `returns`, `positions`, `transactions`, `gross_lev` |
| `Returns` | `backtrader/analyzers/returns.py` | Total/average/compound returns | `rtot`, `ravg`, `rnorm`, `rnorm100` |

## Key Methods (analyzer lifecycle)

| Method | Description |
|--------|-------------|
| `__init__()` | Declare params (e.g., `timeframe`, `compression`, `riskfreerate`) |
| `start()` | Called once before backtest begins |
| `prenext()` / `nextstart()` / `next()` | Called per bar (mirrors strategy lifecycle) |
| `notify_order(order)` | Called when order status changes |
| `notify_trade(trade)` | Called when trade opens/closes |
| `notify_fund(cash, value, fundvalue, shares)` | Called with fund/cash/value updates |
| `notify_dt_over(dt)` | Called when datetime grouping period changes |
| `stop()` | Called at end of backtest |
| `get_analysis()` | Return computed analysis dict |

## Architecture Overview

```
Analyzer (base, backtrader/analyzer.py)
  ├─ Lifecycle: start → next/prenext/nextstart → stop
  ├─ Notifications: notify_order, notify_trade, notify_fund
  ├─ Sub-day grouping: _on_dt_over, _get_dt_cmpkey
  └─ Result: get_analysis() → dict

TimeFrameAnalyzerBase
  └─ Subclasses that group data by timeframe (daily, weekly, monthly)

    ├─ Returns / AnnualReturn / TimeReturn
    │    ├─ Returns: total, average, compound, annualized
    │    ├─ AnnualReturn: dict keyed by year
    │    └─ TimeReturn: dict keyed by datetime
    │
    ├─ Risk Metrics
    │    ├─ SharpeRatio: (return - risk_free) / std
    │    ├─ SharpeRatio_A: annualized version
    │    ├─ VWR: variability-weighted (log) return
    │    ├─ SQN: sqrt(trades) * mean(R) / std(R)  [Van Tharp]
    │    └─ Calmar: annualized_return / max_drawdown
    │
    ├─ Drawdown
    │    ├─ DrawDown: value-based drawdown (peak-to-trough)
    │    └─ TimeDrawDown: time-based duration
    │
    ├─ Trade Analysis
    │    ├─ TradeAnalyzer: won/lost counts, PnL stats, streak
    │    └─ Transactions: per-data transaction log
    │
    ├─ Position/Cash
    │    ├─ PositionsValue: position values over time
    │    ├─ GrossLeverage: gross exposure / net value
    │    └─ LogReturnsRolling: rolling log returns
    │
    ├─ PeriodStats: stats aggregated by timeframe
    │
    └─ PyFolio: multi-analyzer aggregator for pyfolio
         ├─ Returns → timeseries of returns
         ├─ Positions → position values
         ├─ Transactions → trade log
         └─ GrossLeverage → leverage
```

## Common Patterns

### Pattern 1: Add multiple analyzers to Cerebro
```python
import backtrader as bt

cerebro = bt.Cerebro()

# Add strategy, data, broker...

cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe',
                    riskfreerate=0.02, timeframe=bt.TimeFrame.Days)
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='annual')
cerebro.addanalyzer(bt.analyzers.SQN, _name='sqn')

results = cerebro.run()
strat = results[0]

# Retrieve analysis
print(f"Sharpe: {strat.analyzers.sharpe.get_analysis()['sharperatio']:.3f}")
print(f"Max DD: {strat.analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")

trade_analysis = strat.analyzers.trades.get_analysis()
print(f"Total trades: {trade_analysis['total']['closed']}")
print(f"Win rate: {trade_analysis['won']['total'] / trade_analysis['total']['closed']:.2%}")
```

### Pattern 2: Custom analyzer for tracking custom metrics
```python
import backtrader as bt

class MaxConsecutiveLosses(bt.Analyzer):
    def start(self):
        self.max_consecutive = 0
        self.current_streak = 0

    def notify_trade(self, trade):
        if trade.isclosed:
            if trade.pnlcomm < 0:
                self.current_streak += 1
                self.max_consecutive = max(self.max_consecutive, self.current_streak)
            else:
                self.current_streak = 0

    def stop(self):
        self.rets['max_consecutive_losses'] = self.max_consecutive

    def get_analysis(self):
        return self.rets

cerebro.addanalyzer(MaxConsecutiveLosses, _name='consec')
```

### Pattern 3: Monthly Sharpe with compression
```python
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe_monthly',
                    timeframe=bt.TimeFrame.Months, compression=1,
                    riskfreerate=0.0)
```

### Pattern 4: PyFolio integration for full tear sheet
```python
cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')

results = cerebro.run()
pyfolio_analyzer = results[0].analyzers.pyfolio
returns, positions, transactions, gross_lev = pyfolio_analyzer.get_pf_items()

import pyfolio as pf
pf.create_full_tear_sheet(returns, positions=positions, transactions=transactions)
```

### Pattern 5: Annual Returns table
```python
annual = strat.analyzers.annual.get_analysis()
for year, ret in sorted(annual.items()):
    print(f"{year}: {ret:.2%}")
```

## Pitfalls

1. **`get_analysis()` called before `run()`**: Analyzers are populated during `cerebro.run()`. Calling `get_analysis()` before running returns empty dicts. Always access after `run()`.

2. **SharpeRatio `timeframe` mismatch**: The default `timeframe=bt.TimeFrame.Years` gives annualized Sharpe. If your data is daily but you pass `timeframe=bt.TimeFrame.Days`, you get a daily Sharpe — compare apples to apples.

3. **`notify_trade` fires on trade open AND close**: Check `trade.isclosed` before computing trade metrics. Open trades at backtest end are NOT closed — they won't appear in TradeAnalyzer's `total.closed` count but will fire `notify_trade`.

4. **DrawDown `fund=True` vs `fund=False`**: With `fund=True`, drawdown is calculated from the broker's total fund value (cash + positions). With `fund=False`, it's calculated from any other line (e.g., strategy value). Most use cases want `fund=True` (the default).

5. **`_name` is required for multi-analyzer access**: Without `_name='myanalyzer'`, the analyzer is accessible only by class reference — `strat.analyzers.SharpeRatio` becomes ambiguous with multiple Sharpe instances. Always set `_name`.

6. **TradeAnalyzer counts open trades separately**: `trade_analysis['total']['open']` counts trades still open at end. They contribute to `pnl.gross.total` but not `pnl.net.total`. Factor open trades into PnL analysis carefully.

7. **AnnualReturn expects full calendar years**: If the backtest starts mid-year, the first partial year return includes only observations from the start date onward — not a full calendar year return. Same for the final partial year.

## Cross-Library Bridges

| Source | Target | Relationship | Description |
|--------|--------|-------------|-------------|
| `backtrader.SharpeRatio` | `vectorbt.Portfolio.stats` | equivalent | Both compute Sharpe from returns |
| `backtrader.DrawDown` | `vectorbt.Drawdowns` | equivalent | Drawdown calculation parallel |
| `backtrader.TradeAnalyzer` | `vectorbt.Trades.stats` | equivalent | Trade-level PnL statistics |
| `backtrader.PyFolio` | `pyfolio` | wraps | bt's PyFolio feeds pyfolio tear sheets |
| `backtrader.Analyzer` | `optuna.Study` | provides_metric | Analyzer results are HPO objectives |

## Verification Checklist

- [ ] Analyzers added with unique `_name` keys
- [ ] `results = cerebro.run()` successful before accessing analyzers
- [ ] `get_analysis()` returns non-empty dict
- [ ] Sharpe ratio is reasonable (0.5–3.0 for realistic strategies)
- [ ] Max drawdown is a percentage (not absolute dollar value)
- [ ] TradeAnalyzer `total.closed` matches expected trade count
- [ ] PyFolio `get_pf_items()` returns 4-tuple (returns, positions, transactions, leverage)

## Graph Provenance

- Knowledge graph: backtrader, 3,458 nodes, 6,863 edges, 261 communities
- Analyzer communities: 22 (base Analyzer), 44 (Returns/TimeReturn), 49 (Sharpe/TradeAnalyzer/AnnualReturn), 74 (DrawDown), 107 (Calmar), 108 (SQN), 137–165 (other analyzers)
- God node: `Analyzer` base class (17 edges)
- Top analyzers by degree: VWR (8), DrawDown (7), SQN (7), TimeReturn (7), Calmar (6), LogReturnsRolling (6), Returns (6), SharpeRatio (6), TradeAnalyzer (6)
