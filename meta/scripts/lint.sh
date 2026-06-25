#!/usr/bin/env bash
# Линтер для ai-db: проверка Markdown-ссылок и frontmatter
set -euo pipefail

echo "🔍 Lint checks (ai-db)..."
bash scripts/validate-vault.sh
echo "✅ Lint passed"
