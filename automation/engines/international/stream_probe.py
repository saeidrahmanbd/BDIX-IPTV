"""Conservative single-stream probe adapter; observations feed policy but never edit playlists."""
from __future__ import annotations
from datetime import date
import ipaddress
import socket
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from automation.engines.international.stream_failure_policy import Probe

DEFAULT_TIMEOUT_SECONDS = 8
MAX_RESPONSE_SAMPLE = 4096

def _validate_probe_url(url: str) -> None:
    parsed=urlsplit(url.strip())
    if parsed.scheme not in {"http","https"} or not parsed.hostname:
        raise ValueError("stream probe URL must be absolute HTTP(S)")
    if parsed.username or parsed.password:
        raise ValueError("stream probe URL must not embed credentials")
    host=parsed.hostname.casefold().rstrip(".")
    if host=="localhost" or host.endswith(".localhost") or host.endswith(".local"):
        raise ValueError("local hostnames are not allowed for stream probes")
    try:
        address=ipaddress.ip_address(host)
    except ValueError:
        address=None
    if address is not None and not address.is_global:
        raise ValueError("non-public IP addresses are not allowed for stream probes")

def _classify_response(status: int, headers, body: bytes, url: str) -> tuple[str,str]:
    if status in (404,410):
        return "dead",f"HTTP {status}"
    if status in (401,403,429) or status >= 500:
        return "unknown",f"HTTP {status}; access/availability could not be confirmed"
    if status not in (200,206):
        return "unknown",f"HTTP {status}; not conclusive"
    content_type=(headers.get("Content-Type") or headers.get("content-type") or "").lower()
    sample=body.lstrip().lower()
    if b"#extm3u" in sample[:2048]:
        return "verified","HLS playlist response"
    if ".mpd" in url.lower() and b"<mpd" in sample[:MAX_RESPONSE_SAMPLE]:
        return "verified","DASH manifest response"
    if any(value in content_type for value in ("mpegurl","mp2t","video/","dash+xml")):
        return "verified",f"media content type: {content_type}"
    if len(body)>=188 and body[0]==0x47:
        return "verified","transport-stream data"
    if sample.startswith((b"<!doctype html",b"<html",b"<head",b'{"error"',b'{"message"',b"access denied")):
        return "dead","HTTP success returned an HTML/error page, not a TV stream"
    return "unknown","response did not clearly identify a live media stream"

def probe_stream(url: str, today: date, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Probe:
    """Issue a small range GET; only explicit dead responses are marked dead."""
    _validate_probe_url(url)
    if timeout < 1 or timeout > 30:
        raise ValueError("probe timeout must be between 1 and 30 seconds")
    request=Request(url.strip(),headers={
        "Range":f"bytes=0-{MAX_RESPONSE_SAMPLE-1}",
        "User-Agent":"BDIX-IPTV-AutomationV2/1.0",
        "Accept":"*/*",
    },method="GET")
    try:
        with urlopen(request,timeout=timeout) as response:
            status=response.getcode()
            body=response.read(MAX_RESPONSE_SAMPLE)
            state,reason=_classify_response(status,response.headers,body,url)
            return Probe(today,status,stream_state=state,reason=reason)
    except HTTPError as exc:
        status=exc.code
        try:
            exc.close()
        except Exception:
            pass
        if status in (401,403):
            return Probe(today,status,auth_error=True,reason=f"HTTP {status}; authentication/access inconclusive")
        if status==429:
            return Probe(today,status,rate_limited=True,reason="HTTP 429; rate limited")
        if status==451:
            return Probe(today,status,geo_blocked=True,reason="HTTP 451; geo/legal restriction")
        state,reason=_classify_response(status,exc.headers or {},b"",url)
        return Probe(today,status,stream_state=state,reason=reason)
    except (URLError,TimeoutError,socket.timeout,OSError) as exc:
        return Probe(today,None,network_error=True,reason=f"network error: {type(exc).__name__}")
