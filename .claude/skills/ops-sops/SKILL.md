---
name: ops-sops
description: Create and maintain standard operating procedures. Use when the founder asks about SOPs, documenting a process, "how do I do this consistently", or has a task that recurs. Trigger when any task is done more than once a week.
user-invocable: true
---

# Operations — SOPs

A standard operating procedure turns a task the founder holds in their head into a
repeatable, delegable, automatable process. SOPs are what let a one-person business become
a two-person business.

## The rule
Any recurring task done more than once a week becomes an SOP in `docs/sops/`. For the
writing, spawn the `sop-writer` subagent.

## What a good SOP contains
1. **Trigger** — when to run this procedure.
2. **Inputs** — what is needed before starting (tools, accounts, information).
3. **Steps** — numbered, unambiguous, each a single action.
4. **Definition of done** — how you know it worked.
5. **Automation note** — which steps could later be automated, and how.

## Quality bar
An SOP must be followable by a tired person at 9pm, or by a future hire on day one, with no
extra explanation. If it assumes knowledge that lives only in the founder's head, it is not
finished.

## The automation ladder
- **Automate first:** order confirmations, shipping notifications, abandoned-cart, low-stock
  alerts — low brand risk, high time saving.
- **Automate last:** customer-service replies and pricing changes — high brand risk; keep
  these manual until the rules are genuinely proven.

## Maintenance
An SOP not updated when the process changes becomes a lie that misleads the next person.
Update it the same day the process changes, or delete it.
