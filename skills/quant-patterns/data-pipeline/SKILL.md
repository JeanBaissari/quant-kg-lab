---
name: quant-data-pipeline
description: "Use when moving data between pandas, polars, and numpy — conversion, alignment, concatenation, and efficient cross-framework data flow for quant workloads."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [pandas-core, polars-dataframe, numpy-core]
tags: [quantitative-finance, data-pipeline, pandas, polars, numpy, workflow]
related_skills: [pandas-core, polars-dataframe, numpy-core]
target_version: cross-lib
---

# Quant Data Pipeline (pandas <-> polars <-> numpy)

Data in quant pipelines lives in three worlds: pandas for time-indexed I/O and analysis, polars for
high-speed joins and lazy evaluation, and numpy as the numeric substrate for ML and indicators. This
playbook chains them without losing dtype fidelity or index semantics.

## Steps

1. **Load with the right tool** — use polars for large CSVs (lazy scan), pandas when you need
   DatetimeIndex semantics, numpy when you already have arrays.
   ```python
   import polars as pl
   lf = pl.scan_csv("ohlcv.csv")          # polars lazy — push-down predicates
   df = pd.read_csv("ohlcv.csv", parse_dates=["date"], index_col="date")  # pandas
   ```
2. **Convert polars -> pandas** — `DataFrame.to_pandas()` preserves dtypes; use `use_pyarrow=True`
   for Arrow-backed speed on large frames.
   ```python
   pdf = lf.collect().to_pandas()          # polars.DataFrame -> pandas.DataFrame
   ```
   *Citation*: `polars/dataframe/frame.py:L2533`
3. **Convert pandas -> numpy** — `DataFrame.to_numpy()` or `.values` for the raw ndarray; specify
   `dtype` explicitly to avoid silent upcast.
   ```python
   arr = df.to_numpy(dtype=np.float64)     # pandas.DataFrame -> ndarray
   ```
   *Citation*: `polars/dataframe/frame.py:L1932`
4. **Concat / merge / join** — pandas for label-aware merges (`merge`, `join`), polars for
   positional and key-based joins at scale; numpy `concatenate` for raw array stacking.
   ```python
   pd.concat([df1, df2], axis=0)           # vertical stack
   df1.merge(df2, on="date", how="left")   # database-style join
   pl.concat([lf1, lf2], how="vertical")   # polars stack
   ```
   *Citations*: `pandas/core/reshape/merge.py:L149`, `pandas/core/frame.py:L15269`
5. **Round-trip without data loss** — polars `to_pandas()` then `to_numpy()` preserves the numeric
   core; going the other direction, wrap a numpy array in `pd.DataFrame` then `.to_polars()`.
   ```python
   arr = pdf.to_numpy(dtype=np.float64)    # pandas -> numpy
   pdf2 = pd.DataFrame(arr, columns=cols)  # numpy -> pandas
   pl_df = pl.from_pandas(pdf2)            # pandas -> polars
   ```
6. **Index alignment** — when merging pandas with polars-derived data, always reset/set the index
   explicitly; polars has no index concept, so mismatched index semantics silently produce wrong rows.

## Pitfalls

1. **Index handling** — polars has no index; converting `polars -> pandas` assigns a RangeIndex by
   default. If you need date alignment, set the index yourself before merging with time-indexed data.
2. **Null semantics differ** — pandas `NaN` is float-only; polars has typed nulls (`null` vs `NaN`).
   Converting polars nullable integers to pandas can cast to float64 silently.
3. **Dtype drift** — `DataFrame.to_numpy()` without `dtype=` infers from the data, which can produce
   `object` arrays when columns mix types. Always pin `dtype=np.float64` for numeric work.
4. **Copy-on-write (CoW)** — pandas >= 2.0 enables CoW by default; chained assignments like
   `df["a"][mask] = val` no longer mutate in place. Use `.loc` or `.iloc` for explicit mutation.

## Composed Skills & Bridges

| Source | Target | Relation | Description |
|--------|--------|----------|-------------|
| pandas-core | polars-dataframe | converts_to | `DataFrame.to_pandas()` / `pl.from_pandas()` round-trip |
| polars-dataframe | numpy-core | converts_to | `.to_numpy()` / `np.asarray()` for numeric core |
| pandas-core | numpy-core | converts_to | `DataFrame.to_numpy()` / `np.array(df)` |
| pandas-core | polars-dataframe | performance | polars joins are 5-10x faster on large frames |
| numpy-core | pandas-core | wraps_into | `pd.DataFrame(arr)` to add index/columns |
| polars-dataframe | pandas-core | ecosystem | most ML/stats libs expect pandas; convert at boundary |

## Related Skills

- [[pandas-core]]
- [[polars-dataframe]]
- [[numpy-core]]
