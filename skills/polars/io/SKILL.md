---
name: polars-io
description: "Use when reading or writing data with polars \u2014 CSV/Parquet/IPC/JSON/NDJSON/Arrow,\
  \ lazy scan/sink streaming, database and cloud sources."
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
- io
- parquet
- csv
- streaming
related_skills:
- polars
- polars-lazyframe
- polars-dataframe
- pandas-core
- numpy-core
target_version: '1.43.2 (dev: after 1.43.2)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `polars` ahead of the latest PyPI release (1.43.2 (dev: after 1.43.2)). Some APIs may not exist in your installed version.

# polars.io

File and stream I/O for polars: eager readers (`read_*`), lazy scans
(`scan_*`), and streaming sinks (`sink_*`). Parquet/IPC round-trips preserve
schema and compression; CSV/JSON are schema-inferred on read.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `read_csv` | `io/csv/functions.py:L65` | Eager CSV read — schema inference, dtypes, missing-value handling |
| `scan_csv` | `io/csv/functions.py:L1107` | Lazy CSV scan — no data read until `collect()` |
| `read_csv_batched` | `io/csv/functions.py:L772` | Batched CSV reader — chunked processing for very large files |
| `read_parquet` | `io/parquet/functions.py:L55` | Eager Parquet read — column pruning + predicate pushdown |
| `scan_parquet` | `io/parquet/functions.py:L467` | Lazy Parquet scan — the default for large parquet datasets |
| `read_parquet_schema` | `io/parquet/functions.py:L363` | Read only the schema of a parquet file |
| `read_parquet_metadata` | `io/parquet/functions.py:L391` | File metadata: row count, column stats |
| `read_ipc` | `io/ipc/functions.py:L48` | Arrow IPC (feather v2) read — fastest round-trip format |
| `read_ipc_stream` | `io/ipc/functions.py:L266` | IPC stream variant (schema + record batches, no footer) |
| `scan_ipc` | `io/ipc/functions.py:L397` | Lazy IPC scan |
| `read_json` | `io/json/read.py:L22` | JSON read — `pl.read_json(path, format="lines"|"json")` |
| `read_ndjson` | `io/ndjson.py:L28` | Newline-delimited JSON read |
| `scan_ndjson` | `io/ndjson.py:L192` | Lazy NDJSON scan |
| `read_avro` | `io/avro.py:L18` | Avro read (Hadoop-ecosystem columnar format) |
| `scan_arrow_c_stream` | `io/arrow_c_stream.py:L21` | Scan an Arrow C stream (PyArrow interop) |
| `read_database` | `io/database/functions.py:L25` | SQL read via SQLAlchemy/Arrow Flight — returns DataFrame |
| `read_database_uri` | `io/database/functions.py:L296` | SQL read from a connection URI |
| `read_delta` | `io/delta/functions.py:L23` | Delta Lake table read (delta-rs) |
| `scan_delta` | `io/delta/functions.py:L162` | Lazy Delta Lake scan |
| `scan_iceberg` | `io/iceberg/functions.py:L27` | Lazy Iceberg table scan |
| `read_excel` | `io/spreadsheet/functions.py:L118` | Excel read — sheet selection, header rows, dtype hints |
| `read_ods` | `io/spreadsheet/functions.py:L435` | LibreOffice ODS spreadsheet read |

## Common Patterns

- **Lazy parquet pipeline**: `pl.scan_parquet("data/*.parquet")` →
  `.filter(...).group_by(...).agg(...)` → `.collect()` — schema is known up
  front, so filters push down into the reader.
- **Column pruning**: `scan_parquet(path, columns=["date", "px"])` reads only
  those columns — for wide factor files this is the single biggest I/O win.
- **Streaming out**: `lf.sink_parquet("out.parquet")` (or `sink_ipc`/`sink_csv`)
  — streaming write with bounded memory, unlike `collect()` + `write_parquet`.
- **CSV to parquet ETL**: `scan_csv("raw.csv").sink_parquet("clean.parquet")` —
  the canonical polars ETL move; schema is fixed on the parquet side.
- **Batched CSV**: `pl.read_csv_batched(path, batch_size=100_000)` →
  `next(batches)` — process chunks without loading the file into memory.
- **SQL sources**: `pl.read_database("SELECT date, close FROM prices WHERE ticker = %(t)s", uri, params={"t": "AAPL"})`.
- **JSON lines**: `pl.read_ndjson("trades.jsonl")` — one JSON object per line;
  use `format="lines"` for regular JSON arrays.

## Pitfalls

- **Schema inference drift**: CSV/JSON infer dtypes per file — two files with
  the same shape can infer different dtypes. Pin `schema`/`dtypes` explicitly
  for multi-file reads, or normalize through a first `read_parquet` step.
- **CSV nulls**: empty strings are null by default (`null_values=[""]` to keep
  them, or `pl.Null` handling in `infer_schema_length`).
- **scan vs read**: `read_*` returns an eager DataFrame; `scan_*` returns a
  LazyFrame that needs `collect()` — mixing them silently materializes data.
- **IPC vs parquet**: IPC is fastest but single-version; parquet is the
  portable/compressible long-term format. Use IPC for scratch, parquet for
  artifacts.
- **`read_database` drivers**: engine differs by connection string (SQLAlchemy
  vs Arrow Flight); pass `engine="arrow"` where supported for speed.
- **Excel**: only the first sheet is read unless `sheet_name` is passed; dtype
  inference across merged cells is lossy — cast after read.

## Provenance

Graph: `knowledge_graphs/polars/.graphify/graph.json` — 5296 nodes · 16925 edges ·
485 communities · graphify @ 1f779c902568, backend opencode, description coverage 81.6%.

## Verification Checklist

- [ ] `pl.scan_parquet("x.parquet").collect()` round-trips schema from `read_parquet`
- [ ] `pl.scan_csv(f).sink_parquet(g)` produces a valid parquet file
- [ ] QR rows cite `io/*.py` files resolvable in the polars graph
