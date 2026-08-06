# SKILL_SPEC — The One Skill Template

> Authoritative spec for every `SKILL.md` under `skills/`. Phase 2 normalizes all skills to
> this. CI (`scripts/validate_skills.py`) lints against it. There is exactly **one** template
> and **one** frontmatter schema — the three historical "generations" are retired.

## 1. Layout & naming (library-first)

```
skills/<library>/SKILL.md               # router (required when a library has ≥2 sub-skills)
skills/<library>/<module>/SKILL.md      # one atomic skill per library submodule
skills/quant-patterns/<name>/SKILL.md   # cross-library workflow playbooks (see §7)
```

- **Directory** `<module>` uses the library's native module casing (`feature_selection`,
  `gaussian_process`). `<library>` is the import-facing name (`scikit-learn`, `ta-lib`).
- **Frontmatter `name`** is kebab-case, lowercase, underscores → hyphens:
  `scikit-learn-feature-selection`, `numpy-linalg`, `xgboost-sklearn`.
- **Router `name`** is the **bare library name** (`optuna`, `scikit-learn`) and MUST be unique —
  it must never collide with a sub-skill name. *(This is the bug in the current
  `skills/scikit-learn/SKILL.md`, which is a duplicate of `model_selection`.)*
- **Playbooks** use a `quant-` prefix: `quant-full-pipeline`, `quant-factor-research`.
- `name` MUST be **globally unique** across the repo.

## 2. Frontmatter schema (single schema — required unless marked optional)

```yaml
---
name: <library>-<module>                 # unique, kebab-case
description: Use when <trigger>. <one sentence, what it covers>.
version: 0.2.0                           # bump to 0.2.0 = normalized generation
author: quant-kg-lab                     # optional (defaults to quant-kg-lab)
license: MIT
source_repo: <org>/<repo>                # e.g. pandas-dev/pandas
source_commit: <40-char sha>            # pinned; MUST match /graphs.lock  (replaces "source_version: main")
extraction_date: 2026-07-29              # ISO date the graph was built
graph:                                   # provenance block (one shape for everyone)
  nodes: <int>
  edges: <int>
  community_count: <int>                 # distinct-community-ID definition, see GRAPH_SPEC §7
  graph_hash: <16-hex>                   # first 16 hex of sha256(graph.json); reproducible
tags: [<library>, <domain>, ...]         # optional
related_skills: [<name>, ...]            # optional; names must resolve to real skills
---
```

**Portability note.** Only `name` and `description` are consumed by skill loaders
(Claude Code, agentskills.io, Hermes). The rest is provenance/metadata that portable loaders
ignore safely — so a skill stays copy-in-able while carrying full traceability. Do **not**
reintroduce the old `metadata.hermes.*` nesting or the `graph_hash: <n>_nodes_<m>_edges`
pseudo-string — both are retired.

