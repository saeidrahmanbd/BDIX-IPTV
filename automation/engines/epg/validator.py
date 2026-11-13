"""Read-only XMLTV candidate validation; no file publication or network access."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import re
import xml.etree.ElementTree as ET

OFFSET_RE = re.compile(r"^([+-])([0-9]{2})([0-9]{2})$")

@dataclass(frozen=True)
class EpgValidation:
    valid: bool
    channel_count: int
    programme_count: int
    errors: tuple[str, ...]

def _timestamp(value: str) -> datetime:
    raw = value.strip()
    core = raw[:14]
    if len(core) != 14 or not core.isdigit():
        raise ValueError("invalid XMLTV timestamp")
    parsed = datetime.strptime(core, "%Y%m%d%H%M%S")
    suffix = raw[14:].strip()
    if suffix:
        match = OFFSET_RE.fullmatch(suffix)
        if not match:
            raise ValueError("invalid XMLTV timezone offset")
        hours, minutes = int(match.group(2)), int(match.group(3))
        if hours > 23 or minutes > 59:
            raise ValueError("invalid XMLTV timezone offset")
        sign = 1 if match.group(1) == "+" else -1
        parsed = parsed.replace(tzinfo=timezone(timedelta(hours=hours, minutes=minutes) * sign))
    else:
        parsed = parsed.replace(tzinfo=ZoneInfo("Asia/Dhaka"))
    return parsed.astimezone(timezone.utc)

def validate_xmltv(xml_text: str) -> EpgValidation:
    errors: list[str] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        return EpgValidation(False,0,0,(f"malformed XML: {exc}",))
    if root.tag != "tv":
        errors.append("XMLTV root element must be <tv>")
    channel_ids: set[str] = set()
    for channel in root.findall("channel"):
        channel_id = (channel.get("id") or "").strip()
        if not channel_id:
            errors.append("channel without id")
        elif channel_id in channel_ids:
            errors.append(f"duplicate channel id: {channel_id}")
        channel_ids.add(channel_id)
    programme_count = 0
    for programme in root.findall("programme"):
        programme_count += 1
        channel_id = (programme.get("channel") or "").strip()
        if not channel_id or channel_id not in channel_ids:
            errors.append(f"programme references unknown channel: {channel_id or '<missing>'}")
        try:
            start = _timestamp(programme.get("start") or "")
            stop = _timestamp(programme.get("stop") or "")
            if stop <= start:
                errors.append(f"programme stop is not after start for channel: {channel_id}")
        except ValueError as exc:
            errors.append(f"programme has invalid timestamp for channel {channel_id}: {exc}")
    if not channel_ids:
        errors.append("XMLTV contains no channels")
    if programme_count == 0:
        errors.append("XMLTV contains no programmes")
    return EpgValidation(not errors,len(channel_ids),programme_count,tuple(errors))

if __name__ == "__main__":
    raise SystemExit(0)
