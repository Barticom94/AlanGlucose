#!/usr/bin/env python3
"""Optional SessionStart hook (matcher: compact|clear): re-injects the handover after a compaction.

At normal startup nothing is needed — CLAUDE.md imports AGENTS.md and the two live state
files. After a compaction this prints state/handover-latest.md (written by the PreCompact
hook) plus a short git status, as a belt-and-braces restore. Fails silent (exit 0).
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
    source = data.get("source", "")
    if source not in ("compact", "clear"):
        sys.exit(0)

    out = ["=== ALANGLUCOSE — CONTEXT RESTORED AFTER " + source.upper() + " ==="]
    handover = read(STATE / "handover-latest.md")
    if handover:
        out += ["", handover]
    out += ["", "--- git status ---", git_status(),
            "", "Re-read AGENTS.md and state/active_context.md before continuing.",
            "=== END ==="]
    print("\n".join(out))
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
