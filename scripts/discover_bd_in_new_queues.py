#!/usr/bin/env python3
"""Discover Bangladesh/India candidates into manual-review queues.

The source feed sets policy scope, not a hard metadata-verification gate. Keep
source metadata as supplied; country, IDs, language and logos can be corrected
after owner review. Definite policy/URL exclusions and duplicate stream URLs
prevent queueing. Dead streams are removed by the subsequent probe; inconclusive
streams remain for manual review.

Bangladesh channels of all genres are eligible. Indian News, Kids, Education,
Knowledge, Business/Finance and all Religious channels are excluded from this
IPTV playlist discovery policy. International retains its separate policy.
"""
# Owner-authorized policy-alignment retry marker (2026-11-19).

from __future__ import annotations
import json, re, unicodedata, urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlparse

from country_verification import norm_name
from stream_url_identity import stream_url_key

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
# Legacy India exclusions are retained for the International playlist's distinct policy.
FORBIDDEN_CATEGORY_PATTERNS = {
    "news": re.compile(r"\b(?:news|headlines?|current affairs|newsroom|gnt)\b", re.IGNORECASE),
    "religious": re.compile(r"\b(?:religious|religion|darshana tv|angel|hosanna|devotional|bhakti|bhakthi|spiritual|worship|gospel|christian|christ|hindu|hinduism|sanatan|sikh|gurbani|gurubani|church|temple|sermons?|prayer|madani|iqra|huda|noor|deen|mta|qtv|islam|islamic|muslim|quran|quranic|koran|allah|muhammad|mohammed|hadith|sunnah|salafi|sufi|ramadan|mecca|makkah|madinah|medina|masjid|mosque|ummah|deen|fiqh|tafsir|azan|adhan|jumuah|hajj|umrah|kaaba|sharia|peace\s*tv)\b", re.IGNORECASE),
}
# Strict India-only exclusions for IPTV-Playlist.m3u. Bangladesh remains
# unrestricted; International does not opt into this additional policy.
IPTV_KNOWN_INDIAN_EDUCATION_NAMES = {
    "vyas channel", "shiksha tv", "gyandarshan", "gyandarshan hd",
    "dd gyan darshan", "kite victers", "victers", "swayam prabha",
}
IPTV_KNOWN_INDIAN_EDUCATION_IDS = {
    "vyaschannel.in", "shikshatv.in", "gyandarshan.in", "gyandarshanhd.in",
    "ddgyandarshan.in", "kitevicters.in", "victers.in", "swayamprabha.in",
}
IPTV_FORBIDDEN_CATEGORY_PATTERNS = {
    "news": re.compile(r"\b(?:news(?:\s*\d+)?|headlines?|current affairs|newsroom|bulletin|breaking news|gnt|aaj tak|india today|times now|republic(?:\s+(?:bharat|bangla))?|abp(?:\s+ananda)?|zee news|wion|tv\s*9)\b", re.I),
    "kids": re.compile(r"\b(?:kids?|children|childrens|cartoon|animation|animated|junior|nick jr|nickelodeon|disney junior|disney channel|baby tv|pogo|hungama|sonic|discovery kids|green gold|sony yay)\b", re.I),
    "education": re.compile(r"\b(?:education(?:al)?|higher education|university|universities|college|school|e[ -]?learning|learning channel|academic|curriculum|lecture|classroom|courseware|shiksha|vidya|vyas channel|gyandarshan|gyan darshan|swayam|victers|diksha|e[ -]?vidya|educational television|vtu)\b", re.I),
    "knowledge": re.compile(r"\b(?:knowledge|documentary|documentaries|science|scientific|discovery|exploration|history|geography|wildlife|nature|national geographic|animal planet|discovery channel|discovery science|discovery turbo|history tv|inwild|safari tv|dd kisan|krishi darshan|agriculture|agricultural|farming|farmer)\b", re.I),
    "business": re.compile(r"\b(?:business|finance|financial|stock market|share market|market news|economy|economic|corporate|investment|investing|trading|money|cnbc|zee business|ndtv profit|et now|moneycontrol|bloomberg)\b", re.I),
    "religious": re.compile(r"\b(?:religious|religion|devotional|bhakti|bhakthi|spiritual|worship|gospel|christian|christ|hindu|hinduism|sanatan|sikh|gurbani|gurubani|church|temple|sermons?|prayer|islam|islamic|muslim|quran|quranic|koran|allah|muhammad|mohammed|hadith|sunnah|salafi|sufi|ramadan|mecca|makkah|madinah|medina|masjid|mosque|ummah|fiqh|tafsir|azan|adhan|jumuah|hajj|umrah|kaaba|sharia|peace\s*tv|angel|hosanna|madani|iqra|huda|noor|deen|mta|qtv|aastha|sadhna|sanskar|jinvani|satsang|jagran|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|calvary|santvani|sharnam|disha tv)\b", re.I),
}
DISCOVERY_EXTRA_CATEGORY_PATTERNS = {}

