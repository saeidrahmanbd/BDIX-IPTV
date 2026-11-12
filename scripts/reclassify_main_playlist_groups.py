#!/usr/bin/env python3
"""Correct only evidence-backed primary groups in the owner-curated IPTV playlist.

This pass never deletes/replaces stream URLs and never reclassifies Backup,
Review, discovery queues or Adult. It changes only group-title for verified
Bangladesh/India rows. Existing manual queues remain under owner control.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import country_verification
import discover_bd_in_new_queues as bd_policy

PLAYLIST = Path("IPTV-Playlist.m3u")
INTERNATIONAL = Path("International-Playlist.m3u")
REPORT = Path("reports/iptv-grouping-corrections.md")
APPROVALS = Path("/tmp/iptv-owner-requested-migrations.json")

ACTIVE_GROUPS = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
PROTECTED_GROUPS = {
    "Backup", "Review", "Not Playing", "New Channels", "New Backups", "Adult",
}
GENRE_GROUPS = {"Kids", "Sports", "Religious", "Documentary & Wildlife"}
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
KIDS_RE = re.compile(r"\b(kids?|cartoon|pogo|nick(?:elodeon)?|disney\s*(?:jr|junior)|hungama|baby\s*tv|discovery\s*kids|toon)\b", re.I)
SPORTS_RE = re.compile(r"\b(sports?|cricket|football|soccer|wrestling|boxing|ufc|espn|ten\s*sports|sony\s*sports|star\s*sports|bein\s*sports|willow)\b", re.I)
MOVIE_RE = re.compile(r"\b(movie|movies|cinema|film|films|bollywood|hollywood|pictures|cineplex|plex)\b", re.I)
MUSIC_RE = re.compile(r"\b(music|mtv|vh1|9xm|mastiii|sangeet|vevo|music\s*box)\b", re.I)
BANGLA_RE = re.compile(r"\b(bangla|bengali|kolkata)\b", re.I)


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR.findall(info))


def split_info(info: str) -> tuple[str, str]:
    quoted = False
    for index, char in enumerate(info):
        if char == '"':
            quoted = not quoted
        elif char == "," and not quoted:
            return info[:index], info[index:]
    return info, ""


def set_group(info: str, target: str) -> str:
    pattern = re.compile(r'(\bgroup-title=")[^"]*(")')
    if pattern.search(info):
        return pattern.sub(lambda match: match.group(1) + target + match.group(2), info, count=1)
    head, display = split_info(info)
    return head.rstrip() + f' group-title="{target}"' + display


def parse_playlist(text: str):
    preamble, blocks, current = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return preamble, blocks


def stream_url(block: list[str]) -> str:
    return next((line.strip() for line in block[1:] if line.strip().startswith(("http://", "https://"))), "")


# Verified channel-specific genre corrections for Indian services.
CHANNEL_GROUP_OVERRIDES = {
    "aaryaatv.in": "Indian Music",
    "nammabangalore.in@sd": "Indian Entertainment",
    "pitaara.in@sd": "Indian Entertainment",
    "pitaaracomedy.in@sd": "Indian Entertainment",
}

def genre_target(a: dict[str, str], name: str, current: str, country: str) -> str:
    content = a.get("tvg-content", "").casefold()
    evidence = " ".join((name, a.get("tvg-name", ""), a.get("tvg-id", ""), a.get("channel-id", ""), content))
    if country == "IN":
        language_tags = {part.strip().casefold() for part in a.get("tvg-language", "").split(";")}
        # Language-first policy: Bengali Indian channels stay in Indian Bangla,
        # including Bengali movie and music services.
        if language_tags.intersection({"ben", "bn", "bengali", "beng"}) or BANGLA_RE.search(evidence):
            return "Indian Bangla"
    if current in GENRE_GROUPS:
        return current
    if content == "kids" or KIDS_RE.search(evidence):
        return "Kids"
    if content in {"sports", "sport"} or SPORTS_RE.search(evidence):
        return "Sports"
    if country == "IN":
        if content in {"movies", "movie", "film"} or MOVIE_RE.search(evidence):
            return "Indian Movies"
        if content in {"music", "musics"} or MUSIC_RE.search(evidence):
            return "Indian Music"
        return "Indian Entertainment"
    return "Bangladesh"


def target_group(a: dict[str, str], name: str, current: str, reference) -> tuple[str | None, str]:
    verdict = country_verification.verify_country(a, name, reference)
    if not verdict.ok:
        return None, verdict.reason or "country not conclusively verified"
    country = verdict.country
    if country == "IN":
        prohibited = bd_policy.prohibited_channel(a, name, "IN", discovery=True)
        if prohibited:
            return None, f"policy-excluded: {prohibited}; retained in the current group because Review is reserved for streams that do not currently work"
        identity = (a.get("tvg-id") or a.get("channel-id") or "").strip().casefold()
        override = CHANNEL_GROUP_OVERRIDES.get(identity)
        if override:
            return override, "verified channel-specific category mapping"
    return genre_target(a, name, current, country), verdict.basis


def main() -> int:
    if not PLAYLIST.is_file():
        raise SystemExit("IPTV-Playlist.m3u is missing; refusing to create it.")
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    preamble, blocks = parse_playlist(original)
    reference = country_verification.reference_from_playlists([PLAYLIST, INTERNATIONAL])
    changed = []
    approvals = []
    skipped = Counter()
    output = []

    for block in blocks:
        if not block or not block[0].startswith("#EXTINF:"):
            output.append(block)
            continue
        info = block[0]
        a = attrs(info)
        current = a.get("group-title", "").strip()
        if current in PROTECTED_GROUPS or current not in ACTIVE_GROUPS:
            output.append(block)
            continue
        url = stream_url(block)
        if not url:
            skipped["missing HTTP(S) stream URL"] += 1
            output.append(block)
            continue
        display = split_info(info)[1].lstrip(",").strip()
        name = (a.get("tvg-name") or display).strip()
        target, evidence = target_group(a, name, current, reference)
        if target is None:
            skipped[evidence] += 1
            output.append(block)
            continue
        if target != current:
            old = current
            block[0] = set_group(info, target)
            approvals.append({"url": url, "source_group": old, "target_group": target, "allow_metadata": True})
            changed.append((name, old, target, evidence))
        output.append(block)

    updated = "\n".join(preamble + [line for block in output for line in block]).rstrip() + "\n"
    if updated != original:
        PLAYLIST.write_text(updated, encoding="utf-8")
    if approvals:
        prior = []
        if APPROVALS.is_file():
            try:
                prior = json.loads(APPROVALS.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                prior = []
        by_key = {}
        for item in prior + approvals:
            by_key[(item.get("url"), item.get("source_group"), item.get("target_group"))] = item
        APPROVALS.write_text(json.dumps(list(by_key.values()), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# IPTV Primary Grouping Corrections", "",
        f"- Verified primary rows reclassified: **{len(changed)}**",
        f"- Existing stream URLs deleted/replaced: **0** (not permitted by this script)",
        f"- Rows skipped because country was not conclusively verified: **{sum(skipped.values())}**",
        "- Backup, Review, New Channels, New Backups and Adult rows are outside this pass.",
        "- Policy-excluded rows remain in their current group for owner inspection; Review is reserved for streams that do not currently work.", "",
        "| Channel | Previous group | Corrected group | Evidence |",
        "|---|---|---|---|",
    ]
    lines.extend(
        f"| {name.replace('|', '/')} | {old} | {new} | {evidence} |"
        for name, old, new, evidence in changed
    )
    if not changed:
        lines.append("| — | — | — | No verified grouping corrections required |")
    if skipped:
        lines += ["", "## Skipped rows", ""]
        lines.extend(f"- {reason}: {count}" for reason, count in sorted(skipped.items()))
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"IPTV grouping: changed={len(changed)} skipped_unverified={sum(skipped.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