**`description` rule.** Must start with `Use when` and read as a trigger ("Use when working with
scipy statistical tests, distribution fitting, or resampling…"). This is what makes an agent load
the right skill. Noun-phrase blurbs (the old scipy/ta-lib style) are non-conforming.

## 3. Body: canonical section order

Sections appear in this order. **Required**: Quick Reference, Common Patterns, Pitfalls,
Provenance. Others are included when they apply.

```markdown
# <Library> <Module> (`import path`)

<One paragraph: what this module is and when to reach for it in quant work.>

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `Class/func` | `source_file:line` | ... | ... |

## Architecture            <!-- optional; for structurally complex modules -->
<ASCII or prose structural overview.>

## Common Patterns          <!-- required; runnable, correct code -->
```python
...
```

## Pitfalls                 <!-- required; numbered, real failure modes -->
1. ...

## Cross-Library Bridges    <!-- when the module composes with other libs in the repo -->
| Source | Target | Relation | Description |
|--------|--------|----------|-------------|

## Verification Checklist   <!-- claims a machine can re-check -->
- [ ] `Class` imports from `library.module`
- [ ] `func(...)` returns ...

## Provenance               <!-- required; honest about extraction quality -->
- Knowledge graph: <lib>, <nodes> nodes, <edges> edges, <communities> communities
- God nodes: `A` (<deg>), `B` (<deg>) — public-API hubs only (see GRAPH_SPEC noise filter)
- Extraction: graphify @ commit <sha>, backend claude-cli, description coverage <X%>
```

## 4. Traceability requirement (feeds Phase-3 verification)

Every `Quick Reference` row SHOULD carry a **graph node reference** (`source_file:line` and/or
node `id`) that resolves in the corresponding `graph.json`. `scripts/validate_skills.py`'s
provenance check fails a skill whose cited nodes don't exist. This is the concrete meaning of
"verifiable skill": a claim you can trace to source, not a hallucination.

## 5. Progressive disclosure (no dangling links, ever)

`references/` and `scripts/` under a skill are **optional**:

- `references/api.md` — if present, it MUST be generated by `scripts/extract_skill_refs.py`
  from the graph. If it isn't generated, **omit the References section entirely**. Never link a
  file that doesn't exist. *(The current 22 sklearn/optuna skills violate this — they link
  `references/api.md` + `references/examples.md` that were never created.)*
- `scripts/validate.py` — optional runnable check for that specific skill.

CI treats any link to a non-existent `references/*` or `scripts/*` file as a lint failure.

## 6. Router pattern (multi-skill libraries)

Model: the current `skills/optuna/SKILL.md`. A router:
- has `name: <bare-library>` and a `description` that says "Load sub-skills for detail",
- lists every sub-skill in a table linking to `<module>/SKILL.md` with a one-line coverage note,
- carries the library-level `graph:` provenance block,
- does **not** duplicate a sub-skill's content (the sklearn router bug).

## 7. Playbooks (`skills/quant-patterns/`) — the composable-stack layer

Playbooks are cross-library **workflow recipes**, not API surfaces. They:
- use `name: quant-<name>` and a `Use when` description,
- have no `source_repo`/`source_commit`/`graph` block (they aren't extracted from one library);
  instead they carry `composes: [<skill-name>, ...]` listing the atomic skills they chain,
- follow: intro → `## Steps` (numbered, runnable) → `## Pitfalls` → `## Composed Skills & Bridges`.

## 8. Lint rules (enforced by `scripts/validate_skills.py --ci`)

1. Frontmatter has all required keys; `name` matches `^[a-z0-9-]+$` and is globally unique.
2. `description` starts with `Use when`.
3. `source_commit` matches `/graphs.lock` for that library.
4. Required sections present; headers drawn from the allowed set above.
5. No dangling `references/*` or `scripts/*` links.
6. Every library with ≥2 sub-skills has a router whose `name` is the bare library name.
7. Provenance check: cited graph nodes resolve in `graph.json` (§4).
8. API validation: claimed classes/functions exist in the installed library (§ validate_skills).

---

## 9. Copy-paste template

```markdown
---
name: <library>-<module>
description: Use when <trigger>. Covers <scope>.
version: 0.2.0
author: quant-kg-lab
license: MIT
source_repo: <org>/<repo>
source_commit: <sha-from-graphs.lock>
extraction_date: 2026-07-29
graph:
  nodes: <int>
  edges: <int>
  community_count: <int>
  graph_hash: <16-hex>
tags: [<library>, <domain>]
related_skills: []
---

# <Library> <Module> (`<import.path>`)

<one-paragraph intro>

## Quick Reference
| API | Graph Node | Purpose | Key Params |
|-----|-----------|---------|------------|
| `` | `` | | |

## Common Patterns
```python
```

## Pitfalls
1.

## Cross-Library Bridges
| Source | Target | Relation | Description |
|--------|--------|----------|-------------|

## Verification Checklist
- [ ]

## Provenance
- Knowledge graph: <lib>, <nodes> nodes, <edges> edges, <communities> communities
- God nodes:
- Extraction: graphify @ <sha>, backend claude-cli, description coverage <X%>
```
