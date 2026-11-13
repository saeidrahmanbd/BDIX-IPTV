"""End-to-end in-memory EPG candidate engine with approved aliases and regression gates."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from automation.engines.epg.alias_apply import ApprovedAlias, apply_approved_aliases
from automation.engines.epg.candidate_gate import EpgCandidateDecision, evaluate_candidate

@dataclass(frozen=True)
class EpgCandidate:
    xml_text: str
    decision: EpgCandidateDecision
    publish: bool = False

def build_epg_candidate(playlist_text: str, last_known_good_xml: str,
                        source_candidate_xml: str | None = None,
                        approved_aliases: list[ApprovedAlias] | None = None,
                        as_of: datetime | None = None) -> EpgCandidate:
    """Validate a provider candidate, apply only approved aliases, and reject coverage/freshness regression."""
    candidate=source_candidate_xml if source_candidate_xml is not None else last_known_good_xml
    aliases=approved_aliases or []
    if aliases:
        candidate=apply_approved_aliases(playlist_text,candidate,aliases)
    candidate=preserve_missing_fresh_schedules(
        playlist_text,last_known_good_xml,candidate,as_of
    )
    decision=evaluate_candidate(last_known_good_xml,candidate,playlist_text,as_of)
    return EpgCandidate(candidate,decision,False)


def preserve_missing_fresh_schedules(playlist_text: str, baseline_xml: str,
                                     candidate_xml: str,
                                     as_of: datetime | None = None) -> str:
    """Restore missing active-channel metadata and still-valid baseline programmes."""
    import copy
    import xml.etree.ElementTree as ET
    from datetime import timezone
    from zoneinfo import ZoneInfo
    from automation.core.playlist_contract import parse_rows, ATTR_RE
    from automation.engines.epg.freshness import _parse_xmltv_datetime

    if as_of is None:
        as_of = datetime.now(ZoneInfo("Asia/Dhaka"))
    if as_of.tzinfo is None:
        raise ValueError("as_of must be timezone-aware")
    as_of_utc = as_of.astimezone(timezone.utc)
    inactive_groups = {
        "backup", "review", "test", "not playing",
        "new channels", "new backups", "new backup",
    }
    active_ids = set()
    for row in parse_rows(playlist_text):
        attrs = dict(ATTR_RE.findall(row.extinf))
        channel_id = attrs.get("tvg-id", "").strip()
        group = attrs.get("group-title", "").strip().casefold()
        if channel_id and group not in inactive_groups:
            active_ids.add(channel_id)
    if not active_ids:
        raise ValueError("playlist contains no active EPG channel IDs")

    baseline_root = ET.fromstring(baseline_xml)
    candidate_root = ET.fromstring(candidate_xml)
    candidate_channels = {(node.get("id") or "").strip()
                          for node in candidate_root.findall("channel")}
    candidate_scheduled = set()
    for node in candidate_root.findall("programme"):
        channel_id = (node.get("channel") or "").strip()
        stop = _parse_xmltv_datetime(node.get("stop") or "")
        if channel_id in active_ids and stop > as_of_utc:
            candidate_scheduled.add(channel_id)

    restored_channels = 0
    for node in baseline_root.findall("channel"):
        channel_id = (node.get("id") or "").strip()
        if channel_id in active_ids and channel_id not in candidate_channels:
            candidate_root.append(copy.deepcopy(node))
            candidate_channels.add(channel_id)
            restored_channels += 1

    restored_programmes = 0
    for node in baseline_root.findall("programme"):
        channel_id = (node.get("channel") or "").strip()
        if channel_id not in active_ids or channel_id in candidate_scheduled:
            continue
        stop = _parse_xmltv_datetime(node.get("stop") or "")
        if stop > as_of_utc:
            candidate_root.append(copy.deepcopy(node))
            restored_programmes += 1

    if restored_channels or restored_programmes:
        print(
            "EPG fallback: restored "
            f"{restored_channels} active channel definitions and "
            f"{restored_programmes} still-current/future baseline programmes.",
            flush=True,
        )
        return ET.tostring(candidate_root, encoding="unicode")
    # Preserve byte-for-byte source text on a no-op dry run. XML serialization
    # alone can normalize whitespace and falsely look like a production change.
    return candidate_xml



def build_epg_candidate_persisted(playlist_text: str, last_known_good_xml: str,
                                  baseline_commit: str, store,
                                  source_candidate_xml: str | None = None,
                                  approved_aliases: list[ApprovedAlias] | None = None,
                                  as_of: datetime | None = None,
                                  repository_root: str | None = None,
                                  iptv_playlist_text: str | None = None,
                                  international_playlist_text: str | None = None):
    """Build one idempotently reserved EPG candidate; no publication or production writes."""
    import hashlib
    import json
    from zoneinfo import ZoneInfo
    from automation.core.github_state_store import execute_remote_run
    from automation.core.run_ledger import RunRequest

    alias_material = [
        (item.source_id, item.target_id, item.evidence, item.approved)
        for item in (approved_aliases or [])
    ]
    material = "\0".join((
        playlist_text,
        last_known_good_xml,
        source_candidate_xml or ("isolated-live-source-generation" if repository_root else ""),
        json.dumps(alias_material, ensure_ascii=False, sort_keys=True),
        as_of.isoformat() if as_of else "",
    ))
    fingerprint = hashlib.sha256(material.encode("utf-8")).hexdigest()
    request = RunRequest("epg", (as_of.date() if as_of else datetime.now(ZoneInfo("Asia/Dhaka")).date()),
                         baseline_commit, fingerprint)
    def operation():
        candidate_xml = source_candidate_xml
        if candidate_xml is None and repository_root is not None:
            from automation.engines.epg.source_provider import build_epg_source_candidate
            candidate_xml = build_epg_source_candidate(
                repository_root,
                iptv_playlist_text=iptv_playlist_text,
                international_playlist_text=international_playlist_text,
            )
        return build_epg_candidate(
            playlist_text, last_known_good_xml, candidate_xml,
            approved_aliases, as_of
        )

    return execute_remote_run(store, request, operation)
