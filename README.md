# quant-kg-lab

**Open-source PhD-level quantitative research laboratory** — extracting, structuring, and operationalizing knowledge from premier scientific Python libraries into reusable agent skills.

## Thesis

Modern quantitative finance demands fluency across statistical learning (scikit-learn), hyperparameter optimization (optuna), and agent-driven automation. This project builds **persistent, queryable knowledge graphs** of these foundational libraries and distills them into **spec-driven agent skills** that can be loaded into any agentskills.io-compatible agent (Hermes, Claude Code, OpenClaw, Codex).

## Architecture

```
quant-kg-lab/
├── knowledge_graphs/       # graphify-extracted knowledge graphs
│   ├── scikit-learn/       #   ML library graph (.graphify/)
│   └── optuna/             #   HPO framework graph (.graphify/)
├── skills/                 # extracted spec-driven SKILL.md files
│   ├── scikit-learn/       #   per-module skills
│   └── optuna/             #   per-module skills
├── scripts/                # extraction & automation tooling
├── docs/                   # methodology, papers, references
└── .github/                # CI/CD for graph freshness
```

## Pipeline

1. **Extract** → `graphify` ingests library source + docs → structured knowledge graph (nodes: classes/functions/modules, edges: calls/inherits/imports)
2. **Query** → community detection surfaces natural module boundaries; god nodes identify API hubs
3. **Author** → spec-driven `SKILL.md` files for quant-relevant modules
4. **Validate** → cross-reference against live library APIs; freshness gates via CI

## Libraries Under Analysis

| Library | Stars | Focus | Quant Relevance |
|---------|-------|-------|-----------------|
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66.8K | Machine learning | Feature engineering, model selection, metrics, pipelines |
| [optuna](https://github.com/optuna/optuna) | 14.6K | Hyperparameter optimization | Bayesian optimization, pruning, distributed sweeps |

## Skills Produced

Each skill follows the `agentskills.io` specification with:
- Progressive disclosure (SKILL.md → references/ → scripts/)
- Source-to-skill traceability (every claim links back to a graph node)
- Freshness metadata (library version, extraction date, graph hash)

## Status

🚧 **Phase 1 — Extraction Complete** — Knowledge graphs built for both libraries.

### Extraction Results

| Library | Nodes | Edges | Communities | Top God Node |
|---------|-------|-------|-------------|--------------|
| scikit-learn | 18,753 | 49,978 | 1,043 | BaseEstimator (2,309°) |
| optuna | 3,912 | 8,405 | 228 | Study (228°) |

### Key Findings

- **scikit-learn**: `BaseEstimator` is the undisputed hub (2,309 connections). `Pipeline` (536°), `TransformerMixin` (1,171°), and the `*Mixin` hierarchy form the core architecture. Parameter validation classes (`Interval`, `StrOptions`) have surprisingly high centrality.
- **optuna**: `Study` (228°) and `BaseDistribution` (213°) form a tightly-coupled core. The sampler/distribution hierarchy is the dominant structural pattern. 228 natural communities detected.

### Next: Skill Extraction

From these graphs, we'll extract spec-driven agent skills for quant-relevant modules:
- `sklearn.model_selection` → GridSearchCV, cross_val_score
- `sklearn.ensemble` → RandomForest, GradientBoosting
- `sklearn.metrics` → classification/regression metrics
- `optuna.samplers` → TPESampler, BoTorchSampler
- `optuna.pruners` → MedianPruner, HyperbandPruner

## License

MIT — skills are open-source, graphs are reproducible.
