"""Read-only XMLTV candidate validation; no file publication or network access."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
import xml.etree.ElementTree as ET

@dataclass(frozen=True)
class EpgValidation:
    valid: bool
    channel_count: int
    programme_count: int
    errors: tuple[str, ...]

def _timestamp(value: str) -> datetime:
    # XMLTV timestamps commonly use YYYYMMDDhhmmss with an optional timezone suffix.
    core = value.strip()[:14]
    if len(core) != 14 or not core.isdigit():
        raise ValueError("invalid XMLTV timestamp")
    return datetime.strptime(core, "%Y%m%d%H%M%S")

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
        except ValueError:
            errors.append(f"programme has invalid start/stop timestamp for channel: {channel_id}")
    if not channel_ids:
        errors.append("XMLTV contains no channels")
    if programme_count == 0:
        errors.append("XMLTV contains no programmes")
    return EpgValidation(not errors,len(channel_ids),programme_count,tuple(errors))
