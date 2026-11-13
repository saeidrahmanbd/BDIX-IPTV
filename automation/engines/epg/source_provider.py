"""Isolated EPG source acquisition using the repository's tested generator.

The generator runs in a temporary workspace populated with read-only snapshots of
both playlists, the approved mapping file, and the last-known-good guide. It
cannot write the checked-out production paths.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

MAX_CANDIDATE_BYTES = 250 * 1024 * 1024
DEFAULT_TIMEOUT_SECONDS = 20 * 60


def build_epg_source_candidate(repository_root: str | Path,
                               timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
                               max_workers: int = 8,
                               iptv_playlist_text: str | None = None,
                               international_playlist_text: str | None = None) -> str:
    """Generate a candidate XMLTV file in an isolated temporary workspace."""
    if timeout_seconds < 60 or timeout_seconds > 60 * 60:
        raise ValueError("EPG source timeout must be between 60 and 3600 seconds")
    if max_workers < 1 or max_workers > 16:
        raise ValueError("EPG source workers must be between 1 and 16")

    root = Path(repository_root).resolve()
    required = (
        root / "scripts" / "generate_epg.py",
        root / "scripts" / "epg_source_cache.py",
        root / "scripts" / "epg_mapping_policy.py",
        root / "scripts" / "official_epg_sources.py",
        root / "reports" / "epg-channel-mapping.csv",
        root / "IPTV-Playlist.m3u",
        root / "International-Playlist.m3u",
        root / "epg" / "epg.xml",
    )
    missing = [str(path.relative_to(root)) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError("EPG candidate inputs are missing: " + ", ".join(missing))

    with tempfile.TemporaryDirectory(prefix="bdix-epg-v2-") as temp_name:
        workspace = Path(temp_name)
        shutil.copytree(root / "scripts", workspace / "scripts")
        (workspace / "reports").mkdir()
        (workspace / "epg").mkdir()
        for relative in (
            "IPTV-Playlist.m3u",
            "International-Playlist.m3u",
            "reports/epg-channel-mapping.csv",
            "epg/epg.xml",
        ):
            destination = workspace / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if relative == "IPTV-Playlist.m3u" and iptv_playlist_text is not None:
                destination.write_text(iptv_playlist_text, encoding="utf-8")
            elif relative == "International-Playlist.m3u" and international_playlist_text is not None:
                destination.write_text(international_playlist_text, encoding="utf-8")
            else:
                shutil.copy2(root / relative, destination)

        runner = workspace / "run_epg_candidate.py"
        runner.write_text(
            "from pathlib import Path\n"
            "import sys\n"
            "sys.path.insert(0, str(Path('scripts').resolve()))\n"
            "import generate_epg\n"
            "generate_epg.PLAYLISTS = [Path('IPTV-Playlist.m3u'), Path('International-Playlist.m3u')]\n"
            "generate_epg.MAPPING = Path('reports/epg-channel-mapping.csv')\n"
            "generate_epg.OUTPUT = Path('epg/epg.xml')\n"
            f"generate_epg.SOURCE_FETCH_WORKERS = {max_workers}\n"
            "generate_epg.main()\n",
            encoding="utf-8",
        )
        environment = os.environ.copy()
        environment["EPG_SOURCE_CACHE_DIR"] = str(workspace / "source-cache")
        environment["EPG_SOURCE_CACHE_TTL_SECONDS"] = "0"
        try:
            subprocess.run(
                [sys.executable, str(runner)],
                cwd=workspace,
                env=environment,
                check=True,
                timeout=timeout_seconds,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("isolated EPG source acquisition timed out; production guide was not changed") from exc
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                "isolated EPG source acquisition failed; production guide was not changed "
                f"(exit code {exc.returncode})"
            ) from exc

        candidate_path = workspace / "epg" / "epg.xml"
        if not candidate_path.is_file():
            raise RuntimeError("EPG generator produced no candidate file")
        size = candidate_path.stat().st_size
        if size <= 0 or size > MAX_CANDIDATE_BYTES:
            raise RuntimeError("EPG candidate is empty or exceeds the 250 MiB safety limit")
        return candidate_path.read_text(encoding="utf-8")
