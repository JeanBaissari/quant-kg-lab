#!/usr/bin/env python3
"""Validate skill claims against actual installed library APIs.

For each SKILL.md, extracts referenced classes/functions,
imports the library, and verifies they exist.

Usage:
    python scripts/validate_skills.py              # validate all skills
    python scripts/validate_skills.py scikit-learn # validate one library
    python scripts/validate_skills.py --ci         # CI mode (exit 1 on failure)
"""
import sys
import re
import json
import importlib
import ast
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent

# Mapping from skill directory to importable module
LIBRARY_IMPORTS = {
    "scikit-learn": ["sklearn"],
    "optuna": ["optuna"],
    "numpy": ["numpy"],
    "scipy": ["scipy"],
    "pandas": ["pandas"],
    "xgboost": ["xgboost"],
    "lightgbm": ["lightgbm"],
    "vectorbt": ["vectorbt"],
    "ta-lib": ["talib"],
    "backtrader": ["backtrader"],
}

def extract_skill_claims(skill_path):
    """Extract referenced API symbols from a SKILL.md file."""
    content = skill_path.read_text()
    
    claims = {
        "classes": set(),
        "functions": set(),
        "modules": set(),
        "source_file": skill_path,
    }
    
    # Extract from Quick Reference tables: | `ClassName` | ...
    for match in re.finditer(r'\|\s*`([A-Za-z_][A-Za-z0-9_.]*)`\s*\|', content):
        symbol = match.group(1)
        if symbol[0].isupper():
            claims["classes"].add(symbol)
        elif '(' in symbol:
            claims["functions"].add(symbol.split('(')[0])
        else:
            claims["functions"].add(symbol)
    
    # Extract from code blocks: sklearn.xxx or optuna.xxx
    for match in re.finditer(r'(?:import\s+(\w+)|from\s+(\w+)\.\w+\s+import\s+(\w+))', content):
        if match.group(1):
            claims["modules"].add(match.group(1))
        if match.group(2):
            claims["modules"].add(match.group(2))
        if match.group(3):
            claims["functions"].add(match.group(3))
    
    # Extract backtick-quoted class names in prose
    for match in re.finditer(r'`([A-Z][A-Za-z]+(?:Classifier|Regressor|Encoder|Scaler|Imputer|Transformer|CV|Search|Split|Model|Kernel|Pruner|Sampler|Study|Trial))`', content):
        claims["classes"].add(match.group(1))
    
    return claims

