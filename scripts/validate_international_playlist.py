#!/usr/bin/env python3
"""Validate International playlist structure, attribution, categories and local logo paths."""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import discover_international_channels as discovery

PLAYLIST = Path("International-Playlist.m3u")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
FIXED = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani"]
TAIL = ["Fashion TV", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Adult", "Review", "New Channels", "New Backups", "Backup"]
FORBIDDEN = {"international movies", "international music", "backups", "not playing", "test"}
ATTRIBUTION = [
    "#=================================",
    "# Developed by: SAEID RAHMAN",
    "# Facebook: https://www.facebook.com/saeid.rahman.sr",
    "# Email: saeidrahman.mkt@gmail.com",
    "#=================================",
]


def attrs(line):
    return dict(ATTR_RE.findall(line))


def normalized_stream_url(url):
    """Normalize scheme/host only; URL paths and queries are case-sensitive."""
    parsed = urlsplit(url.strip())
    return (
        parsed.scheme.casefold(),
        parsed.netloc.casefold(),
        parsed.path,
        parsed.query,
        parsed.fragment,
    )


def foreign_movie_music_error(a, name, country_code):
    """Return a policy error unless a foreign primary row is explicitly Movies/Music."""
    code = str(country_code or "").strip().upper()
    if code in {"BD", "IN", "PK"}:
        return ""
    policy_attrs = dict(a)
    # Country-group labels are authoritative for the country. Reuse the same
    # canonical discovery policy used by International candidates and legacy rows.
    policy_attrs["group-title"] = "International"
    policy_attrs["tvg-country"] = code
    target, reason, verified_code = discovery.policy(
        policy_attrs, name, allow_legacy_group=True
    )
    if target is None:
        return reason or "not eligible under the foreign Movies/Music-only policy"
    if verified_code != code:
        return f"country identity mismatch (expected {code}, verified {verified_code})"
    genre = discovery.infer_genre(policy_attrs, name)
    if genre not in {"Movies", "Music"}:
        return "not a dedicated Movies/Music channel"
    expected_target = "Pakistani" if code == "PK" else (
        "International Movies" if genre == "Movies" else "International Music"
    )
    if target != expected_target:
        return f"expected policy group {expected_target}, got {target}"
    declared = (a.get("tvg-content") or "").strip().casefold()
    if declared != genre.casefold():
        return f"tvg-content must explicitly be {genre}"
    return ""


GENRE_GROUPS_WITH_FOREIGN_RESTRICTIONS = {
    "documentary & wildlife", "kids", "religious", "sports",
}


def genre_group_policy_error(a, name, group):
    """Keep foreign genre groups out of active categories; preserve BD and allowed Indian groups."""
    group_key = str(group or "").strip().casefold()
    if group_key not in GENRE_GROUPS_WITH_FOREIGN_RESTRICTIONS:
        return ""

    code = discovery.country_code(a)
    if code not in discovery.ISO_CODES:
        # Unknown country metadata is reported by the metadata audit; do not
        # guess a territory or reject an otherwise protected legacy row here.
        return ""
    if code not in {"BD", "IN", "PK"}:
        return f"foreign channels are not permitted in the {group} genre group"
    if code == "IN" and group_key == "religious":
        _target, reason, _verified = discovery.policy(a, name)
        return reason or "Indian religious channels are prohibited"
    # Bangladesh is unrestricted. Indian Kids and Sports are explicitly allowed.
    return ""


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("International playlist is missing.")
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    if not lines or not lines[0].startswith("#EXTM3U"):
        raise SystemExit("Missing #EXTM3U as the first line.")
    if lines[1:1 + len(ATTRIBUTION)] != ATTRIBUTION:
        raise SystemExit("Required attribution block is missing or not immediately after #EXTM3U.")
    if sum(line == ATTRIBUTION[1] for line in lines) != 1:
        raise SystemExit("Attribution block must appear exactly once.")

    registries = [line for line in lines if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    if len(registries) != 1:
        raise SystemExit(f"Expected one category registry; found {len(registries)}.")
    try:
        registry = json.loads(registries[0].split(":", 1)[1])
    except Exception as exc:
        raise SystemExit(f"Invalid category registry JSON: {exc}")
    if not isinstance(registry, list) or len(registry) != len(set(registry)):
        raise SystemExit("Category registry must be a JSON list of unique names.")

    blocks, current = [], None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)
    if not blocks:
        raise SystemExit("Playlist contains no channel entries.")

    urls, groups_seen, group_set = [], [], set()
    missing_logos, broken_logos = 0, []
    country_group_labels = {discovery.country_group(code).casefold(): code
                            for code in discovery.ISO_CODES if code not in {"BD", "IN", "PK"}}
    for block in blocks:
        info = block[0]
        a = attrs(info)
        name = (a.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()
        group = a.get("group-title", "").strip()
        if group.casefold() in FORBIDDEN:
            raise SystemExit(f"Forbidden legacy/catch-all group remains: {group!r} ({name}).")
        group_key = group.casefold()
        # A dedicated country-group label is itself reliable country evidence.
        # Fall back to it when optional tvg-country/tvg-id metadata is incomplete.
        # The explicit country-group label is authoritative when optional metadata is incomplete or inconsistent.
        code = country_group_labels.get(group_key)
        if code is None:
            code = discovery.country_code(a)
        if group_key == "fashion tv":
            if not discovery.FASHION_RE.search(name):
                raise SystemExit(f"Invalid Fashion TV exception entry: {name!r}.")
        elif group_key in country_group_labels or group_key == "pakistani":
            # Dedicated country labels are checked against the country-specific policy;
            # Bangladesh, India and Pakistan are exempt from the general Movies/Music-only rule.
            code = country_group_labels.get(group_key, "PK")
            reason = foreign_movie_music_error(a, name, code)
            if reason:
                raise SystemExit(
                    f"Foreign country group violates Movies/Music policy: {name!r} in {group!r} ({reason})."
                )
        if group_key in {"international", "new channels", "new backup", "new backups"}:
            target, reason, code = discovery.policy(a, name, allow_legacy_group=(group_key == "international"))
            if target is None:
                raise SystemExit(f"Channel violates country/content policy in {group}: {name!r} ({reason or 'not eligible'}).")
            if code not in {"BD", "IN", "PK"}:
                content = (a.get("tvg-content") or "").strip().casefold()
                if content not in {"movies", "movie", "music", "musics"}:
                    raise SystemExit(f"Non-Bangladesh/India/Pakistan review entry is not tagged Movies/Music: {name!r} in {group!r}.")
        genre_issue = genre_group_policy_error(a, name, group)
        if genre_issue:
            raise SystemExit(
                f"Channel violates country/content policy in genre group {group!r}: "
                f"{name!r} ({genre_issue})."
            )

        if group and group not in group_set:
            group_set.add(group)
            groups_seen.append(group)

        stream_rows = [
            line.strip() for line in block[1:]
            if line.strip().startswith(("http://", "https://"))
        ]
        if len(stream_rows) != 1:
            raise SystemExit(f"Expected exactly one URL row for {name!r}; found {len(stream_rows)}.")
        urls.append(normalized_stream_url(stream_rows[0]))

        logo = a.get("tvg-logo", "").strip()
        if not logo:
            missing_logos += 1
            if group_key in {"new channels", "new backup", "new backups"}:
                raise SystemExit(f"Manual-review candidate lacks a local logo: {name!r} in {group!r}.")
            continue
        if logo.startswith(RAW_BASE):
            rel = unquote(urlsplit(logo).path.split("/main/logos/", 1)[-1]).lstrip("/")
            target = (LOGOS / rel).resolve()
        elif logo.startswith("logos/"):
            rel = unquote(logo.split("?", 1)[0].split("#", 1)[0])
            target = Path(rel).resolve()
        else:
            raise SystemExit(f"External or unsupported logo reference for {name!r}: {logo}")
        root = LOGOS.resolve()
        if root not in target.parents or not target.is_file():
            broken_logos.append((name, logo))

    duplicates = [url for url, count in Counter(urls).items() if count > 1]
    if duplicates:
        raise SystemExit(f"Duplicate stream URL records: {len(duplicates)}.")
    if broken_logos:
        sample = "; ".join(f"{name}: {path}" for name, path in broken_logos[:5])
        raise SystemExit(f"Broken local logo references: {len(broken_logos)}. Examples: {sample}")

    threshold_issues = discovery.country_group_threshold_issues(blocks)
    if threshold_issues:
        raise SystemExit("Country-group threshold policy failed: " + " | ".join(threshold_issues))

    if registry[-3:] != ["New Channels", "New Backups", "Backup"]:
        raise SystemExit("The final categories must be New Channels, New Backups, Backup.")
    dynamic = sorted(group for group in group_set if group not in FIXED and group not in TAIL and group.casefold() != "international")
    international_bucket = ["International"] if any(group.casefold() == "international" for group in group_set) else []
    expected_registry = FIXED + dynamic + international_bucket + TAIL
    if registry != expected_registry:
        raise SystemExit(f"Category registry mismatch. Expected {expected_registry}; got {registry}.")
    expected_present_order = [group for group in expected_registry if group in group_set]
    if groups_seen != expected_present_order:
        raise SystemExit(f"Playlist category order mismatch. Expected {expected_present_order}; got {groups_seen}.")

    print(
        f"International structure OK: {len(blocks)} entries, 0 duplicate URLs, "
        f"0 broken/external logo references, {missing_logos} entries without logos. "
        "Playback was not tested."
    )


if __name__ == "__main__":
    main()
