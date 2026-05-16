#!/usr/bin/env python3
"""SessionStart hook: re-injects AlanGlucose context after startup, compact, or clear.

Prints plain text to stdout, which Claude Code adds to the session context. The script
fails silent (exit 0) on any error — a broken hook must never break a session.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "state"


def read(path, limit=6000):
    try:
        return path.read_text(encoding="utf-8")[:limit].strip()
    except Exception:
        return ""


def git_status():
    try:
        out = subprocess.run(
            ["git", "status", "--short", "--branch"],
            cwd=str(ROOT), capture_output=True, text=True, timeout=10,
        )
        return out.stdout.strip() or "(clean working tree)"
    except Exception:
        return "(git status unavailable)"


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    source = data.get("source", "startup")

    out = [
        "=== ALANGLUCOSE — SESSION CONTEXT ===",
        f"(restored by the SessionStart hook; source: {source})",
        "",
        "--- state/active_context.md ---",
        read(STATE / "active_context.md") or "(empty)",
        "",
        "--- state/progress.md ---",
        read(STATE / "progress.md") or "(empty)",
    ]

    handover = read(STATE / "handover-latest.md")
    if handover and "no handover written yet" not in handover:
        out += ["", "--- state/handover-latest.md (restored after compaction) ---", handover]

    out += [
        "",
        "--- git status ---",
        git_status(),
        "",
        "Now read CLAUDE.md and .claude/SYCOPHANCY.md. Lead with the critique, not encouragement.",
        "=== END SESSION CONTEXT ===",
    ]
    print("\n".join(out))
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
