#!/usr/bin/env python3
"""Read-only probe: which reachable XMLTV feeds carry Bangladeshi channels?

For every configured XMLTV source (plus feeds listed on the epgshare01 index) this
reports, per Bangladesh-group playlist channel, feed channels whose XMLTV ID equals
the playlist tvg-id or whose display name equals the playlist name after strict
normalisation (case, punctuation and a trailing HD/SD only). It never edits
mappings, playlists or the guide: the output is evidence for a human to approve,
and similar-but-different names are not reported as matches.

Usage: probe_epg_sources_for_bangladesh.py [output.md]
"""
import ast
import gzip
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYLISTS = ("BDIX-Playlist.m3u", "IPTV-Playlist.m3u", "International-Playlist.m3u")
INDEX_URL = "https://epgshare01.online/epgshare01/"
TIMEOUT = 40
MAX_BYTES = 120 * 1024 * 1024
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
SKIP_URL_PARTS = ("hum.tv/schedule", "rtvbd.tv/schedule")


def norm(value):
    value = re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())
    return re.sub(r"(?:hd|sd)$", "", value)


def load_sources():
    tree = ast.parse((ROOT / "scripts" / "generate_epg.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "SOURCES" for t in node.targets
        ):
            return [s for s in ast.literal_eval(node.value) if not any(p in s for p in SKIP_URL_PARTS)]
    return []


def bangladesh_channels():
    found = {}
    for name in PLAYLISTS:
        path = ROOT / name
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            attrs = dict(ATTR_RE.findall(line))
            tvg_id = attrs.get("tvg-id", "").strip()
            label = line.rsplit(",", 1)[-1].strip()
            group = attrs.get("group-title", "").strip().casefold()
            if tvg_id and (group == "bangladesh" or tvg_id.split("@")[0].endswith(".bd")):
                found.setdefault(tvg_id, label)
    return found


class _Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href") or ""
            if href.endswith((".xml", ".xml.gz")):
                self.links.append(href)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-epg-probe/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise RuntimeError("larger than probe size limit")
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return data


def index_feeds():
    try:
        parser = _Links()
        parser.feed(get(INDEX_URL).decode("utf-8", "ignore"))
        return sorted({INDEX_URL + h.lstrip("./") if not h.startswith("http") else h for h in parser.links})
    except Exception as exc:  # noqa: BLE001 - diagnostics must not abort the probe
        print(f"index listing failed: {exc}")
        return []


def scan(url, targets, window_start, window_end):
    """Return (status, channel_count, hits) for one feed."""
    data = get(url)
    by_name = {}
    for tvg_id, label in targets.items():
        by_name.setdefault(norm(label), []).append(tvg_id)
    wanted_ids = set(targets)
    channels = {}
    programmes = {}
    bd_ids = set()
    for _, el in ET.iterparse(BytesIO(data), events=("end",)):
        if el.tag == "channel":
            cid = el.get("id", "")
            names = [(d.text or "").strip() for d in el.findall("display-name")]
            channels[cid] = names
            if cid.split("@")[0].casefold().endswith(".bd"):
                bd_ids.add(cid)
            el.clear()
        elif el.tag == "programme":
            cid = el.get("channel", "")
            try:
                start = datetime.strptime(el.get("start", "")[:14], "%Y%m%d%H%M%S")
            except ValueError:
                start = None
            if start and window_start <= start <= window_end and (el.findtext("title") or "").strip():
                programmes[cid] = programmes.get(cid, 0) + 1
            el.clear()
    hits = []
    for cid, names in channels.items():
        matched = []
        if cid in wanted_ids:
            matched.append((cid, "EXACT_ID"))
        keys = {norm(cid.split(".")[0])} | {norm(n) for n in names}
        for key in keys:
            for tvg_id in by_name.get(key, []):
                if key and (tvg_id, "EXACT_NAME") not in matched and cid != tvg_id:
                    matched.append((tvg_id, "EXACT_NAME"))
        for tvg_id, kind in matched:
            hits.append((tvg_id, targets[tvg_id], cid, names[:1], kind, programmes.get(cid, 0)))
    return "OK", len(channels), hits, sorted(bd_ids)


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "reports/epg-bangladesh-source-probe.md")
    targets = bangladesh_channels()
    sources = load_sources()
    extra = [u for u in index_feeds() if u not in sources]
    urls = sources + extra
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    window_start, window_end = now - timedelta(hours=6), now + timedelta(days=7)
    results = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(scan, u, targets, window_start, window_end): u for u in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                results[url] = fut.result()
            except Exception as exc:  # noqa: BLE001
                results[url] = (f"FAILED: {type(exc).__name__}: {str(exc)[:120]}", 0, [], [])
            print(results[url][0], url, flush=True)

    lines = [
        "# Bangladesh EPG source probe",
        "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        "",
        "Read-only evidence for human review. Matches are exact XMLTV ID or exact normalised display name "
        "only (case, punctuation and a trailing HD/SD ignored). Nothing here changes mappings or the guide, "
        "and a name match is not proof of the same channel: verify before adding an alias.",
        "",
        f"- Bangladesh-group playlist channels checked: **{len(targets)}**",
        f"- Feeds probed: **{len(urls)}** ({len(extra)} discovered on the epgshare01 index)",
        f"- Feeds reachable: **{sum(1 for r in results.values() if r[0] == 'OK')}**",
        "",
        "## Candidate matches with programmes in the guide window",
        "",
        "| Playlist tvg-id | Playlist name | Feed channel ID | Feed name | Match | Programmes in window | Feed |",
        "|---|---|---|---|---|---:|---|",
    ]
    rows = []
    for url, (status, _count, hits, _bd) in results.items():
        for tvg_id, label, cid, names, kind, n in hits:
            if n:
                rows.append((tvg_id, label, cid, (names or [""])[0], kind, n, url))
    for row in sorted(rows):
        lines.append("| " + " | ".join(str(c).replace("|", "/") for c in row) + " |")
    if not rows:
        lines.append("| _none found_ | | | | | | |")
    lines += ["", "## Feeds containing any `.bd` channel IDs", ""]
    any_bd = False
    for url, (status, _count, _hits, bd_ids) in sorted(results.items()):
        if bd_ids:
            any_bd = True
            lines.append(f"- {url}: {len(bd_ids)} IDs, e.g. {', '.join(bd_ids[:8])}")
    if not any_bd:
        lines.append("- none")
    lines += ["", "## Feed status", "", "| Status | Channels | Feed |", "|---|---:|---|"]
    for url, (status, count, _h, _b) in sorted(results.items()):
        lines.append(f"| {status} | {count} | {url} |")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(rows)} candidate rows")


if __name__ == "__main__":
    main()
