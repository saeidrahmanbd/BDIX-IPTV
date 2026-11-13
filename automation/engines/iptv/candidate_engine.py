"""IPTV owner-curated candidate builder. It only returns candidate text; it never writes files."""
from __future__ import annotations
from dataclasses import dataclass
from automation.core.playlist_contract import parse_rows, assert_iptv_existing_rows_preserved

@dataclass(frozen=True)
class DiscoveryCandidate:
    extinf: str
    url: str
    backup: bool = False

def build_candidate(baseline_text: str, discoveries: list[DiscoveryCandidate]) -> str:
    """Append valid discoveries to manual-review queues while preserving every old row."""
    if not baseline_text.lstrip("\ufeff").startswith("#EXTM3U"):
        raise ValueError("baseline must have an #EXTM3U header")
    baseline_rows = parse_rows(baseline_text)
    existing_urls = {row.url for row in baseline_rows}
    additions: list[str] = []
    seen_new: set[str] = set()
    for item in discoveries:
        url = item.url.strip()
        extinf = item.extinf.strip()
        if not url.startswith(("http://", "https://")):
            raise ValueError("discovery URL must be HTTP(S)")
        if not extinf.startswith("#EXTINF:"):
            raise ValueError("discovery metadata must start with #EXTINF:")
        if url in existing_urls or url in seen_new:
            continue
        queue = "New Backups" if item.backup else "New Channels"
        if f'group-title="{queue}"' not in extinf:
            raise ValueError(f"new discovery must be assigned to {queue}")
        if "\n" in extinf or "\r" in extinf or "\n" in url or "\r" in url:
            raise ValueError("discovery record must be a single line")
        additions.extend((extinf, url))
        seen_new.add(url)
    if not additions:
        return baseline_text
    separator = "" if baseline_text.endswith("\n") else "\n"
    candidate = baseline_text + separator + "\n".join(additions) + "\n"
    assert_iptv_existing_rows_preserved(baseline_text, candidate)
    return candidate


@dataclass(frozen=True)
class IptvCandidate:
    text: str
    baseline_rows: int
    candidate_rows: int
    publish: bool = False

def build_iptv_candidate(baseline_text: str, discoveries: list[DiscoveryCandidate],
                         metadata_patches: list, repository_root) -> IptvCandidate:
    """Combine evidence-approved metadata patches and manual-queue discoveries in memory only."""
    from automation.engines.iptv.metadata_repair import apply_metadata_patches
    baseline_rows=parse_rows(baseline_text)
    metadata_candidate=apply_metadata_patches(baseline_text,metadata_patches,repository_root)
    candidate=build_candidate(metadata_candidate,discoveries)
    assert_iptv_existing_rows_preserved(baseline_text,candidate)
    return IptvCandidate(candidate,len(baseline_rows),len(parse_rows(candidate)),False)
