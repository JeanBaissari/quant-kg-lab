# Phase 4 — Skill Extraction Templates

> **Status**: Awaiting description completion for pandas, vectorbt, scipy, backtrader, ta-lib, xgboost, lightgbm
> **Numpy**: ✅ 100% described — ready for skill extraction

---

## Wave 4A — Core Data Layer (ready when pandas + scipy described)

### numpy (3 skills) — READY NOW (100% described)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `numpy-core` | `numpy` | `ndarray`, `ufunc`, broadcasting, indexing, dtypes |
| `numpy-linalg` | `numpy.linalg` | `solve`, `eig`, `eigh`, `svd`, `norm`, `det`, `inv`, `cholesky`, `qr` |
| `numpy-random` | `numpy.random` | `Generator`, `default_rng`, `random`, `normal`, `uniform`, `choice`, `permutation` |

### scipy (3 skills)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `scipy-stats` | `scipy.stats` | 100+ distributions, `ttest_ind`, `ks_2samp`, `normaltest`, `gaussian_kde`, `zscore` |
| `scipy-optimize` | `scipy.optimize` | `minimize`, `curve_fit`, `root`, `linprog`, `milp`, `basinhopping`, `differential_evolution` |
| `scipy-signal` | `scipy.signal` | `butter`, `filtfilt`, `spectrogram`, `welch`, `stft`, `detrend`, `convolve`, `correlate` |

### pandas (2 skills)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `pandas-core` | `pandas` | `DataFrame`, `Series`, `Index`, `GroupBy`, `merge`, `concat`, `pivot`, `melt` |
| `pandas-ts` | `pandas.tseries` | `resample`, `rolling`, `expanding`, `ewm`, `shift`, `diff`, `pct_change`, `DateOffset` |

---

## Wave 4B — Quant Tools (ready when vectorbt + backtrader + ta-lib described)

### vectorbt (3 skills)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `vectorbt-core` | `vectorbt` | `Config`, `ArrayWrapper`, `Wrapping`, `Accessor`, `Settings` |
| `vectorbt-signals` | `vectorbt.signals` | `SignalFactory`, `MA`, `RSI`, `MACD`, `BBANDS`, `STOCH`, `entry/exit` |
| `vectorbt-portfolio` | `vectorbt.portfolio` | `Portfolio.from_signals`, `from_orders`, `stats`, `metrics`, `trades` |

### backtrader (2 skills)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `backtrader-core` | `backtrader` | `Cerebro`, `Strategy`, `DataFeed`, `Broker`, `Order`, `Trade` |
| `backtrader-analyzers` | `backtrader.analyzers` | `SharpeRatio`, `DrawDown`, `TradeAnalyzer`, `TimeReturn`, `AnnualReturn` |

### ta-lib (1 skill)
| Skill | Module | Key Indicators |
|-------|--------|---------------|
| `ta-lib-indicators` | `talib` | SMA, EMA, RSI, MACD, BBANDS, ATR, ADX, STOCH, SAR, OBV, 200+ total |

---

## Wave 4C — ML Boosters (ready when xgboost + lightgbm described)

### xgboost (2 skills)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `xgboost-core` | `xgboost` | `DMatrix`, `train()`, `Booster`, `cv()`, `XGBModel` |
| `xgboost-sklearn` | `xgboost.sklearn` | `XGBClassifier`, `XGBRegressor`, `XGBRanker`, `XGBRFClassifier` |

### lightgbm (2 skills)
| Skill | Module | Key Classes |
|-------|--------|-------------|
| `lightgbm-core` | `lightgbm` | `Dataset`, `train()`, `Booster`, `cv()`, `LGBMModel` |
| `lightgbm-sklearn` | `lightgbm.sklearn` | `LGBMClassifier`, `LGBMRegressor`, `LGBMRanker` |

---

## Skill Template (agentskills.io spec)

```yaml
---
name: <library>-<module>
description: Use when working with <Library> <ModuleName> — <one_line_summary>.
version: 0.1.0
author: quant-kg-lab
license: MIT
source_repo: <org>/<repo>
source_version: main
extraction_date: 2026-07-29
graph_hash: <nodes>_nodes_<edges>_edges
metadata:
  hermes:
    tags: [<library>, <tags>]
    related_skills: [<related>]
---

# <Library> <ModuleName>

Extracted from <library> knowledge graph.

## Quick Reference

| Class/Function | Purpose | Graph Node |
|---------------|---------|------------|
| ... | ... | `source_file:line` |

## Common Patterns

```python
# example
```

## Pitfalls

1. ...

## Cross-Library Bridges

| Bridge | Connection | Description |
|--------|-----------|-------------|
| ... | ... | ... |

## Verification Checklist

- [ ] Classes validated against live API
- [ ] Graph nodes referenced by ID
- [ ] Cross-library bridges documented
```
