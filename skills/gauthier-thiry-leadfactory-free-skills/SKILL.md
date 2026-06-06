---
name: gauthier-thiry-leadfactory-free-skills
description: Public no-key LeadFactory workflow for Meta Ads research deliverables. Deploys up to 50 parallel sub-agents to research markets, competitors, ICPs, and ad patterns. Outputs a rich master CSV (opportunities + ICP matrix + deep search recap) plus strategy and creative brief. Use when the user wants Gauthier Thiry / LeadFactory free skills, deep market research, public Meta Ads Library competitor research, a rich Excel/CSV dataset, a strategy document, a static creative brief, or a Desktop delivery folder without private LeadFactory tools, paid API keys, database injection, client files, VSL scripts, or proprietary creative generation.
---

# Gauthier Thiry LeadFactory Free Skills

Public, simplified LeadFactory pipeline for people who want the research and strategy layer of a Meta Ads launch without private infrastructure.

This skill deploys **up to 50 parallel sub-agents** across market awareness, competitor research, ICP profiling, ad pattern analysis, and opportunity synthesis. It produces a rich master CSV and a full strategy package on the user's Desktop.

## Final Deliverables

```
~/Desktop/LeadFactory-Free-Skills-{project-slug}/
  00-input/brief.md
  01-deep-search/01-market-awareness.md
  01-deep-search/02-competitor-research.md
  01-deep-search/03-psychographic.md
  02-meta-ads-library/data.csv
  02-meta-ads-library/analysis.md
  03-strategy/strategy.md
  04-creative-brief/creative-brief.md
  05-master-output/master-research.csv       ← rich CSV (all research in one file)
  05-cta/work-with-leadfactory.md
  DELIVERY-MANIFEST.md
```

The **`master-research.csv`** is the primary output: a single enriched spreadsheet combining all research signals — market data, competitor profiles, ICP segments, white spaces, and prioritized ad angles — ready to import into Excel, Google Sheets, or Airtable.

---

## Non-Negotiables

- Never request or use paid API keys, service-role keys, private database credentials, CRM access, internal apps, private repos, or client folders.
- Never copy real LeadFactory client deliverables, PDFs, DOCX files, logs, state files, generated media, private emails, internal paths, or proof assets.
- Do not generate full VSL scripts, long-form sales letters, or proprietary script packs. Only create strategy, angle rationale, static creative brief, and short ad concept copy.
- Use public web research and public Meta Ads Library pages only. Do not bypass login, paywalls, rate limits, or platform restrictions.
- If public scraping fails, create a transparent fallback CSV from manually visible ad URLs, user-provided screenshots, pasted ad text, or public landing pages. Label it as fallback.
- Save final output on the user's Desktop, not inside a private LeadFactory project folder.

---

## Inputs

Collect or infer these fields before starting:
- `project_name`: brand or offer name.
- `market`: niche and geography.
- `offer`: product/service, price range if public, core promise.
- `target_avatar`: buyer profile.
- `competitors`: 3–8 public competitor brand/page names or Meta Ads Library URLs.
- `traffic_goal`: lead form, booking call, waitlist, audit, or lead magnet.
- `tone`: direct, premium, educational, founder-led, etc.

If any critical field is missing, ask one concise grouped question and continue with reasonable defaults once answered.

---

## Workspace

Create a Desktop folder first:

```bash
python3 skills/gauthier-thiry-leadfactory-free-skills/scripts/create_workspace.py \
  --project "Project Name"
```

---

## 50-Agent Research Architecture

Launch sub-agents in parallel batches. Each agent has a focused mandate and returns structured findings that feed the master CSV.

### Batch 1 — Market Foundation (5 agents)

