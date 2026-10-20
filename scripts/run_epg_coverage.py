#!/usr/bin/env python3
"""Run EPG coverage with the same multilingual policy as the generator."""
import epg_coverage


def allow_valid_xmltv_text(elem):
    return bool((elem.text or "").strip())


def main():
    original = epg_coverage.is_english_text_element
    try:
        epg_coverage.is_english_text_element = allow_valid_xmltv_text
        epg_coverage.main()
    finally:
        epg_coverage.is_english_text_element = original


if __name__ == "__main__":
    main()
