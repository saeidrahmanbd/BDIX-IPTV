#!/usr/bin/env python3
"""Discover conservative new Bangladesh/India live channels and backups.

Policy:
- Bangladesh: eligible except sports/religious/kids.
- India: Music/Movie only.
- Non-Bangladeshi news is rejected.
- Existing name+URL pairs are skipped.
- Existing channel name + new URL becomes New Backup.
- A completely new channel gets one New Channels entry; additional streams
  for that same new channel become New Backup.
- Strictly reject query-string/tokenized URLs, proxy/VOD/test/demo/radio/event
  style streams and non-HLS/TS URLs.
"""
from __future__ import annotations
import json, re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/channel-discovery.md")
SOURCES = [
    ("Bangladesh", "https://iptv-org.github.io/iptv/countries/bd.m3u"),
    ("India", "https://iptv-org.github.io/iptv/countries/in.m3u"),
]
BLOCKED_CATEGORIES = {"sports", "religious", "kids", "news", "radio", "xxx"}
INDIA_ALLOWED = {"music", "movies", "movie"}
BLOCKED_WORDS = re.compile(
    r"(?i)\\b(?:vod|video[ _-]?on[ _-]?demand|catch[ _-]?up|test|demo|sample|"
    r"proxy|proxied|cors|webcam|radio|podcast|event|ppv|pay[ _-]?per[ _-]?view|"
    r"24[ _-]?7|timeshift)\\b"
)
BLOCKED_HOST_WORDS = re.compile(r"(?i)(?:proxy|proxied|cors|localhost|127\\.0\\.0\\.1|"
                                 r"workers\\.dev|worker\\.dev|pages\\.dev)")
TOKEN_KEYS = re.compile(r"(?i)(?:token|auth|authorization|hdnts|sig(?:nature)?|expires?|"
                        r"signature|key|session|jwt)=")
LIVE_EXT = re.compile(r"(?i)\\.(?:m3u8|m3u|ts)(?:$|[?#])")

ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(line):
    return dict(ATTR_RE.findall(line))

def norm_name(name):
    name = re.sub(r"\\s+", " ", name.lower()).strip()
    name = re.sub(r"\\s*\\([^)]*\\)\\s*$", "", name)
    name = re.sub(r"\\s*\\[[^]]*\\]\\s*$", "", name)
    return re.sub(r"[^a-z0-9\\u0980-\\u09ff]+", "", name)

