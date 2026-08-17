# ADR-0007: Graph bundles as GitHub Release assets

**Type**: ADR
**ADR**: ADR-0007
**Status**: accepted
**Date**: 2026-08-12
**Last Verified**: 2026-08-12

## Context

The repo's value is the gold-standard knowledge base (28 graphs + 142 skills), but consuming it
today requires running the graphify pipeline or cloning the repo. The 2026-08-12 audit verified
the committed artifacts are free of personal data (repo-relative `source_file`, zero absolute
paths); distribution is therefore safe *if* the gitignored intermediates (`repo/`,
`.graphify/cache|wiki|memory`, `cost.json`) never enter a bundle. Several topologies exist:
commit zips in-tree, a `dist/` branch mirror, or GitHub Release assets.

## Decision

Ship versioned bundles as **GitHub Release assets**, tagged per `graphs.lock` commit
(`v<sha12>`), built by `scripts/export_bundle.py` and attached by a tag-triggered workflow that
first runs the quality gate.

- Bundle contents (exactly): per library `graph.json`, `GRAPH_REPORT.md`,
  `.graphify_labels.json`, plus the `_cross_library` overlay for `--all`; a `bundle.json`
  manifest with per-file sha256, lock commit, node/edge counts.
- The repo tree stays lean: no binaries committed, no history bloat.
- `export_bundle.py` asserts zero absolute paths and rejects any gitignored intermediate —
  the safety verdict becomes mechanical, not point-in-time (a CI safety check follows in
  QKG_015).
- Not chosen: in-tree zips (binary bloat + history growth per rebuild) and a `dist/` branch
  (second source of truth; revisit only if plain-URL consumers need it).

## Consequences

- One short string (`v<graphs.lock sha12>`) identifies a bundle and its reproducibility anchor.
- Consumers get graphs + skills without graphify/network: `unzip` → copy → validate
  (`validate_skills.py --ci` still works on a bundle's skills).
- Curated overlay nodes (QKG_021) ship inside the library bundle — they are part of
  `graph.json`, not a separate artifact.
- Release automation depends on GitHub Actions availability; manual `export_bundle.py` runs
  remain the fallback (same output, deterministic file-content verification).

## Alternatives considered

- In-tree `dist/*.zip` commits — rejected: repo bloat, non-diffable binaries, history grows
  with every rebuild.
- `dist/` branch mirror — deferred: release assets already give plain-URL downloads; add the
  mirror if scripted consumers need it.

## Addendum (2026-08-13, QKG_040) — skills tarball + semver tags

- Releases ship **qkg-skills.zip** (all library skills, copy-in layout) and
  **qkg-quant-patterns.zip** (playbooks) alongside the 28 graph bundles + overlay — the
  "consumers get graphs + skills without graphify" promise is now literal, under the same
  safety assertions (zero absolute paths) and deterministic file-content verification manifest contract.
- Tag scheme is **semver** (`v0.2.0`, …). The first release used a commit-hash tag
  (`v1eec0ffa2b6b`) before the semver convention; `bundle.json` keeps per-library
  `graphs.lock` commits as the reproducibility anchor, so tags stay human-readable while
  pins remain machine-verifiable.

*Last verified against the repo: 2026-08-13.*
