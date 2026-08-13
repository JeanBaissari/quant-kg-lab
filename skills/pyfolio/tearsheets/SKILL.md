---
name: pyfolio-tearsheets
description: "Use when generating portfolio tear sheets with pyfolio — create_returns_tear_sheet, create_full_tear_sheet, and performance statistics."
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
  graph_hash: cc432015b7700967
tags:
- pyfolio
- tearsheets
- performance
related_skills:
- pyfolio
- pyfolio-timeseries
- alphalens-tearsheets
---

# pyfolio.tearsheets

Portfolio reporting: tear sheets assembled from returns/positions/transactions —
the reporting layer of the factor-research stack (alphalens feeds it).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `create_full_tear_sheet()` | `tears.py` | Assembles the full pyfolio report combining returns, positions, transactions and round trips |
| `create_returns_tear_sheet()` | `tears.py` | Returns tear sheet: cumulative returns, drawdown, rolling Sharpe, monthly heatmap |
| `create_position_tear_sheet()` | `tears.py` | Position concentration and sector exposure charts |
| `create_transaction_tear_sheet()` | `tears.py` | Turnover and transaction-cost analysis |
| `create_round_trip_tear_sheet()` | `tears.py` | Round-trip (per-trade) performance analysis |
| `tears.py` | `tears.py` | Module implementing pyfolio tear sheets and their assemblies |

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
