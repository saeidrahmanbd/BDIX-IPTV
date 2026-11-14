from __future__ import annotations

import ast
import unittest
from pathlib import Path


class LogoAuthenticityManifestReadOnlyTests(unittest.TestCase):
    def test_generator_has_no_git_or_subprocess_staging_side_effect(self):
        source = Path("scripts/generate_logo_authenticity_manifest.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported_modules = {
            alias.name for node in ast.walk(tree)
            if isinstance(node, ast.Import) for alias in node.names
        }
        imported_from = {
            node.module for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
        }
        self.assertNotIn("subprocess", imported_modules)
        self.assertNotIn("subprocess", imported_from)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                self.assertNotEqual(node.func.attr, "run")
                self.assertNotEqual(node.func.attr, "Popen")
        self.assertNotIn("git add", source)
        self.assertNotIn("git reset", source)


if __name__ == "__main__":
    unittest.main()
