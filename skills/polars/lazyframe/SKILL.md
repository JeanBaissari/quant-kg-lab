---
name: polars-lazyframe
description: "Use when working with polars LazyFrame \u2014 building lazy query plans,\
  \ collect/sink execution, query planning (explain/inspect), and SQLContext."
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
- lazyframe
- query-plan
- streaming
related_skills:
- polars
- polars-io
- polars-expressions
- polars-performance
- polars-dataframe
target_version: '1.43.2 (dev: after 1.43.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `polars` ahead of the latest PyPI release (1.43.2 (dev: after 1.43.2)). Some APIs may not exist in your installed version.

# polars.lazyframe

Lazy query planning: build a computation graph with `scan_*` + expression
transformations, then execute with `collect` (in-memory) or `sink_*`
(streaming). The optimizer reorders/combines operations before execution.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `LazyFrame` | `lazyframe/frame.py:L253` | Lazy query plan over a DataFrame or scan — the LazyFrame type |
| `.collect()` | `lazyframe/frame.py:L253` | Execute the plan into a DataFrame (in-memory) |
| `.sink_parquet()` | `lazyframe/frame.py:L2822` | Streaming execution writing parquet — bounded memory |
| `.sink_csv()` | `lazyframe/frame.py:L3780` | Streaming execution writing CSV |
| `.sink_ipc()` | `lazyframe/frame.py:L3521` | Streaming execution writing IPC |
| `.sink_ndjson()` | `lazyframe/frame.py:L4145` | Streaming execution writing NDJSON |
| `.sink_delta()` | `lazyframe/frame.py:L3151` | Streaming execution writing a Delta table |
| `.sink_iceberg()` | `lazyframe/frame.py:L3467` | Streaming execution writing an Iceberg table |
| `.explain()` | `lazyframe/frame.py:L1290` | Show the (optimized) query plan as text |
| `.show_graph()` | `lazyframe/frame.py:L1451` | Render the query plan as a Graphviz graph |
| `.inspect()` | `lazyframe/frame.py:L1662` | Inspect a node in the computation graph during execution |
| `.sql()` | `lazyframe/frame.py:L1812` | Execute a SQL query against the LazyFrame (`lf.sql("SELECT * FROM self WHERE ...")`) |
| `.schema()` | `lazyframe/frame.py:L649` | Schema of the plan — resolves without executing |
| `.columns()` | `lazyframe/frame.py:L565` | Column names of the plan |
| `.dtypes()` | `lazyframe/frame.py:L607` | Column dtypes of the plan |
| `.sort()` | `lazyframe/frame.py:L1690` | Sort by columns (stable) |
| `.pipe()` | `lazyframe/frame.py:L919` | Pipe the plan through a function (with schema hint via `.pipe_with_schema`) |
| `.describe()` | `lazyframe/frame.py:L1062` | Summary statistics as a DataFrame |
| `.cache()` | `lazyframe/frame.py:L4654` | Materialize + reuse this node in the plan (memoization) |
| `.fetch()` | `lazyframe/frame.py:L4602` | Collect a small number of rows for debugging (deprecated — use `.limit(n).collect()`) |
| `.profile()` | `lazyframe/frame.py:L2066` | Execution profile: per-node timing (deprecated — see `collect(profile=True)`) |
| `SQLContext` | `sql/context.py:L91` | Register LazyFrames/DataFrames under names; run SQL across them |
| `LazyGroupBy` | `lazyframe/group_by.py:L24` | Lazy grouped aggregation — `lf.group_by(...).agg(...)` |
| `QueryOptFlags` | `lazyframe/opt_flags.py:L25` | Optimization flags: projection pushdown, predicate pushdown, streaming, etc. |
| `GPUEngine` | `lazyframe/engine_config.py:L11` | GPU execution engine configuration |

## Common Patterns

- **Build lazy, collect once**: assemble `scan_parquet` + filters + joins +
  aggregations as a plan, `collect()` at the end — the optimizer pushes
  predicates down into the scan.
- **SQL over polars**: 
  ```python
  ctx = pl.SQLContext(df=lf, trades=lf2)
  result = ctx.execute("SELECT ticker, SUM(px * qty) AS notional FROM trades GROUP BY ticker").collect()
  ```
- **Streaming pipeline**: `pl.scan_parquet("big/*.parquet").filter(...).sink_parquet("out.parquet")`
  — never materializes the full dataset.
- **Plan inspection**: `lf.explain()` before `collect()` to verify predicate
  pushdown actually happened (`FILTER` under the scan node).
- **Multi-query reuse**: `lf.cache()` when the same plan node feeds several
  downstream branches — avoids recomputation.
- **Lazy joins**: join two `scan_parquet` plans and only the required columns
  are read from either side.

## Pitfalls

- **Eager surprise**: methods on a LazyFrame never execute — forgetting
  `.collect()` leaves you with a plan object, and `print(lf)` shows the plan,
  not data.
- **`sink_*` is streaming**: unlike `collect()`, `sink_parquet` does not return
  a DataFrame — if you need both, `collect()` once or use `.collect().write_parquet()`.
- **SQLContext scope**: tables registered in one context are not visible in a
  new `pl.SQLContext()` — register per context.
- **Deprecated APIs**: `.fetch()`, `.profile()` are deprecated in this polars
  version — use `.limit(n).collect()` and `collect(profile=True)`.
- **`inspect()` cost**: per-row callbacks in `inspect` slow streaming pipelines
  substantially — use for debugging only.
- **Optimizer surprises**: type-mismatched predicates can block pushdown —
  `lf.explain()` is the ground truth for whether the optimizer did its job.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `pl.scan_parquet(f).filter(...).collect()` works and `explain()` shows pushdown
- [ ] `SQLContext` query executes over a registered LazyFrame
- [ ] QR rows cite `lazyframe/*.py` / `sql/*.py` files resolvable in the polars graph
