---
name: quantstats-reports
description: "Use when generating quantstats HTML tear-sheet reports — metrics()/full()/basic()/html()/plots(), benchmark preparation, and report embedding."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: ranaroussi/quantstats
source_commit: fbd10daed0227aa0d10da6513f1b15e7e98d7fae
extraction_date: 2026-08-13
graph:
  nodes: 393
  edges: 531
  community_count: 48
  graph_hash: 98393f286b04d0d2
tags:
- quantstats
- reports
- html
- tearsheet
related_skills:
- quantstats
- quantstats-stats
- quantstats-plots
- empyrical-stats
- pandas-core
---

# quantstats.reports

HTML tear-sheet generation: `metrics()` (table), `basic()` (metrics + key plots),
`full()` (the complete report), `html()` (raw HTML string), `plots()` (all plots) —
with benchmark alignment handled internally.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `metrics()` | `reports.py:L1135` | Full metrics table as DataFrame/HTML block |
| `basic()` | `reports.py:L997` | Metrics + key plots (returns, drawdown, rolling) |
| `full()` | `reports.py:L779` | Complete tear-sheet report (metrics + all plots) |
| `html()` | `reports.py:L178` | Returns the report's HTML string without rendering |
| `plots()` | `reports.py:L1835` | All default plots for the returns series |
| `_get_stats()` | `reports.py:L35` | Internal stats accessor used by the report layers |
| `_get_utils()` | `reports.py:L43` | Internal utils accessor |
| `_match_dates()` | `reports.py:L138` | Align returns and benchmark dates |
| `_prepare_returns()` | `utils.py:L583` | Normalize the returns series for analytics |
| `_prepare_benchmark()` | `utils.py:L702` | Normalize the benchmark series |
| `to_prices()` | `utils.py:L299` | Convert returns to a price index for plotting |
| `_calc_dd()` | `reports.py:L2185` | Drawdown calculation for the report sections |
| `_print_parameters_table()` | `reports.py:L100` | Parameters/context table for the report header |
| `_download_html()` | `reports.py:L2377` | Fetch remote HTML assets for the report |
| `QuantStatsError` | `utils.py:L34` | Library exception type |
| `DataValidationError` | `utils.py:L40` | Input validation error |

## Common Patterns

- **One-call report**: `qs.reports.full(returns, benchmark="SPY")` — full HTML tear
  sheet saved/rendered; the default entry point.
- **Embedding**: `qs.reports.html(returns)` returns the string — embed in an email or
  a dashboard.
- **Benchmark-relative**: pass the benchmark returns or a ticker; `_match_dates`
  aligns the two series before any metric is computed.
- **Report pipeline**: `metrics()` for the table, `plots()` for the charts,
  `basic()` when the standard set suffices.
- **Notebook display**: `qs.reports.full(returns, output=False)` then `display(HTML(...))`
  via the html string.

## Pitfalls

- **Frequency assumption**: quantstats assumes daily data by default — pass
  `periods_per_year`/`trading_periods` explicitly for weekly/monthly input.
- **Benchmark alignment**: returns and benchmark must overlap; `_match_dates` silently
  trims to the intersection — a short overlap silently shrinks the sample.
- **HTML assets**: `_download_html` fetches remote assets — offline rendering may
  degrade the report's styling.
- **Data validation**: `DataValidationError` on non-numeric/NaN-heavy inputs — clean
  the series before `full()`.

## Provenance

Graph: `knowledge_graphs/quantstats/.graphify/graph.json` — 393 nodes · 531 edges ·
48 communities · graphify @ fbd10daed022, backend opencode, description coverage 93.5%.

## Verification Checklist

- [ ] `qs.reports.metrics(returns)` returns a populated table
- [ ] `qs.reports.html(returns)` returns a non-empty HTML string
- [ ] QR rows cite `reports.py:L*` / `utils.py:L*` resolvable in the quantstats graph
