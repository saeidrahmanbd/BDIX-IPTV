"""Measure XMLTV channel mapping and schedule coverage against an active M3U playlist."""
from __future__ import annotations
from dataclasses import dataclass
import xml.etree.ElementTree as ET
from automation.core.playlist_contract import parse_rows, ATTR_RE
from automation.engines.epg.validator import validate_xmltv

@dataclass(frozen=True)
class EpgCoverage:
    active_channel_ids: int
    mapped_channel_ids: int
    scheduled_channel_ids: int
    unmapped_ids: tuple[str, ...]
    mapped_without_schedule: tuple[str, ...]
    mapped_ids: tuple[str, ...]
    scheduled_ids: tuple[str, ...]

@dataclass(frozen=True)
class EpgCoverageComparison:
    accepted: bool
    baseline: EpgCoverage
    candidate: EpgCoverage
    reasons: tuple[str, ...]

def calculate_coverage(playlist_text: str, xmltv_text: str) -> EpgCoverage:
    validation = validate_xmltv(xmltv_text)
    if not validation.valid:
        raise ValueError("XMLTV failed validation: " + "; ".join(validation.errors[:5]))
    active_ids = {
        attrs.get("tvg-id", "").strip()
        for row in parse_rows(playlist_text)
        for attrs in [dict(ATTR_RE.findall(row.extinf))]
        if attrs.get("tvg-id", "").strip()
    }
    if not active_ids:
        raise ValueError("playlist contains no active tvg-id values")
    root = ET.fromstring(xmltv_text)
    epg_ids = {(node.get("id") or "").strip() for node in root.findall("channel")}
    epg_ids.discard("")
    scheduled_ids = {(node.get("channel") or "").strip() for node in root.findall("programme")}
    scheduled_ids.discard("")
    mapped = active_ids & epg_ids
    scheduled = active_ids & scheduled_ids
    return EpgCoverage(
        len(active_ids),len(mapped),len(scheduled),
        tuple(sorted(active_ids - epg_ids)),
        tuple(sorted(mapped - scheduled)),
        tuple(sorted(mapped)),
        tuple(sorted(scheduled)),
    )

def compare_coverage(playlist_text: str, baseline_xml: str, candidate_xml: str) -> EpgCoverageComparison:
    baseline = calculate_coverage(playlist_text,baseline_xml)
    candidate = calculate_coverage(playlist_text,candidate_xml)
    reasons: list[str] = []
    if candidate.mapped_channel_ids < baseline.mapped_channel_ids:
        reasons.append("mapped channel coverage regressed")
    if candidate.mapped_channel_ids < baseline.mapped_channel_ids:
        reasons.append("mapped channel coverage regressed")
    if candidate.scheduled_channel_ids < baseline.scheduled_channel_ids:
        reasons.append("programme schedule coverage regressed")
    lost_mapped = set(baseline.mapped_ids) - set(candidate.mapped_ids)
    if lost_mapped:
        reasons.append("mapped channel IDs lost: " + ", ".join(sorted(lost_mapped)))
    lost_scheduled = set(baseline.scheduled_ids) - set(candidate.scheduled_ids)
    if lost_scheduled:
        reasons.append("scheduled channel IDs lost: " + ", ".join(sorted(lost_scheduled)))
    return EpgCoverageComparison(not reasons,baseline,candidate,tuple(reasons))
