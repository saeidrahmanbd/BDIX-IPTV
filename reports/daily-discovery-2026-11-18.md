# Daily Discovery Report — 2026-11-18

Generated: **2026-11-18 06:56:27 Asia/Dhaka** (**2026-11-18T00:56:27Z**)

**Run status: BLOCKED — no fresh discovery scan or stream-probe run was executed.**

This is a new blocker report for 18 November, not a reused discovery result. No candidate list was fetched or evaluated in this run, so zero additions must not be interpreted as a finding that no eligible channels exist.

## Scope

- `IPTV-Playlist.m3u` — Bangladesh/India discovery and backup queues.
- `International-Playlist.m3u` — worldwide Music/Movie-only discovery and backup queues.

## Fresh discovery outcome

| Result | IPTV | International |
|---|---:|---:|
| Candidate scan | Not run | Not run |
| Stream probes | Not run | Not run |
| New Channels added | 0 | 0 |
| New Backup added | 0 | 0 |
| Candidate rejections | Not evaluated | Not evaluated |
| Playlist writes | None | None |

No additions are claimed. Existing playlist contents were not changed.

## GitHub Actions freshness

The repository Actions history was checked through **2026-11-18T00:56Z**. No run for either `IPTV New Channel Discovery` or `International Channel Discovery` was present for Bangladesh date 18 November.

The latest discovery report files are historical:
- IPTV report generated **2026-11-17T04:56:19Z**.
- International report last scanned **2026-11-17 10:29 UTC**.

They were not used as today's result.

## Current playlist baseline

### IPTV-Playlist.m3u

- Entries: **1,352**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URLs: **0**
- Entries in `New Channels`: **0**
- Entries in `New Backup`: **0**
- Current category registry ends with `Backup`, `Review`; it does not include the two required discovery groups.
- Current group sequence ends with `Backup` → `Review`, not `New Channels` → `New Backup` → `Backup`.
- Logo attributes: **1,352 external HTTP(S) URLs**, **0 local `logos/` paths**.

### International-Playlist.m3u

- Entries: **3,251**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URLs: **0**
- Entries in `New Channels`: **0**
- Entries in `New Backup` / `New Backups`: **0**
- Category registry uses the plural label `New Backups`.
- Actual entry group sequence ends with `Backup` → `Documentary & Wildlife` → `Religious`; the discovery queues are not at the end of the playlist.
- Logo attributes: **2,887 external HTTP(S) URLs**, **0 local `logos/` paths**, **364 entries without a logo**.

The M3U pair and duplicate-URL checks pass on the current snapshots. Required discovery-queue placement and the requested local-path logo convention do not pass the baseline audit.

## Blocking policy/workflow mismatches

1. **IPTV religious-channel rule:** `scripts/discover_bd_in_new_queues.py` currently treats Indian religious channels as prohibited even when Islamic. Its religious pattern includes Islamic markers. Your current rule excludes non-Islamic religious channels, so Islamic channels must not be rejected solely for being religious.
2. **International genre rule:** `scripts/discover_international_channels.py` currently returns Bangladesh and Pakistan candidates without a Movie/Music restriction and applies the separate India regional policy. That can admit non-Movie/Music candidates from those countries into discovery queues, contrary to your worldwide Music/Movie-only rule.
3. **Existing-content preservation:** the International workflow runs `scripts/reorganize_international_playlist.py`, which can reclassify, reorder, migrate and remove existing entries. It is not safe to run under the current instruction to preserve unrelated existing entries without first narrowing that step.
4. **Logo representation:** both discovery implementations use raw GitHub HTTP(S) logo URLs and their validators accept those URLs. Your current requirement is local `/logos/` assets with no external `tvg-logo` URL.
5. **Queue labels and order:** the International workflow uses `New Backups` (plural), while the requested label is `New Backup`. The IPTV insertion order also places discovery groups after `Backup` and leaves `Review` after them, rather than keeping both discovery groups immediately before `Backup`.

The available GitHub connection did not expose a direct workflow-dispatch action. I did not substitute a push-triggered workflow-file edit because the current workflows would execute the policy and preservation mismatches listed above.

## Required correction before a safe fresh run

- Align both discovery policies with the current rules.
- Change both queue labels and ordering to `New Channels` → `New Backup` → `Backup`.
- Make discovery logos use verified local `logos/` paths and update validators accordingly.
- Restrict International discovery to Movies/Music for every country, while preserving existing Fashion TV entries.
- Remove or narrow the International whole-playlist reorganization step so discovery cannot broadly reclassify or delete unrelated existing entries.
- Then dispatch both workflows, probe candidates, validate the targeted changes, and publish a fresh result report.

**Final status:** no playlist changes, no candidates added or rejected, and no stream probes. The run is blocked pending the policy/workflow corrections above.
