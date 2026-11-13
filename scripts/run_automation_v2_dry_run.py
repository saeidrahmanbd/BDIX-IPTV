"""Read-only dry run against the immutable production baseline; never writes playlists or EPG."""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from automation.core.playlist_contract import parse_rows, assert_iptv_existing_rows_preserved
from automation.engines.international.candidate_engine import build_candidate as build_international_candidate, assert_international_rows_preserved
from automation.engines.iptv.candidate_engine import build_iptv_candidate
from automation.engines.international.engine import build_international_candidate
from automation.engines.epg.candidate_engine import build_epg_candidate
from automation.engines.epg.coverage import calculate_coverage
from automation.engines.epg.freshness import calculate_freshness
from automation.engines.epg.alias_suggestions import suggest_aliases

BASELINE_COMMIT = "46275f5ebafa2ae1b56f3e480f684ac1e85ae45e"
EXPECTED_BLOB_SHAS = {
    "IPTV-Playlist.m3u": "eb46b5ef4ddfde11a010389d1f0202a7bd418b0a",
    "International-Playlist.m3u": "c49c650d4e445620ae5fb91627eaa7f481ccea38",
    "epg/epg.xml": "b28414c75937bd155067c6db5e6e2083ee4004b4",
}

def git_blob_sha(path: Path) -> str:
    content = path.read_bytes()
    header = f"blob {len(content)}\0".encode("ascii")
    return hashlib.sha1(header + content).hexdigest()

def run(root: Path) -> dict:
    root = root.resolve()
    files = {name: root / name for name in EXPECTED_BLOB_SHAS}
    missing = [name for name,path in files.items() if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing baseline inputs: " + ", ".join(missing))
    actual_shas = {name:git_blob_sha(path) for name,path in files.items()}
    mismatches = [name for name,expected in EXPECTED_BLOB_SHAS.items() if actual_shas[name] != expected]
    if mismatches:
        raise ValueError("Production baseline blobs changed unexpectedly: " + ", ".join(mismatches))

    iptv_text = files["IPTV-Playlist.m3u"].read_text(encoding="utf-8-sig")
    international_text = files["International-Playlist.m3u"].read_text(encoding="utf-8-sig")
    epg_text = files["epg/epg.xml"].read_text(encoding="utf-8-sig")
    iptv_rows = parse_rows(iptv_text)
    international_rows = parse_rows(international_text)

    iptv_result = build_iptv_candidate(iptv_text,[],[],root)
    iptv_candidate = iptv_result.text
    assert_iptv_existing_rows_preserved(iptv_text,iptv_candidate)
    if iptv_candidate != iptv_text or iptv_result.publish:
        raise ValueError("empty IPTV engine dry run unexpectedly changed or published the playlist")

    international_result = build_international_candidate(international_text,[],datetime.now(ZoneInfo("Asia/Dhaka")).date())
    international_candidate = international_result.text
    assert_international_rows_preserved(international_text,international_candidate)
    if international_candidate != international_text or international_result.publish:
        raise ValueError("empty International engine dry run unexpectedly changed or published the playlist")

    epg_iptv_result = build_epg_candidate(iptv_text,epg_text,as_of=datetime.now(ZoneInfo("Asia/Dhaka")))
    epg_international_result = build_epg_candidate(international_text,epg_text,as_of=datetime.now(ZoneInfo("Asia/Dhaka")))
    if not epg_iptv_result.decision.accepted or not epg_international_result.decision.accepted:
        raise ValueError("baseline EPG candidate failed its coverage/freshness gate")
    if epg_iptv_result.xml_text != epg_text or epg_international_result.xml_text != epg_text:
        raise ValueError("empty EPG dry run unexpectedly changed the guide")
    if epg_iptv_result.publish or epg_international_result.publish:
        raise ValueError("EPG dry run unexpectedly enabled publication")

    as_of = datetime.now(ZoneInfo("Asia/Dhaka"))
    iptv_coverage = calculate_coverage(iptv_text,epg_text)
    international_coverage = calculate_coverage(international_text,epg_text)
    iptv_freshness = calculate_freshness(iptv_text,epg_text,as_of)
    international_freshness = calculate_freshness(international_text,epg_text,as_of)
    iptv_alias_suggestions = suggest_aliases(iptv_text,epg_text)
    international_alias_suggestions = suggest_aliases(international_text,epg_text)

    return {
        "schema_version":1,
        "baseline_commit":BASELINE_COMMIT,
        "baseline_blob_shas":actual_shas,
        "iptv_rows":len(iptv_rows),
        "international_rows":len(international_rows),
        "epg_bytes":files["epg/epg.xml"].stat().st_size,
        "iptv_epg_coverage":{
            "active_ids":iptv_coverage.active_channel_ids,
            "mapped_ids":iptv_coverage.mapped_channel_ids,
            "scheduled_ids":iptv_coverage.scheduled_channel_ids,
            "unmapped_ids":list(iptv_coverage.unmapped_ids),
            "mapped_without_schedule":list(iptv_coverage.mapped_without_schedule),
        },
        "international_epg_coverage":{
            "active_ids":international_coverage.active_channel_ids,
            "mapped_ids":international_coverage.mapped_channel_ids,
            "scheduled_ids":international_coverage.scheduled_channel_ids,
            "unmapped_ids":list(international_coverage.unmapped_ids),
            "mapped_without_schedule":list(international_coverage.mapped_without_schedule),
        },
        "iptv_epg_freshness":{
            "fresh_scheduled_ids":list(iptv_freshness.fresh_scheduled_channel_ids),
            "stale_only_ids":list(iptv_freshness.stale_only_channel_ids),
            "no_schedule_ids":list(iptv_freshness.no_schedule_channel_ids),
            "future_programme_count":iptv_freshness.future_programme_count,
        },
        "international_epg_freshness":{
            "fresh_scheduled_ids":list(international_freshness.fresh_scheduled_channel_ids),
            "stale_only_ids":list(international_freshness.stale_only_channel_ids),
            "no_schedule_ids":list(international_freshness.no_schedule_channel_ids),
            "future_programme_count":international_freshness.future_programme_count,
        },
        "iptv_epg_alias_suggestions":iptv_alias_suggestions,
        "international_epg_alias_suggestions":international_alias_suggestions,
        "candidate_playlist_changes":0,
        "candidate_epg_changes":0,
        "engine_validation":{
            "iptv":{"accepted":True,"baseline_rows":iptv_result.baseline_rows,"candidate_rows":iptv_result.candidate_rows,"publish":iptv_result.publish},
            "international":{"accepted":True,"baseline_rows":international_result.baseline_rows,"candidate_rows":international_result.candidate_rows,"publish":international_result.publish},
            "epg_iptv":{"accepted":epg_iptv_result.decision.accepted,"publish":epg_iptv_result.publish},
            "epg_international":{"accepted":epg_international_result.decision.accepted,"publish":epg_international_result.publish},
        },
        "publish":False,
        "production_files_modified":False,
    }

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path("."))
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=run(args.root)
    rendered=json.dumps(report,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(rendered,encoding="utf-8")
    else:
        print(rendered,end="")
    print(f"Baseline dry run: IPTV {report['iptv_rows']} rows; International {report['international_rows']} rows; EPG {report['epg_bytes']} bytes; production files unchanged; publish=false",flush=True)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
