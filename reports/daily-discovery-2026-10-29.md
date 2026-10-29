# Daily IPTV Discovery — 2026-10-29

- **Run timestamp:** 2026-10-29T01:32:59Z
- **Status:** PARTIAL / BLOCKED — structural checks and targeted cleanup completed; a fresh source scan with live stream probes could not be confirmed for this automation attempt.
- **Report freshness:** The published IPTV report timestamped 01:17 UTC and International report timestamped 01:00 UTC are treated as historical runs, not as this run's discovery result.
- **New candidates accepted in this run:** 0. No unverified stream was added.

## IPTV-Playlist.m3u

### Discovery outcome
- No new channel or backup addition is claimed for this automation attempt.
- The previous 01:17 UTC probe report recorded two primary candidates — Star Sports 2 Hindi (HTTP 404) and VCV (HTTP 404) — and 16 backup candidates removed because they were dead or could not be verified (HTTP 403/404 or connection errors). Those are rejected historical candidates, not additions from this run.
- Two discovery-queue entries currently have no authentic local logo available; their logo attributes remain blank rather than using an external or placeholder logo.

### Targeted change
- Moved the existing **Not Playing** block before **New Channels → New Backup → Backup**.
- Updated the Playlist Studio category registry and normalization/hardening order so future maintenance keeps the two discovery groups immediately before Backup.
- Tightened final validation to require these to be the final three playlist groups.

### Current structural validation
- EXTINF entries: **1,159**
- URL lines: **1,159**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URLs: **0**
- Final groups: **New Channels → New Backup → Backup**
- External/non-repository logo URLs in maintained discovery entries: **0**
- Geography/content checks: prior 01:17 UTC report passed; stream probes were not repeated in this structural-only pass.

## International-Playlist.m3u

### Discovery outcome
- No new channel or backup addition is claimed for this automation attempt.
- The published scan timestamped 01:00 UTC is historical and stated that playback was not tested; it is not presented as a current verified discovery result.

### Targeted cleanup
Removed **14 radio/non-TV entries** from the discovery queue because radio-only services do not qualify as live music/movie TV channels:
- Los Angeles TV Radio
- Radio Bonita 106.7
- Radio Chisinau
- Radio Colmenar 92.5 FM
- Radio Cuenca Estéreo
- Radio Discount TV
- Radio Ideal
- Radio Moldova Muzical
- Radio Monumental TV
- Radio San Cristóbal 88.7 FM
- Radio SWH TV
- Radio Tele Hit
- Today Radio
- VoiceOver Radio TV

No other International playlist entries were changed by this cleanup.

### Current structural validation
- EXTINF entries: **3,258**
- URL lines: **3,258**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URLs: **0**
- Final groups: **New Channels → New Backup → Backup**
- Discovery-queue entries: **135 New Channels, 10 New Backup**
- Discovery entries missing a logo: **0**
- External/non-repository logo URLs in discovery entries: **0**
- Discovery-queue `tvg-content` values outside Movie/Music: **0**
- Radio/non-TV names remaining in discovery queues: **0**

## Blockers and next step

The connected GitHub tools can read and commit repository files but do not expose a direct workflow-dispatch or current workflow-run listing action in this session, and the local execution environment cannot reach stream hosts for live probes. A validator change was committed to trigger the repository workflows, but no completed fresh workflow report was observable by this timestamp. Do not treat either older discovery report as the result of this run; accept additions only after the repository workflow produces a new timestamped report with live stream verification and final validation.
