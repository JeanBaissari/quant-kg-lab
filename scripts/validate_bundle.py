#!/usr/bin/env python3
"""Consumer-side bundle verification — the ADR-0007 contract (QKG_053).

A release's dist/ directory must satisfy EVERY invariant below; the tool exits
1 with a clear message on the first violation. This replaces the inline CI
heredoc and is the documented consumer contract (QUICKSTART):

  1. bundle.json parses and is schema v1; every library entry exists.
  2. Every declared artifact exists inside its zip; per-file sha256 AND the
     zip_sha256 match the manifest byte-for-byte.
  3. Zips contain ONLY sanctioned arcnames (no extras, no absolute paths,
     no gitignored intermediates — the export_bundle safety contract).
  4. graph.json's built_from_commit == the manifest commit; node/edge counts
     in graph.json match the manifest.
  5. Every skill's frontmatter graph.graph_hash == sha256(graph.json bytes)[:16]
     of the bundled graph it cites.

Usage:
  python3 scripts/validate_bundle.py dist            # all zips in a release dir
  python3 scripts/validate_bundle.py dist qkg-scipy  # single library
"""
import json, sys, hashlib, pathlib, zipfile, re

SANCTIONED = ("graph.json", "GRAPH_REPORT.md", ".graphify_labels.json")
BAD_MARKERS = ("/home/", "/Users/", "\\Users\\", "C:\\", "/repo/", "node_modules/",
               "cost.json", ".prune.bak", ".labels.bak", "curated.bak",
               "describe-log.jsonl", "cache/", "wiki/", "memory/")
SKILL_RE = re.compile(r"^skills/.*/SKILL\.md$")


def fail(msg):
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def check_zip(path, artifacts, label):
    if not path.exists():
        fail(f"{label}: zip missing: {path}")
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        for arc, expected in artifacts.items():
            if arc not in names:
                fail(f"{label}: missing artifact {arc}")
            if sha256_bytes(z.read(arc)) != expected:
                fail(f"{label}: sha256 mismatch for {arc}")
        for arc in names:
            if arc in artifacts:
                continue
            if SKILL_RE.match(arc):
                continue
            fail(f"{label}: unexpected arcname {arc!r}")
        for arc in names:
            if any(b in arc for b in BAD_MARKERS):
                fail(f"{label}: banned marker in arcname {arc!r}")
    for arc in artifacts:
        if any(b in arc for b in BAD_MARKERS):
            fail(f"{label}: banned marker in artifact {arc!r}")
    if sha256_bytes(path.read_bytes()) != artifacts.get("__zip__", sha256_bytes(path.read_bytes())):
        pass  # zip_sha256 checked below with the manifest value


def lib_skills_count(manifest):
    n = 0
    for fam in ("skills", "quant-patterns"):
        e = manifest.get(fam)
        if e:
            n += e.get("skill_count", 0)
    return n


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    d = pathlib.Path(args[0])
    only = args[1] if len(args) > 1 else None
    mpath = d / "bundle.json"
    if not mpath.exists():
        fail(f"bundle.json missing in {d}")
    manifest = json.load(open(mpath))
    if manifest.get("schema") != "bundle.json v1":
        fail(f"unexpected schema: {manifest.get('schema')!r}")

    libs = [only] if only else list(manifest.get("libraries", {}))
    for lib in libs:
        entry = manifest["libraries"].get(lib)
        if not entry:
            fail(f"library {lib} not in manifest")
        zp = d / f"qkg-{lib}.zip"
        if not zp.exists():
            fail(f"{lib}: qkg-{lib}.zip missing")
        # 2: per-file sha256 + zip sha256 vs manifest
        check_zip(zp, entry["artifacts"], f"{lib}")
        if sha256_bytes(zp.read_bytes()) != entry.get("zip_sha256"):
            fail(f"{lib}: zip_sha256 mismatch")
        # 3: sanctioned arcnames (already enforced in check_zip via artifacts set)
        # 4: graph schema vs manifest commit + counts
        with zipfile.ZipFile(zp) as z:
            g = json.loads(z.read(f"{lib}/graph.json"))
        built = g.get("graph", {}).get("built_from_commit")
        if built != entry["commit"]:
            fail(f"{lib}: built_from_commit {built!r} != manifest commit {entry['commit']!r}")
        if len(g.get("nodes", [])) != entry["nodes"] or len(g.get("links", [])) != entry["edges"]:
            fail(f"{lib}: graph counts {len(g.get('nodes', []))}/{len(g.get('links', []))} "
                 f"!= manifest {entry['nodes']}/{entry['edges']}")
        # 5: skill graph_hash vs bundled graph
        gh = sha256_bytes(zipfile.ZipFile(zp).read(f"{lib}/graph.json"))[:16]
        skills = d / "qkg-skills.zip"
        if skills.exists():
            with zipfile.ZipFile(skills) as z:
                for n in z.namelist():
                    if not SKILL_RE.match(n):
                        continue
                    fm = z.read(n).decode("utf-8", "replace")
                    m = re.search(r"^graph_hash:\s*([0-9a-f]{16})", fm, re.M)
                    if m and m.group(1) != gh:
                        fail(f"{lib}: {n} graph_hash {m.group(1)} != bundled graph {gh}")
        print(f"OK  {lib}: {entry['nodes']} nodes / {entry['edges']} edges, zip verified")

    # skills/quant-patterns tarballs
    for fam in ("skills", "quant-patterns"):
        e = manifest.get(fam)
        if not e:
            continue
        zp = d / f"qkg-{fam}.zip"
        check_zip(zp, e["artifacts"], fam)
        if sha256_bytes(zp.read_bytes()) != e.get("zip_sha256"):
            fail(f"{fam}: zip_sha256 mismatch")
        print(f"OK  {fam}: {e.get('skill_count')} SKILL.md files, zip verified")
    sidx = d / "skills.json"
    if sidx.exists():
        idx = json.load(open(sidx))
        if idx.get("schema") != "skills.json v1":
            fail(f"skills.json: unexpected schema {idx.get('schema')!r}")
        if len(idx.get("skills", [])) != lib_skills_count(manifest):
            fail(f"skills.json: {len(idx.get('skills', []))} entries != "
                 f"{lib_skills_count(manifest)} tarball entries")
        print(f"OK  skills.json: {len(idx.get('skills', []))} indexed skills")
    else:
        print("skills.json absent (pre-QKG_059 release) — index check skipped")
    print("bundle verified: all invariants hold")


if __name__ == "__main__":
    main()
