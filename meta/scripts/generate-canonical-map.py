#!/usr/bin/env python3
"""Generate meta/canonical-map.json from tools/ structure.

Scans tools/ for .md files, extracts display names from:
  1. frontmatter `title:` field
  2. h1 fallback
  3. filename fallback (kebab → Title Case)
Writes a JSON object: { "tool-slug": { "name": "Display Name", "path": "tools/path/to/file.md" }, ... }
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # ai-db/
TOOLS = ROOT / "tools"
MAP_PATH = ROOT / "meta" / "canonical-map.json"

EXCLUDE_DIRS = {"__pycache__", ".git", "meta", "sources", "patterns", "assets"}
EXCLUDE_FILES = {"index.md", "summary.md", "_sidebar.md"}


def extract_frontmatter_title(text: str) -> str | None:
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("title:"):
                val = line[len("title:"):].strip().strip("\"'")
                if val:
                    return val
    return None


def extract_h1(text: str) -> str | None:
    m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def kebab_to_title(name: str) -> str:
    """Convert kebab-case-file-name → Title Case File Name."""
    return " ".join(word.capitalize() for word in name.replace("-", " ").split())


def find_md_files(directory: Path) -> list[Path]:
    files = []
    for f in sorted(directory.rglob("*.md")):
        # skip hidden dirs
        if any(part.startswith(".") for part in f.relative_to(ROOT).parts):
            continue
        if f.name in EXCLUDE_FILES:
            continue
        files.append(f)
    return files


def build_map() -> dict:
    md_files = list(TOOLS.rglob("*.md"))
    md_files = [f for f in md_files
                if f.name not in EXCLUDE_FILES
                and not any(part.startswith(".") for part in f.relative_to(TOOLS).parts)]

    can_map = {}
    for fpath in md_files:
        rel = fpath.relative_to(ROOT)
        slug = fpath.stem  # filename without .md

        text = fpath.read_text(encoding="utf-8")
        name = extract_frontmatter_title(text) or extract_h1(text) or kebab_to_title(slug)

        can_map[slug] = {
            "name": name,
            "path": str(rel),
        }

    return can_map


def main():
    can_map = build_map()
    MAP_PATH.write_text(
        json.dumps(can_map, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"✓ canonical-map.json: {len(can_map)} entries → {MAP_PATH}")


if __name__ == "__main__":
    main()
