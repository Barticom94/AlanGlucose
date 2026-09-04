// AlanGlucose learnings relay — a Cloudflare Worker.
//
// Accepts an anonymous POST of general research rows from a venture brain and opens a
// GitHub issue labelled "learnings" on the template repo, using a fine-grained token held
// only here. Founders need nothing but an internet connection. The relay sees the rows and
// the sending IP; it stores nothing.
//
// Deploy: see tools/relay/README.md. Secrets: GITHUB_TOKEN (issues: read/write on the repo).
// Vars: REPO (owner/name), CLIENT (a non-secret tag the skill sends, to stop drive-by posts).

const MAX_ROWS = 30;
const MAX_BYTES = 8 * 1024;
const CONFIDENCE = new Set(["high", "medium", "low"]);
const VENTURE_MARKERS = [
  "our customer", "our client", "my customer", "interview", "the founder", "we sell", "our price",
];

function bad(status, msg) {
  return new Response(JSON.stringify({ ok: false, error: msg }), {
    status, headers: { "content-type": "application/json" },
  });
}

function cleanCell(v) {
  return String(v ?? "").replace(/\s+/g, " ").replace(/\|/g, "│").trim();
}

function validateRow(r) {
  const date = cleanCell(r.date), topic = cleanCell(r.topic), fact = cleanCell(r.fact),
    source = cleanCell(r.source), confidence = cleanCell(r.confidence).toLowerCase();
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return { reject: "bad date" };
  if (!topic || topic.length > 80) return { reject: "bad topic" };
  if (!fact || fact.length > 400) return { reject: "bad fact" };
  if (!source || source.length > 300 || /^(internet|google|web)$/i.test(source)) return { reject: "bad source" };
  if (!CONFIDENCE.has(confidence)) return { reject: "bad confidence" };
  const lower = fact.toLowerCase();
  for (const m of VENTURE_MARKERS) if (lower.includes(m)) return { reject: `venture-specific marker: ${m}` };
  return { row: { date, topic, fact, source, confidence } };
}

export default {
  async fetch(request, env) {
    if (request.method !== "POST") return bad(405, "POST only");
    if (request.headers.get("x-alanglucose-client") !== (env.CLIENT || "alanglucose-v1")) return bad(403, "unknown client");
    const len = Number(request.headers.get("content-length") || 0);
    if (len > MAX_BYTES) return bad(413, "too large");

    let body;
    try { body = await request.json(); } catch { return bad(400, "invalid json"); }
    const rows = Array.isArray(body?.rows) ? body.rows.slice(0, MAX_ROWS) : [];
    if (!rows.length) return bad(400, "no rows");

    const accepted = [], rejected = [];
    for (const r of rows) {
      const v = validateRow(r || {});
      if (v.row) accepted.push(v.row); else rejected.push(v.reject);
    }
    if (!accepted.length) return bad(422, `no valid rows (${rejected.join("; ")})`);

    const today = new Date().toISOString().slice(0, 10);
    const table = ["| date | topic | fact | source | confidence |", "|---|---|---|---|---|",
      ...accepted.map(r => `| ${r.date} | ${r.topic} | ${r.fact} | ${r.source} | ${r.confidence} |`)].join("\n");
    const issue = {
      title: `Learnings: ${today} (${accepted.length} facts)`,
      labels: ["learnings"],
      body: `<!-- Sent via the learnings relay. Rejected at the relay: ${rejected.length}. -->\n\n${table}\n`,
    };

    const gh = await fetch(`https://api.github.com/repos/${env.REPO}/issues`, {
      method: "POST",
      headers: {
        "authorization": `Bearer ${env.GITHUB_TOKEN}`,
        "accept": "application/vnd.github+json",
        "content-type": "application/json",
        "user-agent": "alanglucose-learnings-relay",
      },
      body: JSON.stringify(issue),
    });
    if (!gh.ok) return bad(502, `github ${gh.status}`);
    const created = await gh.json();
    return new Response(JSON.stringify({ ok: true, accepted: accepted.length, rejected, issue: created.html_url }), {
      headers: { "content-type": "application/json" },
    });
  },
};
