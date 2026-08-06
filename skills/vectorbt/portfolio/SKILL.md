---
name: vectorbt-portfolio
description: "Use when simulating portfolios with vectorbt — Portfolio.from_signals/from_orders, stats, metrics, and trades."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: polakowo/vectorbt
source_commit: f9897528f675114e6b34790178dbb2ca137acb51
extraction_date: 2026-07-29
graph:
  nodes: 5411
  edges: 13588
  community_count: 395
  graph_hash: 517324dd1904bd64
tags: [vectorbt, portfolio]
related_skills: []
---

# vectorbt Portfolio (`vectorbt.portfolio`)

The portfolio simulation engine. `Portfolio.from_signals()` takes boolean entry/exit arrays and simulates through them bar-by-bar, tracking cash, position size, trades, and drawdowns. The engine runs Numba-compiled kernels by default with an optional Rust backend. Performance stats are computed lazily via the `StatsBuilderMixin` inheritance chain.

## Quick Reference

| Class / Function | Source File | Purpose | Key Params |
|------------------|-------------|---------|------------|
| `Portfolio` | `vectorbt/portfolio/base.py` | Core portfolio object with stats, plotting, trades | wraps simulation result |
| `Portfolio.from_signals()` | `vectorbt/portfolio/base.py` | Simulate from entry/exit boolean arrays | `price`, `entries`, `exits`, `init_cash`, `fees`, `slippage` |
| `Portfolio.from_orders()` | `vectorbt/portfolio/base.py` | Simulate from explicit order arrays | `price`, `size`, `order_type` |
| `Orders` | `vectorbt/portfolio/orders.py` | Order record accessor | `.records`, `.count`, `.stats` |
| `Trades` | `vectorbt/portfolio/trades.py` | Trade record accessor (entry+exit pairs) | `.records`, `.pnl`, `.returns` |
| `Positions` | `vectorbt/portfolio/trades.py` | Position record accessor | `.records`, `.duration` |
| `Logs` | `vectorbt/portfolio/logs.py` | Execution log accessor | `.records_readable` |
| `simulate_from_signals_nb()` | `vectorbt/portfolio/nb.py` | Numba simulation kernel | internal (called by from_signals) |
| `simulate_from_orders_nb()` | `vectorbt/portfolio/nb.py` | Numba order execution kernel | internal (called by from_orders) |
| `AccumulationModeT` | `vectorbt/portfolio/enums.py` | Position accumulation mode enum | `Add`, `TargetPercent`, `TargetValue` |

## Key Methods (graph degree centrality)

| Method | Prevalence | Description |
|--------|------------|-------------|
| `Portfolio.__init__()` | 99 edges | Construct from simulation result wrappers |
| `Portfolio.value()` | 7 edges | Total portfolio value over time |
| `Portfolio.cash()` | 7 edges | Cash balance over time |
| `Portfolio.returns()` | 7 edges | Portfolio return series |
| `Portfolio.asset_value()` | 8 edges | Per-asset market value |
| `Portfolio.get_init_cash()` | 12 edges | Initial cash parameter |
| `Portfolio.stats()` | inherited | Performance metrics (Sharpe, Sortino, drawdown, etc.) |
| `Portfolio.plot()` | inherited | Cumulative returns, drawdown, trade markers |
| `Portfolio.regroup()` | 22 edges | Regroup positions by new labels |
| `Portfolio.orders` | attribute | Access Orders object |
| `Portfolio.trades` | attribute | Access Trades object |
| `Portfolio.positions` | attribute | Access Positions object |
| `simulate_from_signals_nb()` | 16 edges | Core Numba entry/exit simulation |
| `simulate_nb()` | 11 edges | Single-column Numba simulation |
| `simulate_row_wise_nb()` | 11 edges | Row-wise (per bar) simulation |
| `check_group_lens_nb()` | 15 edges | Validate group lengths before sim |

## Architecture Overview

```
Portfolio.from_signals(price, entries, exits, ...)
  │
  ├─ Input validation
  │    ├─ check_group_lens_nb() → validate group lengths
  │    ├─ replace_inf_price_nb() → handle NaN/Inf prices
  │    └─ convert to numpy arrays for Numba
  │
  ├─ Simulation Engine (choose one)
  │    ├─ numba: simulate_from_signals_nb() / simulate_from_orders_nb()
  │    │    ├─ Bar-by-bar: process_signals_at() → order_nb()
  │    │    ├─ Track: cash, position, value per bar
  │    │    └─ Record: orders, trades, logs into structured arrays
  │    │
  │    └─ rust: portfolio.rs kernels (selected via engine=)
  │         ├─ process_order(), process_signals_at()
  │         ├─ resolve_signal_conflict()
  │         └─ cash_flow_inner(), asset_flow_py()
  │
  ├─ Record Systems
  │    ├─ Orders → OrdersAccessor (fills, types, status)
  │    ├─ Trades → TradesAccessor (entry/exit pairs, PnL, duration)
  │    │    ├─ EntryTrades (entry side of each trade)
  │    │    ├─ ExitTrades (exit side of each trade)
  │    │    └─ Positions (aggregated by position)
  │    └─ Logs → LogsAccessor (execution details: fills, rejections)
  │
  └─ Stats & Plotting (inherited from mixins)
       ├─ StatsBuilderMixin → stats() → Sharpe, Sortino, Calmar, ...
       ├─ PlotsBuilderMixin → plot() → equity curve, drawdown, trades
       └─ ReturnsAccessor → benchmark comparisons
```

## Common Patterns

