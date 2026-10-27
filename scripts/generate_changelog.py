#!/usr/bin/env python3
"""Generate a non-destructive changelog for all maintained playlist files."""
from __future__ import annotations

import json
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAYLISTS = (
    "IPTV-Playlist.m3u",
    "BDIX-Playlist.m3u",
    "International-Playlist.m3u",
)
STATE = ROOT / "reports/changelog-state.json"
DOC_CHANGELOG = ROOT / "docs/CHANGELOG.md"
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
BACKUP_GROUPS = {"backup", "new backup"}


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def split_extinf(line: str) -> tuple[str, str]:
    in_quote = False
    escaped = False
    for i, ch in enumerate(line):
        if ch == '"' and not escaped:
            in_quote = not in_quote
        elif ch == "," and not in_quote:
            return line[:i], line[i + 1:]
        escaped = ch == "\\" and not escaped
        if ch != "\\":
            escaped = False
    return line, ""


def parse(text: str) -> list[dict[str, str]]:
    lines = text.replace("\r", "").splitlines()
    rows: list[dict[str, str]] = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            continue
        url = lines[j].strip()
        if not url.startswith(("http://", "https://")):
            continue
        prefix, display_name = split_extinf(line)
        metadata = attrs(prefix)
        rows.append({
            "id": (metadata.get("tvg-id") or metadata.get("channel-id") or "").strip(),
            "name": (metadata.get("tvg-name") or display_name).strip(),
            "group": (metadata.get("group-title") or "").strip(),
            "logo": (metadata.get("tvg-logo") or "").strip(),
            "url": url,
        })
    return rows


def identity(row: dict[str, str]) -> str:
    value = row["id"].casefold().strip()
    return value or row["name"].casefold().strip()


def git_text(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
    ).strip()


def current_playlist_commit(path: str) -> str:
    try:
        return git_text("log", "-1", "--format=%H", "--", path)
    except (subprocess.CalledProcessError, OSError):
        return ""


def playlist_at_commit(commit: str, path: str) -> str | None:
    try:
        return git_text("show", f"{commit}:{path}")
    except (subprocess.CalledProcessError, OSError):
        return None


def compare(previous: str, current: str) -> dict[str, object]:
    old = parse(previous)
    new = parse(current)
    old_urls = {row["url"] for row in old}
    new_urls = {row["url"] for row in new}
    added = [row for row in new if row["url"] not in old_urls]
    removed = [row for row in old if row["url"] not in new_urls]

    old_ids = {identity(row) for row in old if identity(row)}
    new_ids = {identity(row) for row in new if identity(row)}
    added_channels = [
        row for row in added
        if identity(row) and identity(row) not in old_ids
        and row["group"].casefold() not in BACKUP_GROUPS
    ]
    removed_channels = [
        row for row in removed
        if identity(row) and identity(row) not in new_ids
        and row["group"].casefold() not in BACKUP_GROUPS
    ]

    old_logo = {(identity(row), row["url"]): row["logo"] for row in old}
    new_logo = {(identity(row), row["url"]): row["logo"] for row in new}
    logo_changes = sum(
        1 for key, value in new_logo.items()
        if key in old_logo and old_logo[key] != value
    )
    replaced_ids = {
        identity(row) for row in added if identity(row)
    } & {
        identity(row) for row in removed if identity(row)
    }
    backup_updates = sum(
        1 for row in added
        if row["group"].casefold() in BACKUP_GROUPS
        and any(
            old_row["url"] in {item["url"] for item in removed}
            and identity(old_row) == identity(row)
            and old_row["group"].casefold() in BACKUP_GROUPS
            for old_row in old
        )
    )
    duplicate_urls_removed = max(
        0, (len(old) - len(old_urls)) - (len(new) - len(new_urls))
    )

    return {
        "added_urls": len(added),
        "removed_urls": len(removed),
        "added_channels": len(added_channels),
        "removed_channels": len(removed_channels),
        "backup_updates": backup_updates,
        "logo_changes": logo_changes,
        "replaced_identities": len(replaced_ids),
        "duplicate_urls_removed": duplicate_urls_removed,
        "added_names": list(dict.fromkeys(row["name"] for row in added_channels if row["name"]))[:10],
        "removed_names": list(dict.fromkeys(row["name"] for row in removed_channels if row["name"]))[:10],
    }


def has_changes(summary: dict[str, object]) -> bool:
    return any(
        int(summary.get(key, 0))
        for key in (
            "added_urls", "removed_urls", "added_channels", "removed_channels",
            "backup_updates", "logo_changes", "replaced_identities",
            "duplicate_urls_removed",
        )
    )


