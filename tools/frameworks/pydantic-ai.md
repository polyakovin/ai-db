---
title: Pydantic AI
url: https://pydantic.dev/docs/ai/overview/
type: url
category: tools
tags: [framework, agents, python, pydantic, type-safety, structured-output, open-source]
added: 2026-07-17
status: new
---

# Pydantic AI

Pydantic AI — open-source Python-фреймворк от команды Pydantic для production GenAI-приложений и агентов. Он объединяет agent loop с типизированными dependencies, tools и structured outputs; базовая библиотека Pydantic строит JSON Schema и валидирует аргументы tools и результаты модели.

## Ключевые возможности

- **Type-safe agents** — типы dependencies и output проходят через `Agent[DepsType, OutputType]` и проверяются статическими анализаторами.
- **Structured output** — Pydantic-модели описывают схему результата; ошибки валидации можно вернуть модели для повторной попытки.
- **Dependency injection** — `RunContext` передаёт соединения, конфигурацию и application services в instructions и tools.
- **Model-agnostic API** — единый интерфейс для нескольких model providers и возможность добавить собственную реализацию.
- **Tools и capabilities** — function tools, toolsets, MCP, deferred tools, approvals и переиспользуемые capabilities.
- **Streaming и multimodal input** — потоковые типизированные результаты, изображения, аудио, видео и документы.
- **Graphs и durable execution** — Pydantic Graph для явных workflow; интеграции с внешними workflow runtimes для надёжного возобновления.
- **Testing, evals и observability** — test model, Pydantic Evals и OpenTelemetry/Logfire instrumentation.
- **Pydantic AI Harness** — композиция готовых capabilities для filesystem, shell, compaction, guardrails, planning и subagents.

## Когда применять

| Сценарий | Почему Pydantic AI |
|---|---|
| Typed Python backend | Dependencies, tool arguments и output описываются Python-типами |
| Structured extraction | Результат валидируется как Pydantic-модель, а не как произвольный JSON |
| FastAPI/Pydantic stack | Совпадает модель типов и dependency-oriented стиль разработки |
| Provider portability | Model API не привязывает весь application layer к одному провайдеру |
| Testable agent logic | Test model, dependency injection и evals упрощают изолированные проверки |

## Когда не применять

- Нужен визуальный low-code builder — используйте [Langflow](langflow.md).
- Главная задача — детальный stateful graph с native checkpointing, time travel и interrupts — [LangGraph](langgraph.md) специализированнее.
- Приложение находится в Kotlin/JVM-стеке — [Koog](koog.md) снижает языковой разрыв.
- Нельзя подключать внешний workflow runtime, но требуется распределённое durable execution: интеграция не равна встроенной инфраструктуре исполнения.

## Агентные возможности

| Возможность | Реализация |
|---|---|
| Agent loop | Instructions, model requests, tools и validated final output |
| Tool calling | Python functions, toolsets, native/deferred tools и MCP |
| Structured output | Pydantic schemas, validation и retry при ошибке |
| Context | Type-safe dependency injection через `RunContext` |
| Human-in-the-loop | Approval для выбранных tool calls |
| Workflows | Pydantic Graph и durable-execution integrations |
| Multi-agent | Agent delegation, agent-as-tool и harness subagents |
| Quality | Test model, Pydantic Evals, OpenTelemetry/Logfire |

## Open Source статус

- Pydantic AI распространяется по лицензии MIT.
- Основной репозиторий: `pydantic/pydantic-ai`.
- Pydantic Logfire и AI Gateway — отдельные сервисы; для фреймворка они не обязательны.

## Сильные стороны и ограничения

**Сильные стороны:** строгие schemas на границах LLM, удобная dependency injection, provider portability, тестируемость и совместимость с привычным typed Python.

**Ограничения:** широкая поверхность API продолжает развиваться; сложный graph orchestration требует отдельного проектирования; production durability зависит от выбранного внешнего runtime и его операционной модели.

## Связи

- [Официальная документация Pydantic AI](../../sources/libraries-tools/pydantic-ai-docs.md) — provenance для этой страницы
- [Исследование фреймворков](../agent-frameworks-research.md) — Pydantic AI в карте выбора
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — harness capabilities вокруг agent loop
- [Evaluations для AI-агентов](../../patterns/implementation/agent-evaluations.md) — evals и regression testing
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — tool schemas и MCP

*Добавлено: 2026-07-17*
