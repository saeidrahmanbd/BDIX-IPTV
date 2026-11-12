# BDIX-IPTV Operational Wiki

The root [README](../README.md) is the project overview. This page records the current multi-country playlist policies and automation boundaries.

## Maintained playlists

- [IPTV-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) — the owner-curated main collection, including Bangladesh, Indian categories, Pakistani, International and other genre/country groups.
- [International-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) — the automation-managed companion collection, including Bangladesh and India under their applicable rules, plus eligible movie and music channels from Pakistan and other countries.

## Automation permissions

### IPTV-Playlist.m3u — owner-curated and manually checked

The owner remains responsible for the final channel selection and manual review. Automation may only perform the following maintenance:

- Correct channel names, IDs, country/language metadata and other metadata when supported by reliable evidence.
- Repair missing or invalid logo references using verified, authentic repository-local assets under `/logos/`; never invent or substitute unrelated logos.
- Improve EPG identity mappings and report schedule gaps. The dedicated EPG workflow owns XMLTV generation/publication.
- Discover eligible Bangladesh/India channels and alternate streams into the manual `New Channels` and `New Backups` queues. These queues remain for owner approval; candidates are not automatically promoted.
- Keep every existing row's `group-title`, `tvg-chno`, category placement and relative order unchanged. New discoveries may be added only to `New Channels` / `New Backups`; they are never promoted automatically.
- Probe streams and identify broken, blocked, restricted, fragile or inconclusive endpoints for owner review. Blocking/access restrictions are diagnostic only and never authorize deletion or URL replacement.

Automation must not make channel-selection decisions for the owner:

- Never delete an existing channel/stream row or automatically retire a channel after failed probes.
- Never replace an existing stream URL, promote/demote an existing Backup or Review entry, or automatically migrate entries out of `New Channels` / `New Backups`.
- A stream failure, authentication block, geo-restriction, rate limit or transient network problem is diagnostic information—not authorization to delete or silently replace the stream.
- Do not alter `Adult` entries or guess country/genre metadata when evidence is ambiguous.

Metadata/logo repairs are allowed, but every existing stream URL, group assignment, channel number and relative row order must remain unchanged. New discovery entries are permitted only in the manual New Channels/New Backups queues. Stream blocking/health results for this playlist are advisory and never trigger deletion or URL replacement; the three-day retirement rule applies only to International-Playlist.m3u.

### International-Playlist.m3u — automation-controlled

Daily automation manages the International playlist end to end:

- Maintain channel metadata, authentic local logos, EPG mappings and correct country/genre grouping.
- Probe all stream entries and retain a consecutive Bangladesh-calendar-day failure history.
- On the first definitive failure, move the stream to `Review`. Remove it only after **three consecutive Bangladesh calendar days** of definitive failure.
- A missed calendar day restarts the failure streak. Inconclusive results—including authentication, rate-limit and geo-restriction responses—do not count as definitive failures and cannot authorize deletion.
- Re-test `Review` entries. A working entry that still satisfies the regional/genre policy must be restored to its correct primary group. When that channel identity already has a primary stream, place the recovered alternate in `Backup`. Keep failed, ambiguous or policy-ineligible entries in `Review`.
- A dedicated country group requires at least **five unique primary channel identities**. Backup alternates and Review rows do not count. Bangladesh and India retain their established fixed groups; Pakistan and every other country-specific group follow the five-identity threshold. Below the threshold, eligible rows stay in `International`.
- Reorganize and validate the playlist under the current regional policy while preserving protected `Adult`, `Review`, `New Channels` and `New Backups` rules.

A single failed probe, an inconclusive response or a runner-wide reachability incident must never cause stream removal. The health batch safety gate must block publication when results indicate a global network anomaly.

## Current channel eligibility

| Origin / collection | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---|---|
| Bangladesh | Eligible; owner-curated | All genres are eligible |
| India | News, religious (including Islamic), educational, business/finance and farming are prohibited. Kids and sports—including cricket and football—are allowed. | Same Indian exclusions; kids and sports are allowed |
| Pakistan | Supported only where explicitly accepted by the main playlist's manual curation | Eligible under Pakistan's unrestricted country policy |
| Other countries | Existing owner-curated entries remain subject to manual selection | Only dedicated Movie and Music channels are eligible |

The main playlist's source scope for new discovery is Bangladesh and India. Its New Channels/New Backups queues exist for manual owner review. The International discovery workflow accepts Bangladesh and Pakistan under their unrestricted country rules, India under its regional exclusions, and Movie/Music-only candidates from other countries.

## Grouping and Review rules

- The International country-group threshold is five **unique primary identities**, not five stream URLs. Backup and Review entries are excluded from the count.
- Working and policy-eligible International Review entries are migrated automatically: to the correct primary group for a new identity, or to Backup when a primary identity already exists.
- Failed, ambiguous or policy-ineligible International entries stay in Review; only definitive failures on three consecutive Bangladesh calendar dates are removed.
- Main-playlist Review, Backup, New Channels and New Backups remain under owner control and are never automatically promoted or removed.
- `Review`, `New Channels` and `New Backups` are excluded from Xtream. Adult entries remain protected.

## Metadata, logos and EPG

Keep channel IDs, names, logo paths, country, language, group, channel number and displayed name consistent. Do not invent channel IDs or assign a logo merely because a filename looks similar. Published playlists use repository-local logo files under `/logos/`; only verified identity matches are accepted.

The all-playlist EPG mapping registry is `reports/epg-channel-mapping.csv`. The EPG refresh workflow audits both maintained playlists and publishes the public guide to `epg/epg.xml) only after source, freshness and quality checks pass. The last-known-good guide is protected from empty, stale or degraded publication. Adult-group rows are excluded from the public mapping report.

## Daily automation schedule

All times below are Bangladesh time (`Asia/Dhaka`):

| Workflow | Schedule | Scope |
|---|---:|---|
| IPTV Playlist Update / maintenance | 07:00 | IPTV: metadata/logo repair only, preserving existing rows; International: full policy-based maintenance and reorganization |
| Playlist Logo Repair and Localization | 08:00 | Authentic local logos for both playlists |
| International Stream Health | 08:45 | Stream probes, Review recovery and three-day retirement for International only |
| Refresh IPTV EPG | 09:00 | EPG mapping audit and XMLTV publication for both playlists |

GitHub may delay scheduled Actions. A workflow's configured schedule is not proof that a run completed; verify the run status and freshness of its output reports.

## Operations and reports

Reports are generated snapshots, not live status pages. Check the generation timestamp and source fingerprint before relying on them.

- [IPTV playlist audit](../reports/iptv-playlist-audit.md)
- [International stream health](../reports/international-stream-health.md)
- [Stream health](../reports/stream-health.md)
- [Backup independence](../reports/backup-independence-audit.md)
- [Maintenance report](../reports/maintenance-report.md)
- [Update report](../reports/Update%20Report.md)
- [Stream risk review](../reports/stream-risk-review.md)
- [Project dashboard](../assets/dashboard.svg)

For an EPG gap, verify both the channel identity and whether a usable matching schedule source exists. A correctly formatted channel ID does not prove that programme data is available.

## Related documentation

- [Multi-country IPTV playlist guide](PLAYLISTS.md)
- [Download Center](DOWNLOADS.md)
- [Playlist Studio guide](PLAYLIST-STUDIO.md)
- [Xtream Gateway](../xtream/README.md)
- [Playlist Automation Policy](PLAYLIST-AUTOMATION-POLICY.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

Report broken streams, incorrect metadata or missing logos via [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues). Never include credentials, private tokens or private provider URLs in public issues.
