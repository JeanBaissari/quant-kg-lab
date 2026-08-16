#!/usr/bin/env python3
"""QKG_011/012 skill-content tooling (stdlib + PyYAML).

Subcommands (--dry-run default, --apply to write):
  headers        normalize section headers to SKILL_SPEC §3 canon:
                 "Quick Reference: …" -> "Quick Reference", "Common Pitfalls" -> "Pitfalls",
                 "Graph Provenance" -> "Provenance"
  provenance     insert/refresh "## Provenance" for every library skill (module-scoped
                 god nodes, graph counts, extraction line with backend + coverage)
  citations      resolve Quick Reference API rows against graph.json and fill the
                 Source File / Graph Node column (adds the column when absent);
                 unresolved rows are reported for manual review

Playbooks (skills/quant-patterns) are exempt from all three.
"""
import sys, json, re, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML required")

import describe_nodes

ALL_LIBS = ["numpy", "scipy", "pandas", "scikit-learn", "optuna", "vectorbt",
            "backtrader", "ta-lib", "xgboost", "lightgbm", "statsmodels"]
HEADER_FIXES = (
    (re.compile(r"^##+ Quick Reference(?:[:\s].*)?$", re.M), "## Quick Reference"),
    (re.compile(r"^##+ Common Pitfalls\s*$", re.M), "## Pitfalls"),
    (re.compile(r"^##+ Graph Provenance\s*$", re.M), "## Provenance"),
)


def skills_of(lib):
    return sorted((ROOT / "skills" / lib).rglob("SKILL.md"))


def is_playbook(p):
    return "quant-patterns" in p.parts


def graph_meta(lib):
    p = ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"
    if not p.exists():
        return None
    g = json.load(open(p))
    deg = collections.Counter()
    for l in g.get("links", []):
        deg[l["source"]] += 1
        deg[l["target"]] += 1
    return g, deg


def module_scope_nodes(g, module):
    """Nodes whose path belongs to the skill's module directory."""
    if not module:
        return None
    out = []
    for n in g["nodes"]:
        sf = (n.get("source_file") or "").replace("\\", "/")
        parts = [p for p in sf.split("/") if p]
        if module == "core" and len(parts) == 1:
            out.append(n)
        elif any(len(p) >= 2 and (p == module or p.startswith(module)) for p in parts):
            out.append(n)
    return out or None


def god_nodes(g, deg, nodes, k=3):
    ranked = sorted(nodes, key=lambda n: -deg[n["id"]])[:k]
    return ", ".join(f"`{n.get('label','?')}` ({deg[n['id']]})" for n in ranked)


def coverage(lib):
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        import describe_nodes
        g = json.load(open(ROOT / "knowledge_graphs" / lib / ".graphify" / "graph.json"))
        pub = [n for n in g["nodes"] if describe_nodes.public(n, lib)]
        done = sum(1 for n in pub if not describe_nodes.is_stub(n.get("description")))
        return 100.0 * done / len(pub) if pub else 0.0
    except Exception:
        return 0.0


def provenance_block(lib, module):
    meta = graph_meta(lib)
    if not meta:
        return None
    g, deg = meta
    nodes = module_scope_nodes(g, module) or g["nodes"]
    lock = json.load(open(ROOT / "graphs.lock"))["libraries"].get(lib, {})
    sha = lock.get("commit", "?")[:12]
    pct = coverage(lib)
    return (
        "## Provenance\n\n"
        f"- Knowledge graph: {lib}, {len(g['nodes'])} nodes, {len(g['links'])} edges, "
        f"{len({nd.get('community') for nd in g.get('nodes', []) if nd.get('community') is not None})} communities\n"  # GRAPH_SPEC §7 (QKG_068)
        f"- God nodes: {god_nodes(g, deg, nodes)} — public-API hubs only "
        f"(see GRAPH_SPEC noise filter)\n"
        f"- Extraction: graphify @ {sha}, backend opencode, description coverage {pct:.0f}%\n"
    )


