# Backup Orphan Audit

Generated: **2026-10-15T00:00:00Z**

An orphan is a Backup route whose channel ID and normalized channel name both fail to match a primary record in `IPTV-Playlist.m3u`. This is a conservative candidate audit: aliases may need manual review. No backup streams are removed automatically.

## Summary

- Primary entries checked: **635**
- Backup routes checked: **408**
- Orphan Backup routes: **20**
- Distinct orphan channel labels: **17**

| Channel label | Channel ID | Stream host | Source line |
|---|---|---|---:|
| Al Jazeera | missing | unknown | 1310 |
| BBC News | missing | unknown | 1412 |
| BTV National | missing | unknown | 1443 |
| Channel 16 | custom.channel.16 | unknown | 1460 |
| Colors | Colors.in | unknown | 1492 |
| Darshana TV | DarshanaTV.in@SD | unknown | 1528 |
| Discovery | missing | unknown | 1583 |
| Duronto TV | DurontoTV.bd | unknown | 1587 |
| Duronto TV | missing | unknown | 1589 |
| Duronto TV | DurontoTV.bd | unknown | 1591 |
| Duronto TV | missing | unknown | 1593 |
| DW News | missing | unknown | 1595 |
| Nick | missing | unknown | 1867 |
| Nick Jr | missing | unknown | 1869 |
| Sonic | missing | unknown | 1985 |
| Star Bharat | missing | unknown | 2012 |
| Star Gold | missing | unknown | 2014 |
| Star Movies | missing | unknown | 2022 |
| Super Hungama | missing | unknown | 2030 |
| ZB Cartoon | ZBCartoon.in | unknown | 2062 |

## Review note

Check whether each item is an intentional standalone channel or a mislabeled alternate before removing it. This report does not make playback-health claims.