| Agent | Mandate |
|-------|---------|
| M1 — Market Size | TAM, SAM, SOM estimates. Growth rate, macro trends, seasonality. Public sources (Statista, Grand View, IBISWorld free previews, industry reports). |
| M2 — Pricing Landscape | Price bands across the market. Entry / mid / premium segments. Price anchors used in ads. |
| M3 — Regulatory & Compliance | Platform ad policies (Meta, TikTok) for this niche. Sensitive categories, banned claims, compliance constraints. |
| M4 — Trend Signals | Google Trends, TikTok trending sounds/hashtags, Reddit hot threads, rising search queries. 6-month window. |
| M5 — Channel Map | Which channels are saturated vs. underused: Meta, TikTok Shop, Google, YouTube, email, influencer. |

### Batch 2 — Competitor Deep Dives (up to 20 agents, one per competitor)

For each competitor brand provided (max 20), launch one agent:

| Sub-agent | Mandate |
|-----------|---------|
| C1…C20 — Competitor {N} | Public website: hero offer, price, brand promise, ICP signals. Meta Ads Library: estimated active ad count, top angles, hook patterns, visual style, CTA. TikTok/Instagram presence. Key strengths, weaknesses, threat level (HIGH / MEDIUM / LOW). |

Each competitor agent returns a structured row for `data.csv` plus narrative notes.

### Batch 3 — ICP Segments (10 agents)

| Agent | Mandate |
|-------|---------|
| ICP1 — Primary Persona | Demographics, psychographics, day-in-the-life, top 3 pain points, primary motivation to buy, main objection, preferred content format. |
| ICP2 — Secondary Persona | Alternative buyer segment — different age, context, or use case. Same fields. |
| ICP3 — Reddit Deep Dive | Subreddits relevant to the niche. Top threads, recurring complaints, vocabulary used ("they say X when they mean Y"), trust signals that work. |
| ICP4 — Review Mining | 1-star and 5-star review analysis from public sources (Amazon, Trustpilot, Google Reviews, App Store). Patterns in language, specific words that recur. |
| ICP5 — Objection Map | Top 5 objections to purchase in this category. For each: objection text → counter-argument → ad angle that addresses it. |
| ICP6 — Awareness Levels | Map the market across Eugene Schwartz's 5 stages (Unaware → Most Aware). Where does the bulk of cold traffic sit? Which stage to target first? |
| ICP7 — TikTok Audience Signals | TikTok hashtag audiences, FYP content patterns, creator types that resonate, comment sentiment on competitor videos. |
| ICP8 — Seasonal Triggers | When does this ICP buy? Events, seasons, life triggers (new year, back to school, pay day, etc.) that drive purchase intent. |
| ICP9 — Cultural / Geo Signals | If multi-market: cultural nuances, localization needs, price sensitivity differences. |
| ICP10 — Micro-Segment Opportunities | Under-served sub-segments ignored by current competitors. Niche within the niche. |

### Batch 4 — Ad Pattern Analysis (10 agents)

| Agent | Mandate |
|-------|---------|
| AP1 — Hook Patterns | Top 20 hooks used across competitors. Categorize by type: question, contrarian, social proof, POV, stat, listicle. Identify saturation level. |
| AP2 — Visual Styles | Dominant visual styles in the category: lifestyle, editorial, UGC, flat-lay, native screenshot, data-viz, advertorial. Which are over/underused? |
| AP3 — CTA Patterns | Most common CTAs in this market. Which map to which funnel stage. Underused CTAs. |
| AP4 — Format Saturation | Distribution of ad formats: feed single / story / reel / carousel / collection. White spaces in format mix. |
| AP5 — Price Framing | How do competitors frame price? Direct price, anchoring, cost-per-use, comparison, "less than X per day"? |
| AP6 — Social Proof Patterns | Review counts, star ratings, "as seen on", TikTok Shop badges, press mentions. Which proof signals are most used/trusted? |
| AP7 — Emotional Angles | Dominant emotional triggers: fear, aspiration, identity, belonging, savings, status. Which are over/underused? |
| AP8 — Anti-Patterns (what NOT to do) | Angles that are overplayed and showing ad fatigue. Visual styles that look dated. Claims likely to get flagged. |
| AP9 — TikTok-Native vs Meta-Polish | Gap between TikTok-native content (lo-fi, UGC) and Meta polished ads. Which performs better in this niche? Evidence? |
| AP10 — White Space Matrix | Combine all above: angles × formats × styles with zero incumbent use → ranked opportunity list. |

