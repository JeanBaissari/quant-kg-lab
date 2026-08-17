---
name: quant-factor-tearsheets
description: "Use when turning a factor into evidence — clean factor panels, IC/quantile analysis with alphalens, performance reporting with pyfolio, and the numbers a factor review deck needs."
version: 0.2.0
author: quant-kg-lab
license: MIT
composes: [alphalens-factor-analysis, alphalens-tearsheets, pyfolio-timeseries, pyfolio-tearsheets, pandas-core, quant-factor-research]
tags: [quantitative-finance, factor-research, alphalens, pyfolio, tearsheets, ic, workflow]
related_skills: [alphalens-factor-analysis, alphalens-tearsheets, pyfolio-timeseries, pyfolio-tearsheets, pandas-core, quant-factor-research]
target_version: cross-lib
---

# Quant Factor Tearsheets (factor → clean panel → IC/quantile evidence → pyfolio report)

Factor tearsheets turn a raw factor column into the evidence block a strategy review needs:
is the signal predictive (IC), monotone across quantiles, persistent (turnover), and does a
long-short implementation of it hold up as a portfolio?

## Steps

1. **Clean the factor panel** — `alphalens-factor-analysis`: the pipeline entry point
   aligns factor values with forward returns.
   ```python
   from alphalens.utils import get_clean_factor_and_forward_returns
   fa = get_clean_factor_and_forward_returns(factor, prices, quantiles=5, periods=(1, 5, 10))
   ```
2. **Measure IC** — `alphalens-factor-analysis`: `factor_information_coefficient(fa)` for
   the series; `mean_information_coefficient` for the headline number.
3. **Check quantile monotonicity** — `mean_return_by_quantile(fa)` then
   `compute_mean_returns_spread(fa)` — the top-minus-bottom spread is the factor's core claim.
4. **Assess persistence** — `quantile_turnover(fa)` + `factor_rank_autocorrelation(fa)` —
   a factor that churns rank dies under transaction costs.
5. **Generate the tear sheets** — `alphalens-tearsheets`:
   ```python
   from alphalens.tears import create_returns_tear_sheet, create_information_tear_sheet
   create_returns_tear_sheet(fa)          # quantile cumulative returns, spread, turnover
   create_information_tear_sheet(fa)      # IC ts/hist/QQ/by-group
   ```
6. **Portfolio-level report** — `pyfolio-tearsheets` + `pyfolio-timeseries`: convert the
   factor long-short returns with `create_pyfolio_input`, then
   `create_full_tear_sheet(returns, positions)` for drawdown, rolling Sharpe, round trips.
7. **Verdict** — `pandas-core` + `quant-factor-research`: assemble IC, spread, turnover,
   alpha/beta into a one-page factor scorecard; only factors passing all four gates move to
   `quant-factor-research` selection.

## Pitfalls

1. **Look-ahead in forward returns**: `get_clean_factor_and_forward_returns` must receive
   point-in-time factor values; shifting prices instead of lagging the factor fabricates IC.
2. **Quantile count**: 5 quantiles is the default and often right; 10 (deciles) on small
   universes produces empty/noisy bins.
3. **Turnover is the silent killer**: high IC + high turnover ≈ zero net edge — report
   turnover next to IC, never alone.
4. **Benchmark mismatch**: `factor_alpha_beta` needs the same universe/frequency as the
   factor — mismatched benchmarks invalidate the alpha claim.
5. **pyfolio input alignment**: `create_pyfolio_input` requires clean long-short positions;
   feeding raw factor values produces nonsense drawdowns.

## Composed Skills & Bridges

| Stage | Skill | Bridge (relation) |
|-------|-------|-------------------|
| pipeline | `alphalens-factor-analysis` | factor → forward-return panel |
| evidence | `alphalens-factor-analysis` | IC / quantile / turnover |
| sheets | `alphalens-tearsheets` | quantile + IC tear sheets |
| portfolio | `pyfolio-tearsheets`, `pyfolio-timeseries` | long-short perf report |
| handoff | `alphalens-factor-analysis` → `pyfolio` | `create_pyfolio_input` (feeds) |
| selection | `quant-factor-research` | factor gates → robust subset |

## Related Skills

- [[alphalens-factor-analysis]]
- [[alphalens-tearsheets]]
- [[pyfolio-timeseries]]
- [[pyfolio-tearsheets]]
- [[pandas-core]]
- [[quant-factor-research]]
