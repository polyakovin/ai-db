# AGENTS.md — правила для AI-агента

## Проект
- **Название:** ai-db
- **Тип агента:** coding / research (обслуживание базы знаний об AI-агентах)
- **Язык:** Markdown, Shell, YAML
- **Цель:** Поддерживать и развивать базу знаний о практическом применении AI-агентов: добавлять источники, писать концепции, фиксировать паттерны, проверять целостность.

## Структура базы знаний

| Раздел | Назначение |
|--------|------------|
| `concepts/` | Базовые понятия и архитектурные блоки |
| `patterns/` | Повторяемые проектные решения |
| `tools/` | Инструменты, модели, SDK, платформы |
| `practices/` | Workflows, recipes и how-to |
| `cases/` | Практические сценарии |
| `sources/` | Внешние источники и provenance |

## Правила работы с файлами
- Файлы — kebab-case, английские названия.
- Обзорные страницы — `overview.md`.
- Одна мысль — один файл, без дублей.
- Ссылки только на существующие файлы.
- После изменений: `bash scripts/validate-vault.sh`.
- Перед коммитом: установлен `.githooks/pre-commit`.

## Как агент работает

1. **Перед началом** — прочитай `plan/current.md`, загрузи skill, проверь git status.
2. **Выполняй** — минимальными порциями, каждая с проверкой.
3. **Пиши evidence** — результаты и наблюдения в `plan/evidence/`.
4. **Фиксируй решения** — важные выборы, причины, альтернативы в `plan/decisions.md`.
5. **Проверяй** — валидацию vault после каждого meaningful изменения.
6. **Commit** — atomic, message с ссылкой на задачу.
7. **Push** — сразу после коммита `git push`, чтобы репозиторий на GitHub был актуален.

## Ограничения (STOP)
- Не изменяй файлы вне scope задачи.
- Не добавляй speculative заметки «на будущее».
- Не удаляй заметки, которые не ты создал (если не указано иное).
- Не оставляй битые Markdown-ссылки как заглушки.
- Если не уверен — запиши вопрос в `plan/decisions.md`.
- Destructive actions (удаление файлов, git reset) требуют подтверждения.

## Инструменты
- shell, filesystem, git
- web_search, web_extract — для исследования и добавления источников
- vision_analyze — для скриншотов и изображений
- MCP — vkusvill (опционально)
- skill_view — загружать skills из `.hermes/skills/` и `meta/skills/`

## Проверки
| Тип | Команда |
|-----|---------|
| Валидация vault | `bash scripts/validate-vault.sh` |
| Markdown-ссылки | `bash scripts/validate-vault.sh` |

## Память проекта
- **System rules:** `.hermes/rules/project-rules.md`
- **Project memory:** `.hermes/memory/project-memory.md`
- **Work plan:** `plan/current.md`
- **Decisions:** `plan/decisions.md`
- **Security policy:** `.hermes/sandbox/security-policy.md`
- **Audit log:** `.hermes/observability/audit-log.md`

## Связанные материалы
- [Agent Harness — ai-db](concepts/agent-harness.md)
- [Работа с код-агентами — ai-db](practices/working-with-coding-agents.md)
- [Skills и правила — ai-db](patterns/agent-skills-and-rules.md)
