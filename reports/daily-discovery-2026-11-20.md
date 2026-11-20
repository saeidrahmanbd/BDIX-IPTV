# Daily IPTV Discovery Report — 2026-11-20

**Audit timestamp (Bangladesh):** 2026-11-20 08:02:54 +06:00  
**Repository:** [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)

## Overall result

Both daily discovery stages ran separately, used fresh source feeds, and completed successfully. The dated stage reports were regenerated during today's runs. A post-run strict audit corrected several IPTV queue candidates that the first validator had accepted using source-feed placement instead of explicit channel-country identity.

| Stage | Run | Run-time result | Fresh report |
|---|---|---|---|
| IPTV Bangladesh + India | [#339](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/44650091117) | Workflow success; 6 invalid queue rows removed, 1 unverified backup moved to Review | [IPTV report](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md) |
| International worldwide Movies/Music | [#323](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/44650091174) | Workflow success; 5 primary promotions, 11 verified backup promotions, 11 candidates held in Review | [International report](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/international-channel-discovery.md) |

## 1. IPTV-Playlist.m3u

**Fresh scan timestamp:** 2026-11-20 06:59:54 +06:00  
**Discovery commit:** [301937915e698ca615391750e695c08da0cba60c](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/301937915e698ca615391750e695c08da0cba60c)

### Discovery and stream checks

- Discovery found 27 primary candidates and 31 alternate-stream candidates.
- 836 candidates were rejected or held by the discovery filters.
- 58 candidate streams were probed: 42 returned live media responses, 12 were definitively dead and removed, and 4 were inconclusive.
- The initial run-time validator passed, but its country logic trusted source-feed placement even when the channel ID explicitly identified another country. A strict post-run audit corrected that defect.

### Strict post-run corrections

Removed these 6 newly staged rows:

1. BTL TV — Netherlands (country ID .nl)
2. Cartoon Network — Pakistan (country ID .pk)
4. Qello Concerts by Stingray — Canada (country ID .ca)
5. National Geographic — India; prohibited Knowledge genre
6. National Geographic Wild — India; prohibited Knowledge genre
7. Nick Jr. — India; prohibited Kids genre

Travelxp 4K HDR was an inconclusive alternate stream (HTTP 403), so it was moved from New Backups to Review with an explicit hold reason. It is not counted as a verified backup. Vokta TV remains in New Channels for manual review because its probe was inconclusive (HTTP 403).

### Final queue and validation state in the correction branch

- **New Channels:** 17 candidates, including 1 inconclusive primary candidate held for manual review.
- **New Backups:** 22 candidates; all 22 had verified live media responses.
- **Review hold:** 1 unverified alternate stream (Travelxp 4K HDR), moved out of New Backups after an inconclusive HTTP 403 probe.
- All 40 retained queue/hold logo references point to repository assets under /logos/; all referenced files were checked.
- tvg-country was normalized from recognized .bd/.in channel IDs on retained discovery rows.
- Discovery queue groups are adjacent in the required order: New Channels → New Backups → Backup. Both discovery queues are A–Z sorted.
- Playlist entries: 1,372.
- Malformed EXTINF/URL pairs: 0.
- Duplicate URL occurrences: 0.
- Queue country, local-logo path and placement checks: PASS.
- Existing non-discovery channel rows and stream URLs were preserved.

The logo-only repair for today's IPTV candidates is recorded in [commit ce16a8ea16ad234697c35a4307fda9210467ac65](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/ce16a8ea16ad234697c35a4307fda9210467ac65).

## 2. International-Playlist.m3u

**Fresh scan timestamp:** 2026-11-20 07:00:29 +06:00  
**Discovery commit:** [95b2f80368fc66394d2f098bf0735545c9895ef2](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/95b2f80368fc66394d2f098bf0735545c9895ef2)

### Discovery and stream checks

- Source records parsed: 12,396.
- New eligible source records after URL and worldwide Movies/Music policy filtering: 149.
- 50 primary candidates and 20 alternate streams were staged and probed.
- 70 streams were checked: 27 returned live media responses and 43 were definitively dead/invalid and removed.
- 5 verified primary channels were promoted into qualifying country groups.
- 11 verified alternate streams were moved to Backup.
- 11 candidates without authentic local logos were held in Review; they were not promoted into active discovery groups.
- No inconclusive stream was promoted.
- Run-time validation: 3,317 entries, 0 malformed EXTINF/URL pairs, 0 duplicate stream URLs, 0 non-local discovery logo references, and 0 geography/content-policy issues.

The subsequent logo-only repair commit [51d524c93016c89a6ec4d2ff5d7c576d16fd9474](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/51d524c93016c89a6ec4d2ff5d7c576d16fd9474) updated International playlist artwork without changing stream URLs. The 11 entries held in Review were not automatically promoted as a side effect.

## 3. Reliability and blockers

- Both independent GitHub discovery jobs completed successfully.
- A duplicate same-day trigger was skipped by the Bangladesh-date guard because today's successful runs had already completed; no duplicate discovery was forced.
- The IPTV country-identity and validator hardening, including the post-run playlist correction and tests, is being submitted separately so future runs reject explicit foreign channel IDs and do not leave inconclusive alternates in New Backups.
- Remaining manual-review items: Vokta TV (primary stream inconclusive in New Channels) and Travelxp 4K HDR (alternate stream inconclusive, held in Review). Playback probes establish HTTP/media-response status, not guaranteed playback in every country or player.

## Source reports

- [IPTV channel discovery report](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md)
- [International channel discovery report](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/international-channel-discovery.md)