def canonical_channel_name(value: str) -> str:
    value = re.sub(r"\([^)]*\)|\[[^]]*\]", " ", str(value or ""))
    value = re.sub(r"\b(?:\d{3,4}p|uhd|fhd|hd|sd|4k)\b", " ", value, flags=re.IGNORECASE)
    value = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()

IPTV_KNOWN_INDIAN_CATEGORY_NAMES = {
    "news": {"r plus", "r plus gold", "bhi channel", "tv 100", "tv 100 national"},
    "kids": {"sony yay", "disney channel", "jungle book", "doraemon"},
    "education": {"vtu"},
    "knowledge": {"dd kisan", "krishi darshan"},
    "religious": {"disha tv", "q tv", "shekinah tv", "darshana tv"},
}
IPTV_KNOWN_INDIAN_CATEGORY_IDS = {
    "rplus.in": "news", "rplusgold.in": "news", "bhi.channel.in": "news", "tv100.in": "news", "tv100national.in": "news",
    "sonyyay.in": "kids", "vtu.in": "education", "dishatv.in": "religious", "qtv.in": "religious", "shekinahtv.in": "religious", "darshanatv.in": "religious",
    "ddkisan.in": "knowledge", "krishidarshan.in": "knowledge",
}


def known_indian_forbidden_category(a: dict[str, str], name: str) -> str | None:
    """Resolve known Indian channels whose names alone do not reveal their genre."""
    names = {
        canonical_channel_name(value)
        for value in (name, a.get("tvg-name", ""))
        if str(value or "").strip()
    }
    ids = {
        str(a.get(key, "")).strip().casefold().split("@", 1)[0]
        for key in ("tvg-id", "channel-id") if a.get(key)
    }
    if names & IPTV_KNOWN_INDIAN_EDUCATION_NAMES or ids & IPTV_KNOWN_INDIAN_EDUCATION_IDS:
        return "education"
    for category, aliases in IPTV_KNOWN_INDIAN_CATEGORY_NAMES.items():
        if names & aliases:
            return category
    for channel_id in ids:
        category = IPTV_KNOWN_INDIAN_CATEGORY_IDS.get(channel_id)
        if category:
            return category
    return None


def is_indian_discovery_candidate(a: dict[str, str], name: str) -> bool:
    """Infer India from source country, country metadata, ID suffix, then alias.

    Explicit source-country metadata wins. If tvg-country conflicts with a
    recognized BD/IN ID suffix, retain the country-code evidence; otherwise an
    explicit non-BD/IN country prevents a name-only Indian alias from overriding it.
    """
    source_country = str(a.get("x-discovery-source-country", "")).strip().upper()
    if source_country:
        return source_country == "IN"
    declared_country = str(a.get("tvg-country", "")).strip().upper()
    if declared_country in {"BD", "IN"}:
        return declared_country == "IN"
    if declared_country:
        id_only = dict(a)
        id_only["tvg-country"] = ""
        id_country = channel_country(id_only)
        return id_country == "IN"
    resolved = channel_country(a)
    if resolved:
        return resolved == "IN"
    return known_indian_forbidden_category(a, name) is not None

