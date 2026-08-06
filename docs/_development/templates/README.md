# Documentation templates

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-06

The closed template set. Copy the one matching your doc's `Type` (see `../standards.md` §1),
fill the identity block, and delete optional sections you don't need. Keep it lean — no
boilerplate for its own sake.

| Template | `Type` | Use for |
|----------|--------|---------|
| `template-spec.md` | Spec | an authoritative standard (like the specs in `docs/specs/`) |
| `template-guide.md` | Guide | a living how-to (pipeline, dev workflow, contributing) |
| `template-library-index.md` | Library Index | a per-library hub — usually **generated** by `scripts/build_library_docs.py`; hand-edit only for prose overview |
| `template-adr.md` | ADR | an architecture decision record |
| `template-audit.md` | Audit | a dated, evidence-backed audit/QA record |

`Narrative` docs are free prose (still carry an identity block). `Generated` docs are owned by
a script and carry a banner, not a template.

*Last verified against the repo: 2026-08-06.*
