#!/usr/bin/env python3
"""Probe discovery streams and append a fresh final validation summary."""
from __future__ import annotations
import concurrent.futures
import os
import re
import json
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import discover_international_channels as discovery

RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
LOGOS = Path("logos")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NEWS_RE = re.compile(r"\b(?:news|headlines?|current affairs|zee business|aaj tak|times now|ndtv\s*(?:24x7|india|profit|world|marathi|mp-cg|rajasthan|haryana|bihar|assam)|republic|india today|news18|tv9)\b", re.I)
RELIGIOUS_RE = re.compile(r"\b(?:calvary|santvani|sharnam|sharanam|christian|christ|hindu|hinduism|bhakti|bhakthi|sanatan|sikh|gurbani|jinvani|jain|devotional|gospel|bible|jesus|church|temple|prayer|sermon|satsang|aastha|sanskar|jagran|krishna|shiva|ganesh)\b", re.I)
ISLAMIC_RE = re.compile(r"\b(?:islam|islamic|muslim|quran|koran|allah|muhammad|madani|peace tv|huda|noor|deen|ummah|mecca|makkah|madina|mosque|masjid|sunnah|ramadan|adhan|azan)\b", re.I)
INTL_BAD_RE = re.compile(r"\b(?:news|sports?|kids?|children|documentary|wildlife|religious|religion|devotional|adult|radio|podcast|vod|catchup|test|demo|webcam|timeshift|ppv|paramount network|sony canal novelas|tv land drama|usa network|universal comedy|twentyseven(?: hd)?|rtsh shqip|star trek\s*:\s*(?:deep space nine|the next generation|the original series|voyager)|the twilight zone|the wild wild west)\b", re.I)
FASHION_RE = re.compile(r"\bfashion\s*tv\b", re.I)

def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def attrs(line):
    return dict(ATTR_RE.findall(line))

def display_name(line):
    return line.rsplit(",", 1)[-1].strip()

def parse_playlist(text):
    lines = text.replace("\r", "").splitlines()
    entries, malformed = [], []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines) or not lines[j].strip().lower().startswith(("http://", "https://")):
            malformed.append((i, line, lines[j] if j < len(lines) else "<EOF>"))
            continue
        a = attrs(line)
        entries.append({
            "start": i, "end": j, "extinf": line, "url": lines[j].strip(),
            "name": (a.get("tvg-name") or display_name(line)).strip(),
            "display": display_name(line), "group": a.get("group-title", "").strip(),
            "logo": a.get("tvg-logo", "").strip(), "attrs": a
        })
    return lines, entries, malformed

def classify_response(status, headers, body, url):
    if status in (404, 410):
        return "dead", f"HTTP {status}"
    if status in (401, 403, 429) or status >= 500:
        return "unknown", f"HTTP {status}; access/availability could not be confirmed"
    if status not in (200, 206):
        return "unknown", f"HTTP {status}; not conclusive"
    content_type = (headers.get("Content-Type") or headers.get("content-type") or "").lower()
    sample = body.lstrip().lower()
    if b"#extm3u" in sample[:2048]:
        return "verified", "HLS playlist response"
    if ".mpd" in url.lower() and b"<mpd" in sample[:4096]:
        return "verified", "DASH manifest response"
    if any(x in content_type for x in ("mpegurl", "mp2t", "video/", "dash+xml")):
        return "verified", f"media content type: {content_type}"
    if len(body) >= 188 and body[0] == 0x47:
        return "verified", "transport-stream data"
    if sample.startswith((b"<!doctype html", b"<html", b"<head", b'{"error"', b'{"message"', b"access denied")):
        return "dead", "HTTP success returned an HTML/error page, not a TV stream"
    return "unknown", "response did not clearly identify a live media stream"

def probe_url(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; BDIX-IPTV-Discovery-Validator/1.0)",
        "Accept": "*/*", "Range": "bytes=0-4095"
    })
    try:
        with urllib.request.urlopen(req, timeout=9) as response:
            body = response.read(4096)
            return classify_response(response.getcode(), response.headers, body, url)
    except urllib.error.HTTPError as exc:
        return classify_response(exc.code, exc.headers or {}, b"", url)
    except (urllib.error.URLError, TimeoutError, socket.timeout, ConnectionError) as exc:
        return "unknown", f"connection could not be confirmed: {type(exc).__name__}"
    except Exception as exc:
        return "unknown", f"probe error: {type(exc).__name__}"

def norm_key(value):
    value = re.sub(r"\b(?:\d{3,4}p|uhd|fhd|hd|sd|4k)\b", " ", str(value or ""), flags=re.I)
    return re.sub(r"[^a-z0-9]+", "", value.casefold())

