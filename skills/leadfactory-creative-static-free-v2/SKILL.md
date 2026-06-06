---
name: leadfactory-creative-static-free-v2
description: Generate a batch of static ad creatives for Meta Ads and TikTok using the HiggsField CLI and GPT Image 2. Works for e-commerce (physical products, DTC) and lead generation (services, SaaS, agencies). Produces a testable variation matrix (angles × formats × styles) with complete prompts and a ready-to-run Python batch runner. Trigger phrases: "generate creatives", "batch of ads", "HiggsField static creatives", "Meta Ads visuals pack", "GPT Image 2 ads".
---

# Lead Factory Creative Static Free Skill V2

Generate a **batch of static ad creatives** ready to test on Meta Ads or TikTok, using the HiggsField CLI and GPT Image 2 as the rendering engine. Both the visual **and** the text (hook + CTA) are rendered directly by the AI — no Photoshop, no Figma, no PIL post-processing required.

Works for: **e-commerce** (physical products, DTC fashion, beauty, home) and **lead generation** (services, SaaS, agencies).

> **Free version**: no API keys beyond your own HiggsField account, no paid scraping, no CRM injection, no internal tools. Pure prompt engineering + CLI batch runner.

---

## What You Need

```bash
# 1. Install the HiggsField CLI (macOS / Linux)
brew install higgsfield-ai/tap/higgsfield
# or:
curl -fsSL https://cli.higgsfield.ai/install.sh | sh

# 2. Log in (opens browser → token stored locally)
higgsfield auth login

# 3. Confirm access
higgsfield model list | grep -E "gpt_image|nano_banana"
```

You need a HiggsField account with credits. All CLI calls are billed — no free tier on the CLI (free generations are web-app only).

---

## Recommended Models

| Model | Credits / image (2k) | Best for |
|-------|---------------------|----------|
| `gpt_image_2` ⭐ | 7 credits | Photorealism + sharp embedded text, wide format support |
| `nano_banana_2` | 2 credits | Excellent EN/FR text rendering, best value, supports 4:5 |
| `nano_banana` | 1 credit | Quick tests, lower quality |

**GPT Image 2 format note**: does **not** support the 4:5 ratio (standard Meta feed). Use **3:4** instead — visually near-identical, never rejected by Meta.
Supported ratios: `1:1` · `3:4` · `9:16` · `16:9`

Check cost before running a batch:
```bash
higgsfield generate cost gpt_image_2 --prompt "test" --aspect_ratio 3:4 --resolution 2k
```

---

## Brand Brief

Before generating, collect these details (ask the user if missing):

```
Brand / Product:      ____
Category:             e-com product | fashion | SaaS | service / lead gen | other
Main product / offer: ____  (describe precisely: material, color, silhouette, price)
Price:                ____
Brand palette:        ____  (e.g. cream #FBF6EC, espresso #3B2F23, terracotta #BE7A52)
Tone:                 ____  (e.g. warm clean-girl, direct/punchy, quiet-luxury, educational)
Ideal customer:       ____  (age, lifestyle, main pain point)
Top angle:            ____  (e.g. social proof, price, anti-competitor, founder story)
Main CTA:             ____  (e.g. SHOP NOW, GET A QUOTE, SEE THE RESULTS)
Number of creatives:  ____  (recommended: 8–15 for a real A/B test)
Formats:              ____  (feed 3:4, story 9:16, square 1:1, wide 16:9)
```

---

## Variation Matrix

A good matrix isolates **one variable per cell** so results are actionable:

| Test variable | Examples |
|---------------|---------|
| `hook` | 2–3 different hooks on the same visual |
| `concept_format` | iMessage vs Tweet vs listicle vs flat-lay |
| `visual_style` | Lifestyle photo vs editorial typography vs data-viz |
| `proof_element` | Review count vs price vs durability |
| `color_archetype` | Warm version vs dark/brutalist version |
| `format` | 3:4 vs 9:16 vs 1:1 for the same creative |

### High-performing native formats

These formats consistently outperform polished editorial ads on Meta cold traffic — because they don't look like ads:

| Format | Description | Best for |
|--------|-------------|---------|
| **iMessage conversation** | Authentic peer-recommendation screenshot | E-com, social proof |
| **Tweet / X review** | Viral-style post, instant read | Social proof, humor |
| **iOS Note** | Personal confession / tip | Education, anti-ad |
| **TikTok Shop review** | Native review screenshot + "As seen on TikTok Shop" | E-com TikTok |
| **Listicle "3 reasons"** | Quantified curiosity, scannable | All categories |
| **Stat / data-viz** | One big number that answers a price objection | Lead gen, e-com |
| **Flat-lay knolling** | Overhead product photo, short copy | Product e-com |
| **Native FB/IG post** | Fake boosted post + link preview | Cold broad |
| **Carousel problem → proof → offer** | 3-slide sequential persuasion | Consideration |

---

## 3 Prompt Rules (apply to every creative)

### Rule 1 — Edge-to-edge, no white borders
The creative must fill 100% of the frame. Logo and CTA go as overlays on the scene — never in a reserved white band.

