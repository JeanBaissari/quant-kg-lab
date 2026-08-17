# Developing with these skills & agents

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-17

Patterns and ideas for *using* quant-kg-lab in day-to-day quantitative work — planning sessions,
research, and PhD documentation. The skills are copy-in; the tooling around them is what turns a
pile of references into a working method.

## Loading skills into an agent

Copy the skill (or a whole library) into your agent's skills directory:

```bash
cp -r skills/scipy/stats   ~/.claude/skills/scipy-stats        # one atomic skill
cp -r skills/vectorbt      ~/.claude/skills/vectorbt           # router + all sub-skills
cp -r skills/quant-patterns ~/.claude/skills/quant-patterns    # the workflow playbooks
```

Only `name` + `description` are required by loaders; the provenance metadata rides along and is
ignored by agents that don't use it. **Progressive disclosure**: point the agent at a library's
router (`skills/<lib>/SKILL.md`); it loads the sub-skill for the module in play.

## Core loops

**Explore a library while planning.** Before writing code, interrogate the graph:
```bash
python scripts/query_graph.py scipy "kolmogorov"     # find the API + neighbors
python scripts/query_graph.py sklearn --explain "Pipeline"
python scripts/query_graph.py _cross_library "Portfolio"   # cross-library bridges
```

**Trust a skill before relying on it.** The validator is the trust surface:
```bash
python scripts/validate_skills.py scipy --provenance   # claims exist + trace to the graph
```

**Compose a research session with a playbook.** The 18 playbooks in `skills/quant-patterns/` chain atomic skills into cross-library workflows — e.g. `quant-full-pipeline` links pandas → ta-lib → features → model → vectorbt → optuna → risk. Each playbook pulls sub-skill API detail on demand.

## Patterns worth reusing

- **Router-first prompting.** Give the agent the router, not every sub-skill — it self-selects the
  module, keeping context small.
- **Provenance in review.** When an agent proposes an API call, the skill's graph citation lets you
  jump to `source_file:line` to confirm it. No more "does this method exist?".
- **Bridges as a design aid.** The `_cross_library` overlay answers "what connects X to Y?" — e.g.
  `ta-lib.RSI → vectorbt.SignalFactory` — which is exactly the seam where quant pipelines break.
- **HPO objective = OOS metric.** Playbooks that involve model training bake in walk-forward, purge/embargo, and risk-adjusted objectives — the leak-free defaults that hand-rolled notebooks usually miss.

## Ideas / backlog for building this out

- **PhD documentation**: auto-generate a per-library appendix (API surface + citations) from the
  graph via `extract_skill_refs.py`; drop it straight into a thesis appendix.
- **Paper reproducibility**: pin the exact library commit a result used via `graphs.lock`, so a
  reviewer can rebuild the same graph and skill set.
- **New-library onboarding**: `rebuild_graph.sh <newlib>` + `normalize_skills.py` gives a first-pass skill set for any library in the expansion backlog — see `ROADMAP.md` Phase 6).
- **Agent evals**: use `validate_skills.py` output as a regression gate — a skill that starts
  failing API validation flags upstream API drift before it reaches your strategies.
- **Studio / Obsidian export**: `graphify export obsidian` for an offline, navigable vault of the
  whole stack (ROADMAP Phase 6).
