#!/usr/bin/env python3
"""Run the EPG generator with build-time guides and a shared, non-destructive text policy.

The core generator is intentionally reused. This runner patches two historical
bottlenecks before invoking it:
1. XMLTV titles are not restricted to English/Bengali scripts; valid Hindi,
   Tamil, Telugu, Arabic, etc. schedules are legitimate for their channels.
2. Every mapped source ID is retained, including multiple provider IDs for the
   same playlist identity. The old Indian-Bangla special case discarded all but
   the first source ID.
"""
from pathlib import Path
import subprocess
import generate_epg
import augment_epg_mapping_from_additional_sources

LOCAL_GUIDE = Path("/tmp/iptv-org-guide.xml")
FREEEPG_BD = "https://free-epg.de/api/epg/bd.xml.gz"

# These are the additional sources supplied during the October 20 EPG repair.
# The India feeds are also used by the mapping-discovery helper; the US feeds
# are retained as schedule fallbacks but never used for India name mapping.
ADDITIONAL_SOURCES = [
    "https://epg.lat/files/in.xml.gz",
    "https://epg.lat/files/us.xml.gz",
    "https://www.free-epg.de/api/epg/in.xml.gz",
    "https://www.free-epg.de/api/epg/us.xml.gz",
    "https://www.open-epg.com/files/india.xml.gz",
]


def allow_valid_xmltv_text(elem):
    """Allow any non-empty XMLTV visible text; language is channel/source specific."""
    return bool((elem.text or "").strip())


def load_mapping_all_sources():
    """Load every approved source ID mapped to each playlist tvg-id."""
    reverse = {}
    if not generate_epg.MAPPING.exists():
        return reverse
    import csv
    with generate_epg.MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            target = row.get("tvg_id", "").strip()
            if not target:
                continue
            for source_id in (x.strip() for x in row.get("epg_id", "").split("|")):
                if source_id:
                    reverse.setdefault(source_id, set()).add(target)
    return {source_id: sorted(targets) for source_id, targets in reverse.items()}


def main():
    if not LOCAL_GUIDE.is_file() or LOCAL_GUIDE.stat().st_size == 0:
        raise SystemExit("Missing /tmp/iptv-org-guide.xml; run fetch_iptv_org_epg.py first")

    # Keep mapping discovery in the same generation path so a newly discovered
    # exact-name ID is immediately available to the XMLTV builder.
    augment_epg_mapping_from_additional_sources.main()
    subprocess.run(["python", "scripts/augment_epg_mapping_from_iptv_org.py"], check=True)

    original_sources = list(generate_epg.SOURCES)
    original_fetch = generate_epg.fetch
    original_policy = generate_epg.is_english_text_element
    original_loader = generate_epg.load_mapping

    def fetch_with_local(url):
        if url.startswith("file://"):
            return LOCAL_GUIDE.read_bytes()
        return original_fetch(url)

    try:
        # Deduplicate while preserving the generator's established source order.
        generate_epg.SOURCES[:] = list(dict.fromkeys(
            [
                "file:///tmp/iptv-org-guide.xml",
                FREEEPG_BD,
                *ADDITIONAL_SOURCES,
            ] + original_sources
        ))
        generate_epg.fetch = fetch_with_local
        generate_epg.is_english_text_element = allow_valid_xmltv_text
        generate_epg.load_mapping = load_mapping_all_sources
        generate_epg.main()
    finally:
        generate_epg.fetch = original_fetch
        generate_epg.is_english_text_element = original_policy
        generate_epg.load_mapping = original_loader
        generate_epg.SOURCES[:] = original_sources


if __name__ == "__main__":
    main()
