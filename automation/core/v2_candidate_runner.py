"""Read-only production candidate pipeline for the three Automation V2 engines."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

from automation.core.candidate_manifest import CandidateManifest
from automation.core.run_ledger import RunRequest
from automation.core.github_state_store import execute_remote_run
from automation.core.transaction_gate import ArtifactEvidence
from automation.core.transaction_staging import stage_transaction_bundle
from automation.engines.iptv.orchestrator import run_iptv_discovery
from automation.engines.international.discovery_orchestrator import run_international_discovery
from automation.engines.international.orchestrator import derive_primary_stream_targets
from automation.engines.international.probe_ledger import parse_ledger
from automation.engines.international.candidate_engine import assert_international_existing_rows_preserved
from automation.engines.epg.candidate_engine import build_epg_candidate
from automation.engines.epg.source_provider import build_epg_source_candidate


@dataclass(frozen=True)
class CandidateBundleResult:
    transaction_id: str
    transaction_path: str
    iptv_candidate_rows: int
    international_candidate_rows: int
    international_probed: int
    international_reused: int
    epg_programmes: int
    publish: bool = False


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run_candidate_bundle(repository_root: str | Path, today: date,
                         baseline_commit: str, store,
                         epg_timeout_seconds: int = 20 * 60,
                         probe_timeout_seconds: int = 8) -> tuple[object, CandidateBundleResult | None]:
    """Build, validate and atomically stage all three candidates; never publish production files."""
    root = Path(repository_root).resolve()
    iptv_path = root / "IPTV-Playlist.m3u"
    international_path = root / "International-Playlist.m3u"
    epg_path = root / "epg" / "epg.xml"
    for path in (iptv_path, international_path, epg_path):
        if not path.is_file():
            raise FileNotFoundError(f"required production baseline is missing: {path.name}")

    iptv_baseline = iptv_path.read_text(encoding="utf-8-sig")
    international_baseline = international_path.read_text(encoding="utf-8-sig")
    epg_baseline = epg_path.read_text(encoding="utf-8")
    baseline_fingerprint = _sha("\0".join((
        iptv_baseline, international_baseline, epg_baseline, baseline_commit
    )))
    request = RunRequest("bundle", today, baseline_commit, baseline_fingerprint)

    def operation():
        # Read the current remote state only after the bundle reservation is held.
        snapshot = store.load()
        iptv_run = run_iptv_discovery(iptv_baseline, root, today)
        iptv_candidate = iptv_run.candidate.text
        if iptv_run.publish:
            raise RuntimeError("IPTV candidate engine unexpectedly enabled publication")

        targets = derive_primary_stream_targets(international_baseline)
        intl_run = run_international_discovery(
            international_baseline,
            json.dumps(snapshot.state["international_probe_ledger"]),
            targets,
            today,
            root,
            timeout=probe_timeout_seconds,
        )
        international_candidate = intl_run.maintenance.candidate.text
        if intl_run.publish or intl_run.maintenance.publish:
            raise RuntimeError("International candidate engine unexpectedly enabled publication")
        assert_international_existing_rows_preserved(international_baseline, international_candidate)

        source_candidate = build_epg_source_candidate(
            root,
            timeout_seconds=epg_timeout_seconds,
            iptv_playlist_text=iptv_candidate,
            international_playlist_text=international_candidate,
        )
        active_candidate_playlists = iptv_candidate + "\n" + international_candidate
        epg_run = build_epg_candidate(
            active_candidate_playlists,
            epg_baseline,
            source_candidate,
            approved_aliases=None,
            as_of=datetime.now(ZoneInfo("Asia/Dhaka")),
        )
        if not epg_run.decision.accepted:
            raise ValueError("EPG candidate rejected: " + "; ".join(epg_run.decision.errors))
        if epg_run.publish:
            raise RuntimeError("EPG candidate engine unexpectedly enabled publication")

        contents = {
            "IPTV-Playlist.m3u": iptv_candidate,
            "International-Playlist.m3u": international_candidate,
            "epg/epg.xml": epg_run.xml_text,
        }
        baseline_by_path = {
            "IPTV-Playlist.m3u": iptv_baseline,
            "International-Playlist.m3u": international_baseline,
            "epg/epg.xml": epg_baseline,
        }
        manifests = []
        artifacts = []
        for engine, path in (
            ("iptv", "IPTV-Playlist.m3u"),
            ("international", "International-Playlist.m3u"),
            ("epg", "epg/epg.xml"),
        ):
            baseline_digest = _sha(baseline_by_path[path])
            candidate_digest = _sha(contents[path])
            manifests.append(CandidateManifest(
                engine=engine,
                baseline_commit=baseline_commit,
                changed_paths=(path,),
                candidate_fingerprints={path: candidate_digest},
            ))
            artifacts.append(ArtifactEvidence(
                path=path,
                baseline_sha256=baseline_digest,
                candidate_sha256=candidate_digest,
                baseline_current_sha256=baseline_digest,
                candidate_current_sha256=candidate_digest,
                validator_passed=True,
            ))

        transaction_digest = _sha("\0".join(
            contents[path] for path in sorted(contents)
        ))[:16]
        transaction_id = f"v2-{today.isoformat()}-{transaction_digest}"
        try:
            staged_path = stage_transaction_bundle(
                root, transaction_id, manifests, artifacts, contents, baseline_commit
            )
        except FileExistsError:
            # A previous attempt may have staged the exact same validated bundle
            # before a state-store outage. Reuse only an exact content match.
            staged_path = root / "reports" / "automation-v2" / "candidates" / "transactions" / transaction_id
            metadata = json.loads((staged_path / "transaction-bundle.json").read_text(encoding="utf-8"))
            expected = {path: _sha(value) for path, value in contents.items()}
            if metadata.get("candidate_fingerprints") != expected or metadata.get("baseline_commit") != baseline_commit:
                raise RuntimeError("existing staged transaction does not match this candidate bundle")

        updated = dict(snapshot.state)
        updated["international_probe_ledger"] = parse_ledger(intl_run.maintenance.ledger_json)
        store.save(updated, snapshot.blob_sha)

        return CandidateBundleResult(
            transaction_id=transaction_id,
            transaction_path=str(staged_path),
            iptv_candidate_rows=iptv_run.candidate.candidate_rows,
            international_candidate_rows=intl_run.maintenance.candidate.candidate_rows,
            international_probed=intl_run.maintenance.probed_count,
            international_reused=intl_run.maintenance.reused_count,
            epg_programmes=epg_run.decision.candidate_programmes,
            publish=False,
        )

    return execute_remote_run(store, request, operation)