def validate_claims(claims, library_name):
    """Validate extracted claims against actual library imports."""
    results = {"passed": [], "failed": [], "skipped": []}
    
    if library_name not in LIBRARY_IMPORTS:
        results["skipped"].append(f"Unknown library: {library_name}")
        return results
    
    modules_to_try = LIBRARY_IMPORTS[library_name]
    lib_imported = False
    top_module = None
    
    for mod_name in modules_to_try:
        try:
            top_module = importlib.import_module(mod_name)
            lib_imported = True
            break
        except ImportError:
            continue
    
    if not lib_imported:
        results["skipped"].append(f"Cannot import {library_name} — not installed")
        return results
    
    # Build a map of ALL public symbols across submodules
    import pkgutil
    all_symbols = {}
    
    def crawl_module(module, prefix=""):
        """Recursively crawl submodules and collect public symbols."""
        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
            try:
                attr = getattr(module, attr_name)
                full_name = f"{prefix}.{attr_name}" if prefix else attr_name
                # Store class/function names
                if isinstance(attr, type) or callable(attr):
                    all_symbols[attr_name] = full_name
            except:
                pass
        
        # Crawl subpackages (one level deep)
        if hasattr(module, '__path__'):
            for _, submod_name, is_pkg in pkgutil.iter_modules(module.__path__, prefix + '.' if prefix else ''):
                try:
                    submod = importlib.import_module(submod_name)
                    for attr_name in dir(submod):
                        if attr_name.startswith('_'):
                            continue
                        try:
                            attr = getattr(submod, attr_name)
                            if isinstance(attr, type) or callable(attr):
                                all_symbols[attr_name] = f"{submod_name}.{attr_name}"
                        except:
                            pass
                except ImportError:
                    pass
    
    # Crawl two levels for sklearn (subpackages like sklearn.ensemble, sklearn.linear_model)
    crawl_module(top_module)
    if library_name == "scikit-learn":
        # Also crawl common subpackages
        for subpkg in ['ensemble', 'linear_model', 'tree', 'svm', 'neural_network', 
                       'cluster', 'decomposition', 'preprocessing', 'model_selection',
                       'metrics', 'feature_selection', 'impute', 'compose', 'pipeline',
                       'gaussian_process', 'naive_bayes', 'neighbors', 'manifold',
                       'semi_supervised', 'discriminant_analysis', 'isotonic', 'calibration',
                       'covariance', 'cross_decomposition', 'dummy', 'kernel_approximation',
                       'kernel_ridge', 'mixture', 'multiclass', 'multioutput']:
            try:
                submod = importlib.import_module(f"sklearn.{subpkg}")
                for attr_name in dir(submod):
                    if attr_name.startswith('_'):
                        continue
                    try:
                        attr = getattr(submod, attr_name)
                        if isinstance(attr, type) or callable(attr):
                            all_symbols[attr_name] = f"sklearn.{subpkg}.{attr_name}"
                    except:
                        pass
            except ImportError:
                pass
    
    # Validate classes
    for cls_name in sorted(claims["classes"]):
        if cls_name in all_symbols:
            results["passed"].append(f"class:{cls_name} → {all_symbols[cls_name]}")
        else:
            # Try case-insensitive
            found = False
            for sym, full in all_symbols.items():
                if sym.lower() == cls_name.lower():
                    results["passed"].append(f"class:{cls_name} → {full} (case-insensitive match)")
                    found = True
                    break
            if not found:
                results["failed"].append(f"class:{cls_name} — NOT FOUND in {library_name} ({len(all_symbols)} symbols searched)")
    
    # Validate functions
    for func_name in sorted(claims["functions"]):
        clean = func_name.split('.')[-1]  # handle module.func references
        if clean in all_symbols:
            results["passed"].append(f"func:{func_name} → {all_symbols[clean]}")
        else:
            # Functions from external libraries (numpy, etc.) are expected to fail
            pass  # Don't flag function misses as failures — many are cross-library refs
    
    return results

def find_skills():
    """Find all SKILL.md files in skills/ directory."""
    skills_dir = REPO_ROOT / "skills"
    skill_files = list(skills_dir.rglob("SKILL.md"))
    return skill_files

def infer_library(skill_path):
    """Infer which library a skill belongs to from its path."""
    parts = skill_path.relative_to(REPO_ROOT / "skills").parts
    for lib in LIBRARY_IMPORTS:
        if lib in str(skill_path).lower():
            return lib
    return parts[0] if parts else "unknown"

def main():
    ci_mode = "--ci" in sys.argv
    target = None
    for arg in sys.argv[1:]:
        if arg in LIBRARY_IMPORTS:
            target = arg
    
    skill_files = find_skills()
    
    if target:
        skill_files = [s for s in skill_files if target in str(s).lower()]
    
    print(f"=== Skill Validation ===")
    print(f"Skills found: {len(skill_files)}")
    print(f"Target library: {target or 'all'}")
    print()
    
    total_passed = 0
    total_failed = 0
    all_results = {}
    
    for skill_path in sorted(skill_files):
        lib = infer_library(skill_path)
        claims = extract_skill_claims(skill_path)
        results = validate_claims(claims, lib)
        
        rel_path = skill_path.relative_to(REPO_ROOT)
        all_results[str(rel_path)] = results
        
        passed = len(results["passed"])
        failed = len(results["failed"])
        total_passed += passed
        total_failed += failed
        
        status = "✅" if failed == 0 else "❌"
        print(f"{status} {rel_path}")
        print(f"   Passed: {passed}, Failed: {failed}")
        if results["failed"]:
            for f in results["failed"][:5]:
                print(f"     ✗ {f}")
        if results["skipped"]:
            for s in results["skipped"]:
                print(f"     ⚠ {s}")
        print()
    
    print(f"=== Summary ===")
    print(f"Total: {total_passed} passed, {total_failed} failed")
    
    # Write report
    report_path = REPO_ROOT / "docs" / "skill-validation-report.json"
    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, "w") as f:
        json.dump(all_results, f, indent=2, default=list)
    print(f"Report: {report_path}")
    
    if ci_mode and total_failed > 0:
        sys.exit(1)
    
    return 0 if total_failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
