#!/usr/bin/env python3
"""CI safety gate for committed/bundled artifacts (QKG_015).

The 2026-08-12 audit proved the committed knowledge base is free of personal
data — but that was point-in-time. This gate makes it mechanical: any commit
that introduces an absolute path, a username, or a known gitignored
intermediate into the artifacts the repo ships fails CI.

Scanned roots (committed): knowledge_graphs/**, skills/**, docs/reference/**,
graphs.lock, README.md, ROADMAP.md.
With --include-dist: also dist/** (bundles produced by scripts/export_bundle.py).

Exits 1 on any hit. Designed to be cheap and deterministic (stdlib only).
"""
import sys, pathlib, re, json, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN_DIRS = ("knowledge_graphs", "skills", "docs/reference")
SCAN_FILES = ("graphs.lock", "README.md", "ROADMAP.md")
ABSOLUTE = ("/home/", "/Users/", "\\Users\\", "C:\\", "baissarienterprises")
INTERMEDIATE = ("/repo/", "node_modules/", "cost.json", ".prune.bak", ".labels.bak",
                ".curated.bak", "describe-log.jsonl", "prompt-", "/cache/", "/wiki/")


def scan():
    hits = []
    # tracked files only — gitignored intermediates (repo/, .graphify cache,
    # studio/, backups) are never shipped, so they are not scanned (QKG_018 F7)
    tracked = set()
    r = subprocess.run(["git", "-C", str(ROOT), "ls-files"],
                       capture_output=True, text=True)
    if r.returncode == 0:
        tracked = {str(ROOT / f) for f in r.stdout.split("\n") if f}
    for d in SCAN_DIRS:
        root = ROOT / d
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if (p.is_file() and p.suffix in (".json", ".md", ".py", ".yml", ".yaml")
                    and str(p) in tracked):
                _check(p, hits)
    for name in SCAN_FILES:
        p = ROOT / name
        if p.exists():
            _check(p, hits)
    if "--include-dist" in sys.argv:
        d = ROOT / "dist"
        if d.exists():
            for p in d.rglob("*"):
                if p.is_file():
                    _check(p, hits)
    return hits


def _check(p, hits):
    try:
        text = p.read_text(errors="replace")
    except OSError:
        return
    rel = p.relative_to(ROOT)
    for pat in ABSOLUTE:
        if pat in text:
            hits.append((str(rel), f"absolute path {pat!r}"))
    # intermediate markers only in graph artifacts (graph.json) and bundles,
    # and only against path-like fields — node descriptions/labels legitimately
    # mention e.g. https://en.wikipedia.org/wiki/... (cvxpy Gershgorin label)
    if p.suffix in (".json", ".zip"):
        if p.suffix == ".json" and p.name == "graph.json":
            try:
                g = json.loads(text)
                text = "\n".join(
                    str(n.get("source_file", "")) + "|" + str(n.get("id", ""))
                    for n in g.get("nodes", []))
            except Exception:
                pass
        for pat in INTERMEDIATE:
            if pat in text:
                hits.append((str(rel), f"intermediate marker {pat!r}"))


def main():
    hits = scan()
    if hits:
        print(f"artifact-safety: {len(hits)} violation(s)")
        for path, why in hits[:20]:
            print(f"  {path}: {why}")
        sys.exit(1)
    print("artifact-safety: clean")


if __name__ == "__main__":
    main()
