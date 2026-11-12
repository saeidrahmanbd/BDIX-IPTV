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
    primary_ids, primary_names = set(), set()
    for row in rows:
        a = attrs(row["info"])
        if a.get("group-title", "").strip() not in ACTIVE:
            continue
        primary_ids.update(id_key(x) for x in (a.get("tvg-id"), a.get("channel-id")) if id_key(x))
        primary_names.add(name_key(a.get("tvg-name") or row["info"].rsplit(",", 1)[-1]))
    candidates = []
    seen = set()
    for row in rows:
        a = attrs(row["info"])
        group = a.get("group-title", "").strip()
        if group in QUEUE:
            include = True
        elif group == "Backup":
            ids = {id_key(x) for x in (a.get("tvg-id"), a.get("channel-id")) if id_key(x)}
            name = name_key(a.get("tvg-name") or row["info"].rsplit(",", 1)[-1])
            include = not (ids & primary_ids) and name not in primary_names
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