def read_fm(text):
    fm = text.split("---", 2)
    if len(fm) < 3:
        return None, None
    try:
        return yaml.safe_load(fm[1]) or {}, fm
    except Exception:
        return None, None


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = a[0]
    apply = "--apply" in a
    libs = [x for x in a[1:] if not x.startswith("-")] or ALL_LIBS
    if cmd == "headers":
        changed = []
        for lib in libs:
            for p in skills_of(lib):
                if is_playbook(p):
                    continue
                t = p.read_text()
                t2 = t
                for rx, repl in HEADER_FIXES:
                    t2 = rx.sub(repl, t2)
                if t2 != t:
                    changed.append(p)
                    if apply:
                        p.write_text(t2)
        print(f"headers: {len(changed)} files to fix" if changed else "headers: clean")
        for p in changed:
            print("  ", p.relative_to(ROOT))
    elif cmd == "provenance":
        changed = []
        for lib in libs:
            for p in skills_of(lib):
                if is_playbook(p):
                    continue
                text = p.read_text()
                meta, fm = read_fm(text)
                if not meta:
                    continue
                name = meta.get("name", "")
                if name.startswith("quant-"):
                    continue
                module = p.parent.name if p.parent.name != lib else None
                block = provenance_block(lib, module)
                if not block:
                    continue
                if "\n## Provenance" in text:
                    # refresh: drop the old section, append the new one
                    head = re.split(r"\n## Provenance\b", text, maxsplit=1)[0].rstrip()
                    new = head + "\n\n" + block.strip() + "\n"
                else:
                    new = text.rstrip() + "\n\n" + block.strip() + "\n"
                if new != text:
                    changed.append((p, new))
                    if apply:
                        p.write_text(new)
        print(f"provenance: {len(changed)} skills to update" if changed else "provenance: clean")
        for p, _ in changed:
            print("  ", p.relative_to(ROOT))
    elif cmd == "citations":
        unresolved = []
        filled_total = 0
        file_changes = {}
        for lib in libs:
            g, deg = graph_meta(lib)
            if not g:
                continue
            by_label = collections.defaultdict(list)
            for n in g["nodes"]:
                lbl = (n.get("label") or "").removesuffix("()")
                by_label[lbl].append(n)
                if lib == "ta-lib":
                    nm = describe_nodes.talib_name(n.get("label"))
                    if nm:
                        by_label[nm].append(n)
            for p in skills_of(lib):
                if is_playbook(p):
                    continue
                lines = p.read_text().split("\n")
                in_qr, header, cit_col, changed = False, None, None, False
                header_idx = -1
                for i, line in enumerate(lines):
                    if line.startswith("## Quick Reference"):
                        in_qr, header, cit_col = True, None, None
                        continue
                    if not in_qr:
                        continue
                    if line.startswith("## "):
                        in_qr = False
                        continue
                    if not line.strip().startswith("|"):
                        continue
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if header is None:
                        header, header_idx = cells, i
                        cit_col = next((j for j, h in enumerate(header)
                                        if re.search(r"source|graph node", h, re.I)), None)
                        continue
                    if all(re.fullmatch(r"[-:]+", c) for c in cells):
                        continue  # separator row
                    api = cells[0].strip("`")
                    api_clean = api.split("(")[0].split(".")[-1].removesuffix("()")
                    if cit_col is not None and len(cells) > cit_col and cells[cit_col].strip():
                        continue  # already cited
                    hit = next((n for n in by_label.get(api_clean, [])), None)
                    if hit is None:
                        hit = next((n for n in by_label.get(api, [])), None)
                    if hit is None:
                        # id fallback: last "_"-segment of the node id == api name
                        hit = next((n for n in g["nodes"]
                                    if n["id"].split("_")[-1].lower() == api_clean.lower()),
                                   None)
                    if hit is None:
                        unresolved.append((p, api))
                        continue
                    cite = f"{hit.get('source_file','?')}:{hit.get('source_location','L1')}"
                    if cit_col is None:
                        header.append("Graph Node")
                        lines[header_idx] = "| " + " | ".join(header) + " |"
                        cells.append(cite)
                    else:
                        while len(cells) <= cit_col:
                            cells.append("")
                        cells[cit_col] = cite
                    lines[i] = "| " + " | ".join(cells) + " |"
                    changed = True
                    filled_total += 1
                if changed:
                    file_changes[p] = "\n".join(lines)
        print(f"citations: {filled_total} rows filled; {len(unresolved)} unresolved")
        for p, api in unresolved[:50]:
            print(f"  {str(p.relative_to(ROOT))}: {api}")
        for p, text in sorted(file_changes.items()):
            print("  fix:", p.relative_to(ROOT))
            if apply:
                p.write_text(text)
        if file_changes and not apply:
            print("dry-run; re-run with --apply to write")
    else:
        print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
