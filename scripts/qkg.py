#!/usr/bin/env python3
"""qkg — single entry point for quant-kg-lab skills."""
import argparse
import sys
import subprocess
import pathlib
import json
import os

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
SKILLS_DIR = ROOT / "skills"


def cmd_install(args):
    """Copy skill dirs to target path."""
    target = pathlib.Path(args.target).expanduser()
    lib = args.lib
    src = SKILLS_DIR / lib
    if not src.exists():
        print(f"ERROR: library '{lib}' not found in {SKILLS_DIR}")
        sys.exit(1)
    # Find all sub-dirs with SKILL.md
    modules = [d for d in src.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
    if not modules:
        # lib itself might be a skill dir
        if (src / "SKILL.md").exists():
            modules = [src]
    dest_base = target / f"quant-kg-{lib}"
    dest_base.mkdir(parents=True, exist_ok=True)
    for mod in modules:
        dest = dest_base / mod.name
        subprocess.run(["cp", "-r", str(mod), str(dest)], check=True)
        print(f"  installed: {lib}/{mod.name} → {dest}")
    print(f"Installed {len(modules)} skill(s) for {lib}")


def cmd_validate(args):
    """Validate skills against installed library."""
    cmd = [sys.executable, str(SCRIPTS / "validate_skills.py"), "--strict"]
    if args.lib:
        cmd.extend([args.lib])
    if args.scores:
        cmd.append("--scores")
    if args.ci:
        cmd.append("--ci")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


def cmd_search(args):
    """Search across all libraries."""
    cmd = [sys.executable, str(SCRIPTS / "query_graph.py"), "--all"] + args.query
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


def cmd_list(args):
    """List all libraries and skill counts."""
    lock = json.load(open(ROOT / "graphs.lock"))["libraries"]
    for lib in sorted(lock.keys()):
        src = SKILLS_DIR / lib
        if not src.exists():
            continue
        modules = [d for d in src.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
        status = lock[lib].get("upstream_status", "?")
        print(f"  {lib:25s} {len(modules):3d} skills  [{status}]")


def cmd_graph(args):
    """Query a single library's graph."""
    cmd = [sys.executable, str(SCRIPTS / "query_graph.py"), args.lib] + args.query
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(
        prog="qkg", description="quant-kg-lab skill manager"
    )
    sub = parser.add_subparsers(dest="command")

    p_install = sub.add_parser("install", help="Install skills for a library")
    p_install.add_argument("lib", help="Library name (e.g., scipy)")
    p_install.add_argument(
        "--target", default="~/.claude/skills", help="Target directory"
    )
    p_install.set_defaults(func=cmd_install)

    p_validate = sub.add_parser(
        "validate", help="Validate skills against installed libs"
    )
    p_validate.add_argument("lib", nargs="?", help="Specific library (default: all)")
    p_validate.add_argument(
        "--scores", action="store_true", help="Show quality scores"
    )
    p_validate.add_argument(
        "--ci", action="store_true", help="CI mode (exit 1 on errors)"
    )
    p_validate.set_defaults(func=cmd_validate)

    p_search = sub.add_parser("search", help="Search across all libraries")
    p_search.add_argument("query", nargs="+", help="Search query")
    p_search.set_defaults(func=cmd_search)

    p_list = sub.add_parser("list", help="List all libraries")
    p_list.set_defaults(func=cmd_list)

    p_graph = sub.add_parser("graph", help="Query a single library graph")
    p_graph.add_argument("lib", help="Library name")
    p_graph.add_argument("query", nargs="+", help="Search query")
    p_graph.set_defaults(func=cmd_graph)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
