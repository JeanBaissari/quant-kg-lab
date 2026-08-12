# ADR-0005: Single `docs/` surface + doc-type taxonomy

**Type**: ADR
**ADR**: ADR-0005
**Status**: accepted
**Date**: 2026-08-06
**Last Verified**: 2026-08-06

## Context

`docs/` was flat and inconsistent — no taxonomy, no templates, two partial indexes, orphaned
artifacts, stale dates. We wanted the scalable, modular system proven in a sibling lab's docs
surface, but without prematurely adopting a full mkdocs + `{@auto}` toolchain.

## Decision

Keep a **single `docs/` surface** (reference + narrative + generated + per-library), authored as
**structured markdown, mkdocs-ready** (folders `index.md`-homed). Govern it with a closed
doc-type taxonomy + identity block ([`docs/_development/standards.md`](../_development/standards.md)),
a closed template set, and a docs CI gate (`scripts/doc_audit.py`). No separate `wiki/`; the
graphify **studio HTML** is the browsable graph view.

## Consequences

- Every doc is machine-classifiable and link-checked; the casing signal is retired in favour of `Type`.
- A future mkdocs site mounts with zero reorg.
- ADRs and audits live inside `docs/` next to the reference material.

## Alternatives considered

- Two surfaces (`docs/` + Obsidian `wiki/`) like a sibling lab — rejected for now to reduce surface area.
- Full mkdocs + auto-gen toolchain — deferred; not needed to get consistency.

*Last verified against the repo: 2026-08-06.*
