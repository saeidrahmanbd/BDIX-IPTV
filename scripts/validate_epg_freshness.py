#!/usr/bin/env python3
"""Reject stale or malformed XMLTV guides before publishing them."""
import argparse
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

UTC = timezone.utc
TIMESTAMP_RE = re.compile(r"^(\d{14})(?:\s*([+-]\d{4}))?$")


def parse_xmltv_time(value):
    """Parse XMLTV time values, defaulting timezone-less values to UTC."""
    match = TIMESTAMP_RE.fullmatch((value or "").strip())
    if not match:
        return None
    base, offset = match.groups()
    try:
        if offset:
            return datetime.strptime(f"{base} {offset}", "%Y%m%d%H%M%S %z").astimezone(UTC)
        return datetime.strptime(base, "%Y%m%d%H%M%S").replace(tzinfo=UTC)
    except ValueError:
        return None


def validate(path, now=None, min_window_ratio=0.70, min_window_programmes=1000, min_window_channels=50):
    """Return a report and a list of blocking errors."""
    path = Path(path)
    now = now or datetime.now(UTC)
    if now.tzinfo is None:
        now = now.replace(tzinfo=UTC)
    now = now.astimezone(UTC)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)

    total = 0
    valid = 0
    window_programmes = 0
    current_programmes = 0
    invalid_intervals = 0
    missing_titles = 0
    window_channels = set()
    current_channels = set()

    try:
        for _, elem in ET.iterparse(path, events=("end",)):
            if elem.tag != "programme":
                continue
            total += 1
            channel_id = (elem.attrib.get("channel") or "").strip()
            title = next(
                ((item.text or "").strip() for item in elem.findall("title") if (item.text or "").strip()),
                "",
            )
            start = parse_xmltv_time(elem.attrib.get("start", ""))
            stop = parse_xmltv_time(elem.attrib.get("stop", ""))

            if not title:
                missing_titles += 1
            if start is None or stop is None or stop <= start:
                invalid_intervals += 1
            elif title:
                valid += 1
                if start <= upper and stop >= lower:
                    window_programmes += 1
                    if channel_id:
                        window_channels.add(channel_id)
                if start <= now < stop and channel_id:
                    current_programmes += 1
                    current_channels.add(channel_id)
            elem.clear()
    except (OSError, ET.ParseError) as exc:
        return {}, [f"Could not parse XMLTV guide {path}: {exc}"]

    ratio = window_programmes / valid if valid else 0.0
    metrics = {
        "checked_at_utc": now.isoformat(timespec="seconds"),
        "window_start_utc": lower.isoformat(timespec="seconds"),
        "window_end_utc": upper.isoformat(timespec="seconds"),
        "programme_elements": total,
        "valid_titled_programmes": valid,
        "programmes_in_window": window_programmes,
        "window_ratio": ratio,
        "channels_with_window_programmes": len(window_channels),
        "programmes_airing_now": current_programmes,
        "channels_airing_now": len(current_channels),
        "invalid_intervals": invalid_intervals,
        "missing_titles": missing_titles,
    }

    errors = []
    if total == 0:
        errors.append("XMLTV has no <programme> entries.")
    if missing_titles:
        errors.append(f"{missing_titles} programme entries have no non-empty title.")
    if invalid_intervals:
        errors.append(f"{invalid_intervals} programme entries have invalid start/stop intervals.")
    if window_programmes < min_window_programmes:
        errors.append(
            f"Only {window_programmes} programmes overlap the current guide window; "
            f"minimum is {min_window_programmes}."
        )
    if len(window_channels) < min_window_channels:
        errors.append(
            f"Only {len(window_channels)} channel IDs have programmes in the current guide window; "
            f"minimum is {min_window_channels}."
        )
    if ratio < min_window_ratio:
        errors.append(
            f"Only {ratio:.1%} of valid programme rows overlap the current guide window; "
            f"minimum is {min_window_ratio:.1%}. The guide may be stale."
        )
    return metrics, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("guide", nargs="?", default="epg/epg.xml")
    parser.add_argument("--report", default="reports/epg-publish-freshness.md")
    parser.add_argument("--min-window-ratio", type=float, default=0.70)
    parser.add_argument("--min-window-programmes", type=int, default=1000)
    parser.add_argument("--min-window-channels", type=int, default=50)
    args = parser.parse_args()

    metrics, errors = validate(
        args.guide,
        min_window_ratio=args.min_window_ratio,
        min_window_programmes=args.min_window_programmes,
        min_window_channels=args.min_window_channels,
    )
    if not metrics:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)

    ratio = metrics["window_ratio"]
    lines = [
        "# EPG Publish Freshness Check",
        "",
        f"Checked: **{metrics['checked_at_utc']}**",
        f"Guide path: {args.guide}",
        "",
        f"- Valid titled programmes: **{metrics['valid_titled_programmes']}**",
        f"- Programmes in current window: **{metrics['programmes_in_window']} ({ratio:.1%})**",
        f"- Channel IDs with programmes in current window: **{metrics['channels_with_window_programmes']}**",
        f"- Programmes airing at check time: **{metrics['programmes_airing_now']}** across **{metrics['channels_airing_now']}** channel IDs",
        f"- Window: **{metrics['window_start_utc']}** to **{metrics['window_end_utc']}**",
        f"- Invalid programme intervals: **{metrics['invalid_intervals']}**",
        f"- Missing programme titles: **{metrics['missing_titles']}**",
        "",
        "Thresholds: at least 70% of valid programmes must overlap the current window, "
        "with at least 1,000 in-window programmes across at least 50 channel IDs.",
        "",
        f"Status: **{'FAIL' if errors else 'PASS'}**",
        "",
    ]
    if errors:
        lines += ["## Blocking reasons", ""] + [f"- {error}" for error in errors] + [""]
    else:
        lines += ["The guide contains substantial current/future schedule data and is eligible for publication.", ""]

    report = Path(args.report)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
