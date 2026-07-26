---
title: LocalCowork
url: https://github.com/Liquid4All/cookbook/tree/main/examples/localcowork
type: url
category: tools
tags: [desktop-agent, local-ai, mcp, tool-calling, privacy, open-source]
added: 2026-07-26
status: verified
---

# LocalCowork

LocalCowork — open-source desktop-агент от Liquid AI для полностью локальных tool-calling workflow. Модель, MCP-серверы и пользовательские данные работают на ноутбуке; inference подключается через локальный [OpenAI](openai.md)-compatible endpoint, а вызовы инструментов записываются в audit trail.

## Архитектура

| Слой | Реализация |
|---|---|
| Desktop UI | Tauri 2.0 + React/TypeScript |
| Agent core | Rust: conversation manager, tool router, MCP client, orchestrator и audit |
| Inference | Локальный [OpenAI](openai.md)-compatible API через llama.cpp, [Ollama](../inference/ollama.md) или [vLLM](../inference/vllm.md) |
| Tools | TypeScript- и Python-MCP-серверы |

Репозиторий содержит 75 инструментов в 14 MCP-серверах: filesystem, документы, OCR, security scanning, knowledge/RAG, встречи, календарь, email, задачи, данные, audit, clipboard, system API и screenshot pipeline. Стартовая конфигурация сознательно ограничена 20 проверенными инструментами из 6 серверов, потому что меньшая tool surface экономит контекст и повышает точность выбора.

Для каталогов из 40+ инструментов предусмотрен экспериментальный pipeline `plan → execute → synthesize`: большая модель строит план, отдельный router выбирает по одному инструменту из RAG-предфильтрованного top-K, затем большая модель собирает ответ.

## Обновление модели

В мае 2026 года Liquid AI перевела демонстрацию на [LFM2.5-8B-A1B](../models/lfm2-5-8b-a1b.md). В официальном анонсе используется один ноутбук, 67 инструментов в 13 MCP-серверах, без облака и API-ключей; dispatch заявлен как субсекундный.

При этом README репозитория всё ещё описывает прежнюю конфигурацию на LFM2-24B-A2B и соответствующие benchmark/quick-start команды. Поэтому текущий model config нужно проверять в коде и release notes, а числа старого benchmark нельзя автоматически переносить на новую модель.

## Human-in-the-loop и безопасность

Local-only inference убирает передачу данных облачному model provider, но не делает локальные side effects безопасными автоматически.

- Каждый вызов инструмента попадает в локальный audit trail.
- Confirmation UI, permission store и tool router существуют в коде, но README отмечает, что они ещё не подключены к agent loop.
- В текущем описанном состоянии модель может сразу выполнить выбранный инструмент.
- Filesystem, clipboard, email, encryption и другие write/destructive capabilities требуют sandbox, least privilege и отдельного approval gate перед production-использованием.

## Когда рассматривать

LocalCowork полезен как reference implementation для:

- privacy-sensitive и offline agent workflow;
- desktop-агента поверх локального inference server;
- MCP-оркестрации множества локальных инструментов;
- сравнения single-model и planner/router архитектур;
- изучения audit trail, tool-selection evals и failure taxonomy.

## Ограничения

- Это демонстрационный проект в составе Liquid AI Cookbook, а не готовая production-платформа.
- Документация и новая конфигурация модели временно расходятся.
- Заявления о скорости и надёжности LFM2.5 принадлежат Liquid AI и требуют независимой проверки на целевом железе и собственных tool schemas.
- Большой каталог похожих инструментов повышает sibling confusion; multi-step и cross-server цепочки нужно оценивать отдельно от single-step tool selection.

## Open Source статус

Код LocalCowork опубликован под MIT License. Лицензия модели отличается: [LFM2.5-8B-A1B](../models/lfm2-5-8b-a1b.md) распространяется по собственной LFM Open License 1.0 с ограничением для коммерческого использования организациями с годовой выручкой от $10 млн.

## Связи

- [LFM2.5-8B-A1B](../models/lfm2-5-8b-a1b.md) — текущая модель демонстрации.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — управление большой tool surface.
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — LocalCowork как локальный agent harness.
- [Human-in-the-loop UX](../../patterns/production-operations/human-in-the-loop-ux.md) — approvals перед side effects.
- [Официальный анонс и репозиторий](../../sources/libraries-tools/localcowork-lfm2-5.md) — provenance и расхождения источников.

*Проверено: 2026-07-26*
