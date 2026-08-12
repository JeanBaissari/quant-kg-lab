#!/usr/bin/env python3
"""Generic community labeler v2 (GRAND_SPEC §5 criterion 1: no default "Community N").

For every community: centroid = highest-degree member, preferring a public-API node
(reuses describe_nodes.public()). Label = "<module path> · <symbol>" — e.g.
"pandas community 12 -> core.frame · DataFrame". Writes BOTH artifacts the spec
commits: knowledge_graphs/<lib>/.graphify/.graphify_labels.json and the
graph.community_labels map inside graph.json.

  --dry-run (default)   print the proposed map, write nothing
  --apply               back up both files, then write

Deterministic, stdlib-only. Replaces the deleted main-era label_communities.py.
"""
import sys, json, shutil, pathlib, collections
from describe_nodes import public, gpath


def module_path(n):
    sf = (n.get("source_file") or "").replace("\\", "/")
    parts = sf.split("/")
    if not parts or parts[-1] in ("__init__.py", "__init__.pyi"):
        return ".".join(parts[:-1]) if len(parts) > 1 else "root"
    return ".".join(parts[:-1]) if len(parts) > 1 else "root"


def display_name(label):
    return (label or "").removesuffix("()")


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    lib = a[0]
    apply = "--apply" in a
    g = json.load(open(gpath(lib)))

    deg = collections.Counter()
    for l in g.get("links", []):
        deg[l["source"]] += 1
        deg[l["target"]] += 1

    by_community = collections.defaultdict(list)
    for n in g["nodes"]:
        by_community[n.get("community")].append(n)

    # Label ONLY live communities (members present in the graph). Stale keys
    # whose members were pruned are dropped — never written as "empty".
    all_ids = set(by_community)
    labels = {}
    for cid in sorted(all_ids):
        ranked = sorted(members, key=lambda n: (-deg[n["id"]], n.get("id", "")))
        centroid = next((n for n in ranked if public(n, lib)), ranked[0])
        labels[str(cid)] = f"{module_path(centroid)} · {display_name(centroid.get('label'))}"

    n_real = sum(1 for v in labels.values() if not v.startswith("Community "))
    print(f"{lib}: {len(labels)} communities labeled; {n_real} real, "
          f"{len(labels) - n_real} default-style")

    if not apply:
        print("dry-run; re-run with --apply to write")
        return 0

    lp = gpath(lib).parent / ".graphify_labels.json"
    shutil.copy(lp, str(lp) + ".bak")
    shutil.copy(gpath(lib), str(gpath(lib)) + ".labels.bak")
    json.dump(labels, open(lp, "w"), indent=1)
    g.setdefault("graph", {})["community_labels"] = {k: v for k, v in labels.items()}
    json.dump(g, open(gpath(lib), "w"))
    print(f"wrote {lp} + graph.community_labels ({gpath(lib)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
