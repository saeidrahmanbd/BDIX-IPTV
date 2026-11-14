#!/usr/bin/env python3
"""Daily International playlist stream monitor and three-day retirement policy."""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import re
import socket
import ssl
import time
import unicodedata
from collections import Counter, defaultdict

import reorganize_international_playlist as international_policy
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

PLAYLIST = Path("International-Playlist.m3u")
HISTORY = Path("reports/international-stream-health-history.json")
REPORT = Path("reports/international-stream-health.md")
REVIEW = "Review"
FAILURE_LIMIT = 3
WORKERS = 48
TIMEOUT = 8
RETRIES = 2
READ_BYTES = 8192
DEFINITIVE_HTTP = {404, 410}
INCONCLUSIVE_HTTP = set(range(400, 600)) - DEFINITIVE_HTTP
SECRET_QUERY = {
    "token", "access_token", "refresh_token", "sig", "signature", "jwt",
    "session", "key", "api_key", "apikey", "authorization", "auth",
    "client_secret", "hdnts", "expires", "e", "username", "user",
    "password", "passwd", "pass",
}
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(info):
    return dict(ATTR.findall(info))


def name_of(info):
    a = attrs(info)
    return (a.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()


def group_of(info):
    return attrs(info).get("group-title", "").strip()


def set_group(info, group):
    p = re.compile(r'(\bgroup-title=")[^"]*(")')
    if p.search(info):
        return p.sub(lambda m: m.group(1) + group + m.group(2), info, count=1)
    return re.sub(r"^(#EXTINF:\S+)", lambda m: m.group(1) + f' group-title="{group}"', info, count=1)


def parse(text):
    pre, blocks, current = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is None:
            pre.append(line)
        else:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return pre, blocks


def urls(block):
    return [s.strip() for s in block[1:] if s.strip().startswith(("http://", "https://"))]


def norm_name(s):
    s = unicodedata.normalize("NFKD", str(s or "")).casefold()
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s)


def stream_key(info, url):
    """Fingerprint a stream without persisting signed URL or credentials."""
    p = urlsplit(url.strip())
    host = (p.hostname or "").casefold()
    try:
        port = p.port
    except ValueError:
        port = None
    netloc = host + (f":{port}" if port else "")
    path = re.sub(
        r"(?i)(/(?:live|movie|series|timeshift)/)[^/]+/[^/]+/",
        r"\1{user}/{password}/",
        p.path,
    )
    query = sorted(
        (k.casefold(), v) for k, v in parse_qsl(p.query, keep_blank_values=True)
        if k.casefold() not in SECRET_QUERY
    )
    safe = urlunsplit((p.scheme.casefold(), netloc, path, urlencode(query), ""))
    a = attrs(info)
    identity = "|".join((
        (a.get("tvg-id") or a.get("channel-id") or "").strip().casefold(),
        a.get("tvg-country", "").strip().upper(),
        norm_name(name_of(info)),
        safe,
    ))
    return hashlib.sha256(identity.encode()).hexdigest()


def headers_for(block):
    a = attrs(block[0])
    h = {
        "User-Agent": a.get("http-user-agent") or "BDIX-IPTV-International-Health/1.0",
        "Accept": "*/*",
        "Range": f"bytes=0-{READ_BYTES - 1}",
        "Connection": "close",
    }
    if a.get("http-referrer"):
        h["Referer"] = a["http-referrer"]
    if a.get("http-origin"):
        h["Origin"] = a["http-origin"]
    for line in block[1:]:
        m = re.match(r"^\s*#EXTVLCOPT:http-(user-agent|referrer|origin)=(.*)$", line, re.I)
        if m:
            h[{"user-agent": "User-Agent", "referrer": "Referer", "origin": "Origin"}[m.group(1).lower()]] = m.group(2).strip()
    return h


