# BDIX-IPTV Search Visibility & SEO Tracking

This guide explains how to measure the site's search performance after the three landing pages have been published and indexed.

## Search Console property

Use the URL-prefix property:

`https://saeidrahmanbd.github.io/BDIX-IPTV/`

Open [Google Search Console](https://search.google.com/search-console) and select this property.

## 1. Monitor the Search results report

Open **Performance → Search results**.

For the first review, select **Last 28 days**. Once enough history has accumulated, compare the latest 28 days with the previous 28 days. Search Console reporting can take time to populate for newly indexed pages, so an initially empty report is not evidence of a technical failure.

Enable these four metrics:

- **Total clicks** — visits from Google Search.
- **Total impressions** — appearances in Google Search results.
- **Average CTR** — clicks divided by impressions.
- **Average position** — the average position of the topmost result from this property.

Review the **Queries** and **Pages** tabs separately. Use **Countries** to check Bangladesh and India, and **Devices** to compare mobile and desktop.

## 2. Query groups to monitor

These are topic groups to observe in actual Search Console data, not claims that the site currently ranks for them. Use the queries Google reports; do not add a phrase to a page simply because it appears in this list.

| Topic group | Example searches |
|---|---|
| Bangladeshi IPTV | `Bangladeshi IPTV`, `Bangladesh IPTV`, `BDIX IPTV` |
| Bangla IPTV | `Bangla IPTV`, `Bangla TV`, `Bangla IPTV M3U` |
| Playlist format | `Bangladesh IPTV M3U`, `M3U playlist Bangladesh` |
| International list | `International IPTV M3U`, `movie music IPTV playlist` |
| Bengali-language queries | `বাংলাদেশি আইপিটিভি`, `বাংলা আইপিটিভি`, `বাংলা টিভি প্লেলিস্ট` |

## 3. Review the three landing pages

Use the **Pages** tab to inspect each URL independently:

- `https://saeidrahmanbd.github.io/BDIX-IPTV/`
- `https://saeidrahmanbd.github.io/BDIX-IPTV/playlists.html`
- `https://saeidrahmanbd.github.io/BDIX-IPTV/bangla-iptv.html`

Look for:
- Pages receiving impressions but few clicks. Review the title and description for clarity and relevance.
- Queries that are relevant but lead to the wrong page. Improve internal links and page explanations.
- Pages with no impressions after a meaningful observation period. Recheck indexing, content usefulness, canonical URL and internal links.
- Queries that are unrelated to the actual project. Do not add irrelevant content to chase them.

Do not treat average position as a guaranteed ranking for every searcher. Results vary by query, location, device and time.

## 4. Indexing and sitemap checks

Open **Indexing → Pages** to review indexed and excluded URLs. Use URL Inspection for a specific page when a status needs investigation.

The current sitemap files are:
- `/sitemap.xml`
- `/sitemap.txt`

A sitemap submission error should be investigated separately from the index status of an individual page. Search Console can index a page discovered through links or other sources even when no referring sitemap is reported.

Avoid repeatedly requesting indexing for unchanged URLs. A request does not guarantee or force indexing.

## 5. Practical review cadence

| When | Review |
|---|---|
| After the first 2–4 weeks of meaningful search data | First baseline: queries, pages, impressions, clicks and CTR |
| Monthly | Compare the latest 28 days with the previous 28 days |
| After a major page update | Inspect the changed URL and request recrawl only when useful |
| Quarterly | Review whether page content still matches the playlist rules and user needs |

## 6. What to export for an SEO review

In Search Console, export the Search results report with:
- Date
- Query
- Page
- Country
- Device
- Clicks
- Impressions
- CTR
- Position

Share that export for a data-based review. It can show which real searches are generating visibility and which landing pages need improvement.

## Measurement limits

Search Console reports Google Search performance; it does not measure every search engine, private browsing query, playlist playback or channel viewing. Some queries are anonymized or omitted for privacy. A click to a playlist M3U file is not proof that a channel played successfully.

SEO changes can improve clarity and crawlability, but no title, keyword, schema type or sitemap can guarantee a particular ranking or a Google AI Overview citation.

## 7. Add Bing Webmaster Tools

Google indexing does not automatically confirm Bing indexing. Register the same project URL in [Bing Webmaster Tools](https://www.bing.com/webmasters/about).

The simplest route is to import the verified Google Search Console property:

1. Sign in to Bing Webmaster Tools with a Microsoft account.
2. Choose **Import from Google Search Console**.
3. Authorize the Google account that owns the verified `https://saeidrahmanbd.github.io/BDIX-IPTV/` property.
4. Select that URL-prefix property and complete the import.
5. Open the imported site in Bing Webmaster Tools and inspect the homepage, playlist guide and Bengali page.
6. Review **Search Performance**, **URL Inspection** and **Sitemaps** after Bing has collected data.

Bing documents the Search Console import option and automatic verification for successfully imported sites. It also supports XML and plain-text sitemap formats. See [Add and verify a site](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b) and [Bing Sitemaps](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed).

Do not assume a Google sitemap error will be resolved by Bing. Check Bing's own processing status and discovered URL count.

