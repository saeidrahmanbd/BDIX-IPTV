# Operational Wiki

The root [README.md](../README.md) is the canonical project overview, playlist catalogue, quick-start guide, and current status page. This Wiki retains operational policies and links rather than duplicating that overview.

## Playlist and discovery policy

- Two maintained playlists: [IPTV](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u) and [International](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u).
- `IPTV-Playlist.m3u` accepts only Bangladesh and India channels. Bangladesh follows its existing policy. Indian News, all Religious channels (including Islamic), Educational and Kids channels are prohibited; Indian Sports channels remain allowed.
- `International-Playlist.m3u` applies the same Bangladesh/India policy. Every other country, including Pakistan, is limited to dedicated Movie and Music channels; news, religious, educational, kids, sports, documentary/wildlife and general-entertainment channels are out of scope.
- `New Channels` and `New Backups` are manual-review queues in both playlists. First streams for newly discovered channels go in `New Channels`; alternate streams go in `New Backups`. Neither queue is promoted automatically, and queue entries do not count toward the five-channel country-group threshold.
- **Permanent denylist:** E-Vidya 4, 5, 6, 7, 8, 9, 10, 11, 12 and Friends TV.
- **Country-group threshold:** A country outside Bangladesh, India and Pakistan receives a dedicated group only when it has at least **five unique curated primary channel names** across eligible Movies/Music entries. Countries with 1–4 curated unique channels stay in `International`; when the fifth unique channel is present, eligible curated channels from that country are grouped together. Alternate stream URLs, duplicate names and `Backup`/review-queue rows do not count toward the threshold. The dedicated thematic groups remain separate and are never counted.
- `New Channels`, `New Backups`, `Backup` and `Not Playing` have separate purposes. The main Xtream worker excludes `Test`, `Not Playing`, and the new discovery queues from service output.

## Metadata and logos

Keep `tvg-id`, `tvg-name`, `tvg-logo`, group, channel number and displayed name consistent. Do not fabricate channel IDs or attach an image just because its filename resembles a name. Use a repository-local logo only when the asset is a reasonable match; if identity cannot be verified, leave it for review.

The all-playlist EPG mapping registry is `reports/epg-channel-mapping.csv`. Adult-group rows are excluded from the public mapping report so that it does not publish named-performer inventory.

## EPG publication

The public XMLTV refresh pipeline is enabled. The guide is published to `epg/epg.xml` after the scheduled workflow passes source-fetch, freshness and quality checks. Both maintained playlist headers advertise the public raw XMLTV URL. The main Xtream worker serves that guide through its authenticated `xmltv.php` endpoint. The EPG pipeline can combine useful public or otherwise accessible sources, including third-party feeds, for discovery, mapping and schedule acquisition. Private credentials and personalized feed URLs are kept out of the repository.

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

For a missing programme guide, check whether EPG publication is enabled first, then verify the channel's ID and an available matching schedule source. A correctly formatted ID is not proof that any schedule source exists.

## Related documentation

- [Downloads](DOWNLOADS.md)
- [Playlist Studio guide](PLAYLIST-STUDIO.md)
- [Xtream Gateway](../xtream/README.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

Report broken streams, wrong metadata or missing/incorrect logos via [GitHub Issues](https://github.com/saeidrahmanbd/BDIX-IPTV/issues). Do not include credentials, private tokens or private provider URLs in public issues.