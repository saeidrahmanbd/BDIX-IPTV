#!/usr/bin/env python3
"""Deterministic deep cleanup for IPTV-Playlist.m3u only.

Never edits BDIX-Playlist.m3u. Never removes a stream merely because a health
probe is temporarily failing.
"""
from pathlib import Path
import re
import unicodedata

P = Path("IPTV-Playlist.m3u")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NO_NUMBER = {"Backup", "New Backup", "Not Playing"}


def attrs(s):
    return dict(ATTR_RE.findall(s))


def set_attr(s, key, value):
    pat = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pat.search(s):
        return pat.sub(f'{key}="{value}"', s, count=1)
    return s.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)


def remove_attr(s, key):
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", s, count=1)


def split_display(s):
    quoted = False
    for i, ch in enumerate(s):
        if ch == '"':
            quoted = not quoted
        elif ch == ',' and not quoted:
            return s[:i], s[i + 1:].strip()
    return s, ""


def set_display(s, name):
    return split_display(s)[0] + "," + name


def slug(value):
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", ".", value.casefold()).strip(".")


def name_of(info):
    a = attrs(info)
    return (a.get("tvg-name") or split_display(info)[1]).strip()


def url_of(block):
    for line in block[1:]:
        x = line.strip()
        if x.startswith(("http://", "https://")):
            return x
    return ""


def parse(text):
    pre, blocks, current = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is None:
            pre.append(line)
        else:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return pre, blocks


def normalize_identity(info):
    a = attrs(info)
    name = name_of(info)
    tvg = a.get("tvg-id", "").strip()
    cid = a.get("channel-id", "").strip()
    if tvg.casefold().startswith("staging."):
        tvg = "custom." + slug(name)
        info = set_attr(info, "tvg-id", tvg)
    if cid.casefold().startswith("staging."):
        cid = tvg or ("custom." + slug(name))
        info = set_attr(info, "channel-id", cid)
    if not tvg and cid:
        info = set_attr(info, "tvg-id", cid)
    if not cid and tvg:
        info = set_attr(info, "channel-id", tvg)
    if not tvg and not cid and name:
        cid = "custom." + slug(name)
        info = set_attr(info, "tvg-id", cid)
        info = set_attr(info, "channel-id", cid)
    if not attrs(info).get("tvg-name", "").strip() and name:
        info = set_attr(info, "tvg-name", name)
    if attrs(info).get("tvg-name", "").strip() and not split_display(info)[1]:
        info = set_display(info, attrs(info)["tvg-name"].strip())
    return info


def main():
    if not P.exists():
        return
    pre, blocks = parse(P.read_text(encoding="utf-8-sig"))
    out = []
    seen_urls = set()
    removed = 0
    changed = 0

    category_fixes = {
        "baiscope tv": "Bangladesh",
        "atn music": "Bangladesh",
    }
    wrong_name_urls = {
        "/api/play/filamchi.m3u8": ("Filamchi", "custom.filamchi"),
        "/api/play/manoranjan%20grand.m3u8": ("Manoranjan Grand", "custom.manoranjan.grand"),
    }
    bad_fragments = ("tvsen5.aynaott.com/tK2BNdfsdfsdf/index.m3u8",)

    for block in blocks:
        info = normalize_identity(block[0])
        url = url_of(block)
        a = attrs(info)
        lname = name_of(info).casefold()
        lowurl = url.casefold()

        if any(x.casefold() in lowurl for x in bad_fragments):
            removed += 1
            continue
        if re.search(r"^https?://(?:[^/]+\.)?dvltv\.cc(?::\d+)?/play(?:/|$)", url, re.I):
            removed += 1
            continue
        if re.search(r"https?://[^/]*vods?\d*\.[^/]+/", url, re.I) or re.search(r"/vod(?:/|$)", url, re.I):
            removed += 1
            continue
        if re.search(r"[?&](?:token|auth)=(?:test|testpub)(?:&|$)", url, re.I):
            removed += 1
            continue
        if re.search(r"https?://[^/@]+@[^/]+", url, re.I):
            removed += 1
            continue

        if lname in category_fixes and a.get("group-title", "").strip() != category_fixes[lname]:
            info = set_attr(info, "group-title", category_fixes[lname])
            changed += 1

        for fragment, (new_name, new_id) in wrong_name_urls.items():
            if fragment in lowurl and name_of(info).casefold() == "b4u movies":
                info = set_attr(info, "tvg-name", new_name)
                info = set_attr(info, "tvg-id", new_id)
                info = set_attr(info, "channel-id", new_id)
                info = set_attr(info, "group-title", "Backup")
                info = remove_attr(info, "tvg-chno")
                info = set_display(info, new_name)
                changed += 1
                break

        if attrs(info).get("group-title", "").strip() in NO_NUMBER:
            info = remove_attr(info, "tvg-chno")

        url_key = url.strip().casefold()
        if url_key:
            if url_key in seen_urls:
                removed += 1
                continue
            seen_urls.add(url_key)

        block[0] = info
        out.append(block)

    # Preserve existing primary channel numbers and repair duplicates/missing values.
    used = set()
    for block in out:
        a = attrs(block[0])
        if a.get("group-title", "").strip() in NO_NUMBER:
            continue
        n = a.get("tvg-chno", "").strip()
        if n.isdigit() and int(n) > 0:
            used.add(int(n))

    next_no = max(used or {0}) + 1
    seen_primary = set()
    for block in out:
        info = block[0]
        a = attrs(info)
        if a.get("group-title", "").strip() in NO_NUMBER:
            block[0] = remove_attr(info, "tvg-chno")
            continue
        n = a.get("tvg-chno", "").strip()
        if n.isdigit() and int(n) > 0 and int(n) not in seen_primary:
            seen_primary.add(int(n))
            continue
        while next_no in used:
            next_no += 1
        block[0] = set_attr(info, "tvg-chno", str(next_no))
        used.add(next_no)
        seen_primary.add(next_no)
        next_no += 1
        changed += 1

    lines = list(pre)
    for block in out:
        lines.extend(block)
    P.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Deep IPTV audit repair: changed={changed} removed={removed} remaining={len(out)}")


if __name__ == "__main__":
    main()
