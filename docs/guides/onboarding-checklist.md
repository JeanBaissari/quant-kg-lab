# Onboarding Checklist — new library through the QKG pipeline

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-12

> Seed for QKG_018 (onboarding playbook), written from the first new-library run
> (statsmodels, QKG_019 stress test, 2026-08-12). Every step lists its **Verify**
> command. Findings from the stress run are at the bottom — read them before starting;
> they are the friction the happy path does not show you.

## 0. Prerequisites

- Worktree on a fresh branch off `main` (one branch per library wave).
- graphify CLI installed: `eval "$(bash scripts/install_graphify.sh)"` → exports `GRAPHIFY_CLI`.
- Network access (clone) + PyYAML (hub generator).

## 1. Pin

- Add `<lib>` to `graphs.lock` with the full 40-char SHA of upstream HEAD
  (`git ls-remote https://github.com/<org>/<repo> HEAD` — do not clone first),
  `"nodes": 0, "edges": 0`.
- **Verify**: `python3 -c "import json; print(json.load(open('graphs.lock'))['libraries']['<lib>']['commit'])"` prints a 40-char SHA.

## 2. Clone + extract

- Clone at the pin: `git clone --filter=blob:none https://github.com/<org>/<repo> knowledge_graphs/<lib>/repo`, then `git checkout <pin>`.
- Extract the importable package subdir (see `pkg_subdir()` in `scripts/rebuild_graph.sh`) with the §6 exclude set from the recipe, **plus any library-specific excludes the findings require**:
  - `--exclude 'tests/'` (nested test dirs — `tests/**` only matches root-level),
  - corpus-extension excludes for non-code data files graphify classifies as documents (`*.m`, `*.txt`, `*.html`, …) — any of these abort the run with
    *"error: detected non-code corpus files that require semantic extraction"*.
- **Verify**: `knowledge_graphs/<lib>/.graphify/GRAPH_REPORT.md` exists; `grep -c "Included files"` shows no test paths in the report; no corpus abort in the log.

## 3. Prune

- `python3 scripts/prune_graph.py <lib> --dry-run` — review removals:
  - legit §6 noise (test paths, `conftest`, bench dirs) → apply,
  - **watch for substring false positives**: paths containing `test_` as part of a real module name (statsmodels hit `hypothesis_test_results.py`).
- Restore any false positives (re-merge nodes + their links from `.prune.bak`), then
  `python3 scripts/prune_graph.py <lib> --apply`.
- **Verify**: `python3 scripts/graph_gate.py <lib>` → criterion **c3 PASS** (clean god nodes).

## 4. Labels

- `python3 scripts/label_communities.py <lib> --dry-run` (spot-check ~10 labels are real module · symbol centroids), then `--apply`.
- **Verify**: `python3 scripts/graph_gate.py <lib>` → **c1 PASS**.

## 5. Edge audit

- `python3 scripts/audit_edges.py <lib>` writes `docs/reference/edge-audits/edge-audit-<lib>.md`.
- **Verify**: `python3 scripts/graph_gate.py <lib>` → **c5 PASS**.

## 6. Descriptions (deferred — separate wave)

- Do **not** run the description pass here. Report the workload instead:
  `python3 scripts/describe_nodes.py --coverage <lib>`.
- **Verify**: describable count printed (statsmodels: 6157 public-API nodes).

## 7. Library hub

- `python3 scripts/build_library_docs.py` is lock-driven; add `<lib>` to its `DOMAIN` taxonomy if missing. It regenerates **all** hubs — revert the date-only diffs of the other libraries before committing.
- **Verify**: `docs/libraries/<lib>/index.md` exists with the pinned `Source` commit and graph counts.

## 7.5 API-surface probe (language-invisible symbols) — NEW, mandatory

