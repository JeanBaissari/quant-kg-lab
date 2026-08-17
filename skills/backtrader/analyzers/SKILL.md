---
name: backtrader-analyzers
description: "Use when adding performance analyzers to a backtrader strategy \u2014\
  \ SharpeRatio, DrawDown, TradeAnalyzer, TimeReturn, and other Cerebro analyzers."
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
- analyzers
related_skills: []
target_version: 1.9.78.123 (untagged, on release day)
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `backtrader` at its pinned commit — an abandoned release line. Target version: 1.9.78.123 (untagged, on release day). Verify against your installed version before use.

# backtrader Analyzers (`backtrader.analyzers`)

Analyzers compute performance metrics asynchronously during a backtest. Unlike Strategy code — which runs per-bar — analyzers receive callbacks (`notify_trade`, `notify_order`, `notify_fund`) and aggregate results into a final analysis dictionary retrievable after `cerebro.run()`.

## Quick Reference
| Analyzer | Source File | Metric | Key Output Keys |
|----------|-------------|--------|-----------------|
| `SharpeRatio` | `analyzers/sharpe.py:L33` | Risk-adjusted return (annualized) | `sharperatio` |
| `SharpeRatio_A` | `analyzers/sharpe.py:L209` | Annualized Sharpe directly | `sharperatio` |
| `DrawDown` | `backtrader/analyzers/drawdown.py:L31` | Drawdown statistics | `max.drawdown`, `max.drawdownperiod`, `max.moneydown` |
| `TimeDrawDown` | `analyzers/drawdown.py:L113` | Time-based drawdown | `max.drawdown`, `max.drawdownperiod` |
| `TradeAnalyzer` | `analyzers/tradeanalyzer.py:L31` | Trade-level statistics | `total.closed`, `won.total`, `lost.total`, `pnl.net.total` |
| `AnnualReturn` | `analyzers/annualreturn.py:L30` | Returns by calendar year | `{year: return_pct}` |
| `TimeReturn` | `backtrader/analyzers/timereturn.py:L27` | Returns by time period | dict of `{datetime: return}` |
| `SQN` | `analyzers/sqn.py:L31` | System Quality Number (Van Tharp) | `sqn` |
| `Calmar` | `analyzers/calmar.py:L31` | Calmar Ratio (return / max drawdown) | `calmar` |
| `VWR` | `analyzers/vwr.py:L32` | Variability-Weighted Return | `vwr` |
| `Transactions` | `analyzers/transactions.py:L31` | Per-data transaction log | `{data_name: [transactions]}` |
| `PositionsValue` | `analyzers/positions.py:L28` | Position values over time | `{datetime: value}` |
| `GrossLeverage` | `analyzers/leverage.py:L27` | Gross leverage ratio | `gross_leverage` |
| `LogReturnsRolling` | `analyzers/logreturnsrolling.py:L33` | Rolling log returns | dict of rolling return arrays |
| `PeriodStats` | `analyzers/periodstats.py:L34` | Stats for given timeframe | `average`, `stddev`, `positive`, `negative` |
| `PyFolio` | `analyzers/pyfolio.py:L33` | PyFolio-compatible output | `returns`, `positions`, `transactions`, `gross_lev` |
| `Returns` | `analyzers/returns.py:L30` | Total/average/compound returns | `rtot`, `ravg`, `rnorm`, `rnorm100` |

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

4. **DrawDown `fund` default is `None`**: `DrawDown`'s `fund` parameter defaults to `None`,
   which delegates to the broker's `fundmode` setting (which itself defaults to `False`).
   With `fund=False`, drawdown is calculated from any line (e.g., strategy value). With
   `fund=True`, drawdown uses the broker's total fund value (cash + positions). Most use
   cases want `fund=True` — pass it explicitly.

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

## Provenance

- Knowledge graph: backtrader, 2680 nodes, 4964 edges, 206 communities
- God nodes: `VWR` (8), `DrawDown` (7), `SQN` (7) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ b853d7c90b67, backend opencode, description coverage 84%
