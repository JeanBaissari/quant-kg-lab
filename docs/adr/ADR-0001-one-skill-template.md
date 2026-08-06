# ADR-0001: One skill template + frontmatter schema

**Type**: ADR
**ADR**: ADR-0001
**Status**: accepted
**Date**: 2026-08-06
**Last Verified**: 2026-08-06

## Context

Skills had drifted into three inconsistent "generations" with three frontmatter schemas, a broken
scikit-learn router (name collision), and 22 skills linking `references/api.md`/`examples.md` files
that were never generated. Agents and CI could not rely on a stable shape.

## Decision

Adopt a **single** authoritative skill template and frontmatter schema — [`docs/specs/SKILL_SPEC.md`](../specs/SKILL_SPEC.md) —
enforced mechanically by `scripts/normalize_skills.py` and gated by `scripts/validate_skills.py --ci`.
Retire the `metadata.hermes.*` nesting and the `graph_hash: <n>_nodes_<m>_edges` pseudo-string.

## Consequences

- All 56 skills conform; routers carry the bare library name; no dangling `references/`.
- New skills copy one template; CI fails on schema drift.
- The `description` "Use when …" trigger convention is now uniform.

## Alternatives considered

- Keep multiple templates per skill kind — rejected: defeats machine-checkability.
- Hand-fix each skill — rejected: not reproducible; a normalizer is idempotent.

*Last verified against the repo: 2026-08-06.*
