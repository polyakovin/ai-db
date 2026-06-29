# AGENTS.md — правила для AI-агента

## Проект
- **Название:** ai-db
- **Тип агента:** coding / research (обслуживание базы знаний об AI-агентах)
- **Язык:** Markdown, Shell, YAML
- **Цель:** Поддерживать и развивать базу знаний о практическом применении AI-агентов: добавлять источники, писать концепции, фиксировать паттерны, проверять целостность.

## Структура базы знаний

| Раздел | Назначение |
|--------|------------|
| `patterns/` | Архитектурные блоки, проектные решения, workflow, recipes, learning path, case-карта, how-to |
| `tools/` | Инструменты, модели, SDK, платформы, сравнения |
| `sources/` | Внешние источники и provenance (tutorials, libraries, engineering patterns, research) |
| `meta/` | Скрипты, шаблоны, проектные skills |

## Правила работы с файлами
- Файлы — kebab-case, английские названия.
- Обзорные страницы — `OVERVIEW.md` (без frontmatter).
- Одна мысль — один файл, без дублей.
- Ссылки только на существующие файлы.
- После изменений — валидация vault.
- Перед коммитом: установлен `.githooks/pre-commit`.

## Как агент работает

1. **Начинай с README.md** — главная навигация по проекту.
2. **Выполняй** — минимальными порциями, каждая с проверкой.
3. **Фиксируй решения** — важные выборы, причины, альтернативы в `meta/decisions.md` (создать при необходимости).
4. **Проверяй** — `python3 meta/scripts/validate-vault.sh` после каждого meaningful изменения.
5. **Commit** — atomic, message с ссылкой на задачу.
6. **Push** — сразу после коммита `git push`, чтобы репозиторий на GitHub был актуален.

## Ограничения (STOP)
- Не изменяй файлы вне scope задачи.
- Не добавляй speculative заметки «на будущее».
- Не удаляй заметки, которые не ты создал (если не указано иное).
- Не оставляй битые Markdown-ссылки как заглушки.
- Если не уверен — запиши вопрос в `meta/decisions.md`.
- Destructive actions (удаление файлов, git reset) требуют подтверждения.

## Проверки
| Тип | Команда |
|-----|---------|
| Валидация vault (битые ссылки) | `python3 meta/scripts/validate-vault.sh` |
| Canonical cross-reference | `python3 meta/scripts/validate-canonical-refs.py` |
| Генерация canonical-map | `python3 meta/scripts/generate-canonical-map.py` |

Pre-commit hook (`.githooks/pre-commit`) выполняет все три проверки автоматически.

## Память проекта
- **Project rules:** `meta/project-rules.md`
- **Project memory:** `meta/project-memory.md`
- **Security policy:** `meta/security-policy.md`
- **Audit log:** `meta/audit-log.md`

## Связанные материалы
- [Agent Harness — ai-db](patterns/architecture-design/agent-harness.md)
- [Работа с код-агентами — ai-db](patterns/implementation/working-with-coding-agents.md)
- [Skills и правила — ai-db](patterns/implementation/agent-skills-and-rules.md)
