#!/usr/bin/env python3
"""Create a concise, source-hash-verified queue for logo provenance review."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

PLAYLISTS = ("IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u")
MANIFEST = Path("reports/logo-authenticity-manifest.json")
OUT = Path("reports/logo-provenance-review.md")


def build_report(manifest, playlist_hashes, generated_at=None, limit=40):
    generated_at = generated_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    entries = manifest.get("entries", [])
    counts = manifest.get("status_counts_by_playlist", {})
    lines = [
        "# Logo Provenance Review", "",
        f"Generated: **{generated_at}**", "",
        "This report tracks source documentation, not visual correctness. A needs_review entry means the exact asset source is missing or ambiguous; it does not by itself prove the logo is wrong. generated_fallback means explicitly unofficial fallback artwork.",
        "Unattributed logos are **not provenance-passed**; they remain pending review. This status is separate from technical image integrity and the pre-publish safety gate.", "",
        "## Source playlist fingerprints", "",
    ]
    for playlist in PLAYLISTS:
        lines.append(f"- {playlist} SHA-256: **{playlist_hashes[playlist]}**")
    lines += ["", "## Provenance status by playlist", "", "| Playlist | Official verified | Third-party verified | Unofficial fallback | Needs review |", "|---|---:|---:|---:|---:|"]
    for playlist in PLAYLISTS:
        status = counts.get(playlist, {})
        lines.append(
            f"| {playlist} | {status.get('official_verified', 0)} | {status.get('third_party_verified', 0)} | "
            f"{status.get('generated_fallback', 0)} | {status.get('needs_review', 0)} |"
        )
    review = sorted(
        (entry for entry in entries if entry.get("status") == "needs_review"),
        key=lambda item: (item.get("playlist", ""), item.get("channel_name", "").casefold(), item.get("tvg_id", "")),
    )
    lines += [
        "", "## First items requiring source attribution", "",
        f"Showing up to {min(limit, len(review))} of {len(review)} items. The complete inventory, including all status reasons and recorded source URLs, is in reports/logo-authenticity-manifest.json.", "",
        "| Playlist | Channel | tvg-id | Local asset | Why it needs review |", "|---|---|---|---|---|",
    ]
    for entry in review[:limit]:
        playlist = str(entry.get("playlist", "")).replace("|", "\\|")
        name = str(entry.get("channel_name", "")).replace("|", "\\|").replace(chr(10), " ")
        tvg_id = str(entry.get("tvg_id", "")).replace("|", "\\|")
        asset = Path(urlsplit(str(entry.get("logo", ""))).path).name.replace("|", "%7C")
        reason = str(entry.get("reason", "No source record.")).replace("|", "\\|").replace(chr(10), " ")
        lines.append(f"| {playlist} | {name} | {tvg_id} | {asset} | {reason} |")
    if not review:
        lines.append("| — | — | — | — | No undocumented provenance records. |")
    # Surface one logo asset assigned to multiple distinct channel identities.
    # This is a manual-review signal, not proof that the artwork is incorrect.
    assets = {}
    for entry in entries:
        if entry.get("playlist") != "IPTV-Playlist.m3u":
            continue
        logo = Path(urlsplit(str(entry.get("logo", ""))).path).name.casefold()
        identity = str(entry.get("tvg_id", "")).strip()
        name = str(entry.get("channel_name", "")).strip()
        if logo and identity:
            item = assets.setdefault(logo, {})
            item.setdefault(identity, set()).add(name or identity)
    shared = [(asset, identities) for asset, identities in sorted(assets.items()) if len(identities) > 1]
    lines += [
        "", "## Shared logo assets across distinct channel identities", "",
        "The same local file is referenced by more than one playlist tvg-id below. Review visually; shared artwork can be legitimate for related channel brands and is not automatically wrong.", "",
        "| Local asset | Channel identity | tvg-id |",
        "|---|---|---|",
    ]
    if shared:
        for asset, identities in shared:
            for identity, names in sorted(identities.items()):
                lines.append(f"| {asset} | {', '.join(sorted(names))} | {identity} |")
    else:
        lines.append("| — | No cross-identity logo reuse detected | — |")
    lines += [
        "", "## Review policy", "",
        "- Do not mark an asset verified from channel-name similarity alone.",
        "- Prefer an exact broadcaster-owned source; otherwise record a reliable, attributable third-party source and review notes.",
        "- Keep generated fallback artwork labelled as unofficial until a genuine logo is verified.",
        "- Verify this report against the current playlist hashes before acting on it.", "",
    ]
    return "\n".join(lines)


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    hashes = {}
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.is_file():
            raise SystemExit(f"Logo provenance review requires {playlist}")
        hashes[playlist] = hashlib.sha256(path.read_bytes()).hexdigest()
    for playlist, digest in hashes.items():
        known = manifest.get("source_sha256_by_playlist", {}).get(playlist)
        if known != digest:
            raise SystemExit(f"Logo authenticity manifest is stale for {playlist}; regenerate it first.")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_report(manifest, hashes), encoding="utf-8")
    print(f"Logo provenance review generated; needs-review entries: {sum(1 for item in manifest.get('entries', []) if item.get('status') == 'needs_review')}")


if __name__ == "__main__":
    main()
