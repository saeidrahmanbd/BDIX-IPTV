# Multi-Country IPTV Playlists (M3U) — BDIX-IPTV

BDIX-IPTV is a public **multi-country IPTV M3U playlist** project with a strong Bangla TV collection. It maintains two M3U collections: a broad main playlist covering Bangladesh, India, Pakistan and eligible channels from other countries, plus a companion International playlist.

The playlist files can be added to an M3U-compatible player such as VLC, Kodi, TiviMate, XCIPTV or IPTV Smarters. This repository publishes playlist references and metadata; it does not host television channels or video.

## Download the playlists

### Multi-Country Main Playlist — IPTV-Playlist.m3u

**[Open the main multi-country IPTV playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u)**

Direct URL:

~~~text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
~~~

This is the primary, broad collection—not a Bangladesh-and-India-only playlist. It is organized into country and genre groups, including Bangladesh, Indian categories, the six-channel Fashion group, Pakistani, International, Documentary & Wildlife, Kids, Religious and Sports. Channel eligibility remains governed by the established country- and genre-specific rules.

### International — International-Playlist.m3u

**[Open the International IPTV playlist](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u)**

Direct URL:

~~~text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/International-Playlist.m3u
~~~

The companion International playlist includes Bangladesh and India under their applicable rules, plus eligible movie and music channels from Pakistan and other countries.

## Channel eligibility

| Origin / collection | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---|---|
| Bangladesh | Included; all genres are eligible. | Included; all genres are eligible. |
| India | Included; News, all religious channels (including Islamic), educational, business/finance and farming channels are excluded. Kids and sports are allowed. | Same Indian exclusions; kids and sports are allowed. |
| Pakistan | Supported in the Pakistani group. News, religious, educational, business/finance, farming, kids and sports channels are excluded. The Indian kids and sports exception does not apply. | Eligible dedicated movie and music channels. |
| Other countries | Eligible channels can appear in International or qualified country groups, subject to the established genre rules. | Only dedicated movie and music channels are eligible. |

Adult channels are not excluded by this policy; they are preserved in the Adult group of the International playlist. Clearly identified Adult channels stranded in Backup are restored to Adult during reorganization.

The main playlist has three distinct non-numbered queues:

- **Review** is reserved for unresolved or questionable entries that the owner wants to check manually.
- **New Channels** is populated automatically by the scheduled Bangladesh/India discovery workflow when it finds a first validated stream for a new channel identity.
- **New Backups** is populated automatically by that workflow when it finds another validated stream for an existing or newly discovered channel identity.

The Bangladesh/India discovery workflow runs daily at **07:00 Asia/Dhaka** and can be started manually. Discovery automatically adds candidates to New Channels/New Backups, but it does not approve or promote them into curated groups. Manual review is required before promotion. All three queues are excluded from Xtream and have no channel numbers. Every country except Bangladesh and India, including Pakistan, needs five unique primary channel identities before it receives a dedicated country group; eligible channels below the threshold remain in International. Backup alternates do not count, while an eligible orphan Backup row without a matching primary is promoted before threshold calculation.

## Add an M3U playlist to your player

1. Copy the M3U URL for the collection you want.
2. Open an M3U-compatible player such as VLC, Kodi, TiviMate, XCIPTV or IPTV Smarters.
3. Choose **Add playlist by URL** (the exact menu name varies by player).
4. Paste the URL, save and refresh the channel list.

## XMLTV EPG programme guide

The repository's XMLTV EPG endpoint is:

**[Open the BDIX-IPTV XMLTV guide](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml)**

The guide is refreshed and published after its generation, freshness and quality checks pass. Schedule coverage varies by channel and source availability.

## Discovery scope

The main playlist is multi-country, but individual discovery workflows can have narrower source-feed scopes. For example, the IPTV new-channel discovery workflow may scan selected Bangladesh and India feeds; this does not define or limit the country coverage of the curated main playlist. The International discovery workflow handles eligible movie/music candidates from other countries.

## About BDIX and stream availability

BDIX-IPTV is focused on Bangladesh and BDIX-related IPTV use cases, but the project does not claim that every listed stream is routed inside every ISP's BDIX network. Access, quality and availability depend on the individual provider, region, network route and player.

The repository does not host TV channels or video content. Users are responsible for complying with applicable laws, broadcaster rights, provider terms and local regulations.

## Project links

- [Main README and repository overview](../README.md)
- [International and IPTV playlist files](../README.md#playlists)
- [EPG documentation](../epg/README.md)
- [Download Center](DOWNLOADS.md)
- [GitHub repository](https://github.com/saeidrahmanbd/BDIX-IPTV)
- [Report an issue](https://github.com/saeidrahmanbd/BDIX-IPTV/issues)