def fetch(url, headers):
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=TIMEOUT) as r:
            return {
                "kind": "response", "status": int(getattr(r, "status", 200) or 200),
                "data": r.read(READ_BYTES), "type": str(r.headers.get("Content-Type", "")),
                "url": str(r.geturl()),
            }
    except HTTPError as e:
        return {"kind": "http", "status": e.code, "data": b"", "type": ""}
    except URLError as e:
        why = e.reason
        if isinstance(why, socket.gaierror):
            label = "DNS"
        elif isinstance(why, ssl.SSLError):
            label = "TLS"
        elif isinstance(why, (TimeoutError, socket.timeout)):
            label = "Timeout"
        elif isinstance(why, (ConnectionError, ConnectionResetError, ConnectionRefusedError)):
            label = "Connection"
        else:
            label = "Network"
        return {"kind": "network", "status": 0, "data": b"", "type": "", "error": label}
    except (TimeoutError, socket.timeout):
        return {"kind": "network", "status": 0, "data": b"", "type": "", "error": "Timeout"}
    except ssl.SSLError:
        return {"kind": "network", "status": 0, "data": b"", "type": "", "error": "TLS"}
    except Exception:
        return {"kind": "network", "status": 0, "data": b"", "type": "", "error": "Other"}


def http_state(status):
    return "fail" if int(status) in DEFINITIVE_HTTP else "inconclusive"


def probe_resource(url, headers, depth=0):
    r = fetch(url, headers)
    if r["kind"] == "http":
        return {"state": http_state(r["status"]), "status": r["status"], "reason": f"HTTP {r['status']}", "type": r["type"], "bytes": 0}
    if r["kind"] == "network":
        return {"state": "inconclusive", "status": 0, "reason": r.get("error", "Network"), "type": "", "bytes": 0}
    status, data, ctype = r["status"], r["data"], (r["type"] or "").casefold()
    if status >= 400:
        return {"state": http_state(status), "status": status, "reason": f"HTTP {status}", "type": ctype, "bytes": len(data)}
    if not data:
        return {"state": "inconclusive", "status": status, "reason": "Empty response; not proof of a dead stream", "type": ctype, "bytes": 0}
    sample = data.lstrip(b"\xef\xbb\xbf \t\r\n")
    low = sample[:1024].lower()
    if low.startswith((b"<!doctype html", b"<html", b"<head", b"<body")) or "text/html" in ctype or "application/json" in ctype or "text/json" in ctype:
        return {"state": "inconclusive", "status": status, "reason": "HTML/JSON response may be an access restriction, not media", "type": ctype, "bytes": len(data)}
    if any(x in low for x in (b"access denied", b"unauthorized", b"forbidden", b"stream unavailable", b"channel offline")):
        return {"state": "inconclusive", "status": status, "reason": "Access-restricted/provider-denial response", "type": ctype, "bytes": len(data)}

    final_url = r.get("url", url)
    final_path = urlsplit(final_url).path.casefold()
    hls = sample.startswith(b"#EXTM3U") or "mpegurl" in ctype or final_path.endswith(".m3u8")
    if hls:
        if depth >= 2:
            return {"state": "inconclusive", "status": status, "reason": "HLS nesting limit; media status unconfirmed", "type": ctype, "bytes": len(data)}
        lines = sample.decode("utf-8", "replace").splitlines()
        resources = [s.strip() for s in lines if s.strip() and not s.lstrip().startswith("#")]
        if not resources:
            return {"state": "inconclusive", "status": status, "reason": "HLS manifest has no accessible media resources", "type": ctype, "bytes": len(data)}
        inconclusive = None
        last_failure = None
        for item in resources[:2]:
            target = urljoin(final_url, item)
            if urlsplit(target).scheme.casefold() not in {"http", "https"}:
                continue
            child = probe_resource(target, headers, depth + 1)
            if child["state"] == "ok":
                return {"state": "ok", "status": child["status"], "reason": "HLS media segment reachable", "type": child["type"] or ctype, "bytes": child["bytes"]}
            if child["state"] == "inconclusive":
                inconclusive = child
            else:
                last_failure = child
        return inconclusive or last_failure or {"state": "inconclusive", "status": status, "reason": "No media segment could be conclusively checked", "type": ctype, "bytes": len(data)}

    if "dash+xml" in ctype or sample[:256].lstrip().startswith(b"<?xml"):
        if b"<MPD" in sample[:4096] and (b"<Segment" in sample or b"<BaseURL" in sample):
            return {"state": "ok", "status": status, "reason": "DASH manifest reachable", "type": ctype, "bytes": len(data)}
        if "dash+xml" in ctype:
            return {"state": "inconclusive", "status": status, "reason": "Invalid/unrecognized DASH manifest; endpoint status inconclusive", "type": ctype, "bytes": len(data)}
    return {"state": "ok", "status": status, "reason": "Media bytes received", "type": ctype, "bytes": len(data)}


