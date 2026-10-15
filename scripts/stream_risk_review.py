#!/usr/bin/env python3
"""Report fragile playlist URL patterns without leaking credentials or mutating routes."""
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

PLAYLIST = Path("IPTV-Playlist.m3u")
HEALTH = Path("reports/stream-health.md")
REPORT = Path("reports/stream-risk-review.md")
ATTR = re.compile(r'([\w-]+)="([^"]*)"')
PROXY_HOSTS = {"iptv-proxy.ahmed-bd-org.workers.dev", "iptvlive.ahmed-bd-org.workers.dev"}
TOKEN_KEYS = {"hdnts", "token", "sig", "signature", "jwt", "session", "key", "authorization"}

def playlist_rows():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    result, current = [], None
    for line_no, line in enumerate(lines, 1):
        if line.startswith("#EXTINF:"):
            a = dict(ATTR.findall(line))
            current = {"line":line_no, "name":a.get("tvg-name") or line.rsplit(",",1)[-1].strip(),
                       "group":a.get("group-title","").strip() or "Uncategorized", "url":""}
        elif current and line.strip().startswith(("http://","https://")):
            current["url"] = line.strip()
            result.append(current)
            current = None
    return result

def main():
    streamtest, signed, xtream, proxies, api_relays = [], [], [], [], []
    for row in playlist_rows():
        if not row["url"]:
            continue
        u = urlsplit(row["url"])
        host, path = u.netloc, u.path
        item = {"name":row["name"], "group":row["group"], "host":host, "path":path}
        if "/streamtest/" in path.lower():
            streamtest.append(item)
        qkeys = sorted({part.split("=",1)[0].lower() for part in u.query.split("&")
                        if part and part.split("=",1)[0].lower() in TOKEN_KEYS})
        if qkeys:
            signed.append({**item,"keys":", ".join(qkeys)})
        if re.search(r"/live/[^/?#]+/[^/?#]+/[^/?#]+\.ts(?:[?#]|$)", path, re.I):
            safe_path = re.sub(r"(/live/)[^/]+/[^/]+/([^/]+\.ts)", r"\1[REDACTED]/[REDACTED]/\2", path, flags=re.I)
            xtream.append({**item,"path":safe_path})
        if host.lower() in PROXY_HOSTS:
            proxies.append(item)
        if host.lower() == "homair-tv-production.up.railway.app" and path.lower().startswith("/api/play/"):
            api_relays.append(item)

    health = HEALTH.read_text(encoding="utf-8") if HEALTH.exists() else ""
    metrics = []
    labels = ["Streams tested","Reachable","Failed this check","Persistent failures (3+ consecutive)",
              "HTTP 401/403 (auth)","HTTP 404 (not found)","HTTP 5xx (server)","Timeout"]
    for label in labels:
        m = re.search(r"- "+re.escape(label)+r": \*\*(\d+)\*\*", health)
        if m:
            metrics.append((label,m.group(1)))
    persistent = []
    if "## Persistent Failures" in health:
        chunk = health.split("## Persistent Failures",1)[1].split("\n## ",1)[0]
        persistent = [line.strip() for line in chunk.splitlines() if line.strip().startswith("- ")]

    lines = [
        "# Stream Risk Review", "",
        "Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.", "",
        "## Summary", "",
        f"- /streamtest/ endpoints: **{len(streamtest)}**",
        f"- Signed/token-query endpoints: **{len(signed)}**",
        f"- Xtream-style credential paths (credentials redacted): **{len(xtream)}**",
        f"- Proxy/worker-host routes: **{len(proxies)}** ({sum(x['group'] != 'Backup' for x in proxies)} primary, {sum(x['group'] == 'Backup' for x in proxies)} Backup)",
        f"- /api/play/ relay routes: **{len(api_relays)}**", "",
        "## Latest Stream-Health Snapshot", "",
        "| Metric | Count |", "|---|---:|"
    ]
    lines += [f"| {k} | {v} |" for k,v in metrics]
    lines += ["", "### Persistent failures", ""] + (persistent or ["No persistent failures recorded."])
    lines += ["", "## /streamtest/ Endpoints", "", "| Channel | Group | Host | Path |", "|---|---|---|---|"]
    lines += [f"| {x['name']} | {x['group']} | {x['host']} | {x['path']} |" for x in streamtest] or ["| — | — | — | — |"]
    lines += ["", "## Signed / Token-Query Endpoints", "",
              "Query values are omitted because they may be expiring signatures or access tokens.", "",
              "| Channel | Group | Host | Parameter names |", "|---|---|---|---|"]
    lines += [f"| {x['name']} | {x['group']} | {x['host']} | {x['keys']} |" for x in signed] or ["| — | — | — | — |"]
    lines += ["", "## Xtream-Style Credential Paths", "",
              "Credentials are intentionally redacted; only the host and safe route pattern are shown.", "",
              "| Channel | Group | Host | Redacted path |", "|---|---|---|---|"]
    lines += [f"| {x['name']} | {x['group']} | {x['host']} | {x['path']} |" for x in xtream] or ["| — | — | — | — |"]
    lines += ["", "## Proxy / Worker-Host Routes", "",
              "Worker routes are relayed endpoints, not direct broadcaster sources. The Sananda primary is the highest-priority route to replace with a verified direct source. Backup candidates are retained pending verification.", "",
              "| Channel | Group | Host |", "|---|---|---|"]
    lines += [f"| {x['name']} | {x['group']} | {x['host']} |" for x in proxies] or ["| — | — | — |"]
    lines += ["", "## Hosted /api/play/ Relay Routes", "",
              "| Channel | Group | Host | Route type |", "|---|---|---|---|"]
    lines += [f"| {x['name']} | {x['group']} | {x['host']} | /api/play/ |" for x in api_relays] or ["| — | — | — | — |"]
    lines += ["", "## Recommendations", "",
              "- Keep fragile routes unchanged until a working, authorized replacement is confirmed.",
              "- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.",
              "- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.",
              "- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.",
              "- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.", ""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Stream risk review: streamtest={len(streamtest)} signed={len(signed)} xtream={len(xtream)} proxy={len(proxies)} api-relay={len(api_relays)}")

if __name__ == "__main__":
    main()
