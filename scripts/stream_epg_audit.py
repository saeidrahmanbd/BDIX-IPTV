#!/usr/bin/env python3
import csv, gzip, re, sys, urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u"
EPG_URLS = [
    "https://iptv-org.github.io/epg/guides/in/dishtv.in.epg.xml",
    "https://epg.pw/xmltv/epg_IN.xml",
    "https://iptv-epg.org/files/epg-in.xml",
]
UA = "BDIX-IPTV-Audit/1.0"
TIMEOUT = 15

def fetch(url, timeout=TIMEOUT):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, dict(r.headers), r.read()

def parse_playlist(text):
    rows, cur = [], None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            cur = {"extinf": line, "url": ""}
        elif cur and line and not line.startswith("#"):
            cur["url"] = line
            rows.append(cur)
            cur = None
    return rows

def attr(extinf, key):
    m = re.search(rf'{re.escape(key)}="([^"]*)"', extinf)
    return m.group(1) if m else ""

def base_id(value):
    return value.split("@", 1)[0] if value else ""

def audit_stream(url):
    try:
        status, headers, body = fetch(url)
        ctype = headers.get("Content-Type", "")
        if ".m3u8" in url.lower() or body.lstrip().startswith(b"#EXTM3U"):
            text = body.decode("utf-8", "replace")
            children = [x.strip() for x in text.splitlines()
                        if x.strip() and not x.startswith("#")]
            if children:
                child = urllib.parse.urljoin(url, children[0])
                try:
                    s2, _, b2 = fetch(child)
                    return ("OK" if 200 <= s2 < 400 else "PARTIAL",
                            f"HTTP {status}; child HTTP {s2}; {len(body)}B/{len(b2)}B")
                except Exception as e:
                    return "PARTIAL", f"HTTP {status}; HLS {len(body)}B; child failed: {type(e).__name__}"
        return ("OK" if 200 <= status < 400 else "FAIL"), f"HTTP {status}; {len(body)}B; {ctype}"
    except Exception as e:
        return "FAIL", f"{type(e).__name__}: {e}"

def parse_epg_ids(data):
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    root = ET.fromstring(data)
    return {c.attrib["id"] for c in root.findall(".//channel") if c.attrib.get("id")}

def main():
    out = Path("audit")
    out.mkdir(exist_ok=True)

    print("Downloading current playlist...")
    status, _, data = fetch(PLAYLIST_URL, timeout=30)
    rows = parse_playlist(data.decode("utf-8", "replace"))
    unique = {}
    for row in rows:
        if row["url"]:
            unique.setdefault(row["url"], row)
    print(f"Playlist entries: {len(rows)}; unique URLs: {len(unique)}")

    results = []
    for n, (url, row) in enumerate(unique.items(), 1):
        name = attr(row["extinf"], "tvg-name")
        state, detail = audit_stream(url)
        print(f"[{n}/{len(unique)}] {state} {name}")
        results.append([attr(row["extinf"], "tvg-id"), name,
                        attr(row["extinf"], "group-title"), url, state, detail])

    with (out / "stream-audit.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["tvg-id", "tvg-name", "group", "url", "status", "detail"])
        w.writerows(results)

    playlist_ids = {attr(r["extinf"], "tvg-id") for r in rows if attr(r["extinf"], "tvg-id")}
    epg_lines = []
    for epg_url in EPG_URLS:
        try:
            _, _, data = fetch(epg_url, timeout=30)
            ids = parse_epg_ids(data)
            matched = {x for x in playlist_ids if x in ids or base_id(x) in ids}
            epg_lines.append(f"- {epg_url}: {len(matched)}/{len(playlist_ids)} playlist IDs matched")
            print(f"EPG OK: {epg_url} ({len(ids)} channel IDs; {len(matched)} matched)")
        except Exception as e:
            epg_lines.append(f"- {epg_url}: FAILED — {type(e).__name__}: {e}")
            print(f"EPG FAIL: {epg_url}: {type(e).__name__}: {e}")

    ok = sum(x[4] == "OK" for x in results)
    partial = sum(x[4] == "PARTIAL" for x in results)
    fail = sum(x[4] == "FAIL" for x in results)
    summary = [
        "# Stream + EPG audit", "",
        f"- Playlist entries: {len(rows)}",
        f"- Unique stream URLs tested: {len(unique)}",
        f"- Stream OK: {ok}",
        f"- Stream PARTIAL: {partial}",
        f"- Stream FAIL: {fail}", "",
        "## EPG coverage", "",
        *epg_lines, "",
        "## Interpretation", "",
        "OK means the URL and, for HLS, the first referenced child playlist/segment returned HTTP 2xx/3xx.",
        "PARTIAL means the parent HLS playlist was reachable but its first child could not be fetched.",
        "FAIL means the request could not be completed or returned a non-success HTTP status.",
        "This is an HTTP/HLS reachability audit, not a guarantee of continuous playback in every IPTV player."
    ]
    (out / "SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
