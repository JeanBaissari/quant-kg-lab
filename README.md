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
  hallucinated cheatsheets. → `docs/SKILL_SPEC.md`, `scripts/validate_skills.py`
- **② A composable quant stack.** Cross-library **bridges** and **workflow playbooks** encode
  *how* the libraries compose into research loops (data → features → model → backtest → HPO →
  risk) — so it reads as one stack, not ten isolated references. → `skills/quant-patterns/`,
  `docs/UNIFIED_INDEX.md`

## Architecture

```
quant-kg-lab/
├── knowledge_graphs/<lib>/.graphify/   # graph.json + GRAPH_REPORT.md + labels (10 libraries)
├── skills/<lib>/<module>/SKILL.md      # atomic, per-module skills (+ routers)
│   └── quant-patterns/                 #   cross-library workflow playbooks
├── scripts/                            # rebuild, query, validate, audit, bridge tooling
├── docs/                               # specs (SKILL_SPEC, GRAPH_SPEC), methodology, index
├── graphs.lock                         # pinned upstream commits — reproducibility manifest
└── .github/workflows/                  # skill validation + graph freshness CI
```

## Pipeline

1. **Extract** — `graphify` ingests a library's source (pinned commit) → knowledge graph
   (nodes = modules/classes/functions, edges = calls/inherits/imports/uses).
2. **Query** — community detection surfaces module boundaries; degree centrality surfaces the
   real API hubs ("god nodes").
3. **Author** — one spec-driven `SKILL.md` per quant-relevant module (`docs/SKILL_SPEC.md`).
4. **Validate** — every skill's claims are checked against the live API + graph provenance in CI.

See `docs/methodology.md` for the full pipeline and `docs/GRAPH_SPEC.md` for the schema, the
noise-filter policy, and the graph quality gate.

## Libraries under analysis

| Library | Domain | Nodes · Edges |
|---------|--------|---------------|
| [pandas](https://github.com/pandas-dev/pandas) | Data frames, time series | 37,983 · 69,899 |
| [scipy](https://github.com/scipy/scipy) | Stats, optimize, signal | 31,042 · 51,352 |
| [numpy](https://github.com/numpy/numpy) | Arrays, linalg, random | 20,436 · 30,581 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Machine learning | 18,753 · 49,978 |
| [xgboost](https://github.com/dmlc/xgboost) | Gradient boosting | 7,708 · 14,747 |
| [vectorbt](https://github.com/polakowo/vectorbt) | Vectorized backtesting | 5,411 · 13,588 |
| [optuna](https://github.com/optuna/optuna) | Hyperparameter optimization | 3,912 · 8,405 |
| [backtrader](https://github.com/mementum/backtrader) | Event-driven backtesting | 3,458 · 6,863 |
| [lightgbm](https://github.com/microsoft/LightGBM) | Gradient boosting | 2,952 · 5,138 |
| [ta-lib](https://github.com/TA-Lib/ta-lib-python) | Technical indicators | 1,305 · 5,564 |

**Total: ~133K nodes / ~256K edges across 10 graphs.** Pinned commits in `graphs.lock`.

## Using a skill (copy-in)

These skills are intentionally **not** distributed as a package. To use one, copy the skill
directory into your agent's skills location:

```bash
cp -r skills/scipy/stats /path/to/your/.claude/skills/scipy-stats
# or into any agentskills.io / Hermes-compatible skills directory
```

Only the `name` and `description` frontmatter are required by loaders; the provenance metadata is
carried along and ignored safely by agents that don't use it.

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

10 library graphs are extracted; the project is **consolidating them to a single gold standard**
(uniform skill template, semantic descriptions + clean god nodes for all 10, full API validation,
and the workflow-playbook layer). See `ROADMAP.md` for the phased plan and current state.

## License

[MIT](LICENSE). Skills are open-source; graphs are reproducible from `graphs.lock`.
