#!/usr/bin/env python3
"""Validate vault: check all wiki-link [[...]] and markdown [...](...) in .md files."""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
EXCLUDE_PREFIXES = ("meta/", ".git/", "assets/")


def find_md_files(root: Path):
    for f in root.rglob("*.md"):
        rel = f.relative_to(root)
        if any(str(rel).startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        yield f


def resolve_href(source_file: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:")):
        return None  # external
    if href.rsplit(".", 1)[-1] in {"svg", "png", "jpg", "jpeg", "gif", "ico", "webp"}:
        return None  # image
    # strip anchor fragment for file check
    href_clean = href.split("#")[0]
    if not href_clean:
        return None
    if href_clean.startswith("/"):
        target = ROOT / href_clean.lstrip("/")
    else:
        target = (source_file.parent / href_clean).resolve()
    return target


def extract_wiki_links(text: str):
    """Extract wiki-link targets, excluding examples with '...' placeholder."""
    links = re.findall(r"\[\[([^]|]+)(?:\|[^]]*)?\]\]", text)
    return [l for l in links if "..." not in l]


def extract_md_links(text: str):
    return re.findall(r"\[([^]]*)\]\(([^)]+)\)", text)


def main():
    broken = 0
    for fpath in find_md_files(ROOT):
        text = fpath.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            # wiki-links
            for target_raw in extract_wiki_links(line):
                target = resolve_href(fpath, target_raw)
                if target is None:
                    continue
                if not target.exists():
                    print(f"Broken link: {fpath.relative_to(ROOT)}:{line_no} -> [[{target_raw}]] → {target}")
                    broken += 1
            # markdown links
            for _text, href in extract_md_links(line):
                target = resolve_href(fpath, href)
                if target is None:
                    continue
                if not target.exists():
                    print(f"Broken link: {fpath.relative_to(ROOT)}:{line_no} -> [{_text}]({href}) → {target}")
                    broken += 1

    if broken > 0:
        print(f"\nVault validation failed: {broken} broken link(s).")
        sys.exit(1)
    print("All links valid.")
    print("Vault validation passed.")


if __name__ == "__main__":
    main()
