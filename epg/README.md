# EPG setup status

This is a prepared, inactive pilot. No live programme guide has been generated or published.

Four real Dish TV catalogue mappings were verified against iptv-org/epg at commit `335458005387e07417a98399eb423c78d62a3bd9`: Zee Bangla, Star Jalsha, Jalsha Movies and Sun Bangla. Their XMLTV output IDs match this repository's existing playlist IDs, so their backups can share the same guide. The pilot uses SD listings; regional/feed equivalence must be confirmed before activation. These are Indian Bangla channels, not Bangladesh channel coverage.

Catalogue evidence: https://github.com/iptv-org/epg/blob/335458005387e07417a98399eb423c78d62a3bd9/sites/dishtv.in/dishtv.in.channels.xml

Programme-data access and redistribution rights have NOT been established. The generator's software licence does not provide those rights. Do not mark the policy approved without provider terms or written permission supporting this use.

## Activation after source approval

1. Obtain terms or written permission covering automated schedule retrieval and public XMLTV redistribution. If using a different approved provider, replace the mappings with that provider's real mappings.
2. Record that evidence in `epg/source-policy.json`, confirm the selected feeds, and set the three approval fields to true only where supported.
3. In repository Settings → Secrets and variables → Actions → Variables, add `EPG_ENABLED` with value `true`.
4. Run Actions → Generate EPG → Run workflow.
5. Only a valid guide with future programmes for all mapped channels will be published. Successful publication adds the actual guide URL to the playlist header. The existing updater has been changed to preserve that header.

The guide will then be available at https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg.xml.gz. That URL is a future output location, not a working feed today.

The workflow is scheduled for 03:00 UTC (09:00 Bangladesh time), but stays inactive without `EPG_ENABLED`. Empty, stale, partial or malformed guides fail validation instead of replacing an existing guide. No empty guide is supplied with this setup.
