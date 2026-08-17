---
name: pyfolio-tearsheets
description: "Use when generating portfolio tear sheets with pyfolio \u2014 create_returns_tear_sheet,\
  \ create_full_tear_sheet, and performance statistics."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: quantopian/pyfolio
source_commit: 4b901f6d73aa02ceb6d04b7d83502e5c6f2e81aa
extraction_date: 2026-08-12
graph:
  nodes: 305
  edges: 361
  community_count: 61
  graph_hash: e3709d355d12539e
tags:
- pyfolio
- tearsheets
- performance
related_skills:
- pyfolio
- pyfolio-timeseries
- alphalens-tearsheets
target_version: '0.9.2 (dev: after 0.9.2)'
upstream_status: dead
---

## Version Note

> ⚠️ **Upstream is frozen** (no commits since the pin). This skill describes `pyfolio` at its pinned commit — an abandoned release line. Target version: 0.9.2 (dev: after 0.9.2). Verify against your installed version before use.

# pyfolio.tearsheets

Portfolio reporting: tear sheets assembled from returns/positions/transactions —
the reporting layer of the factor-research stack (alphalens feeds it).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `create_full_tear_sheet()` | `tears.py:L55` | Assembles the full pyfolio report combining returns, positions, transactions and round trips |
| `create_simple_tear_sheet()` | `tears.py:L231` | Lightweight report: returns + headline stats only |
| `create_returns_tear_sheet()` | `tears.py:L409` | Returns tear sheet: cumulative returns, drawdown, rolling Sharpe, monthly heatmap |
| `create_position_tear_sheet()` | `tears.py:L599` | Position concentration and sector exposure charts |
| `create_txn_tear_sheet()` | `tears.py:L694` | Turnover and transaction-cost analysis |
| `create_round_trip_tear_sheet()` | `tears.py:L780` | Round-trip (per-trade) performance analysis |
| `create_interesting_times_tear_sheet()` | `tears.py:L870` | Drawdown-period behavior drill-down |
| `create_capacity_tear_sheet()` | `tears.py:L954` | Capacity/liquidity analysis of the strategy |
| `create_perf_attrib_tear_sheet()` | `tears.py:L1066` | Factor attribution of performance |

## Common Patterns

- **Full report**: `pyfolio.create_full_tear_sheet(returns, positions, transactions, benchmark_rets)` —
  the complete battery in one call.
- **Quick check**: `create_returns_tear_sheet(returns, benchmark_rets)` — headline stats
  (annual vol, Sharpe, max drawdown) without positions data.
- **From alphalens**: `alphalens.performance.create_pyfolio_input(factor_data)` → feed the
  outputs to the tear sheets.
- **Benchmarks**: pass `benchmark_rets` for alpha/beta and benchmark comparison plots.

## Pitfalls

- **Frequency**: returns must be daily and benchmark-aligned; intraday data breaks the stats.
- **Display backend**: tear sheets call `plt.show()` — headless runs need a matplotlib
  backend configured.
- **Round-trip cost**: without transactions, turnover/cost panels are skipped — pass them
  for the full picture.

## Provenance

Graph: `knowledge_graphs/pyfolio/.graphify/graph.json` — 305 nodes · 361 edges ·
61 communities · graphify @ 4b901f6d73aa, backend opencode, description coverage 80.4%.

## Verification Checklist

- [ ] `create_returns_tear_sheet(returns, benchmark_rets)` renders with synthetic data
- [ ] QR rows cite source files resolvable in the pyfolio graph
