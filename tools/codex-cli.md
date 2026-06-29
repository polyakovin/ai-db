---
title: Codex CLI
url: https://github.com/openai/codex
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Codex CLI

CLI-агент от [OpenAI](platforms/openai.md) для работы в терминале: написание кода, файловая система, подагенты. Крупнейший open-source agentic CLI (67K+ GitHub stars, 9K forks, 400+ контрибьюторов).

## Ключевые возможности

- Терминальный TUI с интерактивным управлением сессиями
- Multi-agent v2: параллельные подагенты с общим состоянием
- Sandbox: изолированное выполнение кода, permission profiles
- `/usage` — daily/weekly/cumulative токен-активность
- `/import` — миграция настроек и чатов из Claude Code
- MCP (Model Context Protocol) — плагины и коннекторы
- `codex doctor` — диагностика окружения
- Plugin marketplace с каталогом и структурированным JSON-выводом
- Режимы: code mode (автономный), chat mode (диалоговый)

## Модели / Продукты

- Рекомендуемая модель по умолчанию: GPT-5.5 (400K контекст)
- Поддержка BYOK (Bring Your Own Key) и ChatGPT-аккаунта
- Codex Web (chatgpt.com/codex), VS Code/[Cursor](cursor.md)/Windsurf extensions

## Цены и доступ

- **Open Source:** да, [MIT-лицензия](https://github.com/openai/codex)
- Бесплатно с ChatGPT-аккаунтом (тратит квоту плана)
- BYOK: оплата через API-ключ пользователя

## Агентные возможности

- Полный agentic loop: plan → execute → observe → retry
- Subagents с делегированием задач
- Filesystem access с approval gates
- Skills system (файлы `SKILL.md` в `~/.agents/skills/`)
- MCP-интеграция для расширения tool-арсенала
- Background agents в Codex Web

## Open Source статус

**Полностью Open Source** (MIT). Активная разработка: версия 0.140.0+ (июнь 2026).

## Use Cases

- Автономное написание и рефакторинг кода
- CI/CD-агенты: запуск тестов, линтинг, деплой
- Миграция кодовой базы
- Исследование репозиториев и генерация документации
- Agent-to-agent review (multi-agent v2)

## Отзывы и критика

- Плюсы: открытый исходный код, частые релизы, глубокая интеграция с [OpenAI](platforms/openai.md)-моделями
- Минусы: менее отполированные skills по сравнению с Claude Code; привязка к экосистеме [OpenAI](platforms/openai.md)

## Связи

- [OpenAI](platforms/openai.md) — платформа-провайдер
- [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md)
- [Agent Harness](../patterns/architecture-design/agent-harness.md)
- [Исследование фреймворков](agent-frameworks-research.md)

*Добавлено: 2026-06-29*
