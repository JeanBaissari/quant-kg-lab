# quant-kg-lab — Phase 2 Expansion Plan

> **Phase 1**: ✅ Complete — scikit-learn + optuna knowledge graphs, 21 skills, validation pipeline
> **Phase 2**: 🔄 In Progress — 9 additional libraries across 3 tiers

---

## Library Extraction Status

| Tier | Library | Size | Status | Agent | Nodes | Edges | Communities |
|------|---------|------|--------|-------|-------|-------|-------------|
| — | optuna (v2) | 32M | 🔄 Extracting | deleg_8c9ae6d3/task-0 | — | — | — |
| 1 | numpy | 52M | 🔄 Extracting | deleg_8c9ae6d3/task-1 | — | — | — |
| 1 | scipy | 114M | 🔄 Extracting | deleg_8c9ae6d3/task-1 | — | — | — |
| 1 | pandas | 78M | 🔄 Extracting | deleg_8c9ae6d3/task-2 | — | — | — |
| 2 | ta-lib | 6.5M | 🔄 Extracting | deleg_8c9ae6d3/task-2 | — | — | — |
| 2 | backtrader | 11M | 🔄 Extracting | deleg_8c9ae6d3/task-2 | — | — | — |
| 2 | vectorbt | 187M | 🔄 Extracting | deleg_29e644c0/task-0 | — | — | — |
| 3 | xgboost | 22M | 🔄 Extracting | deleg_29e644c0/task-0 | — | — | — |
| 3 | lightgbm | 26M | 🔄 Extracting | deleg_29e644c0/task-0 | — | — | — |

---

## Cross-Library Bridge Map (Phase 2)

### Tier 1 → Existing (foundation layer)
```
numpy ────────► scikit-learn (array API, all estimators consume ndarray)
numpy ────────► scipy (scipy is built on numpy)
numpy ────────► pandas (DataFrame backed by numpy arrays)
scipy.stats ──► scikit-learn (statistical tests for feature selection)
scipy.optimize► optuna (alternative optimization backend)
pandas ───────► scikit-learn (DataFrame → numpy → fit())
pandas ───────► vectorbt (time-series data input)
```

### Tier 2 → Existing (quant tools)
```
vectorbt ─────► scikit-learn (ML-based strategy signals)
vectorbt ─────► optuna (strategy parameter optimization)
vectorbt ─────► pandas (data input/output)
ta-lib ───────► scikit-learn (technical indicator features)
ta-lib ───────► vectorbt (indicator inputs for strategies)
backtrader ───► scikit-learn (ML strategy integration)
backtrader ───► optuna (strategy optimization)
backtrader ───► ta-lib (indicator integration via bt-ta-lib)
```

### Tier 3 → Existing (ML boosters)
```
xgboost ──────► scikit-learn (sklearn-compatible API, XGBClassifier)
xgboost ──────► optuna (XGBoostPruningCallback, Optuna integration)
xgboost ──────► vectorbt (ML strategy signals)
lightgbm ─────► scikit-learn (sklearn-compatible API, LGBMClassifier)
lightgbm ─────► optuna (LightGBMPruningCallback, Optuna integration)
lightgbm ─────► pandas (categorical feature support)
```

---

## Skill Extraction Plan (Phase 2)

### Wave A — Core Data Layer (after Tier 1 extraction)
- `numpy-linalg` — Linear algebra, eigenvalue decomposition
- `numpy-random` — Random number generation, distributions
- `numpy-fft` — Fourier transforms
- `pandas-ts` — Time-series: resample, rolling, shift, ewma
- `pandas-io` — Data I/O: read_csv, read_parquet, to_sql
- `scipy-stats` — Statistical tests, distributions, kernel density
- `scipy-optimize` — minimize, curve_fit, root finding
- `scipy-signal` — Signal processing, filtering, detrending

### Wave B — Quant Tools (after Tier 2 extraction)
- `vectorbt-signals` — Entry/exit signal generation
- `vectorbt-portfolio` — Portfolio simulation, from_signals, from_orders
- `vectorbt-indicators` — 100+ built-in technical indicators
- `ta-lib-indicators` — 200+ technical indicators (SMA, RSI, MACD, etc.)
- `backtrader-core` — Cerebro engine, data feeds, broker simulation
- `backtrader-strategies` — Strategy base class, indicators, analyzers

### Wave C — ML Boosters (after Tier 3 extraction)
- `xgboost-core` — DMatrix, train(), Booster API
- `xgboost-sklearn` — XGBClassifier, XGBRegressor, XGBRanker
- `lightgbm-core` — Dataset, train(), Booster API
- `lightgbm-sklearn` — LGBMClassifier, LGBMRegressor, LGBMRanker

---

## Validation Expansion

Add these libraries to `scripts/validate_skills.py` LIBRARY_IMPORTS:
```python
"numpy": ["numpy"],
"scipy": ["scipy"],
"pandas": ["pandas"],
"xgboost": ["xgboost"],
"lightgbm": ["lightgbm"],
"vectorbt": ["vectorbt"],
"ta-lib": ["talib"],
"backtrader": ["backtrader"],
```

---

## Unified Index Structure (target)

```
skills/
├── scikit-learn/     (15 skills) ✅
├── optuna/           (1 → 8 skills) 🔄
├── numpy/            (3 skills) ⬜
├── scipy/            (3 skills) ⬜
├── pandas/           (2 skills) ⬜
├── vectorbt/         (3 skills) ⬜
├── ta-lib/           (1 skill) ⬜
├── backtrader/       (2 skills) ⬜
├── xgboost/          (2 skills) ⬜
├── lightgbm/         (2 skills) ⬜
└── quant-patterns/   (5 skills) ✅
                    ───
                    47 skills total (target)
```
