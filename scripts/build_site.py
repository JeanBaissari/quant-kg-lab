#!/usr/bin/env python3
"""Build a small static site for GitHub Pages (QKG_041).

Renders a curated set of markdown sources into a single-page HTML site under
_site/: the unified index (docs/reference/unified-index.md), the QUICKSTART,
and the README. Stdlib-only, deterministic, no Jekyll/gem dependencies.

The renderer handles the subset of CommonMark these documents actually use:
headings, tables, fenced code blocks, lists, inline code, links, bold, and
blockquotes. Everything else is escaped and kept readable.

Usage:
  python3 scripts/build_site.py            # writes _site/index.html + siblings
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
SOURCES = [
    ("index.html", "quant-kg-lab — Unified Knowledge Index", "docs/reference/unified-index.md"),
    ("quickstart.html", "QUICKSTART — Consume the knowledge base", "QUICKSTART.md"),
    ("readme.html", "quant-kg-lab — README", "README.md"),
]

CSS = """
:root { --fg:#1c1e21; --muted:#5f6672; --accent:#0a66c2; --bg:#ffffff; --code:#f3f4f6; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       color: var(--fg); margin: 0; line-height: 1.55; }
header { background: #101418; color: #fff; padding: 1.4rem 1.2rem; }
header a { color: #9cc3f2; margin-right: 1rem; text-decoration: none; font-size: .95rem; }
header a:hover { text-decoration: underline; }
main { max-width: 1000px; margin: 2rem auto; padding: 0 1.2rem; }
h1 { font-size: 1.6rem; border-bottom: 1px solid #e2e5ea; padding-bottom: .4rem; }
h2 { font-size: 1.25rem; margin-top: 2rem; }
h3 { font-size: 1.05rem; }
a { color: var(--accent); }
code { font-family: ui-monospace, "SF Mono", Consolas, monospace; font-size: .88em;
       background: var(--code); padding: .1em .3em; border-radius: 4px; }
pre { background: var(--code); padding: .9rem 1rem; border-radius: 8px; overflow-x: auto; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 1rem 0; width: 100%; display: block; overflow-x: auto; }
th, td { border: 1px solid #d7dbe1; padding: .4rem .7rem; text-align: left; font-size: .92rem; }
th { background: #f3f5f7; }
blockquote { border-left: 4px solid #c9d2dc; margin: 1rem 0; padding: .2rem 1rem; color: var(--muted); }
ul, ol { padding-left: 1.6rem; }
footer { color: var(--muted); font-size: .85rem; text-align: center; padding: 2rem 0 3rem; }
"""


def inline(text):
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def render(md_text):
    """Render the CommonMark subset used by the curated sources."""
    lines = md_text.split("\n")
    out, i, n, in_code = [], 0, len(lines), False
    while i < n:
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            i += 1
            continue
        if in_code:
            out.append(html.escape(line))
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            if len(rows) > 1 and set(rows[1]) <= set("-: "):
                rows.pop(1)
            if rows:
                head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
                body = "".join(
                    "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                    for row in rows[1:]
                )
                out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("> "):
            out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        elif line.startswith("- "):
            out.append(f"<li>{inline(line[2:])}</li>")
        elif re.match(r"^\d+\. ", line):
            text = re.sub(r"^\d+\. ", "", line)   # f-string cannot contain '\' pre-3.12
            out.append(f"<li>{inline(text)}</li>")
        elif line.strip() == "":
            out.append("")
        else:
            out.append(f"<p>{inline(line)}</p>")
        i += 1
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def page(title, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <strong>quant-kg-lab</strong>
  <a href="index.html">Unified Index</a>
  <a href="quickstart.html">QUICKSTART</a>
  <a href="readme.html">README</a>
</header>
<main>
{body_html}
</main>
<footer>quant-kg-lab — generated from the repo's markdown sources · <a href="https://github.com/JeanBaissari/quant-kg-lab">source</a></footer>
</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, title, src in SOURCES:
        body = render((ROOT / src).read_text())
        (OUT / name).write_text(page(title, body))
        print(f"wrote {OUT / name}")
    _build_status(OUT)
    return 0


REF = ROOT / "docs" / "reference"
STATUS_SOURCES = ("skill-validation-report.json", "citations-report.json",
                  "quality-gate-summary.json", "cross-library-bridges.json",
                  "doc-audit-report.json")


def _load(name):
    p = REF / name
    return json.loads(p.read_text()) if p.exists() else None


def _build_status(out):
    """QKG_052: aggregate the report backbone into status.json + status.html."""
    val = _load("skill-validation-report.json")
    cit = _load("citations-report.json")
    gate = _load("quality-gate-summary.json")
    bridges = _load("cross-library-bridges.json")
    doc = _load("doc-audit-report.json")
    status = {
        "generated": max((d.get("generated", "") for d in (val, cit, gate) if d), default=""),
        "gate": bool(gate and gate.get("pass")),
        "citations": bool(cit and cit.get("pass")),
        "validate": bool(val and val.get("pass")),
        "doc_audit": bool(doc and not doc.get("errors") and not doc.get("census_errors")),
        "bridges": (bridges or {}).get("resolved"),
        "bridges_attempted": (bridges or {}).get("attempted"),
        "totals": (val or {}).get("totals", {}),
        "citations_counts": {"checked": (cit or {}).get("checked"),
                             "dangling": (cit or {}).get("dangling")},
        "libraries": [{"lib": l["lib"], "pass": l["pass"], "criteria": l["criteria"]}
                      for l in (gate or {}).get("libraries", [])],
    }
    (out / "status.json").write_text(json.dumps(status, indent=2) + "\n")

    rows = []
    for l in status["libraries"]:
        crit = " · ".join(f"{k}:{'✅' if v['pass'] else '❌'}" for k, v in l["criteria"].items())
        rows.append(f"<tr><td>{html.escape(l['lib'])}</td><td>{'✅' if l['pass'] else '❌'}</td>"
                    f"<td>{crit}</td></tr>")
    t = (val or {}).get("totals", {})
    body = f"""
<h1>Status</h1>
<p>Generated {html.escape(status['generated'])} · gate {'✅' if status['gate'] else '❌'} ·
citations {'✅' if status['citations'] else '❌'} · validate {'✅' if status['validate'] else '❌'} ·
doc-audit {'✅' if status['doc_audit'] else '❌'}</p>
<h2>Headline</h2>
<table><thead><tr><th>Metric</th><th>Value</th></tr></thead><tbody>
<tr><td>Skills lint / api-fail / api-warn</td><td>{t.get('lint', '–')} / {t.get('api_fail', '–')} / {t.get('api_warn', '–')}</td></tr>
<tr><td>Citations checked / dangling</td><td>{status['citations_counts']['checked']} / {status['citations_counts']['dangling']}</td></tr>
<tr><td>Bridges resolved</td><td>{status['bridges']} / {status['bridges_attempted']}</td></tr>
<tr><td>Docs / identity errors</td><td>{(doc or {}).get('totals', {}).get('docs', '–')} / {(doc or {}).get('totals', {}).get('identity', '–')}</td></tr>
</tbody></table>
<h2>Quality gate per library</h2>
<table><thead><tr><th>Library</th><th>Pass</th><th>Criteria</th></tr></thead><tbody>
{''.join(rows)}
</tbody></table>
"""
    (out / "status.html").write_text(page("Status — quant-kg-lab", body))
    print(f"wrote {out / 'status.json'} + {out / 'status.html'}")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
