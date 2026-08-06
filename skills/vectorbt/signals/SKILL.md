---
name: vectorbt-signals
description: "Use when generating entry/exit signals with vectorbt — SignalFactory, indicator pipelines, and signal generation."
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
tags: [vectorbt, signals]
related_skills: []
---

# vectorbt Signals & Indicators (`vectorbt.signals`, `vectorbt.indicators`)

Dual-layer signal generation: **indicators** (technical analysis primitives from `ta-lib`, `pandas-ta`, or custom numba) produce real-valued arrays; **signals** convert those arrays into boolean entry/exit masks. `SignalFactory` builds signal generators with parameterized rules, backed by Numba-compiled kernels or a Rust engine.

## Quick Reference

| Class / Component | Source File | Purpose | Key Params |
|-------------------|-------------|---------|------------|
| `SignalFactory` | `vectorbt/signals/factory.py` | Build signal generator classes | `entry`, `exit`, `mode` |
| `SignalsAccessor` | `vectorbt/signals/accessors.py` | `.vbt.signals` accessor on DataFrames | wraps boolean signal arrays |
| `IndicatorBase` | `vectorbt/indicators/factory.py` | Base for all indicator classes | `run()`, `plot()`, params |
| `MA` | `vectorbt/indicators/basic.py` | Moving average (SMA, EMA, WMA) | `window`, `wtype` |
| `RSI` | `vectorbt/indicators/basic.py` | Relative Strength Index | `window` (default 14) |
| `MACD` | `vectorbt/indicators/basic.py` | MACD oscillator | `fast`, `slow`, `signal` |
| `BBANDS` | `vectorbt/indicators/basic.py` | Bollinger Bands | `window`, `alpha` |
| `STOCH` | `vectorbt/indicators/basic.py` | Stochastic oscillator | `k_window`, `d_window` |
| `generate_rand_enex()` | `vectorbt/signals/nb.py` | Numba kernel for random entry/exit | `n`, `entry_prob`, `exit_prob` |
| `generate_enex_nb()` | `vectorbt/signals/nb.py` | General entry/exit from rules | condition functions |
| `rand_enex_by_prob` | `vectorbt/signals/generators.py` | Random signals by probability | entry/exit probability |
| `between_partition_ranges` | `vectorbt/signals/dispatch.py` | Engine-neutral range queries | partition indices |

## Key Methods (graph degree centrality)

| Method / Attribute | Prevalence | Description |
|--------------------|------------|-------------|
| `SignalsAccessor.empty()` | 47 edges | Check for empty signal arrays |
| `SignalsAccessor.partition_pos_rank()` | | Rank signals within partitions |
| `SignalsAccessor.generate_random_exits()` | | Generate random exits for entries |
| `SignalFactory.__init__()` | 16 edges | Build signal generator from entry/exit rules |
| `IndicatorBase.run()` | 29 edges | Execute indicator pipeline on data |
| `IndicatorBase.plot()` | core | Plot indicator with subplots |
| `IndicatorBase.from_custom_func()` | 9 edges | Register custom numba function as indicator |
| `IndicatorBase.parse_ta_config()` | 9 edges | Parse ta-lib/pandas-ta config dict |
| `MA.run()` | tested | Compute moving average over window |
| `RSI.run()` | tested | Compute RSI values |
| `MACD.run()` | tested | Compute MACD line, signal, histogram |
| `generate_nb()` | 39 edges | Numba entry/exit kernel |
| `generate_ex_nb()` | | Extended entry/exit with stop exits |
| `generate_rand_enex_by_prob()` | 7 edges | Random signal generation |

## Architecture Overview

```
Indicators Layer (vectorbt.indicators)
  ├─ IndicatorBase ← MetaIndicatorBase
  │    ├─ .run() → call numba kernel or dispatch
  │    ├─ .plot() → subplots with OHLCV overlay
  │    └─ factory.py: build from {ta-lib, pandas-ta, custom}
  │
  ├─ Basic Indicators (indicators/basic.py)
  │    ├─ MA (window, wtype='simple'|'exp'|'wilder')
  │    ├─ RSI (window=14)
  │    ├─ MACD (fast=12, slow=26, signal=9)
  │    ├─ BBANDS (window=20, alpha=2)
  │    ├─ STOCH (k_window=14, d_window=3)
  │    ├─ ATR (window=14)
  │    └─ OBV (on-balance volume)
  │
  ├─ Numba Cache (indicators/nb.py)
  │    ├─ ma_cache_nb(), rsi_apply_nb(), macd_apply_nb()
  │    ├─ bb_apply(), mstd_cache_nb()
  │    └─ Compiled once, reused across runs
  │
  └─ Dispatch (indicators/dispatch.py)
       └─ Engine-neutral: routes to numba, Rust, or pandas

Signals Layer (vectorbt.signals)
  ├─ SignalFactory
  │    ├─ entry → boolean condition
  │    ├─ exit → boolean condition
  │    └─ Generates: entries, exits, entry_exits, entry_exits_df
  │
  ├─ SignalsAccessor (DataFrame.vbt.signals)
  │    ├─ generate_random_exits() → random exit masks
  │    ├─ partition_pos_rank() → rank within partitions
  │    ├─ between_partition_ranges() → filter by range
  │    └─ SignalsSRAccessor (column-level operations)
  │
  ├─ Numba Kernels (signals/nb.py)
  │    ├─ generate_nb() → entry/exit from conditions
  │    ├─ generate_ex_nb() → with stop exits
  │    ├─ clean_enex_nb() → remove duplicates
  │    └─ generate_rand_enex_by_prob_nb() → random
  │
  ├─ Signal Generators (signals/generators.py)
  │    ├─ RANDX → random exits
  │    ├─ RPROBCX → entry/exit by probability
  │    └─ RANDNX → random N-true entries
  │
  └─ Rust Engine (rust/src/signals.rs)
       ├─ between_partition_ranges_rs()
       ├─ generate_stop_enex_rs()
       └─ next_true_in_col()
```

