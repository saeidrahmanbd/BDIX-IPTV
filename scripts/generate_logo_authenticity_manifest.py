#!/usr/bin/env python3
"""Build a conservative, source-attributed logo provenance manifest."""
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

PLAYLISTS = ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u"]
OUT = Path("reports/logo-authenticity-manifest.json")
REGISTRY_PATH = Path("reports/logo-source-registry.json")
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def attrs(line):
    return dict(ATTR_RE.findall(line))


def asset_stem(logo):
    """Return only the local-looking final filename stem, case-insensitively."""
    filename = Path(str(logo or "").split("?", 1)[0].split("#", 1)[0]).name
    return Path(filename).stem.casefold()


def provenance_for(registry, playlist, meta, name, logo):
    """Use an exact registry key, or a strictly identical asset stem after format conversion.

    A name-only match is intentionally forbidden: a different image for the same
    channel must not inherit provenance from a previously verified logo.
    """
    key = f"{playlist}|{meta.get('tvg-id', '')}|{name}|{logo}"
    if key in registry:
        return registry[key], "exact-key"

    wanted_stem = asset_stem(logo)
    if not wanted_stem:
        return {}, "none"

    candidates = []
    for reg_key, source in registry.items():
        parts = reg_key.split("|", 3)
        if len(parts) != 4:
            continue
        reg_playlist, reg_id, reg_name, reg_logo = parts
        if (
            reg_playlist == playlist
            and reg_id == meta.get("tvg-id", "")
            and reg_name == name
            and asset_stem(reg_logo) == wanted_stem
            and source.get("status") in {"official_verified", "third_party_verified", "generated_fallback"}
        ):
            candidates.append(source)

    # Ambiguous provenance is not enough to mark an asset verified.
    if len(candidates) == 1:
        return candidates[0], "same-asset-stem-format-conversion"
    return {}, "none"


def main():
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")) if REGISTRY_PATH.exists() else {}
    records, counts = [], {}

    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.exists():
            continue

        total = 0
        for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.startswith("#EXTINF"):
                continue

            meta = attrs(line)
            name = (meta.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
            logo = meta.get("tvg-logo", "").strip()
            source, registry_match = provenance_for(registry, playlist, meta, name, logo)

            filename = Path(logo.split("?", 1)[0].split("#", 1)[0]).name.casefold()
            if filename.startswith("generated-fallback-"):
                status = "generated_fallback"
                reason = "Explicitly labelled local fallback artwork; it is not an official broadcaster logo."
            elif source.get("status") in {"official_verified", "third_party_verified"} and source.get("source_url"):
                status = source["status"]
                note = source.get("notes", "Source recorded in provenance registry.")
                if registry_match == "same-asset-stem-format-conversion":
                    reason = "Verified source attribution retained for the same local asset stem after file-format conversion. " + note
                else:
                    reason = note
            else:
                status = "needs_review"
                reason = "No unambiguous provenance record matches this exact logo asset; a similar channel name alone is not proof."

            records.append({
                "playlist": playlist,
                "line": line_number,
                "channel_name": name,
                "tvg_id": meta.get("tvg-id", ""),
                "channel_id": meta.get("channel-id", ""),
                "logo": logo,
                "status": status,
                "registry_match": registry_match,
                "source_url": source.get("source_url", ""),
                "reason": reason,
            })
            total += 1
        counts[playlist] = total

    tally = {}
    tally_by_playlist = {}
    for item in records:
        tally[item["status"]] = tally.get(item["status"], 0) + 1
        per_playlist = tally_by_playlist.setdefault(item["playlist"], {})
        per_playlist[item["status"]] = per_playlist.get(item["status"], 0) + 1

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status_definitions": {
            "official_verified": "Verified asset from the broadcaster's official source.",
            "third_party_verified": "Authentic asset confirmed from a reliable, attributable third-party source.",
            "generated_fallback": "Original local fallback artwork; not an official broadcaster logo.",
            "needs_review": "Authenticity is undocumented, the source is ambiguous, or the logo is missing."
        },
        "counts_by_playlist": counts,
        "status_counts": tally,
        "status_counts_by_playlist": tally_by_playlist,
        "entry_count": len(records),
        "entries": records,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}: {len(records)} entries; statuses={tally}")

    # Newly fetched assets must be staged with the matching playlist reference.
    try:
        subprocess.run(["git", "add", "logos/"], check=True)
        print("Staged repaired logo assets: logos/")
    except Exception as exc:
        print(f"Warning: could not stage logo assets automatically: {exc}")


if __name__ == "__main__":
    main()