Extraction only sees Python `def`s: Cython modules (`.pyx`) and C-only symbols
(`arange`, ufuncs, scalar types) **cannot ever appear from re-extraction**
(see F8 — numpy's template case). After the description wave:

- `python3 scripts/api_surface_diff.py <lib> --manifest` — diff public top-level
  symbols vs the graph, classify M1/M2/M3, emit `tools/curated/<lib>.json`
  (descriptions harvested from the live API).
- Review the manifest (spot-check ~10 descriptions + every `source_file` is
  truthful), then `python3 scripts/inject_curated_nodes.py <lib> --apply`.
- Regenerate the probe report + surface json: `python3 scripts/api_surface_diff.py <lib>`.
- **Verify**: `python3 scripts/api_surface_diff.py <lib> --ci` exit 0 (coverage
  ≥95%); `python3 scripts/graph_gate.py <lib>` → **c6 PASS**; skill QR rows
  complete: `python3 scripts/verify_citations.py --require-complete <lib>` exit 0.
- Restamp the library's skill `graph:` blocks (nodes/edges/hash) and sync
  `graphs.lock` counts — curated nodes are part of graph.json.

## 8. Sync + gate + commit

- Set `graph.json` → `graph.built_from_commit` = pin:
  `python3 scripts/stamp_graphs.py <lib>` (QKG_005), then sync `graphs.lock`
  node/edge counts to the final graph.
- Regenerate the gate report: `python3 scripts/graph_gate.py <lib>` (c1–c6).
- Commit per step (pin/extract, prune, labels, audit, hub, checklist, tool fixes separately). Never commit `repo/` or `.graphify` intermediates (nested patterns ignored since QKG_018 F7).

## Findings (QKG_019 stress run — statsmodels)

- **F1 — Nested test dirs defeat `tests/**`.** graphify's `--exclude` globs are root-anchored
  (`globDenyMatch`: `tests/**` requires the path to start with `tests/`). statsmodels nests
  `tests/` at every subpackage (`tsa/statespace/tests/…`), so 449 test files leaked in and the
  run aborted on unsupported corpus files. Workaround: add `--exclude 'tests/'` (the non-glob
  form matches any path segment). The shared recipe (`rebuild_graph.sh`) only carries
  `tests/**` — needs amending for non-flat layouts.
- **F2 — Non-code corpus files hard-abort extraction.** `.m`/`.mat`/`.do`/`.R`/`.f90` MATLAB,
  Stata, R reference files under `tests/results/` plus `.txt`/`.html` dataset metadata were
  classified as `document` corpus files; without a semantic backend the run exits
  *"error: detected non-code corpus files that require semantic extraction"*. Workaround:
  exclude the extensions (`--exclude '*.m' --exclude '*.txt' --exclude '*.html'`).
  Note: graphify has **no tree-sitter for objc/matlab/fortran/R** — unsupported-language
  files in the scan root are a hard failure, not a skip.
- **F3 — Prune substring false positive.** `PATH_PATTERNS` contains bare `test_`, which
  matches `tsa/vector_ar/hypothesis_test_results.py` — a real public API module (imported by
  `var_model`, `svar_model`, `irf`, `vecm`). 21 nodes + 597 links were restored manually from
  `.prune.bak`. Recommendation for QKG_004 tooling: per-lib path allow-list (mirror
  `LIB_EXTRA_SYMBOLS`) or segment-anchored patterns (`/tests/`).
- **F4 — No stamp tool committed.** Nothing writes `graph.built_from_commit`; c4 is FAIL for
  all 11 libraries until the QKG_005 stamp tool lands. The field was set manually per
  GRAPH_SPEC §2 for statsmodels. **RESOLVED (QKG_005):** `scripts/stamp_graphs.py <lib>` writes
  it; step 8 uses the tool.
- **F5 — Hardcoded library lists.** `scripts/graph_gate.py` `ALL` rejects unknown libraries
  (`exit 2 "unknown library"`) — statsmodels added. `scripts/build_library_docs.py` `DOMAIN`
  missing statsmodels — added to Foundation. (`audit_edges.py` needs no list — it takes any
  lib argument.) These hardcoded rosters will keep breaking with every new library until they
  derive from `graphs.lock`.
- **F6 — Edge-quality signal.** statsmodels is 57.3% INFERRED edges (worst of the fleet,
  above sklearn's 53%). INFERRED fan-out from docstring/warning helpers (`Appender` 1089,
  `ValueWarning` 835) drives most cross-module "suspicious" edges. Not a gate failure, but a
  description-pass + edge-audit follow-up target.
- **F7 — `.gitignore` never ignores nested `.graphify` intermediates.** The graphify
  patterns (`.graphify/.graphify_detect.json`, …) contain a slash, so git anchors them at the
  repo root — they never match `knowledge_graphs/<lib>/.graphify/`. Neither the old
  `graphify_*.json` names nor the 0.17.1 set (`entities.json`, `manifest.json`, `scope.json`,
  `scene.json`, `reconciliation-candidates.json`, `workspace-manifest.json`, `studio/`) are
  ignored in practice. Stage only the three canonical artifacts (graph.json, GRAPH_REPORT.md,
  .graphify_labels.json) until the patterns are fixed. **RESOLVED (QKG_018 F7):** every
  intermediate now carries a `**/.graphify/...` pattern (plus the 0.17.1-era set and
  `description-instructions/`); `git check-ignore` verifies nested paths; the three canonical
  artifacts remain explicitly un-ignored.
- **F8 — Language-invisible API surface (QKG_021 template case, numpy).** tree-sitter has no
  Cython grammar and extracts only Python `def`s. numpy: 199/499 top-level symbols absent —
  whole `.pyx` modules (`random/_generator.pyx`), C-only ufuncs/builtins (`arange`, `sin`,
  `dtype` — no `def` exists anywhere), plus a few Python-def'd misses (`array2string`).
  Re-extraction **cannot** fix M1/M2. Mechanism (ADR-0008): curated manifest
  (`tools/curated/<lib>.json`) → curated nodes with truthful `source_file`; gate criterion c6;
  `--require-complete` on skill QR rows. Run step 7.5 for every library.
- **F9 — Label collisions between submodules and the top-level API.** `np.array` resolves to
  `_core/defchararray.py`'s char-array `array()` — label-resolution can't tell them apart.
  Curate the top-level symbol explicitly (source `__init__.py` / true binding module) and cite
  the curated node in the skill; verify with a spot check of `array`/`asarray`-class rows
  (`verify_citations.py --require-complete` + a human look at first-column collisions).
- **F10 — Inline-duplicated table headers (tooling hygiene).** The annotation tool appended a
  `Graph Node` header cell per row, leaving single-line headers like
  `| API | Signature | Description | Graph Node | Graph Node | …` in 11 skills (numpy/linalg
  had 19). Consecutive-line checks miss inline repeats — scan for `line.count('| Graph Node |') > 1`
  after any annotation wave before committing.

*Last verified against the repo: 2026-08-12.*
