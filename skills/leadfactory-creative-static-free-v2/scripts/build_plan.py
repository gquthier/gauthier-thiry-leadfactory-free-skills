#!/usr/bin/env python3
"""
HiggsField Creative Ads — plan builder
Builds plan.json + variation-matrix.json from a list of cells.

Edit the BRAND and CELLS sections, then run:
  python3 build_plan.py
  python3 gen_run.py plan.json
"""
import json, os

# ─── CONFIG ───────────────────────────────────────────────────────────────────

OUTPUT_DIR = "./creatives"   # root output folder
MODEL = "gpt_image_2"        # gpt_image_2 (7 credits) or nano_banana_2 (2 credits)

# Your brand — fill this in
BRAND = {
    "name": "BRAND_NAME",
    "product": (
        "an oversized boxy linen co-ord set (shirt + wide-leg trousers) in clay terracotta, "
        "visible washed-linen texture, soft and relaxed"
    ),
    "palette": "cream #FBF6EC backgrounds, espresso #3B2F23 text, terracotta #BE7A52 CTA",
    "tone": "warm clean-girl, quiet-luxury, editorial",
    "price": "$58",
}

# Suffix added to every prompt — enforces quality + layout rules
def suffix(aspect):
    return (
        f" {BRAND['palette']}. Edge-to-edge, fills the full {aspect} frame, no white margins, "
        f"no white header bar, no white footer bar. Logo and CTA are overlays ON the visual. "
        f"ALL embedded text in flawless US English, perfectly legible, correct spelling, no gibberish. "
        f"Photorealistic, no warped faces or hands, no logo hallucination."
    )


# ─── CELLS — one row = one creative ──────────────────────────────────────────
# Each cell: id, fmt (display label), angle, test variable, aspect ratio, outdir, prompt
# Aspect ratios for gpt_image_2: 3:4 | 1:1 | 9:16 | 16:9  (NOT 4:5)

CELLS = [
    dict(
        id="s01-hook-a", fmt="Lifestyle hero", angle="Effortless / clean-girl", test="hook",
        aspect="3:4", outdir=os.path.join(OUTPUT_DIR, "singles"),
        prompt=(
            f"Premium 3:4 Meta ad for {BRAND['name']}. Product: {BRAND['product']}. "
            f"SCENE: A woman relaxed in golden natural light at home, candid and unposed, full-body. "
            f"BRAND: {BRAND['tone']}. "
            f"TEXT TO RENDER: Headline in elegant serif: "
            f"\"This is what I wear when I don't want to think about what I'm wearing.\" "
            f"CTA in ALL CAPS on a terracotta pill: \"SHOP THE SET\". "
            f"Small wordmark top of frame: \"{BRAND['name']}\". "
            f"CTA placed directly below the headline, same column."
        ),
    ),
    dict(
        id="s02-imessage", fmt="iMessage conversation", angle="Social proof / peer reco", test="concept_format",
        aspect="3:4", outdir=os.path.join(OUTPUT_DIR, "singles"),
        prompt=(
            f"A realistic iMessage conversation screenshot on an iPhone, authentic iOS look. "
            f"Two women friends (25-34) texting. "
            f"Grey bubble: 'ok where is that linen set from?? you've worn it like 5 times 😅'. "
            f"Blue bubble: '{BRAND['name']}. the {BRAND['price']} one — gets softer every wash, I live in it'. "
            f"Grey bubble: 'sending me the link rn'. "
            f"Small attached photo thumbnail of a woman in a clay linen co-ord set. "
            f"Looks like a genuine shared screenshot, NOT an ad."
        ),
    ),
    dict(
        id="s03-tweet", fmt="Tweet / X review", angle="UGC viral proof", test="concept_format",
        aspect="1:1", outdir=os.path.join(OUTPUT_DIR, "singles"),
        prompt=(
            f"A realistic X (Twitter) post screenshot card on an off-white background. "
            f"Tweet from a credible woman's account, round avatar, display name 'mara', handle '@maradoesthings'. "
            f"Tweet: 'the {BRAND['name'].lower()} linen set is the only thing i've worn in three weeks. "
            f"it gets softer every wash and it was {BRAND['price']}. send help.' "
            f"Small reply, repost and like counts (e.g. 1.2K likes). "
            f"Looks like a real viral tweet, not an ad."
        ),
    ),
    # Add more cells here following the same pattern
]

# ─── BUILD ────────────────────────────────────────────────────────────────────

os.makedirs(OUTPUT_DIR, exist_ok=True)

matrix = {
    "brand": BRAND["name"],
    "engine": MODEL,
    "resolution": "2k",
    "credits_per_image": 7 if MODEL == "gpt_image_2" else 2,
    "total_images": len(CELLS),
    "cells": [],
}

plan_items = []

for c in CELLS:
    full_prompt = c["prompt"] + suffix(c["aspect"])
    matrix["cells"].append({k: c[k] for k in ("id", "fmt", "angle", "test", "aspect")})
    plan_items.append({
        "id": c["id"],
        "aspect": c["aspect"],
        "prompt": full_prompt,
        "outdir": c["outdir"],
    })
    os.makedirs(c["outdir"], exist_ok=True)

json.dump(matrix, open("variation-matrix.json", "w"), indent=2, ensure_ascii=False)

plan = {
    "model": MODEL,
    "max_concurrent": 6,
    "resolution": "2k",
    "log": "./gen.log",
    "items": plan_items,
}
json.dump(plan, open("plan.json", "w"), indent=2, ensure_ascii=False)

# Smoke test plan (first item only)
smoke = dict(plan)
smoke["items"] = [plan_items[0]]
json.dump(smoke, open("plan_smoke.json", "w"), indent=2, ensure_ascii=False)

print(f"OK → {len(CELLS)} items in plan.json")
print(f"Smoke test: python3 gen_run.py plan_smoke.json")
print(f"Full batch: python3 gen_run.py plan.json")
print(f"Estimated cost: {len(CELLS)} × {matrix['credits_per_image']} = {len(CELLS) * matrix['credits_per_image']} credits")

for c in CELLS:
    print(f"  {c['id']:<22} [{c['aspect']:>4}] {c['fmt']}")
