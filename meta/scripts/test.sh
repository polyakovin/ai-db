#!/usr/bin/env bash
# Тесты для ai-db: проверка целостности vault
set -euo pipefail

echo "🧪 Test suite (ai-db)..."
bash scripts/validate-vault.sh
echo "✅ All tests passed"
