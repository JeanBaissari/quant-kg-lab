# quant-kg-lab — PhD-Level Roadmap

> **North Star**: A self-updating, queryable, spec-driven knowledge ecosystem where every quant-relevant library module has a corresponding agent skill with full graph-to-skill traceability.

## Execution Waves

```
Wave 1: Graph Completeness    Wave 2: Skill Extraction    Wave 3: Infrastructure   Wave 4: Production
[1][2][3] ──────────────────> [4][5][6] ───────────────> [7] ─────────────────> [8][9]
descriptions                  skill extraction             CI freshness            cross-library edges
community labels              query pipeline               automated updates       quant usage patterns
edge validation               graph traceability
  │                             │                            │                       │
  └─ unlocks labeled,           └─ unlocks 20+               └─ unlocks              └─ unlocks integrated
     described communities         queryable skills             living graphs            quant ecosystem
```

---

## Wave 1 — Graph Completeness (foundation)

### 1.1 Node Descriptions ⬜
**Status**: 0/18,753 nodes described. 469 batch instruction files exist in `description-instructions/`.
**What**: Every graph node gets a human-readable description. Currently all nodes show raw code identifiers.
**How**: Process description-instructions batches via agent → merge descriptions back into graph.json → regenerate studio.
**Verification**: `graphify describe` reports >90% node coverage.
**Depends on**: Nothing.
**Unlocks**: Meaningful studio visualization, searchable skill extraction, community context.

### 1.2 Community Labels ⬜
**Status**: 1,149 communities all labeled "Community N". 1 instruction file at `label-instructions/communities.md`.
**What**: Every community gets a semantic label (e.g., "GradientBoosting Ensemble Methods", "DBSCAN Density Clustering").
**How**: Agent reads community members from GRAPH_REPORT.md → generates 2-5 word labels → writes `.graphify_labels.json` → regenerates report.
**Verification**: GRAPH_REPORT.md shows labeled communities. `_COMMUNITY_*` notes in Obsidian vault.
**Depends on**: Nothing (can run parallel with 1.1).
**Unlocks**: Navigable module map, targeted skill extraction, community cohesion ranking.

### 1.3 Edge Validation ⬜
**Status**: 53% of 49,978 edges are INFERRED (confidence 0.5). 47% EXTRACTED.
**What**: Review + reclassify high-impact INFERRED edges. Flag suspicious edges.
**How**: Agent samples high-degree INFERRED edges → checks source files → reclassifies or flags.
**Verification**: EXTRACTED ratio >70%. Suspicious edge report in `docs/edge-audit.md`.
**Depends on**: 1.1 (descriptions help validate edges).
**Unlocks**: Higher-confidence queries, trustable skill generation.

---

## Wave 2 — Skill Extraction

### 2.1 Per-Community Skills ⬜
**Status**: 2 skills (`model_selection`, `samplers`) out of 1,149 communities.
**What**: Top-20 quant-relevant communities each get a spec-driven `SKILL.md`.
**Priority communities**: ensemble, metrics, preprocessing, pipeline, linear_model, decomposition, feature_selection, calibration, tree, svm, neural_network, clustering, impute, compose, gaussian_process, covariance, cross_decomposition, multiclass, isotonic, kernel_approximation.
**How**: For each community: extract god node → neighborhood → method signatures → author SKILL.md with frontmatter, quick reference, pitfalls, references.
**Verification**: 20+ SKILL.md files in `skills/<library>/<community>/`. Each has `graph_hash` frontmatter.
**Depends on**: 1.1, 1.2.
**Unlocks**: First-mover quant skill registry on SkillDock, usable agent capabilities.

### 2.2 Graph Query Pipeline ⬜
**Status**: No query interface. `graphify query` exists but no project wrapper.
**What**: `scripts/query_graph.py` — a Python CLI that wraps `graphify query`, `graphify path`, `graphify explain` against both graphs.
**How**: Python script with argparse subcommands. Loads graph.json, traverses, prints results.
**Verification**: `python scripts/query_graph.py sklearn "How does Pipeline work?"` returns structured answer.
**Depends on**: 1.1.
**Unlocks**: Agent can query graphs programmatically, skills can embed query results.

### 2.3 Skill-to-Graph Traceability ⬜
**Status**: Skills claim API surface but no auto-generated `references/api.md`.
**What**: For each skill, auto-extract its community's node neighborhood → method signatures → `references/api.md`.
**How**: Script: given a community label, find its nodes in graph.json, extract `source_file`, `source_location`, `label`, neighbor edges → write reference docs.
**Verification**: Every `references/api.md` has per-node `source_file:line` citations.
**Depends on**: 1.1, 1.2, 2.1.
**Unlocks**: Verifiable claims, freshness tracking, auditability.