### Pattern 1: Full signal-to-portfolio pipeline
```python
import vectorbt as vbt
import pandas as pd

price = vbt.YFData.download('AAPL').get('Close')

# Generate signals
fast_ma = vbt.MA.run(price, 10)
slow_ma = vbt.MA.run(price, 30)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

# Simulate portfolio
portfolio = vbt.Portfolio.from_signals(
    price, entries, exits,
    init_cash=10000.0,
    fees=0.001,          # 0.1% per trade
    slippage=0.001,      # 0.1% slippage
    freq='D'
)

# Analyze
print(portfolio.stats())
portfolio.plot().show()
```

### Pattern 2: Parameter optimization (multiple windows)
```python
import vectorbt as vbt

# Parameter grid: try multiple MA windows
fast_windows = range(5, 30, 5)
slow_windows = range(20, 60, 10)

# Generate signals for all combinations
signals = vbt.SignalFactory.from_params([
    ('MA', dict(window=list(fast_windows))),
    ('MA', dict(window=list(slow_windows)))
], mode='cross')

# Each param combination gets its own column pair
# Run portfolio simulation
portfolio = vbt.Portfolio.from_signals(price, *signals, freq='D')

# Stats → DataFrame indexed by (fast_window, slow_window)
stats_df = portfolio.stats()
```

### Pattern 3: Long/Short mode with conflict resolution
```python
import vectorbt as vbt

portfolio = vbt.Portfolio.from_signals(
    price, entries, exits,
    direction='both',           # allow long and short
    upon_long_conflict='exit',  # exit existing long before new entry
    upon_short_conflict='exit', # exit existing short before new entry
    upon_opposite_entry='reverse', # flip position on opposite signal
    init_cash=10000.0,
    fees=0.001
)
```

### Pattern 4: Order-based simulation (explicit sizes)
```python
import vectorbt as vbt

# Create order arrays: positive = buy, negative = sell
size = pd.DataFrame(0, index=price.index, columns=price.columns)
size.iloc[10::20] = 1.0   # buy every 20 bars
size.iloc[15::20] = -1.0  # sell every 20 bars (offset)

portfolio = vbt.Portfolio.from_orders(
    price, size,
    init_cash=10000.0,
    fees=0.001
)
```

### Pattern 5: Access trade details
```python
portfolio = vbt.Portfolio.from_signals(price, entries, exits)

# Trade-by-trade analysis
trades = portfolio.trades
print(trades.records_readable)  # DataFrame: entry/exit idx, PnL, return, duration
print(trades.win_rate)
print(trades.expectancy)
print(trades.profit_factor)

# Position-level
positions = portfolio.positions
print(positions.records_readable)

# Execution logs (fills, rejections)
logs = portfolio.logs
print(logs.records_readable)
```

## Pitfalls

1. **NaN handling in price arrays**: NaN values in price will cause the simulation to skip bars silently. Always forward-fill or interpolate price data before calling `from_signals()`.

2. **Entry without exit = open position at end**: If entries exist without matching exits, the position remains open at the end. The terminal value is marked-to-market at the last price, which inflates unrealized PnL.

3. **`freq` must match data frequency**: The `freq` parameter (e.g., 'D', 'H', '15T') controls annualization in stats. A wrong freq gives wrong annualized Sharpe/Sortino/returns.

4. **Fees compound per fill**: When using `direction='both'`, each entry and each exit incurs fees separately. A round-trip long+short pair pays fees 4 times (entry_long + exit_long + entry_short + exit_short).

5. **Broadcasting explosion in param grids**: `Portfolio.from_signals()` broadcasts the same price across all columns of entries/exits. A 30×50 parameter grid on 5000-bar data creates 1500 simulation columns — memory usage is `5000 × 1500 × 8 bytes ≈ 60 MB` for the value array alone. Use `group_by` or subset columns.

6. **Initial cash allocation in grouped mode**: When `group_by` is set, `init_cash` is allocated per group, not per column. A portfolio with 3 groups and `init_cash=10000` gets 10K per group (30K total exposure simulation).

7. **Rust vs Numba numerical precision**: The Rust and Numba engines may produce slightly different PnL values (<1e-9 difference) due to floating-point accumulation order. Always use the same engine for consistent results.

## Cross-Library Bridges

| Source | Target | Relationship | Description |
|--------|--------|-------------|-------------|
| `vectorbt.Portfolio` | `optuna.Study` | optimized_by | HPO tunes portfolio parameters (MA windows, thresholds) |
| `vectorbt.Portfolio` | `backtrader.Cerebro` | equivalent | Both simulate portfolio from signals/strategy |
| `vectorbt.Trades` | `backtrader.TradeAnalyzer` | equivalent | Trade-level PnL and statistics |
| `vectorbt.Portfolio.stats` | `pyfolio` | superset_of | vectorbt stats cover all pyfolio metrics |
| `vectorbt.from_signals` | `ta-lib.RSI/MACD` | consumes | Indicator outputs become signal input |

## Verification Checklist

- [ ] `Portfolio.from_signals(price, entries, exits)` returns without error
- [ ] `portfolio.stats()` returns Sharpe, Sortino, max drawdown, win rate
- [ ] `portfolio.trades.records_readable` has entry/exit timestamps and PnL
- [ ] `portfolio.plot()` renders equity curve with trade markers
- [ ] Parameter grid produces multi-level column index in stats DataFrame
- [ ] `init_cash=0` raises appropriate error (must be > 0)
- [ ] Fees are applied correctly: verify a round-trip PnL matches manual calculation

## Graph Provenance

- Knowledge graph: vectorbt, 5,411 nodes, 13,588 edges, 395 communities
- Portfolio communities: 6 (Portfolio class), 9 (dispatch/buy-sell), 10 (nb.py kernels), 14 (Rust engine), 39 (enums), 61 (nb order resolution), 73 (nb record updates), 86 (grouped cash/value)
