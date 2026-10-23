#!/usr/bin/env python3
"""Discover Bangladesh/India IPTV-org candidates into review-only queues.

Rules:
- Only the Bangladesh and India country feeds are considered.
- Indian News, Sports and Religious channels are STRICTLY PROHIBITED.
- Existing stream URLs and normalized channel identities are never duplicated.
- First unseen stream for a new identity -> New Channels.
- Additional unseen streams for an existing/newly discovered identity -> New Backup.
- New queues are review-only and are consumed by Xtream only when explicitly enabled;
  the repository's Xtream workers currently exclude both groups.
"""
from __future__ import annotations
import json, re, unicodedata, urllib.request
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qsl, urlparse

from country_verification import norm_name, reference_from_playlists, verify_country

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
# HARD EXCLUSION: Indian News, Sports and Religious channels are never eligible.
INDIA_FORBIDDEN_GROUPS = {"news", "sports", "religious"}
INDIA_FORBIDDEN_WORDS = {
    "news", "sport", "sports", "cricket", "football", "soccer", "tennis",
    "religious", "religion", "devotional", "bhakti", "bhakthi", "spiritual",
    "worship", "gospel", "christian", "christ", "islamic", "islam", "quran",
    "quran", "hindu", "hinduism", "sanatan", "sikh", "gurbani", "gurubani",
    "church", "temple", "mosque", "masjid", "sermons", "sermon", "prayer",
}
BAD_HOSTS = ("proxy", "proxied", "cors", "localhost", "workers.dev", "worker.dev", "pages.dev")
BAD_QUERY_KEYS = {"token", "auth", "authorization", "hdnts", "sig", "signature", "expires", "session", "jwt", "key"}
QUALITY = {"uhd", "fhd", "hd", "sd", "4k", "1080p", "720p", "576p", "480p", "360p", "240p"}
COUNTRY_CODE = {"Bangladesh": "bd", "India": "in"}
OTHER_PLAYLISTS = (Path("BDIX-Playlist.m3u"), Path("International-Playlist.m3u"))
BAD_RE = re.compile(r"(?<![^\W_])(?:" + "|".join(re.escape(w) for w in sorted(BAD_WORDS)) + r")(?![^\W_])")
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
    return norm_name(value)


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


def india_forbidden(a: dict[str, str], name: str) -> str | None:
    """Hard reject Indian News, Sports and Religious channels."""
    values = " ".join((name, a.get("tvg-name", ""), a.get("group-title", ""))).casefold()
    group = a.get("group-title", "").strip().casefold()
    if group in INDIA_FORBIDDEN_GROUPS:
        return f"India {group} channel is prohibited"
    # Match category terms as standalone words to avoid false positives such as 'Sporting Goods'.
    for word in INDIA_FORBIDDEN_WORDS:
        if re.search(r"(?<![\w])" + re.escape(word) + r"(?![\w])", values, re.UNICODE):
            return f"India {word} channel is prohibited"
    return None


def evaluate(country: str, a: dict[str, str], name: str, url: str, reference=None):
    """Return (normalized attrs | None, reason). Country must be verified BD/IN."""
    if country not in COUNTRY_CODE:
        return None, "unknown source feed"
    # STRICT POLICY: no Indian News, Sports or Religious channels, under any circumstance.
    if country == "India":
        forbidden = india_forbidden(a, name)
        if forbidden:
            return None, forbidden
    p = urlparse(url)
    if p.scheme not in {"http", "https"} or not p.netloc or p.fragment:
        return None, "invalid stream URL"
    if BAD_RE.search(" ".join((name, a.get("tvg-id", ""), a.get("group-title", ""))).casefold()):
        return None, "bad word (vod/test/proxy/...)"
    if any(x in p.netloc.casefold() for x in BAD_HOSTS):
        return None, "proxy/worker host"
    if any(key.casefold() in BAD_QUERY_KEYS for key, _ in parse_qsl(p.query, keep_blank_values=True)):
        return None, "tokenized URL"
    if not (p.path.casefold().endswith((".m3u8", ".m3u", ".ts")) and "vod" not in p.path.casefold() and "catchup" not in p.path.casefold()):
        return None, "unsupported stream path"
    verdict = verify_country(a, name, reference, COUNTRY_CODE[country].upper())
    if not verdict.ok:
        return None, "country not verified: " + verdict.reason
    out = dict(a)
    out["tvg-country"] = verdict.country
    out["tvg-id"] = verdict.tvg_id
    if not out.get("channel-id", "").strip() or not re.search(
            r"\." + verdict.country.casefold() + r"(?:@|$)", out["channel-id"].casefold()):
        out["channel-id"] = verdict.tvg_id
    return out, ""


def acceptable(country: str, a: dict[str, str], name: str, url: str, reference=None) -> bool:
    return evaluate(country, a, name, url, reference)[0] is not None


def extinf(a: dict[str, str], name: str, group: str, country: str) -> str | None:
    cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not cid or country not in COUNTRY_CODE or a.get("tvg-country", "").strip().upper() != COUNTRY_CODE[country].upper():
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

    reference = reference_from_playlists([PLAYLIST, *OTHER_PLAYLISTS])
    candidates = []
    rejected = 0
    reasons: Counter = Counter()
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
            normalized, reason = evaluate(country, a, name, url, reference)
            if normalized is not None and key not in seen_source_urls:
                candidates.append((country, normalized, name, url))
                seen_source_urls.add(key)
            else:
                rejected += 1
                reasons[reason or "duplicate stream URL"] += 1

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
        "- **STRICT POLICY: Indian News, Sports and Religious channels are prohibited and must never enter New Channels or New Backup.**",
        f"- New channels: **{len(new_channels)}**",
        f"- New backups: **{len(new_backups)}**",
        f"- Rejected/held candidates: **{rejected}**",
        "- Country policy: only candidates verified as BD/IN (valid `.bd`/`.in` id, or repository-mapping evidence when the id is missing/malformed) are queued; conflicting or unverifiable candidates are held.", "",
        "## Rejection reasons", "",
        *(f"- {r}: {n}" for r, n in sorted(reasons.items())), "",
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
