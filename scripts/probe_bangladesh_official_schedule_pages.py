#!/usr/bin/env python3
"""Read-only qualification probe for Bangladesh broadcaster schedule sources.

Runs the repository's existing official RTV, BTV and Maasranga adapters, then
checks public BTV/Prothom Alo pages for schedule-navigation links. It does not
write playlists, EPG mappings, or epg/epg.xml. Exact tvg-id matches are shown
separately for active and inactive playlist groups.
"""
import sys
import re
import os
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from official_epg_sources import (  # noqa: E402
    fetch_rtv_programmes,
    fetch_btv_programmes,
    fetch_maasranga_programmes,
)

PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
INACTIVE_GROUPS = {
    "backup", "review", "test", "not playing", "new channels",
    "new backups", "new backup",
}
TIMEOUT = 30
MAX_BYTES = 12 * 1024 * 1024
USER_AGENT = "BDIX-IPTV-Bangladesh-EPG-Research/1.0"

PUBLIC_PAGES = (
    ("BTV official homepage", "https://btv.gov.bd/"),
    ("BTV legacy live programme guide", "https://migrate.btvlive.gov.bd/channel/BTV"),
    ("Prothom Alo TV section", "https://www.prothomalo.com/entertainment/tv"),
    ("Prothom Alo entertainment section", "https://www.prothomalo.com/entertainment"),
)


def load_playlist_identities():
    found = {}
    for filename in PLAYLISTS:
        path = ROOT / filename
        if not path.is_file():
            continue
        current = None
        for raw in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            line = raw.strip()
            if line.startswith("#EXTINF:"):
                attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
                current = {
                    "id": attrs.get("tvg-id", "").strip(),
                    "name": line.rsplit(",", 1)[-1].strip(),
                    "group": attrs.get("group-title", "").strip(),
                    "country": attrs.get("tvg-country", "").strip().upper(),
                }
            elif current and line.startswith(("http://", "https://")):
                channel_id = current["id"]
                base_id = channel_id.split("@", 1)[0]
                is_bd_scope = (
                    current["group"].casefold() == "bangladesh"
                    or base_id.casefold().endswith(".bd")
                )
                if channel_id and is_bd_scope:
                    item = found.setdefault(
                        channel_id,
                        {
                            "id": channel_id,
                            "name": current["name"],
                            "groups": set(),
                            "countries": set(),
                        },
                    )
                    item["groups"].add(current["group"])
                    if current["country"]:
                        item["countries"].add(current["country"])
                current = None
    for item in found.values():
        item["active"] = any(
            group.casefold() not in INACTIVE_GROUPS
            for group in item["groups"]
        )
    return found


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.href = None
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self.href = dict(attrs).get("href", "")
            self.parts = []

    def handle_data(self, data):
        if self.href:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.href:
            label = re.sub(r"\s+", " ", " ".join(self.parts)).strip()
            self.links.append((label, self.href))
            self.href = None
            self.parts = []


