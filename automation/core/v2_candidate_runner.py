"""Read-only production candidate pipeline for the three Automation V2 engines."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import hashlib
import json
import os
from pathlib import Path
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

from automation.core.candidate_manifest import CandidateManifest
from automation.core.run_ledger import RunRequest
from automation.core.github_state_store import execute_remote_run
from automation.core.transaction_gate import ArtifactEvidence
from automation.core.transaction_staging import stage_transaction_bundle
from automation.core.playlist_contract import parse_rows, assert_iptv_existing_rows_preserved
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



def _assert_current_main_head(expected_commit: str) -> None:
    """Fail closed if the remote main branch moved away from this candidate baseline."""
    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()
    required = os.environ.get("AUTOMATION_V2_REQUIRE_REMOTE_HEAD_CHECK") == "1"
    if not required:
        # Unit tests and local dry runs may omit credentials. The production
        # shadow workflow explicitly enables this mandatory remote check.
        return
    if not repository:
        raise RuntimeError("GITHUB_REPOSITORY is required to verify the current main baseline")
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required to verify the current main baseline")
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/git/ref/heads/main",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "BDIX-IPTV-AutomationV2",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, urllib.error.HTTPError) as exc:
        raise RuntimeError("unable to verify current main baseline; refusing to stage candidates") from exc
    obj = payload.get("object") if isinstance(payload, dict) else None
    actual = obj.get("sha") if isinstance(obj, dict) else None
    if (
        not isinstance(actual, str)
        or len(actual) not in (40, 64)
        or any(char not in "0123456789abcdefABCDEF" for char in actual)
    ):
        raise RuntimeError("GitHub returned an invalid main branch head")
    if actual.lower() != expected_commit.lower():
        raise RuntimeError(
            f"main advanced during candidate generation (expected {expected_commit}, current {actual})"
        )

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
        _assert_current_main_head(baseline_commit)
        print("V2 bundle: reservation acquired; production baselines captured.", flush=True)
        snapshot = store.load()
        iptv_run = run_iptv_discovery(iptv_baseline, root, today)
        print(
            f"V2 bundle: IPTV candidate ready ({iptv_run.candidate.candidate_rows} rows; "
            f"{len(iptv_run.source_warnings)} source warnings).",
            flush=True,
        )
        iptv_candidate = iptv_run.candidate.text
        if iptv_run.publish:
            raise RuntimeError("IPTV candidate engine unexpectedly enabled publication")
        parse_rows(iptv_candidate)
        assert_iptv_existing_rows_preserved(iptv_baseline, iptv_candidate)

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
        print(
            f"V2 bundle: International candidate ready ({intl_run.maintenance.candidate.candidate_rows} rows; "
            f"{intl_run.maintenance.probed_count} probed; {intl_run.maintenance.reused_count} reused).",
            flush=True,
        )
        if intl_run.publish or intl_run.maintenance.publish:
            raise RuntimeError("International candidate engine unexpectedly enabled publication")
        parse_rows(international_candidate)
        assert_international_existing_rows_preserved(
            international_baseline, international_candidate,
            allowed_removed_identities=intl_run.maintenance.candidate.plan.remove_identities,
        )

        # Persist completed dated probes before the slower EPG source stage. If EPG
        # acquisition fails or the runner is interrupted later, the day's probes
        # remain available to the next disposable Actions runner.
        updated_state = dict(snapshot.state)
        updated_state["international_probe_ledger"] = parse_ledger(intl_run.maintenance.ledger_json)
        store.save(updated_state, snapshot.blob_sha)
        print("V2 bundle: International probe history checkpointed to durable state.", flush=True)

        print("V2 bundle: starting isolated EPG source acquisition.", flush=True)
        source_candidate = build_epg_source_candidate(
            root,
            timeout_seconds=epg_timeout_seconds,
            iptv_playlist_text=iptv_candidate,
            international_playlist_text=international_candidate,
        )
        print(f"V2 bundle: EPG source candidate acquired ({len(source_candidate.encode('utf-8'))} bytes).", flush=True)
        active_candidate_playlists = iptv_candidate + "\n" + international_candidate
        epg_run = build_epg_candidate(
            active_candidate_playlists,
            epg_baseline,
            source_candidate,
            approved_aliases=None,
            as_of=datetime.now(ZoneInfo("Asia/Dhaka")),
        )
        if not epg_run.decision.accepted:
            raise ValueError("EPG candidate rejected: " + epg_run.decision.reason)
        if epg_run.publish:
            raise RuntimeError("EPG candidate engine unexpectedly enabled publication")
        print("V2 bundle: EPG candidate passed validation and coverage gates.", flush=True)

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
        # The working-tree fingerprints protect against local writes; this remote
        # ref check also catches a concurrent push/merge to main while the run worked.
        _assert_current_main_head(baseline_commit)
        manifests = []
        artifacts = []
        for engine, path in (
            ("iptv", "IPTV-Playlist.m3u"),
            ("international", "International-Playlist.m3u"),
            ("epg", "epg/epg.xml"),
        ):
            baseline_digest = _sha(baseline_by_path[path])
            current_path = root / path
            if current_path.is_symlink() or not current_path.resolve().is_relative_to(root):
                raise RuntimeError(f"production baseline path is unsafe: {path}")
            current_digest = _sha(current_path.read_text(encoding="utf-8-sig" if path.endswith(".m3u") else "utf-8"))
            if current_digest != baseline_digest:
                raise RuntimeError(f"production baseline changed during candidate generation: {path}")
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
                baseline_current_sha256=current_digest,
                candidate_current_sha256=candidate_digest,
                validator_passed=True,
            ))

        transaction_digest = _sha("\0".join(
            [baseline_commit.lower(), *(contents[path] for path in sorted(contents))]
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

        print(f"V2 bundle: all candidates staged for owner review ({transaction_id}); publish=false.", flush=True)
        return CandidateBundleResult(
            transaction_id=transaction_id,
            transaction_path=str(staged_path),
            iptv_candidate_rows=iptv_run.candidate.candidate_rows,
            international_candidate_rows=intl_run.maintenance.candidate.candidate_rows,
            international_probed=intl_run.maintenance.probed_count,
            international_reused=intl_run.maintenance.reused_count,
            epg_programmes=len(ET.fromstring(epg_run.xml_text).findall("programme")),
            publish=False,
        )

    return execute_remote_run(store, request, operation)
