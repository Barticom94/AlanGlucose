#!/usr/bin/env python3
"""harvest-learnings.py

Pulls GitHub issues labelled "learnings" from Barticom94/AlanGlucose (opened by the
contribute-learnings skill in venture brains), parses the markdown-table rows in their
bodies, validates and dedupes them against docs/KNOWLEDGE.md, and either prints the
proposed rows (default, dry run) or appends them (--apply).

Usage:
    python tools/harvest-learnings.py                  dry run against live issues
    python tools/harvest-learnings.py --apply           append accepted rows to KNOWLEDGE.md
    python tools/harvest-learnings.py --apply --close   also comment + close processed issues
    python tools/harvest-learnings.py --file some.md    read rows from a local file instead
                                                         of GitHub issues (no gh calls, no
                                                         --close)
    python tools/harvest-learnings.py --knowledge PATH  use an alternate KNOWLEDGE.md-shaped
                                                         file (for testing; default
                                                         docs/KNOWLEDGE.md)

Row shape (5 markdown-table cells, a trailing 6th "shared" cell is tolerated and dropped):
    | date | topic | fact | source | confidence |

Validation rejects a row if: the date does not parse as YYYY-MM-DD; the fact is empty or
>= 400 chars; the source is empty or is just "internet"/"google"; the confidence is not
high/medium/low (case-insensitive); or the row contains an obviously venture-specific
marker ("our customer", "our client", "my customer", "interview", "the founder", "we
sell", "our price").

Dedupe against docs/KNOWLEDGE.md: an identical fact (case-insensitive, whitespace-
collapsed) is skipped outright; a row with the same topic whose fact shares >= 80% of its
words with an existing fact is reported as a probable duplicate instead of being added.

Python 3.9+, standard library only.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

REPO = "Barticom94/AlanGlucose"
LABEL = "learnings"

VENTURE_MARKERS = [
    "our customer",
    "our client",
    "my customer",
    "interview",
    "the founder",
    "we sell",
    "our price",
]

BAD_SOURCES = {"internet", "google"}
CONFIDENCES = {"high", "medium", "low"}
MAX_FACT_LEN = 400
DEDUPE_WORD_OVERLAP = 0.80

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SEPARATOR_CELL_RE = re.compile(r"^:?-+:?$")
WORD_RE = re.compile(r"[a-z0-9']+")


@dataclass
class Row:
    date: str
    topic: str
    fact: str
    source: str
    confidence: str
    origin: str  # "issue #12" or "file <name>"
    issue_number: Optional[int] = None


@dataclass
class IssueResult:
    number: int
    accepted: list = field(default_factory=list)
    rejected: list = field(default_factory=list)  # list of (Row-ish text, reason)
    duplicates: list = field(default_factory=list)  # list of (fact, existing_fact)


# --------------------------------------------------------------------------- gh plumbing

def check_gh_available() -> None:
    try:
        subprocess.run(
            ["gh", "--version"], capture_output=True, text=True, check=False
        )
    except FileNotFoundError:
        print(
            "ERROR: the 'gh' CLI was not found on PATH. Install it from "
            "https://cli.github.com/ and run 'gh auth login'.",
            file=sys.stderr,
        )
        sys.exit(1)


def check_gh_authenticated() -> None:
    result = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    if result.returncode != 0:
        print(
            "ERROR: 'gh' is not authenticated. Run 'gh auth login' first.\n"
            f"{result.stderr.strip()}",
            file=sys.stderr,
        )
        sys.exit(1)


def fetch_issues(repo: str, label: str, state: str, limit: int) -> list:
    cmd = [
        "gh", "issue", "list",
        "--repo", repo,
        "--label", label,
        "--state", state,
        "--limit", str(limit),
        "--json", "number,title,body,createdAt",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: 'gh issue list' failed:\n{result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    try:
        # Assumption: gh emits a JSON array of objects with keys
        # number (int), title (str), body (str, markdown), createdAt (ISO 8601 str).
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print(f"ERROR: could not parse 'gh issue list' JSON output: {exc}", file=sys.stderr)
        sys.exit(1)
    return data


def gh_comment_and_close(repo: str, number: int, body: str) -> None:
    comment = subprocess.run(
        ["gh", "issue", "comment", str(number), "--repo", repo, "--body", body],
        capture_output=True, text=True,
    )
    if comment.returncode != 0:
        print(f"WARNING: could not comment on issue #{number}: {comment.stderr.strip()}", file=sys.stderr)
    close = subprocess.run(
        ["gh", "issue", "close", str(number), "--repo", repo],
        capture_output=True, text=True,
    )
    if close.returncode != 0:
        print(f"WARNING: could not close issue #{number}: {close.stderr.strip()}", file=sys.stderr)


# --------------------------------------------------------------------------- table parsing

def parse_table_rows(text: str):
    """Yield raw 5-cell rows (lists of str) from any markdown table in `text`.

    Skips header rows, separator rows (---|---|...), and fully-blank rows. Tolerates a
    trailing 6th cell (e.g. "shared") by dropping it.
    """
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        inner = stripped[1:-1]
        cells = [c.strip() for c in inner.split("|")]
        if len(cells) == 6:
            cells = cells[:5]
        if len(cells) != 5:
            continue
        if all(c == "" for c in cells):
            continue
        if all(SEPARATOR_CELL_RE.match(c) for c in cells):
            continue
        if cells[0].lower() in ("date", "date verified") and cells[1].lower() == "topic":
            continue
        yield cells


# --------------------------------------------------------------------------- validation

def validate_row(cells) -> Optional[str]:
    """Return None if the row is valid, else a human-readable rejection reason."""
    date, topic, fact, source, confidence = cells

    if not DATE_RE.match(date.strip()):
        return f"bad date '{date}'"
    try:
        year, month, day = (int(p) for p in date.strip().split("-"))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return f"bad date '{date}'"
        import datetime as _dt
        _dt.date(year, month, day)
    except ValueError:
        return f"bad date '{date}'"

    if not fact.strip():
        return "fact is empty"
    if len(fact) >= MAX_FACT_LEN:
        return f"fact too long ({len(fact)} >= {MAX_FACT_LEN} chars)"

    if not source.strip():
        return "source is empty"
    if source.strip().lower() in BAD_SOURCES:
        return f"source is just a placeholder ('{source.strip()}')"

    if confidence.strip().lower() not in CONFIDENCES:
        return f"bad confidence '{confidence}' (must be high/medium/low)"

    haystack = " | ".join(cells).lower()
    for marker in VENTURE_MARKERS:
        if marker in haystack:
            return f"venture-specific marker found: '{marker}'"

    return None


# --------------------------------------------------------------------------- dedupe

def normalize_fact(fact: str) -> str:
    return re.sub(r"\s+", " ", fact.strip().lower())


def normalize_topic(topic: str) -> str:
    return topic.strip().lower()


def words_of(fact: str) -> set:
    return set(WORD_RE.findall(fact.lower()))


def word_overlap_ratio(a: str, b: str) -> float:
    wa, wb = words_of(a), words_of(b)
    if not wa or not wb:
        return 0.0
    smaller = min(len(wa), len(wb))
    if smaller == 0:
        return 0.0
    return len(wa & wb) / smaller


def find_duplicate(new_topic: str, new_fact: str, existing_rows: list) -> Optional[tuple]:
    """existing_rows: list of (topic, fact). Returns (kind, existing_fact) or None."""
    norm_new_fact = normalize_fact(new_fact)
    for topic, fact in existing_rows:
        if normalize_fact(fact) == norm_new_fact:
            return ("exact", fact)
    norm_new_topic = normalize_topic(new_topic)
    for topic, fact in existing_rows:
        if normalize_topic(topic) == norm_new_topic:
            if word_overlap_ratio(new_fact, fact) >= DEDUPE_WORD_OVERLAP:
                return ("probable", fact)
    return None


def load_existing_rows(knowledge_path: Path) -> list:
    if not knowledge_path.exists():
        return []
    text = knowledge_path.read_text(encoding="utf-8")
    return [(cells[1], cells[2]) for cells in parse_table_rows(text)]


# --------------------------------------------------------------------------- rendering

def escape_cell(value: str) -> str:
    return value.strip().replace("|", "\\|")


def render_row(row: Row) -> str:
    return (
        f"| {escape_cell(row.date)} | {escape_cell(row.topic)} | {escape_cell(row.fact)} "
        f"| {escape_cell(row.source)} | {escape_cell(row.confidence.lower())} |"
    )


def render_table(rows: list) -> str:
    if not rows:
        return "(none)"
    header = "| date | topic | fact | source | confidence |"
    sep = "|---|---|---|---|---|"
    lines = [header, sep] + [render_row(r) for r in rows]
    return "\n".join(lines)


# --------------------------------------------------------------------------- knowledge append

def append_to_knowledge(knowledge_path: Path, rows: list) -> None:
    text = knowledge_path.read_text(encoding="utf-8")
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")

    # Drop a single trailing blank line produced by split() when the file ends with "\n".
    had_trailing_newline = lines and lines[-1] == ""
    if had_trailing_newline:
        lines = lines[:-1]

    last_table_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            last_table_idx = i
    if last_table_idx is None:
        raise RuntimeError(f"no markdown table found in {knowledge_path}")

    new_lines = [render_row(r) for r in rows]
    lines[last_table_idx + 1:last_table_idx + 1] = new_lines

    out = "\n".join(lines) + "\n"
    knowledge_path.write_text(out, encoding="utf-8", newline="\n")


# --------------------------------------------------------------------------- main

def process_body(body: str, origin: str, issue_number: Optional[int]) -> list:
    rows = []
    for cells in parse_table_rows(body or ""):
        rows.append((cells, origin, issue_number))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=REPO, help=f"GitHub repo to scan (default {REPO})")
    parser.add_argument("--label", default=LABEL, help=f"issue label (default {LABEL})")
    parser.add_argument("--state", default="open", help="issue state (default open)")
    parser.add_argument("--limit", type=int, default=200, help="max issues to fetch (default 200)")
    parser.add_argument("--file", type=Path, default=None, help="parse a local markdown file instead of GitHub issues")
    parser.add_argument("--knowledge", type=Path, default=Path("docs/KNOWLEDGE.md"), help="path to the KNOWLEDGE.md-shaped file (default docs/KNOWLEDGE.md)")
    parser.add_argument("--apply", action="store_true", help="append accepted rows to --knowledge (default: dry run, print only)")
    parser.add_argument("--close", action="store_true", help="comment on and close each processed issue (requires --apply, not usable with --file)")
    args = parser.parse_args()

    if args.close and not args.apply:
        print("ERROR: --close requires --apply (never closes issues in a dry run).", file=sys.stderr)
        return 1
    if args.close and args.file:
        print("ERROR: --close cannot be used with --file (no issues to close).", file=sys.stderr)
        return 1

    existing_rows = load_existing_rows(args.knowledge)

    issue_results = {}  # number -> IssueResult
    raw_rows = []  # list of (cells, origin, issue_number)
    issues_scanned = 0

    if args.file:
        text = args.file.read_text(encoding="utf-8")
        raw_rows.extend(process_body(text, f"file {args.file.name}", None))
        issues_scanned = 1
    else:
        check_gh_available()
        check_gh_authenticated()
        issues = fetch_issues(args.repo, args.label, args.state, args.limit)
        issues_scanned = len(issues)
        for issue in issues:
            number = issue.get("number")
            body = issue.get("body") or ""
            issue_results[number] = IssueResult(number=number)
            raw_rows.extend(process_body(body, f"issue #{number}", number))

    accepted: list = []
    rejected: list = []  # (origin, fact_excerpt, reason)
    duplicates: list = []  # (origin, fact, existing_fact, kind)

    for cells, origin, issue_number in raw_rows:
        date, topic, fact, source, confidence = cells
        reason = validate_row(cells)
        excerpt = (fact.strip()[:80] + "...") if len(fact.strip()) > 80 else fact.strip()
        if reason:
            rejected.append((origin, excerpt, reason))
            if issue_number in issue_results:
                issue_results[issue_number].rejected.append((excerpt, reason))
            continue

        dup = find_duplicate(topic, fact, existing_rows)
        if dup:
            kind, existing_fact = dup
            duplicates.append((origin, excerpt, existing_fact, kind))
            if issue_number in issue_results:
                issue_results[issue_number].duplicates.append((excerpt, existing_fact))
            continue

        row = Row(
            date=date.strip(), topic=topic.strip(), fact=fact.strip(),
            source=source.strip(), confidence=confidence.strip().lower(),
            origin=origin, issue_number=issue_number,
        )
        accepted.append(row)
        existing_rows.append((row.topic, row.fact))  # prevent dupes within this batch
        if issue_number in issue_results:
            issue_results[issue_number].accepted.append(row)

    source_desc = f"file {args.file}" if args.file else f"{issues_scanned} issue(s) from {args.repo}"
    print(f"Scanned: {source_desc}")
    print(f"Rows found: {len(raw_rows)}")
    print(f"Accepted: {len(accepted)}")
    print(f"Rejected: {len(rejected)}")
    print(f"Duplicates: {len(duplicates)}")
    print()

    if rejected:
        print("Rejected rows:")
        for origin, excerpt, reason in rejected:
            print(f"  - [{origin}] '{excerpt}': {reason}")
        print()

    if duplicates:
        print("Duplicate rows (not added):")
        for origin, excerpt, existing_fact, kind in duplicates:
            label = "identical to" if kind == "exact" else "probable duplicate of"
            print(f"  - [{origin}] '{excerpt}': {label} '{existing_fact}'")
        print()

    print("Accepted rows:" if not args.apply else "Accepted rows to append:")
    print(render_table(accepted))
    print()

    if not args.apply:
        print("Dry run — nothing written. Re-run with --apply to append to "
              f"{args.knowledge}.")
        return 0

    if accepted:
        append_to_knowledge(args.knowledge, accepted)
        print(f"Appended {len(accepted)} row(s) to {args.knowledge}.")
    else:
        print(f"No rows to append; {args.knowledge} left unchanged.")

    if args.close:
        for number, result in issue_results.items():
            n_accepted = len(result.accepted)
            n_rejected = len(result.rejected)
            n_dup = len(result.duplicates)
            if n_accepted == 0 and n_rejected == 0 and n_dup == 0:
                continue  # nothing in this issue's body looked like a row; leave it alone
            reasons = "; ".join(f"'{excerpt}': {reason}" for excerpt, reason in result.rejected)
            body = f"Merged {n_accepted} rows into docs/KNOWLEDGE.md; {n_rejected} rejected"
            body += f": {reasons}" if reasons else ""
            if n_dup:
                body += f"; {n_dup} duplicate(s) skipped"
            gh_comment_and_close(args.repo, number, body)
            print(f"Commented on and closed issue #{number}.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
