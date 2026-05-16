#!/usr/bin/env python3
"""PreToolUse hook (matcher: Bash): blocks destructive shell commands.

On a destructive command it writes a reason to stderr and exits 2, which tells Claude
Code to block the call and feed the reason back to Claude. Claude must then ask the
founder to run it manually if it is genuinely intended. Safe commands exit 0 silently.

This is a backstop, not a substitute for judgement. Edit the BLOCKED list to taste.
"""
import json
import re
import sys

# (regex, human-readable reason). Conservative — only genuinely destructive patterns.
BLOCKED = [
    (r"\brm\s+-\w*[rR]", "recursive delete (rm -r / rm -rf)"),
    (r"\bgit\s+push\b[^\n]*(--force\b|-f\b)", "force push — can overwrite remote history"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard — discards uncommitted work"),
    (r"\bgit\s+clean\s+-\w*f", "git clean -f — deletes untracked files"),
    (r"\bgit\s+checkout\s+--\s*\.\s*$", "git checkout -- . — discards all local changes"),
    (r"\bdd\b[^\n]*\bof=", "dd writing to a device"),
    (r"\bmkfs\b", "mkfs — formats a filesystem"),
    (r">\s*/dev/sd[a-z]", "writing directly to a disk device"),
    (r":\(\)\s*\{.*\};", "fork bomb"),
    (r"\bchmod\s+-R\s+777\b", "chmod -R 777 — recursive world-writable"),
    (r"\bRemove-Item\b[^\n]*-Recurse[^\n]*-Force", "PowerShell recursive force delete"),
    (r"\bformat\s+[A-Za-z]:", "Windows drive format"),
]


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)  # Cannot parse input — do not block.

    if data.get("tool_name") != "Bash":
        sys.exit(0)

    command = (data.get("tool_input") or {}).get("command", "") or ""
    for pattern, reason in BLOCKED:
        if re.search(pattern, command, re.IGNORECASE):
            sys.stderr.write(
                f"BLOCKED by bash-guardrails: {reason}.\n"
                f"Command: {command}\n"
                f"If this is genuinely intended, ask the founder to run it manually, "
                f"or edit .claude/hooks/bash-guardrails.py.\n"
            )
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