## Common Patterns

### Pattern 1: MA crossover strategy with SignalFactory
```python
import vectorbt as vbt
import pandas as pd

price = vbt.YFData.download('AAPL').get('Close')

# Compute indicators
fast_ma = vbt.MA.run(price, window=10)
slow_ma = vbt.MA.run(price, window=30)

# Build signal generator
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

# Or use SignalFactory
sig = vbt.SignalFactory.from_params([
    ('MA', dict(window=10)),
    ('MA', dict(window=30))
], mode='cross')
```

### Pattern 2: RSI threshold signals
```python
import vectorbt as vbt

price = vbt.YFData.download('AAPL').get('Close')
rsi = vbt.RSI.run(price, window=14)

entries = rsi.rsi_crossed_below(30)   # oversold → buy
exits = rsi.rsi_crossed_above(70)     # overbought → sell
```

### Pattern 3: Bollinger Bands breakout
```python
import vectorbt as vbt

price = vbt.YFData.download('AAPL').get('Close')
bb = vbt.BBANDS.run(price, window=20, alpha=2)

entries = price.vbt.crossed_above(bb.lower)   # price crosses above lower band
exits = price.vbt.crossed_below(bb.upper)      # price crosses below upper band
```

### Pattern 4: Random signal generation (monte carlo)
```python
import vectorbt as vbt

# Generate random entry/exit signals for statistical testing
rand_entries = vbt.signals.nb.generate_rand_enex_by_prob_nb(
    target_shape=(1000, 10),
    entry_prob=0.3,
    exit_prob=0.1,
    seed=42
)
```

### Pattern 5: Custom indicator from numba
```python
import vectorbt as vbt
from numba import njit

@njit
def custom_ma(close, window):
    out = np.empty_like(close)
    for i in range(len(close)):
        if i < window - 1:
            out[i] = np.nan
        else:
            out[i] = np.mean(close[i-window+1:i+1])
    return out

MyMA = vbt.IndicatorBase.from_custom_func(
    custom_ma, window=20, param_names=['window']
)
result = MyMA.run(price, window=20)
```

## Pitfalls

1. **Signal look-ahead bias**: Indicators and signals are computed on the full array by default. When generating signals you must shift conditions: `entries = condition.shift(1)` to ensure you only enter on the next bar after the condition triggers.

2. **Signal conflict resolution**: When entry and exit signals occur on the same bar, vectorbt needs a conflict resolution mode (`entry_first`, `exit_first`, `opposite_entry`). Unresolved conflicts can produce portfolio simulation errors.

3. **Numba cache invalidation**: Numba caches are compiled once per session. If you modify the source and re-import, cached compiled functions won't update — restart the kernel.

4. **Rust engine vs Numba engine**: The Rust engine (via `engine='rust'`) is faster but has no GIL — avoid mixing Rust and Python concurrency without proper locking. Use `vbt.settings.engine` to switch globally.

5. **Indicator parameter broadcasting**: When passing list parameters (e.g., `window=[10, 20, 30]`), vectorbt broadcasts and runs all combinations. The result columns are multi-level indexed by parameter values. This can explode memory for wide param grids.

6. **`generate_rand_enex` seed reproducibility**: Random generators accept `seed` but the Rust and Numba engines may produce different sequences for the same seed. Use `vbt.settings.engine = 'numba'` for deterministic testing.

7. **pandas-ta configuration parsing**: `IndicatorBase.parse_ta_config()` converts from ta-lib or pandas-ta config dicts. Parameter names may differ between libraries — `timeperiod` in ta-lib vs `window` in vectorbt.

## Cross-Library Bridges

| Source | Target | Relationship | Description |
|--------|--------|-------------|-------------|
| `vectorbt.indicators` | `ta-lib.SMA/EMA/RSI` | wraps | vectorbt indicators wrap ta-lib functions |
| `vectorbt.SignalFactory` | `vectorbt.Portfolio.from_signals` | feeds | Signals are the primary input to portfolio simulation |
| `vectorbt.generate_rand_enex` | `optuna.Study` | parameterized | HPO tunes signal generation probabilities |
| `vectorbt.indicators` | `pandas-ta` | imports | `IndicatorBase` can parse pandas-ta config |
| `vectorbt.SignalsAccessor` | `backtrader.Strategy.next` | equivalent | Signal generation in vbt ≈ strategy logic in bt |

## Verification Checklist

- [ ] `vbt.MA.run(price, 20)` returns output with `.ma` attribute
- [ ] `vbt.RSI.run(price, 14)` returns values in [0, 100] range
- [ ] Signal cross detection: `fast_ma.ma_crossed_above(slow_ma)` is boolean
- [ ] `vbt.SignalFactory.from_params()` works with parameter list
- [ ] `SignalsAccessor.generate_random_exits()` returns boolean array
- [ ] Entry/exit arrays are same shape as price input
- [ ] Indicator parameter grid produces multi-level column index

## Graph Provenance

- Knowledge graph: vectorbt, 5,411 nodes, 13,588 edges, 395 communities
- Signal communities: 11 (nb.py), 12 (Rust), 21 (accessors), 60 (factory), 19 (generators), 107 (dispatch)
- Indicator communities: 1 (factory), 33 (basic indicators), 35 (dispatch), 36 (nb caches), 44 (Rust indicators)
