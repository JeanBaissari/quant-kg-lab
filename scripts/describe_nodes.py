#!/usr/bin/env python3
"""Assistant-loop node describer (token-free path).

The assistant (Claude Code, on the subscription) supplies descriptions — no API key.
  --list <lib> [N]         print the top-N high-value UNDESCRIBED public-API nodes as JSON
                           (id, name, label, source, neighbors) for the assistant to describe
  --apply <lib> <ans.json> merge {node_id: "one-sentence description"} into graph.json (with backup)
  --coverage [<lib>]        report described / describable public-API counts
  --auto <lib> --backend opencode   drive the whole loop: list -> opencode run -> apply
                           until coverage >= target (default 80%). Prompts from
                           scripts/description_prompts.json (QKG_003 design spec).
                           --batch N (default 200), --limit M (max batches), --target PCT,
                           --dry-run (print the first prompt, no LLM call)

Selection = public-API code nodes (noise-filtered per GRAPH_SPEC §6), ranked by degree, that
still carry an AST stub. ta-lib keeps its __pyx_pw_..._NAME() indicator wrappers (the ta-lib
exception) and reports the clean indicator name.
"""
import sys, json, re, shutil, subprocess, time, pathlib
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
    """Map a __pyx_pw_ wrapper back to its public API name.

    Wrapper shape: __pyx_pw_<mod>talib_<n>_ta_lib_<id><NAME>(), where NAME is one of:
      HT_PHASOR / LINEARREG_SLOPE / CDL*   indicator names (may contain underscores)
      stream_<NAME>                        the streaming API (talib.stream.<NAME>)
      Function_<n><name>                   methods of the abstract Function class
      bytes2str / str2bytes                legacy helpers
    """
    m = re.match(r"__pyx_pw_\d*talib_\d*_ta_lib_\d+(.+)\(\)$", label or "")
    if not m:
        return None
    name = m.group(1)
    if name.startswith("stream_"):
        return "stream." + name[len("stream_"):]
    if name.startswith("Function_"):
        return "Function." + re.sub(r"^\d+", "", name[len("Function_"):])
    return name

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


# ---------------------------------------------------------------- --auto loop

PROMPTS = ROOT / "scripts" / "description_prompts.json"


def load_prompts():
    if not PROMPTS.exists():
        sys.exit("ERROR: scripts/description_prompts.json missing (QKG_003)")
    return json.load(open(PROMPTS))


def batch_nodes(g, deg, lib, N):
    """Top-N still-stub public-API nodes, degree-ranked (same selection as --list)."""
    rows = []
    for n in g["nodes"]:
        name = public(n, lib)
        if not name or not is_stub(n.get("description")):
            continue
        rows.append((deg[n["id"]], n, name))
    rows.sort(key=lambda x: -x[0])
    return [{"id": n["id"], "name": name, "label": n.get("label", ""),
             "source": n.get("source_file", "") + ":" + str(n.get("source_location", "")),
             "neighbors": neighbors(g, n["id"])} for d, n, name in rows[:N]]


def build_prompt(cfg, lib, payload):
    lib_cfg = cfg["libraries"].get(lib)
    if not lib_cfg:
        sys.exit(f"ERROR: no prompt config for {lib} in {PROMPTS}")
    ex = "\n".join(f'  - {e["name"]}: "{e["desc"]}"' for e in lib_cfg["exemplars"])
    return (cfg["base_template"]
            .replace("<<LIBRARY>>", lib)
            .replace("<<EMPHASIS>>", lib_cfg["emphasis"])
            .replace("<<GLOSSARY>>", lib_cfg["glossary"])
            .replace("<<EXEMPLARS>>", ex)
            .replace("<<PAYLOAD>>", json.dumps(payload, ensure_ascii=False, indent=1)))


