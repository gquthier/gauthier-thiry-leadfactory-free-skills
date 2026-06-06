# Gauthier Thiry LeadFactory Free Skills

Public, simplified LeadFactory skills — no API keys beyond your own accounts, no paid tools, no internal infrastructure.

## Skills

### [`gauthier-thiry-leadfactory-free-skills`](skills/gauthier-thiry-leadfactory-free-skills/)
Market research and strategy skill. Creates a Desktop delivery folder with:
- 3 DeepSearch documents.
- Public Meta Ads Library competitor analysis.
- A normalized `data.csv`.
- A strategy document.
- A static creative brief.
- A small CTA linking to `https://www.leadfactory.my`.

### [`leadfactory-creative-static-free-v2`](skills/leadfactory-creative-static-free-v2/) ✨ New
**Lead Factory Creative Static Free Skill V2** — Generate a batch of static ad creatives for Meta Ads and TikTok using the [HiggsField CLI](https://higgsfield.ai) and GPT Image 2. Works for e-commerce and lead generation. Includes:
- A testable variation matrix (angles × formats × styles).
- 9 high-CTR native ad formats (iMessage, Tweet, iOS Note, TikTok Shop review, listicle, data-viz, flat-lay, native post, carousel).
- 3 prompt rules for sharp text rendering and edge-to-edge layout.
- A ready-to-run Python batch runner (`gen_run.py`) with concurrency control and job recovery.
- No Photoshop, no Figma — the full creative (visual + text) is rendered by GPT Image 2.

## What Is Excluded

- No API keys.
- No paid scraping providers.
- No Supabase or CRM injection.
- No internal LeadFactory app/admin links.
- No private client files, proofs, logs, PDFs, DOCX files, ZIPs, or generated media.
- No full VSL scripts or proprietary script packs.

## Install

Copy the skill folder into your Codex/Claude skills directory:

```bash
cp -R skills/gauthier-thiry-leadfactory-free-skills ~/.codex/skills/
```

Then ask:

```text
Use $gauthier-thiry-leadfactory-free-skills for my offer.
```

## Public Safety

Before publishing or sharing any generated folder, run:

```bash
python3 skills/gauthier-thiry-leadfactory-free-skills/scripts/audit_public_safety.py PATH_TO_FOLDER
```

The workflow is designed for public research and public Meta Ads Library data only.
