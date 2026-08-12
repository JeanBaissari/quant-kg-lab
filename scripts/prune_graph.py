#!/usr/bin/env python3
"""Post-filter graph prune per GRAPH_SPEC §6 (noise-filter policy).

Drops nodes whose source path matches the §6 exclude-by-path list or whose symbol
matches the §6 exclude-by-symbol list, then cascades their links. Preserves community
IDs of remaining nodes (no renumbering) so the label pass stays valid.

  --dry-run (default)   report what would be removed, write nothing
  --apply               back up to graph.json.prune.bak, then rewrite graph.json

ta-lib exception (§6): __pyx_pw_* indicator wrappers are the public API — kept.
Only __Pyx_*/traceback trace symbols are pruned there.
"""
import sys, json, re, shutil, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent

PATH_PATTERNS = (
    "tests/", "/test", "test_", "*_test.py", "conftest", "asv_bench", "benchmarks/",
    "bench/", "bench_", "examples/", "samples/", "r-package", "apps/", "/doc/", "docs/",
    ".github", "setup.py", "versioneer", "_vendor/", "third_party/", "vendored/",
)
SYMBOL_PATTERNS = (r"^__Pyx_", r"^__pyx_(?!pw)", r"JNI", r"_safe_call", r"^TA_")

LIB_EXTRA_SYMBOLS = {
    "optuna": ("StorageTestCase",),
    "xgboost": ("IteratorForTest",),
    "backtrader": (),
    "scipy": (),
}


def gpath(lib):
    return ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"


def match_path(sf):
    sf = (sf or "").lower()
    return any(p in sf for p in PATH_PATTERNS)


def match_symbol(label, lib):
    if lib == "ta-lib" and label.startswith("__pyx_pw_"):
        return False
    if any(re.search(p, label or "") for p in SYMBOL_PATTERNS):
        return True
    return any(s in (label or "") for s in LIB_EXTRA_SYMBOLS.get(lib, ()))


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    lib = a[0]
    apply = "--apply" in a
    p = gpath(lib)
    if not p.exists():
        print(f"ERROR: no graph at {p}", file=sys.stderr)
        return 1
    g = json.load(open(p))
    nodes = g["nodes"]
    links = g["links"]

    drop_path, drop_sym = set(), set()
    for i, n in enumerate(nodes):
        if match_path(n.get("source_file")):
            drop_path.add(i)
        elif match_symbol(n.get("label"), lib):
            drop_sym.add(i)
    drop = drop_path | drop_sym
    drop_ids = {nodes[i]["id"] for i in drop}

    removed = len(drop)
    kept = len(nodes) - removed
    n_links = sum(1 for l in links if l["source"] in drop_ids or l["target"] in drop_ids)
    print(f"{lib}: nodes {len(nodes)} -> {kept}  (removing {removed})")
    print(f"{lib}: links {len(links)} -> {len(links) - n_links}  (removing {n_links})")
    by_path = collections.Counter(nodes[i].get("source_file", "?") for i in drop_path)
    print("by-path top:", dict(by_path.most_common(5)))
    by_sym = collections.Counter(nodes[i].get("label", "?") for i in drop_sym)
    print("by-symbol top:", dict(by_sym.most_common(5)))

    if not apply:
        print("dry-run; re-run with --apply to write")
        return 0

    shutil.copy(p, str(p) + ".prune.bak")
    g["nodes"] = [n for i, n in enumerate(nodes) if i not in drop]
    g["links"] = [l for l in links
                  if l["source"] not in drop_ids and l["target"] not in drop_ids]
    live = {n.get("community") for n in g["nodes"]}
    g.setdefault("graph", {}).setdefault("community_labels", {})
    g["graph"]["community_labels"] = {
        k: v for k, v in g["graph"]["community_labels"].items() if int(k) in live
    }
    json.dump(g, open(p, "w"))
    print(f"wrote {p} (backup: {p}.prune.bak)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
