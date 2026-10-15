# Backup Orphan Audit

Generated: **Pending maintenance refresh**

An orphan is a Backup route whose exact channel ID and normalized name do not match any primary entry in IPTV-Playlist.m3u. This is a candidate list, not proof that the stream is unusable or that a similarly named service is equivalent. No Backup entries are deleted by this audit.

## Summary

- Primary entries checked: **635**
- Backup routes checked: **408**
- Orphan Backup routes: **20**
- Distinct orphan channel labels: **17**

| Channel label | Channel ID (if present) | Stream host | Source line |
|---|---|---|---:|
| Al Jazeera | missing | unknown | 1312 |
| BBC News | missing | unknown | 1414 |
| BTV National | missing | unknown | 1445 |
| Channel 16 | custom.channel.16 | unknown | 1462 |
| Colors | Colors.in | unknown | 1494 |
| Darshana TV | DarshanaTV.in@SD | unknown | 1530 |
| Discovery | missing | unknown | 1585 |
| Duronto TV | DurontoTV.bd | unknown | 1589 |
| Duronto TV | DurontoTV.bd | unknown | 1591 |
| Duronto TV | missing | unknown | 1593 |
| Duronto TV | missing | unknown | 1595 |
| DW News | missing | unknown | 1597 |
| Nick | missing | unknown | 1869 |
| Nick Jr | missing | unknown | 1871 |
| Sonic | missing | unknown | 1987 |
| Star Bharat | missing | unknown | 2014 |
| Star Gold | missing | unknown | 2016 |
| Star Movies | missing | unknown | 2024 |
| Super Hungama | missing | unknown | 2032 |
| ZB Cartoon | ZBCartoon.in | unknown | 2062 |

## Action

Review orphan routes before deleting or promoting them. The automated audit intentionally keeps orphan routes available for human review.
