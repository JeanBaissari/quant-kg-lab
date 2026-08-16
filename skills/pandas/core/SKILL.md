---
name: pandas-core
description: "Use when manipulating tabular data with pandas \u2014 DataFrame, Series,\
  \ Index, GroupBy, merge, concat, pivot, and melt."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pandas-dev/pandas
source_commit: 982854070758cd2015fc9e64395684546b1c5444
extraction_date: 2026-07-29
graph:
  nodes: 11368
  edges: 39913
  community_count: 396
  graph_hash: e0d7084604dec6e0
tags:
- pandas
- core
related_skills: []
---

# pandas.core

The core pandas data structures and operations: `DataFrame` (2-D labeled tabular data), `Series` (1-D labeled array), `Index` (axis labels), `GroupBy` (split-apply-combine), plus reshaping (`merge`, `pivot`, `concat`) and I/O.

## Quick Reference

| API | Source File | Degree | Description |
|-----|------------|--------|-------------|
| `DataFrame` | `core/frame.py:L273` | 848 | Two-dimensional, size-mutable, potentially heterogeneous tabular data |
| `Series` | `core/series.py:L211` | 648 | One-dimensional ndarray with axis labels (including time series) |
| `MultiIndex` | `core/indexes/multi.py:L201` | 523 | Multi-level / hierarchical index for higher-dimensional data |
| `ExtensionArray` | `core/arrays/base.py:L122` | 397 | Abstract interface for custom array types backed by any storage |
| `RangeIndex` | `core/indexes/range.py:L88` | 428 | Optimized integer index for monotonic integer ranges |
| `DatetimeArray` | `core/arrays/datetimes.py:L163` | 222 | Array of datetime64 data with timezone support |
| `Index` | `core/indexes/base.py:L313` | 212 | Immutable sequence for axis labeling |
| `GroupBy` | `core/groupby/groupby.py:L752` | 76 | Split-apply-combine grouping operation |
| `Resampler` | `core/resample.py:L119` | 290 | GroupBy-like resampling for time-series data |
| `DataFrameGroupBy` | `core/groupby/generic.py:L2090` | 34 | GroupBy for DataFrames with aggregation/transform/apply |

### Additional Key APIs (by degree rank)

| API | Type | Description |
|-----|------|-------------|
| `SeriesGroupBy` | class | GroupBy for Series |
| `TimedeltaArray` | class | Array of timedelta64 data |
| `Categorical` | class | Efficient categorical data representation |
| `merge()` | function | Database-style join of DataFrames |
| `concat()` | function | Concatenate DataFrames along an axis |
| `pivot()` | function | Reshape from long to wide format |
| `pivot_table()` | function | Spreadsheet-style pivot table with aggregation |
| `melt()` | function | Unpivot from wide to long format |
| `read_csv()` | function | Read CSV into DataFrame |
| `read_parquet()` | function | Read Parquet file into DataFrame |
| `to_datetime()` | function | Convert argument to datetime |
| `date_range()` | function | Generate fixed-frequency DatetimeIndex |
| `isna()` | function | Detect missing values |
| `array()` | function | Create pandas ExtensionArray from sequence |

## Common Patterns

### DataFrame Creation and Manipulation
```python
import pandas as pd
import numpy as np

# Creation
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': ['x', 'y', 'z', 'w']
})
df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))

# Index manipulation
df.set_index('A', inplace=False)
df.reset_index(drop=False)
df.sort_values('B', ascending=False)
```

### Data Selection
```python
# Column selection
df['A']                  # Series
df[['A', 'B']]           # DataFrame subset

# Row selection
df.loc[2]                # by label
df.iloc[0:5]             # by position
df.loc[df['A'] > 2]      # boolean indexing
```

### GroupBy (Split-Apply-Combine)
```python
# Group and aggregate
df.groupby('category')['value'].mean()
df.groupby('category').agg({'value': 'mean', 'count': 'sum'})

# Transform (broadcast group stats back to original shape)
df['zscore'] = df.groupby('group')['value'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Apply arbitrary function
df.groupby('group').apply(lambda g: g.nlargest(3, 'value'))
```

