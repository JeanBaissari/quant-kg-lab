# quant-kg-lab

A quantitative knowledge-graph laboratory: extract knowledge graphs from scientific-Python
libraries, distill them into verifiable, copy-in agent skills for quantitative research.

> **Last Verified**: 2026-08-17

## What it is

- **Knowledge graphs from source.** Each of 28 libraries is extracted at a pinned commit via
  `graphify` into a graph of modules, classes, and functions with semantic edges (calls, inherits,
  imports).
- **Verifiable agent skills.** 142 spec-driven `SKILL.md` files (copy-in, not a package) where
  every Quick Reference row cites a graph node (`source_file:line`), and API symbols and graph
  citations are checked against the live library in CI.
- **Cross-library bridges.** 71/71 precise cross-library edges inject a `_cross_library` overlay
  so skills reference related APIs across pandas, scipy, sklearn, etc.
- **18 workflow playbooks.** End-to-end patterns (data -> features -> model -> backtest -> HPO ->
  risk) that compose across the full quant stack.

## Current state

> Numbers sourced from `docs/reference/truth-counts.json`. Counts are CI-gated; a drift-detector
> catches any mismatch — it does not prevent it.

| Metric | Current main | v0.4.0 release |
|--------|-------------|----------------|
| Libraries | 28 | 28 |
| Knowledge-graph nodes | 92,154 | 92,154 |
| Knowledge-graph edges | 229,921 | 229,921 |
| Skills (total) | 142 | 137 |
| - Routers | 27 | 27 |
| - Module skills | 97 | 97 |
| - Playbooks | 18 | 13 |
| Citations checked | 1,207 | 1,147 |
| Dangling citations | 0 | 0 |
| Cross-library bridges | 71 / 71 | 71 / 71 |
| Governed docs | 127 | 126 |

**Path 8/9 additions since v0.4.0**: `qkg` CLI, BM25 full-text search, quality scores, skill
versioning, freshness timestamps, `node_type` frontmatter field, and 5 new playbooks (13 -> 18).

## Quick start

**Path A — `qkg` CLI (recommended)**

```bash
pip install quant-kg-lab   # or clone and pip install -e .
qkg search "kolmogorov smirnov"   # BM25 search across all graphs
qkg skill scipy-stats             # show a skill with citations
```

**Path B — Manual copy (no tools)**

```bash
# Pick a skill directory and copy it into your agent's skills folder
cp -r skills/scipy/stats ~/.claude/skills/scipy-stats
# The name + description frontmatter are required; provenance metadata is carried along.
```

**Path C — GitHub Release assets (no rebuild)**

```bash
# Download from the latest release: graph bundles + skills tarball
unzip qkg-skills.zip               # all skills in copy-in layout
cp -r skills/scipy/stats ~/.claude/skills/scipy-stats
# Verify against your installed library
python3 scripts/validate_skills.py --ci scipy
```

## What is verified

- **Graph provenance**: every graph is rebuildable from its pinned commit in `graphs.lock`.
- **Community labels**: all 28 graphs have real (non-AST-stub) community labels.
- **Semantic descriptions**: all 28 graphs pass >= 80% description coverage (c2 green).
- **Quality gate**: all 28 graphs pass the full gate (c1-c6) — labels, descriptions, clean god
  nodes, pinned commits, audited edges.
- **Skill citations**: Quick Reference API symbols and graph citations are checked; 0 dangling
  citations across 1,207 checked references.
- **Cross-library bridges**: 71/71 resolved and injected as a `_cross_library` overlay.
- **Doc audit**: `scripts/doc_audit.py --ci` passes with 0 errors.

## What is deferred

- **Freshness timestamps**: skill frontmatter includes `last_verified` but automated freshness
  enforcement across the full corpus is not yet in CI.
- **Full API-surface validation**: the validator checks 10 core libraries in CI; the remaining 18
  are validated locally but not in the matrix (planned — QKG_070).
- **Description coverage beyond 80%**: raising the floor from 80% to 95%+ across all graphs is
  tracked but not a current gate.
- **Byte-identical reproducibility**: bundles are sha256-verified within a release, but
  cross-run byte-identical archives are not guaranteed (graphify can produce minor diffs).

## Specs, guides, and references

| Document | Purpose |
|----------|---------|
| `docs/specs/SKILL_SPEC.md` | Single skill template + frontmatter schema |
| `docs/specs/GRAPH_SPEC.md` | Graph schema, noise-filter policy, quality gate |
| `docs/guides/methodology.md` | Full extraction -> authoring -> validation pipeline |
| `docs/guides/onboarding-checklist.md` | How to onboard a new library |
| `ROADMAP.md` | Phased plan and current status |
| `QUICKSTART.md` | Consume the knowledge base in 2 minutes |
| `CLAUDE.md` | Working conventions for agents |
| `docs/reference/truth-counts.json` | Canonical counts (CI-gated) |
| `graphs.lock` | Pinned upstream commits per library |

## License

[MIT](LICENSE). Skills are open-source; graphs are reproducible from `graphs.lock`.