def parse(text):
    lines = text.replace("\\r", "").splitlines()
    out = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF"):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            continue
        url = lines[j].strip()
        if not url.startswith(("http://", "https://")):
            continue
        a = attrs(line)
        name = (a.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
        out.append((a, name, url))
    return out

def category_values(a):
    values = set()
    for key in ("group-title", "category", "categories"):
        raw = a.get(key, "")
        values.update(x.strip().lower() for x in re.split(r"[,;|]", raw) if x.strip())
    return values

def eligible(country, a, name, url):
    cats = category_values(a)
    hay = " ".join([name, a.get("tvg-id",""), a.get("group-title",""), a.get("category","")])
    if "sports" in cats or "religious" in cats or "kids" in cats:
        return False, "blocked category"
    if BLOCKED_WORDS.search(hay):
        return False, "blocked channel type/name"
    if country == "India":
        if not (cats & INDIA_ALLOWED):
            return False, "India is restricted to Music/Movie"
        if "news" in cats:
            return False, "Indian news blocked"
    elif "news" in cats:
        # Bangladesh news is explicitly permitted.
        pass
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False, "invalid URL"
    if parsed.query or TOKEN_KEYS.search(url):
        return False, "query/tokenized URL"
    if parsed.fragment:
        return False, "fragment URL"
    if BLOCKED_HOST_WORDS.search(parsed.netloc):
        return False, "proxy/worker host"
    if not LIVE_EXT.search(parsed.path):
        return False, "not a direct live HLS/TS URL"
    if "vod" in parsed.path.lower() or "catchup" in parsed.path.lower():
        return False, "VOD/catch-up path"
    return True, ""

def build_extinf(a, name, group):
    tvg_id = a.get("tvg-id","").strip() or a.get("channel-id","").strip()
    channel_id = a.get("channel-id","").strip() or tvg_id
    if not tvg_id or not channel_id:
        return None
    logo = a.get("tvg-logo","").strip()
    parts = [
        '#EXTINF:-1',
        f'tvg-id="{tvg_id}"',
        f'tvg-name="{name}"',
    ]
    if logo:
        parts.append(f'tvg-logo="{logo}"')
    parts.extend([
        f'channel-id="{channel_id}"',
        f'group-title="{group}"',
    ])
    if a.get("tvg-language","").strip():
        parts.append(f'tvg-language="{a["tvg-language"].strip()}"')
    if a.get("tvg-country","").strip():
        parts.append(f'tvg-country="{a["tvg-country"].strip()}"')
    return " ".join(parts) + "," + name

def main():
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    entries = parse(original)

    existing_pairs = set()
    existing_names = set()
    for a, name, url in entries:
        existing_pairs.add((norm_name(name), url.strip()))
        existing_names.add(norm_name(name))

    candidates = []
    rejected = 0
    seen_pairs = set()
    for country, source in SOURCES:
        req = urllib.request.Request(source, headers={"User-Agent": "BDIX-IPTV-channel-discovery/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                text = response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            print(f"Source failed: {source}: {exc}")
            continue
        for a, name, url in parse(text):
            ok, reason = eligible(country, a, name, url)
            if not ok:
                rejected += 1
                continue
            pair = (norm_name(name), url)
            if pair in existing_pairs or pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            candidates.append((country, a, name, url))

    # Prefer Bangladesh first, then Indian Music/Movie candidates. Keep one
    # primary candidate for a new channel; all additional streams are backups.
    candidates.sort(key=lambda x: (0 if x[0] == "Bangladesh" else 1, norm_name(x[2]), x[3]))

    new_channels = []
    new_backups = []
    planned_names = set(existing_names)
    planned_pairs = set(existing_pairs)

    for country, a, name, url in candidates:
        n = norm_name(name)
        pair = (n, url)
        if pair in planned_pairs:
            continue
        if n in planned_names:
            group = "New Backup"
            new_backups.append((country, a, name, url, "existing channel; new stream"))
        else:
            group = "New Channels"
            new_channels.append((country, a, name, url, "new channel"))
            planned_names.add(n)
        planned_pairs.add(pair)

    # Conservative cap against accidental source explosions.
    new_channels = new_channels[:40]
    new_backups = new_backups[:80]

    additions = []
    for country, a, name, url, reason in new_channels + new_backups:
        extinf = build_extinf(a, name, "New Channels" if reason == "new channel" else "New Backup")
        if extinf:
            additions.extend([extinf, url])

    if additions:
        lines = original.replace("\r", "").splitlines()
        insert_at = next((i for i,l in enumerate(lines) if l.startswith("#EXTINF") and 'group-title="Backup"' in l), len(lines))
        lines[insert_at:insert_at] = additions
        header = next((l for l in lines if l.startswith("#PLAYLIST-STUDIO-CATEGORIES:")), "")
        if header:
            cats = json.loads(header.split(":",1)[1])
            for group in ("New Channels", "New Backup"):
                if group not in cats:
                    idx = cats.index("Backup") if "Backup" in cats else len(cats)
                    cats.insert(idx, group)
            for i,l in enumerate(lines):
                if l.startswith("#PLAYLIST-STUDIO-CATEGORIES:"):
                    lines[i] = "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(cats, ensure_ascii=False)
                    break
        PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# Channel Discovery",
        "",
        "Conservative automatic discovery of eligible Bangladesh and India live channels.",
        "",
        f"- New channels added to **New Channels**: **{len(new_channels)}**",
        f"- New backup streams added to **New Backup**: **{len(new_backups)}**",
        f"- Candidates rejected by policy: **{rejected}**",
        "",
        "## New Channels",
        "",
    ]
    report += [f"- {x[2]} ({x[0]}) — {x[3]}" for x in new_channels] or ["None."]
    report += ["", "## New Backups", ""]
    report += [f"- {x[2]} ({x[0]}) — {x[3]}" for x in new_backups] or ["None."]
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Discovery: {len(new_channels)} new channels, {len(new_backups)} new backups, {rejected} rejected.")

if __name__ == "__main__":
    main()
