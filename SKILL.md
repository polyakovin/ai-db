---
name: ai-db
description: База знаний по AI-агентам — Obsidian vault
---

# ai-db — база знаний по AI-агентам

Карта проекта, конвенции и workflow.

## Структура

| Раздел | Назначение |
|--------|------------|
| `patterns/` | Архитектурные блоки, learning path, recipes, case-карта |
| `tools/` | Модели, SDK, фреймворки |
| `sources/` | Внешние источники (tutorials, libraries, engineering patterns, research) |
| `meta/` | Скрипты, шаблоны, проектные skills, rules |

## Начало работы

1. Прочитай `README.md` — главная навигация.
2. Прочитай `AGENTS.md` — правила для агента.
3. Для добавления источника — загрузи skill `add-source` из `meta/skills/add-source.md`.

## Рабочий цикл

1. Валидация после изменений: `bash meta/scripts/validate-vault.sh`
2. Коммит: `git add -A && git commit -m "..." && git push`

## Правила

- Файлы kebab-case, английские названия.
- Обзорные страницы — `OVERVIEW.md` (без frontmatter).
- Одна мысль — один файл, без дублей.
- Ссылки только на существующие файлы.

## Навигация по контенту

- Learning path: `patterns/OVERVIEW.md` → раздел "Learning path"
- Обзор patterns: `patterns/OVERVIEW.md`
- Обзор tools: `tools/OVERVIEW.md`
- Обзор sources: `sources/OVERVIEW.md`
