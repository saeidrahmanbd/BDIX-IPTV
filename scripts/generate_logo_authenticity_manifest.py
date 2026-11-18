#!/usr/bin/env python3
"""Build a conservative, source-attributed logo provenance manifest."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

import logo_provenance

PLAYLISTS = ["IPTV-Playlist.m3u", "International-Playlist.m3u"]
OUT = Path("reports/logo-authenticity-manifest.json")
REGISTRY_PATH = Path("reports/logo-source-registry.json")
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def attrs(line):
    return dict(ATTR_RE.findall(line))


asset_stem = logo_provenance.asset_stem


def provenance_for(registry, playlist, meta, name, logo):
    """Return ``(record, match)`` using the shared deterministic resolver.

    An exact registry key wins; otherwise exactly one distinct record with the same
    playlist, tvg-id, channel name and asset stem. A name-only match is forbidden,
    and ambiguity resolves to no provenance (match ``ambiguous``).
    """
    return logo_provenance.resolve_provenance(
        registry, playlist, logo_provenance.entry_identity(meta), name, logo
    )


def main():
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")) if REGISTRY_PATH.exists() else {}
    records, counts, source_hashes = [], {}, {}

    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.exists():
            continue

        source_hashes[playlist] = hashlib.sha256(path.read_bytes()).hexdigest()
        total = 0
        for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.startswith("#EXTINF"):
                continue

            meta = attrs(line)
            name = (meta.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
            logo = meta.get("tvg-logo", "").strip()
            source, registry_match = provenance_for(registry, playlist, meta, name, logo)

            # The asset decides its class; a registry record can never promote a
            # generated fallback, and a conflicting record is surfaced, not trusted.
            verdict = logo_provenance.classify_logo(source, registry_match, logo)
            status = verdict["status"]
            reason = verdict["reason"]

            records.append({
                "playlist": playlist,
                "line": line_number,
                "channel_name": name,
                "tvg_id": meta.get("tvg-id", ""),
                "channel_id": meta.get("channel-id", ""),
                "logo": logo,
                "status": status,
                "registry_match": registry_match,
                "source_url": verdict["source_url"],
                "reason": reason,
                "registry_conflict": ", ".join(verdict["problems"]),
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
        "source_sha256_by_playlist": source_hashes,
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
