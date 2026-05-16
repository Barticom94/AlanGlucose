# financials/

Detailed financial models. The strategic summary lives in `state/financials.md` — that is
the single source of truth; this folder holds the working models behind it.

## Contents
- `unit-economics-template.md` — copy to `unit-economics.md` and fill in.
- `cashflow-24mo-template.md` — copy to `cashflow-24mo.md` and fill in.
- `scenarios/` — saved scenario runs (base / conservative / optimistic, and stress tests).

## A note on format
The brain's source specification lists these as `.xlsx` spreadsheets. They are provided
here as markdown templates so they live in git, diff cleanly, and are readable by the brain
directly. If you would rather have real Excel files, ask Claude to generate `.xlsx` versions
— the structure is identical.

## Rules
- Every input is cited or tagged `[ASSUMPTION — H/M/L]`. See the `evidence-bar` skill.
- The `financial-modeler-uk` subagent builds models; the `financial-stress-tester` reviews them.
- Verify all UK tax rates against gov.uk — see `@docs/UK-LEGAL-TAX.md`.
