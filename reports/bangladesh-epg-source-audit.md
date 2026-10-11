# Bangladesh EPG Source Audit

Checked: **2026-10-11**
Scope: public XMLTV feeds and channel-ID catalogues for the Bangladesh-group channels in IPTV-Playlist.m3u, BDIX-Playlist.m3u, and NVisionBD-Playlist.m3u.

## Result

**No reliable Bangladesh-domestic XMLTV feed was verified in the public sources checked.** However, one actively published schedule source provides exact programme data for the UK-specific channel **ATN Bangla UK**, and this exact match has now been added for `ATNBanglaUK.uk` only. No local `.bd` IDs were mapped, playlist IDs were not altered, and no programme data was synthesized.

This is a negative finding for the sources checked, not proof that no private or broadcaster-internal feed exists.

## Source checks

| Source | Result | Decision |
|---|---|---|
| [epg.pw XMLTV guide catalogue](https://epg.pw/xmltv.html?lang=en) | The published country-feed list includes a range of country feeds (including India) but no Bangladesh feed. | No Bangladesh feed to add. |
| [epgshare01 directory](https://epgshare01.online/epgshare01/) and its [source-ID readme](https://epgshare01.online/epgshare01/0_READ_ME_FIRST_AS_I_CONTAIN_VERY_HELPFUL_INFO.html) | The directory publishes per-source `.xml.gz` files and matching `.txt` channel-ID lists. No dedicated `epg_ripper_BD1`/Bangladesh feed was found. The combined catalogue did not contain exact native IDs such as `ATNBangla.bd`, `ChannelI.bd`, `NTV.bd`, `JamunaTV.bd`, or `SomoyNewsTV.bd`. | Do not map native Bangladesh IDs from Indian or diaspora lookalikes. The all-sources archive is very large and is not a safe substitute for an exact source. |
| [iptv-org/epg source catalogue](https://github.com/iptv-org/epg/tree/master/sites) and [guide status list](https://github.com/iptv-org/epg/blob/master/GUIDES.md) | No live public Bangladesh-local guide was verified. Some stale source configuration mentions Canadian service variants; the matching CA1 listing endpoint currently returns 404. | Treat CA1 entries as leads only, not an active feed. |
| [nasimali/epg-auto guide (published XMLTV)](https://raw.githubusercontent.com/nasimali/epg-auto/release/main-epg/epg_data/merged_epg.xml) and [Sky XMLTV channel-ID catalogue](https://github.com/WiiLink24/tv-epg/blob/3a119500bdb1cb31f739afce0851527707d60733/sites/sky.com/sky.com.channels.xml) | The published merged guide currently contains `<channel id="6753">` and programme rows; the Sky catalogue independently identifies site ID `6753` as `ATNBanglaUK.uk` / “ATN Bangla UK”. This guide is configured in the repository's source list already. | **Verified narrow mapping:** `ATNBanglaUK.uk` → source EPG ID `6753`. Do not use it for `ATNBangla.bd`. |

## Exact IDs found in a currently listed diaspora feed

The current [epgshare01 ASIANTELEVISION1 ID list](https://epgshare01.online/epgshare01/epg_ripper_ASIANTELEVISION1.txt) is dated `202610110538` and lists these exact XMLTV channel IDs:

| XMLTV channel ID | Catalogue label/context | Possible playlist counterpart | Status |
|---|---|---|---|
| `ATN.Bangla.ca` | ATN Bangla, Canada service/feed | `ATNBangla.bd` | **Unverified equivalent** — do not map automatically. |
| `Channel.I.Bangla.ca` | Channel I Bangla, Canada service/feed | `ChannelI.bd` | **Unverified equivalent** — do not map automatically. |
| `ATN.Colors.Bangla.ca` | ATN Colors Bangla | None; this is not the native Bangladesh ATN Bangla service | **Exclude**. |

The same-name Canadian services may have different schedules, regional inserts, or time alignment. An ID's presence in a catalogue proves only that the source identifies a channel; it does **not** prove that its programmes and start times match the Bangladesh-local stream. The feed's ID catalogue was checked, but its programme rows were not independently compared against a broadcaster-published Bangladesh schedule. These two candidates are therefore not counted as verified mappings.

### Stale CA1 leads (not accepted)

The [iptv-org/epg CA1 channel configuration](https://github.com/iptv-org/epg/blob/master/sites/epgshare01.online/epgshare01.online_CA1.channels.xml) contains scraper-specific identifiers:
- `CA1#Channel.i.(Bangladesh).ca`
- `CA1#ATN.-.Bangla.ca`
- `CA1#NTV.Bangla.ca`

These are source/site identifiers, not verified native `.bd` IDs; the corresponding `epg_ripper_CA1.txt` endpoint returned 404 during this check. They are excluded from eligible sources until a live feed and current programme data can be verified.

The active `nasimali/epg-auto` guide supplies numeric ID `3914` with programme rows for Iqra Bangla; the existing repository lock `IqraBangla.uk` → `3914` remains scoped to the UK service. The published guide also includes `6753` for ATN Bangla UK. These diaspora mappings do not establish coverage for the domestic `ATNBangla.bd`, `NTV.bd`, or other `.bd` IDs.

## Playlist channel identities to preserve

The three playlists already use native/custom identities such as `ATNBangla.bd`, `ATNNews.bd`, `BanglaVision.bd`, `BTVNational.bd`, `Channel24.bd`, `ChannelI.bd`, `DBCNews.bd`, `DeeptoTV.bd`, `EkattorTV.bd`, `JamunaTV.bd`, `MaasrangaTV.bd`, `NTV.bd`, `News24.bd`, `RTV.bd`, `SATV.bd`, and `SomoyNewsTV.bd`. These playlist IDs should remain unchanged unless a verified source supplies programme data for the exact same channel/service.

## Acceptance rules for future discoveries

A feed can be promoted to the production source list only after all of the following are demonstrated:

1. The source URL responds with valid XMLTV and contains real `<programme>` rows, not only channel declarations.
2. The exact source channel ID is present in the XMLTV `<channel id>` set and has current/future programmes.
3. Several programme titles and start/end times match an official broadcaster schedule or a trusted local schedule for the same Bangladesh service.
4. The time zone and any regional/time-shift version are accounted for.
5. The match is added as a narrow, explicit mapping; no fuzzy-name or India-channel fallback is used.

## Implemented exact mapping

| Playlist ID | XMLTV source ID | Evidence | Scope |
|---|---|---|---|
| `ATNBanglaUK.uk` | `6753` | Active merged XMLTV has programme rows for 6753; Sky channel catalogue identifies 6753 as ATN Bangla UK. | UK service only |
| `IqraBangla.uk` | `3914` | Active merged XMLTV has programme rows for 3914; current repository lock already uses this exact source ID. | UK service only |

The merged XMLTV file uses generic display-name values such as `Channel 6753`; the identification is confirmed against the separate Sky channel catalogue rather than inferred from that placeholder display-name. Some other IDs in the feed have conflicting or commented-out mappings in public catalogues (for example 5426 and 3815), so they were deliberately **not** applied.

Until a genuinely local source is found, native Bangladesh channel guide coverage should remain reported as missing rather than being filled with guessed or mismatched programmes.
