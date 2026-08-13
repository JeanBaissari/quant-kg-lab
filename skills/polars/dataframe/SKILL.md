---
name: polars-dataframe
description: "Use when working with polars DataFrames and Series — construction, schema control, group_by/join/reshape operations, and pandas interop."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: pola-rs/polars
source_commit: 1f779c90256872c50a16622ce0e4e4f11e885b1a
extraction_date: 2026-08-12
graph:
  nodes: 5296
  edges: 16925
  community_count: 485
  graph_hash: 4c9e707cde1bc95a
tags:
- polars
- dataframe
- series
- schema
- joins
related_skills:
- polars
- polars-expressions
- polars-io
- polars-lazyframe
- pandas-core
- numpy-core
---

# polars.dataframe

The eager DataFrame/Series API: construction, schemas, row/column access,
`group_by`/`join`/`reshape` operations, and type handling — the polars
counterpart to pandas.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `DataFrame` | `dataframe/frame.py:L204` | The eager tabular structure — select/filter/group_by/join |
| `Series` | `series/series.py:L287` | One-dimensional column with dtype + name — deg 287 hub |
| `Schema` | `schema.py` | Column-name → dtype mapping object |
| `LazyFrame` | `lazyframe/frame.py:L253` | Lazy query plan — collect()/sink_* executes it |
| `DataFrame.group_by` | `dataframe/group_by.py` | Grouped aggregation — `df.group_by("k").agg(...)` |
| `DataFrame.join` | `dataframe/frame.py` | Join two frames — how="inner/left/outer/cross/asof" |
| `DataFrame.melt` | `dataframe/frame.py` | Wide → long reshape (unpivot) |
| `DataFrame.pivot` | `dataframe/frame.py` | Long → wide reshape (pivot) |
| `DataFrame.rename` | `dataframe/frame.py` | Rename columns — `df.rename({"old": "new"})` |
| `DataFrame.with_columns` | `dataframe/frame.py` | Add/overwrite columns with expressions |
| `DataFrame.unique` | `dataframe/frame.py` | Distinct rows — `keep="first/last/none"` |
| `DataFrame.explode` | `dataframe/frame.py` | Expand list columns into one row per element |
| `DataFrame.head/tail` | `dataframe/frame.py` | First/last n rows |
| `DataFrame.sample` | `dataframe/frame.py` | Random rows — `fraction`, `with_replacement`, `seed` |
| `DataFrame.to_pandas` | `dataframe/frame.py` | Convert to pandas (zero-copy where possible) |
| `pl.from_pandas` | `_reexport.py` | Build a polars DataFrame from pandas |
| `pl.from_numpy` | `_reexport.py` | Build from a numpy array (orient/columns) |
| `DataFrame.describe` | `dataframe/frame.py` | Summary statistics (count/mean/std/min/max) |
| `DataFrame.is_empty` | `dataframe/frame.py` | True when zero rows |
| `DataFrame.write_parquet` | `dataframe/frame.py` | Eager write — `df.write_parquet("f.parquet")` |

## Common Patterns

- **Construction with schema**: 
  ```python
  pl.DataFrame({"date": [...], "px": [...]}, schema={"date": pl.Date, "px": pl.Float64})
  ```
  — explicit schema avoids inference surprises.
- **Factor frame pipeline**: `df.with_columns(pl.col("ret").rank().over("date"))` then
  `df.group_by("date").agg(pl.col("ret").qcut(...))` — cross-sectional factor work.
- **Joins**: `df1.join(df2, on=["date", "ticker"], how="left")` — on a list of
  keys; `how="asof"` for nearest-timestamp merges.
- **Wide→long**: `df.melt(id_vars=["date"], value_vars=["px", "vol"])` — the
  standard reshape before group operations.
- **Long→wide**: `df.pivot(index="date", columns="ticker", values="ret")` —
  build a returns matrix for portfolio math.
- **Interop**: `df.to_pandas()` at the boundary for sklearn/optuna work;
  `pl.from_numpy(arr, schema=[...])` from numpy arrays.

## Pitfalls

- **Strictness**: polars is strict about dtypes — mismatches raise rather than
  coerce. Cast explicitly with `.cast(pl.Float64)`.
- **Null semantics**: missing data is explicit `null`; joins/aggregations treat
  it strictly (left join introduces nulls on the right side by design).
- **Index-less**: polars has no row index — row position is implicit; keep an
  explicit id/date column for alignment.
- **group_by returns groups by default**: use `df.group_by(...).len()` or
  `.agg(...)`; a bare group_by does nothing until an aggregation is applied.
- **join duplicate keys**: duplicate join keys multiply rows — dedupe with
  `.unique()` first if the relation should be one-to-many.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `df.group_by("k").agg(pl.col("v").mean())` works on a small frame
- [ ] `df.melt`/`pivot` round-trip a wide matrix
- [ ] QR rows cite `dataframe/*.py` files resolvable in the polars graph
