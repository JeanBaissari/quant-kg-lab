# CLAUDE.md — working conventions for quant-kg-lab

Quantitative knowledge-graph lab: extract knowledge graphs from scientific-Python libraries →
distill into **verifiable, copy-in agent skills**. Read `README.md` for the thesis and
`ROADMAP.md` for the current phase.

## The two specs are authoritative

- **Docs** MUST follow `docs/_development/standards.md` — closed doc-type taxonomy + identity block;
  `python scripts/doc_audit.py --ci` is the gate.
- **Skills** MUST follow `docs/specs/SKILL_SPEC.md` — one template, one frontmatter schema, one naming
  rule. Do not reintroduce the retired variants (`metadata.hermes.*`, `graph_hash: <n>_nodes_<m>_edges`,
  noun-phrase descriptions).
- **Graphs** MUST follow `docs/specs/GRAPH_SPEC.md` — schema, noise filter, quality gate. The definition
  of "described" is *semantic*, not AST stubs.

## Layout

```
knowledge_graphs/<lib>/.graphify/   graph.json + GRAPH_REPORT.md + .graphify_labels.json  (committed)
knowledge_graphs/<lib>/repo/        upstream source clone                                  (gitignored)
skills/<lib>/<module>/SKILL.md      atomic skill        skills/<lib>/SKILL.md = router
skills/quant-patterns/              cross-library workflow playbooks
scripts/                            rebuild / query / validate / audit / bridge tooling (stdlib + PyYAML)
docs/                               index.md hub → specs/ guides/ libraries/ reference/ adr/ audit/ narrative/ _development/
graphs.lock                         pinned upstream commit per library — the reproducibility anchor
```

## Common tasks

```bash
scripts/rebuild_graph.sh <lib>                 # rebuild one graph from its pinned commit
python scripts/query_graph.py <lib> "<query>"  # search + BFS over a graph
python scripts/validate_skills.py [<lib>|--ci] # check skill claims against live APIs
python scripts/audit_edges.py <lib>            # regenerate docs/reference/edge-audits/edge-audit-<lib>.md
python scripts/doc_audit.py [--ci|--write]     # lint docs against docs/_development/standards.md
```

## Environment reality (important)

- **graphify is external**: `npm install -g @sentropic/graphify`. Re-extraction needs the CLI,
  **network access** (to clone upstream), and the **claude-cli backend** (for real descriptions).
  It **cannot** run in a network-less sandbox — do the rebuild on a full machine.
- **Target libraries** (`requirements.txt`) are needed only to *validate* skills. `TA-Lib` needs
  the system C library first (`apt/brew install ta-lib`).
- Committed graph artifacts are only the 3 files above; all graphify intermediates + `repo/` are
  gitignored and reproducible — never commit them.

## Conventions & guardrails

- Skill `name` is globally unique, kebab-case, `<lib>-<module>`; router `name` is the bare library.
- `description` starts with **"Use when …"**.
- Every `Quick Reference` row should cite a graph node (`source_file:line`) that resolves in
  `graph.json` — this is what makes a skill *verifiable*.
- **Never** link a `references/*` file that doesn't exist. The `references/` convention was
  retired in the QKG_011/012 skill-content wave — citation truth lives in Quick Reference rows
  as `source_file:line` (verified by `scripts/verify_citations.py`), not in generated files.
- `source_commit` in skill frontmatter MUST match `graphs.lock`.
- Skills are **copy-in**, not a package — do not add packaging/publish config.

## Git

- Default branch `main`. Branch before committing; commit per phase so the before/after is legible.
- Co-author trailer and session link are set by the harness.
