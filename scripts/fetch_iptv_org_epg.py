#!/usr/bin/env python3
"""Build a bounded, playlist-targeted supplemental XMLTV guide from iptv-org/epg.

The upstream catalogue contains thousands of channels and its all-catalogue crawl
can stall on token/API failures. Only catalogue rows whose xmltv_id is relevant
to an active playlist identity or its approved mapping are scraped. This source
is supplemental: failures produce a valid empty guide so other XMLTV providers
can still supply schedules.
"""
import ast
import csv
import io
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = "https://github.com/iptv-org/epg.git"
WORK = Path("/tmp/iptv-org-epg")
OUTPUT = Path("/tmp/iptv-org-guide.xml")
TARGET_CHANNELS = Path("/tmp/iptv-org-target.channels.xml")
PLAYLISTS = (
    Path("IPTV-Playlist.m3u"),
    Path("BDIX-Playlist.m3u"),
    Path("International-Playlist.m3u"),
)
MAPPING = Path("reports/epg-india-channel-mapping.csv")
SITES = ("dishtv.in", "tataplay.com", "airtelxstream.in", "zee5.com", "sky.com")
# Keep the source set targeted: these sources have stable XMLTV identities. sky.com
# supplements exact UK/diaspora IDs; its rows receive an additional name-consistency check.
INACTIVE_GROUPS = {
    "backup", "backups", "not playing", "not playing...", "not playing…",
    "not playing (review)", "test", "new", "new channels", "new backup", "new backups",
}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
SCRAPE_TIMEOUT_SECONDS = 180
SCRAPE_REQUEST_TIMEOUT_MS = 15000
SCRAPE_MAX_CONNECTIONS = 8
ROOT = Path(__file__).resolve().parent.parent
IDENTITY_CONFIG = ROOT / "scripts" / "epg_coverage.py"


def load_explicit_epg_mappings():
    """Load repository-curated EPG aliases and identity locks without executing the coverage script."""
    if not IDENTITY_CONFIG.is_file():
        return {}
    tree = ast.parse(IDENTITY_CONFIG.read_text(encoding="utf-8"), filename=str(IDENTITY_CONFIG))
    values = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in {"EPG_ALIASES", "EPG_LOCKS"}:
                values[target.id] = ast.literal_eval(node.value)
    explicit = {key: list(value) for key, value in values.get("EPG_ALIASES", {}).items()}
    # A lock is authoritative for that playlist identity and supersedes its aliases.
    explicit.update({key: list(value) for key, value in values.get("EPG_LOCKS", {}).items()})
    return explicit


