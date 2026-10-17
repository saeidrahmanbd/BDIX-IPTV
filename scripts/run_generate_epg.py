#!/usr/bin/env python3
"""Run the normal EPG generator with the build-time iptv-org guide prepended."""
from pathlib import Path
import sys

import generate_epg

LOCAL_GUIDE = Path("/tmp/iptv-org-guide.xml")


def fetch_with_local(url):
    if url.startswith("file://"):
        return LOCAL_GUIDE.read_bytes()
    return generate_epg.fetch(url)


def main():
    if not LOCAL_GUIDE.is_file() or LOCAL_GUIDE.stat().st_size == 0:
        raise SystemExit("Missing /tmp/iptv-org-guide.xml; run fetch_iptv_org_epg.py first")

    original_sources = list(generate_epg.SOURCES)
    original_fetch = generate_epg.fetch
    try:
        generate_epg.SOURCES[:] = ["file:///tmp/iptv-org-guide.xml"] + original_sources
        generate_epg.fetch = fetch_with_local
        generate_epg.main()
    finally:
        generate_epg.fetch = original_fetch
        generate_epg.SOURCES[:] = original_sources


if __name__ == "__main__":
    main()