PERMANENTLY_BANNED_CHANNEL_NAMES = {
    canonical_channel_name(name) for name in (
        "E-Vidya 10",
        "E-Vidya 11",
        "E-Vidya 12",
        "E-Vidya 4",
        "E-Vidya 5",
        "E-Vidya 6",
        "E-Vidya 7",
        "E-Vidya 8",
        "E-Vidya 9",
        "Friends TV",
        "HSTV",
        "4 SiDES TV",
        "DD India",
        "Global Punjab",
        "Jan TV",
        "Kaumudy TV",
        "Nandighosha TV",
        "Odisha TV",
        "Raftaar Media",
        "Taaza TV",
        "Tamilan TV",
        "Tehzeeb TV",
        "NKR TV Kannada",
        "Ayush TV",
        "VCV",
        "KCL TV",
        "Jeevan TV",
        "Siri Kannada All Time",
        "Pankh",
        "Starnet",
        "Unique TV",
        "Subin TV",
        "TV BRICS English",
        "Mei Alai TV",
        "Makkal TV",
        "Madhimugam TV",
        "Bangla Jago TV",
        "DD Bharati",
        "Food Food",
        "Discovery Turbo India",
        "XXTreme Jobs Hindi",
        "Power Turk",
        "Safari TV Tamil",
    )
}
# Stable base channel IDs (region/quality suffixes after "@" are ignored). This
# exact-ID denylist prevents renamed aliases and alternate feeds from returning.
PERMANENTLY_BANNED_CHANNEL_IDS = {
    "4sidestv.in",
    "ddindia.in",
    "globalpunjab.in",
    "jantv.in",
    "kaumudytv.in",
    "nandighoshatv.in",
    "odishatv.in",
    "raftaarmedia.in",
    "taazatv.in",
    "tamilantv.in",
    "tehzeebtv.in",
    "nkrtvkannada.in",
    "ayushtv.in",
    "vcv.in",
    "kcltv.in",
    "jeevantv.in",
    "sirikannadaalltime.in",
    "pankh.in",
    "starnet.in",
    "uniquetv.in",
    "subintv.in",
    "tvbricsenglish.in",
    "meialaitv.in",
    "makkaltv.in",
    "madhimugamtv.in",
    "banglajagotv.in",
    "ddbharati.in",
    "foodfood.in",
    "discoveryturbo.in",
    "xxtremejobshindi.in",
    "powerturktv.tr",
}
# A programme title is not a standalone linear TV channel. Keep this exact
# denylist narrow so incomplete optional metadata alone never blocks a channel.
NON_CHANNEL_PROGRAM_NAMES = {canonical_channel_name("Gopal Bhar")}

FORBIDDEN_WORDS = {"news"}
ISLAMIC_ALLOWED_MARKERS = re.compile(
    r"\b(?:islamic|islam|muslim|qur['’]?an|madani|peace\s*tv|huda|noor|deen|ummah|"
    r"makkah|mecca|madina|al\s*furqan|sunnah|mta|qtv|iqra|hadith|ramadan|hajj|umrah|masjid|mosque|azan|adhan|kaaba|sharia)\b",
    re.IGNORECASE,
)
NON_ISLAMIC_RELIGIOUS_MARKERS = re.compile(
    r"\b(?:angel|hosanna|gospel|christian|christ|hindu|hinduism|sanatan|sikh|"
    r"gurbani|gurubani|church|temple|calvary|santvani|sharnam|sharanam|aastha|"
    r"sadhna|sanskar|jinvani|satsang|jagran|bhagwat|aradhana|prarthana|divya|"
    r"shubh|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|"
    r"deity|holy\s*mass|orthodox|shrine)\b",
    re.IGNORECASE,
)
FORBIDDEN_BRANDS = re.compile(
    r"\b(?:"
    r"network\s*10|saam\s*tv|total\s*tv(?:\s*haryana)?|calvary\s*tv|santvani(?:\s+channel)?|sharnam\s*tv|sharanam\s*tv|aad(?:i|ee)nath|aaseervatham|aastha|sadhna|sanskar|jinvani|satsang|jagran|"
    r"bhagwat|aradhana|prarthana|divya|shubh\s*tv|aagaaz\s+times|"
    r"aaj\s+ki\s+khabar|abp(?:\s+(?:ananda|asmita|ganga|majha|news))?|"
    r"abn\s+andhra\s+jyoti|aaj\s+tak|times\s+now|india\s+today|news18|"
    r"ndtv\s+profit|ndtv\s+24x7|republic(?:\s+bharat|\s+tv)?|news\s+nation|"
    r"sudarshan\s+news|tv9(?:\s+\w+)?|zee\s+news|"
    r"cnbc(?:\s+awaaz|\s+bajar|\s+tv18(?:\s+prime)?)?|dd\s+news|"
    r"et\s+now|mirror\s+now|bharat\s+samachar|pratidin\s+time|amrit\s+gurbani|"
    r"sansad\s+tv(?:\s+[12])?|zee\s+business|"
    
    r""
    r""
    r"sai\s+tv|darshana\s+tv|sarv\s+dharm\s+sangam"
    r")\b",
    re.IGNORECASE,
)
BAD_HOSTS = ("proxy", "proxied", "cors", "localhost", "workers.dev", "worker.dev", "pages.dev")
# Expiry timestamps are not authentication failures by themselves. Keep rejecting
# credentials/signatures; preserve ordinary expires/e query parameters unchanged.
BAD_QUERY_KEYS = {"token", "auth", "authorization", "hdnts", "sig", "signature", "session", "jwt", "ticket", "key"}
QUALITY = {"uhd", "fhd", "hd", "sd", "4k", "1080p", "720p", "576p", "480p", "360p", "240p"}
COUNTRY_CODE = {"Bangladesh": "bd", "India": "in"}
# Country-group threshold used by discovery-policy validation. A new country group
# must not be created from fewer than five legitimate primary identities.
COUNTRY_THRESHOLD = 5
OTHER_PLAYLISTS = (Path("International-Playlist.m3u"),)
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
        while j < len(lines):
            candidate = lines[j].strip()
            if not candidate or (candidate.startswith("#") and not candidate.startswith("#EXTINF:")):
                j += 1
                continue
            break
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


