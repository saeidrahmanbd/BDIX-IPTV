#!/usr/bin/env python3
"""Synchronize static EPG ID maps only for Workers that actually implement one."""
import csv, json, re
from pathlib import Path

CSV = Path("reports/epg-india-channel-mapping.csv")
WORKERS = [
    Path("xtream-main/worker.js"),
    Path("xtream-bdix/worker.js"),
]


def main():
    rows = []
    with CSV.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            status = row.get("status", "")
            if row.get("tvg_id") and row.get("epg_id") and status.startswith("MAPPED"):
                ids = [value.strip() for value in row["epg_id"].split("|") if value.strip()]
                if ids:
                    rows.append((row["tvg_id"].strip(), ids))

    mapping = {}
    for key, ids in rows:
        mapping.setdefault(key, [])
        for value in ids:
            if value not in mapping[key]:
                mapping[key].append(value)

    checked = 0
    updated = 0
    for worker in WORKERS:
        if not worker.exists():
            continue
        checked += 1
        text = worker.read_text(encoding="utf-8")
        pattern = re.compile(r'const EPG_ID_MAP\s*=\s*\{.*?\};', re.S)
        if not pattern.search(text):
            # Current Workers use the published XMLTV and pass the playlist
            # tvg-id through as epg_channel_id. No static alias map is needed.
            if "EPG_ID_MAP" not in text and "epg_channel_id:s.tvgId" in text:
                print(
                    f"EPG worker map sync skipped: {worker} uses playlist tvg-id "
                    "directly with the shared XMLTV guide."
                )
                continue
            active_handler = "export default" in text or ("addEventListener" in text and "fetch" in text)
            if not active_handler:
                print(f"EPG worker map sync skipped: {worker} has no active Worker handler.")
                continue
            raise SystemExit(f"EPG_ID_MAP block not found in active Xtream Worker: {worker}")

        replacement = "const EPG_ID_MAP = " + json.dumps(
            dict(sorted(mapping.items())), ensure_ascii=False, separators=(",", ":")
        ) + ";\n"
        new_text = pattern.sub(replacement, text, count=1)
        if new_text != text:
            worker.write_text(new_text, encoding="utf-8")
            updated += 1

    if checked == 0:
        print("EPG worker map sync skipped: no current Xtream Worker files found; shared XMLTV maintenance can continue.")
    elif updated:
        print(f"EPG worker mappings synchronized: {len(mapping)} channel identities in {updated} Worker(s)")
    else:
        print(f"EPG worker map sync complete: no static EPG_ID_MAP required in {checked} current Worker(s).")


if __name__ == "__main__":
    main()