def local_logo_path(logo):
    if logo.startswith(RAW_BASE):
        rel = urllib.parse.unquote(logo[len(RAW_BASE):])
        return Path("logos") / rel
    if logo.startswith("logos/"):
        return Path(logo)
    return None

def find_logo(name):
    key = norm_key(name)
    if not key or not LOGOS.exists():
        return None
    for path in LOGOS.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg"}:
            if norm_key(path.stem) == key:
                return RAW_BASE + str(path.relative_to(LOGOS)).replace("\\", "/")
    return None

def set_logo(extinf, logo):
    if re.search(r'\btvg-logo="[^"]*"', extinf):
        if logo:
            return re.sub(r'\btvg-logo="[^"]*"', lambda _: f'tvg-logo="{logo}"', extinf, count=1)
        return re.sub(r'\s+tvg-logo="[^"]*"', "", extinf, count=1)
    return extinf

def ensure_local_logo(entry):
    logo = entry["logo"]
    path = local_logo_path(logo)
    if path is not None and path.is_file():
        return entry["extinf"], False, False
    found = find_logo(entry["name"])
    if found:
        return set_logo(entry["extinf"], found), True, False
    if logo:
        return set_logo(entry["extinf"], ""), False, True
    if re.search(r'\btvg-logo=""', entry["extinf"]):
        return set_logo(entry["extinf"], ""), False, True
    return entry["extinf"], False, False

