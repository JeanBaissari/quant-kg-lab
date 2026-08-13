#!/usr/bin/env python3
"""Emit a shields.io-style status badge SVG from the report backbone (QKG_052).

Reads docs/reference/status.json (produced by scripts/build_site.py) and writes
_site/skill-validation.svg — a flat "quant-kg-lab | passing" / "failing" badge.

Stdlib-only, deterministic. Usage:
  python3 scripts/build_site.py        # writes status.json + status.html
  python3 scripts/emit_badge.py        # writes _site/skill-validation.svg
"""
import json
import pathlib
import xml.sax.saxutils as sax

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"


def _badge(label, value, color):
    """Two-segment flat badge (label | value), shields.io look-alike."""
    label_w = 8 + len(label) * 7
    value_w = 8 + len(value) * 7
    total = label_w + value_w
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img">
  <linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/></linearGradient>
  <clipPath id="r"><rect width="{total}" height="20" rx="3" fill="#fff"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{label_w}" height="20" fill="#555"/>
    <rect x="{label_w}" width="{value_w}" height="20" fill="{color}"/>
    <rect width="{total}" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,sans-serif" font-size="11">
    <text x="{label_w // 2}" y="15" fill="#010101" fill-opacity=".3">{sax.escape(label)}</text>
    <text x="{label_w // 2}" y="14">{sax.escape(label)}</text>
    <text x="{label_w + value_w // 2}" y="15" fill="#010101" fill-opacity=".3">{sax.escape(value)}</text>
    <text x="{label_w + value_w // 2}" y="14">{sax.escape(value)}</text>
  </g>
</svg>"""


def main():
    p = OUT / "status.json"
    if not p.exists():
        raise SystemExit("_site/status.json missing — run scripts/build_site.py first")
    status = json.load(open(p))
    all_pass = all(status.get(k) for k in ("gate", "citations", "validate", "doc_audit"))
    color = "4c1" if all_pass else "e05d44"
    value = "passing" if all_pass else "failing"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "skill-validation.svg").write_text(_badge("quant-kg-lab", value, color))
    print(f"wrote {OUT / 'skill-validation.svg'} ({value})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
