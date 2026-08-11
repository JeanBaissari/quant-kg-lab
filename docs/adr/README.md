# Architecture Decision Records

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-06

Append-only decision log. An ADR that is not in the index below does not exist — adding the row
is part of writing the ADR. Template: [`../_development/templates/template-adr.md`](../_development/templates/template-adr.md).
Lifecycle: `proposed → accepted → superseded-by: ADR-000N`.

## When an ADR is required

- a change to a **spec contract** (`SKILL_SPEC`, `GRAPH_SPEC`, docs `standards`);
- a change to the **extraction / description pipeline**;
- a **cross-cutting structural** decision (docs layout, taxonomy, re-extraction scope);
- **retiring or replacing** a subsystem or artifact.

## Index

| ADR | Title | Status |
|-----|-------|--------|
| [ADR-0001](ADR-0001-one-skill-template.md) | One skill template + frontmatter schema | accepted |
| [ADR-0002](ADR-0002-graph-noise-filter.md) | Graph noise-filter policy | accepted |
| [ADR-0003](ADR-0003-graphify-assistant-mode.md) | graphify assistant-mode (no-API-key) pipeline | accepted |
| [ADR-0004](ADR-0004-bridges-as-overlay.md) | Cross-library bridges as a precise overlay graph | accepted |
| [ADR-0005](ADR-0005-single-docs-surface.md) | Single `docs/` surface + doc-type taxonomy | accepted |
| [ADR-0006](ADR-0006-package-subdir-extraction.md) | Package-subdir from-scratch re-extraction | accepted |

*Last verified against the repo: 2026-08-06.*