def fetch_page(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,*/*",
            "Accept-Language": "bn-BD,bn;q=0.9,en;q=0.7",
        },
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        data = response.read(MAX_BYTES + 1)
        final_url = response.geturl()
        status = getattr(response, "status", 200)
    if len(data) > MAX_BYTES:
        raise ValueError("response exceeded 12 MiB limit")
    return status, final_url, data.decode("utf-8-sig", errors="replace")


def probe_public_page(label, url):
    status, final_url, html = fetch_page(url)
    parser = LinkParser()
    parser.feed(html)
    keywords = ("অনুষ্ঠান", "টিভি গাইড", "schedule", "program", "epg")
    links = []
    for text, href in parser.links:
        if any(key.casefold() in (text + " " + href).casefold() for key in keywords):
            links.append((text[:100], href[:350]))
    return {
        "label": label,
        "status": "OK",
        "http": status,
        "url": final_url,
        "bytes": len(html.encode("utf-8")),
        "links": links[:30],
        "note": "Public page fetch only; links are candidates, not schedule rows.",
    }


def probe_adapter(label, channel_id, fetcher, identities, now):
    try:
        rows = fetcher(now=now)
        rows = [
            row for row in rows
            if row.get("channel_id") == channel_id
            and row.get("title")
            and row.get("start_dt")
            and row.get("stop_dt")
            and row["stop_dt"] > row["start_dt"]
        ]
        exact = identities.get(channel_id)
        return {
            "label": label,
            "status": "OK" if rows else "NO_USABLE_ROWS",
            "channel_id": channel_id,
            "rows": rows,
            "count": len(rows),
            "titles": len({row["title"].strip().casefold() for row in rows}),
            "first": min((row["start_dt"] for row in rows), default=None),
            "last": max((row["stop_dt"] for row in rows), default=None),
            "playlist_match": "EXACT_ACTIVE" if exact and exact["active"] else (
                "EXACT_INACTIVE_ONLY" if exact else "NO_EXACT_PLAYLIST_ID"
            ),
            "groups": ", ".join(sorted(exact["groups"])) if exact else "-",
            "error": "",
        }
    except Exception as exc:  # noqa: BLE001 - every source must remain independently auditable
        return {
            "label": label,
            "status": "FAILED",
            "channel_id": channel_id,
            "rows": [],
            "count": 0,
            "titles": 0,
            "first": None,
            "last": None,
            "playlist_match": (
                "EXACT_ACTIVE" if channel_id in identities and identities[channel_id]["active"]
                else "EXACT_INACTIVE_ONLY" if channel_id in identities
                else "NO_EXACT_PLAYLIST_ID"
            ),
            "groups": ", ".join(sorted(identities[channel_id]["groups"])) if channel_id in identities else "-",
            "error": f"{type(exc).__name__}: {str(exc)[:220]}",
        }


def md(value):
    return str(value if value is not None else "-").replace("|", "/").replace("\n", " ").strip()


def main():
    output = Path(
        sys.argv[1] if len(sys.argv) > 1
        else "reports/bangladesh-official-schedule-source-probe.md"
    )
    now = datetime.now(timezone.utc)
    identities = load_playlist_identities()
    in_scope = len(identities)
    active = sum(1 for item in identities.values() if item["active"])

    adapters = [
        ("RTV official weekly/daily schedule", "RTV.bd", fetch_rtv_programmes),
        ("BTV official programme guide (legacy endpoint)", "BTVNational.bd", fetch_btv_programmes),
        ("Maasranga official weekly schedule", "MaasrangaTV.bd", fetch_maasranga_programmes),
    ]
    adapter_results = [
        probe_adapter(label, cid, fetcher, identities, now)
        for label, cid, fetcher in adapters
    ]

    page_results = []
    for label, url in PUBLIC_PAGES:
        try:
            page_results.append(probe_public_page(label, url))
        except Exception as exc:  # noqa: BLE001
            page_results.append({
                "label": label,
                "status": "FAILED",
                "http": "-",
                "url": url,
                "bytes": 0,
                "links": [],
                "note": f"{type(exc).__name__}: {str(exc)[:220]}",
            })

    total_rows = sum(result["count"] for result in adapter_results)
    active_exact = sum(
        result["count"] for result in adapter_results
        if result["playlist_match"] == "EXACT_ACTIVE"
    )
    inactive_exact = sum(
        result["count"] for result in adapter_results
        if result["playlist_match"] == "EXACT_INACTIVE_ONLY"
    )

    lines = [
        "# Bangladesh official schedule source probe",
        "",
        f"Generated: **{now.isoformat(timespec='seconds')}**",
        "",
        "## Safety and scope",
        "",
        "- Read-only. This probe does not change playlists, EPG mappings, source lists or epg/epg.xml.",
        "- It runs only the repository's existing public HTML schedule adapters and fetches public navigation pages.",
        "- Exact tvg-id identity is required. Similar names are not treated as matches.",
        "- No subscriber login, app token, private endpoint, session cookie or API key is used.",
        "- Backup, Review, New Channels and New Backups are counted as inactive groups for the active-match column.",
        "",
        f"- Bangladesh-scope unique IDs in both playlists (group-title Bangladesh or .bd ID): **{in_scope}**",
        f"- IDs currently in active groups: **{active}**",
        f"- Schedule window: **-6 hours to +7 days**",
        "",
        "## Existing official schedule adapters",
        "",
        "| Source | XMLTV channel ID | Result | Usable rows | Unique titles | Exact playlist status | Group | First start (UTC) | Last stop (UTC) | Error |",
        "|---|---|---|---:|---:|---|---|---|---|---|",
    ]
    for result in adapter_results:
        lines.append(
            "| " + " | ".join(md(value) for value in (
                result["label"], result["channel_id"], result["status"],
                result["count"], result["titles"], result["playlist_match"],
                result["groups"],
                result["first"].isoformat(timespec="minutes") if result["first"] else "-",
                result["last"].isoformat(timespec="minutes") if result["last"] else "-",
                result["error"],
            )) + " |"
        )
    lines += [
        "",
        "## Public schedule-navigation pages",
        "",
        "| Page | Fetch result | HTTP | Page URL | Bytes | Candidate schedule links | Note |",
        "|---|---|---:|---|---:|---|---|",
    ]
    for page in page_results:
        links = "; ".join(
            f"{text} — {href}" for text, href in page["links"]
        ) or "-"
        lines.append(
            "| " + " | ".join(md(value) for value in (
                page["label"], page["status"], page["http"], page["url"],
                page["bytes"], links, page["note"],
            )) + " |"
        )
    lines += [
        "",
        "## Summary",
        "",
        f"- Usable programme rows from tested official adapters: **{total_rows}**",
        f"- Rows attached to exact active playlist IDs: **{active_exact}**",
        f"- Rows attached only to exact inactive playlist IDs: **{inactive_exact}**",
        "- A successfully fetched schedule for a Backup/Review-only channel does not count as active-playlist coverage.",
        "- A public navigation page without a current dated schedule is not treated as an EPG source.",
        "- Public pages and adapters require separate data-redistribution review before any schedule data can be added to the public XMLTV guide.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("\n".join(lines[:45]) + "\n")
    print(
        f"Wrote {output}; scope={in_scope}; active={active}; adapter_rows={total_rows}; "
        f"active_exact_rows={active_exact}; inactive_exact_rows={inactive_exact}",
        flush=True,
    )


if __name__ == "__main__":
    main()
