"""Short-lived, privacy-safe cache for XMLTV source downloads.

The EPG workflow audits sources, generates the guide, and audits the result in
separate Python processes. Reusing the same downloaded bytes within one run
keeps all three passes on a consistent source snapshot and avoids downloading
large public feeds repeatedly. Cache filenames are SHA-256 URL digests, so a
private M3U4U URL or credential never appears in the cache path.
"""
import hashlib
import os
import time
import urllib.request
from pathlib import Path

DEFAULT_CACHE_DIR = "/tmp/bdix-iptv-epg-source-cache"
DEFAULT_TTL_SECONDS = 2 * 60 * 60


def fetch_source_bytes(url, *, headers, timeout):
    """Return raw response bytes, reusing a recent per-run cache entry."""
    try:
        ttl_seconds = int(os.environ.get("EPG_SOURCE_CACHE_TTL_SECONDS", str(DEFAULT_TTL_SECONDS)))
    except (TypeError, ValueError):
        ttl_seconds = DEFAULT_TTL_SECONDS

    cache_dir = Path(os.environ.get("EPG_SOURCE_CACHE_DIR", DEFAULT_CACHE_DIR))
    cache_key = hashlib.sha256(str(url).encode("utf-8")).hexdigest()
    cache_path = cache_dir / (cache_key + ".bin")

    if ttl_seconds > 0:
        try:
            stat = cache_path.stat()
            if stat.st_size > 0 and 0 <= time.time() - stat.st_mtime <= ttl_seconds:
                return cache_path.read_bytes()
        except OSError:
            pass

    request = urllib.request.Request(url, headers=dict(headers or {}))
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read()

    if data:
        try:
            cache_dir.mkdir(parents=True, exist_ok=True)
            temporary_path = cache_dir / (cache_key + ".tmp")
            temporary_path.write_bytes(data)
            os.replace(temporary_path, cache_path)
        except OSError:
            # A cache write must never turn a healthy source response into a
            # failed source. The downloaded bytes remain usable by this caller.
            try:
                temporary_path.unlink(missing_ok=True)
            except (OSError, UnboundLocalError):
                pass

    return data