def prohibited_channel(
    a: dict[str, str],
    name: str,
    country: str | None = None,
    *,
    discovery: bool = False,
    iptv_discovery: bool = False,
) -> str | None:
    """Apply legacy active-channel exclusions, plus optional IPTV discovery-only genres."""
    ids = {
        (value or "").strip().casefold().split("@", 1)[0]
        for value in (a.get("tvg-id", ""), a.get("channel-id", ""))
        if (value or "").strip()
    }
    if ids & PERMANENTLY_BANNED_CHANNEL_IDS:
        return "permanently banned channel"
    for candidate in (name, a.get("tvg-name", "")):
        if canonical_channel_name(candidate) in PERMANENTLY_BANNED_CHANNEL_NAMES:
            return "permanently banned channel"

    if iptv_discovery:
        source_country = str(a.get("x-discovery-source-country", "")).strip().upper()
        if source_country:
            if source_country not in {"BD", "IN"}:
                return None
            country = source_country
    resolved_country = channel_country(a, country)
    values = " ".join((name, a.get("tvg-name", ""), a.get("tvg-id", ""), a.get("channel-id", "")))
    if iptv_discovery and resolved_country in {None, "IN"} and is_indian_discovery_candidate(a, name):
        known_category = known_indian_forbidden_category(a, name)
        if known_category:
            return f"Indian {known_category} channel is prohibited"
    if resolved_country == "IN" and re.search(r"\bmh\s*1\s*prime\b|\bmh1prime\b", values, re.IGNORECASE):
        return "known Indian prohibited MH One Prime channel is prohibited"
    # Bangladesh is unrestricted by these India-only genre rules.
    if resolved_country != "IN":
        return None

    # Inspect descriptive and classification metadata in addition to display
    # names and group-title. Source feed country takes precedence in evaluate(),
    # so misleading tvg-country/ID metadata cannot bypass this policy.
    metadata_keys = (
        "tvg-id", "channel-id", "tvg-name", "tvg-description", "description",
        "tvg-content", "tvg-genre", "tvg-category", "tvg-categories",
        "genre", "genres", "category", "categories", "group-title",
        "tvg-network", "network", "provider",
    )
    values = " ".join([name] + [str(a.get(key, "")) for key in metadata_keys])
    group = a.get("group-title", "").strip()
    if iptv_discovery:
        normalized_ids = {
            re.sub(r"@.*$", "", str(a.get(key, "")).strip().casefold())
            for key in ("tvg-id", "channel-id") if a.get(key)
        }
        known_category = known_indian_forbidden_category(a, name)
        if known_category:
            return f"Indian {known_category} channel is prohibited"
        expanded_values = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", values)
        for category, pattern in IPTV_FORBIDDEN_CATEGORY_PATTERNS.items():
            if pattern.search(expanded_values):
                return f"Indian {category} channel is prohibited"
    else:
        for category, pattern in FORBIDDEN_CATEGORY_PATTERNS.items():
            if category == "religious" and ISLAMIC_ALLOWED_MARKERS.search(values) and not NON_ISLAMIC_RELIGIOUS_MARKERS.search(values):
                continue
            if pattern.search(group) or pattern.search(values):
                return f"Indian {category} channel is prohibited"
        if discovery:
            for category, pattern in DISCOVERY_EXTRA_CATEGORY_PATTERNS.items():
                if pattern.search(group) or pattern.search(values):
                    return f"Indian {category} channel is prohibited"
    if FORBIDDEN_BRANDS.search(values):
        return "known Indian prohibited brand/category is prohibited"
    for word in FORBIDDEN_WORDS:
        if re.search(r"(?<![\\w])" + re.escape(word) + r"(?![\\w])", values, re.UNICODE):
            return f"Indian {word} channel is prohibited"
    return None

