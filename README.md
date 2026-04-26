# Gauthier Thiry LeadFactory Free Skills

Public, simplified LeadFactory skill for Meta Ads research and strategy.

It creates a Desktop delivery folder with:
- 3 DeepSearch documents.
- Public Meta Ads Library competitor analysis.
- A normalized `data.csv`.
- A strategy document.
- A static creative brief.
- A small CTA linking to `https://www.leadfactory.my`.

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
