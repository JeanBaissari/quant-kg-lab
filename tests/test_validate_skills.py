#!/usr/bin/env python3
"""Self-tests for scripts/validate_skills.py (QKG_007 — Validator v2).

Each planted violation in tests/fixtures/repo/ must fail `--ci`:

  (a) skills/numpy/core/SKILL.md      — missing `## Provenance` section (SKILL_SPEC §3)
  (b) skills/numpy/stalehash/SKILL.md — stale graph_hash (+ wrong nodes count, warn)
  (c) skills/numpy/dangling/SKILL.md  — related_skills: [no-such-skill] (unresolvable)
  (d) skills/numpy/badcommit/SKILL.md — source_commit does not match graphs.lock
  (e) skills/numpy/linalg/SKILL.md    — hallucinated func/class + cross-library class
                                        (module-scoped API universe; numpy is installed)

Exemptions: the router (skills/numpy/SKILL.md, §6) and the playbook
(skills/quant-patterns/bridge/SKILL.md, §7) must pass the section check.

Run: python3 -m unittest discover -s tests -v
"""
import contextlib
import hashlib
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import validate_skills as vs                      # noqa: E402

FIXTURE = pathlib.Path(__file__).resolve().parent / "fixtures" / "repo"
FIXTURE_HASH = hashlib.sha256(
    (FIXTURE / "knowledge_graphs" / "numpy" / ".graphify" / "graph.json").read_bytes()
).hexdigest()[:16]

REAL_ROOT, REAL_SKILLS, REAL_LOCK = vs.REPO_ROOT, vs.SKILLS, vs.LOCK
CORE_REL = "skills/numpy/core/SKILL.md"
STALEHASH_REL = "skills/numpy/stalehash/SKILL.md"
DANGLING_REL = "skills/numpy/dangling/SKILL.md"
BADCOMMIT_REL = "skills/numpy/badcommit/SKILL.md"
HALLUCINATED_REL = "skills/numpy/linalg/SKILL.md"
PARAMS_REL = "skills/numpy/params/SKILL.md"
ROUTER_REL = "skills/numpy/SKILL.md"
PLAYBOOK_REL = "skills/quant-patterns/bridge/SKILL.md"

try:
    import numpy  # noqa: F401
    NUMPY_INSTALLED = True
except ImportError:
    NUMPY_INSTALLED = False


