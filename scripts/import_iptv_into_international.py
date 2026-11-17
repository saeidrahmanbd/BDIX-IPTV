#!/usr/bin/env python3
"""One-time import of IPTV primary playlist rows into International before reorganization."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import reorganize_international_playlist as organizer

SOURCE = ROOT / "IPTV-Playlist.m3u"
TARGET = ROOT / "International-Playlist.m3u"
REPORT = ROOT / "reports" / "international-import-report.md"


def main():
    if not SOURCE.is_file() or not TARGET.is_file():
        raise SystemExit("Both source and target playlists must exist.")
    source_text = SOURCE.read_text(encoding="utf-8-sig")
    target_text = TARGET.read_text(encoding="utf-8-sig")
    source_header, source_blocks = organizer.parse_playlist(source_text)
    target_header, target_blocks = organizer.parse_playlist(target_text)

    if not source_blocks:
        raise SystemExit("IPTV source playlist has no entries; refusing import.")
    source_rows = []
    skipped_review = 0
    for block in source_blocks:
        if not block or not block[0].startswith("#EXTINF:"):
            continue
        attrs = organizer.attrs(organizer.split_info(block[0])[0])
        if (attrs.get("group-title") or "").strip().casefold() == "review":
            skipped_review += 1
            continue
        source_rows.append(block)

    # Preserve every existing International row, including rows not present in IPTV.
    existing_rows = list(target_blocks)
    # A zero-byte/empty target is recoverable: seed its required attribution/header
    # from IPTV, then rename only the playlist title and let the organizer rebuild categories.
    header = target_header if target_header else source_header
    header = [line for line in header if not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    name_line = next((i for i, line in enumerate(header) if line.startswith("#PLAYLIST-STUDIO-NAME:")), None)
    if name_line is None:
        raise SystemExit("Source/target playlist name header is missing.")
    header[name_line] = '#PLAYLIST-STUDIO-NAME:"International-Playlist.m3u"'
    header.insert(name_line + 1, "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(
        ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment",
         "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports",
         "Backup", "Review", "New Channels", "New Backups"], ensure_ascii=False))

    # Do not pre-filter by discovery policy: this is a one-time source import.
    # The organizer's genre-first classification assigns imported foreign genre channels
    # to their genre groups; future discovery continues using discovery_eligibility().
    merged = header + [line for block in source_rows + existing_rows for line in block]
    TARGET.write_text("\n".join(merged) + "\n", encoding="utf-8")
    organizer.PLAYLIST = TARGET
    organizer.main()

    _, final_blocks = organizer.parse_playlist(TARGET.read_text(encoding="utf-8"))
    final_attrs = [organizer.attrs(organizer.split_info(block[0])[0]) for block in final_blocks]
    groups = {}
    for attrs in final_attrs:
        group = attrs.get("group-title", "")
        groups[group] = groups.get(group, 0) + 1
    final_urls = [organizer.stream_url_key(organizer.url_of(block)) for block in final_blocks]
    if len(final_urls) != len(set(final_urls)):
        raise SystemExit("Post-import duplicate stream URL check failed.")
    if any((a.get("group-title") or "").casefold() == "review" for a in final_attrs):
        raise SystemExit("Review entries must not appear in International.")
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(
        "# One-time IPTV to International Import\n\n"
        f"- IPTV source entries: {len(source_blocks)}\n"
        f"- IPTV Review entries excluded: {skipped_review}\n"
        f"- IPTV entries submitted for import: {len(source_rows)}\n"
        f"- Pre-existing International entries preserved as inputs: {len(existing_rows)}\n"
        f"- Final International entries: {len(final_blocks)}\n"
        f"- Unique stream URLs: {len(set(final_urls))}\n"
        "- Duplicate stream URLs: 0\n"
        "- Review entries in International: 0\n"
        "- Future discovery policy changed: No\n\n"
        "## Final group counts\n\n" +
        "".join(f"- {group}: {count}\n" for group, count in groups.items()),
        encoding="utf-8"
    )
    print(json.dumps({
        "source_entries": len(source_blocks), "review_excluded": skipped_review,
        "source_import_candidates": len(source_rows), "existing_international": len(existing_rows),
        "final_entries": len(final_blocks), "unique_urls": len(set(final_urls)),
        "groups": groups
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