---

## Wave 3 — Infrastructure

### 3.1 CI Freshness Pipeline ⬜
**Status**: Graphs frozen at single commits. No auto-update.
**What**: GitHub Action: weekly `git pull` upstream → detect changes → `graphify --update` → commit updated graphs → open PR if significant changes.
**How**: `.github/workflows/graph-freshness.yml` with cron schedule, graphify update, diff detection.
**Verification**: Action runs on schedule. PR opened when upstream diverges.
**Depends on**: Wave 1 complete.
**Unlocks**: Living graphs, reproducible extraction, version-pinned skills.

---

## Wave 4 — Integration & Production

### 4.1 Cross-Library Edges ⬜
**Status**: scikit-learn and optuna graphs are isolated. No "RandomizedSearchCV → TPESampler" bridge.
**What**: A third "integration" graph or injected cross-edges connecting quant workflows across libraries.
**How**: Agent identifies natural bridges (e.g., `sklearn.model_selection.RandomizedSearchCV` ↔ `optuna.samplers.TPESampler` both do hyperparameter optimization) → injects INFERRED cross-edges.
**Verification**: `graphify path "GridSearchCV" "TPESampler"` returns a path.
**Depends on**: Wave 1, Wave 2.
**Unlocks**: Multi-library queries, quant workflow graphs.

### 4.2 Quant Usage Patterns ⬜
**Status**: Graphs capture library API structure, not usage. No "walk-forward validation" or "factor importance ranking" nodes.
**What**: `skills/quant-patterns/` — usage-level skills that reference both graphs: walk-forward CV, regime detection, factor ranking, portfolio optimization, backtesting loops.
**How**: Author skills manually (these are domain knowledge, not extractable). Each skill references graph nodes from both libraries.
**Verification**: 5+ quant-pattern skills with cross-library graph references.
**Depends on**: Wave 1, Wave 2, 4.1.
**Unlocks**: Production quant agent, differentiated ecosystem position.

---

## Progress Tracker

| Item | Status | Started | Completed | Artifacts |
|------|--------|---------|-----------|-----------|
| 1.1 Node Descriptions | 🔄 In Progress | 2026-07-29 | — | 6,215/18,753 (Task 2 done, Task 1 in memory) |
| 1.2 Community Labels | ✅ Complete | 2026-07-29 | 2026-07-29 | 1,149 labels in `.graphify_labels.json` |
| 1.3 Edge Validation | ⬜ Pending | — | — | `docs/edge-audit.md` |
| 2.1 Per-Community Skills | 🔄 In Progress | 2026-07-29 | — | 14 skills being extracted (2 sub-agents) |
| 2.2 Query Pipeline | ✅ Complete | 2026-07-29 | 2026-07-29 | `scripts/query_graph.py` |
| 2.3 Graph Traceability | ✅ Complete | 2026-07-29 | 2026-07-29 | `scripts/extract_skill_refs.py` |
| 3.1 CI Freshness | ✅ Complete | 2026-07-29 | 2026-07-29 | `.github/workflows/graph-freshness.yml` |
| 4.1 Cross-Library Edges | ✅ Complete | 2026-07-29 | 2026-07-29 | 6/7 bridges in `docs/cross-library-bridges.json` |
| 4.2 Quant Usage Patterns | ⬜ Pending | — | — | `skills/quant-patterns/` |

---

## Methodology Notes

### When to Use Sub-Agents
- **Parallel**: Items with no shared dependency (1.1 + 1.2 can run together)
- **Sequential**: Items that unlock the next wave (Wave 1 → Wave 2)
- **Leaf**: Scoped tasks with clear completion criteria (process N batches, label M communities)
- **Orchestrator**: Multi-step waves where one agent coordinates workers (Wave 2 skill extraction)

### Quality Gates Per Item
1. **Completeness**: Did we process ALL items (not just a sample)?
2. **Verifiability**: Can someone reproduce the result from graph source?
3. **Traceability**: Does every skill claim link back to a graph node?
4. **Freshness**: Is the version/commit pinned and checkable?

### File Hygiene
- `.graphify/description-instructions/` — delete after processing (temporary artifacts)
- `.graphify/label-instructions/` — delete after labeling
- `docs/` — permanent audit trails, methodology
- `scripts/` — reproducible tooling, committed
- `skills/` — permanent skill artifacts, committed
