# QUICKSTART — Consume the quant knowledge base in 2 minutes

**Type**: Guide
**Status**: current
**Last Verified**: 2026-08-13

quant-kg-lab is a gold-standard knowledge base: **19 library knowledge graphs** (~81K nodes /
~204K edges) distilled into **104 verifiable, copy-in agent skills** (13 routers, 79 module
skills, 12 cross-library playbooks) plus **47 curated cross-library bridges**. Every skill
claim traces to a graph node (`source_file:line`) and is validated against the live library
API in CI.

You do **not** need graphify, a clone of upstream repos, or a network to consume it. Three
paths, from lightest to fullest:

## Path 1 — Copy a skill in (30 seconds)

```bash
cp -r skills/scipy/stats ~/.claude/skills/scipy-stats
# or into any agentskills.io / Hermes-compatible skills directory
```

Only the `name` and `description` frontmatter are required by loaders; the provenance
metadata (graph hash, pinned commit, citations) is carried along and ignored safely by
loaders that don't use it. Browse what's available in the
[unified index](docs/reference/unified-index.md).

## Path 2 — Release bundles (graphs, from a release)

Every tag ships versioned bundles as GitHub Release assets (ADR-0007). Download from
**Releases → v0.2.0** (or later):

```bash
unzip qkg-scipy.zip && unzip qkg-cross-library-overlay.zip
#    → scipy/graph.json + scipy/GRAPH_REPORT.md + scipy/.graphify_labels.json
python3 scripts/query_graph.py scipy "kolmogorov smirnov"   # from a repo checkout
```

Bundles are byte-identical across builds and asserted free of absolute paths and
gitignored intermediates (`bundle.json` verifies every sha256).

## Path 3 — Fully offline: bundles + skills tarball (2 minutes)

Since **v0.2.0**, releases also ship the skills:

```bash
unzip qkg-skills.zip && unzip qkg-quant-patterns.zip
#    → skills/...  (copy-in layout, 92 library skills + 12 playbooks)
cp -r skills/scipy/stats ~/.claude/skills/scipy-stats
```

Everything you need is in the release assets — no repo clone required. Verify a bundle's
integrity:

```bash
python3 - <<'EOF'
import json, hashlib, zipfile
m = json.load(open("bundle.json"))
with zipfile.ZipFile("qkg-scipy.zip") as z:
    for art, sha in m["libraries"]["scipy"]["artifacts"].items():
        assert hashlib.sha256(z.read(art)).hexdigest() == sha
print("scipy bundle intact")
EOF
```

## What you get

| Layer | Contents |
|-------|----------|
| Graphs | 19 libraries pinned in `graphs.lock`, all passing the GRAPH_SPEC §5 quality gate (c1–c6) |
| Skills | 104 `SKILL.md` — 13 routers + 79 modules + 12 playbooks, 726 citations, 0 dangling |
| Bridges | 47 curated cross-library edges (overlay graph) |
| Playbooks | volatility modelling, factor tearsheets, portfolio optimization, explainability, HPO, walk-forward, and more |
| CI gates | provenance, quality-gate, citations, `--require-complete` 19/19, doc audit, artifact safety |

## Validating skills against your own environment

With a repo checkout and the target libraries installed (`pip install -r requirements.txt`,
TA-Lib needs the system C library first):

```bash
python3 scripts/validate_skills.py --ci <lib>   # lint + API claims
python3 scripts/verify_citations.py             # all citations resolve
```

## Building a bundle yourself

```bash
python3 scripts/export_bundle.py --lib all --out dist --tag local
python3 scripts/check_artifact_safety.py --include-dist
```

## Pitfalls

1. **TA-Lib validation** needs the system C library (`apt/brew install ta-lib`) before
   `pip install TA-Lib` — the skill lint still runs without it.
2. **Skills are copy-in, not a package** — no `pip install`; copy the directory.
3. **Bundles ≠ upstream source** — graphs are extracted at pinned commits; `repo/` clones
   are gitignored and never shipped.
4. **Tags identify reproducibility** — `bundle.json` records the per-library
   `graphs.lock` commit; a bundle tag string alone is the short anchor.

## Related

- [README](README.md) — the front door, thesis, and architecture
- [Unified index](docs/reference/unified-index.md) — A–Z map of the stack
- [Consume without rebuilding](README.md#consume-without-rebuilding) — README section
- [ADR-0007](docs/adr/ADR-0007-distribution-bundles.md) — the bundle contract

*Last verified against the repo: 2026-08-13.*