class ValidatorTestCase(unittest.TestCase):
    """Runs the validator in-process against a temp copy of the fixture repo."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.root)
        vs.REPO_ROOT = self.root
        vs.SKILLS = self.root / "skills"
        with open(self.root / "graphs.lock") as f:
            vs.LOCK = json.load(f)["libraries"]
        for cache in (vs._SYMS, vs._SRC, vs._GINFO, vs._HASH):
            cache.clear()

    def tearDown(self):
        self.tmp.cleanup()
        vs.REPO_ROOT, vs.SKILLS, vs.LOCK = REAL_ROOT, REAL_SKILLS, REAL_LOCK
        for cache in (vs._SYMS, vs._SRC, vs._GINFO, vs._HASH):
            cache.clear()

    # ------------------------------------------------------------ helpers
    def run_main(self, *args):
        old_argv = sys.argv
        sys.argv = ["validate_skills.py", *args]
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                vs.main()
            code = 0
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 0
        finally:
            sys.argv = old_argv
        return code, out.getvalue()

    def load_report(self):
        with open(self.root / "docs" / "reference" / "skill-validation-report.json") as f:
            return json.load(f)

    def report_for(self, rel):
        return self.load_report()["report"][rel]

    def write_known_debt(self, violations):
        p = self.root / "tools"
        p.mkdir(exist_ok=True)
        (p / "known_debt.json").write_text(
            json.dumps({"generated": "2026-08-12", "violations": violations}, indent=2))

    def assert_lint_contains(self, rel, needle):
        lint = self.report_for(rel)["lint"]
        self.assertTrue(any(needle in m for m in lint), f"{needle!r} not in {lint}")


class TestSectionCheck(ValidatorTestCase):
    def test_missing_provenance_fails_ci(self):
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)
        lint = self.report_for(CORE_REL)["lint"]
        self.assertIn("missing required section: ## Provenance", lint)
        self.assertEqual(len(lint), 1, f"core fixture should violate only Provenance: {lint}")

    def test_router_exempt_from_sections(self):
        code, _ = self.run_main()
        self.assertEqual(code, 0)
        self.assertEqual(self.report_for(ROUTER_REL)["lint"], [])

    def test_playbook_exempt_from_sections(self):
        code, _ = self.run_main()
        self.assertEqual(code, 0)
        self.assertEqual(self.report_for(PLAYBOOK_REL)["lint"], [])

    def test_duplicate_section_header_fails_ci(self):
        # QKG_057: a repeated `## ` header must be a lint violation.
        p = self.root / "skills" / "numpy" / "core" / "SKILL.md"
        t = p.read_text().replace("## Common Patterns", "## Common Patterns\n\n## Common Patterns", 1)
        p.write_text(t)
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)
        lint = self.report_for(CORE_REL)["lint"]
        self.assertTrue(any("duplicate section header" in m for m in lint), lint)

    def test_table_dup_cell_fails_ci(self):
        # QKG_057/F10: a table row whose cells repeat a value (old annotation tool
        # appended the Graph Node column twice) must be a lint violation.
        p = self.root / "skills" / "numpy" / "core" / "SKILL.md"
        t = p.read_text()
        t = t.replace("| `array` | `array.py:L1` | Create an ndarray | `dtype` |",
                      "| `array` | `array.py:L1` | Create an ndarray | `array.py:L1` | `array.py:L1` |")
        p.write_text(t)
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)
        lint = self.report_for(CORE_REL)["lint"]
        self.assertTrue(any("duplicated cell value" in m for m in lint), lint)


class TestGraphHashCheck(ValidatorTestCase):
    def test_stale_hash_fails_ci(self):
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)
        lint = self.report_for(STALEHASH_REL)["lint"]
        self.assertTrue(
            any(m.startswith(f"graph_hash mismatch: expected {FIXTURE_HASH}") for m in lint),
            f"expected-hash {FIXTURE_HASH} missing from {lint}")
        self.assertTrue(any("found 0000000000000000" in m for m in lint), lint)

    def test_stale_hash_detected_in_dump(self):
        _, out = self.run_main("--dump-known-debt")
        debt = json.loads(out)["violations"]
        self.assertIn(f"hash:stale:{FIXTURE_HASH}", debt[STALEHASH_REL])

    def test_graph_meta_warn_on_node_count(self):
        self.run_main()
        self.assertTrue(
            any("graph meta: nodes mismatch" in m
                for m in self.report_for(STALEHASH_REL)["meta_warn"]))


class TestRelatedResolution(ValidatorTestCase):
    def test_dangling_related_fails_ci(self):
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)
        self.assert_lint_contains(DANGLING_REL, "related_skills: 'no-such-skill'")

    def test_composes_must_resolve(self):
        self.run_main()
        self.assertEqual(self.report_for(PLAYBOOK_REL)["lint"], [])


class TestSourceCommitCheck(ValidatorTestCase):
    def test_wrong_source_commit_fails_ci(self):
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)
        self.assert_lint_contains(BADCOMMIT_REL, "source_commit does not match graphs.lock")


class TestModuleScopedApi(ValidatorTestCase):
    def test_hallucinated_api_fails(self):
        if not NUMPY_INSTALLED:
            self.skipTest("numpy not installed — fixture requires an installed library")
        self.run_main()
        api_fail = self.report_for(HALLUCINATED_REL)["api_fail"]
        joined = "\n".join(api_fail)
        self.assertIn("func ictus_flip", joined, joined)
        self.assertIn("class QuandaryRegression", joined, joined)

    def test_cross_library_symbol_is_warn_not_fail(self):
        # QKG_050 contract: a class that resolves in ANOTHER library's graph (or any
        # installed library) is a documented cross-library reference — it must be a
        # visible warning, not an api_fail. Only symbols that resolve NOWHERE are
        # hallucinations (test_hallucinated_api_fails above).
        if not NUMPY_INSTALLED:
            self.skipTest("numpy not installed — fixture requires an installed library")
        self.run_main()
        report = self.report_for(HALLUCINATED_REL)
        joined_fail = "\n".join(report["api_fail"])
        joined_warn = "\n".join(report["api_warn"])
        # StandardScaler lives in scikit-learn's graph → cross-library reference (warn)
        self.assertTrue(any("class StandardScaler" in m for m in report["api_warn"]),
                        joined_warn)
        self.assertNotIn("class StandardScaler", joined_fail, joined_fail)

    def test_parameter_table_rows_are_not_api_claims(self):
        # QKG_050: parameter/alias tables document surface, not callables — rows
        # like `n_estimators` / `learning_rate` must never become api_fails.
        if not NUMPY_INSTALLED:
            self.skipTest("numpy not installed — fixture requires an installed library")
        self.run_main("--strict")
        report = self.report_for(PARAMS_REL)
        joined = "\n".join(report["api_fail"])
        self.assertNotIn("n_estimators", joined, joined)
        self.assertNotIn("max_depth", joined, joined)
        self.assertNotIn("learning_rate", joined, joined)
        self.assertEqual(report["api_fail"], [], report["api_fail"])


class TestExitCodes(ValidatorTestCase):
    def test_ci_exits_nonzero_on_planted_debt(self):
        code, _ = self.run_main("--ci")
        self.assertEqual(code, 1)

    def test_plain_run_exits_zero(self):
        code, _ = self.run_main()
        self.assertEqual(code, 0)

    def test_strict_exits_nonzero_on_api_fail(self):
        if not NUMPY_INSTALLED:
            self.skipTest("numpy not installed")
        code, _ = self.run_main("--strict")
        self.assertEqual(code, 1)


class TestKnownDebtBridge(ValidatorTestCase):
    def test_exclude_known_debt_goes_green(self):
        _, out = self.run_main("--dump-known-debt")
        self.write_known_debt(json.loads(out)["violations"])
        code, _ = self.run_main("--ci", "--exclude-known-debt")
        self.assertEqual(code, 0)
        report = self.load_report()
        self.assertEqual(report["totals"]["lint"], 0)

    def test_exclude_known_debt_still_fails_new_violations(self):
        # Only the core section violation is allowlisted — every other planted
        # violation must keep failing.
        self.write_known_debt({CORE_REL: ["section:missing:Provenance"]})
        code, _ = self.run_main("--ci", "--exclude-known-debt")
        self.assertEqual(code, 1)
        for rel in (STALEHASH_REL, DANGLING_REL, BADCOMMIT_REL):
            self.assertTrue(self.report_for(rel)["lint"], f"{rel} must still fail")


class TestDumpKnownDebt(ValidatorTestCase):
    def test_dump_shape(self):
        code, out = self.run_main("--dump-known-debt")
        self.assertEqual(code, 0)
        payload = json.loads(out)
        self.assertIn("violations", payload)
        v = payload["violations"]
        self.assertIn(CORE_REL, v)
        self.assertIn("section:missing:Provenance", v[CORE_REL])
        self.assertIn("related:no-such-skill", v[DANGLING_REL])
        self.assertNotIn(ROUTER_REL, v)          # router has no debt
        self.assertNotIn(PLAYBOOK_REL, v)        # playbook has no debt

    def test_dump_roundtrip_regenerates_file(self):
        _, out = self.run_main("--dump-known-debt")
        self.write_known_debt(json.loads(out)["violations"])
        self.run_main("--ci", "--exclude-known-debt")
        self.assertEqual(self.load_report()["totals"]["lint"], 0)


class TestSubprocessCli(ValidatorTestCase):
    """End-to-end: the real script via `python3 ... --ci` on the fixture tree."""

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(REPO / "scripts" / "validate_skills.py"), *args],
            capture_output=True, text=True, timeout=180)

    def test_subprocess_ci_fails_on_planted_tree(self):
        r = self.run_script("--root", str(self.root), "--ci")
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertIn("missing required section: ## Provenance", r.stdout)
        self.assertIn(f"graph_hash mismatch: expected {FIXTURE_HASH}", r.stdout)
        self.assertIn("related_skills: 'no-such-skill'", r.stdout)
        self.assertIn("source_commit does not match graphs.lock", r.stdout)

    def test_subprocess_ci_skills_dir_targets_one_library(self):
        r = self.run_script("--root", str(self.root),
                            "--skills", str(self.root / "skills" / "numpy"), "--ci")
        self.assertEqual(r.returncode, 1, r.stderr)

    def test_subprocess_ci_exclude_known_debt_exits_zero(self):
        _, out = self.run_main("--dump-known-debt")
        self.write_known_debt(json.loads(out)["violations"])
        r = self.run_script("--root", str(self.root), "--ci", "--exclude-known-debt")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)



class TestLineAwareCitations(ValidatorTestCase):
    """QKG_069: verify_citations --require-lines fails on wrong/missing lines.
    verify_citations.py resolves ROOT at import (no --root flag), so these
    tests plant a bad row in the REAL numpy/core skill, run the real script,
    and restore via addCleanup."""

    def run_verify(self, *extra):
        import subprocess
        r = subprocess.run(
            [sys.executable, "scripts/verify_citations.py", *extra],
            capture_output=True, text=True, cwd=str(REAL_ROOT))
        return r

    def _plant(self, old_row, new_row):
        p = REAL_ROOT / "skills" / "numpy" / "core" / "SKILL.md"
        t = p.read_text()
        assert old_row in t, f"plant anchor missing: {old_row}"
        p.write_text(t.replace(old_row, new_row, 1))
        self.addCleanup(lambda: p.write_text(t))

    def test_wrong_line_fails(self):
        self._plant("_core/_asarray.py:L24", "_core/_asarray.py:L999")
        r = self.run_verify("--require-lines")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("LINE", r.stdout + r.stderr)

    def test_missing_line_fails_require_lines(self):
        self._plant("`_core/_asarray.py:L24`", "`_core/_asarray.py`")
        r = self.run_verify("--require-lines")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("no :L line", r.stdout + r.stderr)

    def test_plain_gate_ignores_missing_lines(self):
        self._plant("`_core/_asarray.py:L24`", "`_core/_asarray.py`")
        r = self.run_verify()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()



if __name__ == "__main__":
    unittest.main()



if __name__ == "__main__":
    unittest.main()
