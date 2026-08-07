#!/usr/bin/env python3
"""Assistant-loop node describer (token-free path).

The assistant (Claude Code, on the subscription) supplies descriptions — no API key.
  --list <lib> [N]         print the top-N high-value UNDESCRIBED public-API nodes as JSON
                           (id, name, label, source, neighbors) for the assistant to describe
  --apply <lib> <ans.json> merge {node_id: "one-sentence description"} into graph.json (with backup)
  --coverage [<lib>]        report described / describable public-API counts

Selection = public-API code nodes (noise-filtered per GRAPH_SPEC §6), ranked by degree, that
still carry an AST stub. ta-lib keeps its __pyx_pw_..._NAME() indicator wrappers (the ta-lib
exception) and reports the clean indicator name.
"""
import sys, json, re, shutil, pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
NOISE = ("tests/", "/test", "test_", "asv_bench", "benchmarks/", "bench_", "examples/",
         "r-package", "apps/", "/doc/", "docs/", ".github", "conftest", "samples/")

def gpath(lib):
    return ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"

def is_stub(d):
    d = d or ""
    return (not d) or ("containing symbols such as" in d) or (" in the _" in d) \
        or re.match(r"^(The .+\(\) function|Python module|Member|Entity|An example|R source|Function |Class )", d) is not None

def talib_name(label):
    m = re.match(r"__pyx_pw_\d*talib_\d*_ta_lib_\d+([A-Z][A-Za-z0-9]*)\(\)$", label or "")
    return m.group(1) if m else None

def public(n, lib):
    sf = (n.get("source_file") or "").lower(); lbl = n.get("label") or ""
    if any(p in sf for p in NOISE) or n.get("file_type") not in (None, "code") or not lbl:
        return None
    if lib == "ta-lib":
        nm = talib_name(lbl)
        return nm                                   # only the public __pyx_pw_ indicator wrappers
    if " " in lbl or len(lbl) > 40 or lbl.startswith("_") or lbl.startswith("__pyx") or re.fullmatch(r"__\w+__", lbl):
        return None
    return lbl

def load(lib):
    g = json.load(open(gpath(lib)))
    deg = Counter()
    for l in g.get("links", []):
        deg[l["source"]] += 1; deg[l["target"]] += 1
    return g, deg

def neighbors(g, nid, k=5):
    out = []
    for l in g.get("links", []):
        if l["source"] == nid: out.append(l["target"])
        elif l["target"] == nid: out.append(l["source"])
        if len(out) >= 12: break
    labels = {n["id"]: n["label"] for n in g["nodes"]}
    return [labels.get(x, x) for x in out[:k]]

def cmd_list(lib, N):
    g, deg = load(lib)
    rows = []
    for n in g["nodes"]:
        name = public(n, lib)
        if not name or not is_stub(n.get("description")):
            continue
        rows.append((deg[n["id"]], n, name))
    rows.sort(key=lambda x: -x[0])
    out = [{"id": n["id"], "name": name, "label": n["label"],
            "source": n.get("source_file", "") + ":" + str(n.get("source_location", "")),
            "neighbors": neighbors(g, n["id"])} for d, n, name in rows[:N]]
    print(json.dumps(out, indent=1, ensure_ascii=False))
    sys.stderr.write(f"{lib}: {len(rows)} describable public-API nodes; listed top {len(out)}\n")

def cmd_apply(lib, ansfile):
    ans = json.load(open(ansfile))
    p = gpath(lib); g = json.load(open(p))
    shutil.copy(p, str(p) + ".predesc.bak")
    by_id = {n["id"]: n for n in g["nodes"]}
    n = 0
    for nid, desc in ans.items():
        if nid in by_id and desc:
            by_id[nid]["description"] = desc; n += 1
    json.dump(g, open(p, "w"))
    print(f"{lib}: merged {n} descriptions into {p}")

def cmd_coverage(libs):
    print(f"{'lib':13} {'described':>9} {'describable':>11} {'pct':>6}")
    for lib in libs:
        g, _ = load(lib)
        pub = [n for n in g["nodes"] if public(n, lib)]
        done = sum(1 for n in pub if not is_stub(n.get("description")))
        pct = (100*done/len(pub)) if pub else 0
        print(f"{lib:13} {done:9} {len(pub):11} {pct:5.0f}%")

def main():
    a = sys.argv[1:]
    ALL = ["numpy","scipy","pandas","scikit-learn","optuna","vectorbt","backtrader","ta-lib","xgboost","lightgbm"]
    if "--list" in a:
        i = a.index("--list"); lib = a[i+1]; N = int(a[i+2]) if len(a) > i+2 and a[i+2].isdigit() else 40
        cmd_list(lib, N)
    elif "--apply" in a:
        i = a.index("--apply"); cmd_apply(a[i+1], a[i+2])
    elif "--coverage" in a:
        i = a.index("--coverage"); libs = [a[i+1]] if len(a) > i+1 and not a[i+1].startswith("-") else ALL
        cmd_coverage(libs)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
