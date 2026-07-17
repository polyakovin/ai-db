---
title: Koog
url: https://docs.koog.ai/
type: url
category: tools
tags: [framework, agents, kotlin, java, jvm, multiplatform, open-source]
added: 2026-07-17
status: new
---

# Koog

Koog — open-source фреймворк JetBrains для создания AI-агентов в экосистеме Kotlin и Java. Он даёт type-safe Kotlin DSL, Java builder API и несколько моделей агента: готовый basic loop, функциональную логику, графовую стратегию и planner. Kotlin-агенты можно переносить с JVM на JS, WasmJS, Android и iOS через Kotlin Multiplatform.

## Ключевые возможности

- **Типизированные API** — Kotlin DSL и Java API для prompts, tools, structured output и agent strategies.
- **Несколько типов агентов** — basic, functional, graph-based и planner agents; часть модулей помечена beta.
- **Tools и agents-as-tools** — registry для встроенных и пользовательских tools; специализированный агент можно вызвать как tool другого агента.
- **Состояние и контекст** — persistence, history compression и восстановление состояния в long-running диалогах.
- **Streaming** — потоковые ответы и параллельные tool calls.
- **Интеграции** — MCP, A2A, OpenTelemetry, Spring Boot и Ktor; статус стабильности нужно проверять по конкретному модулю.
- **Knowledge и memory** — retrieval, embeddings и long-term memory доступны как развивающиеся модули.

## Когда применять

| Сценарий | Почему Koog |
|---|---|
| Kotlin/JVM backend | Нативные Kotlin/Java API, корутины и интеграция с существующим приложением |
| Spring Boot или Ktor | Агент можно встроить в привычный JVM service stack |
| Kotlin Multiplatform | Общую агентную логику можно использовать на нескольких targets |
| Явный workflow | Graph strategy делает переходы и обработку состояния видимыми |
| Иерархия агентов | Agents-as-tools поддерживает supervisor/specialist композицию |

## Когда не применять

- Команда и инфраструктура полностью Python-first — [Pydantic AI](pydantic-ai.md) или [LangGraph](langgraph.md) дадут более естественную экосистему.
- Нужен визуальный builder для non-engineering команды — [Langflow](langflow.md) подходит лучше.
- Нужен распределённый durable runtime с готовой моделью checkpoints и interrupts — сравните с [LangGraph](langgraph.md); persistence Koog не следует считать автоматической заменой production workflow engine.
- Нельзя принимать beta-зависимости — проверяйте стабильность каждого модуля, а не только ядра.

## Агентные возможности

| Возможность | Реализация |
|---|---|
| Tool calling | Built-in, annotation-based и class-based tools, tool registry |
| Orchestration | Functional logic, graph strategies, subgraphs, planner agents |
| State | Agent state, storage и persistence API |
| Multi-agent | Преобразование агента в tool для иерархических схем |
| Interoperability | MCP и A2A integrations |
| Observability | Tracing и OpenTelemetry exporters |
| Structured output | Типизированные схемы результата |

## Open Source статус

- Koog распространяется по лицензии Apache 2.0.
- Основной репозиторий: `JetBrains/koog`.
- Фреймворк бесплатен; inference и внешние managed-сервисы оплачиваются отдельно.

## Сильные стороны и ограничения

**Сильные стороны:** нативный путь для Kotlin/Java команд, type-safe DSL, Kotlin Multiplatform, явные graph strategies и интеграция с JVM-стеком.

**Ограничения:** экосистема моложе Python-фреймворков; часть возможностей остаётся beta; production persistence, distributed execution, evals и governance требуют отдельной архитектуры.

## Связи

- [Официальная документация Koog](../../sources/libraries-tools/koog-docs.md) — provenance для этой страницы
- [Исследование фреймворков](../agent-frameworks-research.md) — Koog в карте выбора
- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) — agents-as-tools для иерархических систем
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — Koog как runtime внутри harness
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — tools и MCP-интеграция

*Добавлено: 2026-07-17*