def render_entry(date: str, playlist: str, summary: dict[str, object]) -> str:
    marker = f"<!-- playlist-changelog:{playlist} -->"
    lines = [
        marker,
        f"### {date} — `{playlist}`",
        "",
        f"- New channel identities: **{summary['added_channels']}**",
        f"- Channel identities removed: **{summary['removed_channels']}**",
        f"- Stream URLs added / removed: **{summary['added_urls']} / {summary['removed_urls']}**",
        f"- Backup URL updates: **{summary['backup_updates']}**",
        f"- Logo reference changes: **{summary['logo_changes']}**",
        f"- Replaced channel identities: **{summary['replaced_identities']}**",
        f"- Duplicate URL occurrences removed: **{summary['duplicate_urls_removed']}**",
    ]
    if summary["added_names"]:
        lines.extend(["", "Added channel identities (up to 10):"])
        lines.extend(f"- {name}" for name in summary["added_names"])
    if summary["removed_names"]:
        lines.extend(["", "Removed channel identities (up to 10):"])
        lines.extend(f"- {name}" for name in summary["removed_names"])
    return "\n".join(lines)


def insert_unreleased(existing: str, entries: list[tuple[str, str]]) -> str:
    if "## [Unreleased]" not in existing:
        lines = existing.splitlines()
        if lines and lines[0].startswith("# "):
            lines[1:1] = ["", "## [Unreleased]", ""]
            existing = "\n".join(lines).rstrip() + "\n"
        else:
            existing = "# Changelog\n\n## [Unreleased]\n\n" + existing.lstrip()

    marker_header = "## [Unreleased]"
    start = existing.index(marker_header)
    content_start = start + len(marker_header)
    next_h2 = re.search(r"(?m)^## (?!\[Unreleased\]).*$", existing[content_start:])
    end = content_start + next_h2.start() if next_h2 else len(existing)
    prefix, body, suffix = existing[:content_start], existing[content_start:end], existing[end:]

    for marker, entry in entries:
        if marker in body:
            marker_pos = body.index(marker)
            next_marker = re.search(r"(?m)^<!-- playlist-changelog:", body[marker_pos + len(marker):])
            stop = marker_pos + len(marker) + next_marker.start() if next_marker else len(body)
            body = body[:marker_pos] + entry + "\n\n" + body[stop:].lstrip("\n")
        else:
            body = body.rstrip() + "\n\n" + entry + "\n"

    return prefix + body + suffix


def main() -> None:
    try:
        state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}
    except (json.JSONDecodeError, OSError):
        state = {}

    stored = state.get("playlists", {})
    if not isinstance(stored, dict):
        stored = {}
    entries: list[tuple[str, str]] = []
    new_state: dict[str, object] = {"schema_version": 2, "playlists": {}}
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for playlist in PLAYLISTS:
        path = ROOT / playlist
        if not path.is_file():
            continue
        current = path.read_text(encoding="utf-8-sig")
        current_commit = current_playlist_commit(playlist)
        if not current_commit:
            continue

        saved = stored.get(playlist, {})
        previous_commit = saved.get("commit", "") if isinstance(saved, dict) else ""
        if not previous_commit and playlist == "IPTV-Playlist.m3u":
            # Read the original single-playlist state format during migration.
            previous_commit = str(state.get("playlist_commit", "") or "")

        previous = playlist_at_commit(previous_commit, playlist) if previous_commit else None
        if previous is not None and previous_commit != current_commit:
            summary = compare(previous, current)
            if has_changes(summary):
                entry = render_entry(date, playlist, summary)
                entries.append((f"<!-- playlist-changelog:{playlist} -->", entry))

        new_state["playlists"][playlist] = {"commit": current_commit}

    state_changed = new_state != {
        "schema_version": state.get("schema_version"),
        "playlists": stored,
    }
    if entries:
        existing = DOC_CHANGELOG.read_text(encoding="utf-8") if DOC_CHANGELOG.exists() else "# Changelog\n"
        updated = insert_unreleased(existing, entries)
        DOC_CHANGELOG.write_text(updated.rstrip() + "\n", encoding="utf-8")
        print(f"Updated changelog for {len(entries)} playlist(s).")
    else:
        print("No meaningful playlist changes detected.")

    if state_changed:
        new_state["generated"] = datetime.now(timezone.utc).isoformat()
        STATE.write_text(json.dumps(new_state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Updated per-playlist changelog state.")


if __name__ == "__main__":
    main()
