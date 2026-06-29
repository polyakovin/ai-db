#!/usr/bin/env bash
# Валидация проекта ai-db
set -euo pipefail

echo "🔎 Validation (ai-db)..."
script_dir="$(cd "$(dirname "$0")" && pwd)"
python3 "$script_dir/validate-vault.sh"
echo "✅ Validation passed"
