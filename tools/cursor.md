---
title: Cursor
url: https://www.cursor.com/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Cursor

AI-first редактор кода на базе VS Code с глубокими агентными возможностями: Composer, Agent mode, Debug Mode, Plan Mode, визуальный редактор.

## Ключевые возможности

- **Agent Mode** — автономный агент с доступом к файлам, терминалу, браузеру
- **Composer** — multi-file редактирование целых фич одной командой
- **Plan Mode** — Mermaid-диаграммы плана перед выполнением
- **Debug Mode** — автономный поиск багов с инструментацией кода
- **Visual Editor** — drag-and-drop редактирование UI в Cursor Browser
- **Multi-Agent Judging** — сравнение параллельных выводов разных моделей
- **Tab completion** — интеллектуальное автодополнение
- **Background Agents** — облачные sandbox-агенты (2026)
- **BugBot** — автоматическое ревью pull request'ов
- **MCP** — Model Context Protocol для подключения к инфраструктуре

## Модели / Продукты

- Собственная модель Composer (proprietary)
- Поддержка GPT-5.5, Claude Opus/Sonnet, Gemini (BYOK)
- До 8 параллельных агентов

## Цены и доступ

- **Open Source:** нет (proprietary, форк VS Code)
- **Бесплатный тариф:** Hobby (ограниченные запросы)
- **Pro:** $20/мес
- **Business:** $40/мес/пользователь

## Агентные возможности

- Полный цикл: plan → execute → debug → verify
- Работа с файловой системой, терминалом и браузером
- Hooks для кастомной автоматизации
- Agent-to-agent judging (сравнение моделей)
- Background agents для длительных задач

## Open Source статус

**Proprietary.** Базируется на открытом VS Code, но AI-функции закрыты.

## Use Cases

- Full-stack разработка: frontend + backend в одном окне
- Bug fixing с Debug Mode
- Рефакторинг крупных проектов через Composer
- Быстрое прототипирование UI с Visual Editor
- Code review через BugBot

## Отзывы и критика

- Плюсы: глубокая интеграция в IDE, богатый набор агентных фич
- Минусы: закрытый исходный код, частые изменения UI, платные тарифы для активного использования

## Связи

- [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md)
- [Codex CLI](codex-cli.md) — open-source CLI-альтернатива
- [Agent Harness](../patterns/architecture-design/agent-harness.md)

*Добавлено: 2026-06-29*
