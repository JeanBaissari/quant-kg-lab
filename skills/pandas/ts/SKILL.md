---
name: pandas-ts
description: "Use when working with pandas time series \u2014 resample, rolling, expanding,\
  \ ewm, shift, diff, pct_change, and DateOffset."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pandas-dev/pandas
source_commit: 982854070758cd2015fc9e64395684546b1c5444
extraction_date: 2026-07-29
graph:
  nodes: 11368
  edges: 39913
  community_count: 410
  graph_hash: 4d026ee98025ac0c
tags:
- pandas
- ts
related_skills: []
---

# pandas time series (ts)

Temporal data manipulation: frequency conversion (`resample`), moving window computations (`rolling`, `expanding`, `ewm`), lag operations (`shift`, `diff`, `pct_change`), date generation (`date_range`), and datetime indexing (`DatetimeIndex`, `PeriodIndex`). Foundational for quant workflows — every OHLCV pipeline starts here.

## Quick Reference

| API | Source File | Degree | Description |
|-----|------------|--------|-------------|
| `DatetimeIndex` | `core/indexes/datetimes.py:L148` | 54 | Immutable ndarray-like of datetime64 for axis indexing |
| `Resampler` | `core/resample.py:L119` | 290 | GroupBy-like resampling for frequency conversion (down/upsampling) |
| `Rolling` | `core/window/rolling.py:L1955` | 32 | Fixed-size moving window (mean, std, corr, apply) |
| `Expanding` | `core/window/expanding.py:L43` | 30 | Expanding (cumulative) window from start of series |
| `ExponentialMovingWindow` | `core/window/ewm.py:L127` | 20 | Exponentially weighted moving window (EWMA, EWMSD, EWMCorr) |
| `BaseWindow` | `core/window/rolling.py:L116` | 35 | Base class for Rolling, Expanding, EWM windows |
| `PeriodIndex` | `core/indexes/period.py:L92` | 27 | Immutable ndarray of periods (e.g., '2023-Q1') |
| `TimedeltaIndex` | `core/indexes/timedeltas.py:L107` | 17 | Immutable ndarray of timedelta64 for duration indexing |
| `date_range()` | `core/indexes/datetimes.py` | 3 | Fixed-frequency DatetimeIndex generator |
| `to_datetime()` | `core/tools/datetimes.py` | 6 | Convert scalars, arrays, Series to datetime |

### Additional Key APIs (by degree rank)

| API | Type | Description |
|-----|------|-------------|
| `TimedeltaArray` | class | Array of timedelta64 with timezone-naive storage |
| `DatetimeIndexResampler` | class | Resampler specialized for DatetimeIndex |
| `PeriodIndexResampler` | class | Resampler specialized for PeriodIndex |
| `RollingGroupby` | class | Rolling window within GroupBy groups |
| `ExpandingGroupby` | class | Expanding window within GroupBy groups |
| `ExponentialMovingWindowGroupby` | class | EWM within GroupBy groups |
| `OnlineExponentialMovingWindow` | class | Online (streaming) EWMA for large datasets |
| `DatetimeArray` | class | Array of datetime64 with timezone handling |
| `asfreq()` | function | Convert time series to specified frequency |
| `is_subperiod()` | function | Check if one offset is a subperiod of another |
| `is_superperiod()` | function | Check if one offset is a superperiod of another |

## Common Patterns

### Time-Series Index Setup
```python
import pandas as pd
import numpy as np

# Generate datetime index
idx = pd.date_range('2020-01-01', periods=1000, freq='D')

# Or parse from data
df = pd.read_csv('data.csv', parse_dates=['date'], index_col='date')
df.index = pd.to_datetime(df['date'])

# Timezone handling
df.index = df.index.tz_localize('US/Eastern')
df.index = df.index.tz_convert('UTC')
```

### Resampling (Frequency Conversion)
```python
# Downsample: daily → monthly
monthly = df.resample('ME').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
})

# Upsample: daily → hourly (forward fill)
hourly = df.resample('h').ffill()

# Custom aggregation
weekly = df.resample('W').apply(lambda x: x.iloc[-1] - x.iloc[0])
```

### Rolling Window Operations
```python
# Simple moving averages
df['SMA_20'] = df['close'].rolling(20).mean()
df['SMA_50'] = df['close'].rolling(50).mean()

# Rolling volatility
df['vol_20'] = df['return'].rolling(20).std() * np.sqrt(252)

# Rolling correlation
df['corr'] = df['asset1'].rolling(60).corr(df['asset2'])

# Rolling quantiles
df['upper'] = df['close'].rolling(100).quantile(0.95)

# Custom rolling function
df['roll_max_dd'] = df['close'].rolling(252).apply(
    lambda x: (x / x.cummax() - 1).min()
)
```

### Expanding Window (Cumulative)
```python
# Expanding mean (ever-growing window)
df['exp_mean'] = df['return'].expanding().mean()

# Expanding max
df['cum_max'] = df['close'].expanding().max()

# Expanding volatility
df['exp_vol'] = df['return'].expanding().std()
```