Add to every prompt:
```
"Edge-to-edge, fills the full [ratio] frame, no white margins,
no white header bar, no white footer bar.
Logo and CTA are overlays ON the visual content."
```

### Rule 2 — CTA in ALL CAPS, aligned with copy column
`SHOP NOW` not `Shop now`. Place the CTA in the same vertical column as the headline — not isolated in an opposite corner.

```
"CTA label in ALL CAPS. Place the CTA directly below the headline,
same horizontal alignment."
```

### Rule 3 — Prompt-only for GPT Image 2 (do NOT pass --image)
When `--image` is used, GPT Image 2 copies the reference photo and **removes all text** (hook, CTA, wordmark). Instead, describe the product precisely in the prompt text — the AI generates everything including the embedded text.

---

## 3-Step Pipeline

```
Brief → Variation Matrix → Batch Generate
```

**Step 1 — Brief**: Collect brand info above. If competitor data or a Meta Ad Library analysis is available, read it to identify unsaturated angles (white space).

**Step 2 — Matrix**: Edit `scripts/build_plan.py` with your brand details and cell list. Run it to produce `plan.json`. Key rule: **never deliver 12 versions of the same editorial style** — mix native, lifestyle, typography, data-viz.

**Step 3 — Generate**: Run `gen_run.py plan_smoke.json` first (1 image smoke test), review the result, then `gen_run.py plan.json` for the full batch.

```bash
# Edit your brand + cells in build_plan.py, then:
python3 scripts/build_plan.py          # builds plan.json + plan_smoke.json

python3 scripts/gen_run.py plan_smoke.json   # 1-image smoke test first
# → review the output image before committing to the full batch

python3 scripts/gen_run.py plan.json   # full batch (runs 6 jobs in parallel)
```

---

## Prompt Structure — 7 Blocks

```
[1. Product context]
Premium [ratio] advertising creative for [BRAND], a [category] brand.
The product: [precise description — material, color, silhouette, visible texture].

[2. Scene & concept]
SCENE: [mise en scène description, native format or lifestyle].

[3. Brand register]
BRAND AESTHETIC: [hex palette, mood, clean-girl / luxury / direct / educational].

[4. Text to render — EXACT]
TEXT TO RENDER (spell exactly, crisp, no typos):
- Headline in elegant serif: "[exact hook]"
- CTA in ALL CAPS on a [color] pill: "[CTA]"
- Small brand wordmark top of frame: "[BRAND]"

[5. Layout]
LAYOUT: Edge-to-edge, image fills the entire [ratio] frame. NO white margins.
Logo and CTA are overlays ON the visual. CTA directly below the headline, same column.

[6. Quality]
QUALITY: Photorealistic, sharp, no distorted hands, no warped faces, no gibberish text.
All embedded text in flawless [EN/FR], perfectly legible, correct spelling.

[7. Safety suffix]
Fills the full [ratio] frame, no white margins. No logo hallucination.
```

---

## Suggested Output Folder Structure

```
my-ads-batch/
├── plan.json                 ← items list for the runner
├── variation-matrix.json     ← full matrix (angles, formats, test variables)
├── plan_smoke.json           ← single-item smoke test
├── gen.log                   ← append-only generation log
├── singles/                  ← single-frame creatives
│   ├── s01-hook-a.png
│   ├── s02-imessage.png
│   └── ...
└── carousel-A/               ← carousel slides
    ├── a1-cover.png
    └── ...
```

---

## Visual Checklist Before Shipping

For each generated creative, check:
- [ ] Main text is legible at thumbnail size (~400px wide)
- [ ] No stray letters / correct spelling
- [ ] Edge-to-edge — no white bands
- [ ] CTA in ALL CAPS, aligned with the headline
- [ ] Product is recognizable
- [ ] No distorted hands or uncanny faces
- [ ] Palette matches the requested register

---

## Recovering Lost Jobs

If a batch crashes mid-run, **do not re-submit** (it would double-bill you). Recover completed jobs:

```bash
higgsfield generate list --size 40 --json
# Filter for "completed" status → result_url has the image download link
```

The `gen_run.py` runner also skips any output file that already exists and is > 50 KB, so re-running the same plan is safe.

---

## Useful CLI Commands

```bash
higgsfield model list                          # list all available models
higgsfield generate cost <model> --prompt x --aspect_ratio 3:4 --resolution 2k
higgsfield generate list --size 20 --json      # recent jobs
higgsfield generate get <job-id> --json        # poll a specific job
```

---

## What This Skill Does NOT Include

- No internal LeadFactory pipeline (onboarding → deep-search → competitor mining → copy pack)
- No Council review agents
- No brand-lock PIL pass
- No 6-point copy validation framework
- No Supabase, CRM, or admin integrations

This is the standalone, no-dependencies version: **CLI + prompts + runner**.

---

*Lead Factory Creative Static Free Skill V2 — HiggsField CLI + GPT Image 2. Recommended model: `gpt_image_2` (7 credits / 2k image). Budget alternative: `nano_banana_2` (2 credits, supports 4:5).*
