#!/usr/bin/env python3
"""Run EPG coverage with the same multilingual policy as the generator."""
import epg_coverage
import augment_epg_mapping_from_additional_sources

ADDITIONAL_SOURCES = [
    "https://epg.lat/files/in.xml.gz",
    "https://epg.lat/files/us.xml.gz",
    "https://www.free-epg.de/api/epg/in.xml.gz",
    "https://www.free-epg.de/api/epg/us.xml.gz",
    "https://www.open-epg.com/files/india.xml.gz",
]


def allow_valid_xmltv_text(elem):
    return bool((elem.text or "").strip())


def main():
    # Discover conservative exact-name mappings from the newly supplied India
    # feeds before coverage is calculated. Existing trusted mappings are kept.
    augment_epg_mapping_from_additional_sources.main()
    original_policy = epg_coverage.is_english_text_element
    original_sources = list(epg_coverage.SOURCES)
    try:
        epg_coverage.SOURCES[:] = list(dict.fromkeys(original_sources + ADDITIONAL_SOURCES))
        epg_coverage.is_english_text_element = allow_valid_xmltv_text
        epg_coverage.main()
    finally:
        epg_coverage.is_english_text_element = original_policy
        epg_coverage.SOURCES[:] = original_sources


if __name__ == "__main__":
    main()
