# SKILL_SPEC ↔ Hermes Skill Schema — Reconciliation

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-17

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

**Verified against the vault's live mechanics (2026-08-13):**

1. **The compatibility header lives in the VAULT's canonical tree as a real file** —
   `.hermes/skills/<category>/<name>/SKILL.md` — NOT in `~/.hermes/skills` and NOT as a
   symlink overlay. The inventory scanner (`skill-inventory.py:23-26`) reads only the
   vault tree and its `rglob` does **not** follow directory symlinks; `sync-skills.sh`
   wipes and re-copies `~/.hermes/skills` on every sync. A symlinked skill would be
   **invisible to every gate and to propagation**.
2. The vault copy appends a small **compatibility header** that satisfies the inventory
   without touching the repo copy:

```yaml
# appended to the VAULT copy only (never committed in the repo)
skill_id: SKILL-<kebab-name>
type: procedure           # default for library skills; orchestration for playbooks
```

3. **The vault gate is broader than skill_id/type.** Verified against all 142 repo
   skills: 2 files exceed the vault's ≤300-line rule (`numpy/core` 410,
   `lightgbm/sklearn` 313) and 12 module dirs are snake_case (the vault requires
   kebab-case dir names — `factor_analysis`, `black_litterman`, `feature_selection`,
   `gaussian_process`, `neural_network`, `model_selection`, `linear_model`, `vector_ar`,
   `walk_forward`-style, etc.). The vault's pre-commit gate and the sync validation
   gate (which aborts the WHOLE vault's sync on any violation) enforce all of these.
   The landing therefore needs: rename the 12 snake_case dirs to kebab in the vault
   copy + split/shorten the 2 oversized files to ≤300 lines.
4. **The sync gate is a system-wide kill switch** (`sync-skills.sh:43-51`): one malformed
   skill aborts every subsequent sync. A sloppy landing degrades the entire estate.
5. **`projects.conf` format is a token line**: `$PROJECTS_ROOT/quant-kg-lab quant-dev quant-libs`
   (space-separated category allowlist; `grep -qw` exact match).
6. **quant-kg-lab must gitignore `.hermes/`** (be-quant-engine precedent, `.gitignore:10`)
   or machine-absolute symlinks would be committed.
7. **`skill_id` format is policed**: must be `SKILL-<kebab>`; the `SKILL-[name]`
   placeholder form is rejected.

Equivalently, a vault-side "foreign skill" allowance could exempt skills whose
`source_repo`/`graph` provenance marks them as knowledge-base skills. **Decision (D2a):
adopt the compatibility-header approach** — the repo stays clean, the vault gate passes,
and the mapping is one documented, deterministic step (the vault-copy landing checklist
below).

## Category placement

Vault rule (vault-map.md): a new category needs ≥3 skills or an explicit sponsor
decision. The 28 library skills + 18 playbooks clear it trivially. Proposed mapping:

| Hermes category | Repo content |
|---|---|
| `quant-dev` (existing) | 18 `quant-patterns` playbooks (they ARE quant workflows) |
| `quant-libs` (new, sponsor decision) | 124 library/module skills by domain |

`projects.conf` gains `$PROJECTS_ROOT/quant-kg-lab quant-dev quant-libs` → `sync-skills.sh`
creates one symlink per category dir in the project (whole-category granularity — you
cannot link a subset).

## Landing checklist (vault-side, verified 2026-08-13)

**Phase A — vault content (~1 day)**
1. Copy the 124 library skills + 18 playbooks into the vault as **real dirs**:
   `.hermes/skills/quant-libs/<lib>[-<module>]/SKILL.md` +
   `.hermes/skills/quant-dev/<playbook>/SKILL.md`.
2. Append the compatibility header to each vault copy (`skill_id: SKILL-<kebab>`,
   `type: procedure`/`orchestration`).
3. **Rename the 12 snake_case module dirs to kebab** in the vault copy (verified
   collision-free) and **split the 2 oversized files to ≤300 lines** (`numpy/core`,
   `lightgbm/sklearn`).
4. Record the `quant-libs` category + sponsor decision (vault-map.md ≥3-skills rule).
5. `skill-inventory.py` exit 0, then commit (pre-commit gate re-verifies).

**Phase B — wiring (~30 min)**
6. `projects.conf`: `$PROJECTS_ROOT/quant-kg-lab quant-dev quant-libs`.
7. quant-kg-lab: add `.hermes/` to `.gitignore`.
8. `sync-skills.sh --dry-run` → `sync-skills.sh` (manual; no cron).

**Phase C — verification (~15 min)**
9. Symlink read test per category; inventory exit 0; `system/SKILLS.md` shows
   `quant-libs` + `quant-dev` additions.

## What this PRD does NOT do

- **No converter script ships in the repo** — the header is a 4-line addition; a
  converter adds maintenance surface for zero benefit until a consumer needs bulk
  onboarding (add then, in the vault's tooling, not here).
- **No change to SKILL_SPEC** — the repo's frontmatter stays as-is; the mapping is
  vault-side.
- **No be-quant wiring** — that's D3 (their PRD book, **BQ_097** — the next free
  be-quant PRD ID, verified 2026-08-13), which consumes the playbooks' `composes`
  chains directly.

## Consumers

1. `skills.json` (QKG_059) — the machine-readable index, already emitted per release:
   `name`, `description`, `library`, `module`, `type`, `source_commit`, `graph_hash`,
   `sha256`. Loaders and the Hermes inventory can consume it without parsing SKILL.md.
2. `qkg-skills.zip` / `qkg-quant-patterns.zip` — the copy-in payload.
3. `status.json` / badge (QKG_052) — the trust surface.

## Pitfalls

1. **Never mutate the repo copy** for loader compatibility — the compatibility header
   belongs to the vault canonical copy only (real files; symlink overlays are invisible
   to the inventory, propagation, and pre-commit gates).
2. **`type` choice**: library skills are `procedure`; playbooks are `orchestration` —
   the vault's five-type template set applies.
3. **Duplicate `name` space**: repo names (`numpy-core`) don't collide with vault skill
   names (`quant-pipeline`) — verify before any bulk sync.
4. **Gate drift**: if SKILL_SPEC adds a required field later, re-check this mapping
   (it's versioned in the vault ROADMAP §7, D2).
5. **The sync gate is a whole-vault kill switch** — a single malformed vault skill
   aborts every future `sync-skills.sh`; land the vault copy gate-clean first.
6. **Re-sync maintenance**: each new extraction wave must re-apply the header + kebab
   rename steps to the vault copies — recorded as a D2 maintenance note in the vault
   ROADMAP.

## Related

- `docs/specs/SKILL_SPEC.md` — the repo's authoritative skill schema
- Vault: `system/SKILLS.md`, `system/skills/cross-repo-skill-sync/SKILL.md`,
  `system/vault-map.md`
- `prd/00-foundation/QKG_058_ecosystem_surface_map.md` — decisions D1–D6

*Last verified against the repo: 2026-08-17.*
