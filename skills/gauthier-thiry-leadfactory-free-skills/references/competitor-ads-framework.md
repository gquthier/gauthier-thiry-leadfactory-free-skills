# Competitor Ads Framework

Use this public framework to classify ads and extract patterns from `data.csv`.

## Angle Classification

Assign one primary angle per ad. Use the first visible hook or first three seconds as the deciding signal.

### Douleur

The ad names a specific pain, frustration, or current failure.

Signals:
- "Marre de..."
- "Tu galeres a..."
- "Si tu es [persona] et que [problem]..."
- Concrete problem before solution.

### Desir

The ad leads with the desired future state.

Signals:
- Measurable result.
- Transformation.
- Faster, easier, more predictable outcome.

### Preuve

The ad leads with proof, case study, testimonial, review, or demonstrated result.

Signals:
- Named or anonymized customer result.
- Screenshot, quote, rating, case study.
- Before/after proof when compliant.

### ContreIntuitif

The ad breaks a common belief or attacks a default solution.

Signals:
- "Tout le monde pense X, mais..."
- "Le probleme n'est pas X."
- Contrarian diagnostic.

### Urgence

The ad creates a reason to act now.

Signals:
- Deadline.
- Limited spots.
- Seasonal timing.
- Closing enrollment.

### Other Useful Public Angles

Use these only if the five core angles do not fit:
- `Educatif`
- `Comparaison`
- `Autorite`
- `Transformation`

## Winner Rules

Use duration as a proxy, not proof of performance.

| Duration visible | Label |
|---|---|
| 0-6 days | Test |
| 7-21 days | Validation |
| 22+ days | Winner |
| 60+ days | Hero |
| 180+ days | Evergreen |

Set `winner=true` at 22+ days. If the start date is hidden, leave `winner` blank and add a note.

## Pattern Extraction

Extract:
- Repeated hook formulas.
- Repeated creative formats.
- Repeated CTAs.
- Repeated proof types.
- Repeated funnel destinations.
- Saturated pains.
- White spaces from DeepSearch pains not used by competitors.

## Recommendation Rule

Never tell the user to copy a competitor. Convert patterns into original tests:
- Same buyer tension, different mechanism.
- Same format, different proof.
- Same CTA intent, different wording.
- Same pain, more specific audience.
