---
name: arch-unitroot
description: "Use when testing for unit roots and stationarity with arch — ADF, Phillips-Perron, KPSS, and cointegration tests."
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: bashtage/arch
source_commit: 704bb70e48372e3ccccdde7da379811657ad0224
extraction_date: 2026-08-12
graph:
  nodes: 1367
  edges: 3900
  community_count: 135
  graph_hash: 5b23bf9efa5ee1d1
tags:
- arch
- unitroot
- stationarity
related_skills:
- arch
- arch-volatility
- scipy-stats
---

# arch.unitroot

Unit-root and stationarity testing: `ADF`, `PhillipsPerron`, `KPSS` — the
pre-estimation gate for volatility models and cointegration setups.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `ADF` | `unitroot/unitroot.py:L672` | Augmented Dickey-Fuller test — null: unit root |
| `PhillipsPerron` | `unitroot/unitroot.py:L1012` | Phillips-Perron test — robust to serial correlation |
| `KPSS` | `unitroot/unitroot.py:L1215` | Kwiatkowski-Phillips-Schmidt-Shin — null: stationary |

## Common Patterns

- **Stationarity gate**: `ADF(series).pvalue < 0.05` → reject unit root; cross-check with
  `KPSS(series).pvalue > 0.05` (null: stationary). Each test exposes `stat`, `pvalue`,
  `critical_values` and `.summary()`.
- **Pair strategy pre-check**: Engle-Granger cointegration (`arch.unitroot.cointegration`)
  before pairs trading.
- **On returns vs levels**: test LEVELS for vol-model inputs; returns are usually stationary.

## Pitfalls

- **Test power**: ADF/PP are weak on short samples; KPSS is the confirmatory test — use both.
- **Lag selection**: default lag selection matters — pass `lags` explicitly for reproducibility.
- **Trend specification**: `trend='ct'` vs `'c'` changes critical values — match the data's
  drift.

## Provenance

Graph: `knowledge_graphs/arch/.graphify/graph.json` — 1367 nodes · 3900 edges ·
135 communities · graphify @ 704bb70e4837, backend opencode, description coverage 94.3%.

## Verification Checklist

- [ ] `ADF(series)` and `KPSS(series)` return stat/pvalue/critical_values
