from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TEXT_EXTENSIONS = {".md", ".py", ".ipynb", ".csv", ".txt", ".yml", ".yaml", ".toml", ".json"}
SKIP_PARTS = {".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints"}

assistant_names = ["chat" + "gpt", "open" + "ai", "co" + "pilot", "gem" + "ini"]
checks = {
    "email address": re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    "Windows user path": re.compile(r"(?i)\b[A-Z]:\\\\Users\\\\[^\\\\\s\"]+"),
    "Unix home path": re.compile(r"(?:/Users/|/home/)[^/\s\"]+"),
    "student identifier": re.compile(r"(?i)\bstudent\s*(?:id|number)\s*[:#-]?\s*\d{7,10}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credential assignment": re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]+"),
    "assistant reference": re.compile("(?i)\\b(?:" + "|".join(assistant_names) + ")\\b"),
}

allow_email_suffixes = ("@users.noreply.github.com",)
problems = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    if any(part in SKIP_PARTS for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for label, pattern in checks.items():
        for match in pattern.finditer(text):
            value = match.group(0)
            if label == "email address" and value.lower().endswith(allow_email_suffixes):
                continue
            line = text.count("\n", 0, match.start()) + 1
            problems.append(f"{path.relative_to(ROOT)}:{line}: {label}")

if problems:
    print("Safety scan failed:")
    print("\n".join(problems))
    raise SystemExit(1)

print("Safety scan passed.")