def evaluate(country: str, a: dict[str, str], name: str, url: str, reference=None):
    """Return source metadata unchanged when policy and URL checks pass.

    The source-feed country is used for country-specific content exclusions; it
    is not proof that tvg-country or channel IDs are accurate. Missing,
    conflicting or unverified metadata stays in the manual-review queue.
    """
    if country not in COUNTRY_CODE:
        return None, "unknown source feed"
    forbidden = prohibited_channel(a, name, country, discovery=True, iptv_discovery=True)
    if forbidden:
        return None, forbidden
    p = urlparse(url)
    if p.scheme not in {"http", "https"} or not p.netloc or p.fragment:
        return None, "invalid stream URL"
    bad_name = re.sub(r"\btest\b", " ", name, flags=re.IGNORECASE) if re.search(
        r"\btest\s+cricket\b", name, re.IGNORECASE
    ) else name
    if BAD_RE.search(" ".join((bad_name, a.get("tvg-id", ""), a.get("group-title", ""))).casefold()):
        return None, "bad word (vod/test/proxy/...)"
    if any(x in p.netloc.casefold() for x in BAD_HOSTS):
        return None, "proxy/worker host"
    if any(key.casefold() in BAD_QUERY_KEYS for key, _ in parse_qsl(p.query, keep_blank_values=True)):
        return None, "tokenized URL"
    if not (p.path.casefold().endswith((".m3u8", ".m3u", ".ts")) and "vod" not in p.path.casefold() and "catchup" not in p.path.casefold()):
        return None, "unsupported stream path"
    return dict(a), ""


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
        is_discovery_queue = (
            group in queue_groups
            or bool(re.search(r'group-title="(?:New Channels|New Backups|New Backup)"', extinf_line, re.I))
        )
        if is_discovery_queue:
            queue_country = "IN" if is_indian_discovery_candidate(a, name) else None
            reason = prohibited_channel(a, name, queue_country, discovery=True, iptv_discovery=True)
            if not reason and canonical_channel_name(name) in NON_CHANNEL_PROGRAM_NAMES:
                reason = "programme title, not a standalone live TV channel"
            if reason:
                removed.append(name or "(unnamed)")
                continue
        kept.extend(block)
    result = "\n".join(prefix + kept).rstrip() + "\n"
    return result, removed


def extinf(a: dict[str, str], name: str, group: str, country: str) -> str:
    """Build a review-queue row without guessing or repairing metadata."""
    fields = []
    for key in ("tvg-id", "tvg-name", "tvg-logo", "tvg-country", "tvg-language", "channel-id"):
        value = (a.get(key) or "").strip()
        if value:
            fields.append(f'{key}="{name if key == "tvg-name" else value}"')
    if not a.get("tvg-name", "").strip():
        fields.append(f'tvg-name="{name}"')
    fields.append(f'x-discovery-source-country="{COUNTRY_CODE.get(country, "").upper()}"')
    fields.append(f'group-title="{group}"')
    return "#EXTINF:-1 " + " ".join(fields) + "," + name


