# research/

Evidence gathered about the market, customers, and competitors. Everything here should be
sourced — this is where the `evidence-bar` skill is enforced in practice.

## Subfolders
- `customer-interviews/` — one file per interview, plus `SYNTHESIS-<date>.md` files written
  by the `customer-interview-synthesiser` subagent.
  `INTERVIEW-TEMPLATE.md` is the shape of each interview file; `SOURCING-TEMPLATE.md` is the
  shape of `SOURCING.md`, the plan for where the ten strangers come from.
- `competitor-profiles/` — one file per competitor, `<competitor>-<YYYY-MM-DD>.md`. Written
  by the `competitor-analyst` subagent.
- `market-reports/` — TAM/SAM/SOM and sector sizing, `market-<topic>-<YYYY-MM-DD>.md`.
  Written by the `market-researcher` subagent.
- `sector-notes/` — trends, regulation, and general sector reading.

## Rule
Every claim in this folder is cited (source + date) or tagged `[ASSUMPTION — H/M/L]`.
Date every file — undated research rots silently and is mistaken for current fact later.
