---
name: ta
description: "Use when computing technical indicators with ta \u2014 pure-Python pandas-native\
  \ indicators (trend/momentum/volatility/volume), add_all_ta_features, and the ta-lib\
  \ alternative without the system C library."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: bukosabino/ta
source_commit: a890410710a6e483c9ba08da7f3dd5089e4b9dff
extraction_date: 2026-08-13
graph:
  nodes: 538
  edges: 1208
  community_count: 42
  graph_hash: cbe70e45f62aaff1
tags:
- ta
- technical-analysis
- indicators
- pandas
related_skills:
- ta-lib-indicators
- pandas-core
- vectorbt-signals
- mplfinance
- quantstats-plots
target_version: '0.11.0 (dev: after 0.11.0)'
upstream_status: stale
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `ta` ahead of the latest PyPI release (0.11.0 (dev: after 0.11.0)). Some APIs may not exist in your installed version.

# ta

Pure-Python technical-analysis library (the pandas-native successor to the dead
pandas-ta niche): indicator families in trend/momentum/volatility/volume modules,
plus `add_all_ta_features` for one-call feature expansion. No system C library
needed (unlike ta-lib).

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `IndicatorMixin` | `utils.py:L14` | Base class — the shared indicator API (deg 259 hub) |
| `add_all_ta_features` | `wrapper.py:L543` | Add the full indicator suite as new DataFrame columns |
| `RSIIndicator` | `momentum.py:L14` | RSI — relative strength over a window |
| `StochasticOscillator` | `momentum.py:L217` | Stochastic %K/%D |
| `StochRSIIndicator` | `momentum.py:L549` | Stochastic of RSI |
| `MACD` | `trend.py:L84` | MACD line/signal/histogram |
| `ADXIndicator` | `trend.py:L678` | Average Directional Index |
| `IchimokuIndicator` | `trend.py:L340` | Ichimoku cloud |
| `AroonIndicator` | `trend.py:L14` | Aroon up/down |
| `PSARIndicator` | `trend.py:L934` | Parabolic SAR |
| `VortexIndicator` | `trend.py:L863` | Vortex VI+ / VI- |
| `KSTIndicator` | `trend.py:L440` | Know Sure Thing oscillator |
| `BollingerBands` | `volatility.py:L67` | Bollinger bands (MA ± k·std) |
| `AverageTrueRange` | `volatility.py:L14` | ATR — average true range |
| `KeltnerChannel` | `volatility.py:L183` | Keltner channel (EMA ± ATR multiples) |
| `DonchianChannel` | `volatility.py:L334` | Donchian channel (rolling high/low) |
| `EaseOfMovementIndicator` | `volume.py:L197` | Ease of movement (volume-adjusted price) |
| `PercentagePriceOscillator` | `momentum.py:L622` | PPO — price oscillator |
| `PercentageVolumeOscillator` | `momentum.py:L695` | PVO — volume oscillator |
| `KAMAIndicator` | `momentum.py:L282` | Kaufman adaptive moving average |
| `AwesomeOscillatorIndicator` | `momentum.py:L408` | Awesome oscillator |

## Common Patterns

- **One-call feature expansion**:
  ```python
  from ta import add_all_ta_features
  df = add_all_ta_features(df, open="Open", high="High", low="Low",
                           close="Close", volume="Volume")
  ```
  — appends the full indicator suite (volatility/trend/momentum/volume groups).
- **Individual indicator**: `ta.trend.MACD(close).macd()` / `.macd_signal()` /
  `.macd_diff()` — the standard class → series API.
- **Feature columns**: each indicator's output columns carry the
  `trend_macd`-style names for downstream model work (sklearn/pandas-native).
- **Signal layer**: indicator columns feed vectorbt `SignalFactory` or a custom
  strategy directly — no C library, no TA-Lib install step.
- **Alternative to ta-lib**: same indicator families, pandas-native; use ta when the
  system-C dependency of ta-lib is the blocker, ta-lib when its exact numeric
  compatibility matters.

## Pitfalls

- **Column name convention**: `add_all_ta_features` expects exact
  `open/high/low/close/volume` column names — rename before calling.
- **fillna behavior**: most indicators take `fillna=False` (default NaN propagation) —
  enable explicitly when downstream models reject NaNs.
- **Window defaults**: indicator defaults (14, 26, 9, 20…) are the standard ones —
  verify they match your convention before trusting signals.
- **Look-ahead**: any indicator on a full series is causal (only past bars), but
  rolling-window implementations must not be re-run on the validation split.
- **ta vs ta-lib numerics**: rounding conventions differ slightly between the two —
  don't mix sources in the same study without a documented tolerance.

## Provenance

Graph: `knowledge_graphs/ta/.graphify/graph.json` — 538 nodes · 1208 edges ·
42 communities · graphify @ a890410710a6, backend opencode, description coverage 88.6%,
1 curated M2b entry (macd, ADR-0008).

## Verification Checklist

- [ ] `add_all_ta_features(df)` appends the indicator columns
- [ ] `ta.trend.MACD(close).macd_diff()` returns a series
- [ ] QR rows cite `trend.py:L1`/`momentum.py:L1`/`volatility.py:L1`/`volume.py:L1`/`utils.py:L1`
      files resolvable in the ta graph
