#!/usr/bin/env bash
# Тесты для ai-db: проверка целостности vault
set -euo pipefail

echo "🧪 Test suite (ai-db)..."
script_dir="$(cd "$(dirname "$0")" && pwd)"
bash "$script_dir/validate-vault.sh"
echo "✅ All tests passed"