def probe(url, headers):
    result = {"state": "fail", "status": 0, "reason": "No probe result", "type": "", "bytes": 0}
    for attempt in range(RETRIES):
        result = probe_resource(url, headers)
        if result["state"] in {"ok", "inconclusive"}:
            return result
        if attempt + 1 < RETRIES:
            time.sleep(0.7)
    return result


def validate_probe_batch(results):
    """Abort a scan that cannot prove any stream is reachable.

    A runner-wide routing/DNS/TLS outage must never turn into thousands of
    false Review labels. This gate runs before the playlist/history is changed.
    """
    total = len(results)
    reachable = sum(item.get("state") == "ok" for item in results)
    failures = sum(item.get("state") == "fail" for item in results)
    if total >= 100 and reachable == 0:
        raise SystemExit(
            "Safety stop: zero media streams were reachable in this batch; "
            "the runner/network may be restricted. Playlist and failure history were not changed."
        )
    if total >= 100 and failures >= int(total * 0.80) and reachable < int(total * 0.02):
        raise SystemExit(
            "Safety stop: the scan shows a repository-wide reachability anomaly "
            "(at least 80% hard failures and under 2% reachable). "
            "Playlist and failure history were not changed."
        )


def load_history():
    if not HISTORY.is_file():
        return {"schema_version": 1, "entries": {}, "removed": []}
    try:
        x = json.loads(HISTORY.read_text(encoding="utf-8"))
    except Exception:
        x = {}
    return {
        "schema_version": 1,
        "entries": x.get("entries", {}) if isinstance(x, dict) and isinstance(x.get("entries"), dict) else {},
        "removed": x.get("removed", []) if isinstance(x, dict) and isinstance(x.get("removed"), list) else [],
    }


def validate_metadata_preservation(before_text, after_text, removed_urls):
    """Ensure health automation changes grouping only, never channel metadata."""
    _, before_blocks = parse(before_text)
    _, after_blocks = parse(after_text)

    def by_url(blocks):
        result = {}
        for block in blocks:
            stream_urls = urls(block)
            if len(stream_urls) != 1:
                raise ValueError(f"Expected one stream URL for {name_of(block[0])!r}")
            stream_url = stream_urls[0]
            if stream_url in result:
                raise ValueError(f"Duplicate stream URL in playlist: {stream_url}")
            result[stream_url] = block
        return result

    before = by_url(before_blocks)
    after = by_url(after_blocks)
    if set(after) - set(before):
        raise ValueError("Health automation unexpectedly added stream rows")
    actually_removed = set(before) - set(after)
    if actually_removed != set(removed_urls):
        raise ValueError("Removed stream rows do not match the three-day retirement decisions")

    for stream_url, new_block in after.items():
        old_block = before[stream_url]
        old_attrs = attrs(old_block[0])
        new_attrs = attrs(new_block[0])
        old_attrs.pop("group-title", None)
        new_attrs.pop("group-title", None)
        if old_attrs != new_attrs:
            raise ValueError(f"Health automation changed channel metadata/logo for {name_of(old_block[0])!r}")
        if old_block[1:] != new_block[1:]:
            raise ValueError(f"Health automation changed stream directives/URL for {name_of(old_block[0])!r}")


