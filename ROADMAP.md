# quant-kg-lab — Forward Roadmap

> **Current**: 10 libraries extracted (133K nodes, 256K edges), 28 skills, 27 commits
> **GitHub**: https://github.com/JeanBaissari/quant-kg-lab

---

## State Assessment

| Layer | Complete | In Progress | Gap |
|-------|----------|-------------|-----|
| Knowledge Graphs | 10/10 libraries ✅ | — | — |
| Node Descriptions | 2/10 (sklearn 88.9%, optuna 36.7%) | — | 8 libraries at 0% |
| Community Labels | 2/10 (sklearn, optuna) | — | 8 unlabeled |
| Skills | 28 (15 sklearn + 8 optuna + 5 quant) | — | 0 skills for 8 new libraries |
| Edge Audits | 2/10 (sklearn, optuna) | — | 8 unaudited |
| Cross-Library Bridges | sklearn↔optuna (6/7) | — | No bridges for 8 new libraries |
| Skill Validation | sklearn + optuna (92.2%) | — | 8 libraries not validated |
| CI Pipelines | Freshness + Validation | — | — |
| Studio HTML | sklearn (17MB) | — | 9 libraries not generated |

**Critical bottleneck**: Only sklearn and optuna have descriptions. Without descriptions, query_graph.py returns bare labels, skills can't auto-generate API references, and the studio shows "0% described". Descriptions unlock everything downstream.

---

## Phase 3 — Description Generation (est. 3-4 sub-agent waves)

**Goal**: Generate node descriptions for the 8 undescribed libraries. This is the single highest-leverage action.

### Wave 3A — Tier 1 (largest impact)
| Library | Nodes | Est. Batches | Priority | Why |
|---------|-------|-------------|----------|-----|
| pandas | 37,983 | ~800 | P0 | Core quant data layer. Descriptions unlock DataFrame/Series/GroupBy queryability |
| numpy | 20,436 | ~450 | P0 | Numerical backbone. ndarray/linalg/random descriptions enable all downstream |
| scipy | 31,042 | ~650 | P1 | stats/optimize/signal — quant workhorses |

### Wave 3B — Tier 2 (quant tools)
| Library | Nodes | Est. Batches | Priority | Why |
|---------|-------|-------------|----------|-----|
| vectorbt | 5,411 | ~120 | P0 | Core backtesting library. Config/ArrayWrapper/Portfolio descriptions critical |
| backtrader | 3,458 | ~75 | P1 | Event-driven backtesting. Strategy/Cerebro descriptions |
| ta-lib | 1,305 | ~30 | P1 | Technical indicators. Smallest graph, quick win |

### Wave 3C — Tier 3 (ML boosters)
| Library | Nodes | Est. Batches | Priority | Why |
|---------|-------|-------------|----------|-----|
| xgboost | 7,708 | ~170 | P1 | Gradient boosting. sklearn-compatible API |
| lightgbm | 2,952 | ~65 | P1 | Microsoft GBDT. Smallest Tier 3, quick win |

**Method**: Same pipeline as sklearn — `graphify extract --backend claude-cli` → batch processing → merge descriptions → `graphify cluster-only` to regenerate studio.