def main() -> int:
    # The owner authorized removal of prohibited Indian candidates from the two
    # discovery queues. All other existing playlist rows remain untouched.
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    original, purged_existing = purge_forbidden_existing_queue_rows(original)
    entries = parse(original)
    existing_urls = {stream_url_key(u) for _, _, u in entries}
    existing_names = {norm(n) for _, n, _ in entries}
    existing_ids = {base_id(a.get("tvg-id") or a.get("channel-id")) for a, _, _ in entries if base_id(a.get("tvg-id") or a.get("channel-id"))}

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
            key = stream_url_key(url)
            normalized, reason = evaluate(country, a, name, url)
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

    def insert_queue_rows(current_lines, group, additions):
        if not additions:
            return current_lines
        category_order = [
            "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
            "Indian Entertainment", "Pakistani", "International",
            "Documentary & Wildlife", "Kids", "Religious", "Sports",
            "New Channels", "New Backups", "Backup", "Review",
        ]
        rank = {value: index for index, value in enumerate(category_order)}
        matching = [
            i for i, line in enumerate(current_lines)
            if line.startswith("#EXTINF:") and attrs(line).get("group-title", "").strip() == group
        ]
        if matching:
            last = matching[-1]
            insert_at = next(
                (i for i in range(last + 1, len(current_lines)) if current_lines[i].startswith("#EXTINF:")),
                len(current_lines),
            )
        else:
            target_rank = rank[group]
            insert_at = next(
                (i for i, line in enumerate(current_lines)
                 if line.startswith("#EXTINF:")
                 and rank.get(attrs(line).get("group-title", "").strip(), len(rank)) > target_rank),
                len(current_lines),
            )
        current_lines[insert_at:insert_at] = additions
        return current_lines

    lines = original.replace("\r", "").splitlines()
    new_channel_rows = []
    for country, a, name, url in new_channels:
        new_channel_rows.extend([extinf(a, name, "New Channels", country), url])
    new_backup_rows = []
    for country, a, name, url in new_backups:
        new_backup_rows.extend([extinf(a, name, "New Backups", country), url])
    # Modify only the two discovery queues; do not sort or normalize old records.
    lines = insert_queue_rows(lines, "New Channels", new_channel_rows)
    lines = insert_queue_rows(lines, "New Backups", new_backup_rows)

    # Reserve the two manual queues in the Playlist Studio registry immediately
    # before Backup. This changes no existing row, group, channel number or order.
    registry_indexes = [i for i, line in enumerate(lines)
                        if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    if len(registry_indexes) != 1:
        raise SystemExit("Expected exactly one Playlist Studio category registry; refusing discovery write.")
    registry_index = registry_indexes[0]
    try:
        registry = json.loads(lines[registry_index].split(":", 1)[1])
    except (IndexError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Invalid Playlist Studio category registry; refusing discovery write: {exc}")
    if not isinstance(registry, list) or "Backup" not in registry:
        raise SystemExit("Playlist Studio registry has no Backup category; refusing discovery write.")
    for queue in ("New Channels", "New Backups"):
        if queue not in registry:
            registry.insert(registry.index("Backup"), queue)
    lines[registry_index] = "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry, ensure_ascii=False)
    PLAYLIST.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# IPTV Channel Discovery", "",
        f"Generated: **{datetime.now(timezone.utc).isoformat()}**", "",
        "- Sources: Bangladesh + India iptv-org country feeds",
        "- **Discovery scope: Bangladesh and India source feeds. Feed context sets content-policy scope; country metadata is retained as supplied and is not a discovery gate.**",
        "- Bangladesh channels of all genres are eligible. Indian News, Kids, Education, Knowledge, Business/Finance and all Religious channels are prohibited in this IPTV playlist.",
        f"- Previously admitted prohibited Indian queue rows purged: **{len(purged_existing)}**",
        "- Permanent denylist: E-Vidya 4–12, Friends TV, HSTV, and 31 additional channel IDs/names listed in the canonical permanent denylist.",
        f"- Country-group threshold: **{COUNTRY_THRESHOLD}** legitimate primary identities",
        "- Existing manual-review queue rows changed only where they violated the owner-authorized Indian exclusion policy.",
        f"- New channels: **{len(new_channels)}**",
        f"- New backups: **{len(new_backups)}**",
        f"- Rejected/held candidates: **{rejected}**",
        "- Country metadata, channel IDs, language and logos are advisory at this stage; retain uncertain values for owner review and repair later.", "",
        "## Rejection reasons", "",
        *(f"- {r}: {n}" for r, n in sorted(reasons.items())), "",
        "## New Channels", "",
    ]
    report.extend(f"- {name} (source feed: {country}) — {url}" for country, _, name, url in new_channels)
    report += ["", "## New Backups", ""]
    report.extend(f"- {name} (source feed: {country}) — {url}" for country, _, name, url in new_backups)
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Discovery: {len(new_channels)} new channels, {len(new_backups)} new backups, {rejected} rejected; {len(purged_existing)} prohibited Indian queue rows purged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())