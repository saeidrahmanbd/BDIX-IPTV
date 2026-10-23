#!/usr/bin/env python3
"""Discover and organize International channels without playback testing.

Rules:
- Movies and music from any country are allowed.
- Non-Bangladeshi news is rejected.
- Non-Islamic religious channels are rejected.
- A country gets its own group at 5 legitimate channels, or immediately if
  that country group already exists.
- Countries below the threshold remain in International.
- Existing staging groups are not used.
"""
from __future__ import annotations

import hashlib
import os
import re
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path("International-Playlist.m3u")
REPORT = Path("reports/international-channel-discovery.md")
LOGOS = Path("logos")
SOURCE_URL = "https://iptv-org.github.io/iptv/index.category.m3u"
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
COUNTRY_THRESHOLD = 5
MAX_NEW_CHANNELS = 50
MAX_NEW_BACKUPS = 40
MAX_NEW_PER_GROUP = 14
MAX_SOURCE_BYTES = 50 * 1024 * 1024
MAX_LOGO_BYTES = 2 * 1024 * 1024

FIXED_GROUPS = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani"]
TAIL_GROUPS = ["International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup"]
LEGACY_GROUPS = {"new channels", "new backup", "not playing", "international movies", "international music"}

COUNTRY_NAMES = {
"BD":"Bangladesh","IN":"India","PK":"Pakistan","NP":"Nepal","TH":"Thailand","JP":"Japan","KR":"South Korea","ID":"Indonesia","MY":"Malaysia","PH":"Philippines","VN":"Vietnam","CN":"China","TW":"Taiwan","HK":"Hong Kong","SG":"Singapore","AU":"Australia","NZ":"New Zealand","GB":"United Kingdom","US":"United States","CA":"Canada","MX":"Mexico","BR":"Brazil","AR":"Argentina","CL":"Chile","CO":"Colombia","PE":"Peru","ES":"Spain","PT":"Portugal","FR":"France","DE":"Germany","IT":"Italy","NL":"Netherlands","BE":"Belgium","CH":"Switzerland","AT":"Austria","SE":"Sweden","NO":"Norway","DK":"Denmark","FI":"Finland","IS":"Iceland","IE":"Ireland","PL":"Poland","CZ":"Czech Republic","SK":"Slovakia","HU":"Hungary","RO":"Romania","BG":"Bulgaria","GR":"Greece","TR":"Turkey","RU":"Russia","UA":"Ukraine","IL":"Israel","AE":"United Arab Emirates","SA":"Saudi Arabia","QA":"Qatar","KW":"Kuwait","OM":"Oman","BH":"Bahrain","JO":"Jordan","LB":"Lebanon","EG":"Egypt","MA":"Morocco","DZ":"Algeria","TN":"Tunisia","ZA":"South Africa","NG":"Nigeria","KE":"Kenya","GH":"Ghana","TZ":"Tanzania","UG":"Uganda","ZW":"Zimbabwe","ET":"Ethiopia","LK":"Sri Lanka","MM":"Myanmar","KH":"Cambodia","LA":"Laos","MN":"Mongolia","KZ":"Kazakhstan","UZ":"Uzbekistan","AZ":"Azerbaijan","GE":"Georgia","AM":"Armenia","AL":"Albania","RS":"Serbia","HR":"Croatia","SI":"Slovenia","BA":"Bosnia and Herzegovina","ME":"Montenegro","MK":"North Macedonia","LT":"Lithuania","LV":"Latvia","EE":"Estonia","IS":"Iceland","IR":"Iran","IQ":"Iraq","SY":"Syria","PS":"Palestine","QA":"Qatar","FJ":"Fiji","WS":"Samoa","PG":"Papua New Guinea","NP":"Nepal","BT":"Bhutan","MV":"Maldives"
}
ISO_CODES = set(COUNTRY_NAMES)
ALIASES = {"UK":"GB", "EL":"GR"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_GROUPS = {"news"}
SPORTS_GROUPS = {"sport", "sports"}
DOC_GROUPS = {"documentary", "documentaries", "wildlife", "nature"}
KIDS_GROUPS = {"kids", "kid", "children", "childrens"}
RELIGIOUS_GROUPS = {"religious", "religion", "faith"}
NEWS_NAME_RE = re.compile(r"\b(?:news|headlines?|current affairs|cnn|cnbc|bloomberg|reuters|euronews|france\s*24|al\s*jazeera|msnbc|fox\s*news|sky\s*news|bbc\s*(?:news|world)|abc\s*news|nbc\s*news|dw\s*news|rt\s*news|ndtv|aaj\s*tak|times\s*now|news\s*18|news\s*nation|republic\s*(?:tv|bharat)|india\s*today|tv9|dd\s*news|trt\s*world)\b", re.I)
RELIGIOUS_RE = re.compile(r"\b(?:religious|religion|christian|christ|gospel|bible|jesus|church|catholic|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|jain|buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|prarthana|darshan|worship|sermon|evangelical|zoroastrian|ministry|dharma|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|deity|holy\s*mass|orthodox|shrine)\b", re.I)
ISLAMIC_RE = re.compile(r"\b(?:islam|islamic|muslim|quran|koran|sunnah|sunna|mecca|makkah|madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|allah|muhammad|mohammad|madani|iqra|peace\s*tv|kaaba|kabah|huda\s*tv|hidayat\s*tv|takbeer|ahlulbayt|mta\s*(?:international|world|1)|quran\s*kareem|al\s*huda|saudi\s*quran|holy\s*quran)\b", re.I)
BAD_NAME_RE = re.compile(r"\b(?:vod|video\s*on\s*demand|catch[\s-]?up|test|demo|webcam|podcast|radio|timeshift|ppv|pay\s*per\s*view|preview|sample|placeholder|coming\s*soon)\b", re.I)


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def split_extinf(line: str) -> str:
    quoted = False
    for i, c in enumerate(line):
        if c == '"':
            quoted = not quoted
        elif c == "," and not quoted:
            return line[i + 1:].strip()
    return ""


def parse_m3u(text: str):
    prefix, blocks, current = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is None:
            prefix.append(line)
        else:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return prefix, blocks


def name_of(block: list[str]) -> str:
    a = attrs(block[0])
    return (a.get("tvg-name") or split_extinf(block[0])).strip()


def url_of(block: list[str]) -> str:
    return next((x.strip() for x in block[1:] if x.strip().startswith(("http://", "https://"))), "")


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def country_code(a: dict[str, str]) -> str:
    for value in [a.get("tvg-country", "")]:
        for item in re.split(r"[;,|/\s]+", value.upper()):
            item = ALIASES.get(item, item)
            if item in ISO_CODES:
                return item
    ident = (a.get("tvg-id") or a.get("channel-id") or "").casefold()
    m = re.search(r"\.([a-z]{2})(?:@[^.]*)?$", ident)
    if m:
        code = ALIASES.get(m.group(1).upper(), m.group(1).upper())
        if code in ISO_CODES:
            return code
    return "ZZ"


def country_group(code: str) -> str:
    return COUNTRY_NAMES.get(code, "")


def eligible_country(a: dict[str, str], name: str) -> str:
    code = country_code(a)
    return code if code in ISO_CODES else ""


def policy(a: dict[str, str], name: str):
    code = country_code(a)
    groups = {re.sub(r"[^a-z0-9]+", "", x) for x in re.split(r"[;,|/]+", a.get("group-title", "").casefold()) if x.strip()}
    text = f"{name} {a.get('tvg-name','')} {a.get('tvg-id','')}"
    religious = bool(groups & RELIGIOUS_GROUPS) or bool(RELIGIOUS_RE.search(text))
    islamic = bool(ISLAMIC_RE.search(text))
    news = bool(groups & NEWS_GROUPS) or bool(NEWS_NAME_RE.search(text))
    if religious and not islamic:
        return None, "non-Islamic religious channel", code
    if news and code != "BD":
        return None, "non-Bangladeshi or unverified-country news channel", code
    if religious and islamic:
        return "Religious", None, code
    if news:
        return "Bangladesh", None, code
    if groups & KIDS_GROUPS:
        return "Kids", None, code
    if groups & DOC_GROUPS:
        return "Documentary & Wildlife", None, code
    if groups & SPORTS_GROUPS:
        return "Sports", None, code
    if code == "BD":
        return "Bangladesh", None, code
    if code == "PK":
        return "Pakistani", None, code
    if code == "IN":
        if re.search(r"\b(?:movie|movies|cinema|film|films)\b", name, re.I) or groups & {"movie", "movies", "cinema", "film", "films"}:
            return "Indian Movies", None, code
        if re.search(r"\b(?:music|musix|musica|musique)\b", name, re.I) or groups & {"music", "musics"}:
            return "Indian Music", None, code
        if re.search(r"\b(?:bangla|bengali)\b", name, re.I) or "bn" in re.split(r"[;,|/\s]+", a.get("tvg-language", "").casefold()):
            return "Indian Bangla", None, code
        return "Indian Entertainment", None, code
    return "International", None, code


def safe_url(url: str) -> bool:
    try:
        p = urllib.parse.urlsplit(url)
        if p.scheme not in {"http", "https"} or not p.hostname or p.username or p.password:
            return False
        if p.fragment:
            return False
        if any(x in p.hostname.casefold() for x in ("workers.dev", "pages.dev", "corsproxy", "streamproxy", "localhost")):
            return False
        bad = {"token", "auth", "authorization", "password", "passwd", "pwd", "username", "signature", "sig", "expires", "jwt", "session"}
        return not any(k.casefold() in bad for k, _ in urllib.parse.parse_qsl(p.query, keep_blank_values=True))
    except ValueError:
        return False


def slug(value: str) -> str:
    x = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold()
    x = re.sub(r"[^a-z0-9]+", "-", x).strip("-")[:80]
    return x or "channel-" + hashlib.sha256(value.encode()).hexdigest()[:10]


def local_logo(a: dict[str, str], name: str) -> str:
    target = norm(name)
    for p in LOGOS.rglob("*") if LOGOS.exists() else []:
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg"} and "unused" not in p.parts and norm(p.stem) == target:
            return RAW_BASE + str(p.relative_to(LOGOS)).replace("\\", "/")
    source = (a.get("tvg-logo") or "").strip()
    if not source.startswith(("http://", "https://")):
        return ""
    try:
        req = urllib.request.Request(source, headers={"User-Agent": "BDIX-IPTV-International-Discovery/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read(MAX_LOGO_BYTES + 1)
            typ = (r.headers.get("Content-Type") or "").split(";")[0].lower()
        if not data or len(data) > MAX_LOGO_BYTES:
            return ""
        ext = {"image/png":".png","image/jpeg":".jpg","image/webp":".webp","image/svg+xml":".svg"}.get(typ)
        if not ext:
            return ""
        d = LOGOS / "international"
        d.mkdir(parents=True, exist_ok=True)
        p = d / (slug(name) + ext)
        if not p.exists():
            p.write_bytes(data)
        return RAW_BASE + str(p.relative_to(LOGOS)).replace("\\", "/")
    except Exception:
        return ""


def make_extinf(a: dict[str, str], name: str, group: str, code: str, logo: str) -> str:
    clean = " ".join(name.replace('"', "").split())
    ident = (a.get("tvg-id") or a.get("channel-id") or "custom.intl." + slug(clean).replace("-", ".")).strip()
    fields = [f'tvg-id="{ident}"', f'tvg-name="{clean}"']
    if logo.startswith(RAW_BASE):
        fields.append(f'tvg-logo="{logo}"')
    if code:
        fields.append(f'tvg-country="{code}"')
    if a.get("tvg-language"):
        fields.append(f'tvg-language="{a["tvg-language"].replace(chr(34), "")}"')
    fields.append(f'channel-id="{(a.get("channel-id") or ident).replace(chr(34), "")}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + clean


def main() -> int:
    if not PLAYLIST.exists():
        raise SystemExit("International-Playlist.m3u not found; refusing to create it.")
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "BDIX-IPTV-International-Discovery/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        raw = r.read(MAX_SOURCE_BYTES + 1)
    if not raw or len(raw) > MAX_SOURCE_BYTES:
        raise SystemExit("Source feed is empty or exceeds the safety limit; playlist unchanged.")
    _, source = parse_m3u(raw.decode("utf-8-sig", "replace"))
    prefix, existing = parse_m3u(PLAYLIST.read_text(encoding="utf-8-sig"))
    if not source:
        raise SystemExit("Source feed has no channel records; playlist unchanged.")

    existing_urls = {url_of(b).casefold() for b in existing if url_of(b)}
    existing_names = defaultdict(list)
    country_counts = Counter()
    established = set()
    for b in existing:
        a = attrs(b[0]); name = name_of(b); key = norm(name); group = a.get("group-title", "").strip()
        if key and group.casefold() not in LEGACY_GROUPS:
            existing_names[key].append(a)
        code = eligible_country(a, name)
        if code:
            country_counts[code] += 1
            if group.casefold() == country_group(code).casefold():
                established.add(code)

    candidates = []
    seen = set()
    rejected = Counter()
    for b in source:
        a = attrs(b[0]); name = name_of(b); url = url_of(b)
        if not name:
            rejected["missing channel name"] += 1; continue
        if BAD_NAME_RE.search(name):
            rejected["test/VOD/non-TV name"] += 1; continue
        if not safe_url(url):
            rejected["unsafe or tokenized URL"] += 1; continue
        if url.casefold() in existing_urls or url.casefold() in seen:
            continue
        group, reason, code = policy(a, name)
        if group is None:
            rejected[reason] += 1; continue
        seen.add(url.casefold())
        candidates.append((a, name, url, norm(name), group, code))

    discovered_counts = Counter(code for a, name, url, key, group, code in candidates if code)
    totals = country_counts + discovered_counts
    country_groups = set(established) | {c for c, n in totals.items() if n >= COUNTRY_THRESHOLD}
    country_groups = {c for c in country_groups if country_group(c)}

    additions = []
    new_rows = []
    backup_rows = []
    per_group = Counter()
    planned = {k: list(v) for k, v in existing_names.items()}
    for a, name, url, key, base_group, code in candidates:
        if not key:
            continue
        backup = key in planned
        if backup and len(backup_rows) >= MAX_NEW_BACKUPS:
            continue
        if not backup and len(new_rows) >= MAX_NEW_CHANNELS:
            continue
        target = "Backup" if backup else base_group
        if not backup and code in country_groups and code not in {"BD", "IN", "PK"} and base_group not in {"Religious", "Sports", "Kids", "Documentary & Wildlife"}:
            target = country_group(code)
        if not backup and per_group[target] >= MAX_NEW_PER_GROUP:
            continue
        canonical = planned[key][0] if backup else a
        cname = canonical.get("tvg-name", name).strip() if backup else name
        ccode = country_code(canonical) if backup else code
        logo = local_logo(a, cname)
        if backup and canonical.get("tvg-logo", "").startswith(RAW_BASE) and not logo:
            logo = canonical["tvg-logo"]
        ext = make_extinf(canonical, cname, target, ccode, logo)
        directives = [x for x in b[1:] if x.strip().startswith(("#EXTVLCOPT:", "#KODIPROP:"))] if False else []
        additions.append([ext, url])
        if backup:
            backup_rows.append((cname, ccode))
        else:
            new_rows.append((cname, target, ccode)); per_group[target] += 1; planned.setdefault(key, []).append(attrs(ext))

    # Combine existing entries and new entries, then migrate legacy International
    # buckets into an established country group when their country qualifies.
    all_blocks = existing + additions
    migrated = []
    normalized = []
    for b in all_blocks:
        a = attrs(b[0]); name = name_of(b); old = a.get("group-title", "").strip()
        group = old
        if group.casefold() in LEGACY_GROUPS:
            group = "International"
        code = eligible_country(a, name)
        if code in country_groups and group.casefold() in {"international", "international movies", "international music"}:
            target = country_group(code)
            if group != target:
                b[0] = make_extinf(a, name, target, code, a.get("tvg-logo", ""))
                migrated.append((name, group, target))
        elif group != old:
            b[0] = make_extinf(a, name, group, code, a.get("tvg-logo", ""))
        normalized.append(b)

    dynamic = FIXED_GROUPS + sorted(country_group(c) for c in country_groups) + TAIL_GROUPS
    rank = {g.casefold(): i for i, g in enumerate(dynamic)}
    normalized.sort(key=lambda b: (rank.get(attrs(b[0]).get("group-title", "").strip().casefold(), len(rank)), norm(name_of(b)), url_of(b).casefold()))
    header = "#PLAYLIST-STUDIO-CATEGORIES:" + str(dynamic).replace("'", '"')
    out_prefix = [x for x in prefix if not x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    idx = next((i + 1 for i, x in enumerate(out_prefix) if x.startswith("#EXTM3U")), 0)
    out_prefix.insert(idx, header)
    output = out_prefix[:]
    for b in normalized: output.extend(b)
    PLAYLIST.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = ["# International Channel Discovery", "", f"- Last scan: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}", f"- Country threshold: {COUNTRY_THRESHOLD} legitimate channels.", "- Existing country groups accept new channels immediately.", "- Playback was not tested.", f"- New channels: {len(new_rows)}", f"- Backup streams: {len(backup_rows)}", f"- Country migrations: {len(migrated)}", f"- Established country groups: {', '.join(sorted(country_group(c) for c in country_groups)) or 'none'}", "", "## New Channels", ""]
    report += [f"- **{n}** — `{g}` — {c}" for n, g, c in new_rows]
    report += ["", "## Backup Streams", ""] + [f"- **{n}** — {c}" for n, c in backup_rows]
    report += ["", "## Country Migrations", ""] + [f"- **{n}**: `{old}` → `{new}`" for n, old, new in migrated]
    report += ["", "## Rejections", ""] + [f"- {k}: {v}" for k, v in sorted(rejected.items())]
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"International discovery complete: new={len(new_rows)} backup={len(backup_rows)} migrations={len(migrated)} countries={len(country_groups)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
