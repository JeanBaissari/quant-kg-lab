# quant-kg-lab

**A quantitative knowledge-graph laboratory** — it extracts structured knowledge graphs from
premier scientific-Python libraries and distills them into **verifiable, copy-in agent skills**
for quantitative research and development.

Not a package to install. A knowledge base to **copy from** — every skill traces back to a
graph node and a source line, and is checked against the live library API in CI.

## Thesis

Quantitative work spans data (pandas, numpy), statistics & signal processing (scipy),
statistical learning (scikit-learn, xgboost, lightgbm), hyperparameter optimization (optuna),
technical analysis (ta-lib), and backtesting (vectorbt, backtrader). This repo builds a
**persistent, queryable knowledge graph** of each of those libraries and turns them into
**spec-driven agent skills** an agent can load to work fluently across the whole stack.

Two things make it more than a pile of library docs:

- **① Verifiable skills.** Every claim in a skill traces to a graph node (`source_file:line`)
  and is validated against the installed library's real API in CI. Skills you can trust, not
  hallucinated cheatsheets. → `docs/specs/SKILL_SPEC.md`, `scripts/validate_skills.py`
- **② A composable quant stack.** Cross-library **bridges** and **workflow playbooks** encode
  *how* the libraries compose into research loops (data → features → model → backtest → HPO →
  risk) — so it reads as one stack, not ten isolated references. → `skills/quant-patterns/`,
  `docs/reference/unified-index.md`

## Architecture

```
quant-kg-lab/
├── knowledge_graphs/<lib>/.graphify/   # graph.json + GRAPH_REPORT.md + labels (13 libraries)
├── skills/<lib>/<module>/SKILL.md      # atomic, per-module skills (+ routers)
│   └── quant-patterns/                 #   cross-library workflow playbooks
├── scripts/                            # rebuild, query, validate, audit, bundle tooling
├── docs/                               # index.md hub → specs/ guides/ libraries/ reference/ adr/ audit/
├── graphs.lock                         # pinned upstream commits — reproducibility manifest
└── .github/workflows/                  # skill validation + graph provenance gate + docs audit
```

## Pipeline

1. **Extract** — `graphify` ingests a library's source (pinned commit) → knowledge graph
   (nodes = modules/classes/functions, edges = calls/inherits/imports/uses).
2. **Query** — community detection surfaces module boundaries; degree centrality surfaces the
   real API hubs ("god nodes").
3. **Author** — one spec-driven `SKILL.md` per quant-relevant module (`docs/specs/SKILL_SPEC.md`).
4. **Validate** — every skill's claims are checked against the live API + graph provenance in CI.

See `docs/guides/methodology.md` for the full pipeline and `docs/specs/GRAPH_SPEC.md` for the schema, the
noise-filter policy, and the graph quality gate.

## Libraries under analysis

