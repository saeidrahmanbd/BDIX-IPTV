"""Evaluate whether active channels have current or future XMLTV programmes."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import re
import xml.etree.ElementTree as ET
from automation.core.playlist_contract import parse_rows, ATTR_RE
from automation.engines.epg.validator import validate_xmltv

OFFSET_RE = re.compile(r"^([+-])(\d{2})(\d{2})$")

@dataclass(frozen=True)
class EpgFreshness:
    active_channel_ids: int
    fresh_scheduled_channel_ids: tuple[str, ...]
    stale_only_channel_ids: tuple[str, ...]
    no_schedule_channel_ids: tuple[str, ...]
    future_programme_count: int
    latest_programme_stop_utc: datetime | None

@dataclass(frozen=True)
class EpgFreshnessComparison:
    accepted: bool
    baseline: EpgFreshness
    candidate: EpgFreshness
    reasons: tuple[str, ...]

def _parse_xmltv_datetime(value: str) -> datetime:
    raw = value.strip()
    core = raw[:14]
    if len(core) != 14 or not core.isdigit():
        raise ValueError("invalid XMLTV timestamp")
    parsed = datetime.strptime(core,"%Y%m%d%H%M%S")
    suffix = raw[14:].strip()
    if suffix:
        match = OFFSET_RE.fullmatch(suffix)
        if not match:
            raise ValueError("invalid XMLTV timezone offset")
        hours, minutes = int(match.group(2)), int(match.group(3))
        if hours > 23 or minutes > 59:
            raise ValueError("invalid XMLTV timezone offset")
        sign = 1 if match.group(1) == "+" else -1
        offset = timedelta(hours=hours,minutes=minutes) * sign
        parsed = parsed.replace(tzinfo=timezone(offset))
    else:
        parsed = parsed.replace(tzinfo=ZoneInfo("Asia/Dhaka"))
    return parsed.astimezone(timezone.utc)

def calculate_freshness(playlist_text: str, xmltv_text: str,
                         as_of: datetime | None = None) -> EpgFreshness:
    validation = validate_xmltv(xmltv_text)
    if not validation.valid:
        raise ValueError("XMLTV failed validation: " + "; ".join(validation.errors[:5]))
    if as_of is None:
        as_of = datetime.now(ZoneInfo("Asia/Dhaka"))
    if as_of.tzinfo is None:
        raise ValueError("as_of must be timezone-aware")
    as_of_utc = as_of.astimezone(timezone.utc)
    active_ids = {
        attrs.get("tvg-id","").strip()
        for row in parse_rows(playlist_text)
        for attrs in [dict(ATTR_RE.findall(row.extinf))]
        if attrs.get("tvg-id","").strip()
    }
    if not active_ids:
        raise ValueError("playlist contains no active tvg-id values")
    root = ET.fromstring(xmltv_text)
    scheduled: dict[str,list[datetime]] = {}
    future_programmes = 0
    latest_stop: datetime | None = None
    for programme in root.findall("programme"):
        channel = (programme.get("channel") or "").strip()
        stop = _parse_xmltv_datetime(programme.get("stop") or "")
        scheduled.setdefault(channel,[]).append(stop)
        if latest_stop is None or stop > latest_stop:
            latest_stop = stop
        if stop > as_of_utc:
            future_programmes += 1
    fresh_ids = {channel for channel, stops in scheduled.items() if channel in active_ids and any(stop > as_of_utc for stop in stops)}
    stale_ids = {channel for channel, stops in scheduled.items() if channel in active_ids and stops and all(stop <= as_of_utc for stop in stops)}
    all_scheduled_ids = set(scheduled) & active_ids
    no_schedule = active_ids - all_scheduled_ids
    return EpgFreshness(
        len(active_ids),tuple(sorted(fresh_ids)),tuple(sorted(stale_ids)),
        tuple(sorted(no_schedule)),future_programmes,latest_stop,
    )

def compare_freshness(playlist_text: str, baseline_xml: str, candidate_xml: str,
                      as_of: datetime | None = None) -> EpgFreshnessComparison:
    baseline = calculate_freshness(playlist_text,baseline_xml,as_of)
    candidate = calculate_freshness(playlist_text,candidate_xml,as_of)
    lost = set(baseline.fresh_scheduled_channel_ids) - set(candidate.fresh_scheduled_channel_ids)
    reasons = ("current/future schedules lost for active channels: " + ", ".join(sorted(lost)),) if lost else ()
    return EpgFreshnessComparison(not reasons,baseline,candidate,reasons)
