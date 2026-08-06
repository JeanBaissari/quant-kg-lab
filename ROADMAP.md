# quant-kg-lab — Roadmap

> **Mission**: consolidate the existing 10 library graphs + skills into a single **gold standard**
> — verifiable, uniform, and composable — before expanding to new libraries.
> Canonical specs: `docs/SKILL_SPEC.md`, `docs/GRAPH_SPEC.md`. Pins: `graphs.lock`.

## State of the repo (accurate as of this roadmap)

| Layer | State |
|-------|-------|
| Knowledge graphs | 10/10 extracted (~133K nodes, ~256K edges) |
| Semantic node descriptions | **2/10 real** (scikit-learn 88.9%, optuna 36.7%); other 8 are AST-stub only → Phase 1 |
| Community labels | 2/10 real (sklearn, optuna); others default `"Community N"` → Phase 1 |
| Skills | 46 `SKILL.md`, but **3 inconsistent templates**, 1 broken router, 22 dangling `references/` → Phase 2 |
| Skill validation | partial (CI installs 5/10 libs; validator has known false-negatives) → Phase 3 |
| Cross-library bridges | 28/29 **defined** in JSON, **not injected** as edges → Phase 4 |
| Docs | specs added; `UNIFIED_INDEX.md` still a stale template → Phase 4/5 |

## Gold-standard bar (per library)

Re-extracted at a pinned commit with **real** descriptions + labels, **noise-filtered** god
nodes, every skill on the **one template**, every claim **traceable to a graph node** and
**validated against the live API**, cross-library **bridges as real edges**, and depth matched to
API importance. Full definitions: `docs/GRAPH_SPEC.md` §5 and `docs/SKILL_SPEC.md`.

---

## Phase 0 — Truth reset & foundations  ✅ (this cycle)

- [x] `LICENSE`, `requirements.txt`
- [x] `docs/SKILL_SPEC.md` — the single skill template + frontmatter schema
- [x] `docs/GRAPH_SPEC.md` — graph schema, noise-filter policy, quality gate
- [x] `graphs.lock` — pinned upstream commits for all 10 libraries
- [x] `scripts/rebuild_graph.sh` — reproducible per-library rebuild
- [x] Archived stale plans → `docs/archive/`; rewrote `README.md` + this roadmap
- [x] `CLAUDE.md` — repo conventions for agents

## Phase 1 — Rebuild all 10 graphs, done right  🔧 (pipeline PROVEN working)

> **graphify runs here, from scratch, with NO API key / NO credits.** Verified 2026-08-06:
> code extraction is a local tree-sitter AST + Louvain pass (no LLM); node descriptions use
> graphify's **assistant mode** (emits batch prompts the assistant answers — still no key).
> End-to-end proof: ta-lib Python API re-extracted from scratch → 10/10 nodes described.
> Working invocation captured in `scripts/rebuild_graph.sh`. graphify install: isolated
> (`npm i @sentropic/graphify` in a dir whose parent has no node_modules), then `GRAPHIFY_CLI`.

- [x] Proven: `graphify extract <pkg> --no-description --no-label --exclude …` (local, no LLM)
- [x] Proven: `graphify describe` assistant loop ingests answers → real descriptions (no key)
- [x] `scripts/rebuild_graph.sh` uses the real, working invocation (package-dir + noise excludes)
- [x] `scripts/query_graph.py` accepts all 10 libraries
- [ ] Run for all 10: clone@pin → extract → answer describe batches → ingest → labels
- [ ] Every graph passes the Quality Gate (`docs/GRAPH_SPEC.md` §5)

## Phase 2 — Normalize all 46 skills to `SKILL_SPEC`

- [ ] One template + one frontmatter schema across every skill (retire the 3 generations)
- [ ] Fix `skills/scikit-learn/SKILL.md` router name collision; add routers for all multi-skill libs
- [ ] Remove/generate the 22 dangling `references/` sections (`scripts/extract_skill_refs.py`)
- [ ] Rebalance depth from clean god-nodes (expand pandas/backtrader/ta-lib; split overloaded files)
- [ ] Re-ground content on the rebuilt graphs (kill hallucinated API + duplicate headers)

## Phase 3 — Verifiable skills

- [ ] Harden `scripts/validate_skills.py`: validate functions; scope to module; fix `infer_library`
      (`quant-patterns` → "unknown"); fix optuna false-negatives
- [ ] Provenance check: every cited graph node resolves in `graph.json`
- [ ] CI installs all 10 libraries; validation + provenance gate PRs; pin versions in frontmatter

## Phase 4 — Composable quant stack  ✅ (rebuild-independent parts done)

- [x] `scripts/inject_cross_edges_v2.py` resolves bridges precisely + writes a `_cross_library` overlay graph
- [x] Playbooks authored: `quant-full-pipeline`, `quant-factor-research`, `quant-ml-strategy`
- [x] `docs/UNIFIED_INDEX.md` regenerated via `scripts/build_unified_index.py` (domain overlay)
- [ ] After rebuild: re-resolve the 3 noise-only bridges + add the node-level concept index

## Phase 5 — Docs standardization & the before/after narrative  ✅

- [x] `docs/README.md` — living-reference vs generated vs archive, with a naming convention
- [x] `methodology.md` v2; `docs/BEFORE_AFTER.md` case study; `docs/workflows.md` (dev patterns & ideas)
- [x] `README.md` finalized as the front door (Phase 0)

## Phase 6 — Library expansion (deferred; scoped only)

Once the 10 are gold standard, add, in priority order: **statsmodels**, **cvxpy**,
**PyPortfolioOpt**, then arch, riskfolio-lib, pyfolio, alphalens, polars, shap. Rationale in
`docs/archive/AUDIT.md` §5.2.

---

## Execution notes

- Phases are largely sequential (0 → 1 → 2 → 3 → 4 → 5); Phases 2–3 fan out per-library and are
  good candidates for parallel sub-agent waves once `SKILL_SPEC.md` + rebuilt graphs exist.
- Commit per phase so the before/after is legible in git history.
