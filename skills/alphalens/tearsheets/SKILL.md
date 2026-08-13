---
name: alphalens-tearsheets
description: "Use when generating alphalens tear sheets — returns, IC, and event-study visual reports for factor research."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: quantopian/alphalens
source_commit: 77084f1e4c2c0be407e032d444fb19e4be4b0f37
extraction_date: 2026-08-12
graph:
  nodes: 172
  edges: 231
  community_count: 5
  graph_hash: b1726a0e2484f41b
tags:
- alphalens
- tearsheets
- reporting
related_skills:
- alphalens
- alphalens-factor-analysis
---

# alphalens.tearsheets

Reporting layer: one-call tear sheets for returns, IC, and event studies — the
factor-research output format that feeds pyfolio for portfolio-level reporting.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `create_returns_tear_sheet()` | `tears.py` | Returns tear sheet: quantile cumulative returns, spread, and turnover |
| `create_information_tear_sheet()` | `tears.py` | IC tear sheet: IC time series, histogram, QQ, and mean IC by quantile |
| `create_event_returns_tear_sheet()` | `tears.py` | Event-study returns around an event window |
| `create_event_study_tear_sheet()` | `tears.py` | Event study: abnormal returns and cumulative abnormal returns |
| `GridFigure` | `tears.py` | Coordinates tear sheet charts across a grid of subplots |
| `plotting.py` | `plotting.py` | Style contexts and chart helpers for tear sheets |

## Common Patterns

- **Quick report**: `alphalens.tears.create_returns_tear_sheet(factor_data)` — full
  quantile/IC/turnover report in one call.
- **IC deep-dive**: `create_information_tear_sheet(factor_data)` after the returns sheet.
- **Event studies**: `create_event_study_tear_sheet(returns, events, ...)` for
  announcements/data releases.

## Pitfalls

- **Display backend**: tear sheets call `plt.show()` — run in a notebook or headless-safe
  context with a matplotlib backend configured.
- **Data volume**: full sheets on large universes are slow; use `by_group`/subsetting for
  exploration.

## Provenance

Graph: `knowledge_graphs/alphalens/.graphify/graph.json` — 172 nodes · 231 edges ·
5 communities · graphify @ 77084f1e4c2c, backend opencode, description coverage 86.8%.

## Verification Checklist

- [ ] `create_returns_tear_sheet` renders with a synthetic factor
- [ ] QR rows cite source files resolvable in the alphalens graph
