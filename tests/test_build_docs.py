"""Exercise the documentation build through its public command-line interface."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_docs.py"


class BuildDocsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "scripts").mkdir()
        (self.root / "tests").mkdir()
        (self.root / "mkdocs").mkdir()
        (self.root / "mkdocs" / "__init__.py").write_text("")
        if SCRIPT.exists():
            shutil.copyfile(SCRIPT, self.root / "scripts" / "build_docs.py")
        (self.root / "scripts" / "optimize_screenshots.py").write_text(
            "import os, pathlib, sys\n"
            "pathlib.Path(os.environ['BUILD_TRACE']).open('a').write('optimize\\n')\n"
            "sys.exit(os.environ.get('BUILD_FAIL') == 'optimize')\n"
        )
        (self.root / "scripts" / "check_docs.py").write_text(
            "import os, pathlib, sys\n"
            "pathlib.Path(os.environ['BUILD_TRACE']).open('a').write('check\\n')\n"
            "sys.exit(os.environ.get('BUILD_FAIL') == 'check')\n"
        )
        (self.root / "tests" / "test_docs.py").write_text(
            "import os, pathlib, unittest\n"
            "class DocsTests(unittest.TestCase):\n"
            "    def test_docs(self):\n"
            "        pathlib.Path(os.environ['BUILD_TRACE']).open('a').write('test\\n')\n"
            "        self.assertNotEqual(os.environ.get('BUILD_FAIL'), 'test')\n"
        )
        (self.root / "mkdocs" / "__main__.py").write_text(
            "import os, pathlib, sys\n"
            "pathlib.Path(os.environ['BUILD_TRACE']).open('a').write('build\\n')\n"
            "sys.exit(os.environ.get('BUILD_FAIL') == 'build')\n"
        )

    def run_build(
        self, *, optimize: bool = False, fail: str = "", provider: str = ""
    ) -> tuple[int, list[str]]:
        trace = self.root / "trace.txt"
        trace.unlink(missing_ok=True)
        env = os.environ.copy()
        env.update(BUILD_TRACE=str(trace), BUILD_FAIL=fail, PYTHONPATH=str(self.root))
        env.pop("CI", None)
        env.pop("GITHUB_ACTIONS", None)
        env.pop("CF_PAGES", None)
        if provider == "github":
            env.update(CI="true", GITHUB_ACTIONS="true")
        elif provider == "cloudflare":
            env.update(CI="true", CF_PAGES="1")
        elif provider == "generic-ci":
            env.update(CI="true")
        command = [sys.executable, str(self.root / "scripts" / "build_docs.py")]
        if optimize:
            command.append("--optimize-screenshots")
        result = subprocess.run(command, cwd=self.root, env=env, capture_output=True, text=True)
        return result.returncode, trace.read_text().splitlines() if trace.exists() else []

    def test_default_build_does_not_modify_screenshots(self) -> None:
        code, trace = self.run_build()
        self.assertEqual(code, 0)
        self.assertEqual(trace, ["check", "test", "build"])

    def test_optimization_requires_ci_checkout(self) -> None:
        code, trace = self.run_build(optimize=True)
        self.assertNotEqual(code, 0)
        self.assertEqual(trace, [])
        code, trace = self.run_build(optimize=True, provider="generic-ci")
        self.assertNotEqual(code, 0)
        self.assertEqual(trace, [])

    def test_ci_opt_in_runs_optimization_before_validation(self) -> None:
        for provider in ("github", "cloudflare"):
            with self.subTest(provider=provider):
                code, trace = self.run_build(optimize=True, provider=provider)
                self.assertEqual(code, 0)
                self.assertEqual(trace, ["optimize", "check", "test", "build"])

    def test_each_failed_step_stops_later_steps(self) -> None:
        for failed, expected in {
            "optimize": ["optimize"],
            "check": ["optimize", "check"],
            "test": ["optimize", "check", "test"],
            "build": ["optimize", "check", "test", "build"],
        }.items():
            with self.subTest(failed=failed):
                code, trace = self.run_build(optimize=True, provider="github", fail=failed)
                self.assertNotEqual(code, 0)
                self.assertEqual(trace, expected)


if __name__ == "__main__":
    unittest.main()
