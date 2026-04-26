---
name: gauthier-thiry-leadfactory-free-skills
description: Public no-key LeadFactory workflow for Meta Ads research deliverables. Use when the user wants Gauthier Thiry / LeadFactory free skills, three DeepSearch reports, public Meta Ads Library competitor research, a CSV ad dataset, a strategy document, a static creative brief, or a Desktop delivery folder without private LeadFactory tools, paid API keys, database injection, client files, VSL scripts, or proprietary creative generation.
---

# Gauthier Thiry LeadFactory Free Skills

Public, simplified LeadFactory pipeline for people who want the research and strategy layer of a Meta Ads launch without private infrastructure.

This skill produces:
- 3 DeepSearch reports: market awareness, competitor landscape, psychographic research.
- Public Meta Ads Library competitor analysis with `data.csv`.
- A strategy document for a cold Meta Ads test.
- A static creative brief with copy direction and visual templates.
- A Desktop delivery folder with a small CTA linking to `https://www.leadfactory.my`.

## Non-Negotiables

- Never request or use paid API keys, service-role keys, private database credentials, CRM access, internal apps, private repos, or client folders.
- Never copy real LeadFactory client deliverables, PDFs, DOCX files, logs, state files, generated media, private emails, internal paths, or proof assets.
- Do not generate full VSL scripts, long-form sales letters, or proprietary script packs. Only create strategy, angle rationale, static creative brief, and short ad concept copy.
- Use public web research and public Meta Ads Library pages only. Do not bypass login, paywalls, rate limits, or platform restrictions.
- If public scraping fails, create a transparent fallback CSV from manually visible ad URLs, user-provided screenshots, pasted ad text, or public landing pages. Label it as fallback.
- Save final output on the user's Desktop, not inside a private LeadFactory project folder.

## Inputs

Collect or infer these fields before starting:
- `project_name`: brand or offer name.
- `market`: niche and geography.
- `offer`: product/service, price range if public, core promise.
- `target_avatar`: buyer profile.
- `competitors`: 3-8 public competitor brand/page names or Meta Ads Library URLs.
- `traffic_goal`: lead form, booking call, waitlist, audit, or lead magnet.
- `tone`: direct, premium, educational, founder-led, etc.

If any critical field is missing, ask one concise grouped question and continue with reasonable defaults once answered.

## Workspace

Create a Desktop folder first:

```bash
python3 skills/gauthier-thiry-leadfactory-free-skills/scripts/create_workspace.py \
  --project "Project Name"
```

If the script path differs because the skill is installed elsewhere, run the script from this skill's `scripts/` directory.

Expected output:

```text
~/Desktop/LeadFactory-Free-Skills-{project-slug}/
  00-input/brief.md
  01-deep-search/01-market-awareness.md
  01-deep-search/02-competitor-research.md
  01-deep-search/03-psychographic.md
  02-meta-ads-library/data.csv
  02-meta-ads-library/analysis.md
  03-strategy/strategy.md
  04-creative-brief/creative-brief.md
  05-cta/work-with-leadfactory.md
  DELIVERY-MANIFEST.md
```

## Parallel Research Plan

Use subagents when available. Launch the first four tasks in parallel:

1. Market awareness DeepSearch.
2. Competitor landscape DeepSearch.
3. Psychographic DeepSearch.
4. Public Meta Ads Library extraction and CSV normalization.

Then synthesize:

5. Strategy document from the three DeepSearch reports plus ad CSV.
6. Static creative brief from the strategy, psychographics, and competitor ad patterns.
7. Final manifest, CTA, and public-safety audit.

If subagents are unavailable, run the same tasks sequentially but keep files separated.

## DeepSearch

Read `references/deep-search-prompts.md` only when writing the three research reports.

Each report must:
- Be in French unless the user asks otherwise.
- Use public sources with URLs and access dates.
- Separate facts from inferences.
- Include direct implications for Meta Ads angles.
- Avoid private LeadFactory or client examples.

Save:
- `01-deep-search/01-market-awareness.md`
- `01-deep-search/02-competitor-research.md`
- `01-deep-search/03-psychographic.md`

## Public Meta Ads Library Research

Read `references/meta-ads-library-workflow.md` and `references/competitor-ads-framework.md` before extracting ads.

Goal:
- Build `02-meta-ads-library/data.csv` with one row per public ad or public ad-like asset.
- Build `02-meta-ads-library/analysis.md` with patterns, saturated angles, white spaces, hooks, CTAs, and recommendations.

Use no-key sources:
- Meta Ads Library public search pages.
- Public landing pages linked from ads.
- Public social posts if the ad page cannot be accessed.
- User-provided screenshots, URLs, or pasted text.

CSV columns are fixed. Use the template in `assets/templates/meta_ads_data_template.csv`.

## Strategy And Creative Brief

Read `references/strategy-and-creative-brief.md` and `references/meta-ad-copy-checklist.md` before writing final strategy assets.

Create:
- `03-strategy/strategy.md`: positioning, awareness level, test plan, campaign structure, angle matrix, risks, next actions.
- `04-creative-brief/creative-brief.md`: target audience, visual direction, static creative concepts, copy direction, examples of on-image text, and CTA.

Keep this public/free:
- Provide strategic frameworks and creative directions.
- Do not include complete VSL scripts.
- Do not include internal LeadFactory performance thresholds, automation scripts, or client proof.

## CTA

Create `05-cta/work-with-leadfactory.md` with a short, transparent CTA:

```markdown
# Aller plus loin avec LeadFactory

Ce dossier gratuit vous donne la recherche et la strategie de depart.
Pour deleguer la creation, le lancement et l'optimisation de vos campagnes Meta Ads, decouvrez LeadFactory :

https://www.leadfactory.my
```

## Public-Safety Audit

Before saying the folder is ready, run:

```bash
python3 skills/gauthier-thiry-leadfactory-free-skills/scripts/audit_public_safety.py \
  ~/Desktop/LeadFactory-Free-Skills-{project-slug}
```

If any issue is flagged, remove or rewrite the file before delivery.

Final quality gate:
- No API keys, tokens, environment files, private databases, CRM, or admin URLs.
- No real client names unless the user explicitly supplied them for their own public use.
- No absolute private local paths.
- No private emails, invoices, contracts, logs, generated client media, PDF/DOCX exports, or ZIPs.
- No VSL script files or full ad script packs.
- All sources are public and cited.
- The CTA points only to `https://www.leadfactory.my`.

## Final Response

Return:
- Desktop folder path.
- List of created deliverables.
- Note whether Meta Ads Library extraction was direct or fallback.
- Result of `audit_public_safety.py`.