def consolidate_international_country_groups(playlist_path):
    """Reconcile dynamic country groups after stream probes remove dead candidates."""
    p = Path(playlist_path)
    prefix, blocks = discovery.parse(p.read_text(encoding="utf-8-sig"))
    labels = {
        discovery.country_group(code).casefold(): code
        for code in discovery.ISO_CODES
        if code not in {"BD", "IN", "PK"}
    }
    dynamic_codes = set(labels.values())
    identities = defaultdict(set)

    # Country-group labels are authoritative for rows already in those groups.
    # New Channels rows count only when country metadata is independently known.
    for block in blocks:
        a = discovery.attrs(block[0])
        group_key = (a.get("group-title") or "").strip().casefold()
        if group_key in labels:
            code = labels[group_key]
        elif group_key == "new channels":
            code = discovery.country_code(a)
        else:
            continue
        if code not in dynamic_codes:
            continue
        identity = (a.get("tvg-id") or a.get("channel-id") or discovery.norm(discovery.name_of(block))).strip().casefold()
        if identity:
            identities[code].add(identity)

    qualified = {
        code for code, channel_ids in identities.items()
        if len(channel_ids) >= discovery.COUNTRY_THRESHOLD
    }
    changes = []
    for block in blocks:
        a = discovery.attrs(block[0])
        old = (a.get("group-title") or "").strip()
        old_key = old.casefold()
        target = None
        if old_key in labels:
            code = labels[old_key]
            if code not in qualified:
                target = "New Channels"
        elif old_key == "new channels":
            code = discovery.country_code(a)
            if code in qualified:
                target = discovery.country_group(code)
        if target and target != old:
            block[0] = discovery.set_attr(block[0], "group-title", target)
            changes.append((discovery.name_of(block), old, target))

    if not changes:
        return []

    present_groups = {discovery.attrs(block[0]).get("group-title", "").strip() for block in blocks}
    registry = discovery.category_registry(present_groups)
    rank = {group.casefold(): index for index, group in enumerate(registry)}
    blocks.sort(key=lambda block: (
        rank.get(discovery.attrs(block[0]).get("group-title", "").strip().casefold(), len(rank)),
        discovery.natural_key(discovery.name_of(block)),
        discovery.url_of(block).casefold(),
    ))
    preamble = [line for line in prefix if not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    header = "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry, ensure_ascii=False)
    index = next((i + 1 for i, line in enumerate(preamble) if line.startswith("#EXTM3U")), 0)
    preamble.insert(index, header)
    output = preamble[:]
    for block in blocks:
        output.extend(block)
    p.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    return changes


def append_section(report_path, heading, body):
    p = Path(report_path)
    original = p.read_text(encoding="utf-8") if p.exists() else "# Discovery report\n"
    if heading == "Stream verification":
        original = re.split(r"\n## (?:Stream verification|Final validation)\b", original, maxsplit=1)[0].rstrip()
    else:
        original = re.split(rf"\n## {re.escape(heading)}\b", original, maxsplit=1)[0].rstrip()
    p.write_text(original + "\n\n## " + heading + "\n\n" + body.rstrip() + "\n", encoding="utf-8")

def probe_mode(playlist, report, baseline, mode):
    p = Path(playlist)
    bp = Path(baseline)
    if not p.exists() or not bp.exists():
        raise SystemExit("Playlist or baseline snapshot is missing; no changes made.")
    text = p.read_text(encoding="utf-8-sig")
    before = bp.read_text(encoding="utf-8-sig")
    lines, entries, malformed = parse_playlist(text)
    _, before_entries, before_malformed = parse_playlist(before)
    if malformed or before_malformed:
        append_section(report, "Stream verification", f"- Run timestamp: {now()}\n- BLOCKER: malformed EXTINF/URL pairs detected before stream verification; playlist left unchanged.")
        raise SystemExit(1)
    baseline_urls = {e["url"].casefold() for e in before_entries}
    queues = {"new channels", "new backup", "new backups"}
    targets = [e for e in entries if e["group"].casefold() in queues or e["url"].casefold() not in baseline_urls]
    counts = Counter()
    details = []
    remove_starts = set()
    update_lines = {}
    seen = set()
    for e in entries:
        urlkey = e["url"].casefold()
        if urlkey in seen and (urlkey not in baseline_urls or e["group"].casefold() in queues):
            remove_starts.add(e["start"])
            counts["duplicate discovery entries removed"] += 1
            details.append(f"- Removed duplicate discovery entry {e['name']} — duplicate stream URL.")
        seen.add(urlkey)
    probe_targets = [e for e in targets if e["start"] not in remove_starts]
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(probe_url, e["url"]): e for e in probe_targets}
        for future in concurrent.futures.as_completed(futures):
            e = futures[future]
            results[e["start"]] = future.result()
    for e in probe_targets:
        status, reason = results[e["start"]]
        counts[f"stream status: {status}"] += 1
        group_key = e["group"].casefold()
        is_backup = group_key in {"new backup", "new backups"}
        if status == "dead" or (is_backup and status != "verified"):
            remove_starts.add(e["start"])
            why = reason if status == "dead" else f"backup stream not verified ({reason})"
            details.append(f"- Removed {e['name']} from {e['group']} — {why}.")
            counts["removed invalid/dead or unverified backup entries"] += 1
            continue
        if status == "verified":
            counts["verified streams"] += 1
        else:
            counts["primary streams retained as unverified"] += 1
            details.append(f"- Retained {e['name']} for review — stream could not be conclusively verified ({reason}).")
        new_extinf, localized, cleared = ensure_local_logo(e)
        if new_extinf != e["extinf"]:
            update_lines[e["start"]] = new_extinf
        if localized:
            counts["logos localized to repository assets"] += 1
        if cleared:
            counts["external/missing-asset logo references cleared"] += 1
    remove_indices = set()
    by_start = {e["start"]: e for e in entries}
    for start in remove_starts:
        e = by_start[start]
        remove_indices.update(range(e["start"], e["end"] + 1))
    new_lines = [update_lines.get(i, line) for i, line in enumerate(lines) if i not in remove_indices]
    p.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")
    if mode == "international":
        consolidated = consolidate_international_country_groups(p)
        counts["country-group rows consolidated after stream probing"] += len(consolidated)
        details.extend(
            f"- Moved {name} from {old_group} to {new_group} after stream-probe removals and the five-channel threshold check."
            for name, old_group, new_group in consolidated
        )
    report_body = [
        f"- Run timestamp: {now()}",
        f"- Mode: {mode}",
        f"- New entries and discovery queues probed: {len(probe_targets)}",
        f"- Verified live media responses: {counts['verified streams']}",
        f"- Primary entries retained but not conclusively verified: {counts['primary streams retained as unverified']}",
        f"- Dead/invalid entries and unverified backups removed: {counts['removed invalid/dead or unverified backup entries']}",
        f"- Duplicate discovery entries removed: {counts['duplicate discovery entries removed']}",
        f"- Country-group rows consolidated after stream probing: {counts['country-group rows consolidated after stream probing']}",
        f"- Logo references localized to authentic repository assets: {counts['logos localized to repository assets']}",
        f"- Logo references cleared because no authentic local asset was found: {counts['external/missing-asset logo references cleared']}",
        "",
        "### Stream probe details",
        *(details[:100] if details else ["- No stream removals or uncertain responses to report."]),
    ]
    append_section(report, "Stream verification", "\n".join(report_body))

