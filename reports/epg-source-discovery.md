# EPG Source Discovery — Unmapped Channels

Reviewed: 2026-10-14

## Current coverage gap

The last completed repository audit reported 255 unmapped active channel IDs: 63 in Bangladesh, 13 in Pakistani, and 62 in International. These are active unique IDs across the two published playlists.

## Bangladesh

No current, maintained, machine-readable XMLTV source was verified for the remaining domestic Bangladesh channels in the public source catalogue reviewed.

The official [Bangladesh Television daily programme schedule](https://btv.gov.bd/site/page/6bc2fea7-2a61-4479-9e6e-1811d0e0a9ec/-%E0%A6%A6%E0%A7%88%E0%A6%A8%E0%A6%BF%E0%A6%95-%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE%E0%A6%A8%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A6%BF) lists its last update as 11 August 2025. The weekly schedule archive was also last updated in August 2025. These archives are too stale to treat as a current 2026 guide.

Domestic IDs such as ATN Bangla, Jamuna TV, Channel 24, NTV and BTV National remain unmapped until current schedule data can be verified. A live stream or a similarly named foreign listing is not sufficient evidence.

## Pakistan

- [HUM TV official schedule](https://hum.tv/schedule/) lists named programmes and weekly airtimes, including an advertised 24-hour schedule view. It is an HTML source, not an XMLTV feed. It may support a future, tightly scoped HTML-to-XMLTV adapter after its timetable structure and rights to republish are reviewed, but it has not been inserted as an automated feed in this change.
- [HUM Sitaray schedule](https://humsitaray.tv/schedule/) did not establish a complete timed broadcast grid in the page content reviewed.
- [Discover Pakistan official website](https://www.discoverpakistan.tv/) presents its live broadcast and programme catalogue but did not expose a verified current machine-readable timed schedule in the content reviewed.
- The EPGShare public directory lists `epg_ripper_PK1.xml.gz` at only 310 bytes, which is not a usable current schedule feed for these channels.
- Open-EPG's currently displayed public guide list states that a source merge is underway and does not list a current Pakistan guide. An older indexed search result for `pakistan4.xml.gz` was therefore not treated as a reliable live feed.

No Pakistan-local IDs were mapped to UK/US diaspora schedules or based on unverified numeric ID guesses. This intentionally keeps the mapping coverage conservative.

## International

The iptv-org EPG project is a source scraper/catalogue, not itself a guarantee that every source has a directly hosted XMLTV output. Its current [GUIDES.md](https://github.com/iptv-org/epg/blob/master/GUIDES.md) lists only user-maintained guide hosts; the per-source StreamingTVGuides XML URL considered during research could not be verified as a currently published feed. That URL and its candidate aliases were removed from the automation rather than risking a dead source or false coverage gains.

The channel catalogue can confirm that source adapters know about channel names, but that alone does not provide retrievable schedules. Remaining international IDs should be mapped only when a live XMLTV feed or official time grid is validated for the same regional channel version.

## Verification policy

The next maintenance run should continue using the synchronized sources in `scripts/epg_coverage.py` and `scripts/generate_epg.py`. A candidate is eligible only if the feed is reachable, the exact channel identity matches, and it contains valid current/future programmes in the expected time window. `epg/README.md` also retains the warning that public accessibility does not automatically grant public redistribution rights.

Source references: [iptv-org EPG guides list](https://github.com/iptv-org/epg/blob/master/GUIDES.md), [iptv-org source catalogue](https://github.com/iptv-org/epg/blob/master/SITES.md), [Open-EPG guide status](https://www.open-epg.com/app/epgguide.php), [EPGShare directory](https://epgshare01.online/epgshare01/), and the official broadcaster pages linked above.
