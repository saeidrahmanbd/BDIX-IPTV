#!/usr/bin/env python3
"""Conservative stream URL identity: normalize scheme/host, preserve path/query case."""
from __future__ import annotations
from urllib.parse import urlsplit, urlunsplit

def stream_url_key(url: str) -> str:
    """Normalize only case-insensitive URI components."""
    value = str(url or "").strip()
    if not value:
        return ""
    try:
        parts = urlsplit(value)
        if not parts.scheme or not parts.netloc:
            return value
        host = parts.hostname
        if not host:
            return value
        port = parts.port
        prefix = ""
        if "@" in parts.netloc:
            prefix, _, _ = parts.netloc.rpartition("@")
            prefix += "@"
        host_key = f"[{host.casefold()}]" if ":" in host else host.casefold()
        if port is not None:
            host_key += f":{port}"
        if parts.netloc.rsplit("@", 1)[-1].endswith(":") and port is None:
            host_key += ":"
        return urlunsplit((parts.scheme.casefold(), prefix + host_key, parts.path, parts.query, parts.fragment))
    except (TypeError, ValueError):
        return value


def stream_endpoint_family_key(url: str) -> str:
    """Identify alternate playlist/track URLs for the same host and path.

    Unlike stream_url_key, this intentionally ignores HTTP-vs-HTTPS and common
    terminal HLS rendition filenames. Host is case-insensitive; path case and
    query are preserved so distinct case-sensitive endpoints are not collapsed.
    """
    value = str(url or "").strip()
    if not value:
        return ""
    try:
        parts = urlsplit(value)
        if not parts.scheme or not parts.netloc or not parts.hostname:
            return value
        host = parts.hostname.casefold()
        if parts.port is not None:
            host += f":{parts.port}"
        path = __import__("re").sub(
            r"/(?:tracks-v\\d+a\\d+/mono(?:\\.ts)?|index|playlist|master|chunks)(?:\\.fmp4)?\\.m3u8$",
            "",
            parts.path,
            flags=__import__("re").IGNORECASE,
        )
        return host + path + ("?" + parts.query if parts.query else "")
    except (TypeError, ValueError):
        return value
