#!/usr/bin/env python3
"""Final policy/structure repair for IPTV-Playlist.m3u only.

This pass is deliberately conservative: it changes metadata/group structure,
removes exact duplicate URLs, and preserves orphan Backup records for manual
review instead of deleting them. It preserves known required movie/drama records
and never changes a stream URL merely because a live probe fails.
"""
from pathlib import Path
import re
import unicodedata

P = Path("IPTV-Playlist.m3u")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup",
    "Not Playing",
]
NO_NUMBER = {"Backup", "Not Playing"}
BACKUP = "Backup"
REQUIRED_RECORDS = [
    [
        '#EXTINF:-1 channel-id="custom.gseriesdrama" tvg-id="custom.gseriesdrama" tvg-chno="23" tvg-name="G Series Drama" group-title="Bangladesh" tvg-logo="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/g-series-drama.png",G Series Drama',
        "https://vods2.aynaott.com/gseriesDrama/tracks-v1a1/mono.ts.m3u8",
    ],
    [
        '#EXTINF:-1 tvg-chno="1095" tvg-id="new.hindi.movie.classic.24" channel-id="new.hindi.movie.classic.24" tvg-name="Hindi Movie Classic 24" tvg-logo="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/hindi-movie-classic-24.png" group-title="Indian Movies",Hindi Movie Classic 24',
        "https://vods2.aynaott.com/hindimovies/index.m3u8",
    ],
]


def attrs(s):
    return dict(ATTR_RE.findall(s))


def set_attr(s, key, value):
    p = re.compile(rf'{re.escape(key)}="[^"]*"')
    if p.search(s):
        return p.sub(f'{key}="{value}"', s, count=1)
    return s.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)


def remove_attr(s, key):
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", s, count=1)


def display_name(info):
    a = attrs(info)
    return (a.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()


def norm_name(value):
    s = unicodedata.normalize("NFKD", str(value or "")).casefold()
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def url_of(block):
    for line in block[1:]:
        u = line.strip()
        if u.startswith(("http://", "https://")):
            return u
    return ""


def parse(text):
    pre, blocks, cur = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if cur is not None:
                blocks.append(cur)
            cur = [line]
        elif cur is None:
            pre.append(line)
        else:
            cur.append(line)
    if cur is not None:
        blocks.append(cur)
    return pre, blocks


def repair_category_registry(pre):
    canonical = '#PLAYLIST-STUDIO-CATEGORIES:["' + '", "'.join(ORDER) + '"]'
    out = [x for x in pre if not x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    insert_at = 0
    for i, line in enumerate(out):
        if line.startswith("#EXTM3U"):
            insert_at = i + 1
            break
    out.insert(insert_at, canonical)
    return out


def ensure_required_records(blocks):
    urls = {url_of(b).strip().casefold() for b in blocks if url_of(b).strip()}
    added = 0
    for record in REQUIRED_RECORDS:
        url = record[1].casefold()
        if url not in urls:
            blocks.append(list(record))
            urls.add(url)
            added += 1
    return added


def main():
    if not P.exists():
        raise SystemExit("IPTV-Playlist.m3u not found")

    pre, blocks = parse(P.read_text(encoding="utf-8-sig"))
    changed = 0
    removed_duplicate = 0
    orphan_backups_preserved = 0
    removed_malformed = 0

    seen_urls = set()
    kept = []
    for block in blocks:
        info = block[0]
        a = attrs(info)
        group = a.get("group-title", "").strip()
        url = url_of(block)

        if not url:
            removed_malformed += 1
            continue

        if group not in ORDER:
            info = set_attr(info, "group-title", "Not Playing")
            group = "Not Playing"
            changed += 1

        if group in NO_NUMBER and attrs(info).get("tvg-chno"):
            info = remove_attr(info, "tvg-chno")
            changed += 1

        key = url.casefold()
        if key in seen_urls:
            removed_duplicate += 1
            continue
        seen_urls.add(key)

        block[0] = info
        kept.append(block)
    blocks = kept

    primary_ids = set()
    primary_names = set()
    for block in blocks:
        a = attrs(block[0])
        if a.get("group-title", "").strip() in NO_NUMBER:
            continue
        for cid in (a.get("tvg-id", ""), a.get("channel-id", "")):
            if cid.strip():
                primary_ids.add(cid.strip().casefold())
        primary_names.add(norm_name(display_name(block[0])))

    out = []
    for block in blocks:
        info = block[0]
        a = attrs(info)
        group = a.get("group-title", "").strip()
        if group == BACKUP:
            ids = {x.strip().casefold() for x in (a.get("tvg-id", ""), a.get("channel-id", "")) if x.strip()}
            name_key = norm_name(display_name(info))
            if not (ids & primary_ids) and name_key not in primary_names:
                # Orphan detection is advisory only: a backup-only stream may be
                # a future candidate. Preserve its record and URL for manual review.
                orphan_backups_preserved += 1
        out.append(block)
    blocks = out

    added_required = ensure_required_records(blocks)

    for block in blocks:
        info = block[0]
        if attrs(info).get("group-title", "").strip() in NO_NUMBER and attrs(info).get("tvg-chno"):
            block[0] = remove_attr(info, "tvg-chno")
            changed += 1

    rank = {name: i for i, name in enumerate(ORDER)}
    def natural(value):
        s = unicodedata.normalize("NFKD", str(value or "")).casefold().strip()
        return tuple(int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s))
    blocks.sort(key=lambda b: (
        rank.get(attrs(b[0]).get("group-title", "").strip(), len(rank)),
        natural(display_name(b[0])),
        url_of(b).casefold(),
    ))

    pre = repair_category_registry(pre)
    lines = list(pre)
    for block in blocks:
        lines.extend(block)
    P.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(
        f"Playlist policy repair: changed={changed}, duplicate_urls_removed={removed_duplicate}, "
        f"orphan_backups_preserved={orphan_backups_preserved}, malformed_records_removed={removed_malformed}, "
        f"required_records_restored={added_required}, entries={len(blocks)}"
    )


if __name__ == "__main__":
    main()
