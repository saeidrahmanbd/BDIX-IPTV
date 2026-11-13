"""Apply only explicitly approved EPG aliases to an in-memory XMLTV candidate."""
from __future__ import annotations
from dataclasses import dataclass
import copy
import xml.etree.ElementTree as ET
from automation.core.playlist_contract import parse_rows, ATTR_RE
from automation.engines.epg.validator import validate_xmltv

@dataclass(frozen=True)
class ApprovedAlias:
    source_id: str
    target_id: str
    evidence: str
    approved: bool = False

def apply_approved_aliases(playlist_text: str, baseline_xml: str,
                           aliases: list[ApprovedAlias]) -> str:
    """Clone source channel/schedules to active playlist IDs after explicit approval; never writes files."""
    validation = validate_xmltv(baseline_xml)
    if not validation.valid:
        raise ValueError("baseline XMLTV failed validation: " + "; ".join(validation.errors[:5]))
    active_ids = {
        attrs.get("tvg-id","").strip()
        for row in parse_rows(playlist_text)
        for attrs in [dict(ATTR_RE.findall(row.extinf))]
        if attrs.get("tvg-id","").strip()
    }
    if not active_ids:
        raise ValueError("playlist has no active tvg-id values")
    root = ET.fromstring(baseline_xml)
    channels = {(node.get("id") or "").strip():node for node in root.findall("channel")}
    programmes: dict[str,list[ET.Element]] = {}
    for programme in root.findall("programme"):
        programmes.setdefault((programme.get("channel") or "").strip(),[]).append(programme)

    targets: set[str] = set()
    sources: set[str] = set()
    for alias in aliases:
        source, target = alias.source_id.strip(), alias.target_id.strip()
        if not alias.approved or not alias.evidence.strip():
            raise ValueError("EPG alias requires explicit approval and evidence")
        if not source or not target or source == target:
            raise ValueError("EPG alias source and target must be distinct non-empty IDs")
        if source not in channels:
            raise ValueError(f"EPG alias source channel does not exist: {source}")
        if target not in active_ids:
            raise ValueError(f"EPG alias target is not active in the playlist: {target}")
        if target in channels or target in targets:
            raise ValueError(f"EPG alias target already exists or is duplicated: {target}")
        if source in sources:
            raise ValueError(f"EPG alias source is duplicated: {source}")
        if not programmes.get(source):
            raise ValueError(f"EPG alias source has no programmes: {source}")
        targets.add(target)
        sources.add(source)

    for alias in aliases:
        source, target = alias.source_id.strip(), alias.target_id.strip()
        channel_copy = copy.deepcopy(channels[source])
        channel_copy.set("id",target)
        root.append(channel_copy)
        for programme in programmes[source]:
            programme_copy = copy.deepcopy(programme)
            programme_copy.set("channel",target)
            root.append(programme_copy)

    return ET.tostring(root,encoding="unicode")