def run_opencode(prompt, timeout=600):
    exe = shutil.which("opencode")
    if not exe:
        sys.exit("ERROR: opencode not on PATH (QKG_003 backend)")
    t0 = time.time()
    p = subprocess.run([exe, "run", "--pure"], input=prompt, capture_output=True,
                       text=True, timeout=timeout)
    dt = time.time() - t0
    if p.returncode != 0:
        return None, dt, p.stderr[-500:]
    return p.stdout, dt, None


def extract_json(text):
    """Lenient {node_id: sentence} extraction: strip fences, first { to last }."""
    if not text:
        return None
    t = re.sub(r"```(?:json)?", "", text)
    i, j = t.find("{"), t.rfind("}")
    if i < 0 or j <= i:
        return None
    try:
        return json.loads(t[i:j + 1])
    except Exception:
        return None


def sentence_ok(v):
    return (isinstance(v, str) and v.strip() and "\n" not in v
            and 8 <= len(v.split()) <= 40 and not is_stub(v))


def log_run(lib, rec):
    p = gpath(lib).parent / "describe-log.jsonl"
    rec["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with open(p, "a") as f:
        f.write(json.dumps(rec) + "\n")


def cmd_auto(lib, batch, limit, target, dry_run, backend="opencode"):
    if backend != "opencode":
        sys.exit("ERROR: only --backend opencode is supported (QKG_003)")
    g, deg = load(lib)
    by_id = {n["id"]: n for n in g["nodes"]}
    cfg = load_prompts()
    batches = 0
    while True:
        pub = [n for n in g["nodes"] if public(n, lib)]
        done = sum(1 for n in pub if not is_stub(n.get("description")))
        pct = 100.0 * done / len(pub) if pub else 100.0
        if pct >= target:
            print(f"{lib}: coverage {pct:.1f}% >= {target}% — done")
            break
        payload = batch_nodes(g, deg, lib, batch)
        if not payload:
            print(f"{lib}: no describable nodes left ({pct:.1f}%)")
            break
        prompt = build_prompt(cfg, lib, payload)
        if dry_run:
            out = gpath(lib).parent / f"prompt-{lib}-{batches}.txt"
            out.write_text(prompt)
            print(f"dry-run: first prompt ({len(payload)} nodes) -> {out}")
            break
        batches += 1
        if limit and batches > limit:
            print(f"{lib}: hit --limit {limit} ({pct:.1f}%)")
            break
        print(f"{lib}: batch {batches} ({len(payload)} nodes) -> opencode ...", flush=True)
        stdout, dt, err = run_opencode(prompt)
        ans = extract_json(stdout) if stdout else None
        ok, rejected = 0, []
        if ans:
            for nid, desc in ans.items():
                n = by_id.get(nid)
                if n and sentence_ok(desc):
                    n["description"] = desc.strip()
                    ok += 1
                else:
                    rejected.append(nid)
        if ok:
            shutil.copy(gpath(lib), str(gpath(lib)) + ".predesc.bak")
            json.dump(g, open(gpath(lib), "w"))
        pct_after = 100.0 * (done + ok) / len(pub) if pub else 100.0
        log_run(lib, {"batch": batches, "nodes": len(payload), "applied": ok,
                      "rejected": len(rejected), "secs": round(dt, 1),
                      "coverage_pct": round(pct_after, 1), "error": err})
        print(f"  applied {ok}/{len(payload)} (rejected {len(rejected)}, {dt:.0f}s) -> "
              f"{pct_after:.1f}%", flush=True)
        if ok == 0:
            print(f"{lib}: no progress this batch — stopping (error: {(err or 'no JSON')[:200]})")
            break


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
    elif "--auto" in a:
        i = a.index("--auto"); lib = a[i+1]
        batch = int(a[a.index("--batch")+1]) if "--batch" in a else 200
        limit = int(a[a.index("--limit")+1]) if "--limit" in a else None
        target = int(a[a.index("--target")+1]) if "--target" in a else 80
        dry = "--dry-run" in a
        backend = a[a.index("--backend")+1] if "--backend" in a else "opencode"
        cmd_auto(lib, batch, limit, target, dry, backend)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
