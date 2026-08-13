---
name: mplfinance
description: "Use when charting financial data with mplfinance — plot() with candle/OHLC/line/renko/pnf types, addplot overlays, styles, volume panels, and market colors."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: matplotlib/mplfinance
source_commit: 493811dac9a203de7ec148fb95504e7d3f400ba5
extraction_date: 2026-08-13
graph:
  nodes: 244
  edges: 317
  community_count: 12
  graph_hash: 9e4084dc3d4e6492
tags:
- mplfinance
- charting
- candlestick
- matplotlib
- visualization
related_skills:
- quantstats-plots
- pandas-core
- ta-lib-indicators
- numpy-core
---

# mplfinance

Matplotlib-based financial charting: `mpf.plot()` renders OHLCV data as candles/OHLC/
line/renko/point-and-figure with styles, volume panels, moving averages, and addplot
overlays — the charting layer for strategy and factor reviews.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `plot()` | `plotting.py:L402` | The main entry — type/style/volume/mav/addplot/panels/figscale |
| `make_addplot()` | `plotting.py:L1422` | Build an overlay series (indicator/MA) for a panel |
| `make_marketcolors()` | `_styles.py:L282` | Custom up/down/edge market colors |
| `make_mpf_style()` | `_styles.py` | Compose a full style from a base + market colors |
| `candlestick2_ohlc()` | `original_flavor.py:L555` | Legacy candle primitive (original_flavor API) |
| `plot_day_summary2_ohlc()` | `original_flavor.py:L411` | Daily OHLC summary plot |
| `Mpf_Figure` | `_mplwraps.py:L65` | The figure wrapper returned by plot() |
| `IntegerIndexDateTimeFormatter` | `_utils.py:L1251` | X-axis date formatter for integer-indexed frames |

## Common Patterns

- **Standard candle chart**:
  ```python
  import mplfinance as mpf
  mpf.plot(df, type="candle", style="yahoo", volume=True, mav=(20, 50))
  ```
- **Indicator overlay**: `mpf.make_addplot(sma20, panel=0)` then `addplot=[sma20_plot]`
  — overlay moving averages, bands, or signal markers on the price panel.
- **Multi-panel**: `mpf.plot(df, addplot=[vol_norm, rsi], panel_ratios=(3, 1, 1))` —
  indicators in their own panels below price.
- **Chart types**: `type="renko"` (trend filtering), `type="pnf"` (point-and-figure),
  `type="ohlc"`/`"line"` for compressed views.
- **Headless output**: `mpf.plot(df, savefig="chart.png")` — no display needed
  (backend-agnostic for CI/reports).
- **Return figure**: `fig, axes = mpf.plot(df, returnfig=True)` — post-process axes
  for report embedding.

## Pitfalls

- **Index requirements**: the DataFrame needs a datetime index — integer/string
  indices produce broken x-axes unless `IntegerIndexDateTimeFormatter` handles them.
- **OHLCV column names**: mplfinance expects `Open/High/Low/Close/Volume` (case-
  insensitive) — rename before plotting or pass `axtitle`/`columns` overrides.
- **addplot length**: overlay series must match the price series length — mismatched
  lengths raise or silently misalign.
- **Style inheritance**: custom styles build on `base_mpf_style` — a missing base
  falls back oddly; always pass the base explicitly.
- **Non-trading rows**: NaNs/weekends in the input distort candle spacing — pre-filter
  to trading days.

## Provenance

Graph: `knowledge_graphs/mplfinance/.graphify/graph.json` — 244 nodes · 317 edges ·
12 communities · graphify @ 493811dac9a2, backend opencode, description coverage 100%.

## Verification Checklist

- [ ] `mpf.plot(df, type="candle", volume=True, savefig="t.png")` renders headless
- [ ] `make_addplot(series)` overlays on the price panel
- [ ] QR rows cite `plotting.py`/`addplot.py`/`_styles.py` resolvable in the mplfinance graph
