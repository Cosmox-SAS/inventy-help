#!/usr/bin/env python3
"""Validate and build the documentation with the same checks in CI and Pages."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--optimize-screenshots",
        action="store_true",
        help="convert tracked PNG screenshots only in a CI build checkout",
    )
    args = parser.parse_args()

    if args.optimize_screenshots and not (
        os.environ.get("CI") == "true"
        and (os.environ.get("GITHUB_ACTIONS") == "true" or os.environ.get("CF_PAGES") == "1")
    ):
        parser.error("--optimize-screenshots requires a GitHub Actions or Cloudflare Pages CI build")

    commands = []
    if args.optimize_screenshots:
        commands.append([sys.executable, str(ROOT / "scripts" / "optimize_screenshots.py")])
    commands.extend(
        [
            [sys.executable, str(ROOT / "scripts" / "check_docs.py")],
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
            [sys.executable, "-m", "mkdocs", "build", "--strict"],
        ]
    )

    for command in commands:
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
