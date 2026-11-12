#!/usr/bin/env python3
"""Country metadata diagnostics for discovery queues.

New Channels / New Backups are intentionally manual-review queues. Their source
country, tvg-country, IDs, language and logo may be missing or inconsistent;
those metadata defects are warnings, not discovery gates. Strict verification
helpers remain available for later audits and metadata repair.

The validate command reports country metadata warnings and fails only on
invalid stream URL syntax.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

# Only these two queues require BD/IN candidate verification. Review is a general
# quarantine queue and may legitimately contain channels from any country.
REVIEW_QUEUES = frozenset({"New Channels", "New Backups", "New Backup"})
NON_PRIMARY_GROUPS = frozenset({"Backup", "Review", "Not Playing", *REVIEW_QUEUES})
ALLOWED = frozenset({"BD", "IN"})

# Curated exceptions for India-feed variants whose upstream catalogue IDs carry
# a distribution-market suffix (for example .uk/.us) rather than the Indian
# service identity. These are exact normalized channel-name matches and apply
# ONLY when the discovery source itself is the India feed. Never use them for
# an unknown feed or for similarly named international channels.
INDIA_FEED_ID_OVERRIDES = {
    "cartoonnetwork": "CartoonNetwork.in",
    "colorscineplex": "ColorsCineplex.in",
}

QUALITY = {"uhd", "fhd", "hd", "sd", "4k", "1080p", "720p", "576p", "480p", "360p", "240p"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
ID_CC_RE = re.compile(r"\.([a-z]{2})(?:@|$)")

# ISO 3166-1 alpha-2 codes (+ "uk", which iptv-org uses for the United Kingdom).
ISO_CODES = frozenset(
    "ad ae af ag ai al am ao aq ar as at au aw ax az ba bb bd be bf bg bh bi bj bl bm bn bo bq br bs bt bv bw by bz "
    "ca cc cd cf cg ch ci ck cl cm cn co cr cu cv cw cx cy cz de dj dk dm do dz ec ee eg eh er es et fi fj fk fm fo fr "
    "ga gb gd ge gf gg gh gi gl gm gn gp gq gr gs gt gu gw gy hk hm hn hr ht hu id ie il im in io iq ir is it je jm jo "
    "jp ke kg kh ki km kn kp kr kw ky kz la lb lc li lk lr ls lt lu lv ly ma mc md me mf mg mh mk ml mm mn mo mp mq mr "
    "ms mt mu mv mw mx my mz na nc ne nf ng ni nl no np nr nu nz om pa pe pf pg ph pk pl pm pn pr ps pt pw py qa re ro "
    "rs ru rw sa sb sc sd se sg sh si sj sk sl sm sn so sr ss st sv sx sy sz tc td tf tg th tj tk tl tm tn to tr tt tv "
    "tw tz ua ug um us uy uz va vc ve vg vi vn vu wf ws ye yt za zm zw uk".split()
)


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def norm_name(value: str) -> str:
    """Normalize a channel name for identity comparison.

    Letters, digits *and combining marks* (categories L, M, N) are preserved so
    Bengali/Hindi names that differ only by vowel signs do not collide.
    """
    value = unicodedata.normalize("NFKC", value or "").casefold().replace("_", " ")
    value = re.sub(r"\[[^]]*\]|\([^)]*\)", " ", value)
    value = " ".join(x for x in value.split() if x not in QUALITY)
    return "".join(c for c in value if c.isalnum() or unicodedata.category(c)[0] in "LMN")


def id_country(value: str) -> str | None:
    """Country code (upper-case) encoded in an id suffix, or None if absent/not a country."""
    m = ID_CC_RE.search((value or "").strip().casefold())
    if m and m.group(1) in ISO_CODES:
        return m.group(1).upper()
    return None


@dataclass
class Verdict:
    country: str | None
    tvg_id: str = ""
    basis: str = ""
    reason: str = ""

    @property
    def ok(self) -> bool:
        return self.country in ALLOWED


class Reference:
    """Existing repository mappings used as independent country evidence."""

    def __init__(self) -> None:
        self.ids_by_name: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.foreign_names: set[str] = set()

    def add(self, a: dict[str, str], name: str) -> None:
        group = a.get("group-title", "").strip()
        if group in NON_PRIMARY_GROUPS:
            return  # backups and review queues are never identity evidence
        key = norm_name(name or a.get("tvg-name", ""))
        if not key:
            return
        ids = [x.strip() for x in (a.get("tvg-id", ""), a.get("channel-id", "")) if x and x.strip()]
        ccs = {id_country(x) for x in ids} - {None}
        if group == "International" or (ccs - ALLOWED):
            self.foreign_names.add(key)
            return
        if len(ccs) != 1:
            return
        cc = next(iter(ccs))
        declared = a.get("tvg-country", "").strip().upper()
        if declared and declared != cc:
            return
        self.ids_by_name[key][cc].add(next(x for x in ids if id_country(x) == cc))


def build_reference(rows) -> Reference:
    """rows: iterable of (attrs, name)."""
    ref = Reference()
    for a, name in rows:
        ref.add(a, name)
    return ref


def verify_country(a: dict[str, str], name: str, reference: Reference | None = None,
                   feed_country: str | None = None) -> Verdict:
    """Verify a candidate is Bangladeshi/Indian.  ``feed_country`` is 'BD'/'IN'/None."""
    reference = reference or Reference()
    feed = (feed_country or "").upper() or None
    declared = a.get("tvg-country", "").strip().upper()
    ids = [x.strip() for x in (a.get("tvg-id", ""), a.get("channel-id", "")) if x and x.strip()]
    ccs = {id_country(x) for x in ids} - {None}

    # Some India-feed catalogues publish Indian services with a UK/US
    # distribution suffix. Accept only the two explicitly curated identities,
    # only on the India feed, and rewrite them to canonical .in IDs downstream.
    override_id = INDIA_FEED_ID_OVERRIDES.get(norm_name(name or a.get("tvg-name", "")))
    if feed == "IN" and override_id:
        return Verdict("IN", tvg_id=override_id, basis="curated-india-feed-override")

    if declared and declared not in ALLOWED:
        return Verdict(None, reason=f"declared country {declared} is not BD/IN")
    if ccs - ALLOWED:
        return Verdict(None, reason="id carries a non-BD/IN country suffix")
    if len(ccs) > 1:
        return Verdict(None, reason="tvg-id/channel-id disagree on country")

    if ccs:  # strong evidence: exactly one of BD / IN
        cc = next(iter(ccs))
        if feed and feed != cc:
            return Verdict(None, reason=f"id country {cc} conflicts with {feed} source feed")
        if declared and declared != cc:
            return Verdict(None, reason=f"id country {cc} conflicts with tvg-country {declared}")
        good = next(x for x in ids if id_country(x) == cc)
        tid = a.get("tvg-id", "").strip()
        return Verdict(cc, tvg_id=tid if id_country(tid) == cc else good, basis="id")

    # id missing/malformed: need independent repository evidence
    key = norm_name(name or a.get("tvg-name", ""))
    if not key:
        return Verdict(None, reason="no usable channel name for verification")
    if key in reference.foreign_names:
        return Verdict(None, reason="name matches a known International/foreign channel")
    mapped = reference.ids_by_name.get(key, {})
    if len(mapped) != 1:
        return Verdict(None, reason="id missing/malformed and no unambiguous repository mapping"
                       if not mapped else "repository mapping is ambiguous between BD and IN")
    cc = next(iter(mapped))
    if feed and feed != cc:
        return Verdict(None, reason=f"repository mapping {cc} conflicts with {feed} source feed")
    if declared and declared != cc:
        return Verdict(None, reason=f"repository mapping {cc} conflicts with tvg-country {declared}")
    return Verdict(cc, tvg_id=sorted(mapped[cc])[0], basis="repository-mapping")


def parse_entries(text: str):
    """Yield (extinf_line, attrs, name, url) for each EXTINF/URL pair."""
    lines = text.replace("\r", "").splitlines()
    cur = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            cur = line
        elif cur is not None and line.strip().lower().startswith(("http://", "https://")):
            a = attrs(cur)
            display = cur.rsplit(",", 1)[-1].strip() if "," in cur else ""
            yield cur, a, (a.get("tvg-name") or display).strip(), line.strip()
            cur = None


def reference_from_playlists(paths) -> Reference:
    rows = []
    for p in paths:
        p = Path(p)
        if p.is_file():
            rows.extend((a, n) for _, a, n, _ in parse_entries(p.read_text(encoding="utf-8-sig", errors="replace")))
    return build_reference(rows)


def queue_metadata_warnings(entries, reference: Reference) -> list[str]:
    """Describe uncertain discovery metadata without treating it as an error."""
    warnings = []
    for a, name, url in entries:
        if a.get("group-title", "").strip() not in REVIEW_QUEUES:
            continue
        label = name or a.get("tvg-name", "") or url
        verdict = verify_country(a, name, reference)
        if not verdict.ok:
            warnings.append(f"{label}: country metadata needs manual review ({verdict.reason})")
            continue
        declared = a.get("tvg-country", "").strip().upper()
        if declared != verdict.country:
            warnings.append(
                f"{label}: tvg-country is {declared or 'missing'}; metadata suggests {verdict.country}"
            )
    return warnings


def queue_errors(entries, reference: Reference) -> list[str]:
    """Only malformed/non-HTTP stream URLs are hard queue errors."""
    errors = []
    for a, name, url in entries:
        if a.get("group-title", "").strip() not in REVIEW_QUEUES:
            continue
        label = name or a.get("tvg-name", "") or url
        if not url.lower().startswith(("http://", "https://")):
            errors.append(f"{label}: invalid stream URL")
    return errors


def validate_playlist(path: Path, extra_reference_paths=()) -> list[str]:
    rows = list(parse_entries(path.read_text(encoding="utf-8-sig", errors="replace")))
    reference = reference_from_playlists([path, *extra_reference_paths])
    return queue_errors([(a, n, u) for _, a, n, u in rows], reference)


def validate_playlist_warnings(path: Path, extra_reference_paths=()) -> list[str]:
    rows = list(parse_entries(path.read_text(encoding="utf-8-sig", errors="replace")))
    reference = reference_from_playlists([path, *extra_reference_paths])
    return queue_metadata_warnings([(a, n, u) for _, a, n, u in rows], reference)


def main(argv: list[str]) -> int:
    if not argv or argv[0] != "validate":
        print(__doc__)
        return 2
    paths = [Path(x) for x in argv[1:]] or [Path("IPTV-Playlist.m3u")]
    extra = [Path("International-Playlist.m3u")]
    failed = False
    for p in paths:
        warnings = validate_playlist_warnings(p, [x for x in extra if x != p])
        for warning in warnings:
            print(f"::warning::{p}: {warning}")
        errors = validate_playlist(p, [x for x in extra if x != p])
        for error in errors:
            print(f"::error::{p}: {error}")
        failed = failed or bool(errors)
    if failed:
        return 1
    print("Discovery queues remain available for manual review; country metadata warnings do not block.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