def normalize_channel_name(value):
    """Normalize display labels only for the conservative sky.com name guard."""
    value = str(value or "").casefold()
    value = re.sub(r"\b(?:\d{3,4}p|50fps|60fps)\b", " ", value)
    value = re.sub(r"\b(?:hd|sd|uhd|fhd|tv|channel)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def active_playlist_name_index(playlist_texts, mapping_text="", explicit_mappings=None):
    """Map active playlist and approved alternate IDs to their normalized display names."""
    names_by_id = {}
    active_names = {}
    for text in playlist_texts:
        current = None
        for line in text.splitlines():
            if line.startswith("#EXTINF:"):
                current = dict(ATTR_RE.findall(line))
                continue
            if current is not None and line.strip().startswith(("http://", "https://")):
                group = current.get("group-title", "").strip().casefold()
                tvg_id = current.get("tvg-id", "").strip()
                if tvg_id and group not in INACTIVE_GROUPS:
                    label = (current.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
                    key = normalize_channel_name(label)
                    if key:
                        active_names.setdefault(tvg_id, set()).add(key)
                        names_by_id.setdefault(tvg_id, set()).add(key)
                current = None
    if mapping_text.strip():
        try:
            for row in csv.DictReader(io.StringIO(mapping_text)):
                target_id = (row.get("tvg_id") or "").strip()
                if target_id not in active_names:
                    continue
                for source_id in (item.strip() for item in (row.get("epg_id") or "").split("|")):
                    if source_id:
                        names_by_id.setdefault(source_id, set()).update(active_names[target_id])
        except (csv.Error, TypeError) as exc:
            print(f"Warning: could not fully read EPG mapping names: {exc}")
    for target_id, source_ids in (explicit_mappings or {}).items():
        if target_id not in active_names:
            continue
        for source_id in source_ids:
            if source_id:
                names_by_id.setdefault(source_id, set()).update(active_names[target_id])
    return names_by_id


def run(*args, cwd=None, timeout=None):
    """Run an external command and enforce a finite timeout when requested."""
    print("+", " ".join(str(arg) for arg in args), flush=True)
    return subprocess.run(args, cwd=cwd, check=True, timeout=timeout)


def active_playlist_ids(playlist_texts):
    """Collect tvg-ids with stream URLs from active groups only."""
    result = set()
    for text in playlist_texts:
        current = None
        for line in text.splitlines():
            if line.startswith("#EXTINF:"):
                current = dict(ATTR_RE.findall(line))
                continue
            if current is not None and line.strip().startswith(("http://", "https://")):
                group = current.get("group-title", "").strip().casefold()
                tvg_id = current.get("tvg-id", "").strip()
                if tvg_id and group not in INACTIVE_GROUPS:
                    result.add(tvg_id)
                current = None
    return result


def target_channel_ids(playlist_texts, mapping_text="", explicit_mappings=None):
    """Return active IDs, existing mappings, and repository-approved IDs/aliases for active channels."""
    active_ids = active_playlist_ids(playlist_texts)
    result = set(active_ids)
    if mapping_text.strip():
        try:
            rows = csv.DictReader(io.StringIO(mapping_text))
            for row in rows:
                target_id = (row.get("tvg_id") or "").strip()
                if target_id not in active_ids:
                    continue
                for source_id in (item.strip() for item in (row.get("epg_id") or "").split("|")):
                    if source_id:
                        result.add(source_id)
        except (csv.Error, TypeError) as exc:
            print(f"Warning: could not fully read EPG mapping for targeted catalogue selection: {exc}")
    for target_id in active_ids:
        for source_id in (explicit_mappings or {}).get(target_id, []):
            if source_id:
                result.add(source_id)
    return result


def build_target_channels_xml(catalogue_texts, target_ids, target_names_by_id=None):
    """Merge exact target IDs; additionally require exact normalized names for sky.com rows."""
    root = ET.Element("channels")
    target_names_by_id = target_names_by_id or {}
    seen = set()
    for text in catalogue_texts:
        try:
            catalogue = ET.fromstring(text)
        except ET.ParseError as exc:
            print(f"Warning: skipping malformed iptv-org channel catalogue: {exc}")
            continue
        for channel in catalogue.findall("channel"):
            xmltv_id = (channel.attrib.get("xmltv_id") or "").strip()
            if not xmltv_id or xmltv_id not in target_ids:
                continue
            # Require the extra source's label to identify the same channel; exact
            # XMLTV IDs alone are not enough when a provider catalogue is mislabeled.
            if channel.attrib.get("site", "") == "sky.com":
                source_name = normalize_channel_name(channel.text or "")
                expected_names = target_names_by_id.get(xmltv_id, set())
                if not expected_names or source_name not in expected_names:
                    continue
            key = (
                channel.attrib.get("site", ""),
                channel.attrib.get("site_id", ""),
                channel.attrib.get("lang", ""),
                xmltv_id,
            )
            if key in seen:
                continue
            seen.add(key)
            root.append(ET.fromstring(ET.tostring(channel, encoding="utf-8")))
    return ET.tostring(root, encoding="unicode", xml_declaration=False)


def write_empty_guide(reason):
    """Make an XMLTV-valid empty guide so independent sources can still run."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    root = ET.Element("tv", {"generator-info-name": "BDIX-IPTV optional iptv-org source"})
    OUTPUT.write_bytes(
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        + ET.tostring(root, encoding="utf-8")
    )
    print(f"Warning: {reason}; continuing with other XMLTV sources.")


def read_active_targets():
    playlist_texts = []
    for path in PLAYLISTS:
        if not path.is_file():
            print(f"Warning: playlist unavailable for target selection: {path}")
            continue
        playlist_texts.append(path.read_text(encoding="utf-8-sig"))
    mapping_text = MAPPING.read_text(encoding="utf-8-sig") if MAPPING.is_file() else ""
    return target_channel_ids(playlist_texts, mapping_text, load_explicit_epg_mappings())


def read_active_target_names():
    playlist_texts = []
    for path in PLAYLISTS:
        if path.is_file():
            playlist_texts.append(path.read_text(encoding="utf-8-sig"))
    mapping_text = MAPPING.read_text(encoding="utf-8-sig") if MAPPING.is_file() else ""
    return active_playlist_name_index(playlist_texts, mapping_text, load_explicit_epg_mappings())


def selected_catalogue_texts():
    texts = []
    for site in SITES:
        path = WORK / "sites" / site / f"{site}.channels.xml"
        if not path.is_file():
            print(f"Warning: upstream channel catalogue unavailable: {path}")
            continue
        texts.append(path.read_text(encoding="utf-8"))
    return texts


def main():
    targets = read_active_targets()
    target_names_by_id = read_active_target_names()
    if not targets:
        write_empty_guide("no active tvg-ids found across the published playlists")
        return

    if WORK.exists():
        shutil.rmtree(WORK)
    if OUTPUT.exists():
        OUTPUT.unlink()
    if TARGET_CHANNELS.exists():
        TARGET_CHANNELS.unlink()

    try:
        run("git", "clone", "--depth", "1", REPO, str(WORK), timeout=90)
        run("npm", "ci", "--no-audit", "--no-fund", cwd=WORK, timeout=240)

        catalogue_texts = selected_catalogue_texts()
        target_xml = build_target_channels_xml(catalogue_texts, targets, target_names_by_id)
        TARGET_CHANNELS.write_text(target_xml + "\n", encoding="utf-8")
        selected_count = len(ET.fromstring(target_xml).findall("channel"))
        print(
            f"iptv-org target selection: {len(targets)} IDs considered; "
            f"{selected_count} exact catalogue rows selected across {len(SITES)} sites."
        )
        if selected_count == 0:
            write_empty_guide("no exact active/mapped IDs matched the selected iptv-org catalogues")
            return

        run(
            "npm", "run", "grab", "---",
            f"--channels={TARGET_CHANNELS}",
            f"--output={OUTPUT}",
            "--lang=en",
            f"--timeout={SCRAPE_REQUEST_TIMEOUT_MS}",
            f"--maxConnections={SCRAPE_MAX_CONNECTIONS}",
            "--days=3",
            cwd=WORK,
            timeout=SCRAPE_TIMEOUT_SECONDS,
        )

        if not OUTPUT.is_file() or OUTPUT.stat().st_size == 0:
            write_empty_guide("iptv-org scraper produced no XMLTV output")
            return
        try:
            root = ET.parse(OUTPUT).getroot()
        except ET.ParseError as exc:
            write_empty_guide(f"iptv-org scraper output was malformed ({exc})")
            return
        if root.tag != "tv":
            write_empty_guide(f"iptv-org scraper output had unexpected root element {root.tag!r}")
            return
        programme_count = len(root.findall("programme"))
        print(
            f"iptv-org targeted guide ready: {OUTPUT} ({OUTPUT.stat().st_size} bytes, "
            f"{len(root.findall('channel'))} channels, {programme_count} programmes)."
        )
        if programme_count == 0:
            print("Warning: targeted iptv-org guide has no programmes; the main generator will use other configured sources.")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, ET.ParseError) as exc:
        write_empty_guide(f"optional iptv-org fetch failed ({type(exc).__name__}: {exc})")


if __name__ == "__main__":
    main()
