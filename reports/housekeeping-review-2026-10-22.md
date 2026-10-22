# Repository Housekeeping Review — 2026-10-22

## Unreferenced scripts

The following scripts were identified for review because repository searches did not find a caller/reference:

- `enhance_bd_epg.py`
- `final_iptv_playlist_fixes.py`
- `generate_metadata_backfill_report.py`
- `run_epg_coverage.py`
- `validate_local_logos.py`

**Action:** no deletion in this PR. These files are preserved pending explicit approval and a fuller dependency review.

## Test CI

The metadata validation workflow previously ran targeted `unittest` commands but did not invoke `pytest`. This PR adds a `pytest` installation step and a final `pytest -q tests` run.

## EPG documentation

`epg/README.md` previously described the mapping/coverage pipeline as auditing two published playlists. It now documents all three published playlists: `BDIX-Playlist.m3u`, `IPTV-Playlist.m3u`, and `International-Playlist.m3u`.

## Stream URL placeholders

The following were intentionally not changed because they are part of stream URLs and the maintenance rules require approval before modifying them:

- `?token=test`
- `auth=testpub`
- unresolved `{TC_STRING}`
- `{APP_NAME}` / `{APP_DOMAIN}` macros

No stream URL was edited, reordered, evaluated, or removed by this PR.

## Metadata/playlist changes deferred

Playlist metadata changes and cross-playlist field propagation require a complete current working copy so that every affected EXTINF entry can be rewritten without changing any stream URL. They are therefore explicitly deferred rather than reconstructed from partial API output.

## Logo provenance

Generated-fallback logo enforcement was added to `scripts/pre_publish_gate.py`. Active channels marked `generated_fallback` in `reports/logo-authenticity-manifest.json` now block publication instead of being silently treated as a clean logo state.
