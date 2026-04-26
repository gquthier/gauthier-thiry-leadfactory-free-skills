# Public Meta Ads Library Workflow

This workflow is no-key and public-only. It must not use paid scraping APIs, private MCP servers, fake accounts, credentials, or platform bypasses.

## Sources

Preferred:
- Public Meta Ads Library search pages: `https://www.facebook.com/ads/library/`
- Public ad detail URLs shared by the user.
- Public landing pages linked from ads.

Fallback:
- User screenshots.
- Pasted ad text.
- Public social posts and public landing pages when the ad cards are not accessible.

Always label the extraction mode in `analysis.md`:
- `direct_public_library`
- `user_provided_public_urls`
- `screenshot_or_paste_fallback`
- `public_assets_fallback`

## CSV Schema

Use these exact columns:

```csv
competitor,page_name,ad_library_url,ad_id,format,angle,hook,primary_text,headline,cta,start_date,last_seen,days_active,winner,countries,platforms,media_type,landing_url,source_mode,notes
```

Field guidance:
- `format`: `Static`, `Video`, `Carousel`, `UGC`, `FaceCam`, `LeadForm`, `Other`.
- `angle`: `Douleur`, `Desir`, `Preuve`, `ContreIntuitif`, `Urgence`, `Educatif`, `Comparaison`, `Autorite`, `Transformation`.
- `winner`: `true` if the ad appears active for more than 21 days or is repeatedly used; otherwise `false` or blank if unknown.
- `source_mode`: one of the extraction modes above.
- Leave unknown fields blank instead of inventing data.

## Extraction Steps

For each competitor:

1. Search the brand/page name in Meta Ads Library.
2. Filter by geography when possible.
3. Capture 10-30 public ads if visible.
4. For each ad, extract visible text, CTA, start date, platforms, destination URL, and visible format.
5. Categorize the angle from the hook and promise.
6. Add a row to `data.csv`.
7. Visit public landing pages only when needed to understand the funnel.

Do not download or redistribute media unless the user owns it or explicitly confirms public reuse rights. It is enough to describe format and visible creative pattern.

## Analysis Structure

Write `analysis.md` with:

1. Extraction scope and mode.
2. Total ads/assets analyzed.
3. Competitor-by-competitor summary.
4. Distribution by angle and format.
5. Top hooks.
6. Top CTAs.
7. Saturated angles.
8. White spaces.
9. Strategy recommendations for the user's offer.
10. Limitations and what should be manually verified before launch.

## Ethics

Do not recommend copying competitor ads verbatim. Use competitor data to identify patterns, gaps, and positioning opportunities.