### Batch 5 — Synthesis (5 agents)

| Agent | Mandate |
|-------|---------|
| S1 — Opportunity Scoring | Score each white space (0–10) on: audience size, competition density, ad fatigue level, format accessibility, compliance risk. |
| S2 — Positioning Statement | Draft 3 positioning options for the brand. For each: one-liner, key differentiator, primary ICP, primary channel. |
| S3 — Angle Priority Matrix | Rank the top 10 ad angles by: expected CTR tier, awareness stage fit, format fit, and ease of execution. |
| S4 — 30-Day Test Plan | Recommend Phase 1 (days 1–10): 3 angles × 2 formats = 6 creatives, $X daily budget, kill criteria. Phase 2 scaling logic. |
| S5 — Master CSV Assembly | Aggregate all agent outputs into `master-research.csv` following the schema below. |

---

## Master CSV Schema — `master-research.csv`

One file, multiple `record_type` values so it imports cleanly into Excel / Google Sheets / Airtable.

### Column definitions

| Column | Description |
|--------|-------------|
| `record_type` | `MARKET` / `COMPETITOR` / `ICP` / `AD_ANGLE` / `OPPORTUNITY` |
| `id` | Unique row ID (e.g. `MKT-001`, `COMP-003`, `ICP-002`, `ANG-007`, `OPP-004`) |
| `name` | Entity name (market segment, competitor brand, persona name, angle name, opportunity label) |
| `category` | Sub-classification (e.g. for COMPETITOR: `direct` / `indirect` / `aspirational`) |
| `summary` | 1–2 sentence description |
| `price_range_usd` | Price range or N/A |
| `primary_channel` | Main distribution channel (Meta / TikTok / Google / Email / etc.) |
| `icp_fit` | Which ICP segment(s) this maps to |
| `awareness_stage` | Schwartz stage: 1=Unaware … 5=Most Aware |
| `hook_example` | A concrete hook line for this angle/competitor/opportunity |
| `visual_style` | Dominant or recommended visual style |
| `format` | Best ad format(s) for this row |
| `cta` | Recommended CTA |
| `strength` | Key strength (for competitors) or why this angle works |
| `weakness` | Key weakness or risk |
| `threat_level` | HIGH / MEDIUM / LOW / N/A |
| `saturation_score` | 0–10 — how saturated is this angle/competitor/format in the market |
| `opportunity_score` | 0–10 — overall opportunity rating |
| `priority` | P1 / P2 / P3 — execution priority |
| `source` | Public URL(s) or "Meta Ads Library", "Reddit", "Review mining", etc. |
| `notes` | Additional context, compliance flags, caveats |
| `agent` | Which sub-agent produced this row (e.g. `C05`, `ICP3`, `AP10`) |

### Example rows

