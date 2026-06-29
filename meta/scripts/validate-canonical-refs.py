#!/usr/bin/env python3
"""Проверяет, что все текстовые упоминания canonical-инструментов в patterns/ и tools/
обёрнуты в markdown-ссылку на их страницу."""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
os.chdir(ROOT)

# Список canonical страниц и их ключевых слов
# (target_path_from_root, [keyword1, keyword2, ...])
CANONICAL_MAP = [
    ("tools/platforms/openai.md",     ["OpenAI", "Codex CLI", "Responses API", "Agents SDK", "Realtime API"]),
    ("tools/platforms/anthropic.md",  ["Anthropic", "Claude Code", "Claude Opus", "Claude Sonnet", "Claude Haiku", "Claude Cowork", "Computer Use"]),
    ("tools/platforms/mistral.md",    ["Mistral", "Codestral", "Le Chat"]),
    ("tools/platforms/deepseek.md",   ["DeepSeek"]),
    ("tools/platforms/qwen.md",       ["Qwen"]),
    ("tools/platforms/z-ai.md",       ["Z.ai", "Zhipu AI", "AutoGLM"]),
    ("tools/gemini.md",               ["Gemini"]),
    ("tools/perplexity.md",           ["Perplexity"]),
    ("tools/models/mimo-code.md",     ["MiMo Code"]),
    ("tools/frameworks/langgraph.md", ["LangGraph"]),
    ("tools/frameworks/autogen.md",   ["AutoGen"]),
    ("tools/frameworks/crewai.md",    ["CrewAI"]),
    ("tools/frameworks/semantic-kernel.md", ["Semantic Kernel"]),
    ("tools/frameworks/llamaindex.md",["LlamaIndex"]),
    ("tools/frameworks/dify.md",      ["Dify"]),
    ("tools/vector-dbs/pinecone.md",  ["Pinecone"]),
    ("tools/rerankers.md",            ["Cohere Rerank", "BGE", "Jina"]),
    ("tools/embedding-models.md",     ["Voyage AI"]),
]


def relative_path(from_abs: Path, to_abs: Path) -> str:
    rel = os.path.relpath(str(to_abs), start=str(from_abs))
    if rel.startswith("./"):
        rel = rel[2:]
    return rel


def check_file(filepath: Path) -> list[str]:
    """Проверяет один .md файл на bare mentions."""
    violations = []

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Определяем directory для рассчёта relative paths
    filedir = filepath.parent

    for target_rel, keywords in CANONICAL_MAP:
        target_abs = (ROOT / target_rel).resolve()
        if filepath.resolve() == target_abs:
            continue  # пропускаем сам canonical-файл

        rel_path = relative_path(filedir, target_abs)

        for term in keywords:
            if term not in "".join(lines):
                continue

            term_escaped = re.escape(term)

            for i, line in enumerate(lines, 1):
                line_stripped = line.strip()

                # Пропускаем заголовки
                if line_stripped.startswith("#"):
                    continue

                # Пропускаем блоки кода
                if line_stripped.startswith("```"):
                    continue

                # Пропускаем таблицы (содержат |) — первая колонка = метка
                if "|" in line and term in line:
                    continue

                if term not in line:
                    continue

                # Ищем позиции термина, не внутри markdown-ссылки и не в списке источников
                for m in re.finditer(term_escaped, line):
                    pos = m.start()
                    after = line[pos + len(term):]

                    # Уже ссылка: [term](url)
                    if after.lstrip().startswith("]("):
                        continue

                    # Термин внутри [...](...) где после ] идёт (
                    full_ref_pattern = re.compile(
                        r"\[([^\]]*" + term_escaped + r"[^\]]*)\]\([^)]+\)"
                    )
                    if full_ref_pattern.search(line):
                        continue

                    # Термин внутри кода (инлайн `код`)
                    # Проверяем что это не внутри backtick
                    before = line[:pos]
                    if before.count("`") % 2 == 1:
                        continue

                    violations.append(
                        f"{filepath.relative_to(ROOT)}:{i}: bare mention of "
                        f'"{term}" — should be [{term}]({rel_path})'
                    )
                    break  # одно нарушение на строку хватит

    return violations


def main():
    source_dirs = ["patterns", "tools"]
    all_violations = []

    for sdir in source_dirs:
        srcdir_abs = ROOT / sdir
        if not srcdir_abs.exists():
            continue
        for md_file in sorted(srcdir_abs.rglob("*.md")):
            base = md_file.name
            if base.upper() == "OVERVIEW.MD":
                continue
            violations = check_file(md_file)
            all_violations.extend(violations)

    if all_violations:
        print("🔍 Canonical cross-reference check: violations found")
        print("=" * 70)
        for v in all_violations:
            print(v)
        print("=" * 70)
        print(f"\n❌ {len(all_violations)} bare mention(s) found.")
        print("Each technology mention should be a wiki-link to its canonical page.")
        sys.exit(1)

    print("✅ All technology mentions are properly linked to canonical pages.")
    sys.exit(0)


if __name__ == "__main__":
    main()
