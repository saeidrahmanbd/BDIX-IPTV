#!/usr/bin/env python3
"""Discover broad international channels without testing playback.

Country grouping is dynamic: a country gets its own group once at least five
legitimate channels from that country are known, or immediately if that country
group already exists. Existing staging groups are not used.
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
COUNTRY_THRESHOLD = 5

FIXED_GROUPS = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani",
]
TAIL_GROUPS = ["International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup"]
LEGACY_STAGING_GROUPS = {"new channels", "new backup", "not playing", "international movies", "international music"}
SPECIAL_GROUPS = set(FIXED_GROUPS + TAIL_GROUPS)

# ISO-3166 alpha-2 -> readable playlist group name.
COUNTRY_NAMES = {
    "AD":"Andorra","AE":"United Arab Emirates","AF":"Afghanistan","AG":"Antigua and Barbuda","AI":"Anguilla","AL":"Albania","AM":"Armenia","AO":"Angola","AR":"Argentina","AS":"American Samoa","AT":"Austria","AU":"Australia","AW":"Aruba","AX":"Åland Islands","AZ":"Azerbaijan",
    "BA":"Bosnia and Herzegovina","BB":"Barbados","BD":"Bangladesh","BE":"Belgium","BF":"Burkina Faso","BG":"Bulgaria","BH":"Bahrain","BI":"Burundi","BJ":"Benin","BL":"Saint Barthélemy","BM":"Bermuda","BN":"Brunei","BO":"Bolivia","BQ":"Caribbean Netherlands","BR":"Brazil","BS":"Bahamas","BT":"Bhutan","BV":"Bouvet Island","BW":"Botswana","BY":"Belarus","BZ":"Belize",
    "CA":"Canada","CC":"Cocos Islands","CD":"Democratic Republic of the Congo","CF":"Central African Republic","CG":"Republic of the Congo","CH":"Switzerland","CI":"Côte d'Ivoire","CK":"Cook Islands","CL":"Chile","CM":"Cameroon","CN":"China","CO":"Colombia","CR":"Costa Rica","CU":"Cuba","CV":"Cape Verde","CW":"Curaçao","CX":"Christmas Island","CY":"Cyprus","CZ":"Czech Republic",
    "DE":"Germany","DJ":"Djibouti","DK":"Denmark","DM":"Dominica","DO":"Dominican Republic","DZ":"Algeria","EC":"Ecuador","EE":"Estonia","EG":"Egypt","EH":"Western Sahara","ER":"Eritrea","ES":"Spain","ET":"Ethiopia",
    "FI":"Finland","FJ":"Fiji","FK":"Falkland Islands","FM":"Micronesia","FO":"Faroe Islands","FR":"France","GA":"Gabon","GB":"United Kingdom","GD":"Grenada","GE":"Georgia","GF":"French Guiana","GG":"Guernsey","GH":"Ghana","GI":"Gibraltar","GL":"Greenland","GM":"Gambia","GN":"Guinea","GP":"Guadeloupe","GQ":"Equatorial Guinea","GR":"Greece","GS":"South Georgia and South Sandwich Islands","GT":"Guatemala","GU":"Guam","GW":"Guinea-Bissau","GY":"Guyana",
    "HK":"Hong Kong","HM":"Heard Island and McDonald Islands","HN":"Honduras","HR":"Croatia","HT":"Haiti","HU":"Hungary","ID":"Indonesia","IE":"Ireland","IL":"Israel","IM":"Isle of Man","IN":"India","IO":"British Indian Ocean Territory","IQ":"Iraq","IR":"Iran","IS":"Iceland","IT":"Italy","JE":"Jersey","JM":"Jamaica","JO":"Jordan","JP":"Japan",
    "KE":"Kenya","KG":"Kyrgyzstan","KH":"Cambodia","KI":"Kiribati","KM":"Comoros","KN":"Saint Kitts and Nevis","KP":"North Korea","KR":"South Korea","KW":"Kuwait","KY":"Cayman Islands","KZ":"Kazakhstan","LA":"Laos","LB":"Lebanon","LC":"Saint Lucia","LI":"Liechtenstein","LK":"Sri Lanka","LR":"Liberia","LS":"Lesotho","LT":"Lithuania","LU":"Luxembourg","LV":"Latvia","LY":"Libya",
    "MA":"Morocco","MC":"Monaco","MD":"Moldova","ME":"Montenegro","MF":"Saint Martin","MG":"Madagascar","MH":"Marshall Islands","MK":"North Macedonia","ML":"Mali","MM":"Myanmar","MN":"Mongolia","MO":"Macao","MP":"Northern Mariana Islands","MQ":"Martinique","MR":"Mauritania","MS":"Montserrat","MT":"Malta","MU":"Mauritius","MV":"Maldives","MW":"Malawi","MX":"Mexico","MY":"Malaysia","MZ":"Mozambique",
    "NA":"Namibia","NC":"New Caledonia","NE":"Niger","NF":"Norfolk Island","NG":"Nigeria","NI":"Nicaragua","NL":"Netherlands","NO":"Norway","NP":"Nepal","NR":"Nauru","NU":"Niue","NZ":"New Zealand","OM":"Oman","PA":"Panama","PE":"Peru","PF":"French Polynesia","PG":"Papua New Guinea","PH":"Philippines","PK":"Pakistan","PL":"Poland","PM":"Saint Pierre and Miquelon","PN":"Pitcairn","PR":"Puerto Rico","PS":"Palestine","PT":"Portugal","PW":"Palau","PY":"Paraguay",
    "QA":"Qatar","RE":"Réunion","RO":"Romania","RS":"Serbia","RU":"Russia","RW":"Rwanda","SA":"Saudi Arabia","SB":"Solomon Islands","SC":"Seychelles","SD":"Sudan","SE":"Sweden","SG":"Singapore","SH":"Saint Helena","SI":"Slovenia","SJ":"Svalbard and Jan Mayen","SK":"Slovakia","SL":"Sierra Leone","SM":"San Marino","SN":"Senegal","SO":"Somalia","SR":"Suriname","SS":"South Sudan","ST":"São Tomé and Príncipe","SV":"El Salvador","SX":"Sint Maarten","SY":"Syria","SZ":"Eswatini",
    "TC":"Turks and Caicos Islands","TD":"Chad","TF":"French Southern Territories","TG":"Togo","TH":"Thailand","TJ":"Tajikistan","TK":"Tokelau","TL":"Timor-Leste","TM":"Turkmenistan","TN":"Tunisia","TO":"Tonga","TR":"Turkey","TT":"Trinidad and Tobago","TV":"Tuvalu","TW":"Taiwan","TZ":"Tanzania","UA":"Ukraine","UG":"Uganda","UM":"United States Minor Outlying Islands","US":"United States","UY":"Uruguay","UZ":"Uzbekistan","VA":"Vatican City","VC":"Saint Vincent and the Grenadines","VE":"Venezuela","VG":"British Virgin Islands","VI":"U.S. Virgin Islands","VN":"Vietnam","VU":"Vanuatu","WF":"Wallis and Futuna","WS":"Samoa","YE":"Yemen","YT":"Mayotte","ZA":"South Africa","ZM":"Zambia","ZW":"Zimbabwe","XK":"Kosovo",
}
ISO_CODES = set(COUNTRY_NAMES)
COUNTRY_ALIASES = {"UK": "GB", "EL": "GR"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_GROUPS = {"news"}
MOVIE_GROUPS = {"movie", "movies", "cinema", "film", "films"}
MUSIC_GROUPS = {"music", "musics"}
KIDS_GROUPS = {"kids", "kid", "children", "childrens"}
DOC_GROUPS = {"documentary", "documentaries", "wildlife", "nature"}
SPORTS_GROUPS = {"sport", "sports"}
RELIGIOUS_GROUPS = {"religious", "religion", "faith"}
NEWS_NAME_RE = re.compile(r"\b(?:news|newsmax|newsnation|headlines?|current affairs|newsroom|cnn|cnbc|bloomberg|reuters|euronews|france\s*24|al\s*jazeera|msnbc|fox\s*news|sky\s*news|bbc\s*(?:news|world)|abc\s*news|cbc\s*news|nbc\s*news|dw\s*news|rt\s*news|ndtv\s*(?:24x7|profit|india|world)|aaj\s*tak|times\s*now|news\s*18|news\s*nation|republic\s*(?:tv|bharat)|india\s*today|tv9\s*(?:bharatvarsh|news|telugu|kannada|marathi|gujarati)|dd\s*news|trt\s*world|tvp\s*world|new\s*china\s*tv)\b", re.IGNORECASE)
RELIGIOUS_NAME_RE = re.compile(r"\b(?:religious|religion|christian|christ|gospel|bible|jesus|church|catholic|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|jain|buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|prarthana|darshan|worship|sermon|evangelical|zoroastrian|ministry|dharma|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|deity|faith\s*tv|holy\s*mass|orthodox|shrine)\b", re.IGNORECASE)
ISLAMIC_NAME_RE = re.compile(r"\b(?:islam|islamic|muslim|quran|koran|sunnah|sunna|mecca|makkah|madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|allah|muhammad|mohammad|madani|iqra(?:a)?|peace\s*tv|kaaba|kabah|huda\s*tv|hidayat\s*tv|takbeer|ahlulbayt|mta\s*(?:international|world|1)|quran\s*kareem|al\s*huda|saudi\s*quran|holy\s*quran)\b", re.IGNORECASE)
BAD_NAME_RE = re.compile(r"\b(?:vod|video\s*on\s*demand|catch[\s-]?up|test|demo|webcam|podcast|radio|timeshift|time\s*shift|ppv|pay\s*per\s*view|preview|sample|placeholder|coming\s*soon)\b", re.IGNORECASE)
BAD_HOST_PARTS = ("localhost", "workers.dev", "worker.dev", "pages.dev", "corsproxy", "cors-proxy", "proxy.example", "streamproxy")
BAD_QUERY_KEYS = {"token", "auth", "authorization", "password", "passwd", "pwd", "username", "signature", "sig", "expires", "hdnts", "jwt", "session", "key"}


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
    return next((line.strip() for line in block[1:] if line.strip().startswith(("http://", "https://"))), "")


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"\b(?:backup|uhd|fhd|hd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value)
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
        if bool(groups & MOVIE_GROUPS) or re.search(r"\b(?:movies?|cinema|films?)\b", name, re.I):
            return "Indian Movies", None, country
        if bool(groups & MUSIC_GROUPS) or re.search(r"\b(?:music|musix|musica|musique)\b", name, re.I):
            return "Indian Music", None, country
        language = (a.get("tvg-language") or "").casefold()
        if any(code in {"ben", "bn"} for code in re.split(r"[;,|/\s]+", language)) or re.search(r"\b(?:bangla|bengali)\b", name, re.I):
            return "Indian Bangla", None, country
        return "Indian Entertainment", None, country
    return "International", None, country


def country_group(country: str) -> str | None:
    return COUNTRY_NAMES.get(country) if country in COUNTRY_NAMES else None


def eligible_country_code(a: dict[str, str], name: str) -> str:
    group, reason, country = policy_group(a, name)
    if reason or country in {"ZZ", "BD", "IN", "PK"}:
        return ""
    if group in {"Religious", "Sports", "Kids", "Documentary & Wildlife"}:
        return ""
    return country if country_group(country) else ""


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
        if "unused" in relative_parts or path.name.casefold() in {"default.png", "placeholder.png", "no-logo.png", "nologo.png", "unknown.png", "blank.png", "generic.png", "favicon.png"}:
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
    if re.search(r"placeholder|generic|no[-_]?logo|unknown|blank|favicon", parsed.path, re.I):
        return None
    try:
        request = urllib.request.Request(source_url, headers={"User-Agent": "BDIX-IPTV-International-Discovery/1.0"})
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
            extension = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp", "image/svg+xml": ".svg"}.get(content_type)
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
    ident = (a.get("tvg-id") or a.get("channel-id") or "").strip() or "custom.intl." + slug(clean_name).replace("-", ".")
    fields = [f'tvg-id="{ident}"', f'tvg-name="{clean_name}"']
    if logo and logo.startswith(RAW_BASE):
        fields.append(f'tvg-logo="{logo}"')
    fields.append(f'tvg-country="{country}"')
    language = (a.get("tvg-language") or "").strip().replace('"', "")
    if language:
        fields.append(f'tvg-language="{language}"')
    fields.append(f'channel-id="{(a.get("channel-id") or ident).replace(chr(34), "").strip()}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + clean_name


def natural_key(value: str):
    return tuple(int(piece) if piece.isdigit() else piece.casefold() for piece in re.split(r"(\d+)", value or ""))


def localize_candidate_logo(a: dict[str, str], name: str, fallback: str = "") -> str:
    existing = local_logo_for(name)
    if existing:
        return logo_uri(existing)
    downloaded = download_logo((a.get("tvg-logo") or "").strip(), name)
    if downloaded:
        return logo_uri(downloaded)
    if fallback.startswith(RAW_BASE):
        relative = urllib.parse.urlsplit(fallback).path.split("/logos/", 1)[-1]
        if relative and (LOGOS / relative).is_file() and "unused" not in Path(relative).parts:
            return fallback
    return ""


def fetch_source() -> str:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "BDIX-IPTV-International-Discovery/1.0"})
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
    existing_country_counts: Counter[str] = Counter()
    established_groups: set[str] = set()
    for block in existing_blocks:
        if not block:
            continue
        a = attrs(block[0])
        name = name_of(block[0])
        key = norm(name)
        group = a.get("group-title", "").strip()
        if key and group.casefold() not in LEGACY_STAGING_GROUPS:
            existing_names[key].append(a)
        country = eligible_country_code(a, name)
        if country:
            existing_country_counts[country] += 1
            if group.casefold() == COUNTRY_NAMES[country].casefold():
                established_groups.add(country)

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
            rejected[reason or "invalid URL"] += 1
            continue
        key_url = url.casefold()
        if key_url in existing_urls or key_url in seen_source_urls:
            rejected["duplicate or existing stream URL"] += 1
            continue
        group, reason, country = policy_group(a, name)
        if group is None:
            rejected[reason or "policy exclusion"] += 1
            continue
        seen_source_urls.add(key_url)
        candidates.append({"attrs": a, "name": name, "url": url, "key": norm(name), "group": group, "country": country, "directives": [line for line in block[1:] if line.strip().startswith("#EXTVLCOPT:") or line.strip().startswith("#KODIPROP:")]})

    candidate_country_counts: Counter[str] = Counter()
    for candidate in candidates:
        code = eligible_country_code(candidate["attrs"], candidate["name"])
        if code:
            candidate_country_counts[code] += 1
    country_counts = existing_country_counts + candidate_country_counts
    established_countries = set(established_groups)
    established_countries.update(code for code, count in country_counts.items() if count >= COUNTRY_THRESHOLD)
    country_groups = {code: country_group(code) for code in established_countries if country_group(code)}

    planned_names = {key: values[:] for key, values in existing_names.items()}
    additions: list[list[str]] = []
    new_primary_rows = []
    new_backup_rows = []
    per_group = Counter()
    for candidate in candidates:
        name, key = candidate["name"], candidate["key"]
        if not key:
            rejected["unmatchable channel identity"] += 1
            continue
        is_backup = key in planned_names
        if is_backup and len(new_backup_rows) >= MAX_NEW_BACKUPS:
            rejected["backup limit reached for this run"] += 1
            continue
        if not is_backup and len(new_primary_rows) >= MAX_NEW_CHANNELS:
            rejected["new-channel limit reached for this run"] += 1
            continue
        country = candidate["country"]
        if country in country_groups and country not in {"BD", "IN", "PK"} and candidate["group"] not in {"Religious", "Sports", "Kids", "Documentary & Wildlife"}:
            target_group = country_groups[country]
        else:
            target_group = "Backup" if is_backup else candidate["group"]
        if not is_backup and per_group[target_group] >= MAX_NEW_PER_GROUP:
            rejected["per-group limit reached for this run"] += 1
            continue
        canonical_attrs = planned_names[key][0] if is_backup and planned_names[key] else candidate["attrs"]
        canonical_name = (canonical_attrs.get("tvg-name") or name).strip() if is_backup else name
        canonical_country = country_of(canonical_attrs) if is_backup else country
        inherited_logo = (canonical_attrs.get("tvg-logo") or "").strip() if is_backup else ""
        logo = localize_candidate_logo(candidate["attrs"], canonical_name, inherited_logo)
        group = "Backup" if is_backup else target_group
        extinf = make_extinf(canonical_attrs if is_backup else candidate["attrs"], canonical_name, group, canonical_country, logo)
        additions.append([extinf, *candidate["directives"], candidate["url"]])
        if is_backup:
            new_backup_rows.append({"name": canonical_name, "country": canonical_country})
        else:
            new_primary_rows.append({"name": name, "group": target_group, "country": country})
            per_group[target_group] += 1
            planned_names.setdefault(key, []).append(attrs(extinf))

    # Remove obsolete staging groups and migrate generic international entries
    # into a country group once that country reaches five legitimate channels.
    all_blocks = existing_blocks + additions
    migrated = []
    normalized = []
    for block in all_blocks:
        if not block:
            continue
        a = attrs(block[0])
        name = name_of(block[0])
        old_group = a.get("group-title", "").strip()
        lower_group = old_group.casefold()
        if lower_group in {"new channels", "new backup", "not playing"}:
            a["group-title"] = "International"
            lower_group = "international"
        code = eligible_country_code(a, name)
        if code in country_groups and lower_group in {"international", "international movies", "international music"}:
            target = country_groups[code]
            if old_group != target:
                block[0] = make_extinf(a, name, target, code, a.get("tvg-logo", ""))
                migrated.append({"name": name, "from": old_group or "(none)", "to": target})
        normalized.append(block)

    rank = {name: index for index, name in enumerate(FIXED_GROUPS)}
    rank.update({name: index for index, name in enumerate(sorted(country_groups.values()), start=len(FIXED_GROUPS))})
    rank.update({name: len(FIXED_GROUPS) + len(country_groups) + index for index, name in enumerate(TAIL_GROUPS)})
    normalized.sort(key=lambda block: (rank.get(attrs(block[0]).get("group-title", "").strip(), len(rank)), natural_key(name_of(block[0])), url_of(block).casefold()))

    updated_prefix = [line for line in prefix if not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    dynamic_order = FIXED_GROUPS + sorted(country_groups.values()) + TAIL_GROUPS
    header = '#PLAYLIST-STUDIO-CATEGORIES:' + str(dynamic_order).replace("'", '"')
    extm3u_index = next((i + 1 for i, line in enumerate(updated_prefix) if line.startswith("#EXTM3U")), 0)
    updated_prefix.insert(extm3u_index, header)
    output = updated_prefix[:]
    for block in normalized:
        output.extend(block)
    PLAYLIST.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report_lines = ["# International Channel Discovery", "", f"- Last scan: {timestamp}", "- Source: IPTV-org categorized worldwide channel index.", "- Playback was not tested.", f"- Country-group threshold: {COUNTRY_THRESHOLD} legitimate channels, or an already-established country group.", f"- New channels added: {len(new_primary_rows)}", f"- Backup streams added: {len(new_backup_rows)}", f"- Existing entries migrated into country groups: {len(migrated)}", f"- Country groups currently established: {', '.join(sorted(country_groups.values())) or 'none'}", "", "## New Channels", ""]
    report_lines.extend(f"- **{row['name']}** — {row['group']} — {row['country']}" for row in new_primary_rows)
    report_lines += ["", "## New Backup Streams", ""]
    report_lines.extend(f"- **{row['name']}** — {row['country']}" for row in new_backup_rows)
    report_lines += ["", "## Country-group migrations", ""]
    report_lines.extend(f"- **{row['name']}**: `{row['from']}` → `{row['to']}`" for row in migrated)
    report_lines += ["", "## Filtering", ""]
    report_lines.extend(f"- {reason}: {count}" for reason, count in sorted(rejected.items()))
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    write_step_summary("\n".join(["# International Channel Discovery", "", f"- New channels: {len(new_primary_rows)}", f"- Backup streams: {len(new_backup_rows)}", f"- Country-group migrations: {len(migrated)}", f"- Established country groups: {', '.join(sorted(country_groups.values())) or 'none'}", "- Playback testing: not performed."]))
    print(f"International discovery complete: new={len(new_primary_rows)} backup={len(new_backup_rows)} migrated={len(migrated)} country_groups={len(country_groups)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
