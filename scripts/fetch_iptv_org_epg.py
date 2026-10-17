#!/usr/bin/env python3
"""Fetch a targeted XMLTV guide using the upstream iptv-org/epg scrapers.

This is intentionally a build-time source. The generated guide is kept in /tmp
and is consumed by generate_epg.py; it is not committed as a second public EPG.
"""
from pathlib import Path
import shutil
import subprocess

REPO = "https://github.com/iptv-org/epg.git"
WORK = Path("/tmp/iptv-org-epg")
OUTPUT = Path("/tmp/iptv-org-guide.xml")
SITES = ["dishtv.in", "tataplay.com", "airtelxstream.in", "zee5.com"]


def run(*args, cwd=None):
    print("+", " ".join(args))
    subprocess.run(args, cwd=cwd, check=True)


def main():
    if WORK.exists():
        shutil.rmtree(WORK)
    if OUTPUT.exists():
        OUTPUT.unlink()

    run("git", "clone", "--depth", "1", REPO, str(WORK))
    run("npm", "ci", "--no-audit", "--no-fund", cwd=WORK)
    run(
        "npm", "run", "grab", "---",
        f"--sites={','.join(SITES)}",
        f"--output={OUTPUT}",
        "--lang=en",
        cwd=WORK,
    )

    if not OUTPUT.is_file() or OUTPUT.stat().st_size == 0:
        raise SystemExit("iptv-org EPG generation produced no guide")
    print(f"iptv-org guide ready: {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
