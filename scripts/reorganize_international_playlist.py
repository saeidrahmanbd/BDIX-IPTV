#!/usr/bin/env python3
"""Reorganize International-Playlist.m3u with strict naming, country and content rules."""
from collections import Counter, defaultdict
from pathlib import Path
import json
import re
import unicodedata
import discover_international_channels as discovery

PLAYLIST = Path("International-Playlist.m3u")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
FIXED = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani"]
TAIL = ["Fashion TV", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Adult", "New Channels", "New Backups", "Backups"]
BACKUP_GROUPS = {"backup", "backups", "new backup", "new backups"}
INDIAN_GROUPS = {"Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_RE = re.compile(r"\b(news|newsroom|breaking news|headlines?|news\s*24|24\s*news|noticias|notizie|nachrichten|haber|khabar|akhbar|nieuws|actualit[eé]s?|informativo|news\s*tv|tv\s*news|cnbc|cnn|bloomberg|reuters|euronews|france\s*24|al\s*jazeera|msnbc|fox\s*news|sky\s*news|bbc\s*(?:news|world)|abc\s*news|nbc\s*news|dw\s*news|rt\s*news|ndtv|aaj\s*tak|times\s*now|news\s*18|news\s*nation|republic\s*(?:tv|bharat)|india\s*today|tv9|dd\s*news|atn\s*news|dbc\s*news|somoy\s*tv|jamuna\s*tv|channel\s*24|ekattor\s*tv|ekh[oó]n\s*tv|independent\s*tv|wion)\b", re.I)
NON_ISLAM_RE = re.compile(r"\b(christian|christ|gospel|bible|church|catholic|evangel(?:ical)?|orthodox|3abn|three\s*angels|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|guru\s*bani|jain|buddh(?:a|ist|ism)?|temple|mandir|devotional|aarti|satsang|aastha|prarthana|darshan|worship|sermon|zoroastrian|ministry|dharma|krishna|shiva|ganesh|hanuman|bhagwan|vedic|bhagavad|gita|mantra|deity|holy\s*mass|shrine|calvary|god\s*tv|daystar|tbn|cbn|ewtn|sonlife|trinity|shalom|enlace|vida\s*tv|dios|jesus|christ\s*tv)\b", re.I)
ISLAM_RE = re.compile(r"\b(islam(?:ic)?|muslim|quran|qur'an|koran|sunnah|sunna|mecca|makkah|madina|madinah|medina|masjid|mosque|azan|adhan|ramadan|hajj|ummah|allah|muhammad|mohammad|madani|iqra|peace\s*tv|kaaba|kabah|haramain|huda\s*tv|hidayat\s*tv|takbeer|al\s*huda|saudi\s*quran|quran\s*kareem|qtv|deen\s*tv|madina\s*live)\b", re.I)
MOVIE_RE = re.compile(r"\b(movie|movies|cinema|film|films|bollywood|hollywood|aflam|cine|cineplex|ciné|thriller|horror|western|star\s*movies|sony\s*max|zee\s*cinema|b4u\s*movies|jalsha\s*movies|movieplex|fxm|epix|hbo\b|amc\b|ifc\b|turner\s*classic\s*movies|tcm\b|screenpix|cinemax|starz|shemaroo\s*bollywood|goldmines|pictures|movie\s*sphere|moviesphere|filmrise|cinevault|gravitas|kino\b|a?media\s*hit|dom\s*kino|film\+|cine\+|filmua|enterfilm|bolt\b|cinemaraton|cinewow|scream[in]*|persiana\s*cinema|moviestar|rakuten\s*tv.*movies?|cin[eé]\s*nanar|cine\s*western)\b", re.I)
MUSIC_RE = re.compile(r"\b(music|musix|musica|musique|tunes|xite|v2beat|trace\s*urban|kronehit|cmc\s*tv|eu\s*music|ua\s*music|arabica\s*tv|epic\s*music|totalmusic|vevo|qello\s*concerts|concerts|mtv|vh1|now\s*(?:70s|80s|rock|90s)|4music|music\s*box|8xm|9xm|9x\s*(?:jalwa|jhakaas|tashan)|stingray|zoom\s*music|star\s*music|afrobeats|dance\s*tv|melody|sangeet|ptc\s*music|ary\s*music|joo\s*music|balle\s*balle|fuse|axs\s*tv|california\s*music\s*channel|radio|fm\b|ocko|atomic\s*tv|impact\s*tv|fomix|qmusic|canal\s*musica|clap\s*tv)\b", re.I)
DOC_RE = re.compile(r"\b(documentary|documentaries|wildlife|animal\s*planet|nat\s*geo|national\s*geographic|bbc\s*earth|discovery(?:\s*(?:channel|science|turbo|world|life|investigation|family))?|history\s*(?:channel|tv)?|smithsonian|nature|love\s*nature|wild\s*earth|science\s*channel|inwild|inwonder|investigation\s*discovery|destination\s*america|american\s*heroes\s*channel|motortrend|powernation|food\s*network|cooking\s*channel|crime\s*and\s*investigation)\b", re.I)
KIDS_RE = re.compile(r"\b(kids?|children|cartoon|baby\s*shark|disney\s*(?:jr|junior|channel|xd)|nick(?:elodeon)?(?:\s*jr|\s*junior|\s*toons)?|pogo|pbs\s*kids|toongoggles?|toonami|teletubbies|doraemon|discovery\s*kids|mr\s*bean\s*animated|strawberry\s*shortcake|smurf(?:s)?\s*tv|duck\s*tv|zoo\s*moo|boomerang|spacetoon|kartoon|lego\s*channel|caillou|jungle\s*book|moonbug|retrocrush|pop\s*kids|tinypop|yugioh|yu-gi-oh|ebs\s*kids|trt\s*cocuk)\b", re.I)
SPORTS_RE = re.compile(r"\b(sports?|football|soccer|basketball|tennis|cricket|golf|racing|motorsport|fight|boxing|wrestling|ufc|esports?|arena\s*sport|league|espn|fox\s*sports|bein\s*sport|sky\s*sports|eurosport|nba|nfl|nhl|mlb|fifa|olympic|horse\s*racing|willow|ten\s*sports|sony\s*sports|star\s*sports|sport\s*tv|sport1|setanta|sportitalia|motorvision|real\s*madrid\s*tv)\b", re.I)
ADULT_RE = re.compile(r"\b(adult|xxx|porn|erotic|redlight|playboy|penthouse|hustler|brazzers|dorcel|blue\s*hustler|satisfaction|sexy|babes|private\s*tv|desire\s*tv|passion\s*tv|hot\s*adult)\b", re.I)
FASHION_RE = re.compile(r"\bfashion\s*tv\b", re.I)
GENERAL_OUT_OF_SCOPE_RE = re.compile(r"\b(servus\s*tv|star\s*channel|warner\s*(?:channel|tv)|persiana\s*(?:family|iranian|korea|plus)|nile\s*drama|mbc\s*\+?\s*drama|groovy\s*tv|mci\s*television|general\s*entertainment|variety\s*channel)\b", re.I)
MANUAL_NEWS = {"rplus", "rplusnews", "rplusnews24x7"}
MANUAL_COUNTRY = {"rajdhanitv": "BD", "sonimax": "IN", "sonimax2": "IN", "asiansonimax2": "IN", "shemaroobollywood": "IN"}
MANUAL_GROUP = {"sonimax": "Indian Movies", "sonimax2": "Indian Movies", "asiansonimax2": "Indian Movies", "shemaroobollywood": "Indian Movies"}
COUNTRY_NAME_BY_NORMALIZED = {
    re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().casefold()): code
    for code, name in discovery.COUNTRY_NAMES.items()
}
for alias, code in {"uk":"GB", "usa":"US", "unitedstatesofamerica":"US", "czechia":"CZ", "czechrepublic":"CZ", "southkorea":"KR", "northkorea":"KP", "uae":"AE", "macedonia":"MK", "northmacedonia":"MK", "thenetherlands":"NL"}.items():
    COUNTRY_NAME_BY_NORMALIZED[alias] = code

def attrs(line):
    return dict(ATTR_RE.findall(line))

def split_info(line):
    quoted = False
    escaped = False
    for i, char in enumerate(line):
        if char == '"' and not escaped:
            quoted = not quoted
        if char == "," and not quoted:
            return line[:i], line[i + 1:]
        if char == "\\" and not escaped:
            escaped = True
        else:
            escaped = False
    return line, ""

def normalize_key(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"\b(?:backup|uhd|fhd|hd|sd|4k|8k|hevc|h\.?265|\d{3,4}\s*[pi])\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)

def clean_name(value):
    value = str(value or "").replace('"', "").strip()
    value = re.sub(r"\b(?:geo[\s-]?blocked|geo[\s-]?block|not\s*24/7|not\s*24\s*/\s*7|not\s*24h|not\s*24\s*hours)\b", " ", value, flags=re.I)
    value = re.sub(r"[\[(]\s*\d{3,4}\s*[pi]\s*[\])]", " ", value, flags=re.I)
    value = re.sub(r"\b\d{3,4}\s*[pi]\b", " ", value, flags=re.I)
    value = re.sub(r"[\[(]\s*(?:UHD|FHD|HD(?:\+)?|SD|4K|8K|HEVC|H\.?265)\s*[\])]", " ", value, flags=re.I)
    value = re.sub(r"\s+\b(?:UHD|FHD|HD(?:\+)?|SD|4K|8K|HEVC|H\.?265)\b\s*$", " ", value, flags=re.I)
    value = re.sub(r"\s*\[(?:test|demo|placeholder|sample)\]\s*", " ", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip(" \t\r\n-–|,.")

def channel_key(name):
    key = normalize_key(clean_name(name))
    if key in {"rajdhani", "rajdhanitv", "rajdhanitvsd"}:
        return "rajdhanitv"
    return key

def country_from_group(group):
    key = normalize_key(group)
    return next((cc for cc, name in discovery.COUNTRY_NAMES.items() if normalize_key(name) == key), None)

def country_code(a, group, name):
    key = channel_key(name)
    if key in MANUAL_COUNTRY:
        return MANUAL_COUNTRY[key]
    ident = (a.get("tvg-id") or a.get("channel-id") or "").strip()
    parts = ident.split("@")
    if len(parts) > 1:
        variant = re.sub(r"[^a-z0-9]+", "", parts[-1].casefold())
        if variant in COUNTRY_NAME_BY_NORMALIZED:
            return COUNTRY_NAME_BY_NORMALIZED[variant]
    match = re.search(r"\.([a-z]{2})(?:@[^.]*)?$", ident, re.I)
    if match and match.group(1).upper() in discovery.ISO_CODES:
        return discovery.ALIASES.get(match.group(1).upper(), match.group(1).upper())
    raw = (a.get("tvg-country") or "").split(";")[0].split(",")[0].strip().upper()
    if raw in discovery.ISO_CODES:
        return discovery.ALIASES.get(raw, raw)
    if group == "Bangladesh":
        return "BD"
    if group in INDIAN_GROUPS:
        return "IN"
    if group == "Pakistani":
        return "PK"
    return country_from_group(group) or "ZZ"

def parse_playlist(text):
    preamble, blocks, current = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
            if line.strip().startswith(("http://", "https://")):
                blocks.append(current)
                current = None
    if current is not None:
        blocks.append(current)
    return preamble, blocks

def url_of(block):
    return next((line.strip() for line in block[1:] if line.strip().startswith(("http://", "https://"))), "")

def local_logo_path(logo):
    logo = str(logo or "").strip()
    if logo.startswith(RAW_BASE):
        rel = logo[len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0]
    elif logo.startswith("logos/"):
        rel = logo[len("logos/"):].split("?", 1)[0].split("#", 1)[0]
    else:
        return None
    rel = rel.replace("%20", " ")
    path = LOGOS / rel
    if not rel or "unused" in {p.casefold() for p in Path(rel).parts} or not path.is_file():
        return None
    return path

def infer_kind(name, group, a):
    if re.match(r"FTV\.uz\b", str(a.get("tvg-id") or ""), re.I):
        return "music"
    hint = (a.get("tvg-content") or "").strip().casefold()
    if hint in {"movie", "movies", "film", "films"}:
        return "movie"
    if hint in {"music", "musics"}:
        return "music"
    group_key = str(group or "").strip().casefold()
    if group_key == "international movies":
        return "movie"
    if group_key == "international music":
        return "music"
    if MOVIE_RE.search(name):
        return "movie"
    if MUSIC_RE.search(name):
        return "music"
    if country_from_group(group):
        return None
    return None

def classify(a, name, group, country):
    key = channel_key(name)
    group = str(group or "").strip()
    group_key = group.casefold()
    joined = f"{name} {a.get('tvg-id', '')} {a.get('channel-id', '')}"

    if not name or re.fullmatch(r"(?:\d+|n/?a|unknown|test|demo|sample|placeholder|new channel|unnamed|no name|not available)", name, re.I):
        return None, None, "non-real/test channel"
    if key in MANUAL_NEWS or NEWS_RE.search(joined) or re.search(r"\b(?:news|headlines|current affairs|newsroom)\b", group, re.I):
        if country == "BD":
            return "Bangladesh", None, None
        return None, None, "non-Bangladesh news"
    if NON_ISLAM_RE.search(joined):
        return None, None, "non-Islamic religious"
    if FASHION_RE.search(joined) or group_key == "fashion tv":
        if FASHION_RE.search(joined):
            return "Fashion TV", None, None
        return None, None, "invalid Fashion TV exception group"
    if ISLAM_RE.search(joined) or (group == "Religious" and not NON_ISLAM_RE.search(joined)):
        return "Religious", None, None
    if ADULT_RE.search(joined) or group == "Adult":
        return "Adult", None, None
    if KIDS_RE.search(joined) or group == "Kids":
        return "Kids", None, None
    if SPORTS_RE.search(joined) or group == "Sports":
        return "Sports", None, None
    if DOC_RE.search(joined) or group == "Documentary & Wildlife":
        return "Documentary & Wildlife", None, None
    if country not in {"BD", "IN"} and group not in {"Fashion TV", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Adult"} and GENERAL_OUT_OF_SCOPE_RE.search(joined):
        return None, None, "general entertainment, not a dedicated Movie/Music channel"
    if key in MANUAL_GROUP:
        return MANUAL_GROUP[key], None, None
    if group_key in BACKUP_GROUPS:
        return ("New Backups" if group_key in {"new backup", "new backups"} else "Backups"), infer_kind(name, group, a), None
    if country == "BD" or group == "Bangladesh":
        return "Bangladesh", None, None
    if country == "IN" or group in INDIAN_GROUPS:
        if group == "Indian Bangla" or re.search(r"\b(?:bengali|bangla)\b", f"{a.get('tvg-language','')} {name}", re.I):
            return "Indian Bangla", None, None
        if group == "Indian Movies" or MOVIE_RE.search(joined):
            return "Indian Movies", None, None
        if group == "Indian Music" or MUSIC_RE.search(joined):
            return "Indian Music", None, None
        return "Indian Entertainment", None, None
    if country == "PK" or group == "Pakistani":
        kind = infer_kind(name, group, a)
        if kind:
            return "Pakistani", kind, None
        return None, None, "foreign channel not clearly movie/music"
    kind = infer_kind(name, group, a)
    if kind:
        return "__FOREIGN__", kind, None
    return None, None, "foreign channel not clearly movie/music"

def set_extinf(block, name, group, country, content_kind, keep_logo, is_queue=False):
    left, _ = split_info(block[0])
    for key in ("group-title", "tvg-name", "tvg-logo", "tvg-content", "tvg-country", "tvg-chno", "http-user-agent", "http-referrer"):
        left = re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", left)
    fields = [left.rstrip()]
    if keep_logo:
        original = attrs(block[0]).get("tvg-logo", "")
        fields.append(f'tvg-logo="{original}"')
    if country in discovery.ISO_CODES:
        fields.append(f'tvg-country="{country}"')
    if content_kind and (is_queue or group not in FIXED + TAIL):
        tag = "Movies" if content_kind == "movie" else "Music"
        fields.append(f'tvg-content="{tag}"')
    fields.append(f'group-title="{group}"')
    fields.append(f'tvg-name="{name}"')
    return " ".join(field for field in fields if field).replace("  ", " ").strip() + "," + name

def natural_key(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    return tuple((1, int(item)) if item.isdigit() else (0, item) for item in re.split(r"(\d+)", value))

def main():
    if not PLAYLIST.is_file():
        raise SystemExit("International-Playlist.m3u is missing; refusing to create it.")
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    preamble, blocks = parse_playlist(original)
    staged, removed = [], Counter()
    names_normalized = malformed_options = invalid_logos = 0

    for block in blocks:
        if not block or not block[0].startswith("#EXTINF:"):
            removed["malformed entry"] += 1
            continue
        left, display = split_info(block[0])
        a0 = attrs(left)
        options = {key: a0[key] for key in ("http-user-agent", "http-referrer") if a0.get(key)}
        for option in options:
            left = re.sub(rf'\s+{re.escape(option)}="[^"]*"', "", left)
        a = attrs(left)
        raw_name = a.get("tvg-name") or display
        name = clean_name(raw_name)
        if channel_key(name) == "rajdhanitv":
            name = "Rajdhani TV"
        group = a.get("group-title", "").strip()
        country = country_code(a, group, name)
        url = url_of(block)
        if not url:
            removed["missing stream URL"] += 1
            continue
        if not name:
            removed["empty name"] += 1
            continue
        names_normalized += int(name != str(raw_name or "").strip())
        malformed_options += int(bool(options))
        target, kind, reason = classify(a, name, group, country)
        if reason:
            removed[reason] += 1
            continue
        logo = a.get("tvg-logo", "")
        local_logo = local_logo_path(logo)
        invalid_logos += int(bool(logo) and local_logo is None)
        extras = [line for line in block[1:] if line.strip()
                  and not line.strip().startswith(("http://", "https://"))
                  and not re.match(r"#EXTVLCOPT:http-(?:user-agent|referrer)=", line.strip(), re.I)]
        staged.append({
            "block": block, "a": a, "name": name, "key": channel_key(name),
            "group": target, "country": country, "kind": kind, "content_kind": kind,
            "url": url, "options": options, "extras": extras, "keep_logo": local_logo is not None,
            "was_backup": group.casefold() in BACKUP_GROUPS,
            "identity": (a.get("tvg-id") or a.get("channel-id") or channel_key(name)).strip().casefold(),
        })

    country_identities = defaultdict(set)
    for row in staged:
        if row["was_backup"] or row["group"] != "__FOREIGN__" or row["country"] not in discovery.ISO_CODES:
            continue
        country_identities[row["country"]].add(row["key"])
    qualifying_countries = {cc for cc, ids in country_identities.items() if len(ids) >= discovery.COUNTRY_THRESHOLD}
    for row in staged:
        if row["group"] != "__FOREIGN__":
            continue
        row["group"] = discovery.country_group(row["country"]) if row["country"] in qualifying_countries else "New Channels"
        if not row["group"]:
            row["group"] = "New Channels"

    primary = [row for row in staged if not row["was_backup"]]
    backup_rows = [row for row in staged if row["was_backup"]]
    group_order = FIXED + sorted({row["group"] for row in primary if row["group"] not in FIXED + TAIL}) + TAIL
    group_rank = {group: index for index, group in enumerate(group_order)}
    primary.sort(key=lambda row: (group_rank.get(row["group"], len(group_rank)), natural_key(row["name"]), row["url"].casefold()))
    identity_primary = {}
    for row in primary:
        identity_primary.setdefault((row["country"], row["key"]), row)
    output, seen_urls, seen_channels = [], set(), set()

    def emit(row, group, as_backup=False):
        url_key = row["url"].casefold()
        if url_key in seen_urls:
            removed["exact duplicate URL"] += 1
            return
        target = group
        ident = (row["country"], row["key"])
        if not as_backup and group != "New Backups":
            if ident in seen_channels:
                target = "Backups"
                removed["duplicate channel stream moved to Backups"] += 1
            else:
                seen_channels.add(ident)
        seen_urls.add(url_key)
        content_kind = row.get("content_kind") or row.get("kind")
        ext = set_extinf(row["block"], row["name"], target, row["country"], content_kind,
                         row["keep_logo"], is_queue=target in {"New Channels", "New Backups"})
        extras = list(row["extras"])
        for option, value in row["options"].items():
            directive = f"#EXTVLCOPT:{option}={value}"
            extras = [line for line in extras if not line.strip().casefold().startswith(f"#extvlcopt:{option}=")]
            extras.append(directive)
        output.append({"group": target, "name": row["name"], "key": row["key"], "url": row["url"],
                       "block": [ext, *extras, row["url"]]})

    for row in primary:
        emit(row, row["group"])
    for row in backup_rows:
        match = identity_primary.get((row["country"], row["key"]))
        if match:
            row["content_kind"] = match.get("content_kind") or match.get("kind")
            emit(row, "Backups", as_backup=True)
        elif row["group"] == "New Backups" and row.get("kind"):
            emit(row, "New Backups", as_backup=True)
        elif row["country"] in {"BD", "IN"} or row["group"] in {"Religious", "Adult", "Kids", "Sports", "Documentary & Wildlife"} or row.get("kind"):
            emit(row, "Backups", as_backup=True)
        else:
            removed["orphan backup outside policy"] += 1

    present = {row["group"] for row in output}
    dynamic = sorted(group for group in present if group not in FIXED + TAIL)
    category_order = FIXED + dynamic + TAIL
    category_rank = {group: index for index, group in enumerate(category_order)}
    output.sort(key=lambda row: (category_rank.get(row["group"], len(category_rank)), natural_key(row["name"]), row["url"].casefold()))

    header = [line for line in preamble if line and not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    name_index = next((i for i, line in enumerate(header) if line.startswith("#PLAYLIST-STUDIO-NAME:")), None)
    if name_index is None:
        raise SystemExit("Playlist name header is missing; refusing to write.")
    header.insert(name_index + 1, "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(category_order, ensure_ascii=False))
    new_text = "\n".join(header + [line for row in output for line in row["block"]]) + "\n"

    _, final_blocks = parse_playlist(new_text)
    final_urls, groups_seen, group_counts = [], [], Counter()
    last_group = None
    for block in final_blocks:
        a = attrs(split_info(block[0])[0])
        name = a.get("tvg-name") or split_info(block[0])[1]
        group = a.get("group-title", "").strip()
        url = url_of(block)
        if not group or not url:
            raise SystemExit(f"Malformed final entry: {name}")
        if group != last_group:
            if group in groups_seen:
                raise SystemExit(f"Category group is split: {group}")
            groups_seen.append(group)
            last_group = group
        if re.search(r"\b\d{3,4}\s*[pi]\b|\bgeo[\s-]?blocked\b|\bnot\s*24/7\b", name, re.I):
            raise SystemExit(f"Name was not normalized: {name}")
        if a.get("tvg-logo") and local_logo_path(a["tvg-logo"]) is None:
            raise SystemExit(f"Invalid or external logo reference: {name}")
        if group.casefold() in {"new channels", "new backups"} and (a.get("tvg-content") or "").casefold() not in {"movies", "movie", "music"}:
            raise SystemExit(f"Review queue entry lacks validated movie/music classification: {name}")
        final_urls.append(url.casefold())
        group_counts[group] += 1
    if len(final_urls) != len(set(final_urls)):
        raise SystemExit("Duplicate stream URLs remain after reorganization.")
    if [group for group in category_order if group in group_counts] != groups_seen:
        raise SystemExit("Category registry does not match contiguous playlist groups.")

    PLAYLIST.write_text(new_text, encoding="utf-8")
    report = [
        "# International Playlist Organization Audit", "",
        f"- Entries before: {len(blocks)}", f"- Entries after: {len(final_blocks)}",
        f"- Channel names normalized: {names_normalized}",
        f"- Malformed HTTP options moved into VLC directives: {malformed_options}",
        f"- Invalid/external logo references removed: {invalid_logos}",
        f"- Exact duplicate URLs omitted: {removed['exact duplicate URL']}",
        f"- Additional same-channel streams moved to Backups: {removed['duplicate channel stream moved to Backups']}",
        "- News outside Bangladesh and non-Islamic religious channels are excluded.",
        "- Foreign movie/music services are placed under country names after at least five unique primary channels; smaller/unknown countries remain in New Channels with tvg-content tags.",
        "- Retained stream URLs are preserved; playback/availability was not tested.", "",
        "## Removal summary", "", *[f"- {reason}: {count}" for reason, count in sorted(removed.items())], "",
        "## Category counts", "",
        *[f"- {group}: {count}" for group, count in sorted(group_counts.items(), key=lambda item: category_rank[item[0]])], ""
    ]
    Path("reports").mkdir(exist_ok=True)
    Path("reports/international-playlist-audit.md").write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"before": len(blocks), "after": len(final_blocks), "removed": dict(removed),
                      "normalized_names": names_normalized, "malformed_http_options_moved": malformed_options,
                      "duplicate_urls": removed["exact duplicate URL"],
                      "duplicate_channels_moved_to_backups": removed["duplicate channel stream moved to Backups"],
                      "groups": dict(group_counts)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
