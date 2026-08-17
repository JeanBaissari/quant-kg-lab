# Before / After — the consolidation

> **Note**: This document describes the state of the repo at commit 368f6f0 on 2026-08-12. For current state, see [README.md](../../README.md).

**Type**: Narrative
**Status**: historical
**Last Verified**: 2026-08-12

This repo is its own case study: how a promising-but-drifted "pile of skills" became a verifiable,
reproducible, composable knowledge base. If you're building something similar for *your* stack,
this is the transformation — and the method — in one page.

## The problem (before)

The substance was real (10 library graphs, ~133K nodes, 46 skills, CI, cross-library bridges), but
it *read* like "another random skills repo" because of **drift**, not thin content:

- **Three template "generations"** with three different frontmatter schemas; the `description`
  voice drifted between trigger-style and noun-phrase blurbs.
- **22 skills linked `references/api.md` + `references/examples.md` that were never generated.**
- **The scikit-learn "router" was a bug** — a duplicate of `model_selection` with a colliding `name`.
- **8 of 10 graphs were AST-stub-only** — "Token cost: 0", default `"Community N"` labels
  (pandas' label map was literally `{"None": "Tests"}`), yet reported as "96% described".
- **God nodes were extraction noise** — `__pyx_...RSI()`, `XGBoostJNI`, `Benchmark`, test files —
  not the real API. Querying "RSI" returned a Cython trampoline; "DMatrix" returned the R package.
- **Cross-library bridges resolved to garbage** — "28/29 found" pointed at benchmark files and
  docstring fragments.
- **Three sources of truth disagreed**: README said 2 libraries (Phase 1), ROADMAP said 8 libs at
  0% descriptions (already done), UNIFIED_INDEX was an unfilled template.
- **No reproducibility scaffolding**: no `LICENSE`, `requirements.txt`, `Makefile`, or pinned commits.

## The intervention (after)

| Dimension | Before | After |
|-----------|--------|-------|
| Skill templates | 3 inconsistent generations | **1** spec (`SKILL_SPEC.md`), enforced by `normalize_skills.py` |
| Frontmatter schemas | 3 variants | **1** schema; `source_commit` pinned to `graphs.lock` |
| Dangling `references/` | 22 skills | **0** |
| Routers | 1 broken (name collision) | **9** clean, bare-library names |
| "Use when" descriptions | 32/46 | **56/56** |
| Skill validator | class-only, ~false-negatives (optuna router "failed") | lint gate + API tiers + provenance; **0 hallucinations**, false-positives cut 50 → 0 |
| Cross-library bridges | 28/29 to noise | **16/19 to real classes**, honest about the rest; written as a queryable overlay graph |
| Graph reproducibility | none | `graphs.lock` (10 pinned commits) + `rebuild_graph.sh` |
| Sources of truth | 3 disagreeing | README = ROADMAP = UNIFIED_INDEX, generated from disk |
| Scaffolding | missing | `LICENSE`, `requirements.txt`, `CLAUDE.md`, specs, CI split into lint gate + API |

## What makes it stand out (the two bets)

1. **Verifiable skills.** Every claim traces to a graph node and is checked against the live API in
   CI. A skill you can *trust* — not a hallucinated cheatsheet. The validator caught real content
   risks and, tuned for precision, distinguishes public / private-internal / genuinely-absent
   symbols so it never cries wolf.
2. **A composable quant stack.** Bridges + workflow playbooks (`quant-full-pipeline`,
   `quant-factor-research`, `quant-ml-strategy`) encode *how* the libraries compose into research
   loops. It reads as one stack, not ten isolated references.

## Honest status (what's still ahead)

The skills are **structurally** gold-standard and validated, but not yet **content-regrounded**:
8/10 graphs remain AST-stub until the Phase-1 rebuild (`rebuild_graph.sh`, needs graphify + network).
That rebuild is the gate for real semantic descriptions, clean god nodes, and the final bridge/
concept resolution. Tracked in [`ROADMAP.md`](../../ROADMAP.md).

## The method, transferable to your stack

1. Write the **specs first** (`SKILL_SPEC`, `GRAPH_SPEC`) — the single source of truth for "done".
2. **Pin** your sources (`graphs.lock`) and script the rebuild.
3. **Normalize mechanically** (a script beats 46 hand-edits for consistency).
4. **Validate in CI** — a lint gate you can keep green, plus best-effort API/provenance.
5. **Compose** — atomic skills + playbooks + a cross-library overlay.
6. Keep **one** source of truth and generate the rest.
