# EPG Source Discovery — Unmapped Channels

Generated: 2026-10-14

## Scope

The last completed audit found 255 unmapped active channel identities: 63 in Bangladesh, 13 in Pakistani, and 62 in International. Counts describe active unique `tvg-id` values across the two published playlist files and will be refreshed by the maintenance workflow.

## Source added

Added the iptv-org-generated [StreamingTVGuides XMLTV feed](https://iptv-org.github.io/epg/sites/streamingtvguides.com/streamingtvguides.com.xml) to the mapping analyser and XMLTV generator.

The upstream channel catalogue exposes these exact US/international identities:

| Playlist ID | Exact upstream channel | Source ID |
|---|---|---|
| `Circle.us` | Circle | `CIRCLE` |
| `custom.epix.tv` | EPIX HD | `EPIXHD` |
| `MBCDramaUSA.us` | MBC Drama HD | `MBCDRHD` |

The feed is allowlisted to these three identities. The workflow must confirm that each mapping has current/future programme entries before counting it as covered. The source is not permitted to fuzzy-match other channel names.

## Bangladesh

No maintained machine-readable XMLTV source could be verified for the remaining domestic Bangladesh identities in the public source catalogue reviewed.

The official [Bangladesh Television daily programme schedule](https://btv.gov.bd/site/page/6bc2fea7-2a61-4479-9e6e-1811d0e0a9ec/-%E0%A6%A6%E0%A7%88%E0%A6%A8%E0%A6%BF%E0%A6%95-%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE%E0%A6%A8%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A6%BF) was last updated 11 August 2025 in the page metadata reviewed. That is stale for a current 2026 guide, so it is not being republished as current data.

Domestic identities such as ATN Bangla, Jamuna TV, Channel 24, NTV, BTV National and others remain unmapped unless a source can establish both channel identity and up-to-date airtimes. Similar channel names, a live stream, or a stale programme archive are not enough.

## Pakistan

- [HUM TV official schedule](https://hum.tv/schedule/) publishes selected named shows and primetime airtimes. It is an HTML page, not an XMLTV feed, and does not establish a complete daily guide for all hours.
- [HUM Sitaray schedule page](https://humsitaray.tv/schedule/) lists programme/episode information but did not establish a complete timed broadcast grid in the reviewed page.
- [Discover Pakistan official website](https://www.discoverpakistan.tv/) presents its live broadcast and programme catalogue but did not expose a verified current machine-readable timed schedule in the reviewed page.

The above pages are useful official references but are not currently used to generate a full EPG. No schedule has been inferred from programme titles alone, and the Pakistan-local channel IDs are not mapped to diaspora variants such as UK/US listings.

## International

The new feed is a targeted supplement only. The other remaining international IDs require exact source identity plus usable current/future programme data in the correct regional market. Name similarity alone does not qualify.

## Rights and validation

The existing rights caution in `epg/README.md` remains: public accessibility and an upstream scraper licence do not by themselves confirm permission for public redistribution. The new feed is a candidate data source; the maintenance run must test whether it is reachable and whether its exact mapped IDs carry schedules.

Sources reviewed: [iptv-org EPG source catalogue](https://github.com/iptv-org/epg/blob/master/SITES.md), [StreamingTVGuides channel catalogue](https://github.com/iptv-org/epg/blob/master/sites/streamingtvguides.com/streamingtvguides.com.channels.xml), and the official broadcaster pages linked above.
