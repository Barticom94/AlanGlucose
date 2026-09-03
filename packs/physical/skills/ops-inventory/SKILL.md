---
name: ops-inventory
description: Manage stock and inventory for the live venture. Use when the founder asks about inventory, stock levels, reordering, stockouts, SKUs, or inventory software. Phase 2 and beyond.
---

# Operations — Inventory

Inventory is cash sitting on a shelf. Too little and you lose sales; too much and you lose
working capital. For a bootstrap, cash discipline beats availability.

## How to use this skill
1. Confirm the gate first — check `state/progress.md`. Below Phase 2, keep stock levels
   minimal; do not build tooling for volume the venture does not have yet.
2. Pick the tooling for the current stage (below) — do not skip ahead to software the SKU
   count and location count do not yet justify.
3. Set the reorder point and safety buffer for each line, using real lead time, not the
   supplier's quoted best case.
4. Track stock turn and days of cover; flag slow movers early rather than at year-end.
5. Connect inventory to bookkeeping so stock value flows into the model automatically where
   possible.
6. Set up a low-stock alert once the product range is stable enough to be worth automating.

## Tooling by stage
- **Paper or a spreadsheet** — genuinely sufficient below a few hundred units and one
  location; it costs nothing and forces you to look at the stock.
- **The till or platform you already have** — most EPOS (Square, SumUp, Zettle) and store
  platforms track stock natively; do not buy a second system to duplicate one you are already
  paying for.
- **Dedicated inventory software** (Cin7 Core, Linnworks, Katana for makers) — only once
  multiple locations or thousands of SKUs make manual counting unreliable [ASSUMPTION — med
  risk; thresholds vary by trade, test against your own count time]. That is a tooling
  threshold, not a phase gate — see AGENTS.md for the phase gates.

## The numbers that matter
- **Lead time** — order to shelf. Drives how early you must reorder.
- **Reorder point** = (average daily sales × lead time) + a safety buffer.
- **Stock turn** — how many times a year stock sells through. Low turn is trapped cash.
- **Days of cover** — how long current stock lasts at the current sales rate.

## For a bootstrap specifically
1. Start lean. It is cheaper to sell out briefly than to tie cash up in dead stock.
2. Negotiate the lowest viable minimum order quantity with suppliers (see `ops-suppliers`).
3. Watch the slow movers — discount and clear them; do not let them anchor cash.
4. Connect inventory to bookkeeping so stock value flows into `state/financials.md`.

## Automate
A low-stock alert is worth setting up early. Automatic reordering comes later, once demand
is predictable enough to trust.

## Output
Update `state/financials.md` with current stock value and the reorder points for each line.
