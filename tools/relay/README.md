# Learnings relay (maintainer only)

Lets a venture brain send its research rows home with nothing but an internet connection.
The brain POSTs JSON here; this Worker validates it and opens a `learnings` issue on the
template repo with a token only the relay holds. Review and merge happen as before
(`tools/harvest-learnings.py` → PR).

## Deploy once (about ten minutes)

1. **Token.** GitHub → Settings → Developer settings → Fine-grained tokens → Generate.
   Repository access: only `AlanGlucose`. Permissions: Issues → Read and write. Nothing else.
   Copy it; you will paste it in step 3 and never store it in a file.
2. **Cloudflare account** (free) if you do not have one. Then, from this folder:
   ```
   npx wrangler login
   ```
3. **Secret and deploy:**
   ```
   npx wrangler secret put GITHUB_TOKEN
   npx wrangler deploy
   ```
   Wrangler prints the URL, e.g. `https://alanglucose-learnings.<your-subdomain>.workers.dev`.
4. **Wire it in.** Put that URL into `.claude/skills/contribute-learnings/SKILL.md` where it
   says `ENDPOINT:`, run `python tools/build-adapters.py`, commit, and cut a release. Ventures
   downloaded before this will use the fallback routes; nothing is lost.
5. **Smoke test:**
   ```
   curl -sS -X POST -H "content-type: application/json" -H "x-alanglucose-client: alanglucose-v1" \
     --data '{"rows":[{"date":"2026-09-04","topic":"test","fact":"Relay smoke test","source":"tools/relay/README.md","confidence":"low"}]}' \
     https://alanglucose-learnings.<your-subdomain>.workers.dev
   ```
   Expect `{"ok":true,...,"issue":"https://github.com/.../issues/N"}`. Close that issue.

## What it does and does not do
- Accepts up to 30 rows / 8 KB per post; rejects bad dates, empty sources, unknown
  confidence values, and rows carrying venture-specific markers (same list as the harvest
  script). Rejections are counted in the issue, not stored.
- Stores nothing. Sees the rows and the sender's IP, as any web server does.
- The `x-alanglucose-client` header is a speed bump, not a secret — it stops accidental
  posts, not a determined spammer. If spam ever appears, add Cloudflare's rate limiting to
  this Worker, or rotate `CLIENT` and cut a release.
- If the token leaks, the blast radius is spam issues on one public repo. Revoke and
  re-issue it; nothing else is exposed.