### Exponential Weighted Moving (EWM)
```python
# EWMA (exponentially weighted moving average)
df['ewma_20'] = df['close'].ewm(span=20).mean()
df['ewma_alpha'] = df['close'].ewm(alpha=0.1).mean()  # smoothing factor

# EWM volatility
df['ewm_vol'] = df['return'].ewm(span=60).std()

# EWM correlation
df['ewm_corr'] = df['asset1'].ewm(span=60).corr(df['asset2'])
```

### Lag Operations
```python
# Shift (lag)
df['close_lag1'] = df['close'].shift(1)     # t-1
df['close_lead1'] = df['close'].shift(-1)   # t+1

# Percentage change
df['return'] = df['close'].pct_change()      # (p_t - p_{t-1}) / p_{t-1}
df['return_log'] = np.log(df['close'] / df['close'].shift(1))

# Difference
df['diff'] = df['close'].diff()             # p_t - p_{t-1}
df['diff2'] = df['close'].diff(2)           # p_t - p_{t-2}
```

### Datetime Accessors
```python
# Extract datetime components
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df['dayofweek'] = df.index.dayofweek      # Monday=0
df['quarter'] = df.index.quarter
df['is_month_end'] = df.index.is_month_end
df['week_of_year'] = df.index.isocalendar().week
```

### Window within GroupBy
```python
# Rolling per group (by symbol)
df.groupby('symbol')['close'].rolling(20).mean()

# Expanding per group
df.groupby('symbol')['return'].expanding().std()

# EWM per group
df.groupby('symbol')['close'].ewm(span=20).mean()
```

## Pitfalls

1. **`resample` requires datetime index**: `df.resample('D')` raises `TypeError` if the index is not datetime-like. Always verify `isinstance(df.index, pd.DatetimeIndex)` before resampling. Use `pd.to_datetime(df.index)` or `df.set_index(pd.to_datetime(df['date']))` to convert.

2. **`rolling().apply()` is extremely slow**: Custom functions via `rolling().apply()` run in pure Python, one window at a time. For large datasets (>100K rows), use `rolling().agg()` with built-in methods, or vectorize your computation with `numpy` before creating rolling windows.

3. **`resample` label convention affects which timestamp is used**: `resample('ME').mean()` labels the output with the last day of the month by default (`label='right'`). Use `label='left'` to label with the first day. This matters when merging resampled data with other monthly series.

4. **`shift` on a DatetimeIndex doesn't shift the index**: `df.shift(1)` shifts values but keeps the index stationary. To shift both, use `df.tshift(periods=1, freq='D')` (deprecated) or reindex: `df.reindex(df.index + pd.Timedelta(days=1))`.

5. **`ewm(span=20)` is not equivalent to `rolling(20).mean()`**: EWM uses exponential decay, so weights decrease exponentially with `alpha = 2/(span+1)`. The effective window is approximately `span` periods, but the computation is fundamentally different — every past observation contributes with exponentially decaying weight.

6. **`pct_change()` on log prices gives arithmetic returns, not log returns**: `df['price'].pct_change()` = arithmetic return. For log returns, use `np.log(df['price'] / df['price'].shift(1))` — these are additive over time (log returns sum to cumulative log return).

7. **`resample` upsampling introduces NaN gaps**: When upsampling from monthly to daily, `resample('D')` creates NaN for all intermediate days. Use `.ffill()`, `.bfill()`, or `.interpolate()` to fill, or `.asfreq()` for simple conversion without filling.

## Cross-Library Bridges

| Bridge | Relation | Description |
|--------|----------|-------------|
| pandas rolling → ta-lib | `implements` | pandas rolling window underpins ta-lib moving average calculations (SMA, EMA) |
| pandas DatetimeIndex → numpy datetime64 | `backed_by` | DatetimeIndex is backed by numpy datetime64 arrays |
| pandas resample/rolling → scipy.signal | `alternative_to` | scipy.signal filters (butter/filtfilt) as alternative smoothing to pandas rolling windows |
| pandas timestamp index → vectorbt | `input_to` | OHLCV DataFrames with DatetimeIndex are the standard input format for vectorbt |

## Verification Checklist

- [ ] `df.resample('ME').mean()` downsamples daily to monthly
- [ ] `df['close'].rolling(20).mean()` computes 20-period SMA
- [ ] `df['close'].expanding().std()` computes cumulative expanding std
- [ ] `df['close'].ewm(span=20).mean()` computes EWMA
- [ ] `df['close'].shift(1)` creates 1-period lag
- [ ] `df['close'].pct_change()` computes percentage change
- [ ] `df['close'].diff()` computes first difference
- [ ] `pd.date_range('2020-01-01', periods=100, freq='D')` generates 100 daily timestamps
- [ ] `pd.to_datetime(['2020-01-01', '2020-01-02'])` creates DatetimeIndex
- [ ] `df.index.year` extracts year component from DatetimeIndex
- [ ] `df.groupby('sym')['close'].rolling(20).mean()` computes per-group rolling
- [ ] `df['close'].rolling(60).corr(df['other'])` computes rolling correlation
- [ ] `df.resample('h').ffill()` upsamples with forward fill

## Provenance

- Knowledge graph: pandas, 11368 nodes, 39913 edges, 410 communities
- God nodes: `_FrequencyInferer` (28), `AbstractHolidayCalendar` (19), `holiday.py` (18) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 982854070758, backend opencode, description coverage 81%
