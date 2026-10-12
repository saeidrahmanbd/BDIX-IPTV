#!/usr/bin/env python3
"""Build a logo provenance manifest for all maintained playlists."""
import json
import re
from pathlib import Path
from datetime import datetime, timezone

PLAYLISTS = ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "NVisionBD-Playlist.m3u"]
OUT = Path("reports/logo-authenticity-manifest.json")
REGISTRY_PATH = Path("reports/logo-source-registry.json")
ATTR_RE = re.compile(r'([\\w-]+)="([^"]*)"')

def attrs(line):
    return dict(ATTR_RE.findall(line))

def main():
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")) if REGISTRY_PATH.exists() else {}
    records, counts = [], {}
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.exists():
            continue
        total = 0
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if not line.startswith("#EXTINF"):
                continue
            meta = attrs(line)
            name = (meta.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
            logo = meta.get("tvg-logo", "").strip()
            key = f"{playlist}|{meta.get('tvg-id','')}|{name}|{logo}"
            source = registry.get(key, {})
            if logo and Path(logo.split("?", 1)[0]).name.startswith("generated-fallback-"):
                status = "generated_fallback"
                reason = "Original generated artwork marked UNOFFICIAL ARTWORK; not a broadcaster logo."
            elif source.get("status") in {"official_verified", "third_party_verified"} and source.get("source_url"):
                status = source["status"]
                reason = source.get("notes", "Source recorded in provenance registry.")
            else:
                status = "needs_review"
                reason = "No explicit provenance record confirms this image as an authentic broadcaster asset."
            records.append({
                "playlist": playlist, "channel_name": name,
                "tvg_id": meta.get("tvg-id", ""), "channel_id": meta.get("channel-id", ""),
                "logo": logo, "status": status, "source_url": source.get("source_url", ""),
                "reason": reason
            })
            total += 1
        counts[playlist] = total
    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status_definitions": {
            "official_verified": "Verified asset from the broadcaster's official source.",
            "third_party_verified": "Authentic asset confirmed from a reliable, attributable third-party source.",
            "generated_fallback": "Original generated artwork; not an official broadcaster logo.",
            "needs_review": "Authenticity is undocumented, or the logo is missing."
        },
        "counts_by_playlist": counts, "entry_count": len(records), "entries": records
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    tally = {}
    for item in records:
        tally[item["status"]] = tally.get(item["status"], 0) + 1
    print(f"Wrote {OUT}: {len(records)} playlist entries; statuses={tally}")

if __name__ == "__main__":
    main()
