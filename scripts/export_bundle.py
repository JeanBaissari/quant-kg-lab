#!/usr/bin/env python3
"""Export versioned knowledge-base bundles (ADR-0007, QKG_014, QKG_040).

Bundles are the distribution artifact of the gold-standard knowledge base: a
consumer unzips one per library (or `all`) and gets the same committed artifacts
the repo ships — no graphify, no network, no rebuild.

Bundle contents (exactly the sanctioned artifacts):
  graph.json · GRAPH_REPORT.md · .graphify_labels.json
  (+ knowledge_graphs/_cross_library overlay when exporting `all`)
  (+ qkg-skills.zip / qkg-quant-patterns.zip skills tarballs, QKG_040)

Safety invariants (asserted, not assumed — ADR-0007 / QKG_015):
  - no absolute paths (/home/, /Users/, drive letters) anywhere in a bundle;
  - no gitignored intermediates (repo/, cache/, wiki/, memory/, cost.json,
    *.bak, describe-log, prompt-*, node_modules/);
  - bundle.json manifest: per-file sha256, lock commit, node/edge counts.

Usage:
  python3 scripts/export_bundle.py --lib all --out dist
  python3 scripts/export_bundle.py --lib scipy --out dist --tag v9828540707ab
  python3 scripts/export_bundle.py --lib all --out dist --tag v0.2.0
"""
import sys, os, json, zipfile, hashlib, pathlib, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SANCTIONED = ("graph.json", "GRAPH_REPORT.md", ".graphify_labels.json")


def main():
    args = sys.argv[1:]
    libs = "all"
    out = "dist"
    tag = None
    i = 0
    while i < len(args):
        if args[i] == "--lib":
            libs = args[i + 1]; i += 2
        elif args[i] == "--out":
            out = args[i + 1]; i += 2
        elif args[i] == "--tag":
            tag = args[i + 1]; i += 2
        else:
            sys.exit(f"unknown arg: {args[i]}\n{__doc__}")
    lock = json.load(open(ROOT / "graphs.lock"))
    lib_names = list(lock["libraries"]) if libs == "all" else [libs]
    missing = [l for l in lib_names if l not in lock["libraries"]]
    if missing:
        sys.exit(f"unknown libraries: {missing}")
    outdir = ROOT / out
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = {"schema": "bundle.json v1", "tag": tag}
    for lib in lib_names:
        gdir = ROOT / "knowledge_graphs" / lib / ".graphify"
        files = [gdir / a for a in SANCTIONED]
        missing_files = [f for f in files if not f.exists()]
        if missing_files:
            sys.exit(f"{lib}: missing sanctioned artifacts: {[f.name for f in missing_files]}")
        _assert_safe(files, lib)
        node_counts = _counts(lib, lock)
        zip_path = outdir / f"qkg-{lib}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in files:
                z.write(f, arcname=f"{lib}/{f.name}")
        entry = {"commit": lock["libraries"][lib]["commit"],
                 "nodes": node_counts[0], "edges": node_counts[1],
                 "artifacts": {f"{lib}/{f.name}": _sha256(f) for f in files},
                 "zip_sha256": _sha256(zip_path)}
        manifest.setdefault("libraries", {})[lib] = entry
        print(f"{lib}: {zip_path.relative_to(ROOT)}  ({entry['nodes']} nodes, {entry['edges']} edges)")
    if libs == "all":
        overlay = ROOT / "knowledge_graphs" / "_cross_library" / ".graphify" / "graph.json"
        if overlay.exists():
            _assert_safe([overlay], "_cross_library")
            zpath = outdir / "qkg-cross-library-overlay.zip"
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
                z.write(overlay, arcname="_cross_library/graph.json")
            manifest["cross_library_overlay"] = {"zip_sha256": _sha256(zpath),
                                                 "artifacts": {"_cross_library/graph.json": _sha256(overlay)}}
            print(f"cross-library overlay: {zpath.relative_to(ROOT)}")
    mpath = outdir / "bundle.json"
    mpath.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"manifest: {mpath.relative_to(ROOT)}")
    if libs == "all":
        _export_skills(outdir, tag, manifest)
    mpath.write_text(json.dumps(manifest, indent=2) + "\n")


