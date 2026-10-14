# EPG Source Discovery — Unmapped Channels

Reviewed: 2026-10-14

## New verified schedule adapter

Added a limited parser for the official [HUM TV Pakistan schedule](https://hum.tv/schedule/). It extracts only programme names with explicit airtimes from the weekly schedule and expands those published weekday/time slots to the next seven days. It omits image-only or unnamed slots. The official page's 24-hour view is divided into hourly slots, so the adapter uses one-hour windows; those stop times are derived from the hourly grid rather than printed individually.

The adapter applies only to the exact playlist identity `HumTV.pk`, not HUM World, HUM Europe, HUM Sitaray or other regional variants. The workflow must confirm that the page still exposes enough valid title/time pairs before the mapping counts as covered.

## Bangladesh

No current, maintained, machine-readable XMLTV source was verified for the remaining domestic Bangladesh channels in the public source catalogue reviewed.

The official [Bangladesh Television daily programme schedule](https://btv.gov.bd/site/page/6bc2fea7-2a61-4479-9e6e-1811d0e0a9ec/-%E0%A6%A6%E0%A7%88%E0%A6%A8%E0%A6%BF%E0%A6%95-%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE%E0%A6%A8%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A6%BF) lists its last update as 11 August 2025; the weekly schedule archive also shows its last update in August 2025. This is too stale for a current 2026 guide.

Domestic IDs such as ATN Bangla, Jamuna TV, Channel 24, NTV and BTV National remain unmapped until current schedule data can be verified. Similar names or a live stream do not establish programme airtimes.

## Pakistan

- The official HUM TV schedule is now used only for explicit title/time pairs on the Pakistan-local service; image-only slots are not guessed.
- [HUM Sitaray schedule](https://humsitaray.tv/schedule/) did not establish a complete timed broadcast grid in the page content reviewed.
- [Discover Pakistan official website](https://www.discoverpakistan.tv/) presents its live broadcast and programme catalogue but did not expose a verified current machine-readable timed schedule in the content reviewed.
- The EPGShare public directory lists `epg_ripper_PK1.xml.gz` at only 310 bytes, so it was not accepted as a usable schedule feed.
- The current [Open-EPG guide page](https://www.open-epg.com/app/epgguide.php) says a source merge is underway and does not list a current Pakistan guide; an older indexed result for `pakistan4.xml.gz` was not treated as a live source.

No Pakistan-local IDs are mapped to UK/US diaspora schedules or based on unverified numeric IDs.

## International

A channel catalogue or scraper configuration proves that a provider knows a channel name; it does not prove that a direct XMLTV feed is currently published. The iptv-org project's current [GUIDES.md](https://github.com/iptv-org/epg/blob/master/GUIDES.md) lists user-maintained guide hosts; the per-source StreamingTVGuides XML URL considered during research could not be verified as a live feed. It was removed from automation and its candidate aliases were removed.

The remaining international identities still require a directly reachable schedule feed whose programme data matches the exact regional channel version. No fuzzy mapping has been added from source catalogues alone.

## Rights and validation

The repository's existing rights notice remains: public accessibility does not automatically establish permission for public redistribution. The HUM TV page is an official schedule source, but its terms have not been verified as granting XMLTV redistribution rights. The adapter is deliberately limited to a small set of explicitly scheduled entries.

After the workflow completes, see [the EPG coverage report](epg-coverage.md) for the measured number of usable schedule slots and validation results.

Sources reviewed: [HUM TV schedule](https://hum.tv/schedule/), [Bangladesh Television daily schedule](https://btv.gov.bd/site/page/6bc2fea7-2a61-4479-9e6e-1811d0e0a9ec/-%E0%A6%A6%E0%A7%88%E0%A6%A8%E0%A6%BF%E0%A6%95-%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A6%BE%E0%A6%A8%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A6%BF), [Open-EPG guide status](https://www.open-epg.com/app/epgguide.php), [EPGShare directory](https://epgshare01.online/epgshare01/), and [iptv-org current guide list](https://github.com/iptv-org/epg/blob/master/GUIDES.md).
