#!/usr/bin/env bash
# Проверка canonical cross-references (тонкая обёртка над Python-реализацией)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

python3 meta/scripts/validate-canonical-refs.py