```csv
record_type,id,name,category,summary,price_range_usd,primary_channel,icp_fit,awareness_stage,hook_example,visual_style,format,cta,strength,weakness,threat_level,saturation_score,opportunity_score,priority,source,notes,agent
MARKET,MKT-001,Linen co-ord sets US,DTC fashion,"$200–420M SAM, growing 18% YoY, driven by clean-girl TikTok aesthetics",58–180,TikTok+Meta,Women 24–35,2,,"UGC lifestyle",,,,,,,,4,8,P1,Statista 2025 / TikTok trends,,M1
COMPETITOR,COMP-001,Quince,direct,"Premium linen basics, $60–120, strong Meta presence, weak TikTok Shop",60–120,Meta+Email,Women 28–42,3,"Premium linen. Not $180.","Editorial lifestyle",3:4 feed,SHOP NOW,"Price positioning, strong reviews","No TikTok Shop native presence",HIGH,7,6,P2,meta.com/ads/library,,C2
ICP,ICP-001,Maya,"primary persona","28yo, millennial, seeks effortless style, $58 feels acceptable if quality is proven",,TikTok+Meta,,"2–3","This is what I wear when I don't want to think.","UGC selfie",9:16,"SHOP THE SET","Responds to social proof + fabric quality","Needs proof before price commitment",,,9,P1,Reddit r/femalefashionadvice,,ICP1
AD_ANGLE,ANG-001,Cost-per-wear,value framing,"$0.29/wear reframes $58 as exceptional value vs fast fashion",,,ICP-001,3–4,"$0.29 per wear. 200 wears. The set that earns its place.","Data-viz bold stat",1:1,"SHOP THE SET","Directly counters price objection","Requires some numeracy from viewer",,3,9,P1,Competitor ad analysis,,AP5
OPPORTUNITY,OPP-001,TikTok-native UGC + iMessage format,white space,"Zero incumbents use native social-proof formats (iMessage/TikTok review) for linen co-ords",,TikTok+Meta,ICP-001,2,"ok where is that linen set from?? 😅","iMessage native screenshot",3:4,"shop link in bio",,"Requires no brand recognition to thumb-stop",,0,10,P1,"Meta Ad Library sweep — 0 results",,AP10
```

---

## Parallel Research Plan

### Phase 1 — Launch all 50 agents simultaneously

```
Batch 1 (M1–M5):    Market foundation — 5 agents
Batch 2 (C1–C20):   One agent per competitor — up to 20 agents
Batch 3 (ICP1–10):  ICP segments — 10 agents
Batch 4 (AP1–10):   Ad pattern analysis — 10 agents
```

All 45 agents run in parallel. Each writes its structured findings back as JSON or structured markdown.

### Phase 2 — Synthesis (after Batch 1–4 complete)

```
Batch 5 (S1–S5):    Synthesis — 5 agents
```

S5 (Master CSV Assembly) runs last: aggregates all agent outputs into `master-research.csv`.

### Phase 3 — Strategy & Creative Brief

6. Strategy document from DeepSearch reports + master CSV.
7. Static creative brief from strategy, psychographics, and competitor ad patterns.
8. Final manifest, CTA, and public-safety audit.

If sub-agents are unavailable, run the same tasks sequentially but keep files separated.

---

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

---

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

---

## Strategy And Creative Brief

Read `references/strategy-and-creative-brief.md` and `references/meta-ad-copy-checklist.md` before writing final strategy assets.

Create:
- `03-strategy/strategy.md`: positioning, awareness level, test plan, campaign structure, angle matrix, risks, next actions.
- `04-creative-brief/creative-brief.md`: target audience, visual direction, static creative concepts, copy direction, examples of on-image text, and CTA.

Keep this public/free:
- Provide strategic frameworks and creative directions.
- Do not include complete VSL scripts.
- Do not include internal LeadFactory performance thresholds, automation scripts, or client proof.

---

## CTA

Create `05-cta/work-with-leadfactory.md` with a short, transparent CTA:

```markdown
# Aller plus loin avec LeadFactory

Ce dossier gratuit vous donne la recherche et la strategie de depart.
Pour deleguer la creation, le lancement et l'optimisation de vos campagnes Meta Ads, decouvrez LeadFactory :

https://www.leadfactory.my
```

---

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

---

## Final Response

Return:
- Desktop folder path.
- List of created deliverables.
- Number of sub-agents launched and completed.
- Row count of `master-research.csv` (breakdown by `record_type`).
- Note whether Meta Ads Library extraction was direct or fallback.
- Result of `audit_public_safety.py`.
