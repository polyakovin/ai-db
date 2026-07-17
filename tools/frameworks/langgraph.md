---
title: LangGraph
url: https://docs.langchain.com/oss/python/langgraph/overview
type: url
category: tools
tags: [framework, orchestration, stateful, durable-execution, agents, python, open-source]
added: 2026-06-29
updated: 2026-07-17
status: verified
---

# LangGraph

LangGraph — low-level orchestration framework и runtime для long-running stateful workflows и AI-агентов. Он не задаёт готовую prompt-архитектуру: разработчик явно моделирует state, nodes и transitions, а runtime обеспечивает persistence, durable execution, streaming и human-in-the-loop. Компоненты [LangChain](langchain.md) удобны, но не обязательны.

## Ключевые возможности

- **StateGraph** — nodes читают состояние и возвращают его обновления; edges задают обычные и условные переходы.
- **Persistence** — checkpointer сохраняет snapshots по шагам и группирует их в threads.
- **Durable execution** — выполнение можно продолжить после сбоя или restart с сохранённого состояния.
- **Human-in-the-loop** — interrupts приостанавливают граф для inspection, изменения state или approval.
- **Memory** — checkpoints дают thread-level history, отдельный store поддерживает данные между threads.
- **Streaming** — события выполнения, state updates, messages, tokens и custom events.
- **Time travel** — replay и fork из сохранённого checkpoint для debugging и альтернативных траекторий.
- **Subgraphs** — композиция stateful workflows и multi-agent схем с общим или изолированным state.
- **[LangSmith](../observability/langsmith.md)** — отдельная платформа для tracing, evaluation и managed deployment.

## Модель выполнения

1. Node получает текущий state и возвращает update.
2. Edges определяют следующий шаг; независимые ветви могут выполняться в одном super-step.
3. Настроенный checkpointer фиксирует snapshot и pending writes.
4. Ошибка, interrupt или restart возобновляет graph с согласованной точки.
5. Внешний код или человек может inspect и update state перед продолжением.

## Когда применять

| Сценарий | Почему LangGraph |
|---|---|
| Long-running agents | Checkpoints и resume после process/API failures |
| Сложное ветвление и циклы | Явные conditional edges и state transitions |
| Human approvals | Interrupt, inspection, state update и resume |
| Stateful conversations | Thread persistence и long-term store |
| Multi-agent orchestration | Subgraphs и контролируемая передача состояния |
| Debuggable workflows | Streaming, checkpoints, replay и fork |

## Когда не применять

- Простой tool-calling agent без сложного state — [LangChain](langchain.md) или [Pydantic AI](pydantic-ai.md) дадут более высокий уровень абстракции.
- Быстрый visual prototype — [Dify](dify.md), [Flowise](flowise.md) или [Langflow](langflow.md) сокращают путь до demo.
- Kotlin/JVM-first application — [Koog](koog.md) может лучше совпасть с языком и runtime команды.
- Обычный deterministic workflow без LLM-specific state — сначала сравните с general-purpose workflow engine.

## Агентные возможности

| Возможность | Реализация |
|---|---|
| State management | Typed state, reducers, checkpoints и stores |
| Control flow | Nodes, edges, commands, branches, loops и parallel super-steps |
| Human-in-the-loop | Interrupts, state inspection/update и resume |
| Memory | Thread-scoped checkpoints и cross-thread store |
| Fault tolerance | Resume, pending writes и configurable durability modes |
| Multi-agent | Subgraphs, supervisor/router patterns, shared или private state |
| Observability | Event streaming и интеграция с LangSmith/OpenTelemetry stack |

## Open Source статус и deployment

- LangGraph распространяется по лицензии MIT; основной репозиторий — `langchain-ai/langgraph`.
- OSS runtime можно запускать самостоятельно с выбранным checkpointer и storage backend.
- [LangSmith](../observability/langsmith.md) Deployment — отдельный managed-вариант; observability и hosting не являются обязательными для LangGraph.
- Inference, databases и managed services оплачиваются отдельно по тарифам выбранных поставщиков.

## Сильные стороны и ограничения

**Сильные стороны:** явная модель состояния, pause/resume, fault tolerance, replay, human-in-the-loop и возможность использовать runtime без [LangChain](langchain.md).

**Ограничения:** разработчик отвечает за декомпозицию graph/state и идемпотентность side effects; granular nodes увеличивают число checkpoints; production storage, migrations, permissions, evals и deployment остаются архитектурными задачами.

## Связи

- [Официальная документация LangGraph](../../sources/libraries-tools/langgraph-docs.md) — provenance для этой страницы
- [LangChain](langchain.md) — high-level agent framework и integrations
- [Pydantic AI](pydantic-ai.md) — typed Python agent framework более высокого уровня
- [Koog](koog.md) — Kotlin/JVM agent framework с graph strategies
- [Langflow](langflow.md) — visual builder для прототипирования flows
- [Исследование фреймворков](../agent-frameworks-research.md) — LangGraph в карте выбора
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — runtime как часть harness
- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) — graph-based coordination

*Добавлено: 2026-06-29; обновлено: 2026-07-17*