def validate_rendered_playlist(playlist_text):
    """Validate safe playlist structure and the canonical Review/discovery tail."""
    preamble, blocks = parse(playlist_text)
    registry_lines = [
        line for line in preamble
        if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")
    ]
    if len(registry_lines) != 1:
        raise ValueError(f"Expected one category registry; found {len(registry_lines)}")
    registry = json.loads(registry_lines[0].split(":", 1)[1])
    if not isinstance(registry, list) or len(registry) != len(set(registry)):
        raise ValueError("Category registry must contain unique category names")
    if registry[-3:] != ["New Channels", "New Backups", "Backup"]:
        raise ValueError("Category registry must end New Channels/New Backups/Backup")
    if REVIEW not in registry or registry.index(REVIEW) > registry.index("New Channels"):
        raise ValueError("Review must be present before the New Channels discovery queue")

    seen_urls = set()
    seen_groups = []
    rank = {group: index for index, group in enumerate(registry)}
    for block in blocks:
        group = group_of(block[0])
        if not group or group not in rank:
            raise ValueError(f"Missing/unregistered category for {name_of(block[0])!r}: {group!r}")
        if not seen_groups or group != seen_groups[-1]:
            seen_groups.append(group)
        stream_urls = urls(block)
        if len(stream_urls) != 1:
            raise ValueError(f"Expected one HTTP(S) URL for {name_of(block[0])!r}; found {len(stream_urls)}")
        if stream_urls[0] in seen_urls:
            raise ValueError(f"Duplicate stream URL for {name_of(block[0])!r}")
        seen_urls.add(stream_urls[0])

    expected_groups = [group for group in registry if group in set(seen_groups)]
    if seen_groups != expected_groups:
        raise ValueError("Playlist groups do not follow the registered category order")
    return True


