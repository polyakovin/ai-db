#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

FAILURES=0
OK_LINKS=0
LINK_RE='\[[^][]+\]\(([^)]*)\)'

check_target() {
    local source_file="$1"
    local line_no="$2"
    local href="$3"
    local target filedir

    href="${href%%#*}"
    [[ -z "$href" ]] && return
    [[ "$href" == http://* || "$href" == https://* || "$href" == mailto:* ]] && return
    [[ "$href" == *.svg || "$href" == *.png || "$href" == *.jpg || "$href" == *.jpeg || "$href" == *.gif || "$href" == *.ico || "$href" == *.webp ]] && return

    filedir="$(dirname "$source_file")"
    if [[ "$href" == /* ]]; then
        target="$ROOT$href"
    else
        target="$filedir/$href"
    fi

    if [[ -f "$target" || -d "$target" ]]; then
        OK_LINKS=$((OK_LINKS + 1))
    else
        echo "Broken link: $source_file:$line_no -> $href"
        FAILURES=$((FAILURES + 1))
    fi
}

while IFS= read -r -d '' file; do
    line_no=0
    while IFS= read -r line || [[ -n "$line" ]]; do
        line_no=$((line_no + 1))
        rest="$line"
        while [[ "$rest" =~ $LINK_RE ]]; do
            match="${BASH_REMATCH[0]}"
            href="${BASH_REMATCH[1]}"
            check_target "$file" "$line_no" "$href"
            rest="${rest#*"$match"}"
        done
    done < "$file"
done < <(find . -path ./.git -prune -o -name '*.md' -type f -print0)

while IFS= read -r -d '' file; do
    [[ "$(basename "$file")" == "overview.md" || "$(basename "$file")" == "OVERVIEW.md" ]] && continue

    if [[ "$(sed -n '1p' "$file")" != "---" ]]; then
        echo "Missing frontmatter: $file"
        FAILURES=$((FAILURES + 1))
        continue
    fi

    for key in title url type category tags added status; do
        if ! awk 'NR == 1 { next } /^---$/ { exit } { print }' "$file" | grep -q "^$key:"; then
            echo "Missing frontmatter key '$key': $file"
            FAILURES=$((FAILURES + 1))
        fi
    done
done < <(find ./sources -name '*.md' -type f -print0)

echo "Valid local markdown links: $OK_LINKS"

if [[ "$FAILURES" -gt 0 ]]; then
    echo "Vault validation failed: $FAILURES issue(s)."
    exit 1
fi

echo "Vault validation passed."
