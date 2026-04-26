#!/usr/bin/env python3
"""Create a public LeadFactory Free Skills delivery workspace on Desktop."""

from __future__ import annotations

import argparse
import csv
import re
from datetime import date
from pathlib import Path


CSV_COLUMNS = [
    "competitor",
    "page_name",
    "ad_library_url",
    "ad_id",
    "format",
    "angle",
    "hook",
    "primary_text",
    "headline",
    "cta",
    "start_date",
    "last_seen",
    "days_active",
    "winner",
    "countries",
    "platforms",
    "media_type",
    "landing_url",
    "source_mode",
    "notes",
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "project"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Project, brand, or offer name.")
    parser.add_argument(
        "--desktop",
        default=str(Path.home() / "Desktop"),
        help="Desktop path. Defaults to ~/Desktop.",
    )
    args = parser.parse_args()

    slug = slugify(args.project)
    root = Path(args.desktop).expanduser() / f"LeadFactory-Free-Skills-{slug}"
    today = date.today().isoformat()

    dirs = [
        "00-input",
        "01-deep-search",
        "02-meta-ads-library",
        "03-strategy",
        "04-creative-brief",
        "05-cta",
    ]
    for folder in dirs:
        (root / folder).mkdir(parents=True, exist_ok=True)

    write_if_missing(
        root / "00-input" / "brief.md",
        f"""# Brief Source

Project: {args.project}
Created: {today}

## Market

## Offer

## Target Avatar

## Competitors

## Traffic Goal

## Tone
""",
    )

    placeholders = {
        "01-deep-search/01-market-awareness.md": "# Market Awareness DeepSearch\n\n",
        "01-deep-search/02-competitor-research.md": "# Competitor Research DeepSearch\n\n",
        "01-deep-search/03-psychographic.md": "# Psychographic DeepSearch\n\n",
        "02-meta-ads-library/analysis.md": "# Public Meta Ads Library Analysis\n\n",
        "03-strategy/strategy.md": "# Meta Ads Strategy\n\n",
        "04-creative-brief/creative-brief.md": "# Static Creative Brief\n\n",
        "05-cta/work-with-leadfactory.md": "# Aller plus loin avec LeadFactory\n\nCe dossier gratuit vous donne la recherche et la strategie de depart.\n\nPour deleguer la creation, le lancement et l'optimisation de vos campagnes Meta Ads, decouvrez LeadFactory :\n\nhttps://www.leadfactory.my\n",
        "DELIVERY-MANIFEST.md": f"# Delivery Manifest\n\nProject: {args.project}\nPrepared on: {today}\n\n## Contents\n\n- 00-input/brief.md\n- 01-deep-search/01-market-awareness.md\n- 01-deep-search/02-competitor-research.md\n- 01-deep-search/03-psychographic.md\n- 02-meta-ads-library/data.csv\n- 02-meta-ads-library/analysis.md\n- 03-strategy/strategy.md\n- 04-creative-brief/creative-brief.md\n- 05-cta/work-with-leadfactory.md\n\n## Public Safety\n\nThis package must contain only public research, user-provided inputs, no API keys, no private LeadFactory files, and no client-confidential assets.\n",
    }
    for relative_path, content in placeholders.items():
        write_if_missing(root / relative_path, content)

    csv_path = root / "02-meta-ads-library" / "data.csv"
    if not csv_path.exists():
        with csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(CSV_COLUMNS)

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