SKILL_FILES = ("SKILL.md",)


def _export_skills(outdir, tag, manifest):
    """Skills tarballs (QKG_040): qkg-skills.zip (all library skills, copy-in layout)
    + qkg-quant-patterns.zip (playbooks). Same safety + manifest contract as graphs.
    QKG_059: also emits skills.json — the machine-readable skill index (name,
    description, library, module, type, source_commit, graph_hash) for loaders
    (agentskills.io / Hermes / be-quant registries)."""
    lib_skills = sorted((ROOT / "skills").rglob("SKILL.md"))
    playbooks = [p for p in lib_skills if p.relative_to(ROOT / "skills").parts[0] == "quant-patterns"]
    library_skills = [p for p in lib_skills if p not in playbooks]
    index = []
    for name, files in (("skills", library_skills), ("quant-patterns", playbooks)):
        if not files:
            continue
        zip_path = outdir / f"qkg-{name}.zip"
        _assert_safe(files, name)
        arts = {}
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in files:
                arc = str(f.relative_to(ROOT / "skills"))
                z.write(f, arcname=arc)
                arts[arc] = _sha256(f)
                parts = f.relative_to(ROOT / "skills").parts
                fm = _frontmatter(f)
                index.append({
                    "path": arc,
                    "name": fm.get("name", ""),
                    "description": fm.get("description", ""),
                    "library": parts[0],
                    "module": parts[1] if len(parts) > 2 else "router",
                    "type": "playbook" if parts[0] == "quant-patterns" else "skill",
                    "source_commit": fm.get("source_commit"),
                    "graph_hash": (fm.get("graph") or {}).get("graph_hash"),
                    "sha256": arts[arc],
                })
        manifest[name] = {"zip_sha256": _sha256(zip_path), "artifacts": arts,
                          "skill_count": len(files), "tag": tag}
        print(f"{name}: {zip_path.relative_to(ROOT)}  ({len(files)} SKILL.md files)")
    index.sort(key=lambda e: e["path"])
    (outdir / "skills.json").write_text(
        json.dumps({"schema": "skills.json v1", "tag": tag, "skills": index}, indent=2) + "\n")
    print(f"skills index: {outdir / 'skills.json'}  ({len(index)} entries)")


def _frontmatter(path):
    """Minimal YAML-subset frontmatter read (name/description/source_commit/graph
    block) — no yaml dependency needed for the index."""
    text = path.read_text(errors="replace")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm_lines = parts[1].split("\n")
    fm, graph, section = {}, {}, None
    for line in fm_lines:
        line = line.rstrip()
        if line.startswith("graph:"):
            section = "graph"
            continue
        if section == "graph":
            if line.startswith("  ") and ":" in line:
                k, _, v = line.strip().partition(":")
                graph[k.strip()] = v.strip().strip('"')
            elif line and not line.startswith(" "):
                section = None
        if section is None and line and not line.startswith((" ", "-")) and ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            if k in ("name", "description", "source_commit"):
                fm[k] = v.strip().strip('"')
    if graph:
        fm["graph"] = graph
    return fm


def _counts(lib, lock):
    g = json.load(open(ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"))
    return len(g.get("nodes", [])), len(g.get("links", []))


def _assert_safe(files, lib):
    for f in files:
        text = f.read_text(errors="replace")
        for bad in ("/home/", "/Users/", "\\Users\\", "C:\\", "baissarienterprises"):
            if bad in text:
                sys.exit(f"{lib}: ABSOLUTE-PATH VIOLATION in {f.name} ({bad!r}) — refusing to bundle")
        if f.name == "graph.json":
            for bad in ("/repo/", "node_modules/", "cost.json", ".prune.bak", ".labels.bak",
                        "graph.json.curated.bak", "describe-log.jsonl"):
                if bad in text:
                    sys.exit(f"{lib}: INTERMEDIATE-ARTIFACT VIOLATION in {f.name} ({bad!r}) — refusing to bundle")


def _sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    main()
