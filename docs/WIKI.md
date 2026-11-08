# BDIX-IPTV Operational Wiki

The root [README](../README.md) is the project overview. This page records the current **multi-country IPTV M3U playlist policies** so that documentation and automation use the same rules.

## Maintained playlists

- [IPTV-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) — the broad, multi-country main collection, including Bangladesh, Indian categories, Pakistani, International and other genre/country groups. It is not limited to Bangladesh and India.
- [International-Playlist.m3u](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u) — a companion collection containing Bangladesh and India under their applicable rules, plus eligible movie and music channels from Pakistan and other countries.

## Current channel eligibility

| Origin / collection | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---|---|
| Bangladesh | All genres are eligible. | All genres are eligible. |
| India | News, all religious channels (including Islamic), educational, business/finance and farming channels are prohibited. Kids and sports are allowed. | Same Indian exclusions; kids and sports are allowed. |
| Pakistan | Supported in the Pakistani group. News, religious, educational, business/finance, farming, kids and sports channels are prohibited. The Indian kids and sports exception does not apply. | Eligible dedicated movie and music channels. |
| Other countries | Eligible channels may appear in International or qualified country groups, subject to the established genre rules. | Only dedicated movie and music channels are eligible. |

The main playlist's multi-country scope is distinct from the source scope of any individual discovery workflow. The International discovery workflow is specifically limited to eligible movie/music candidates from Pakistan and other countries; it must not stage non-Bangladesh/India news, sports, religious, kids, educational, documentary, radio, VOD or general-entertainment channels as eligible movie/music candidates. A country-specific group for other countries requires at least five unique, manually curated primary channel identities.

## Review and automatic discovery queues

- **Review** is the manual-check queue for unresolved, questionable or quarantined entries. It is not an automatic discovery destination. Keep its entries available for the owner's inspection; do not silently promote them into curated groups.
- **New Channels** is automatically populated by the scheduled Bangladesh/India discovery workflow. The first validated stream for a genuinely new channel identity is added here.
- **New Backups** is automatically populated by the same discovery workflow. Additional validated stream URLs for an existing or newly discovered identity are added here.
- The discovery workflow runs daily at **07:00 Asia/Dhaka** and can also be started manually. Automatic discovery only collects and validates candidates; it does not approve or promote them into curated groups. Manual review is required before promotion.
- **Review**, **New Channels** and **New Backups** are unnumbered and excluded from Xtream. Their entries do not count toward the five-channel country-group threshold.
- Existing **Backup** records are alternate streams linked to a primary channel identity. Do not delete them solely because a probe is inconclusive; only explicitly owner-authorized removals may be deleted.
- Keep uncertain stream checks available for manual review; remove only duplicates, clearly invalid/non-TV sources, explicitly prohibited candidates, unsafe proxy/tokenized links or definitively dead endpoints under the workflow's validation rules.

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

- [Multi-country IPTV playlist guide](PLAYLISTS.md)
- [Download Center](DOWNLOADS.md)
- [Playlist Studio guide](PLAYLIST-STUDIO.md)
- [Xtream Gateway](../xtream/README.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

Report broken streams, incorrect metadata or missing logos via [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues). Never include credentials, private tokens or private provider URLs in public issues.
