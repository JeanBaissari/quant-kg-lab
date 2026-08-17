---
name: quant-factor-research
description: "Use when researching alpha factors — building candidate features, measuring their predictive power and importance, selecting a robust subset, and validating out-of-sample before any backtest."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [quant-full-pipeline, quant-factor-importance, quant-walk-forward-validation, quant-factor-tearsheets, alphalens-factor-analysis]
tags: [quantitative-finance, factor-research, feature-selection, alpha, workflow]
related_skills: [quant-full-pipeline, quant-factor-importance, quant-walk-forward-validation, quant-factor-tearsheets, alphalens-factor-analysis]
target_version: cross-lib
---

# Quant Factor Research (data → features → importance → selection → validation)

Factor research answers "which signals actually predict forward returns, robustly?" — *before*
committing them to a strategy. This playbook chains feature construction, information-coefficient
analysis, model-based importance, and leak-free selection.

## Steps

1. **Build a candidate factor panel** — `pandas-ts` + `ta-lib-indicators`: momentum, mean-reversion,
   volatility, volume factors, all point-in-time and cross-sectionally comparable (rank/z-score).
2. **Univariate power (IC)** — `scipy-stats`: for each factor, the information coefficient is the
   rank correlation between the factor at *t* and forward return at *t+h*.
   ```python
   from scipy.stats import spearmanr
   ic = {f: spearmanr(panel[f], fwd_ret, nan_policy="omit").statistic for f in factors}
   ```
3. **Multivariate importance** — `scikit-learn-ensemble` (or `xgboost`): fit a tree model on all
   factors and read `feature_importances_`; cross-check with permutation importance to avoid the
   cardinality bias of impurity importance. See `quant-factor-importance`.
4. **Select a robust subset** — `scikit-learn-feature-selection`: `SelectFromModel`, `RFECV`, or a
   stability-selection loop across walk-forward folds; keep factors selected in ≥N folds.
5. **Validate OOS** — `quant-walk-forward-validation`: recompute IC and importance on each OOS fold;
   a real factor is stable across folds and regimes, not a single-period artifact.
6. **Decorrelate** — drop factors that are near-duplicates (high pairwise rank correlation); prefer
   the one with higher, more stable OOS IC.

## Pitfalls

1. **Single-period IC** is noise. Require sign-stable IC across walk-forward folds before trusting a factor.
2. **Impurity importance is biased** toward high-cardinality/continuous features — always corroborate with permutation importance (`quant-factor-importance`).
3. **Selection leakage**: run selection *inside* each training fold, not once on the full sample.
4. **Multiple-testing**: scanning hundreds of factors guarantees false positives — adjust p-values (`scipy.stats` combine/FDR) or use a holdout.
5. **Cross-sectional vs time-series** factors need different normalization; don't mix them blindly.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| features | `pandas-ts`, `ta-lib-indicators` | ta-lib → factor panel |
| univariate IC | `scipy-stats` | scipy.stats → feature selection (powers) |
| importance | `scikit-learn-ensemble`, `quant-factor-importance` | sklearn importances / SHAP |
| selection | `scikit-learn-feature-selection` | scipy.stats.f_classif → SelectKBest |
| validation | `quant-walk-forward-validation` | leak-free OOS folds |

## Related Skills

- [[quant-full-pipeline]]
- [[quant-factor-importance]]
- [[quant-walk-forward-validation]]
- [[quant-factor-tearsheets]]
- [[alphalens-factor-analysis]]
