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

def probe_stream(url: str, today: date, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Probe:
    """Issue a one-byte range GET; network/auth/rate/geo outcomes never count as definitive failures."""
    _validate_probe_url(url)
    if timeout < 1 or timeout > 30:
        raise ValueError("probe timeout must be between 1 and 30 seconds")
    request=Request(url.strip(),headers={
        "Range":"bytes=0-0",
        "User-Agent":"BDIX-IPTV-AutomationV2/1.0",
        "Accept":"*/*",
    },method="GET")
    try:
        with urlopen(request,timeout=timeout) as response:
            status=response.getcode()
            return Probe(today,status)
    except HTTPError as exc:
        status=exc.code
        if status in (401,403):
            return Probe(today,status,auth_error=True)
        if status==429:
            return Probe(today,status,rate_limited=True)
        if status==451:
            return Probe(today,status,geo_blocked=True)
        return Probe(today,status)
    except (URLError,TimeoutError,socket.timeout,OSError):
        return Probe(today,None,network_error=True)
