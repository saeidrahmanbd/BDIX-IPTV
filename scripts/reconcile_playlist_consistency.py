#!/usr/bin/env python3
"""Normalize IPTV identity metadata without deleting distinct stream URLs."""
from collections import defaultdict
from pathlib import Path
import re

P = Path("IPTV-Playlist.m3u")
ACTIVE = {"Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports"}
REVIEW_PRIORITY = {"New Channels": 3, "New Backup": 2, "Not Playing": 1}
REVIEW = set(REVIEW_PRIORITY)
ATTR = re.compile(r'([\w-]+)="([^"]*)"')
RAW_TAG = re.compile(r"\s*(?:\[[^]]*(?:geo[- ]?blocked)[^]]*\]|\((?:\d{3,4}[pi]|UHD|FHD|HD\+?|SD)\)|\s+(?:\d{3,4}[pi]))\s*$", re.I)
ALIASES = {"disney channel india": "Disney Channel India", "disney channel (india)": "Disney Channel India", "gazi tv": "G TV", "g tv": "G TV", "nick": "Nickelodeon (India)", "nickelodeon (india)": "Nickelodeon (India)"}

def attrs(line):
    return dict(ATTR.findall(line))

def set_attr(line, key, value):
    pattern = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pattern.search(line):
        return pattern.sub(f'{key}="{value}"', line, count=1)
    return line.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)

def split_extinf(line):
    quoted = False
    escaped = False
    for i, ch in enumerate(line):
        if ch == '"' and not escaped:
            quoted = not quoted
        elif ch == "," and not quoted:
            return line[:i], line[i + 1:]
        escaped = ch == "\\" and not escaped
        if ch != "\\":
            escaped = False
    return line, ""

def clean_name(value):
    value = RAW_TAG.sub("", str(value or "").strip())
    value = re.sub(r"\s+", " ", value).strip()
    return ALIASES.get(value.casefold(), value)

def identity_key(value):
    return clean_name(value).casefold()

def main():
    original = P.read_text(encoding="utf-8-sig")
    lines = original.replace("\r", "").splitlines()
    records = []
    current = None
    for idx, line in enumerate(lines):
        if line.startswith("#EXTINF:"):
            current = {"info_idx": idx, "attrs": attrs(line)}
        elif current and line.strip().startswith(("http://", "https://")):
            current["url_idx"] = idx
            current["url"] = line.strip()
            records.append(current)
            current = None
    ids_by_name = defaultdict(set)
    active_urls = set()
    for row in records:
        a = row["attrs"]
        group = a.get("group-title", "").strip()
        name = identity_key(a.get("tvg-name", ""))
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
        if group in ACTIVE:
            if cid and name:
                ids_by_name[name].add(cid)
            active_urls.add(row["url"].casefold())
    canonical_ids = {name: next(iter(ids)) for name, ids in ids_by_name.items() if len(ids) == 1}
    removed_lines, review_url_kept = set(), {}
    changed = 0
    for row in records:
        info = lines[row["info_idx"]]
        prefix, display = split_extinf(info)
        a = attrs(info)
        group = a.get("group-title", "").strip()
        old_name = a.get("tvg-name", "").strip()
        clean_tvg_name = clean_name(old_name)
        clean_display = clean_name(display)
        if clean_tvg_name != old_name:
            prefix = set_attr(prefix, "tvg-name", clean_tvg_name)
            changed += 1
        if clean_display != display.strip():
            display = clean_display
            changed += 1
        info = prefix + ("," + display if display else "")
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
        canonical = canonical_ids.get(identity_key(clean_tvg_name))
        if group in REVIEW and canonical and cid and cid.casefold() != canonical.casefold():
            info = set_attr(info, "tvg-id", canonical)
            if 'channel-id="' in info:
                info = set_attr(info, "channel-id", canonical)
            changed += 1
        url_key = row["url"].casefold()
        if group in REVIEW and url_key in active_urls:
            removed_lines.update({row["info_idx"], row["url_idx"]})
            continue
        if group in REVIEW:
            previous = review_url_kept.get(url_key)
            if previous:
                prior_group, prior_info_idx, prior_url_idx = previous
                if REVIEW_PRIORITY.get(group, 0) <= REVIEW_PRIORITY.get(prior_group, 0):
                    removed_lines.update({row["info_idx"], row["url_idx"]})
                    continue
                removed_lines.update({prior_info_idx, prior_url_idx})
            review_url_kept[url_key] = (group, row["info_idx"], row["url_idx"])
        lines[row["info_idx"]] = info
    if removed_lines:
        lines = [line for idx, line in enumerate(lines) if idx not in removed_lines]
    updated = "\n".join(lines).rstrip("\n") + "\n"
    if updated != original:
        P.write_text(updated, encoding="utf-8")
    print(f"Consistency repair: metadata changes={changed}; exact duplicate review lines removed={len(removed_lines)}; distinct stream URLs preserved.")

if __name__ == "__main__":
    main()
