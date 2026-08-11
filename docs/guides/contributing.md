# Contributing — docs & skills

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-06

How to add or change a doc or a skill without breaking the standards. The two gates are
`scripts/doc_audit.py` (docs) and `scripts/validate_skills.py` (skills).

## Adding a doc

1. Pick the `Type` and copy the matching template from
   [`../_development/templates/`](../_development/templates/README.md) (see the taxonomy in
   [`../_development/standards.md`](../_development/standards.md) §1).
2. Fill the **identity block** (`Type` / `Status` / `Last Verified`) right under the H1.
3. Put it in the right home: `specs/`, `guides/`, `libraries/<lib>/`, `adr/`, `audit/`, `narrative/`.
   Use relative links; every `](path)` must resolve.
4. Run `python scripts/doc_audit.py --ci` — it fails on a missing identity block, a `Type` outside
   the enum, a dangling link, or a census mismatch. Then `--write` to refresh the census.

**Never hand-edit a `Generated` doc** (banner-marked, under `reference/` or `libraries/<lib>/index.md`);
change its producer script and regenerate (see `standards.md` §4).

## Adding / changing a skill

1. Follow [`../specs/SKILL_SPEC.md`](../specs/SKILL_SPEC.md) — one template, one frontmatter schema,
   `name` unique and kebab-case, `description` a "Use when …" trigger, cite graph nodes.
2. `python scripts/normalize_skills.py --apply` normalizes frontmatter/routers mechanically.
3. `python scripts/validate_skills.py --ci` must pass (lint gate). It also checks API existence
   and graph provenance.

## Regenerating derived docs

```bash
python scripts/build_unified_index.py     # docs/reference/unified-index.md
python scripts/build_library_docs.py      # docs/libraries/<lib>/index.md
python scripts/audit_edges.py <lib>       # docs/reference/edge-audits/edge-audit-<lib>.md
python scripts/inject_cross_edges_v2.py --apply   # docs/reference/cross-library-bridges.json + overlay
```

## Committing

Branch off `main`; commit per workstream so history stays legible. Keep `Last Verified` current
when you touch a doc.

## Related

- [Standards](../_development/standards.md) — the canon.
- [Docs index](../index.md) — the hub.

*Last verified against the repo: 2026-08-06.*
