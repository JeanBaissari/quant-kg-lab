---
name: polars-dataframe
description: "Use when working with polars DataFrames and Series — construction, IO (read/scan parquet+csv), schema, and the eager API."
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
- io
related_skills:
- polars
- polars-expressions
- polars-performance
- pandas-core
---

# polars.dataframe

Eager DataFrame/Series API: construction, schemas, IO (`read_parquet`, `read_csv`,
`scan_*`), and type handling — the polars counterpart to pandas.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `DataFrame` | `dataframe/base.py` | The eager tabular structure — select/filter/group_by/join |
| `Series` | `series/series.py` | One-dimensional column with dtype + name |
| `Schema` | `schema.py` | Column-name → dtype mapping object |
| `LazyFrame` | `lazyframe/base.py` | Lazy query plan — collect()/sink_* executes it |
| `QueryOptFlags` | `lazyframe/opt_flags.py` | Lazy-query optimization flags |
| `exceptions.py` | `exceptions.py` | Error types: ShapeError, ComputeError, ModuleUpgradeRequiredError |

## Common Patterns

- **IO**: `pl.read_csv("data.csv")`, `pl.read_parquet("f.parquet")`, `pl.scan_parquet(dir)` for
  lazy streaming reads.
- **Schema control**: `df = pl.DataFrame(data, schema={'a': pl.Int64, 'b': pl.String})`.
- **Eager vs lazy**: build with `pl.DataFrame` for small data; `LazyFrame` +
  `.collect()` for pipelines.
- **Conversions**: `df.to_pandas()` for interop; `pl.from_pandas(df)` the reverse.

## Pitfalls

- **Strictness**: polars is strict about dtypes — mismatches raise rather than coerce.
- **Null semantics**: missing data is explicit `null`; joins/aggregations treat it strictly.
- **Index-less**: polars has no row index — row position is implicit; keep an id column.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `pl.DataFrame({"a": [1, 2]})` round-trips to pandas
