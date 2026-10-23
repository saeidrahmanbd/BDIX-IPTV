#!/usr/bin/env python3
"""Discover a broad set of international channels without testing playback.

This script only adds candidate entries. It never removes existing playlist
entries and never performs HTTP requests to stream URLs. Source/logo requests
are separate from playback validation.
"""
from __future__ import annotations

import hashlib
import os
import re
import unicodedata
import urllib.error
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
MAX_SOURCE_BYTES = 50 * 1024 * 1024
MAX_NEW_CHANNELS = 50
MAX_NEW_BACKUPS = 40
MAX_NEW_PER_GROUP = 14
MAX_LOGO_BYTES = 2 * 1024 * 1024

ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International Movies",
    "International Music", "International", "Documentary & Wildlife",
    "Kids", "Religious", "Adult", "Sports", "Backup", "New Channels",
    "New Backup", "Not Playing",
]
NO_LOGO = {
    "default.png", "placeholder.png", "no-logo.png", "nologo.png",
    "unknown.png", "blank.png", "generic.png", "favicon.png",
}
ISO_CODES = set("""
AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ
CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW XK
""".split())
COUNTRY_ALIASES = {"UK": "GB", "EL": "GR"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_GROUPS = {"news"}
MOVIE_GROUPS = {"movie", "movies", "cinema", "film", "films"}
MUSIC_GROUPS = {"music", "musics"}
KIDS_GROUPS = {"kids", "kid", "children", "childrens"}
DOC_GROUPS = {"documentary", "documentaries", "wildlife", "nature"}
SPORTS_GROUPS = {"sport", "sports"}
RELIGIOUS_GROUPS = {"religious", "religion", "faith"}
NEWS_NAME_RE = re.compile(
    r"\b(?:news|newsmax|newsnation|headlines?|current affairs|newsroom|"
    r"cnn|cnbc|bloomberg|reuters|euronews|france\s*24|al\s*jazeera|msnbc|"
    r"fox\s*news|sky\s*news|bbc\s*(?:news|world)|abc\s*news|cbc\s*news|"
    r"nbc\s*news|dw\s*news|rt\s*news|ndtv\s*(?:24x7|profit|india|world)|"
    r"aaj\s*tak|times\s*now|news\s*18|news\s*nation|republic\s*(?:tv|bharat)|"
    r"india\s*today|tv9\s*(?:bharatvarsh|news|telugu|kannada|marathi|gujarati)|"
    r"dd\s*news|trt\s*world|tvp\s*world|new\s*china\s*tv)\b",
    re.IGNORECASE,
)
RELIGIOUS_NAME_RE = re.compile(
    r"\b(?:religious|religion|christian|christ|gospel|bible|jesus|church|"
    r"catholic|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|jain|"
    r"buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|"
    r"prarthana|darshan|worship|sermon|evangelical|zoroastrian|ministry|"
    r"faith\s*tv|holy\s*mass|orthodox|shrine)\b",
    re.IGNORECASE,
)
ISLAMIC_NAME_RE = re.compile(
    r"\b(?:islam|islamic|muslim|quran|koran|sunnah|sunna|mecca|makkah|"
    r"madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|"
    r"allah|muhammad|mohammad|madani|iqra(?:a)?|peace\s*tv|kaaba|kabah|"
    r"huda\s*tv|hidayat\s*tv|takbeer|ahlulbayt|quran\s*kareem|"
    r"al\s*huda|saudi\s*quran|holy\s*quran)\b",
    re.IGNORECASE,
)
BAD_NAME_RE = re.compile(
    r"\b(?:vod|video\s*on\s*demand|catch[\s-]?up|test|demo|webcam|"
    r"podcast|radio|timeshift|time\s*shift|ppv|pay\s*per\s*view|"
    r"preview|sample|placeholder|coming\s*soon)\b",
    re.IGNORECASE,
)
BAD_HOST_PARTS = (
    "localhost", "workers.dev", "worker.dev", "pages.dev", "corsproxy",
    "cors-proxy", "proxy.example", "streamproxy",
)
BAD_QUERY_KEYS = {
    "token", "auth", "authorization", "password", "passwd", "pwd", "username",
    "signature", "sig", "expires", "hdnts", "jwt", "session", "key",
}


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def split_extinf(line: str) -> tuple[str, str]:
    quoted = False
    for index, char in enumerate(line):
        if char == '"':
            quoted = not quoted
        elif char == "," and not quoted:
            return line[:index], line[index + 1:].strip()
    return line, ""


def parse_m3u(text: str) -> tuple[list[str], list[list[str]]]:
    prefix: list[str] = []
    blocks: list[list[str]] = []
    current: list[str] | None = None
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


def name_of(extinf: str) -> str:
    a = attrs(extinf)
    return (a.get("tvg-name") or split_extinf(extinf)[1]).strip()


def url_of(block: list[str]) -> str:
    return next(
        (line.strip() for line in block[1:]
         if line.strip().startswith(("http://", "https://"))),
        "",
    )


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(
        r"\b(?:backup|uhd|fhd|hd|sd|4k|1080p|720p|576p|480p|360p)\b",
        " ", value,
    )
    return "".join(char for char in value if char.isalnum())


def slug(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", str(value or ""))
    ascii_value = decomposed.encode("ascii", "ignore").decode("ascii").casefold()
    result = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    return result[:90] or ("channel-" + hashlib.sha256(value.encode("utf-8")).hexdigest()[:10])


def group_tokens(value: str) -> set[str]:
    parts = re.split(r"[;,|/]+", (value or "").casefold())
    return {re.sub(r"[^a-z0-9]+", "", part) for part in parts if part.strip()}


def country_of(a: dict[str, str]) -> str:
    explicit = (a.get("tvg-country") or "").strip().upper()
    for item in re.split(r"[;,|/\s]+", explicit):
        item = COUNTRY_ALIASES.get(item, item)
        if item in ISO_CODES:
            return item
    ident = (a.get("tvg-id") or a.get("channel-id") or "").casefold().strip()
    match = re.search(r"\.([a-z]{2})(?:@[^.]*)?$", ident)
    if match:
        code = COUNTRY_ALIASES.get(match.group(1).upper(), match.group(1).upper())
        if code in ISO_CODES:
            return code
    return "ZZ"


def policy_group(a: dict[str, str], name: str) -> tuple[str | None, str | None, str]:
    """Return (playlist group or None, rejection reason or None, country code)."""
    country = country_of(a)
    groups = group_tokens(a.get("group-title", ""))
    text = " ".join((name, a.get("tvg-name", ""), a.get("tvg-id", ""))).strip()

    religious = bool(groups & RELIGIOUS_GROUPS) or bool(RELIGIOUS_NAME_RE.search(text))
    islamic = bool(ISLAMIC_NAME_RE.search(text))
    news_category = bool(groups & NEWS_GROUPS)
    named_news = bool(NEWS_NAME_RE.search(text))

    if religious and not islamic:
        return None, "non-Islamic religious channel", country
    if (news_category or named_news) and country != "BD":
        return None, "non-Bangladeshi or unverified-country news channel", country
    if religious and islamic:
        return "Religious", None, country
    if news_category or named_news:
        return "Bangladesh", None, country

    movies = bool(groups & MOVIE_GROUPS)
    music = bool(groups & MUSIC_GROUPS)
    if not movies and not music:
        movies = bool(re.search(r"\b(?:movies?|cinema|films?)\b", name, re.IGNORECASE))
        music = bool(re.search(r"\b(?:music|musix|musica|musique)\b", name, re.IGNORECASE))

    if groups & KIDS_GROUPS:
        return "Kids", None, country
    if groups & DOC_GROUPS:
        return "Documentary & Wildlife", None, country
    if groups & SPORTS_GROUPS:
        return "Sports", None, country

    if country == "BD":
        return "Bangladesh", None, country
    if country == "PK":
        return "Pakistani", None, country
    if country == "IN":
        if movies:
            return "Indian Movies", None, country
        if music:
            return "Indian Music", None, country
        language = (a.get("tvg-language") or "").casefold()
        if any(code in {"ben", "bn"} for code in re.split(r"[;,|/\s]+", language)):
            return "Indian Bangla", None, country
        if re.search(r"\b(?:bangla|bengali)\b", name, re.IGNORECASE):
            return "Indian Bangla", None, country
        return "Indian Entertainment", None, country

    if movies:
        return "International Movies", None, country
    if music:
        return "International Music", None, country
    return "International", None, country


def safe_stream_url(url: str) -> tuple[bool, str | None]:
    try:
        parsed = urllib.parse.urlsplit(url.strip())
        if parsed.scheme.lower() not in {"http", "https"} or not parsed.hostname:
            return False, "invalid or unsupported URL"
        if parsed.username or parsed.password:
            return False, "credentials embedded in URL"
        host = parsed.hostname.casefold()
        if any(part in host for part in BAD_HOST_PARTS):
            return False, "proxy or worker URL"
        if "dai.google.com" in host or "doubleclick.net" in host:
            return False, "ad-insertion URL"
        if parsed.fragment:
            return False, "URL fragment present"
        for key, _ in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
            if key.casefold() in BAD_QUERY_KEYS:
                return False, "tokenized or credentialed URL"
        if re.search(r"/(?:vod|catchup|timeshift|movie-on-demand)(?:/|$)", parsed.path, re.I):
            return False, "VOD or catch-up URL"
        return True, None
    except Exception:
        return False, "invalid URL"


def local_logo_for(name: str) -> Path | None:
    target = norm(name)
    if not target or not LOGOS.exists():
        return None
    candidates = []
    for path in LOGOS.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".svg"}:
            continue
        relative_parts = {part.casefold() for part in path.relative_to(LOGOS).parts}
        if "unused" in relative_parts or path.name.casefold() in NO_LOGO:
            continue
        if path.stem.casefold().startswith("generated-fallback-"):
            continue
        if norm(path.stem) == target:
            candidates.append(path)
    if not candidates:
        return None
    candidates.sort(key=lambda path: (len(path.parts), str(path).casefold()))
    return candidates[0]


def download_logo(source_url: str, name: str) -> Path | None:
    if not source_url or not source_url.startswith(("http://", "https://")):
        return None
    parsed = urllib.parse.urlsplit(source_url)
    if Path(urllib.parse.unquote(parsed.path)).name.casefold() in NO_LOGO:
        return None
    if re.search(r"placeholder|generic|no[-_]?logo|unknown|blank|favicon", parsed.path, re.I):
        return None
    try:
        request = urllib.request.Request(
            source_url,
            headers={"User-Agent": "BDIX-IPTV-International-Discovery/1.0"},
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read(MAX_LOGO_BYTES + 1)
            content_type = (response.headers.get("Content-Type") or "").split(";")[0].lower()
        if not data or len(data) > MAX_LOGO_BYTES:
            return None
        left = data.lstrip()
        if data.startswith(b"\x89PNG\r\n\x1a\n"):
            extension = ".png"
        elif data.startswith(b"\xff\xd8\xff"):
            extension = ".jpg"
        elif data.startswith(b"RIFF") and data[8:12] == b"WEBP":
            extension = ".webp"
        elif left.startswith(b"<svg") or (left.startswith(b"<?xml") and b"<svg" in left[:1000]):
            extension = ".svg"
        else:
            extension = {
                "image/png": ".png",
                "image/jpeg": ".jpg",
                "image/webp": ".webp",
                "image/svg+xml": ".svg",
            }.get(content_type)
        if extension is None:
            return None
        directory = LOGOS / "international"
        directory.mkdir(parents=True, exist_ok=True)
        target = directory / (slug(name) + extension)
        if target.exists() and target.stat().st_size > 0:
            return target
        target.write_bytes(data)
        return target
    except (OSError, urllib.error.URLError, TimeoutError, ValueError):
        return None


def logo_uri(path: Path | None) -> str:
    if path is None:
        return ""
    return RAW_BASE + str(path.relative_to(LOGOS)).replace("\\", "/")


def make_extinf(a: dict[str, str], name: str, group: str, country: str, logo: str) -> str:
    clean_name = " ".join(name.replace('"', "").replace("\r", " ").replace("\n", " ").split())
    ident = (a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not ident:
        ident = "custom.intl." + slug(clean_name).replace("-", ".")
    fields = [f'tvg-id="{ident}"', f'tvg-name="{clean_name}"']
    if logo and logo.startswith(RAW_BASE):
        fields.append(f'tvg-logo="{logo}"')
    fields.append(f'tvg-country="{country}"')
    language = (a.get("tvg-language") or "").strip().replace('"', "")
    if language:
        fields.append(f'tvg-language="{language}"')
    channel_id = (a.get("channel-id") or ident).replace('"', "").strip()
    fields.append(f'channel-id="{channel_id}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + clean_name


def natural_key(value: str):
    return tuple(int(piece) if piece.isdigit() else piece.casefold() for piece in re.split(r"(\d+)", value or ""))


def localize_candidate_logo(a: dict[str, str], name: str, fallback: str = "") -> str:
    existing = local_logo_for(name)
    if existing:
        return logo_uri(existing)
    source_logo = (a.get("tvg-logo") or "").strip()
    downloaded = download_logo(source_logo, name)
    if downloaded:
        return logo_uri(downloaded)
    if fallback.startswith(RAW_BASE):
        relative = urllib.parse.urlsplit(fallback).path.split("/logos/", 1)[-1]
        if relative and (LOGOS / relative).is_file() and "unused" not in Path(relative).parts:
            return fallback
    return ""


def fetch_source() -> str:
    request = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "BDIX-IPTV-International-Discovery/1.0"},
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        data = response.read(MAX_SOURCE_BYTES + 1)
    if not data or len(data) > MAX_SOURCE_BYTES:
        raise RuntimeError("Source feed is empty or exceeds the configured safety limit.")
    return data.decode("utf-8-sig", "replace")


def write_step_summary(text: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as handle:
            handle.write(text.rstrip() + "\n")


def main() -> int:
    if not PLAYLIST.is_file():
        raise SystemExit("International-Playlist.m3u not found; refusing to create or replace it.")
    try:
        source_text = fetch_source()
    except Exception as exc:
        raise SystemExit(f"International source feed could not be fetched; playlist unchanged: {exc}")

    prefix, existing_blocks = parse_m3u(PLAYLIST.read_text(encoding="utf-8-sig"))
    _, source_blocks = parse_m3u(source_text)
    if not source_blocks:
        raise SystemExit("Source feed contained no channel records; playlist unchanged.")

    existing_urls = {url_of(block).casefold() for block in existing_blocks if url_of(block)}
    existing_names: dict[str, list[dict[str, str]]] = defaultdict(list)
    for block in existing_blocks:
        if not block:
            continue
        a = attrs(block[0])
        key = norm(name_of(block[0]))
        if key and a.get("group-title", "").strip().casefold() != "adult":
            existing_names[key].append(a)

    candidates = []
    seen_source_urls: set[str] = set()
    rejected: Counter[str] = Counter()
    for block in source_blocks:
        if not block:
            continue
        info = block[0]
        a = attrs(info)
        name = name_of(info)
        url = url_of(block)
        if not name:
            rejected["missing channel name"] += 1
            continue
        if BAD_NAME_RE.search(name):
            rejected["non-TV, test, or VOD-style name"] += 1
            continue
        allowed, reason = safe_stream_url(url)
        if not allowed:
            rejected[reason or "invalid stream URL"] += 1
            continue
        key_url = url.casefold()
        if key_url in existing_urls:
            rejected["stream URL already present"] += 1
            continue
        if key_url in seen_source_urls:
            rejected["duplicate URL in source feed"] += 1
            continue
        group, reason, country = policy_group(a, name)
        if group is None:
            rejected[reason or "policy exclusion"] += 1
            continue
        seen_source_urls.add(key_url)
        candidates.append({
            "attrs": a, "name": name, "url": url, "key": norm(name),
            "group": group, "country": country, "directives": [
                line for line in block[1:]
                if line.strip().startswith("#EXTVLCOPT:") or line.strip().startswith("#KODIPROP:")
            ],
        })

    priority = {
        "International Movies": 0, "International Music": 1, "International": 2,
        "Sports": 3, "Documentary & Wildlife": 4, "Kids": 5, "Religious": 6,
        "Pakistani": 7, "Indian Movies": 8, "Indian Music": 9,
        "Indian Entertainment": 10, "Indian Bangla": 11, "Bangladesh": 12,
    }
    candidates.sort(key=lambda item: (
        priority.get(item["group"], 99),
        item["country"] in {"BD", "IN", "PK"},
        norm(item["name"]), item["url"].casefold(),
    ))

    planned_names = {key: values[:] for key, values in existing_names.items()}
    additions: list[list[str]] = []
    new_primary_rows = []
    new_backup_rows = []
    per_group = Counter()
    for candidate in candidates:
        name = candidate["name"]
        key = candidate["key"]
        if not key:
            rejected["unmatchable channel identity"] += 1
            continue
        is_backup = key in planned_names
        if is_backup:
            if len(new_backup_rows) >= MAX_NEW_BACKUPS:
                rejected["backup limit reached for this run"] += 1
                continue
        else:
            if len(new_primary_rows) >= MAX_NEW_CHANNELS:
                rejected["new-channel limit reached for this run"] += 1
                continue
            if per_group[candidate["group"]] >= MAX_NEW_PER_GROUP:
                rejected["per-category limit reached for this run"] += 1
                continue

        canonical_attrs = planned_names[key][0] if is_backup and planned_names[key] else candidate["attrs"]
        canonical_name = (canonical_attrs.get("tvg-name") or name).strip() if is_backup else name
        group = "Backup" if is_backup else candidate["group"]
        canonical_country = country_of(canonical_attrs) if is_backup else candidate["country"]
        if canonical_country == "ZZ":
            canonical_country = candidate["country"]
        inherited_logo = (canonical_attrs.get("tvg-logo") or "").strip() if is_backup else ""
        logo = localize_candidate_logo(candidate["attrs"], canonical_name, inherited_logo)
        extinf = make_extinf(canonical_attrs if is_backup else candidate["attrs"],
                             canonical_name, group, canonical_country, logo)
        row = [extinf, *candidate["directives"], candidate["url"]]
        additions.append(row)
        if is_backup:
            new_backup_rows.append({"name": canonical_name, "group": "Backup", "country": canonical_country})
        else:
            new_primary_rows.append({"name": name, "group": candidate["group"], "country": candidate["country"]})
            per_group[candidate["group"]] += 1
            planned_names.setdefault(key, []).append(attrs(extinf))

    if additions:
        all_blocks = existing_blocks + additions
        rank = {name: index for index, name in enumerate(ORDER)}
        all_blocks.sort(key=lambda block: (
            rank.get(attrs(block[0]).get("group-title", "").strip(), len(rank)),
            natural_key(name_of(block[0])),
            url_of(block).casefold(),
        ))
        updated_prefix = [line for line in prefix if not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
        header = '#PLAYLIST-STUDIO-CATEGORIES:' + str(ORDER).replace("'", '"')
        extm3u_index = next((i + 1 for i, line in enumerate(updated_prefix) if line.startswith("#EXTM3U")), 0)
        updated_prefix.insert(extm3u_index, header)
        output = updated_prefix[:]
        for block in all_blocks:
            output.extend(block)
        PLAYLIST.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    else:
        header = '#PLAYLIST-STUDIO-CATEGORIES:' + str(ORDER).replace("'", '"')
        current = PLAYLIST.read_text(encoding="utf-8-sig")
        if "#PLAYLIST-STUDIO-CATEGORIES:" not in current or header not in current:
            lines = [line for line in current.replace("\r", "").splitlines()
                     if not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
            extm3u_index = next((i + 1 for i, line in enumerate(lines) if line.startswith("#EXTM3U")), 0)
            lines.insert(extm3u_index, header)
            PLAYLIST.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report_lines = [
        "# International Channel Discovery", "",
        f"- Last scan with this report: {timestamp}",
        "- Source: IPTV-org categorized worldwide channel index.",
        "- Playback was not tested; stream checking remains a manual task.",
        "- Existing channel metadata and stream URL lines were preserved; entries may be re-sorted to keep category order.",
        f"- New primary channels added: {len(new_primary_rows)}",
        f"- Additional streams added under Backup: {len(new_backup_rows)}",
        f"- Candidates rejected or held: {sum(rejected.values())}",
        "", "## New Channels", "",
    ]
    report_lines.extend(
        f"- **{row['name']}** — {row['group']} — {row['country']}"
        for row in new_primary_rows
    )
    report_lines += ["", "## New Backup Streams", ""]
    report_lines.extend(f"- **{row['name']}** — {row['country']}" for row in new_backup_rows)
    report_lines += ["", "## Policy and filtering", ""]
    report_lines.extend(f"- {reason}: {count}" for reason, count in sorted(rejected.items()))
    if not new_primary_rows and not new_backup_rows:
        report_lines += ["", "No new entries were added during this scan."]
    report_text = "\n".join(report_lines) + "\n"

    if new_primary_rows or new_backup_rows or not REPORT.exists():
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(report_text, encoding="utf-8")

    step_summary = [
        "# International Channel Discovery", "",
        f"- Source entries scanned: {len(source_blocks)}",
        f"- New channels added: {len(new_primary_rows)}",
        f"- Additional Backup streams added: {len(new_backup_rows)}",
        f"- Candidates rejected or held: {sum(rejected.values())}",
        "- Playback testing: not performed (manual by repository owner).",
    ]
    if new_primary_rows:
        step_summary += ["", "## New Channels", ""]
        step_summary.extend(f"- {row['name']} — {row['group']}" for row in new_primary_rows)
    if new_backup_rows:
        step_summary += ["", "## New Backup Streams", ""]
        step_summary.extend(f"- {row['name']}" for row in new_backup_rows)
    if rejected:
        step_summary += ["", "## Policy / quality filter counts", ""]
        step_summary.extend(f"- {reason}: {count}" for reason, count in sorted(rejected.items()))
    write_step_summary("\n".join(step_summary))
    print(
        f"International discovery complete: scanned={len(source_blocks)} "
        f"new_channels={len(new_primary_rows)} new_backups={len(new_backup_rows)} "
        f"rejected={sum(rejected.values())}; playback checks were not performed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
