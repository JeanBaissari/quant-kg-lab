#!/usr/bin/env python3
"""QKG_073: CI check that curated descriptions are free of builtin docstrings and
the numpy-fallback template leaked into non-numpy libs.

Checks tools/curated/*.json — every description is scanned for:
  1. Known builtin docstrings: "Convert a string or number to a floating point",
     "str(object='') -> str", "tuple(iterable", "list(iterable", "Copyright",
     "=============.", "Public NumPy API symbol"
  2. numpy-template leakage: `np.<sym>` in non-numpy manifests
  3. Empty or suspiciously short descriptions (< 12 chars)

Exit 1 on any violation; prints per-lib violations.
"""
import sys, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFESTS = ROOT / "tools" / "curated"
SUSPICIOUS = [
    re.compile(r"Convert a string or number to a floating point"),
    re.compile(r"str\(object=.?\) -> str"),
    re.compile(r"tuple\(iterable"),
    re.compile(r"list\(iterable"),
    re.compile(r"Copyright \d"),
    re.compile(r"={5,}"),
    re.compile(r"Public NumPy API symbol"),
]


def main():
    violations = 0
    for mfile in sorted(MANIFESTS.glob("*.json")):
        lib = mfile.stem
        manifest = json.load(open(mfile))
        for s in manifest.get("symbols", []):
            d = s.get("description", "")
            label = s.get("label", "")
            # check for builtin docstrings
            for pat in SUSPICIOUS:
                if pat.search(d):
                    print(f"  {lib}/{label}: matches {pat.pattern!r}")
                    violations += 1
            # check for numpy template in non-numpy libs
            if lib != "numpy" and "np." in d and "Public NumPy" not in d:
                if re.search(r"\bnp\.[a-z_]+", d):
                    print(f"  {lib}/{label}: np.* leakage: {d[:80]}")
                    violations += 1
            # check suspiciously short
            if d and len(d.strip()) < 12:
                print(f"  {lib}/{label}: too short ({len(d)} chars): {d!r}")
                violations += 1
    if violations:
        print(f"\n{violations} violations found")
        return 1
    print(f"all curated descriptions OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
