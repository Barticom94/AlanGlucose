# Tech Context

> Tools, stack, and integrations for this venture.

## Active stack
- Claude Code brain — this folder
- Python 3.13 (`py`) — runs the hooks in `.claude/hooks/`
- Node / `npx` — runs MCP servers
- git + GitHub (personal account)

## MCP servers — starter pack (active in `.mcp.json`)
`companies-house`, `exa`, `firecrawl`, `filesystem`, `sequential-thinking`, `github`,
`basic-memory`. Each needs the environment variables listed in `CLAUDE.local.md.example`.

## MCP servers — growth pack (wire in at Phase 2+, once the venture is live)
- Shopify Dev MCP — via the Shopify AI Toolkit
- Klaviyo — Claude Settings → Connectors, or `https://mcp.klaviyo.com`
- Stripe — `https://mcp.stripe.com` (OAuth) or `npx -y @stripe/mcp`
- Notion — the hosted remote MCP (OAuth)
- Linear — `https://mcp.linear.app/mcp`
- Playwright — `npx @playwright/mcp@latest`
- PostHog — `https://mcp.posthog.com/sse` (EU: set `POSTHOG_BASE_URL`)

Keep total active servers to roughly 5–8 — more crowds the context with tool schemas.

## No good MCP exists for
Trademark/domain checking, Royal Mail / DPD / Evri, HMRC. Use the gov.uk sites,
carrier APIs, or aggregators (Sendcloud, Easyship) directly.

## Tooling decisions
- {{DATE}} — {{ decision and reason }}
