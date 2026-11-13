"""Conservative EPG alias suggestions. This module never changes aliases or guide data."""
from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
import unicodedata
import re
import xml.etree.ElementTree as ET
from automation.core.playlist_contract import parse_rows, ATTR_RE
from automation.engines.epg.validator import validate_xmltv

@dataclass(frozen=True)
class ActiveChannel:
    tvg_id: str
    names: tuple[str, ...]

@dataclass(frozen=True)
class EpgChannel:
    channel_id: str
    names: tuple[str, ...]

def normalize_name(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD",value.casefold())
    return "".join(char for char in decomposed if char.isalnum())

def extract_active_channels(playlist_text: str) -> dict[str,ActiveChannel]:
    names: dict[str,set[str]] = defaultdict(set)
    for row in parse_rows(playlist_text):
        attrs = dict(ATTR_RE.findall(row.extinf))
        tvg_id = attrs.get("tvg-id","").strip()
        if not tvg_id:
            continue
        name = attrs.get("tvg-name","").strip()
        if not name and "," in row.extinf:
            name = row.extinf.split(",",1)[1].strip()
        if name:
            names[tvg_id].add(name)
    return {key:ActiveChannel(key,tuple(sorted(value))) for key,value in names.items()}

def extract_epg_channels(xmltv_text: str) -> dict[str,EpgChannel]:
    validation = validate_xmltv(xmltv_text)
    if not validation.valid:
        raise ValueError("XMLTV failed validation: " + "; ".join(validation.errors[:5]))
    root = ET.fromstring(xmltv_text)
    names: dict[str,set[str]] = defaultdict(set)
    for channel in root.findall("channel"):
        channel_id = (channel.get("id") or "").strip()
        if not channel_id:
            continue
        for node in channel.findall("display-name"):
            value = (node.text or "").strip()
            if value:
                names[channel_id].add(value)
        if not names[channel_id]:
            names[channel_id].add(channel_id)
    return {key:EpgChannel(key,tuple(sorted(value))) for key,value in names.items()}

def _locale_signature(channel_id: str) -> tuple[str | None,str | None]:
    value = channel_id.casefold()
    country_match = re.search(r"\\.([a-z]{2})(?:@|$)",value)
    country = country_match.group(1) if country_match else None
    region_match = re.search(r"@([a-z]+)$",value)
    region = region_match.group(1) if region_match else None
    if region in {"sd","hd","uhd","fhd","4k"}:
        region = None
    return country,region

def _locale_conflict(active_id: str, epg_id: str) -> str | None:
    active_country,active_region = _locale_signature(active_id)
    epg_country,epg_region = _locale_signature(epg_id)
    if active_country and epg_country and active_country != epg_country:
        return f"country suffix differs ({active_country} vs {epg_country})"
    if active_region and epg_region and active_region != epg_region:
        return f"region suffix differs ({active_region} vs {epg_region})"
    return None

def suggest_aliases(playlist_text: str, xmltv_text: str,
                    minimum_score: float = 0.90, minimum_margin: float = 0.05) -> dict:
    if not 0 < minimum_score <= 1 or not 0 <= minimum_margin <= 1:
        raise ValueError("score thresholds must be within 0..1")
    active = extract_active_channels(playlist_text)
    epg = extract_epg_channels(xmltv_text)
    epg_id_normalized: dict[str,list[str]] = defaultdict(list)
    epg_name_normalized: dict[str,set[str]] = defaultdict(set)
    epg_names: dict[str,list[tuple[str,str]]] = {}
    for channel_id,channel in epg.items():
        epg_id_normalized[normalize_name(channel_id)].append(channel_id)
        epg_names[channel_id] = [(name,normalize_name(name)) for name in channel.names if normalize_name(name)]
        for _,normalized in epg_names[channel_id]:
            epg_name_normalized[normalized].add(channel_id)

    suggestions: list[dict] = []
    ambiguous: list[dict] = []
    already_mapped = 0
    for tvg_id,channel in sorted(active.items()):
        if tvg_id in epg:
            already_mapped += 1
            continue
        normalized_id = normalize_name(tvg_id)
        id_matches = epg_id_normalized.get(normalized_id,[]) if normalized_id else []
        if len(id_matches) == 1:
            target = id_matches[0]
            suggestions.append({
                "tvg_id":tvg_id,"epg_channel_id":target,"playlist_names":list(channel.names),
                "epg_names":list(epg[target].names),"match_type":"normalized_id",
                "confidence":1.0,"status":"manual_review_required",
            })
            continue
        if len(id_matches) > 1:
            ambiguous.append({"tvg_id":tvg_id,"playlist_names":list(channel.names),
                              "candidate_ids":sorted(id_matches),"reason":"normalized ID collision"})
            continue

        exact_targets = sorted({target for name in channel.names for target in epg_name_normalized.get(normalize_name(name),set())})
        locale_conflicts = [(target,_locale_conflict(tvg_id,target)) for target in exact_targets]
        locale_conflicts = [(target,reason) for target,reason in locale_conflicts if reason]
        if locale_conflicts:
            ambiguous.append({"tvg_id":tvg_id,"playlist_names":list(channel.names),
                              "candidate_ids":[target for target,_ in locale_conflicts],
                              "reason":"; ".join(reason for _,reason in locale_conflicts)})
            continue
        if len(exact_targets) == 1:
            target = exact_targets[0]
            matched_names = [name for name in epg[target].names if normalize_name(name) in {normalize_name(x) for x in channel.names}]
            suggestions.append({
                "tvg_id":tvg_id,"epg_channel_id":target,"playlist_names":list(channel.names),
                "epg_names":matched_names,"match_type":"exact_name",
                "confidence":1.0,"status":"manual_review_required",
            })
            continue
        if len(exact_targets) > 1:
            ambiguous.append({"tvg_id":tvg_id,"playlist_names":list(channel.names),
                              "candidate_ids":exact_targets,"reason":"exact display-name collision"})
            continue

        scores: dict[str,tuple[float,str]] = {}
        locale_rejected: list[tuple[str,str]] = []
        for target_id,candidates in epg_names.items():
            conflict = _locale_conflict(tvg_id,target_id)
            if conflict:
                locale_rejected.append((target_id,conflict))
                continue
            best = (0.0,"")
            for active_name in channel.names:
                active_norm = normalize_name(active_name)
                if not active_norm:
                    continue
                for epg_name,epg_norm in candidates:
                    score = SequenceMatcher(None,active_norm,epg_norm).ratio()
                    if score > best[0]:
                        best = (score,epg_name)
            scores[target_id] = best
        ranked = sorted(((score,target_id,name) for target_id,(score,name) in scores.items()),reverse=True)
        if not ranked or ranked[0][0] < minimum_score:
            if locale_rejected and not ranked:
                ambiguous.append({"tvg_id":tvg_id,"playlist_names":list(channel.names),
                                  "candidate_ids":[target for target,_ in locale_rejected[:5]],
                                  "reason":"all name candidates conflict by locale"})
            continue
        top_score,top_id,top_name = ranked[0]
        second_score = ranked[1][0] if len(ranked) > 1 else 0.0
        if top_score - second_score < minimum_margin:
            ambiguous.append({
                "tvg_id":tvg_id,"playlist_names":list(channel.names),
                "candidates":[{"epg_channel_id":target_id,"epg_name":name,"score":round(score,4)}
                              for score,target_id,name in ranked[:5]],
                "reason":"top EPG name matches are too close to distinguish",
            })
            continue
        suggestions.append({
            "tvg_id":tvg_id,"epg_channel_id":top_id,"playlist_names":list(channel.names),
            "epg_names":[top_name],"match_type":"fuzzy_name",
            "confidence":round(top_score,4),"status":"manual_review_required",
        })
    suggestions.sort(key=lambda item:(item["match_type"],item["tvg_id"]))
    ambiguous.sort(key=lambda item:item["tvg_id"])
    return {
        "active_channel_ids":len(active),
        "already_mapped":already_mapped,
        "suggestion_count":len(suggestions),
        "normalized_id_suggestions":sum(item["match_type"]=="normalized_id" for item in suggestions),
        "exact_name_suggestions":sum(item["match_type"]=="exact_name" for item in suggestions),
        "fuzzy_name_suggestions":sum(item["match_type"]=="fuzzy_name" for item in suggestions),
        "ambiguous_count":len(ambiguous),
        "unmatched_count":len(active)-already_mapped-len(suggestions)-len(ambiguous),
        "suggestions":suggestions,
        "ambiguous":ambiguous,
        "auto_applied":False,
    }
