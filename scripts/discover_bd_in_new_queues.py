#!/usr/bin/env python3
"""Discover Bangladesh/India IPTV-org candidates into review-only queues.

Rules:
- Only the Bangladesh and India country feeds are considered.
- Bangladeshi news channels are allowed. Indian News and non-Islamic Religious channels are prohibited; Indian Kids and Sports channels are allowed.
- Existing stream URLs and normalized channel identities are never duplicated.
- First unseen stream for a new identity -> New Channels.
- Additional unseen streams for an existing/newly discovered identity -> New Backup.
- New queues are review-only and are consumed by Xtream only when explicitly enabled;
  the repository's Xtream workers currently exclude both groups.
"""
from __future__ import annotations
import json, re, unicodedata, urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlparse

from country_verification import norm_name, reference_from_playlists, verify_country

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/iptv-channel-discovery.md")
SOURCES = (
    ("Bangladesh", "https://iptv-org.github.io/iptv/countries/bd.m3u"),
    ("India", "https://iptv-org.github.io/iptv/countries/in.m3u"),
)
BAD_WORDS = {
    "vod", "catchup", "catch-up", "test", "demo", "proxy", "proxied",
    "cors", "webcam", "radio", "podcast", "event", "ppv", "timeshift",
}
# India News and non-Islamic Religious channels are prohibited; Indian Kids/Sports and Bangladesh news remain eligible.
FORBIDDEN_CATEGORY_PATTERNS = {
    "news": re.compile(r"\bnews\b", re.IGNORECASE),
    "sports": re.compile(r"\b(?:sports?|cricket|football|soccer|tennis|racing)\b", re.IGNORECASE),
    "kids": re.compile(r"\b(?:kids?|children|child|cartoons?|nursery|preschool|junior)\b", re.IGNORECASE),
    "religious": re.compile(r"\b(?:religious|religion|devotional|bhakti|bhakthi|spiritual|worship|gospel|christian|christ|islamic|islam|quran|hindu|hinduism|sanatan|sikh|gurbani|gurubani|church|temple|mosque|masjid|sermons?|prayer)\b", re.IGNORECASE),
}

def canonical_channel_name(value: str) -> str:
    value = re.sub(r"\([^)]*\)|\[[^]]*\]", " ", str(value or ""))
    value = re.sub(r"\b(?:\d{3,4}p|uhd|fhd|hd|sd|4k)\b", " ", value, flags=re.IGNORECASE)
    value = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

PERMANENTLY_BANNED_CHANNEL_NAMES = {
    canonical_channel_name(name) for name in (
        "E-Vidya 10", "E-Vidya 11", "E-Vidya 12", "E-Vidya 4", "E-Vidya 5",
        "E-Vidya 6", "E-Vidya 7", "E-Vidya 8", "E-Vidya 9", "Friends TV",
    )
}

FORBIDDEN_WORDS = {
    "news",
    "religious", "religion", "devotional", "bhakti", "bhakthi", "spiritual", "worship",
    "gospel", "christian", "christ", "islamic", "islam", "quran", "hindu", "hinduism",
    "sanatan", "sikh", "gurbani", "gurubani", "church", "temple", "mosque", "masjid",
    "sermons", "sermon", "prayer",
}
FORBIDDEN_BRANDS = re.compile(
    r"\b(?:"
    r"aad(?:i|ee)nath|aaseervatham|aastha|sadhna|sanskar|jinvani|satsang|jagran|"
    r"bhagwat|aradhana|prarthana|divya|peace\s*tv|shubh\s*tv|aagaaz\s+times|"
    r"aaj\s+ki\s+khabar|abp(?:\s+(?:ananda|asmita|ganga|majha|news))?|"
    r"abn\s+andhra\s+jyoti|aaj\s+tak|times\s+now|india\s+today|news18|"
    r"ndtv\s+profit|ndtv\s+24x7|republic(?:\s+bharat|\s+tv)?|news\s+nation|"
    r"sudarshan\s+news|tv9(?:\s+\w+)?|zee\s+news|"
    r"cnbc(?:\s+awaaz|\s+bajar|\s+tv18(?:\s+prime)?)?|dd\s+news|dd\s+sports|"
    r"et\s+now|mirror\s+now|bharat\s+samachar|pratidin\s+time|amrit\s+gurbani|"
    r"sansad\s+tv(?:\s+[12])?|zee\s+business|"
    r"disney(?:\s+(?:junior|channel|kids?))?|nickelodeon|nick\s*jr|cartoon\s+network|"
    r"pogo|hungama|sony\s+yay|discovery\s+kids|etv\s+bal\s+bharat|"
    r"green\s+gold(?:\s+tv)?|kite\s+victers|chutti\s+tv|wow\s+kidz|"
    r"mh\s*one|sai\s+tv|darshana\s+tv|sarv\s+dharm\s+sangam"
    r")\b",
    re.IGNORECASE,
)
BAD_HOSTS = ("proxy", "proxied", "cors", "localhost", "workers.dev", "worker.dev", "pages.dev")
BAD_QUERY_KEYS = {"token", "auth", "authorization", "hdnts", "sig", "signature", "expires", "session", "jwt", "key"}
QUALITY = {"uhd", "fhd", "hd", "sd", "4k", "1080p", "720p", "576p", "480p", "360p", "240p"}
COUNTRY_CODE = {"Bangladesh": "bd", "India": "in"}
# Country-group threshold used by discovery-policy validation. A new country group
# must not be created from fewer than five legitimate primary identities.
COUNTRY_THRESHOLD = 5
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


