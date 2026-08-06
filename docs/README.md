# docs/ — index & conventions

Three kinds of document live here. Keep them separate; don't let generated artifacts or
historical plans masquerade as living reference.

## Living reference (edit these; they define how the repo works)

| Doc | What it is |
|-----|-----------|
| [`SKILL_SPEC.md`](SKILL_SPEC.md) | The single skill template + frontmatter schema + lint rules. |
| [`GRAPH_SPEC.md`](GRAPH_SPEC.md) | Graph schema, noise-filter policy, and the graph quality gate. |
| [`methodology.md`](methodology.md) | The end-to-end reproducible pipeline (extract → query → author → validate). |
| [`BEFORE_AFTER.md`](BEFORE_AFTER.md) | The consolidation case study — what changed and why (the "stand out" story). |
| [`workflows.md`](workflows.md) | How to develop *with* these skills/agents — patterns & ideas. |

## Generated artifacts (do not hand-edit; regenerate with the named script)

| Artifact | Regenerate with |
|----------|-----------------|
| [`UNIFIED_INDEX.md`](UNIFIED_INDEX.md) | `scripts/build_unified_index.py` |
| `cross-library-bridges-v2.json` | `scripts/inject_cross_edges_v2.py` |
| `skill-validation-report.json` | `scripts/validate_skills.py` |
| `edge-audit-<lib>.md` | `scripts/audit_edges.py <lib>` |

## Archive (historical; superseded — see [`archive/README.md`](archive/README.md))

`archive/AUDIT.md`, `archive/PHASE2_PLAN.md`, `archive/PHASE4_SKILLS.md`.

## Naming convention

- `UPPER_SNAKE.md` = a durable spec or narrative (SKILL_SPEC, GRAPH_SPEC, BEFORE_AFTER).
- `lower-kebab.md` = a living how-to (methodology, workflows).
- `*.json` = a machine-generated artifact (never hand-edited).
- `edge-audit-<lib>.md` = per-library generated report.
