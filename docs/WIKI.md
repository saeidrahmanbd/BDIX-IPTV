# Operational Wiki

The root [README.md](../README.md) is the canonical project overview, playlist catalogue, quick-start guide, and current status page. This Wiki retains operational policies and links rather than duplicating that overview.

## Playlist and discovery policy

- Three maintained playlists: [IPTV](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u), [BDIX](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u), and [International](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u).
- International country groups are for movie/music channels. Documentary & Wildlife, Kids, Sports, Religious, Adult, and the explicit Fashion TV exception remain in dedicated groups.
- Discovery queues are restricted to verified Bangladesh/India candidates. Bangladeshi news is allowed; Indian News and non-Islamic religious channels are prohibited; Indian Kids/Sports and Islamic religious channels are allowed.
- **Permanent denylist:** E-Vidya 4, 5, 6, 7, 8, 9, 10, 11, 12 and Friends TV.
- Country groups for discovery candidates are created only when there are at least five legitimate primary channel identities for that country; smaller sets remain in the review queue.
- `New Channels`, `New Backup`, `Backup` and `Not Playing` have separate purposes. The Xtream workers exclude `Test`, `Not Playing`, and the new discovery queues from service output.

## Metadata and logos

Keep `tvg-id`, `tvg-name`, `tvg-logo`, group, channel number and displayed name consistent. Do not fabricate channel IDs or attach an image just because its filename resembles a name. Use a repository-local logo only when the asset is a reasonable match; if identity cannot be verified, leave it for review.

The all-playlist EPG mapping registry is `reports/epg-channel-mapping.csv`. Adult-group rows are excluded from the public mapping report so that it does not publish named-performer inventory.

## EPG publication

The public XMLTV refresh pipeline is enabled again. The guide is published to `epg/epg.xml` after the scheduled workflow passes source-fetch, freshness and quality checks. The three playlist headers advertise the public raw XMLTV URL, and both Xtream `xmltv.php` handlers fetch that same guide. EPG.PW remains excluded, the personalized M3U4U endpoint is not included in the public build, and unresolved upstream source reviews remain documented in the [source-rights register](../epg/source-rights-register.csv).

See [EPG status and maintenance](../epg/README.md) and the [coverage report](../reports/epg-coverage.md).

## Operations and reports

Reports are snapshots, not live status pages. Check the generated timestamp and source fingerprint before relying on them.

- [IPTV playlist audit](../reports/iptv-playlist-audit.md)
- [Stream health](../reports/stream-health.md)
- [Backup independence](../reports/backup-independence-audit.md)
- [Maintenance report](../reports/maintenance-report.md)
- [Update report](../reports/Update%20Report.md)
- [Stream risk review](../reports/stream-risk-review.md)
- [Project dashboard](../assets/dashboard.svg)

For a missing programme guide, check whether EPG publication is enabled first, then verify the channel's ID and permission-approved schedule source. A correctly formatted ID is not proof that any schedule source exists.

## Related documentation

- [Downloads](DOWNLOADS.md)
- [Playlist Studio guide](PLAYLIST-STUDIO.md)
- [Xtream Gateway](../xtream/README.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

Report broken streams, wrong metadata or missing/incorrect logos via [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues). Do not include credentials, private tokens or private provider URLs in public issues.
