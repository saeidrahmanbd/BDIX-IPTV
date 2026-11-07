# BDIX-IPTV Operational Wiki

The root [README](../README.md) is the project overview. This page records the current **Bangladeshi IPTV, Bangla IPTV and International M3U playlist policies** so that documentation and automation use the same rules.

## Maintained playlists

- [IPTV-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) — Bangladesh and India channel collection.
- [International-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) — Bangladesh and India under the same rules, plus eligible international movie and music channels.

## Current channel eligibility

| Origin | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---|---|
| Bangladesh | All genres are eligible. | All genres are eligible. |
| India | News, all religious channels (including Islamic), educational and business/finance channels are prohibited. Kids and sports are allowed. | Same Indian exclusions; kids and sports are allowed. |
| Other countries | Not included. | Only dedicated movie and music channels are eligible. |

The International discovery workflow must not stage non-Bangladesh/India news, sports, religious, kids, educational, documentary, radio, VOD or general-entertainment channels as eligible movie/music candidates. A country-specific group for other countries requires at least five unique, manually curated primary channel identities.

## Discovery and manual review

- First-stream candidates for genuinely new channels are placed in **New Channels**.
- Alternate streams are placed in **New Backups**.
- Both groups are **manual-review queues**. Automation must not approve, promote or move candidates from these queues into curated groups.
- Queue entries do not count toward the five-channel country-group threshold.
- Keep uncertain stream checks available for manual review; remove only duplicates, clearly invalid/non-TV sources, explicitly prohibited candidates, unsafe proxy/tokenized links or definitively dead endpoints under the workflow's validation rules.
- Existing **Backup** and **Not Playing** records have separate preservation rules. Do not delete them solely because a probe is inconclusive.

## Metadata and logos

Keep channel IDs, names, logo paths, country, language, group, channel number and displayed name consistent. Do not invent channel IDs or assign a logo merely because a filename looks similar. Published playlists use repository-local logo files under /logos/; use an asset only when it is a reasonable identity match.

The all-playlist EPG mapping registry is reports/epg-channel-mapping.csv. Adult-group rows are excluded from the public mapping report to avoid publishing named-performer inventory.

## EPG publication

The public XMLTV refresh pipeline is enabled. A guide is published to epg/epg.xml after source-fetch, freshness and quality checks pass. The maintained playlist headers advertise the public raw XMLTV URL. The main Xtream worker serves the guide through its authenticated xmltv.php endpoint. Source-review metadata is advisory; source-specific restrictions and private credentials remain protected.

See [EPG status and maintenance](../epg/README.md) and the [EPG coverage report](../reports/epg-coverage.md).

## Operations and reports

Reports are generated snapshots, not live status pages. Check the generation timestamp and source fingerprint before relying on them.

- [IPTV playlist audit](../reports/iptv-playlist-audit.md)
- [Stream health](../reports/stream-health.md)
- [Backup independence](../reports/backup-independence-audit.md)
- [Maintenance report](../reports/maintenance-report.md)
- [Update report](../reports/Update%20Report.md)
- [Stream risk review](../reports/stream-risk-review.md)
- [Project dashboard](../assets/dashboard.svg)

For an EPG gap, verify both the channel identity and whether a usable matching schedule source exists. A correctly formatted channel ID does not prove that programme data is available.

## Related documentation

- [Bangladeshi IPTV playlist guide](PLAYLISTS.md)
- [Download Center](DOWNLOADS.md)
- [Playlist Studio guide](PLAYLIST-STUDIO.md)
- [Xtream Gateway](../xtream/README.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

Report broken streams, incorrect metadata or missing logos via [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues). Never include credentials, private tokens or private provider URLs in public issues.
