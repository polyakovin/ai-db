#!/usr/bin/env bash
# Валидация проекта ai-db
set -euo pipefail

echo "🔎 Validation (ai-db)..."
bash scripts/validate-vault.sh
echo "✅ Validation passed"
