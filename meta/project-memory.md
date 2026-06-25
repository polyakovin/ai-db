# Project Memory — ai-db

## Основное
- **Название:** ai-db
- **Тип:** база знаний (Obsidian vault + Git-репозиторий)
- **Создан:** 2026-06-24
- **Язык/стек:** Markdown, Shell, Obsidian

## Конвенции
- Файлы называть на английском в kebab-case: `agent-harness.md`, `working-with-coding-agents.md`.
- Обзорные страницы — `OVERVIEW.md`.
- Одна мысль — один файл, без дублей. Ссылаться на canonical note.
- Порядок разделов фиксирован: navigation → patterns → tools → sources → meta.
- Внешние источники — с frontmatter (title, url, type, category, tags, added, status).
- После изменений — запустить `meta/scripts/validate-vault.sh`.
- После коммита — сразу `git push`.

## Принятые решения
| Дата | Решение | Причина | Альтернативы |
|------|---------|---------|--------------|
| 2026-06-24 | Ветка master вместо main | HEAD ремоута — master | main |
| 2026-06-24 | Файловая структура harness (meta/, AGENTS.md) в корне | Единая точка входа для агента | Разнести по проекту |

## Предпочтения
- Русский язык для контента, английский для имён файлов и служебных файлов.
- Все Markdown-ссылки — локальные, относительные (не URL).
