#!/usr/bin/env python3
"""Inject curated nodes into a graph.json (QKG_021).

Some public API surfaces cannot be extracted from source: numpy.random's core
is Cython (`_generator.pyx` etc.) and tree-sitter has no Cython grammar, so the
extracted graph contains the C internals (`random/src/...`) but not the public
re-export symbols (`default_rng`, `Generator`, `SeedSequence`, ...).

This tool adds them as CURATED nodes pinned to the real re-export module
(`random/__init__.py` — truthful: that is where the public API is imported),
with real semantic descriptions, joined to the module node via a CURATED
'contains' link. It mirrors the `_cross_library` overlay precedent (curated
nodes without extractable source_file still resolve for citations).

Usage:
  python3 scripts/inject_curated_nodes.py <lib> [--dry-run|--apply]

The curated set per library lives in the CURATED dict below. Every node must
carry: label (graph convention: 'fn()' for functions, bare name for classes),
source_file (the re-export module), description (semantic, non-stub).
"""
import sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

CURATED = {
    "numpy": [
        {"label": "default_rng()",
         "source_file": "random/__init__.py",
         "description": "Create a new Generator seeded from a default BitGenerator "
                        "(PCG64) or from explicit entropy; the modern RNG entry point "
                        "for reproducible streams."},
        {"label": "Generator",
         "source_file": "random/__init__.py",
         "description": "Primary random-number generator class wrapping a BitGenerator; "
                        "hosts the distribution methods (random, normal, uniform, "
                        "integers, choice, permutation, ...)."},
        {"label": "PCG64()",
         "source_file": "random/__init__.py",
         "description": "Default BitGenerator: a counter-based PRNG with good "
                        "statistical quality and speed; supports seeding and jumping."},
        {"label": "SeedSequence()",
         "source_file": "random/__init__.py",
         "description": "Converts entropy into independent seed states for "
                        "BitGenerators, enabling parallel/independent RNG streams."},
        {"label": "random()",
         "source_file": "random/__init__.py",
         "description": "Generate uniform floats in [0, 1) from a Generator "
                        "(module-level legacy alias exists on RandomState)."},
        {"label": "normal()",
         "source_file": "random/__init__.py",
         "description": "Gaussian/normal samples with configurable loc, scale and "
                        "output shape."},
        {"label": "uniform()",
         "source_file": "random/__init__.py",
         "description": "Uniform floats in [low, high) with configurable output shape."},
        {"label": "integers()",
         "source_file": "random/__init__.py",
         "description": "Random integers in [low, high) — Generator method "
                        "(module-level numpy.random.integers was removed in "
                        "NumPy 2.0)."},
        {"label": "choice()",
         "source_file": "random/__init__.py",
         "description": "Random sample from a 1-D array, with optional probabilities "
                        "and replacement."},
        {"label": "permutation()",
         "source_file": "random/__init__.py",
         "description": "Randomly permute a sequence, or return a permuted range of "
                        "length n."},
    ],
}


def main():
    argv = sys.argv[1:]
    if len(argv) < 1:
        sys.exit(__doc__)
    lib = argv[0]
    apply = "--apply" in argv
    if lib not in CURATED:
        sys.exit(f"no curated set for {lib!r}; known: {sorted(CURATED)}")
    gpath = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not gpath.exists():
        sys.exit(f"missing graph: {gpath}")
    g = json.load(open(gpath))
    byid = {n["id"]: n for n in g["nodes"]}
    # module node of the re-export file → community for the curated nodes
    mods = [n for n in g["nodes"] if n.get("source_file") == "random/__init__.py"]
    if not mods:
        sys.exit("re-export module node not found in graph")
    mod = mods[0]
    community = mod.get("community")
    cname = mod.get("community_name")
    added, skipped = [], []
    for entry in CURATED[lib]:
        nid = "curated_" + entry["label"].split("(")[0].lower()
        if nid in byid:
            skipped.append(nid)
            continue
        node = {
            "id": nid,
            "label": entry["label"],
            "file_type": "code",
            "source_file": entry["source_file"],
            "community": community,
            "community_name": cname,
            "description": entry["description"],
        }
        added.append(node)
        byid[nid] = node
    links = list(g.get("links", []))
    added_links = 0
    existing = {(l["source"], l["target"]) for l in links}
    for node in added:
        if (mod["id"], node["id"]) in existing:
            continue
        links.append({
            "source": mod["id"], "target": node["id"],
            "relation": "contains", "confidence": "CURATED",
            "source_file": "random/__init__.py", "weight": 1,
            "_src": mod["id"], "_tgt": node["id"], "confidence_score": 1,
        })
        added_links += 1
    print(f"{lib}: {len(added)} curated nodes to add, {len(skipped)} already present, "
          f"{added_links} contains links")
    if not apply:
        print("dry-run: no changes written (use --apply)")
        return
    g["nodes"] = list(byid.values())
    g["links"] = links
    bak = gpath.with_name("graph.json.curated.bak")
    bak.write_text(json.dumps(json.load(open(gpath)), indent=1))  # pre-change copy
    gpath.write_text(json.dumps(g, indent=1))
    print(f"applied: {gpath} (backup {bak.name})")


if __name__ == "__main__":
    main()