def final_mode(playlist, report, baseline, mode):
    p = Path(playlist)
    bp = Path(baseline)
    if not p.exists() or not bp.exists():
        raise SystemExit("Playlist or baseline snapshot is missing.")
    text = p.read_text(encoding="utf-8-sig")
    before = bp.read_text(encoding="utf-8-sig")
    lines, entries, malformed = parse_playlist(text)
    _, before_entries, _ = parse_playlist(before)
    baseline_urls = {e["url"].casefold() for e in before_entries}
    groups = []
    for e in entries:
        if e["group"] and e["group"] not in groups:
            groups.append(e["group"])
    queue_names = {"new channels", "new backup", "new backups"}
    candidates = [e for e in entries if e["group"].casefold() in queue_names or e["url"].casefold() not in baseline_urls]
    url_counts = Counter(e["url"].casefold() for e in entries)
    duplicate_count = sum(n - 1 for n in url_counts.values() if n > 1)
    errors = []
    validator_outcome = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME", "success").casefold()
    if validator_outcome != "success":
        errors.append(f"official validator result: {validator_outcome}")
    if malformed:
        errors.append(f"{len(malformed)} malformed EXTINF/URL pairs")
    if duplicate_count:
        errors.append(f"{duplicate_count} duplicate stream URLs remain")
    required = ["New Channels", "New Backup", "Backup"]
    ordering_ok = groups[-3:] == required
    if not ordering_ok:
        errors.append("New Channels/New Backup/Backup must be the final three playlist groups")
    missing_logo = 0
    external_logo = 0
    policy_issues = []
    for e in candidates:
        logo = e["logo"]
        if not logo:
            missing_logo += 1
        else:
            path = local_logo_path(logo)
            if path is None or not path.is_file():
                external_logo += 1
                errors.append(f"non-local logo reference for {e['name']}")
        attrs = e["attrs"]
        country = (attrs.get("tvg-country") or "").upper()
        if not country:
            for ident in (attrs.get("tvg-id", ""), attrs.get("channel-id", "")):
                m = re.search(r"\.([a-z]{2})(?:@|$)", ident, re.I)
                if m:
                    country = m.group(1).upper()
                    break
        if mode == "iptv" and country == "IN":
            text_value = " ".join((e["name"], e["group"], attrs.get("tvg-id", ""), attrs.get("channel-id", "")))
            if NEWS_RE.search(text_value):
                policy_issues.append(f"Indian news: {e['name']}")
            if RELIGIOUS_RE.search(text_value) and not ISLAMIC_RE.search(text_value):
                policy_issues.append(f"non-Islamic religious: {e['name']}")
        elif mode == "international" and not FASHION_RE.search(e["name"]):
            text_value = " ".join((e["name"], e["group"], attrs.get("tvg-content", "")))
            content = attrs.get("tvg-content", "").strip().casefold()
            if INTL_BAD_RE.search(text_value):
                policy_issues.append(f"out-of-scope content: {e['name']}")
            if content and content not in {"movie", "movies", "film", "films", "music", "musics"}:
                policy_issues.append(f"non-Movie/Music tvg-content: {e['name']}")
    if policy_issues:
        errors.extend(policy_issues)
    status = "PASS" if not errors else "FAIL"
    body = [
        f"- Run timestamp: {now()}",
        f"- Validation status: {status}",
        f"- M3U entries parsed: {len(entries)}",
        f"- Malformed EXTINF/URL pairs: {len(malformed)}",
        f"- Duplicate stream URLs: {duplicate_count}",
        f"- New Channels/New Backup/Backup ordering: {'passed' if ordering_ok else 'failed'}",
        f"- Discovery entries missing a logo (left blank rather than using a placeholder): {missing_logo}",
        f"- Non-local discovery logo references: {external_logo}",
        f"- Geography/content policy issues: {len(policy_issues)}",
        "- Existing non-discovery entries were not removed by the stream-validation step.",
    ]
    if errors:
        body += ["", "### Blockers", *(f"- {e}" for e in errors[:100])]
    append_section(report, "Final validation", "\n".join(body))
    print("\n".join(body))

def main():
    if len(sys.argv) != 6 or sys.argv[1] not in {"probe", "finalize"}:
        raise SystemExit("Usage: validate_discovery_run.py <probe|finalize> <playlist> <report> <baseline> <iptv|international>")
    action, playlist, report, baseline, mode = sys.argv[1:]
    if mode not in {"iptv", "international"}:
        raise SystemExit("Mode must be iptv or international.")
    if action == "probe":
        probe_mode(playlist, report, baseline, mode)
    else:
        final_mode(playlist, report, baseline, mode)

if __name__ == "__main__":
    main()
