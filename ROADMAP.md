# quant-kg-lab — Roadmap

> **Mission**: consolidate the 11 library graphs + skills into a single **gold standard**
> — verifiable, uniform, and composable — before expanding to new libraries.
> Canonical specs: `docs/specs/SKILL_SPEC.md`, `docs/specs/GRAPH_SPEC.md`. Pins: `graphs.lock`.
> Planning/tracking lives in the hermes-vault PRD index (QKG_001–021); this file is the pointer + live status.

## State of the repo (accurate as of this roadmap)

| Layer | State |
|-------|-------|
| Knowledge graphs | 11/11 extracted (~65K nodes, ~163K edges), incl. statsmodels stress wave |
| Semantic node descriptions | **11/11 ≥80%** (81–100%; ta-lib 93.8%) — `describe_nodes.py --auto` via opencode; numpy random API curated (QKG_021) |
| Community labels | **11/11 real** (0 default `"Community N"`; e.g. pandas 396, scipy 1061, statsmodels 638) |
| Quality Gate | **11/11 GREEN** (c1 labels · c2 descriptions · c3 god nodes · c4 pin · c5 audited) — `scripts/graph_gate.py --ci --all` exits 0 |
| Skills | 56 `SKILL.md` (9 routers + 39 modules + 8 playbooks), uniform template, 0 dangling refs; graph blocks synced (QKG_010); content wave done (QKG_011–013): canonical headers, auto-Provenance, Common Patterns, playbook §7, citation gate **264/0** (QKG_012) |
| Skill validation | validator v2 (sections/hash/related-skills, module-scoped API) gates plain `--ci`; API/TA-Lib gating live (QKG_008); citation gate in lint job; known-debt bridge retired |
| Cross-library bridges | 19/19 resolved, injected as `_cross_library` overlay (24 nodes) |
| Docs | 54-doc governed corpus, `doc_audit.py --ci` green; gate reports in `docs/reference/quality-gate/` |
| CI | lint + docs + provenance gates active; freshness cron replaced by provenance gate + informational report (QKG_006) |

## Gold-standard bar (per library)

Re-extracted at a pinned commit with **real** descriptions + labels, **noise-filtered** god
nodes, every skill on the **one template**, every claim **traceable to a graph node** and
**validated against the live API**, cross-library **bridges as real edges**, and depth matched to
API importance. Full definitions: `docs/specs/GRAPH_SPEC.md` §5 and `docs/specs/SKILL_SPEC.md`.

---

## Phase 0 — Truth reset & foundations  ✅ (this cycle)

- [x] `LICENSE`, `requirements.txt`
- [x] `docs/specs/SKILL_SPEC.md` — the single skill template + frontmatter schema
- [x] `docs/specs/GRAPH_SPEC.md` — graph schema, noise-filter policy, quality gate
- [x] `graphs.lock` — pinned upstream commits for all 11 libraries
- [x] `scripts/rebuild_graph.sh` — reproducible per-library rebuild
- [x] Archived stale plans → `docs/archive/`; rewrote `README.md` + this roadmap
- [x] `CLAUDE.md` — repo conventions for agents

## Phase 1 — Rebuild all 10 graphs, done right  ✅ (now 11 incl. statsmodels)

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
- [x] Run for all 10 (now 11 incl. statsmodels): clone@pin → extract → describe (opencode) → labels → prune → stamp
- [x] Every graph passes the Quality Gate (`docs/specs/GRAPH_SPEC.md` §5) — **11/11 green** (`scripts/graph_gate.py --ci --all`)

## Phase 2 — Normalize all skills to `SKILL_SPEC`  ✅

- [x] One template + one frontmatter schema across every skill (retire the 3 generations)
- [x] Fix `skills/scikit-learn/SKILL.md` router name collision; add routers for all multi-skill libs
- [x] Remove/generate the 22 dangling `references/` sections (`scripts/extract_skill_refs.py`)
- [x] Re-ground content on the rebuilt graphs: canonical headers, auto-Provenance ×48, Common Patterns ×7, QR citations with line numbers, 2 new skills (QKG_011/012)
- [x] Playbook anatomy unified to §7 (QKG_013)
- [ ] Rebalance depth from clean god-nodes (expand pandas/backtrader/ta-lib; split overloaded files) — follow-up (QKG_020 context)

## Phase 3 — Verifiable skills  ✅

- [x] Harden `scripts/validate_skills.py`: validate functions; scope to module; fix `infer_library`
      (`quant-patterns` → "unknown"); fix optuna false-negatives (QKG_007)
- [x] Provenance check: every cited graph node resolves in `graph.json` (QKG_012 — `verify_citations.py` gate, 264/0)
- [x] CI installs all 10 libraries (11 incl. statsmodels); validation + provenance gate PRs; pin versions in frontmatter (QKG_008)

## Phase 4 — Composable quant stack  ✅ (concept index pending)

- [x] `scripts/inject_cross_edges_v2.py` resolves bridges precisely + writes a `_cross_library` overlay graph
- [x] Playbooks authored: `quant-full-pipeline`, `quant-factor-research`, `quant-ml-strategy` (+5 more, §7 anatomy)
- [x] `docs/reference/unified-index.md` regenerated via `scripts/build_unified_index.py` (domain overlay)
- [x] The 3 noise-only bridges re-resolved (ta-lib Cython wrappers, backtrader `DataBase`) — 19/19
- [ ] Node-level concept index (unified-index v2) — drafted as QKG_017

## Phase 5 — Docs standardization & the before/after narrative  ✅

- [x] `docs/README.md` — living-reference vs generated vs archive, with a naming convention
- [x] `methodology.md` v2; `docs/BEFORE_AFTER.md` case study; `docs/workflows.md` (dev patterns & ideas)
- [x] `README.md` finalized as the front door (Phase 0)

## Phase 6 — Library expansion (gated on the gold standard)

✅ **statsmodels** onboarded as a parallel stress wave (QKG_019, gate 5/5, 7 findings codified
in `docs/guides/onboarding-checklist.md`). Next, in priority order: **cvxpy**,
**PyPortfolioOpt** (+ statsmodels skills wave — QKG_020), then arch, riskfolio-lib, pyfolio,
alphalens, polars, shap. Rationale in `docs/archive/AUDIT.md` §5.2. Every new library must
pass the quality gate on day one (QKG_018 playbook).

---

## Execution notes

- Phases are largely sequential (0 → 1 → 2 → 3 → 4 → 5); Phases 2–3 fan out per-library and are
  good candidates for parallel sub-agent waves once `SKILL_SPEC.md` + rebuilt graphs exist.
- Commit per phase so the before/after is legible in git history.
