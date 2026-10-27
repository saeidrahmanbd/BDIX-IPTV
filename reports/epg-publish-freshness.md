# EPG Publish Freshness Check

Generated: **2026-10-27**

## Status: PENDING — first successful EPG refresh required

The refresh pipeline is enabled, but `epg/epg.xml` is not present in the current `main` branch. A freshness PASS cannot be asserted until a non-empty XMLTV guide is generated, validated, and committed. This is a pending status note, not a successful freshness check.

The next **Refresh IPTV EPG** run should replace this note with measured freshness and quality results. If the guide is still missing afterward, inspect that workflow's source-fetch and publication-gate logs.