| Library | Domain | Nodes · Edges |
|---------|--------|---------------|
| [pandas](https://github.com/pandas-dev/pandas) | Data frames, time series | 11,368 · 39,913 |
| [scipy](https://github.com/scipy/scipy) | Stats, optimize, signal | 14,071 · 23,466 |
| [numpy](https://github.com/numpy/numpy) | Arrays, linalg, random | 8,306 · 13,483 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Machine learning | 8,450 · 28,094 |
| [xgboost](https://github.com/dmlc/xgboost) | Gradient boosting | 1,631 · 4,318 |
| [vectorbt](https://github.com/polakowo/vectorbt) | Vectorized backtesting | 3,682 · 9,212 |
| [optuna](https://github.com/optuna/optuna) | Hyperparameter optimization | 2,205 · 4,010 |
| [backtrader](https://github.com/mementum/backtrader) | Event-driven backtesting | 2,680 · 4,964 |
| [lightgbm](https://github.com/microsoft/LightGBM) | Gradient boosting | 593 · 2,029 |
| [ta-lib](https://github.com/TA-Lib/ta-lib-python) | Technical indicators | 381 · 379 |
| [statsmodels](https://github.com/statsmodels/statsmodels) | Statistical models (regression, GLM, time series) | 11,616 · 33,529 |
| [cvxpy](https://github.com/cvxpy/cvxpy) | Convex optimization | 6,380 · 16,515 |
| [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) | Portfolio optimization | 342 · 512 |
| [arch](https://github.com/bashtage/arch) | Volatility modelling (ARCH/GARCH) | 1,367 · 3,900 |
| [alphalens](https://github.com/quantopian/alphalens) | Factor analysis | 172 · 231 |
| [pyfolio](https://github.com/quantopian/pyfolio) | Portfolio tear sheets | 305 · 361 |
| [Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) | Portfolio optimization suite | 426 · 599 |
| [shap](https://github.com/shap/shap) | Model explainability | 1,277 · 1,752 |
| [polars](https://github.com/pola-rs/polars) | Fast DataFrame library | 5,296 · 16,925 |

**Total: ~76K nodes / ~200K edges across 19 graphs.** Pinned commits in `graphs.lock`; every
graph passes the [quality gate](docs/specs/GRAPH_SPEC.md#5-quality-gate) (labels, descriptions,
god nodes, pin, audit, API-surface coverage).

## Using a skill (copy-in)

These skills are intentionally **not** distributed as a package. To use one, copy the skill
directory into your agent's skills location:

```bash
cp -r skills/scipy/stats /path/to/your/.claude/skills/scipy-stats
# or into any agentskills.io / Hermes-compatible skills directory
```

Only the `name` and `description` frontmatter are required by loaders; the provenance metadata is
carried along and ignored safely by agents that don't use it.

## Consume without rebuilding

Every tag ships versioned bundles as **GitHub Release assets** (ADR-0007): one zip per library
plus the cross-library overlay, with a `bundle.json` manifest (per-file sha256, pinned commit,
node/edge counts). Bundles carry the **graphs** — the knowledge base skills cite; skills
themselves stay copy-in from this repo. No graphify, no network, no rebuild:

```bash
# 1. Download the bundle for a library from the release (tag = graphs.lock commit)
unzip qkg-scipy.zip && unzip qkg-cross-library-overlay.zip
#    → scipy/graph.json + scipy/GRAPH_REPORT.md + scipy/.graphify_labels.json
# 2. Copy the skills you need (copy-in, per SKILL_SPEC) — from this repo
cp -r skills/scipy/stats ~/.claude/skills/scipy-stats
# 3. Verify skills against your installed library (with the repo checkout)
python3 scripts/validate_skills.py --ci scipy
```

Bundles are byte-identical across builds (`bundle.json` verifies every sha256), and are
asserted free of absolute paths and gitignored intermediates — the same
`scripts/check_artifact_safety.py` check runs in CI. Build one locally with
`python3 scripts/export_bundle.py --lib all --out dist`.

## Reproducibility

Every graph is rebuildable from its pinned commit:

```bash
npm install -g @sentropic/graphify      # the external extraction engine
pip install -r requirements.txt         # the target libraries (for validation)
scripts/rebuild_graph.sh scipy          # clone@pin → extract → merge → cluster → audit
python scripts/query_graph.py scipy "kolmogorov smirnov"   # query any graph
python scripts/validate_skills.py --ci  # verify skill claims against live APIs
```

## Status

**Gold standard reached for all 13 libraries**: every graph passes the quality gate (real
community labels, ≥80% semantic descriptions, clean god nodes, `built_from_commit` pinned,
audited edges, ≥95% API-surface coverage); 65 spec-normalized skills with live-API validation,
graph-node citations and a green citation gate; 41/42 precise cross-library bridges as a
curated overlay; workflow playbooks across the whole stack; provenance-gated CI. See
`ROADMAP.md` for the phased plan, remaining polish, and the expansion queue (arch,
riskfolio-lib, pyfolio, alphalens, polars, shap…).

## License

[MIT](LICENSE). Skills are open-source; graphs are reproducible from `graphs.lock`.
