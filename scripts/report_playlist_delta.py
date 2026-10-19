#!/usr/bin/env python3
"""Report exact playlist additions/removals without conflating identity rewrites with new streams."""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT_DIR = Path("reports")
REVIEW_GROUPS = {"Backup", "Not Playing"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
SENSITIVE_QUERY = re.compile(r"(?:token|auth|key|sig|signature|pass|password|passwd|user|username|session|credential|jwt|secret)", re.I)


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(info))


def parse(text: str) -> list[dict[str, str]]:
    """Read EXTINF/URL pairs while tolerating VLC/HLS option lines between them."""
    records: list[dict[str, str]] = []
    info: str | None = None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF"):
            if info is not None:
                records.append({"info": info, "url": ""})
            info = line
        elif info is not None and line.strip().lower().startswith(("http://", "https://")):
            records.append({"info": info, "url": line.strip()})
            info = None
    if info is not None:
        records.append({"info": info, "url": ""})
    return [r for r in records if r["url"]]


def ident(info: str) -> str:
    a = attrs(info)
    return (a.get("tvg-id") or a.get("channel-id") or "").strip().lower()


def name(info: str) -> str:
    a = attrs(info)
    return (a.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()


def group(info: str) -> str:
    return attrs(info).get("group-title", "").strip()


def redact_url(raw: str) -> str:
    try:
        p = urlsplit(raw)
        query = [(k, "[REDACTED]" if SENSITIVE_QUERY.search(k) else v) for k, v in parse_qsl(p.query, keep_blank_values=True)]
        path = re.sub(r"(/(?:live|hls|stream|play)/)[^/]+/[^/]+(?=/|$)", r"\1[REDACTED]/[REDACTED]", p.path, flags=re.I)
        return urlunsplit((p.scheme, p.netloc, path, urlencode(query), p.fragment))
    except Exception:
        return raw.split("?", 1)[0]


def safe_show(value: str) -> str:
    return (value or "").replace("\n", " ").replace("\r", " ").strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("pre-restore", "final"), default="final")
    args = parser.parse_args()

    if not PLAYLIST.is_file():
        raise SystemExit(f"Missing {PLAYLIST}")
    try:
        old_text = subprocess.check_output(["git", "show", "HEAD:IPTV-Playlist.m3u"], text=True, encoding="utf-8")
    except Exception as exc:
        raise SystemExit(f"Cannot read baseline IPTV-Playlist.m3u from HEAD: {exc}")

    old = parse(old_text)
    new = parse(PLAYLIST.read_text(encoding="utf-8-sig", errors="replace"))
    old_by_url: dict[str, list[dict[str, str]]] = defaultdict(list)
    new_by_url: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in old:
        old_by_url[r["url"].strip().casefold()].append(r)
    for r in new:
        new_by_url[r["url"].strip().casefold()].append(r)
    old_urls, new_urls = set(old_by_url), set(new_by_url)
    url_added, url_removed = new_urls - old_urls, old_urls - new_urls

    # Match the legacy guard's identity+URL key semantics for reconciliation.
    old_keys = {(ident(r["info"]), r["url"].strip()) for r in old if r["url"].strip()}
    new_keys = {(ident(r["info"]), r["url"].strip()) for r in new if r["url"].strip()}
    key_added, key_removed = new_keys - old_keys, old_keys - new_keys
    identity_rekey_urls = {
        u for u in (old_urls & new_urls)
        if {ident(x["info"]) for x in old_by_url[u]} != {ident(x["info"]) for x in new_by_url[u]}
    }

    out_name = "maintenance-change-review" + ("-pre-restore" if args.stage == "pre-restore" else "")
    csv_path = REPORT_DIR / f"{out_name}.csv"
    summary_path = REPORT_DIR / f"{out_name}-summary.md"
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    fields = [
        "change_side", "reason", "channel_name", "group", "identity_key", "url_redacted",
        "old_name", "old_group", "old_identity", "new_name", "new_group", "new_identity",
    ]
    rows: list[dict[str, str]] = []

    def record_for(index: dict[str, list[dict[str, str]]], url_key: str) -> dict[str, str] | None:
        return index[url_key][0] if index.get(url_key) else None

    def make_row(side: str, key_id: str, url_raw: str, old_rec: dict[str, str] | None, new_rec: dict[str, str] | None) -> dict[str, str]:
        old_info = old_rec["info"] if old_rec else ""
        new_info = new_rec["info"] if new_rec else ""
        url_key = url_raw.strip().casefold()
        if url_key in old_urls and url_key in new_urls:
            reason = "identity key replaced on an existing stream URL; not a new/deleted stream"
        elif side == "key_added":
            target_groups = {group(x["info"]) for x in new_by_url.get(url_key, [])}
            reason = "new stream URL in a review queue" if target_groups and target_groups.issubset(REVIEW_GROUPS) else "new stream URL"
        else:
            old_groups = {group(x["info"]) for x in old_by_url.get(url_key, [])}
            reason = "review-queue stream URL disappeared" if old_groups and old_groups.issubset(REVIEW_GROUPS) else "stream URL disappeared"
        chosen = new_info or old_info
        return {
            "change_side": side,
            "reason": reason,
            "channel_name": safe_show(name(chosen)),
            "group": safe_show(group(chosen)),
            "identity_key": safe_show(key_id),
            "url_redacted": redact_url(url_raw),
            "old_name": safe_show(name(old_info)) if old_info else "",
            "old_group": safe_show(group(old_info)) if old_info else "",
            "old_identity": safe_show(ident(old_info)) if old_info else "",
            "new_name": safe_show(name(new_info)) if new_info else "",
            "new_group": safe_show(group(new_info)) if new_info else "",
            "new_identity": safe_show(ident(new_info)) if new_info else "",
        }

    for cid, url in sorted(key_added, key=lambda x: (x[1].casefold(), x[0])):
        u = url.casefold()
        rows.append(make_row("key_added", cid, url, record_for(old_by_url, u), record_for(new_by_url, u)))
    for cid, url in sorted(key_removed, key=lambda x: (x[1].casefold(), x[0])):
        u = url.casefold()
        rows.append(make_row("key_removed", cid, url, record_for(old_by_url, u), record_for(new_by_url, u)))

    # Also list URL-level change rows explicitly so genuinely removed streams are separable.
    for u in sorted(url_added):
        rec = record_for(new_by_url, u)
        rows.append(make_row("stream_url_added", ident(rec["info"]) if rec else "", rec["url"] if rec else u, record_for(old_by_url, u), rec))
    for u in sorted(url_removed):
        rec = record_for(old_by_url, u)
        rows.append(make_row("stream_url_removed", ident(rec["info"]) if rec else "", rec["url"] if rec else u, rec, record_for(new_by_url, u)))

    with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    active_removed = sum(
        1 for u in url_removed
        if (record_for(old_by_url, u) is not None and group(record_for(old_by_url, u)["info"]) not in REVIEW_GROUPS)
    )
    review_removed = len(url_removed) - active_removed
    summary = [
        "# Playlist Change Review",
        "",
        f"- Stage: **{args.stage}**",
        f"- Baseline parsed entries: **{len(old)}**",
        f"- Current parsed entries: **{len(new)}**",
        f"- Legacy identity+URL key additions: **{len(key_added)}**",
        f"- Legacy identity+URL key removals: **{len(key_removed)}**",
        f"- Actual new stream URLs: **{len(url_added)}**",
        f"- Actual missing stream URLs: **{len(url_removed)}**",
        f"- Missing active-primary stream URLs: **{active_removed}**",
        f"- Missing Backup/Not Playing stream URLs: **{review_removed}**",
        f"- Existing URLs with changed identity key: **{len(identity_rekey_urls)}**",
        f"- Note: key-level additions/removals on a persistent URL are metadata/identity rewrites, not new or deleted streams.",
        "",
        "See the CSV for per-entry old/new names, groups, identities and redacted URLs.",
    ]
    summary_path.write_text("\n".join(summary) + "\n", encoding="utf-8")
    print(
        f"Change review ({args.stage}): key_added={len(key_added)} key_removed={len(key_removed)} "
        f"url_added={len(url_added)} url_removed={len(url_removed)} identity_rekey_urls={len(identity_rekey_urls)}"
    )
    print(f"Detailed review saved: {csv_path}")
    print(f"Summary saved: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
