#!/usr/bin/env python3
"""Discover Bangladesh/India IPTV-org candidates into review-only queues.

Rules:
- Only the Bangladesh and India country feeds are considered.
- Existing stream URLs and normalized channel identities are never duplicated.
- First unseen stream for a new identity -> New Channels.
- Additional unseen streams for an existing/newly discovered identity -> New Backup.
- New queues are review-only and are consumed by Xtream only when explicitly enabled;
  the repository's Xtream workers currently exclude both groups.
"""
from __future__ import annotations
import json, re, unicodedata, urllib.request
from pathlib import Path
from urllib.parse import parse_qsl, urlparse

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/channel-discovery.md")
SOURCES = (
    ("Bangladesh", "https://iptv-org.github.io/iptv/countries/bd.m3u"),
    ("India", "https://iptv-org.github.io/iptv/countries/in.m3u"),
)
BAD_WORDS = {
    "vod", "catchup", "catch-up", "test", "demo", "proxy", "proxied",
    "cors", "webcam", "radio", "podcast", "event", "ppv", "timeshift",
}
BAD_HOSTS = ("proxy", "proxied", "cors", "localhost", "workers.dev", "worker.dev", "pages.dev")
BAD_QUERY_KEYS = {"token", "auth", "authorization", "hdnts", "sig", "signature", "expires", "session", "jwt", "key"}
QUALITY = {"uhd", "fhd", "hd", "sd", "4k", "1080p", "720p", "576p", "480p", "360p", "240p"}
COUNTRY_CODE = {"Bangladesh": "bd", "India": "in"}
BAD_RE = re.compile(r"(?<![a-z0-9])(?:" + "|".join(re.escape(w) for w in sorted(BAD_WORDS)) + r")(?![a-z0-9])")
ID_CC_RE = re.compile(r"\.([a-z]{2})(?:@|$)")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def split_extinf(line: str) -> tuple[str, str]:
    quoted = False
    for i, ch in enumerate(line):
        if ch == '"':
            quoted = not quoted
        elif ch == ',' and not quoted:
            return line[:i], line[i + 1:]
    return line, ""


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold().replace("_", " ")
    value = re.sub(r"\[[^]]*\]|\([^)]*\)", " ", value)
    value = " ".join(x for x in value.split() if x not in QUALITY)
    return "".join(c for c in value if c.isalnum() or unicodedata.category(c)[0] in "LMN")


def base_id(value: str) -> str:
    return (value or "").strip().casefold().split("@", 1)[0]


def parse(text: str):
    lines = text.replace("\r", "").splitlines()
    out = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines) or not lines[j].strip().lower().startswith(("http://", "https://")):
            continue
        a = attrs(line)
        _, display = split_extinf(line)
        name = (a.get("tvg-name") or display).strip()
        out.append((a, name, lines[j].strip()))
    return out


def acceptable(country: str, a: dict[str, str], name: str, url: str) -> bool:
    if country not in COUNTRY_CODE:
        return False
    m = ID_CC_RE.search((a.get("tvg-id") or a.get("channel-id") or "").strip().casefold())
    if not m or m.group(1) != COUNTRY_CODE[country]:
        return False
    p = urlparse(url)
    if p.scheme not in {"http", "https"} or not p.netloc or p.fragment:
        return False
    if BAD_RE.search(" ".join((name, a.get("tvg-id", ""), a.get("group-title", ""))).casefold()):
        return False
    if any(x in p.netloc.casefold() for x in BAD_HOSTS):
        return False
    if any(key.casefold() in BAD_QUERY_KEYS for key, _ in parse_qsl(p.query, keep_blank_values=True)):
        return False
    return p.path.casefold().endswith((".m3u8", ".m3u", ".ts")) and "vod" not in p.path.casefold() and "catchup" not in p.path.casefold()


def extinf(a: dict[str, str], name: str, group: str, country: str) -> str | None:
    cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not cid:
        return None
    fields = [f'tvg-id="{cid}"', f'tvg-name="{name}"']
    if a.get("tvg-logo", "").strip():
        fields.append(f'tvg-logo="{a["tvg-logo"].strip()}"')
    fields.append(f'tvg-country="{COUNTRY_CODE[country].upper()}"')
    fields.append(f'channel-id="{a.get("channel-id", cid).strip()}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + name


def main() -> int:
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    entries = parse(original)
    existing_urls = {u.casefold() for _, _, u in entries}
    existing_names = {norm(n) for _, n, _ in entries}
    existing_ids = {base_id(a.get("tvg-id") or a.get("channel-id")) for a, _, _ in entries if base_id(a.get("tvg-id") or a.get("channel-id"))}

    candidates = []
    rejected = 0
    seen_source_urls = set(existing_urls)
    for country, source in SOURCES:
        try:
            req = urllib.request.Request(source, headers={"User-Agent": "BDIX-IPTV-discovery/2.0"})
            text = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
        except Exception as exc:
            print(f"Source unavailable: {source}: {exc}")
            continue
        for a, name, url in parse(text):
            key = url.casefold()
            if acceptable(country, a, name, url) and key not in seen_source_urls:
                candidates.append((country, a, name, url))
                seen_source_urls.add(key)
            else:
                rejected += 1

    candidates.sort(key=lambda x: (x[0] != "Bangladesh", norm(x[2]), x[3]))
    new_channels, new_backups = [], []
    planned_names, planned_ids = set(existing_names), set(existing_ids)

    for country, a, name, url in candidates:
        key = norm(name)
        cid = base_id(a.get("tvg-id") or a.get("channel-id"))
        if key in planned_names or (cid and cid in planned_ids):
            new_backups.append((country, a, name, url))
        else:
            new_channels.append((country, a, name, url))
            planned_names.add(key)
            if cid:
                planned_ids.add(cid)

    new_channels = new_channels[:40]
    new_backups = new_backups[:80]

    lines = original.replace("\r", "").splitlines()
    additions = []
    for country, a, name, url in new_channels:
        info = extinf(a, name, "New Channels", country)
        if info:
            additions.extend([info, url])
    for country, a, name, url in new_backups:
        info = extinf(a, name, "New Backup", country)
        if info:
            additions.extend([info, url])

    if additions:
        while lines and not lines[-1].strip():
            lines.pop()
        lines.append("")
        lines.extend(additions)
        PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# Channel Discovery", "",
        "- Sources: Bangladesh + India iptv-org country feeds",
        f"- New channels: **{len(new_channels)}**",
        f"- New backups: **{len(new_backups)}**",
        f"- Rejected candidates: **{rejected}**", "",
        "## New Channels", "",
    ]
    report.extend(f"- {name} ({country}) — {url}" for country, _, name, url in new_channels)
    report += ["", "## New Backups", ""]
    report.extend(f"- {name} ({country}) — {url}" for country, _, name, url in new_backups)
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Discovery: {len(new_channels)} new channels, {len(new_backups)} new backups, {rejected} rejected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
