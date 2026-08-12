# GRAPH_SPEC — Knowledge Graph Schema, Noise Filter & Quality Gate

**Type**: Spec
**Status**: current
**Last Verified**: 2026-08-06

> Authoritative spec for every graph under `knowledge_graphs/<lib>/.graphify/`.
> Governs the Phase-1 rebuild. If a rebuilt graph does not meet the **Quality Gate**
> (§5), it is not done.

## 1. What a graph is

One **undirected** [networkx](https://networkx.org) node-link graph per library, emitted by
[`graphify`](https://github.com/sentropic/graphify) (`npm i -g @sentropic/graphify`) from the
library's source tree at a pinned commit. Nodes are code entities (modules, classes,
functions/methods) and rationale fragments (docstrings/comments); edges are the relationships
between them.

**Committed artifacts** (per library, in `.graphify/`):

| File | Purpose |
|------|---------|
| `graph.json` | The graph (node-link JSON). |
| `GRAPH_REPORT.md` | Human-readable audit: counts, extraction quality, god nodes, communities. |
| `.graphify_labels.json` | `{community_id: "Human Label"}` map. |

Everything else graphify writes (`repo/` source clone, `.graphify_*.json` intermediates,
`description-instructions/`, `cache/`, `memory/`, `wiki/`) is **gitignored** and reproducible.

## 2. Storage format

`graph.json` = `networkx.node_link_data(G)`. Top-level keys:

```json
{
  "directed": false,
  "multigraph": false,
  "graph": {
    "community_labels": { "0": "Samplers — NSGA", "...": "..." },
    "built_from_commit": "<40-char upstream sha>"
  },
  "topology_signature": "n=<N>;e=<E>;<feature-hints>",
  "nodes": [ /* see §3 */ ],
  "links": [ /* see §4 — note the key is "links", not "edges" */ ],
  "hyperedges": []
}
```

`built_from_commit` MUST match the pin in `/graphs.lock`.

## 3. Node schema

Every node carries these keys (no `type`/`kind` field — granularity is inferred from `label`
and `source_location`):

```json
{
  "id": "benchmarks_algorithms",
  "label": "algorithms.py",
  "file_type": "code",
  "source_file": "pandas/core/algorithms.py",
  "source_location": "L1",
  "community": 419,
  "community_name": "Factorize & Hashing",
  "description": "Factorization and hashing helpers: factorize, unique, value_counts..."
}
```

- `file_type` ∈ `code` | `rationale` (docstring/comment text) | `doc`.
- `description` is the field skills quote. A node is **described** only if `description` is a
  non-empty *semantic* summary — **not** an AST stub of the templated form
  `"Python module at <path> containing symbols such as A, B, C"`. Stubs count as **undescribed**
  for the Quality Gate (§5). This is the single most important correction versus the current
  state, where 8/10 libraries are AST-stub-only.

## 4. Edge (link) schema

```json
{
  "source": "accessors_test_cat_accessor",
  "target": "numpy",
  "relation": "imports",
  "confidence": "EXTRACTED",
  "confidence_score": 1,
  "source_file": "pandas/tests/series/accessors/test_cat_accessor.py",
  "source_location": "L1",
  "weight": 1
}
```

- **`relation`** vocabulary: `method`, `uses`, `contains`, `calls`, `imports_from`, `imports`,
  `inherits`, `rationale_for`. New relations MUST be documented here before use.
- **`confidence`**: `EXTRACTED` (AST-derived, score 1) | `INFERRED` (semantic guess, score ~0.5) |
  `AMBIGUOUS`. `docs/reference/edge-audits/edge-audit-<lib>.md` reports the ratio per library.

## 5. Quality Gate (definition of done for a rebuilt graph)

A rebuilt graph is **gold standard** only when ALL hold:

1. **Real labels** — `.graphify_labels.json` has no default `"Community N"` values and no
   degenerate maps (the current pandas map is literally `{"None": "Tests"}`); labels cover
   ≥ 95% of non-singleton communities.
2. **Real descriptions** — ≥ 80% of *retained public-API code nodes* (§6) have semantic
   descriptions (not AST stubs). AST-only extraction (`Token cost: 0` in the report) does **not**
   pass this gate.
3. **Clean god nodes** — the top-20 nodes by degree contain **zero** excluded-noise symbols
   (§6). Current failures to fix: `__Pyx_AddTraceback` (ta-lib), `XGBoostJNI` (xgboost),
   `Benchmark` (scipy), `AxisError` (numpy), test/benchmark files.
4. **Pinned & reproducible** — `built_from_commit` is set and matches `/graphs.lock`;
   `scripts/rebuild_graph.sh <lib>` reproduces the graph.
5. **Audited** — `docs/reference/edge-audits/edge-audit-<lib>.md` regenerated; INFERRED ratio reported (sklearn's
   53%-inferred graph is the known worst case to re-check).
6. **API-surface coverage** — ≥ 95% of the library's public top-level symbols resolve to a
   graph node **or** a curated-manifest entry (`tools/curated/<lib>.json`, ADR-0008) **or** an
   explicit manifest exclusion. Measured by `scripts/api_surface_diff.py <lib>` (committed
   report in `docs/reference/api-surface/<lib>.md`), enforced by
   `scripts/verify_citations.py --require-complete <lib>` on every skill Quick Reference row.

### 5.1 Language-coverage note (criterion 6, ADR-0008)

Tree-sitter has **no Cython grammar** and extracts only Python `def`s: whole `.pyx` modules
(M1), C-only ufuncs/builtins like `arange` or `dtype` (M2), and a few Python-def'd symbols
inside known files (M3) can never appear from re-extraction alone. The curated manifest is the
sanctioned mechanism: nodes carry a real description and a truthful `source_file` (the module
where the symbol is bound), joined to that module via a CURATED `contains` link. A symbol
without a node and without a manifest entry is a **gate failure** — silent extraction gaps are
no longer acceptable.

## 6. Noise-filter policy

The extractor MUST exclude the following from the graph (and therefore from god-node ranking
and skill authoring). Rationale: a knowledge graph of a *library's public API* should not be
dominated by its test harness or its C/JNI binding internals.

**Exclude by source path** (test/bench/build/vendor/docs, not the shipped API):
```
tests/            test_*            *_test.py         conftest.py
asv_bench/         benchmarks/       bench/
doc/  docs/  examples/  .github/     setup.py  versioneer*  _vendor/  third_party/  vendored/
```

**Exclude by symbol/label** (compiler & binding internals, not user-facing API):
```
__Pyx_*   __pyx_*   *JNI*   *_safe_call*   TA_*  (raw C entry points, keep the Python wrapper)
```

**Retain but demote** — `rationale`/docstring nodes are kept (they back `rationale_for` edges)
but are **excluded from god-node centrality ranking** so hubs reflect real API, not prose.

Filter patterns live here and are applied at extraction time via graphify's ignore config
(or a post-extract prune pass in `scripts/rebuild_graph.sh`). Any deviation for a specific
library (e.g. ta-lib is legitimately a Cython wrapper — see note below) MUST be recorded in that
library's `GRAPH_REPORT.md`.

> **ta-lib exception**: ta-lib's Python API *is* the Cython wrapper `talib/_ta_lib.c`. There, the
> god node is expected to be the wrapper module; filter only the `__Pyx_*`/traceback trace symbols,
> not the indicator functions.

## 7. Canonical metrics (resolve prior ambiguities)

- **Community count** = number of **distinct `community` IDs assigned to retained nodes**
  (e.g. pandas = 1,986). The lower figure some `GRAPH_REPORT.md` headers show (pandas "1771")
  counts only non-singleton communities; report BOTH, but `community_count` in skill frontmatter
  and `graphs.lock` uses the distinct-ID definition.
- **Description coverage** = `described_code_nodes / retained_code_nodes` using the semantic
  definition in §3 (stubs excluded).

## 8. Rebuild procedure

See `scripts/rebuild_graph.sh <library>`. Pipeline (also in `docs/guides/methodology.md`):

1. Clone upstream at the `/graphs.lock` commit into `knowledge_graphs/<lib>/repo/` (gitignored).
2. `graphify extract --backend claude-cli` with the §6 ignore config → real descriptions + edges.
3. `scripts/merge_descriptions.py` → merge any batched descriptions into `graph.json`.
4. `graphify cluster-only .` → community detection + labels + `GRAPH_REPORT.md`.
5. `scripts/audit_edges.py <lib>` → `docs/reference/edge-audits/edge-audit-<lib>.md`.
6. Verify against the §5 Quality Gate before committing.

> Re-extraction requires the graphify CLI **and** network access to clone upstream. It cannot run
> in a sandbox without those; run it in an environment that has both.
