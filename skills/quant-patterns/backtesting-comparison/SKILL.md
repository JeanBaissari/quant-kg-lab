---
name: quant-backtesting-comparison
description: "Use when choosing between backtrader and vectorbt for strategy backtesting — tradeoffs between event-driven flexibility and vectorized speed."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [backtrader-core, vectorbt-portfolio, vectorbt-signals]
tags: [quantitative-finance, backtesting, backtrader, vectorbt, workflow]
related_skills: [backtrader-core, vectorbt-portfolio, vectorbt-signals]
target_version: cross-lib
---

# Quant Backtesting Comparison (backtrader vs vectorbt)

Two backtesting philosophies: backtrader's event-driven loop (realistic fills, order types,
analyzers) and vectorbt's vectorized simulation (blazing fast parameter sweeps, portfolio-level
analysis). This playbook maps when each wins and how to bridge between them.

## Steps

1. **Define the strategy logic** — write the core signal generation in pure numpy/pandas first,
   independent of the engine. This makes it portable across both backtesting frameworks.
   ```python
   entries = (sma_fast > sma_slow) & (sma_fast.shift(1) <= sma_slow.shift(1))
   exits   = (sma_fast < sma_slow) & (sma_fast.shift(1) >= sma_slow.shift(1))
   ```
2. **Vectorized sweep (vectorbt)** — `Portfolio.from_signals` for fast parameter search. Vectorbt
   wraps a numpy array and simulates the full portfolio in C/Rust.
   ```python
   import vectorbt as vbt
   pf = vbt.Portfolio.from_signals(close, entries, exits, fees=0.001, freq="1D")
   print(pf.sharpe_ratio())                 # vectorbt/portfolio/base.py:L2048
   ```
   *Citation*: `vectorbt/portfolio/base.py:L1498`
3. **Event-driven validation (backtrader)** — once you have a candidate, run it through backtrader's
   `Cerebro`/`Strategy` for realistic simulation: stop-loss orders, partial fills, margin.
   ```python
   import backtrader as bt
   cerebro = bt.Cerebro()                   # backtrader/cerebro.py:L60
   cerebro.addstrategy(MyStrategy)          # cerebro.py:L909
   cerebro.run()                            # cerebro.py:L1030
   ```
   *Citations*: `backtrader/cerebro.py:L60`, `backtrader/strategy.py:L107`
4. **Compare results** — vectorbt's stats (Sharpe, max DD, turnover) vs backtrader's analyzers.
   Discrepancies reveal hidden assumptions (close-to-close vs intrabar, fee model differences).
5. **Use vectorbt for HPO, backtrader for final validation** — vectorized backtest runs 1000x
   parameter combos in seconds; backtrader confirms the winner under realistic execution.
6. **Signal bridging** — vectorbt `SignalFactory` generates boolean arrays; backtrader strategies
   call `self.buy()`/`self.sell()` in `next()`. Map between them with a shared signal generator.

## Pitfalls

1. **Event-driven vs vectorized assumption** — vectorbt assumes you can trade at the close of the
   signal bar; backtrader can simulate next-bar execution. The 1-bar latency difference changes
   Sharpe materially on fast signals.
2. **Memory on large universes** — vectorbt stores full result matrices in memory; 10,000 assets x
   1,000 parameter combos x 5,000 days can OOM. Use chunked backtests or polars preprocessing.
3. **Speed** — vectorbt is 100-1000x faster for parameter sweeps; backtrader is single-threaded
   and can take minutes for complex strategies. Never use backtrader for the initial search.
4. **Flexibility ceiling** — vectorbt cannot model partial fills, margin calls, or custom order
   types. Backtrader can, but at the cost of speed and code complexity. Match the engine to the
   question you are asking.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| fast sweep | `vectorbt-portfolio`, `vectorbt-signals` | entries/exits -> Portfolio (simulates) |
| validation | `backtrader-core` | Cerebro/Strategy (realistic fills) |
| signal source | (this playbook) | shared numpy signal generator (powers both) |
| HPO | `optuna-study` | parameter grid -> vectorbt objective (optimized_by) |
| comparison | (this playbook) | stats discrepancy -> hidden assumption (diagnoses) |

## Related Skills

- [[backtrader-core]]
- [[vectorbt-portfolio]]
- [[vectorbt-signals]]