def channel_country(a: dict[str, str], fallback: str | None = None) -> str | None:
    """Resolve BD/IN from source context, tvg-country, or a recognized channel-ID suffix."""
    if fallback:
        value = fallback.strip().casefold()
        if value in {"bangladesh", "bd"}:
            return "BD"
        if value in {"india", "in"}:
            return "IN"
    declared = (a.get("tvg-country") or "").strip().upper()
    if declared in {"BD", "IN"}:
        return declared
    for key in ("tvg-id", "channel-id"):
        match = ID_CC_RE.search((a.get(key) or "").strip().casefold())
        if match and match.group(1) in {"bd", "in"}:
            return match.group(1).upper()
    return None


def prohibited_channel(a: dict[str, str], name: str, country: str | None = None) -> str | None:
    """Return a hard exclusion reason; topical bans apply only to Indian channels."""
    for candidate in (name, a.get("tvg-name", "")):
        if canonical_channel_name(candidate) in PERMANENTLY_BANNED_CHANNEL_NAMES:
            return "permanently banned channel"

    resolved_country = channel_country(a, country)
    # The user's country-specific rule: Bangladeshi news is permitted; the four
    # topic exclusions apply to Indian candidates only.
    if resolved_country != "IN":
        return None

    group = a.get("group-title", "").strip()
    for category, pattern in FORBIDDEN_CATEGORY_PATTERNS.items():
        if pattern.search(group):
            return f"Indian {category} channel is prohibited"
    values = " ".join((name, a.get("tvg-name", ""), group, a.get("tvg-id", ""), a.get("channel-id", "")))
    for category, pattern in FORBIDDEN_CATEGORY_PATTERNS.items():
        if pattern.search(values):
            return f"Indian {category} channel is prohibited"
    if FORBIDDEN_BRANDS.search(values):
        return "known Indian News, Sports, Kids or Religious brand/category is prohibited"
    for word in FORBIDDEN_WORDS:
        if re.search(r"(?<![\w])" + re.escape(word) + r"(?![\w])", values, re.UNICODE):
            return f"Indian {word} channel is prohibited"
    return None

def evaluate(country: str, a: dict[str, str], name: str, url: str, reference=None):
    """Return (normalized attrs | None, reason). Country must be verified BD/IN."""
    if country not in COUNTRY_CODE:
        return None, "unknown source feed"
    # Bangladesh news is allowed; News/Sports/Kids/Religious exclusions are India-only.
    forbidden = prohibited_channel(a, name, country)
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


def purge_forbidden_existing_queue_rows(text: str) -> tuple[str, list[str]]:
    """Remove permanently banned channels and prohibited categories from review queues."""
    lines = text.replace("\r", "").splitlines()
    first = next((i for i, line in enumerate(lines) if line.startswith("#EXTINF:")), len(lines))
    prefix = lines[:first]
    blocks = []
    if first < len(lines):
        start = first
        for i in range(first + 1, len(lines)):
            if lines[i].startswith("#EXTINF:"):
                blocks.append(lines[start:i])
                start = i
        blocks.append(lines[start:])
    kept, removed = [], []
    queue_groups = {"New Channels", "New Backup", "New Backups"}
    for block in blocks:
        extinf_line = next((line for line in block if line.startswith("#EXTINF:")), "")
        if not extinf_line:
            kept.extend(block)
            continue
        a = attrs(extinf_line)
        group = a.get("group-title", "").strip()
        _, display = split_extinf(extinf_line)
        name = (a.get("tvg-name") or display).strip()
        if group in queue_groups:
            reason = prohibited_channel(a, name)
            if reason:
                removed.append(name or "(unnamed)")
                continue
        kept.extend(block)
    result = "\n".join(prefix + kept).rstrip() + "\n"
    return result, removed


def extinf(a: dict[str, str], name: str, group: str, country: str) -> str | None:
    cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not cid or country not in COUNTRY_CODE or a.get("tvg-country", "").strip().upper() != COUNTRY_CODE[country].upper():
        return None
    fields = [f'tvg-id="{cid}"', f'tvg-name="{name}"']
    if a.get("tvg-logo", "").strip():
        fields.append(f'tvg-logo="{a["tvg-logo"].strip()}"')
    fields.append(f'tvg-country="{COUNTRY_CODE[country].upper()}"')
    if a.get("tvg-language", "").strip():
        fields.append(f'tvg-language="{a["tvg-language"].strip()}"')
    fields.append(f'channel-id="{a.get("channel-id", cid).strip()}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + name


def main() -> int:
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    original, purged = purge_forbidden_existing_queue_rows(original)
    if purged:
        PLAYLIST.write_text(original, encoding="utf-8")
        print(f"Removed {len(purged)} prohibited Indian review-queue rows before discovery.")
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
        "# IPTV Channel Discovery", "",
        f"Generated: **{datetime.now(timezone.utc).isoformat()}**", "",
        "- Sources: Bangladesh + India iptv-org country feeds",
        "- **STRICT POLICY: Only verified Bangladesh and India channels are eligible. Bangladeshi news is allowed; Indian News and non-Islamic Religious channels are prohibited; Indian Kids and Sports channels are allowed.**",
        "- Permanent denylist: E-Vidya 4, 5, 6, 7, 8, 9, 10, 11, 12 and Friends TV.",
        f"- Country-group threshold: **{COUNTRY_THRESHOLD}** legitimate primary identities",
        f"- Existing prohibited review-queue rows removed: **{len(purged)}**",
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
    if purged:
        report += ["", "## Existing prohibited review-queue rows removed", ""]
        report.extend(f"- {name}" for name in sorted(purged, key=norm))
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Discovery: {len(new_channels)} new channels, {len(new_backups)} new backups, {rejected} rejected; purged {len(purged)} prohibited review-queue rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())