---
title: OpenAI
url: https://openai.com/
type: url
category: tools
tags: [llm, platform, agent, coding, codex, responses-api, agents-sdk]
added: 2026-06-29
status: new
---

# OpenAI

OpenAI — ведущая американская AI-компания, создатель GPT-семейства моделей и managed agent stack: Responses API, Agents SDK, [Codex CLI](../ides/codex-cli.md). Предоставляет самую полную на сегодня managed-платформу для создания production AI-агентов: от моделей до evals, tracing, guardrails и sandbox.

## Ключевые возможности

- **Responses API** — основной API для агентов: заменяет Chat Completions и Assistants API. Поддерживает reasoning, tool calling, structured outputs, web search, file search, computer use, streaming, background mode.
- **Agents SDK** — Python/Node.js SDK для построения агентов: orchestration, handoffs, guardrails, tracing, evals, sandbox agents, MCP-серверы.
- **[Codex CLI](../ides/codex-cli.md)** — open-source терминальный coding agent: работает с репозиториями, multi-agent workflows, skills catalog, облачные sandbox. #1 на Terminal-Bench 2.1 (83.4%).
- **ChatKit** — фреймворк для построения UI-агентов с Actions, Skills, Shell, [Computer Use](anthropic.md).
- **Realtime API** — голосовые агенты с WebRTC, WebSocket, SIP.
- **Agent Builder** — low-code инструмент для создания агентов.

## Модели (июнь 2026)

| Модель | Статус | Цена API (input/output за 1M токенов) | Особенности |
|--------|--------|--------------------------------------|-------------|
| **GPT-5.5** | GA | ~$2.50 / $10 | Флагман: reasoning, tool calling, structured outputs, 256K контекст. Рекомендуется для Responses API |
| **GPT-5.5 Pro** | GA | Выше | Enhanced reasoning для самых сложных задач |
| **GPT-5.4** | GA | экономичнее | Предыдущее поколение, всё ещё competitive |
| **o3 / o1** | GA | varies | Reasoning-специализированные модели |

### Reasoning effort (GPT-5.5):
- `low` — минимальная задержка
- `medium` — сбалансированный старт
- `high` / `xhigh` — для сложных асинхронных агентных задач

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Responses API** | Единый API для агентов: tools, reasoning, structured outputs, streaming, background mode, compaction. Заменяет Assistants API (вывод из эксплуатации к 2026) |
| **Agents SDK** | Python/Node.js: orchestration (цепочки, параллельные агенты), handoffs, guardrails (input/output/content), tracing (OpenTelemetry), evals |
| **Codex CLI** | Open-source терминальный coding agent: multi-agent workflows, skills catalog, облачные sandbox, IDE-интеграция. Терминальный #1 на Terminal-Bench 2.1 |
| **Computer Use** | Управление десктопом/браузером через API |
| **Web Search / File Search** | Встроенные hosted tools в Responses API |
| **Realtime API** | Голосовые агенты: WebRTC, WebSocket, SIP интеграция |
| **MCP Server** | OpenAI Agents SDK поддерживает MCP-серверы |
| **Agent Builder** | Low-code платформа для конструирования агентов |

## OpenAI стек для агентов

| Слой | Инструменты |
|------|-------------|
| **Model** | GPT-5.5, GPT-5.5 Pro через Responses API |
| **Agent SDK** | OpenAI Agents SDK (Python/Node.js), Codex CLI |
| **Orchestration** | Agents SDK: handoffs, параллельные агенты, guardrails |
| **Tools** | Web Search, File Search, Computer Use, MCP |
| **Observability** | OpenTelemetry traces, интеграция с LangSmith, Phoenix |
| **Evals** | Встроенная evaluation framework |
| **Sandbox** | Codex sandbox для безопасного исполнения кода |

## Open Source статус

- **GPT-модели** — закрытые, доступны только через API.
- **[Codex CLI](../ides/codex-cli.md)** — open source (GitHub: `openai/codex`, ~75.7K звёзд, MIT-like).
- **Agents SDK** — open source (GitHub: `openai/openai-agents-python`).
- **MCP-серверы** — поддержка открытого стандарта MCP.
- **Open-source модели**: OpenAI выкладывает некоторые модели (Whisper, CLIP, Point-E), но не GPT.

## Цены и доступ

### API (GPT-5.5)
- Input: ~$2.50/MTok
- Output: ~$10/MTok
- Reasoning tokens: оплачиваются отдельно при extended reasoning
- Prompt caching: ~50% скидка на кешированные чтения
- Batch API: 50% скидка

### Подписки
- **ChatGPT Plus** ($20/мес): GPT-5.5, [Codex CLI](../ides/codex-cli.md) базовый, ограниченный лимит
- **ChatGPT Pro** ($200/мес): полный доступ
- **Team/Enterprise**: расширенные лимиты, администрирование

### Codex CLI
- Кредитная система: включена в подписку ChatGPT или оплата через API
- Облачные sandbox: дополнительные лимиты

## Use Cases

- **Production AI-агенты**: Responses API + Agents SDK для tool-heavy workflows
- **Coding Agent**: Codex CLI как альтернатива [Claude Code](anthropic.md)
- **Голосовые агенты**: Realtime API для голосовых интерфейсов
- **Enterprise RAG**: File Search, Web Search как hosted tools
- **Multi-agent системы**: Agents SDK orchestration с handoffs

## Отзывы и критика

### Сильные стороны:
- Самый полный managed agent stack: от модели до evals
- GPT-5.5 — топ на Terminal-Bench 2.1 (83.4% через [Codex CLI](../ides/codex-cli.md))
- Agents SDK с guardrails, handoffs, tracing из коробки
- [Codex CLI](../ides/codex-cli.md) — open source, активное сообщество
- Быстрый инференс, надёжный API

### Слабые стороны:
- Закрытые модели — полная зависимость от провайдера
- Цены выше open-weight альтернатив ([DeepSeek](deepseek.md) V4 Flash: $0.14/MTok)
- Prompt caching слабее, чем у [Anthropic](anthropic.md) (50% vs 90%)
- Agents SDK требует изучения концепций (orchestration, handoffs)
- Codex CLI уступает [Claude Code](anthropic.md) в reasoning depth (SWE-bench Pro: 58.6% vs 69.2%)

## Связи

- [Anthropic (Claude)](../../tools/platforms/anthropic.md) — главный конкурент
- [Google Gemini](gemini.md) — альтернативный провайдер
- [Исследование фреймворков](../agent-frameworks-research.md) — OpenAI стек в карте выбора
- [Модельная карта](../agent-model-map.md) — GPT-5.5 в карте моделей
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — Codex CLI как реализация coding harness
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — практический workflow с Codex
- [Tool use и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — Responses API как реализация tool use

*Добавлено: 2026-06-29*