### Merge and Join
```python
# Database-style joins
pd.merge(left, right, on='key', how='inner')
pd.merge(left, right, left_on='lkey', right_on='rkey', how='left')

# Concatenation
pd.concat([df1, df2], axis=0)  # stack rows
pd.concat([df1, df2], axis=1)  # combine columns
```

### Reshaping
```python
# Pivot: long → wide
df.pivot(index='date', columns='symbol', values='close')

# Pivot table with aggregation
pd.pivot_table(df, index='date', columns='sector',
               values='return', aggfunc='mean')

# Melt: wide → long
pd.melt(df, id_vars=['date'], value_vars=['AAPL', 'GOOGL'],
        var_name='symbol', value_name='price')
```

### Missing Data
```python
df.dropna(subset=['critical_col'])
df.fillna(method='ffill')   # forward fill
df.fillna(df.mean())         # fill with column means
df.isna().sum()              # count missing per column
```

### I/O
```python
df = pd.read_csv('data.csv', parse_dates=['date'], index_col='date')
df.to_csv('output.csv')
df = pd.read_parquet('data.parquet')
df.to_parquet('output.parquet')
```

## Pitfalls

1. **`inplace=True` is deprecated for most methods**: Prefer assignment: `df = df.drop('col', axis=1)` over `df.drop('col', axis=1, inplace=True)`. The `inplace` parameter will be removed in future pandas versions for most methods.

2. **Chained indexing (`df['A']['B']`) returns a copy, not a view**: Setting values through chained indexing (`df['A']['B'] = 0`) may raise `SettingWithCopyWarning` and not modify the original. Use `df.loc[:, ('A', 'B')]` or `df.at[idx, col]` instead.

3. **`groupby().apply()` can be slow**: `apply` with Python functions bypasses pandas' C-optimized code paths. Prefer built-in aggregations (`mean`, `sum`, `std`), or use `.agg()` with named functions. For complex operations, `.transform()` is generally faster than `.apply()`.

4. **`merge` on float columns can miss matches**: Floating-point precision issues cause `merge` to drop rows that appear identical. Round or convert to categorical before merging: `df['key'] = df['key'].round(6)`.

5. **MultiIndex slicing requires sorted index**: `df.loc[('a', slice(None)), :]` may raise `UnsortedIndexError` if the MultiIndex is not sorted. Always call `df.sort_index()` before positional slicing on MultiIndex.

6. **`concat` with `axis=1` aligns on index**: If indices don't match, NaN is introduced. Use `pd.concat([df1, df2], axis=1, join='inner')` to only keep matching indices, or reset both indices first.

## Cross-Library Bridges

| Bridge | Relation | Description |
|--------|----------|-------------|
| numpy ndarray → pandas DataFrame | `backed_by` | pandas DataFrame is backed by numpy ndarray for numerical storage |
| pandas DataFrame → sklearn `fit()` | `input_to` | pandas DataFrame is the standard input to sklearn estimators |
| pandas → vectorbt Portfolio | `input_to` | pandas DataFrame is the primary data input to vectorbt Portfolio simulation |
| pandas `read_csv()` → sklearn `train_test_split()` | `precedes` | Data loaded via pandas feeds into sklearn train/test splits |
| pandas rolling → ta-lib | `implements` | pandas rolling window underpins ta-lib moving average calculations |

## Verification Checklist

- [ ] `pd.DataFrame({'a': [1,2,3]})` creates a valid DataFrame
- [ ] `df.groupby('key')['val'].mean()` returns a Series
- [ ] `pd.merge(df1, df2, on='key', how='inner')` returns joined DataFrame
- [ ] `df.pivot(index='date', columns='sym', values='close')` reshapes correctly
- [ ] `pd.concat([df1, df2])` stacks rows
- [ ] `pd.read_csv('file.csv')` parses CSV
- [ ] `df.loc[condition]` filters rows correctly
- [ ] `df.isna().sum()` counts missing values
- [ ] `df.sort_values('col')` returns sorted DataFrame
- [ ] `df.reset_index()` moves index to column

## Provenance

- Knowledge graph: pandas, 11368 nodes, 39913 edges, 410 communities
- God nodes: `DatetimeTZDtype` (1582), `CategoricalDtype` (1480), `PeriodDtype` (1087) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ 982854070758, backend opencode, description coverage 81%
