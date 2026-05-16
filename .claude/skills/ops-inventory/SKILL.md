---
name: ops-inventory
description: Manage stock and inventory for the live venture. Use when the founder asks about inventory, stock levels, reordering, stockouts, SKUs, or inventory software. Phase 2 and beyond.
user-invocable: true
---

# Operations — Inventory

Inventory is cash sitting on a shelf. Too little and you lose sales; too much and you lose
working capital. For a bootstrap, cash discipline beats availability.

## Tooling by stage
- **Shopify native** — sufficient to roughly £300k revenue and a manageable SKU count. Do
  not pay for more until you need it.
- **Scale-up** — Cin7 Core, Linnworks, or similar, once you cross ~5,000 SKUs or go
  multi-warehouse. That is the phase-gate threshold.

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
