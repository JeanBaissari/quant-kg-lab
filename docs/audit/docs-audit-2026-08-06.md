# Docs Audit — 2026-08-06

**Type**: Audit
**Date**: 2026-08-06
**Status**: current
**Verdict**: flat/inconsistent `docs/` restructured into a governed, modular system; fat removed
**Last Verified**: 2026-08-06

## Executive summary

`docs/` was a flat pile of 25 files with no taxonomy, no templates, two partial indexes, and stale
artifacts. It is now a modular, standards-governed corpus (single `docs/` surface, doc-type taxonomy,
identity blocks, per-library hubs, ADRs, CI gate). Skills/graphs remain the authoritative reference;
docs index them.

| Metric | Before | After |
|--------|--------|-------|
| Structure | flat, 25 files | `specs/ guides/ libraries/ reference/ adr/ audit/ narrative/ _development/` |
| Doc-type taxonomy | none | closed 7-type enum + identity block |
| Templates / standards | none | `_development/standards.md` + 5 templates |
| Indexes | 2 partial | 1 two-tier hub (`docs/index.md`) |
| Per-library docs | none | 11 generated hubs |
| Decision records | none | 6 ADRs |
| Docs CI gate | none | `scripts/doc_audit.py` |

## Findings

| ID | Severity | Finding | Evidence | Verdict |
|----|----------|---------|----------|---------|
| D-1 | high | Orphaned v1 bridges JSON + dead producer script | `docs/cross-library-bridges.json`, `scripts/inject_cross_edges.py` | DELETED |
| D-2 | med | Naming-vs-type conflict (`UNIFIED_INDEX.md` UPPER but generated) | old `docs/UNIFIED_INDEX.md` | FIXED → `docs/reference/unified-index.md` + banner |
| D-3 | med | Two partial indexes, no single hub | old `docs/README.md`, `UNIFIED_INDEX.md` | FIXED → `docs/index.md` two-tier hub |
| D-4 | med | Pipeline restated in 3 places | `methodology.md`, `BEFORE_AFTER.md`, `GRAPH_SPEC §8` | FIXED → single source in `guides/methodology.md`, cross-linked |
| D-5 | low | Stale `2026-07-29` dates across generated docs | edge-audits | FIXED → regenerated on the fresh graphs |
| D-6 | low | Near-empty edge-audit stubs (100%-EXTRACTED libs) | `edge-audit-{xgboost,lightgbm,ta-lib}.md` | OPEN → emit an explicit "no INFERRED edges" line (`audit_edges.py`) |

## Action items

- [x] Restructure `docs/` + update all inbound references (Workstream B)
- [x] Standards engine + templates + hub (Workstream A)
- [x] Per-library hubs on the fresh graphs (Workstream C)
- [x] ADRs capturing the real decisions (Workstream D)
- [ ] `scripts/doc_audit.py` + CI `docs-audit` job (Workstream E)
- [ ] Online-docs ingestion for numpy/sklearn (Workstream F — needs the user's key)
- [ ] D-6: explicit "no INFERRED edges" line in the 3 stub edge-audits

*Last verified against the repo: 2026-08-06.*
