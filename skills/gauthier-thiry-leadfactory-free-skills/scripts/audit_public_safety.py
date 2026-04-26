#!/usr/bin/env python3
"""Fail if a folder contains obvious secrets or private LeadFactory artifacts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = {
    "api_key_name": re.compile(
        r"\b("
        r"SUPABASE|SERVICE_ROLE|OPENAI_API_KEY|ANTHROPIC_API_KEY|"
        r"GEMINI_API_KEY|GOOGLE_API_KEY|FAL_KEY|SCRAPECREATORS|"
        r"STRIPE_SECRET|GH_TOKEN|GITHUB_TOKEN|BEARER"
        r")\b",
        re.IGNORECASE,
    ),
    "secret_like_value": re.compile(
        r"\b("
        r"sk-[A-Za-z0-9_-]{20,}|"
        r"ghp_[A-Za-z0-9_]{20,}|"
        r"github_pat_[A-Za-z0-9_]{20,}|"
        r"AIza[0-9A-Za-z_-]{20,}"
        r")\b"
    ),
    "private_local_path": re.compile(r"/Users/[^/\s]+/(brainOS|leadfactory|Desktop/LeadFactory)", re.IGNORECASE),
    "admin_url": re.compile(r"https?://app\.leadfactory\.my/admin", re.IGNORECASE),
    "env_file_reference": re.compile(r"(^|/)\.env(\.|$)|\.env\.local", re.IGNORECASE),
    "private_artifact": re.compile(
        r"(_session-analysis|state\.json|cron\.log|launchd|\.zip|\.docx|\.pdf)$",
        re.IGNORECASE,
    ),
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".csv",
    ".json",
    ".yaml",
    ".yml",
    ".py",
    ".js",
    ".ts",
    ".html",
    ".css",
}


def should_scan(path: Path) -> bool:
    if any(part in {".git", "__pycache__", "node_modules"} for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Folder to audit before public sharing.")
    args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()

    if not root.exists():
        print(f"ERROR: path does not exist: {root}")
        return 2

    findings: list[str] = []

    for path in root.rglob("*"):
        relative = path.relative_to(root)
        rel_text = str(relative)
        for name, pattern in PATTERNS.items():
            if pattern.search(rel_text):
                findings.append(f"{relative}: suspicious path ({name})")

        if not should_scan(path):
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            findings.append(f"{relative}: could not read ({exc})")
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            for name, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{relative}:{line_number}: {name}")

    if findings:
        print("PUBLIC SAFETY AUDIT FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("PUBLIC SAFETY AUDIT PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
