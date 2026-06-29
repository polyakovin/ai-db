#!/usr/bin/env bash
# Проверка: все текстовые упоминания canonical-инструментов в patterns/ и tools/
# должны быть обёрнуты в markdown-ссылку.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

FAILURES=0
SOURCE_DIRS=("patterns" "tools")

# Список canonical страниц и их ключевых слов для поиска
# Формат: "tools/target.md:keyword1:keyword2:..."
declare -a CANONICAL_MAP=(
  "tools/platforms/openai.md:OpenAI:GPT-5.5:GPT-5:Codex CLI:Responses API:Agents SDK:Realtime API"
  "tools/platforms/anthropic.md:Anthropic:Claude Code:Claude Opus:Claude Sonnet:Claude Haiku:Claude Cowork:Computer Use"
  "tools/platforms/mistral.md:Mistral:Codestral:Le Chat"
  "tools/platforms/deepseek.md:DeepSeek"
  "tools/platforms/qwen.md:Qwen"
  "tools/platforms/z-ai.md:Z.ai:Zhipu AI:GLM-5:AutoGLM"
  "tools/gemini.md:Gemini"
  "tools/perplexity.md:Perplexity"
  "tools/models/mimo-code.md:MiMo Code:MiMo-V2"
  "tools/frameworks/langgraph.md:LangGraph"
  "tools/frameworks/autogen.md:AutoGen"
  "tools/frameworks/crewai.md:CrewAI"
  "tools/frameworks/semantic-kernel.md:Semantic Kernel"
  "tools/frameworks/llamaindex.md:LlamaIndex"
  "tools/frameworks/dify.md:Dify"
  "tools/vector-dbs/pinecone.md:Pinecone"
  "tools/rerankers.md:Cohere Rerank:BGE:Jina"
  "tools/embedding-models.md:Voyage AI:voyage-4"
)

# Вспомогательная функция: рассчитать относительный путь от файла до canonical-страницы
relative_path() {
  local from_dir="$1"
  local to_file="$2"
  python3 -c "
import os.path
from_path = os.path.normpath('$from_dir')
to_path = os.path.normpath('$to_file')
rel = os.path.relpath(to_path, from_path)
# Нормализация: убираем './' в начале для консистентности
if rel.startswith('./'):
    rel = rel[2:]
print(rel)
"
}

echo "🔍 Checking canonical cross-references..."

for entry in "${CANONICAL_MAP[@]}"; do
  target="${entry%%:*}"
  keywords="${entry#*:}"

  IFS=':' read -ra TERMS <<< "$keywords"

  for dir in "${SOURCE_DIRS[@]}"; do
    canonical_abs="$ROOT/$target"

    while IFS= read -r -d '' srcfile; do
      # Пропускаем сам canonical-файл и overview-файлы
      basefile="$(basename "$srcfile")"
      [[ "$basefile" == "OVERVIEW.md" || "$basefile" == "overview.md" ]] && continue

      src_abs="$(realpath "$srcfile")"
      [[ "$src_abs" == "$canonical_abs" ]] && continue

      # Определяем правильный относительный путь от srcfile до canonical_abs
      src_dir="$(dirname "$src_abs")"
      rel_path="$(relative_path "$src_dir" "$canonical_abs")"

      for term in "${TERMS[@]}"; do
        # Шаблон: слово НЕ внутри markdown-ссылки [...](...) и НЕ в заголовке
        # Используем python3 для надёжного парсинга
        violations=$(python3 -c "
import re, sys

with open('$src_abs', 'r') as f:
    lines = f.readlines()

term = '$term'
term_escaped = re.escape(term)

# Шаблон для markdown-ссылки: [text](url)
link_pattern = re.compile(r'\[' + term_escaped + r'\]\([^)]+\)')

for i, line in enumerate(lines, 1):
    # Пропускаем заголовки
    if line.strip().startswith('#'):
        continue
    # Пропускаем строки с кодом (блоки ```)
    if line.strip().startswith('\`\`\`'):
        continue
    # Пропускаем таблицы (содержат |)
    if '|' in line and term in line:
        # Проверяем — первая колонка таблицы (это метка, не требующая ссылки)
        # Пропускаем, т.к. таблицы сравнения не трогаем
        continue
    # Проверяем не в ссылке ли уже
    if term in line:
        # Находим все вхождения
        for m in re.finditer(term_escaped, line):
            pos = m.start()
            # Проверяем — не внутри ли [...](...) ?
            # Ищем [ назад от позиции
            before = line[:pos]
            bracket_open = before.rfind('[')
            bracket_close = before.rfind(']')
            paren_open = before.rfind('(')
            paren_close = before.rfind(')')

            # Простейшая эвристика: если между [ и ] есть наш термин и затем (url) — это ссылка
            link_before = re.search(r'\[' + term_escaped + r'\]\([^)]*\)', before + term)
            if link_before:
                # Уже в ссылке
                next_link = re.search(r'\[' + term_escaped + r'\]\([^)]*\)', line[pos:])
                if next_link and next_link.start() == 0:
                    continue

            # Дополнительная проверка: термин внутри уже существующей ссылки
            # Ищем обратно: [текст](url) — если термин между [ и ] и за ним следует ](
            after = line[pos + len(term):]
            if after.startswith(']('):
                continue
            # Ищем полную ссылку, содержащую термин
            full_ref = re.search(r'\[([^\]]*' + term_escaped + r'[^\]]*)\]\([^)]+\)', line)
            if full_ref:
                continue

            print(f'{srcfile[len(\"$ROOT/\") + 1:]}:{i}: bare mention of \"{term}\" — should be [{term}]({rel_path})')
" 2>/dev/null || true)

        if [[ -n "$violations" ]]; then
          echo "$violations"
          FAILURES=$((FAILURES + 1))
        fi
      done
    done < <(find "$dir" -name '*.md' -type f -print0 2>/dev/null || true)
  done
done

if [[ "$FAILURES" -gt 0 ]]; then
  echo ""
  echo "❌ Canonical cross-reference check: $FAILURES bare mention(s) found."
  echo "ℹ️  Each technology should be a wiki-link to its canonical page."
  echo ""
  exit 1
fi

echo "✅ All technology mentions are properly linked to canonical pages."
