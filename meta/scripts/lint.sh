#!/usr/bin/env bash
# Линтер для ai-db: проверка Markdown-ссылок и frontmatter
set -euo pipefail

echo "🔍 Lint checks (ai-db)..."
script_dir="$(cd "$(dirname "$0")" && pwd)"
python3 "$script_dir/validate-vault.sh"
echo "✅ Lint passed"