def render_playlist(preamble, blocks):
    idx = next((i for i, line in enumerate(preamble) if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")), None)
    if idx is None:
        raise ValueError("Missing #PLAYLIST-STUDIO-CATEGORIES registry; no playlist changes written")
    registry = json.loads(preamble[idx].split(":", 1)[1])
    if not isinstance(registry, list):
        raise ValueError("Playlist category registry is not a list")
    if REVIEW not in registry:
        pos = next((i for i, g in enumerate(registry) if g in {"New Channels", "New Backups", "Backup"}), len(registry))
        registry.insert(pos, REVIEW)
    # A recovered stream can create the fifth qualifying primary identity for
    # a country. Register that newly materialized country group before the
    # International catch-all and the fixed tail queues.
    present_groups = {group_of(block[0]) for block in blocks if group_of(block[0])}
    missing_groups = present_groups - set(registry)
    if missing_groups:
        tail_names = set(international_policy.TAIL)
        insert_at = next((i for i, group in enumerate(registry) if group == "International"), None)
        if insert_at is None:
            insert_at = next((i for i, group in enumerate(registry) if group in tail_names), len(registry))
        dynamic = sorted(group for group in missing_groups if group not in tail_names)
        registry[insert_at:insert_at] = dynamic
    preamble[idx] = "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry, ensure_ascii=False)
    rank = {g: i for i, g in enumerate(registry)}
    def natural(s):
        return tuple(int(x) if x.isdigit() else x.casefold() for x in re.split(r"(\d+)", s or ""))
    blocks.sort(key=lambda b: (rank.get(group_of(b[0]), len(rank)), natural(name_of(b[0])), (urls(b)[0] if urls(b) else "").casefold()))
    return "\n".join(preamble + [line for b in blocks for line in b]).rstrip() + "\n"



def _row_identity_keys(info: str, country: str) -> set[tuple[str, str, str]]:
    """Stable channel identity keys for duplicate-primary detection."""
    a = attrs(info)
    name_key = international_policy.channel_key(name_of(info))
    keys = {("name", country, name_key)} if name_key else set()
    for field in ("tvg-id", "channel-id"):
        value = (a.get(field) or "").strip().casefold().split("@", 1)[0]
        if value:
            keys.add(("id", country, value))
    return keys


def _primary_identity_state(blocks):
    """Index existing primary identities and non-BD/IN country-group counts."""
    primary_keys: set[tuple[str, str, str]] = set()
    country_ids: dict[str, set[str]] = defaultdict(set)
    excluded = {"backup", "backups", "not playing", "review",
                "new channels", "new backup", "new backups"}
    for block in blocks:
        group = group_of(block[0])
        if group.casefold() in excluded:
            continue
        a = attrs(block[0])
        name = name_of(block[0])
        country = international_policy.country_code(a, group, name)
        if not country or country == "ZZ":
            continue
        primary_keys.update(_row_identity_keys(block[0], country))
        is_country_group = (
            group == "International"
            or (country == "PK" and group == "Pakistani")
            or international_policy.country_from_group(group) == country
        )
        if group.casefold() != "adult" and country not in {"BD", "IN"} and is_country_group:
            country_ids[country].add(international_policy.channel_key(name))
    return primary_keys, country_ids


def _review_recovery_target(info: str, original_group: str,
                            primary_keys: set[tuple[str, str, str]],
                            country_ids: dict[str, set[str]]) -> str | None:
    """Classify a working Review stream, routing duplicate identities to Backup."""
    a = attrs(info)
    name = name_of(info)
    context_group = original_group if original_group and original_group.casefold() != REVIEW.casefold() else "International"
    country = international_policy.country_code(a, context_group, name)
    if not country or country == "ZZ":
        return None
    if country == "IN" and international_policy.bd_policy.prohibited_channel(a, name, "IN"):
        return None
    target, kind, reason = international_policy.classify(
        a, name, context_group, country, promote_backup=True
    )
    if reason or not target or target == "Review":
        return None
    # "Backup" with no inferred primary/genre kind is the organizer's
    # quarantine outcome for an out-of-policy or unclassifiable channel, not
    # proof that a working Review row is a valid alternate stream.
    if target == "Backup" and kind is None:
        return None

    name_key = international_policy.channel_key(name)
    identity_keys = _row_identity_keys(info, country)
    if target != "Backup" and identity_keys & primary_keys:
        return "Backup"

    # Country-specific groups require five unique primary identities. Review
    # rows and Backup alternates do not count; the recovered channel itself does.
    if target == "__FOREIGN__":
        candidates = set(country_ids.get(country, set()))
        if name_key:
            candidates.add(name_key)
        target = (
            international_policy.discovery.country_group(country)
            if len(candidates) >= international_policy.discovery.COUNTRY_THRESHOLD
            else "International"
        ) or "International"
    elif target == "Pakistani":
        candidates = set(country_ids.get("PK", set()))
        if name_key:
            candidates.add(name_key)
        if len(candidates) < international_policy.discovery.COUNTRY_THRESHOLD:
            target = "International"

    if target not in {"Backup", "Review"}:
        primary_keys.update(identity_keys)
        if target != "Adult" and country not in {"BD", "IN"} and (
            target == "International"
            or target == "Pakistani"
            or international_policy.country_from_group(target) == country
        ):
            country_ids[country].add(name_key)
    return target


def apply_results(text, results, history, check_date):
    pre, blocks = parse(text)
    if len(results) != len(blocks):
        raise ValueError("Probe-result count differs from playlist-entry count")
    today = date.fromisoformat(check_date)
    yesterday = (today - timedelta(days=1)).isoformat()
    entries = history.setdefault("entries", {})
    removed_log = history.setdefault("removed", [])
    output, events, removed_urls = [], [], set()
    primary_keys, country_ids = _primary_identity_state(blocks)

    for block, result in zip(blocks, results):
        entry_urls = urls(block)
        if len(entry_urls) != 1:
            raise ValueError(f"Expected exactly one stream URL for {name_of(block[0])!r}")
        info, url = block[0], entry_urls[0]
        key, a, current = stream_key(info, url), attrs(info), group_of(info)
        name = name_of(info)
        state = result.get("state", "inconclusive")
        if state not in {"ok", "fail", "inconclusive"}:
            state = "inconclusive"
        rec = entries.get(key)
        if not isinstance(rec, dict) or rec.get("removed"):
            rec = {
                "name": name,
                "tvg_id": a.get("tvg-id") or a.get("channel-id", ""),
                "country": a.get("tvg-country", ""),
                "original_group": current,
                "auto_review": False,
                "consecutive_failures": 0,
                "last_checked_date": "",
                "last_status": "",
                "removed": False,
            }
            entries[key] = rec

        action = "unchanged"
        if rec.get("last_checked_date") == check_date:
            action = "already-checked-today"
        else:
            previous_date, previous_status = rec.get("last_checked_date", ""), rec.get("last_status", "")
            if state == "ok":
                if current.casefold() == REVIEW.casefold():
                    original = rec.get("original_group", "")
                    target = _review_recovery_target(info, original, primary_keys, country_ids)
                    if target and target.casefold() != REVIEW.casefold():
                        info = set_group(info, target)
                        current = target
                        action = "restored-to-backup" if target == "Backup" else "restored-to-primary"
                rec["consecutive_failures"] = 0
                rec["auto_review"] = False
                rec["last_status"] = "ok"
                rec["last_ok_date"] = check_date
            elif state == "fail":
                streak = int(rec.get("consecutive_failures", 0))
                streak = streak + 1 if previous_date == yesterday and previous_status == "fail" else 1
                rec["consecutive_failures"] = streak
                if current.casefold() != REVIEW.casefold():
                    rec["original_group"] = current
                    rec["auto_review"] = True
                    info = set_group(info, REVIEW)
                    current = REVIEW
                    action = "moved-to-review"
                if streak >= FAILURE_LIMIT:
                    rec["removed"] = True
                    rec["removed_date"] = check_date
                    action = "removed-after-three-failed-days"
                rec["last_status"] = "fail"
                rec["last_failure_date"] = check_date
            else:
                # 401/403/429/geo restrictions and uncertain responses reset the
                # consecutive-failure streak without releasing an existing Review row.
                rec["consecutive_failures"] = 0
                rec["last_status"] = "inconclusive"
            rec["last_checked_date"] = check_date

        rec["name"] = name
        rec["tvg_id"] = a.get("tvg-id") or a.get("channel-id", "")
        rec["country"] = a.get("tvg-country", "")
        event = {
            "name": name,
            "tvg_id": rec.get("tvg_id", ""),
            "original_group": rec.get("original_group", current),
            "group_before": group_of(block[0]),
            "group_after": current,
            "state": state,
            "streak": int(rec.get("consecutive_failures", 0)),
            "action": action,
            "status": int(result.get("status", 0) or 0),
            "reason": str(result.get("reason", "")),
        }
        if action == "removed-after-three-failed-days":
            removed_urls.add(url)
            removed_log.append({
                "name": name, "tvg_id": rec.get("tvg_id", ""),
                "original_group": rec.get("original_group", ""),
                "removed_date": check_date, "consecutive_failures": rec["consecutive_failures"],
            })
            events.append(event)
            continue
        block[0] = info
        output.append(block)
        events.append(event)

    history["schema_version"] = 1
    history["entries"] = entries
    history["removed"] = removed_log[-1000:]
    updated_text = render_playlist(pre, output)
    validate_metadata_preservation(text, updated_text, removed_urls)
    validate_rendered_playlist(updated_text)
    return updated_text, history, events


def build_report(events, history, check_date, generated, total):
    ok = sum(e["state"] == "ok" for e in events)
    failures = [e for e in events if e["state"] == "fail"]
    uncertain = [e for e in events if e["state"] == "inconclusive"]
    moved = [e for e in events if e["action"] == "moved-to-review"]
    recovered = [e for e in events if e["action"] in {"restored", "restored-to-primary", "restored-to-backup"}]
    removed = [e for e in events if e["action"] == "removed-after-three-failed-days"]
    flagged = sum(1 for r in history["entries"].values() if r.get("auto_review") and not r.get("removed"))
    inconclusive_reasons = Counter(
        (e.get("reason") or (f"HTTP {e['status']}" if e.get("status") else "Unspecified"))
        for e in uncertain
    )
    inconclusive_statuses = Counter(
        str(e["status"]) for e in uncertain if int(e.get("status", 0) or 0) > 0
    )
    lines = [
        "# International Stream Health", "",
        f"- Generated: **{generated}**",
        f"- Bangladesh check date: **{check_date}**",
        f"- Playlist rows checked: **{total}**",
        f"- Reachable media streams: **{ok}**",
        f"- Definitive failures today: **{len(failures)}**",
        f"- Inconclusive checks: **{len(uncertain)}**",
        f"- Newly moved to Review: **{len(moved)}**",
        f"- Restored from Review to primary/Backup: **{len(recovered)}**",
        f"- Removed after three consecutive failed days: **{len(removed)}**",
        f"- Automatically flagged rows still under Review: **{flagged}**", "",
        "## Rules", "",
        "- First definitive failed day: move the row to Review; all metadata and its logo stay intact.",
        "- A successful later check reclassifies a Review row to its eligible primary category; a working alternate whose identity already has a primary is placed in Backup.",
        "- Third consecutive definitive failed Bangladesh calendar day: remove the stream row.",
        "- A working Review row that is not eligible under the country/genre policy remains in Review.",
        "- Reruns on the same Bangladesh date do not increase the streak; a missed day restarts it.",
        "- Only HTTP 404/410 are definitive HTTP failures. All other HTTP errors, access-denial pages, empty responses, DNS/TLS/timeouts and connection failures are inconclusive and never advance the three-day retirement streak.",
        "- HLS validation checks a media segment rather than relying only on a manifest HTTP 200. Raw stream URLs and credentials are not stored in the report/history.", "",
        "## Newly marked Review", "",
    ]
    lines += [f"- **{e['name']}** — prior group: {e['group_before']} — {e['reason'] or e['status']}" for e in moved] or ["None."]
    lines += ["", "## Failed streams still under Review", ""]
    pending = [e for e in failures if e["action"] != "removed-after-three-failed-days"]
    lines += [f"- **{e['name']}** — {e['streak']}/3 consecutive days — {e['reason'] or e['status']}" for e in pending] or ["None."]
    lines += ["", "## Recovered streams", ""]
    lines += [f"- **{e['name']}** — restored to **{e['group_after']}**" for e in recovered] or ["None."]
    lines += ["", "## Removed after three consecutive failed days", ""]
    lines += [f"- **{e['name']}** — former group: **{e['original_group']}**" for e in removed] or ["None."]
    lines += ["", "## Inconclusive reason summary", ""]
    lines += [f"- **{reason}** — {count}" for reason, count in inconclusive_reasons.most_common()] or ["None."]
    if inconclusive_statuses:
        lines += ["", "### HTTP status breakdown", ""]
        lines += [f"- **HTTP {status}** — {count}" for status, count in sorted(inconclusive_statuses.items(), key=lambda item: int(item[0]))]
    lines += ["", "## Inconclusive checks", ""]
    lines += [f"- **{e['name']}** — HTTP {e['status']} — {e['reason'] or 'inconclusive'}" if e["status"] else f"- **{e['name']}** — {e['reason'] or 'inconclusive'}" for e in uncertain] or ["None."]
    return "\n".join(lines) + "\n"


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("International-Playlist.m3u missing; refusing to proceed")
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    _, blocks = parse(text)
    if not blocks:
        raise SystemExit("International playlist is empty; refusing to proceed")
    targets = []
    for block in blocks:
        u = urls(block)
        if len(u) != 1:
            raise SystemExit(f"Expected one HTTP URL for {name_of(block[0])!r}; found {len(u)}. No changes made.")
        targets.append((u[0], headers_for(block)))

    results = [None] * len(targets)
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(probe, u, h): i for i, (u, h) in enumerate(targets)}
        for future in concurrent.futures.as_completed(futures):
            i = futures[future]
            try:
                results[i] = future.result()
            except Exception:
                results[i] = {"state": "inconclusive", "status": 0, "reason": "Unexpected probe exception"}
    if any(result is None for result in results):
        raise SystemExit("Incomplete probe run; no playlist changes written")

    check_date = datetime.now(ZoneInfo("Asia/Dhaka")).date().isoformat()
    validate_probe_batch(results)
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    updated, history, events = apply_results(text, results, load_history(), check_date)
    PLAYLIST.write_text(updated, encoding="utf-8")
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    HISTORY.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(build_report(events, history, check_date, generated, len(blocks)), encoding="utf-8")
    print(
        "International stream health: "
        f"checked={len(blocks)} "
        f"ok={sum(e['state']=='ok' for e in events)} "
        f"failed={sum(e['state']=='fail' for e in events)} "
        f"inconclusive={sum(e['state']=='inconclusive' for e in events)} "
        f"reviewed={sum(e['action']=='moved-to-review' for e in events)} "
        f"recovered={sum(e['action']=='restored' for e in events)} "
        f"removed={sum(e['action']=='removed-after-three-failed-days' for e in events)}"
    )


if __name__ == "__main__":
    main()
