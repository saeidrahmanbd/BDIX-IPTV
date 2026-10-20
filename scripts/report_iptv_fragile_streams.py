#!/usr/bin/env python3
"""Report fragile/session-like IPTV URLs without exposing token or credential values."""
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, quote, unquote, urlencode, urlsplit, urlunsplit

P = Path("IPTV-Playlist.m3u")
OUT = Path("reports/iptv-fragile-streams.md")
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
SENSITIVE = {
    "token", "access_token", "refresh_token", "sig", "signature", "jwt", "session",
    "key", "api_key", "apikey", "authorization", "auth", "client_secret", "hdnts",
    "expires", "e", "username", "user", "password", "passwd", "pass",
}
CREDENTIAL_PATHS = {"live", "movie", "series", "timeshift"}


def attrs(s):
    return dict(ATTR.findall(s))


def parse(t):
    rows, current = [], None
    for line in t.splitlines():
        if line.startswith("#EXTINF:"):
            current = line
        elif current and line.strip().startswith(("http://", "https://")):
            rows.append((attrs(current), line.strip()))
            current = None
    return rows


def redact_url(url):
    """Keep route context but remove userinfo, path credentials and secret query values."""
    try:
        parts = urlsplit(url)
        netloc = parts.netloc.rsplit("@", 1)[-1]
        if "@" in parts.netloc:
            netloc = "REDACTED:REDACTED@" + netloc
        path_parts = parts.path.split("/")
        decoded_parts = [unquote(part).casefold() for part in path_parts]
        for i, segment in enumerate(decoded_parts):
            if segment in CREDENTIAL_PATHS and i + 3 < len(path_parts):
                path_parts[i + 1] = "REDACTED"
                path_parts[i + 2] = "REDACTED"
        safe_path = "/".join(quote(part, safe=":@!$&'()*+,;=-._~%") for part in path_parts)
        query = [(key, "REDACTED" if key.casefold() in SENSITIVE else value)
                 for key, value in parse_qsl(parts.query, keep_blank_values=True)]
        return urlunsplit((parts.scheme, netloc, safe_path, urlencode(query, doseq=True), ""))
    except (TypeError, ValueError):
        return "[URL redacted: invalid URL]"


def main():
    raw = P.read_bytes()
    rows = parse(raw.decode("utf-8-sig"))
    found = []
    for metadata, url in rows:
        parts = urlsplit(url)
        query_names = {key.casefold() for key, _ in parse_qsl(parts.query, keep_blank_values=True)}
        reasons = []
        if query_names & SENSITIVE:
            reasons.append("sensitive query parameter (value redacted)")
        if any(host in url.casefold() for host in ("/api/play/", "workers.dev", "railway.app")):
            reasons.append("dynamic/proxy endpoint")
        if any(part.casefold() in CREDENTIAL_PATHS for part in parts.path.split("/")):
            reasons.append("credential-bearing route pattern (values redacted)")
        if reasons:
            found.append((metadata.get("tvg-name", ""), metadata.get("group-title", ""), redact_url(url), ", ".join(dict.fromkeys(reasons))))

    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    digest = hashlib.sha256(raw).hexdigest()
    tick = chr(96)
    lines = [
        "# IPTV Fragile Stream Review", "",
        f"Generated: **{generated}**",
        f"IPTV-Playlist.m3u SHA-256: **{digest}**", "",
        "These streams are not automatically removed. URL credentials, user information and secret query values are redacted; the remaining route shape is shown for review.",
        "", f"- Flagged streams: **{len(found)}**", "",
        "| Channel | Group | Reason | Sanitized URL |", "|---|---|---|---|",
    ]
    for name, group, safe_url, reason in found:
        clean = lambda value: str(value).replace("|", "%7C").replace(chr(10), " ")
        lines.append(f"| {clean(name)} | {clean(group)} | {clean(reason)} | {tick}{clean(safe_url)}{tick} |")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Fragile stream report: {len(found)} flagged; secret values redacted; playlist SHA-256 {digest}")


if __name__ == "__main__":
    main()
