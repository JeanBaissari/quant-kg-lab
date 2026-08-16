---
name: arch-unitroot
description: "Use when testing for unit roots and stationarity with arch \u2014 ADF,\
  \ Phillips-Perron, KPSS, and cointegration tests."
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
  graph_hash: e1c10f7f48d897c2
tags:
- arch
- unitroot
- stationarity
related_skills:
- arch
- arch-volatility
- scipy-stats
target_version: '8.0.0 (dev: after 8.0.0)'
upstream_status: current
---

## Version Note

> ⚠️ **Pin is an unreleased dev commit.** This skill describes `arch` ahead of the latest PyPI release (8.0.0 (dev: after 8.0.0)). Some APIs may not exist in your installed version.

# arch.unitroot

Unit-root and stationarity testing: `ADF`, `PhillipsPerron`, `KPSS` — the
pre-estimation gate for volatility models and cointegration setups.

## Quick Reference

| API | Source File | Description |
|-----|------------|-------------|
| `ADF` | `unitroot/unitroot.py:L672` | Augmented Dickey-Fuller test — null: unit root |
| `PhillipsPerron` | `unitroot/unitroot.py:L1012` | Phillips-Perron test — robust to serial correlation |
| `KPSS` | `unitroot/unitroot.py:L1215` | Kwiatkowski-Phillips-Schmidt-Shin — null: stationary |
| `phillips_ouliaris()` | `unitroot/_phillips_ouliaris.py:L134` | Phillips-Ouliaris cointegration test — residual-based, two series |
| `engle_granger()` | `unitroot/_engle_granger.py:L25` | Engle-Granger two-step cointegration test |
| `EngleGrangerTestResults` | `unitroot/_engle_granger.py:L108` | EG results — rho, lags, summary, critical values |
| `ADF.pvalues` / `.stat` | `unitroot/unitroot.py:L672` | Test statistic + MacKinnon p-values |
| `.lags` / `.max_lags` | `unitroot/_engle_granger.py:L163` | Optimal lag selection used in the test |

## Common Patterns

- **Stationarity gate**: `ADF(series).pvalue < 0.05` → reject unit root; cross-check with
  `KPSS(series).pvalue > 0.05` (null: stationary). Each test exposes `stat`, `pvalue`,
  `critical_values` and `.summary()`.
- **Pair strategy pre-check**: `engle_granger(y, x)` / `phillips_ouliaris(...)` before
  pairs trading — stationary residuals imply a cointegrating vector.
- **On returns vs levels**: test LEVELS for vol-model inputs; returns are usually stationary.
- **Cointegration workflow**: run EG on the pair, check the residual ADF via the EG result
  (`rho`, `pvalue`), and only trade pairs whose residuals are stationary.

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
