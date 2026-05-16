#!/usr/bin/env python3
"""Stop hook: appends a one-line session entry to state/session-log.md.

A lightweight audit trail. Fails silent (exit 0) on any error.
"""
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "state" / "session-log.md"


def count_entries(transcript_path):
    try:
        lines = Path(transcript_path).read_text(encoding="utf-8").splitlines()
        return sum(1 for ln in lines if ln.strip())
    except Exception:
        return 0


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}

    session_id = str(data.get("session_id", "unknown"))
    transcript_path = data.get("transcript_path", "")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entries = count_entries(transcript_path) if transcript_path else 0

    line = f"- **{stamp}** — session `{session_id[:8]}` ended ({entries} transcript entries)\n"
    try:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
