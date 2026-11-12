#!/usr/bin/env python3
"""Probe only owner-requested Backup or discovery-queue migration candidates."""
from __future__ import annotations
import concurrent.futures
import json
import re
import socket
import ssl
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PLAYLIST = Path("IPTV-Playlist.m3u")
OUTPUT = Path("/tmp/iptv-owner-requested-probes.json")
ACTIVE = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
QUEUE = {"New Channels", "New Backups", "New Backup"}
ATTR = re.compile(r'([\w-]+)="([^"]*)"')

def attrs(line):
    return dict(ATTR.findall(line))

def name_key(value):
    value = re.sub(r"\([^)]*\)|\[[^]]*\]", " ", str(value or ""))
    value = re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "", value.casefold())

def id_key(value):
    value = str(value or "").strip().casefold()
    if not value:
        return ""
    return value.split("@", 1)[0]

def country_for(metadata):
    country = str(metadata.get("tvg-country", "") or "").strip().upper()
    if re.fullmatch(r"[A-Z]{2}", country):
        return country
    for value in (metadata.get("tvg-id", ""), metadata.get("channel-id", "")):
        match = re.search(r"\\.([a-z]{2})(?:@|$)", str(value or ""), re.I)
        if match:
            return match.group(1).upper()
    return ""


def has_unique_primary_match(info, primary_rows):
    """Mirror migrate_owner_requested_main_queues.primary_match exactly.

    A same-name candidate in a different country is not treated as a match;
    ambiguous matches are still probed so the migration can retain them safely.
    """
    metadata = attrs(info)
    ids = {id_key(value) for value in (metadata.get("tvg-id"), metadata.get("channel-id")) if id_key(value)}
    current_name = metadata.get("tvg-name") or info.rsplit(",", 1)[-1]
    normalized_name = name_key(current_name)
    id_matches = []
    name_matches = []
    for row in primary_rows:
        primary = attrs(row["info"])
        primary_ids = {id_key(value) for value in (primary.get("tvg-id"), primary.get("channel-id")) if id_key(value)}
        if ids & primary_ids:
            id_matches.append(row)
        elif normalized_name and name_key(primary.get("tvg-name") or row["info"].rsplit(",", 1)[-1]) == normalized_name:
            left_country = country_for(metadata)
            right_country = country_for(primary)
            if not left_country or not right_country or left_country == right_country:
                name_matches.append(row)
    if id_matches:
        return len(id_matches) == 1
    return len(name_matches) == 1

def parse():
    rows, current = [], None
    for line in PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if current:
                rows.append(current)
            current = {"info": line, "url": ""}
        elif current is not None and line.strip().lower().startswith(("http://", "https://")):
            current["url"] = line.strip()
            rows.append(current)
            current = None
    if current:
        rows.append(current)
    return rows

def probe(url):
    start = time.monotonic()
    try:
        req = Request(url, headers={
            "User-Agent": "BDIX-IPTV-Owner-Migration-Check/1.0",
            "Accept": "*/*",
            "Range": "bytes=0-4095",
        })
        with urlopen(req, timeout=15) as response:
            data = response.read(4096)
            status = int(getattr(response, "status", 200) or 200)
            return {
                "ok": status < 400 and bool(data),
                "status": status,
                "bytes": len(data),
                "error": "",
                "latency_ms": round((time.monotonic() - start) * 1000),
            }
    except HTTPError as exc:
        return {"ok": False, "status": exc.code, "bytes": 0, "error": f"HTTP {exc.code}",
                "latency_ms": round((time.monotonic() - start) * 1000)}
    except URLError as exc:
        reason = exc.reason
        if isinstance(reason, socket.gaierror):
            kind = "DNS"
        elif isinstance(reason, ssl.SSLError):
            kind = "TLS"
        elif isinstance(reason, (TimeoutError, socket.timeout)):
            kind = "Timeout"
        else:
            kind = "Network"
        return {"ok": False, "status": 0, "bytes": 0, "error": kind,
                "latency_ms": round((time.monotonic() - start) * 1000)}
    except (TimeoutError, socket.timeout):
        return {"ok": False, "status": 0, "bytes": 0, "error": "Timeout",
                "latency_ms": round((time.monotonic() - start) * 1000)}
    except Exception as exc:
        return {"ok": False, "status": 0, "bytes": 0, "error": type(exc).__name__,
                "latency_ms": round((time.monotonic() - start) * 1000)}

def main():
    rows = parse()
    primary_rows = [
        row for row in rows
        if attrs(row["info"]).get("group-title", "").strip() in ACTIVE
    ]
    candidates = []
    seen = set()
    for row in rows:
        a = attrs(row["info"])
        group = a.get("group-title", "").strip()
        if group in QUEUE:
            include = True
        elif group == "Backup":
            include = not has_unique_primary_match(row["info"], primary_rows)
        else:
            include = False
        url = row["url"]
        if include and url and url not in seen:
            candidates.append({"url": url, "name": a.get("tvg-name") or row["info"].rsplit(",", 1)[-1],
                               "group": group})
            seen.add(url)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
        futures = [executor.submit(probe, row["url"]) for row in candidates]
        for row, future in zip(candidates, futures):
            results.append({**row, **future.result()})
    payload = {"probe_count": len(results), "results": results}
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ok = sum(1 for row in results if row["ok"])
    print(f"Owner-requested migration probe: {len(results)} candidates checked; {ok} reachable; {len(results)-ok} not reachable.")
    print(f"Detailed results saved to {OUTPUT} (local runner artifact only).")

if __name__ == "__main__":
    main()
