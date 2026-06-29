#!/usr/bin/env python3
"""Check that every technology mention in patterns/ and tools/ is a wiki-link.

How it works:
1. Collects all .md files under tools/ (excluding OVERVIEW.md, comparisons.md)
2. For each file, reads frontmatter title + H1 heading + filename
3. Extracts keywords to search for bare mentions
4. Scans all patterns/*.md and tools/*.md for those keywords without links

Adding a new canonical page under tools/ automatically includes it in checks.
No manual mapping required.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)

CONTENT_DIRS = ["patterns", "tools"]
EXCLUDE_FILES = {"OVERVIEW.md", "overview.md", "comparisons.md"}


def extract_keywords(fp: Path) -> list[str]:
    """Extract search keywords from a canonical page: frontmatter title, H1, filename."""
    keywords = []
    raw = fp.read_text(encoding="utf-8")

    # 1. Frontmatter title
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, re.DOTALL)
    if fm:
        m = re.search(r"^title:\s*(.+)$", fm.group(1), re.MULTILINE)
        if m:
            keywords.append(m.group(1).strip())

    # 2. H1 heading (first # line after frontmatter)
    body = raw.split("---", 2)[-1] if "---" in raw else raw
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    if m:
        keywords.append(m.group(1).strip())

    # 3. Filename stem (kebab-case -> Title Case)
    stem = fp.stem
    keywords.append(stem.replace("-", " ").title())
    if stem.isupper() and len(stem) <= 8:
        keywords.append(stem)

    # Deduplicate, keep order, drop short entries
    seen: set[str] = set()
    out: list[str] = []
    for kw in keywords:
        k = kw.lower().strip()
        if k and len(k) > 2 and k not in seen:
            seen.add(k)
            out.append(kw.strip())
    return out


def rel_path(from_dir: Path, to_abs: Path) -> str:
    r = os.path.relpath(str(to_abs), start=str(from_dir))
    return r[2:] if r.startswith("./") else r


def collect_canonical() -> list[tuple[Path, str, list[str]]]:
    """Return list of (abs_path, relative_path, [keywords]) for every canonical page."""
    pages: list[tuple[Path, str, list[str]]] = []
    for md in sorted((ROOT / "tools").rglob("*.md")):
        if md.name in EXCLUDE_FILES:
            continue
        kws = extract_keywords(md)
        pages.append((md.resolve(), str(md.relative_to(ROOT)), kws))
    return pages


def check_file(path: Path, pages: list[tuple[Path, str, list[str]]]) -> list[str]:
    """Return violation messages for bare mentions in a single .md file."""
    violations: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    filedir = path.parent

    for target_abs, canonical_rel, keywords in pages:
        if path.resolve() == target_abs:
            continue

        joined = "".join(lines)
        term_filter = [t for t in keywords if t in joined]
        if not term_filter:
            continue

        for term in term_filter:
            pattern = re.compile(re.escape(term))
            rel = rel_path(filedir, target_abs)

            for i, line in enumerate(lines, 1):
                s = line.strip()
                if not s or s.startswith("#") or s.startswith("```"):
                    continue
                if "|" in line and term in line:
                    continue
                if term not in line:
                    continue

                for m in pattern.finditer(line):
                    pos = m.start()
                    before = line[:pos]
                    after = line[pos + len(term) :]

                    # Part of description after an existing link: [X](url) — Y
                    if "]" in before and "](" in line:
                        lb = before.rfind("]")
                        if before[lb + 1 :].startswith("("):
                            continue

                    # Already wrapped: [term](url)
                    if after.lstrip().startswith("]("):
                        continue

                    # Inside [text](url) somewhere
                    link_pat = re.compile(
                        r"\[([^\]]*" + re.escape(term) + r"[^\]]*)\]\([^)]+\)"
                    )
                    if link_pat.search(line):
                        continue

                    # Inside inline code
                    if before.count("`") % 2 == 1:
                        continue

                    # URL path, not a technology mention
                    if term.lower() in line.lower() and (
                        ".com/" in line or "/api" in line
                    ):
                        continue

                    # ColQwen != Qwen
                    if "Qwen" in term and "ColQwen" in line:
                        continue

                    # Bullet list label: "- **Name**: ..."
                    if s.startswith("- "):
                        rest = s[2:]
                        if rest.startswith("**") and "**" in rest:
                            label = rest.split("**")[1]
                            if label == term:
                                continue

                    violations.append(
                        f"{path.relative_to(ROOT)}:{i}: bare mention of "
                        f'"{term}" -> [{term}]({rel})'
                    )
                    break  # one per line

    return violations


def main() -> None:
    pages = collect_canonical()
    all_v = []

    for content_dir in CONTENT_DIRS:
        d = ROOT / content_dir
        if not d.exists():
            continue
        for md in sorted(d.rglob("*.md")):
            if md.name in EXCLUDE_FILES:
                continue
            all_v.extend(check_file(md, pages))

    if all_v:
        print("Canonical cross-reference check: violations found")
        print("=" * 70)
        for v in all_v:
            print(v)
        print("=" * 70)
        print(f"\n{len(all_v)} bare mention(s) found.")
        sys.exit(1)

    print("All technology mentions are properly linked to canonical pages.")
    sys.exit(0)


if __name__ == "__main__":
    main()
