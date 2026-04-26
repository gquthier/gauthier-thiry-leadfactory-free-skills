# Client Intake Schema

Use this schema to normalize the user's input into `00-input/brief.md`.

## Required Fields

```yaml
project_name:
market:
geography:
offer:
price_range:
target_avatar:
traffic_goal:
competitors:
tone:
proof_available:
constraints:
```

## Field Guidance

- `project_name`: public name of the brand, offer, or example project.
- `market`: niche or category.
- `geography`: default to France if the user gives no geography.
- `offer`: what is sold and how it is delivered.
- `price_range`: optional; leave blank if private or unknown.
- `target_avatar`: who should buy.
- `traffic_goal`: booking call, lead form, lead magnet, waitlist, checkout, or audit.
- `competitors`: 3-8 public competitors or Meta Ads Library URLs.
- `tone`: direct, premium, educational, founder-led, expert-led, etc.
- `proof_available`: public proof only. Do not invent proof.
- `constraints`: compliance, claims to avoid, words to avoid, legal limits.

## Missing Data Rule

Ask once for missing critical data. If the user cannot provide competitors, research likely competitors from public search and mark them as `inferred`.
