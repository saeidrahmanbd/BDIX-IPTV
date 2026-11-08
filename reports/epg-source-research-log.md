# EPG Source Research Log — Blocked

Generated: **2026-11-08 (session date, UTC; probes run after the inventory step)**

Status: **BLOCKED — no source was reached, tested, or verified.** No XMLTV source is recorded as useful, no mapping was added or changed, and no channel was verified against any feed.

## Attempts

| URL | Method | Result |
|---|---|---|
| https://epgshare01.online/epgshare01/epg_ripper_BD1.xml.gz | curl HEAD | No HTTP response (000) |
| https://iptv-epg.org/files/epg-bd.xml.gz | curl HEAD | No HTTP response (000). Proxy status check: `CONNECT tunnel failed, response 403` |
| https://iptv-epg.org/files/epg-in.xml.gz | curl HEAD | No HTTP response (000) |
| https://i.mjh.nz/SamsungTVPlus/us.xml | curl HEAD | No HTTP response (000) |
| https://www.open-epg.com/files/india.xml.gz | curl HEAD | No HTTP response (000) |
| https://raw.githubusercontent.com/iptv-org/epg/master/README.md | curl HEAD | No HTTP response (000) |
| https://iptv-epg.org/files/epg-bd.xml.gz | WebFetch | Rejected: URL not on the session allowlist. Not retried. |

## Limitations

- Outbound HTTPS to the EPG source hosts is blocked by the sandbox egress policy. The proxy returns 403 on CONNECT for these hosts.
- The WebFetch allowlist does not include the EPG source hosts.
- Nothing was downloaded, parsed, or matched. Channel-ID matches, schedule coverage, timestamp offsets, title quality and licensing are all **not assessed**.
- Source discovery must be run from an environment with outbound access, using the scripts listed in reports/epg-research-inventory.md.
