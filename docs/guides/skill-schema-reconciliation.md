# SKILL_SPEC ↔ Hermes Skill Schema — Reconciliation

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-13

> QKG_059, decision D2 from the ecosystem surface map (QKG_058). This document
> reconciles the two skill-frontmatter schemas so quant-kg-lab skills can be loaded by
> the vault's Hermes skill system (and vice versa) without breaking either gate.

## The two schemas

| Field | quant-kg-lab (SKILL_SPEC §2) | Hermes vault (`system/SKILLS.md`) |
|---|---|---|
| identity | `name` (kebab, `<lib>-<module>`) | `name` + `skill_id` (SKILL-<name>) |
| trigger | `description` "Use when …" | `description` (≤60-char headline + tags) |
| type | — | `type` (procedure/lessons/tool/audit/orchestration/overview) |
| version | `version` | `version` |
| license | `license` | — |
| provenance | `source_repo`, `source_commit`, `extraction_date`, `graph:` block | — |
| composition | `related_skills`, `composes` (playbooks) | — |

**Loaders** (Claude Code, agentskills.io, Hermes) consume only `name` + `description` —
the provenance block is safely ignored. BUT the vault's own inventory gate
(`system/scripts/skill-inventory.py`, REQUIRED_FIELDS incl. `skill_id`/`type`) would
REJECT a bare copy-in repo skill. That gate is a vault-authoring check, not a loader.

## The mapping (copy-in direction: repo → Hermes)

A repo skill placed in `~/.hermes/skills/<category>/<name>/SKILL.md` gains a small
**compatibility header** that satisfies the vault inventory without touching the repo
copy:

```yaml
# appended when placed in the Hermes tree (never committed in the repo)
skill_id: SKILL-<repo-name>
type: procedure           # default for library skills; orchestration for playbooks
```

Equivalently, a vault-side "foreign skill" allowance could exempt skills whose
`source_repo`/`graph` provenance marks them as knowledge-base skills. **Decision (D2a):
adopt the compatibility-header approach** — the repo stays clean, the vault gate passes,
and the mapping is one documented, deterministic step.

## Category placement

Vault rule (vault-map.md): a new category needs ≥3 skills or an explicit sponsor
decision. The 25 library skills + 12 playbooks clear it trivially. Proposed mapping:

| Hermes category | Repo content |
|---|---|
| `quant-dev` (existing) | 12 `quant-patterns` playbooks (they ARE quant workflows) |
| `quant-libs` (new, sponsor decision) | 115 library/module skills by domain |

`projects.conf` gains `quant-kg-lab: quant-dev quant-libs` → `sync-skills.sh` symlinks
them per the cross-repo-skill-sync convention (vault canonical, repos symlink).

## What this PRD does NOT do

- **No converter script ships in the repo** — the header is a 4-line addition; a
  converter adds maintenance surface for zero benefit until a consumer needs bulk
  onboarding (add then, in the vault's tooling, not here).
- **No change to SKILL_SPEC** — the repo's frontmatter stays as-is; the mapping is
  vault-side.
- **No be-quant wiring** — that's D3 (their PRD book, BQ_098-style), which consumes the
  playbooks' `composes` chains directly.

## Consumers

1. `skills.json` (QKG_059) — the machine-readable index, already emitted per release:
   `name`, `description`, `library`, `module`, `type`, `source_commit`, `graph_hash`,
   `sha256`. Loaders and the Hermes inventory can consume it without parsing SKILL.md.
2. `qkg-skills.zip` / `qkg-quant-patterns.zip` — the copy-in payload.
3. `status.json` / badge (QKG_052) — the trust surface.

## Pitfalls

1. **Never mutate the repo copy** for loader compatibility — the compatibility header
   belongs to the Hermes tree only (or a symlink overlay).
2. **`type` choice**: library skills are `procedure`; playbooks are `orchestration` —
   the vault's five-type template set applies.
3. **Duplicate `name` space**: repo names (`numpy-core`) don't collide with vault skill
   names (`quant-pipeline`) — verify before any bulk sync.
4. **Gate drift**: if SKILL_SPEC adds a required field later, re-check this mapping
   (it's versioned in the vault ROADMAP §7, D2).

## Related

- `docs/specs/SKILL_SPEC.md` — the repo's authoritative skill schema
- Vault: `system/SKILLS.md`, `system/skills/cross-repo-skill-sync/SKILL.md`,
  `system/vault-map.md`
- `prd/00-foundation/QKG_058_ecosystem_surface_map.md` — decisions D1–D6

*Last verified against the repo: 2026-08-13.*