**Verification**: Description coverage >30% per library (AST-only without LLM keys won't reach 88% like sklearn, but 30-40% is solid for code-symbol nodes).

---

## Phase 4 — Skill Extraction (est. 3 sub-agent waves)

**Goal**: Extract spec-driven skills for all libraries. Target: 47 → 65+ total skills.

### Wave 4A — Core Data Layer (numpy, scipy, pandas)
| Skill | Library | Key Classes |
|-------|---------|-------------|
| `numpy-linalg` | numpy | `linalg.solve`, `linalg.eig`, `linalg.svd`, `linalg.norm` |
| `numpy-random` | numpy | `Generator`, `RandomState`, distributions, permutation |
| `numpy-core` | numpy | `ndarray`, `ufunc`, broadcasting, indexing |
| `scipy-stats` | scipy | Distributions, statistical tests, kernel density |
| `scipy-optimize` | scipy | `minimize`, `curve_fit`, root finding, linear programming |
| `scipy-signal` | scipy | Filtering, spectral analysis, detrending, convolution |
| `pandas-ts` | pandas | `resample`, `rolling`, `shift`, `ewm`, `DateOffset` |
| `pandas-core` | pandas | `DataFrame`, `Series`, `GroupBy`, `merge`, `pivot` |

### Wave 4B — Quant Tools (vectorbt, backtrader, ta-lib)
| Skill | Library | Key Classes |
|-------|---------|-------------|
| `vectorbt-signals` | vectorbt | `SignalFactory`, entry/exit generation, indicator pipelines |
| `vectorbt-portfolio` | vectorbt | `Portfolio.from_signals`, `from_orders`, metrics, stats |
| `vectorbt-core` | vectorbt | `Config`, `ArrayWrapper`, `Wrapping`, accessors |
| `backtrader-core` | backtrader | `Cerebro`, `Strategy`, `DataFeed`, `Broker` |
| `backtrader-analyzers` | backtrader | `SharpeRatio`, `DrawDown`, `TradeAnalyzer`, `TimeReturn` |
| `ta-lib-indicators` | ta-lib | SMA, RSI, MACD, Bollinger, ATR, 200+ indicators |

### Wave 4C — ML Boosters (xgboost, lightgbm)
| Skill | Library | Key Classes |
|-------|---------|-------------|
| `xgboost-core` | xgboost | `DMatrix`, `train()`, `Booster`, `cv()` |
| `xgboost-sklearn` | xgboost | `XGBClassifier`, `XGBRegressor`, `XGBRanker` |
| `lightgbm-core` | lightgbm | `Dataset`, `train()`, `Booster`, `cv()` |
| `lightgbm-sklearn` | lightgbm | `LGBMClassifier`, `LGBMRegressor`, `LGBMRanker` |

---

## Phase 5 — Integration & Cross-Library (est. 2 waves)

### 5.1 Cross-Library Bridge Expansion
Extend `scripts/inject_cross_edges.py` with bridges for all 10 libraries:
```
numpy.ndarray → pandas.DataFrame (backing store)
numpy.linalg → scipy.linalg (superset relationship)
pandas.DataFrame → sklearn.BaseEstimator (fit input)
pandas.DataFrame → vectorbt.Portfolio (backtest input)
ta-lib.RSI → vectorbt.SignalFactory (indicator → signal)
xgboost.XGBClassifier → sklearn.Pipeline (sklearn-compatible)
optuna.Study → xgboost.train (HPO integration)
scipy.optimize → optuna.samplers (alternative backend)
backtrader.Strategy → sklearn.ensemble (ML strategy)
pandas.rolling → numpy.lib.stride_tricks (implementation detail)
```

### 5.2 Unified Index Regeneration
Regenerate `docs/UNIFIED_INDEX.md` with actual graph node IDs, description snippets, and cross-library paths from all 10 graphs. Currently it's a template — needs real data.

### 5.3 Quant Workflow Patterns v2
Expand `skills/quant-patterns/` with multi-library workflows:
- `quant-full-pipeline` — pandas → ta-lib → sklearn → vectorbt → optuna → analysis
- `quant-factor-research` — data → features → importance → selection → backtest
- `quant-ml-strategy` — sklearn/xgboost/lightgbm model → vectorbt/backtrader execution

---

## Phase 6 — Production Polish (est. 1-2 waves)

### 6.1 Skill Validation Expansion
- Install all 10 libraries in CI venv
- Run `validate_skills.py` across all libraries
- Fix any validation failures
- Add validation to pre-commit hooks

### 6.2 Edge Audits for New Libraries
- Run `audit_edges.py` on all 8 unaudited libraries
- Flag suspicious cross-module edges
- Generate `docs/edge-audit-<lib>.md` reports

### 6.3 Community Labels for New Libraries
- Label communities for the 8 unlabeled libraries
- Regenerate GRAPH_REPORTs with semantic labels

### 6.4 Studio HTML Generation
- Regenerate studio for all 10 libraries after descriptions applied
- Commit studio HTML (or link to it)

### 6.5 Obsidian Vault Export
- `graphify export obsidian` for all 10 libraries
- Creates navigable offline knowledge base

---

## Priority Matrix

| Priority | Phase | Item | Impact | Effort | Unlocks |
|----------|-------|------|--------|--------|---------|
| **P0** | 3A | pandas + numpy descriptions | Critical | 2 sub-agents | All downstream queries, skills, studio |
| **P0** | 3B | vectorbt descriptions | Critical | 1 sub-agent | Backtesting skill extraction |
| **P1** | 3A | scipy descriptions | High | 1 sub-agent | Stats/optimize skill extraction |
| **P1** | 3B-3C | backtrader + ta-lib + xgboost + lightgbm descriptions | Medium | 2 sub-agents | Remaining skill extraction |
| **P1** | 4A | numpy + pandas + scipy skills (8) | High | 2 sub-agents | Core data layer skills |
| **P1** | 4B | vectorbt + backtrader + ta-lib skills (6) | High | 1 sub-agent | Quant tool skills |
| **P2** | 4C | xgboost + lightgbm skills (4) | Medium | 1 sub-agent | ML booster skills |
| **P2** | 5.1 | Cross-library bridges expansion | Medium | 1 script | Multi-library queries |
| **P2** | 5.2 | Unified Index regeneration | Medium | 1 agent | Authoritative reference |
| **P3** | 6.x | Validation, audits, labels, studio | Polish | 2 waves | Production readiness |

---

## Execution Strategy

1. **Phase 3 first** — descriptions are the bottleneck. Everything downstream depends on them.
2. **Phase 3A + 3B in parallel** — pandas, numpy, vectorbt simultaneously (3 sub-agents, P0 items)
3. **Phase 4A starts as soon as Phase 3A completes** — skills can be extracted from described graphs
4. **Phase 5 is script-driven** — cross-library bridges and unified index don't need sub-agents
5. **Phase 6 is cleanup** — validation, audits, labels — batchable into CI

**Total estimated**: 8-12 sub-agent waves, 15-25 new skills, 10 regenerated studios, full cross-library bridge matrix.
