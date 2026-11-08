# Manual maintenance tools

These scripts are intentionally kept as operator-run utilities. They are not scheduled workflows and must not be added to automatic playlist maintenance without a separate review.

Run commands from the repository root after creating a Git backup or working on a clean feature branch. Do not run them while a GitHub Actions workflow is writing the same files.

## Approved logo asset repair

`python scripts/repair_approved_logos_20261107.py`

This one-off tool downloads the specifically reviewed source artwork for three previously audited logo defects, writes local files under `logos/`, and generates `reports/logo-repair-2026-11-07.md`. Review the source URLs and resulting image dimensions before committing. It is not a general-purpose logo updater.

## IPTV playlist quality repair

`python scripts/repair_playlist_quality.py`

This deterministic repair operates only on `IPTV-Playlist.m3u`. It can modify group assignments and fill missing identity metadata for a fixed set of previously audited records. It does not run automatically. Inspect `git diff -- IPTV-Playlist.m3u` immediately afterward and run the full playlist tests and pre-publish gate before committing. Never use it as a substitute for reviewing a proposed channel change.

## Xtream EPG map synchronization

`python scripts/sync_epg_worker_map.py`

This utility reads `reports/epg-channel-mapping.csv` and updates a static `EPG_ID_MAP` only in Workers that implement that map. The current `xtream-main/worker.js` passes the playlist `tvg-id` directly to the shared published XMLTV guide and does not need a static map; the script should therefore report that synchronization was skipped. Do not add a redundant static map merely to make this utility modify a file.

## General safety

- These utilities preserve their one-off/manual status unless a reviewed workflow explicitly requires them.
- Never commit private upstream credentials, personalized source URLs or tokens.
- Keep local logo references only; do not replace authentic channel artwork with generated placeholders.
- Preserve primary channel streams and protected Backup/Review/Not Playing queues.
- Run the applicable test suite and validators after any utility changes.
