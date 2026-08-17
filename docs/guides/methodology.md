# Methodology — the quant-kg-lab pipeline

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-17

How a library becomes a set of verifiable, copy-in skills. Four stages, each reproducible.
Specs: [`GRAPH_SPEC.md`](../specs/GRAPH_SPEC.md) (graphs), [`SKILL_SPEC.md`](../specs/SKILL_SPEC.md) (skills).

```
 EXTRACT ───▶ QUERY ───▶ AUTHOR ───▶ VALIDATE
 graphify     god nodes   SKILL.md    live API + graph provenance
 @pinned      communities  one spec    lint gate in CI
```

## 1. Extract — source → knowledge graph

We use [graphify](https://github.com/sentropic/graphify) (`npm i -g @sentropic/graphify`) to
ingest a library's source tree at a **pinned commit** (recorded in [`/graphs.lock`](../../graphs.lock))
and emit a networkx node-link graph.

- Reproducible entry point: `scripts/rebuild_graph.sh <lib>` — clone@pin → `graphify extract --no-description --no-label` → assistant loop for descriptions → Louvain clustering → audit.

- The **noise filter** (`GRAPH_SPEC.md` §6) excludes tests, benchmarks, examples, and
  binding-internals so the graph reflects the *public API*, not the test harness.
- Requires the graphify CLI **and** network access to clone upstream — run it on a full machine,
  not a network-restricted sandbox.

Graph schema (nodes = code entities + rationale; edges = calls/inherits/imports/uses, each tagged
`EXTRACTED`/`INFERRED`/`AMBIGUOUS`) is defined in `GRAPH_SPEC.md`.

## 2. Query — find the API that matters

- `scripts/query_graph.py <lib> "<term>"` — substring + BFS over any of the 28 graphs (plus the
  `_cross_library` overlay).
- **God nodes** (highest degree) are the API hubs; **communities** are the natural module
  boundaries. After the noise filter, these reflect real user-facing API — the signal that tells
  us which modules deserve a skill and what a skill's Quick Reference should contain.

## 3. Author — graph → skill

One skill per quant-relevant module, following `SKILL_SPEC.md`:
- one template, one frontmatter schema, `name` unique, `description` a "Use when" trigger;
- every Quick-Reference row cites a graph node (`source_file:line`) — the traceability that makes
  the skill *verifiable*;
- multi-skill libraries get a router; playbooks (`skills/quant-patterns/`) compose atomic skills
  into cross-library workflows.
- `scripts/normalize_skills.py` enforces the template mechanically across all skills.

## 4. Validate — trust, then rely

`scripts/validate_skills.py` runs three checks:
- **Lint** (CI gate): frontmatter schema, unique "Use when" names, no dangling `references/`,
  `source_commit` matches `graphs.lock`, routers present.
- **API**: every claimed class/function exists in the installed library (public / private-internal
  / genuinely-absent tiers) — the anti-hallucination guarantee.
- **Provenance**: cited source files resolve to a node in `graph.json`.

CI (`.github/workflows/skill-validation.yml`) runs a fast deterministic lint gate plus a
best-effort all-28-library API/provenance job.
Freshness is tracked by the `built_from_commit` field in each graph.

## Reproduce from scratch

```bash
npm i -g @sentropic/graphify
pip install -r requirements.txt
scripts/rebuild_graph.sh <lib>          # per library, on a machine with network
python scripts/normalize_skills.py --apply
python scripts/validate_skills.py --provenance
python scripts/build_unified_index.py
```
