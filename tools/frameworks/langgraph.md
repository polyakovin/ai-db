---
title: LangGraph
url: https://docs.langchain.com/oss/python/langgraph/overview
type: url
category: tools
tags: [framework, orchestration, stateful, agents, langchain, python, open-source]
added: 2026-06-29
status: new
---

# LangGraph

LangGraph — низкоуровневый orchestration runtime для построения stateful, long-running AI-агентов от [LangChain](langchain.md). Предоставляет графовую модель выполнения с контролем состояния, durable execution, human-in-the-loop, streaming и production deployment. Рекомендуется для сложных агентных workflow, где важны контроль состояния и длительное исполнение.

## Ключевые возможности

- **StateGraph** — типизированное управление состоянием агента. Каждая нода графа читает и пишет состояние.
- **Durable execution** — checkpointing состояния после каждого шага. При сбое агент восстанавливается из последнего чекпоинта.
- **Human-in-the-loop** — прерывание выполнения для approvals, правок и подтверждений.
- **Streaming** — потоковая передача событий: токены, tool calls, обновления состояния.
- **Memory** — встроенная поддержка кратковременной и долговременной памяти агента.
- **Postgres checkpointing** — production-grade хранение чекпоинтов в PostgreSQL.
- **Typed StateGraph** — строгая типизация схемы состояния для надёжности.
- **[LangSmith](../observability/langsmith.md) integration** — tracing, observability, evals через [LangSmith](../observability/langsmith.md).
- **LangGraph Cloud** — managed hosting для production deployment.

## Архитектура

```
StateGraph
├── Nodes (шаги: model call, tool call, decision)
├── Edges (условные переходы на основе состояния)
├── State (typed, persistable)
├── Checkpointer (Postgres, SQLite, in-memory)
└── Interrupts (human-in-the-loop)
```

## Модель выполнения

1. Узел получает состояние → возвращает обновления состояния
2. LangGraph автоматически сохраняет чекпоинт
3. Условные рёбра направляют поток к следующему узлу
4. При ошибке — восстановление из последнего чекпоинта
5. Human-in-the-loop: прерывание, ожидание подтверждения, продолжение

## Когда применять

| Сценарий | Почему LangGraph |
|----------|-----------------|
| **Long-running stateful agents** | Durable execution, checkpointing, восстановление после сбоев |
| **Сложные workflow с ветвлением** | Условные рёбра, циклы, параллельные ветви |
| **HITL approvals** | Встроенные interrupts для подтверждений |
| **Production deployment** | Postgres checkpointing, LangGraph Cloud, FastAPI |
| **Multi-agent orchestration** | Subgraphs, изолированные состояния, координация |

## Когда НЕ применять

- Простая цепочка вызовов LLM — достаточно [LangChain](langchain.md) Expression Language (LCEL)
- Short-lived запросы без состояния — избыточно
- Быстрый прототип — [Dify](dify.md)/Flowise/LangFlow быстрее для MVP
- [OpenAI](../platforms/openai.md)-first managed stack — [Agents SDK](../platforms/openai.md) проще

## Open Source статус

- **LangGraph** — open source (MIT license), GitHub: `langchain-ai/langgraph`
- **LangGraph Cloud** — managed service (платный)
- **[LangSmith](../observability/langsmith.md)** — observability и evals платформа (freemium)
- **[LangChain](langchain.md)** — open source, на котором построен LangGraph

## Цены

- **LangGraph OSS**: бесплатно
- **LangSmith**: бесплатный tier → Developer ($39/мес) → Enterprise
- **LangGraph Cloud (LangSmith Deployment)**: $0.0036/мин за production deployment
- Стоимость inference — отдельно, через выбранную модель ([OpenAI](../platforms/openai.md), [Anthropic](../platforms/anthropic.md), etc.)

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **State management** | Строго типизированное состояние, checkpointing, восстановление |
| **Tool calling** | Интеграция с LangChain tools, MCP-серверы |
| **Memory** | Short-term (checkpoints) + long-term (persistent memory store) |
| **Streaming** | Пошаговая потоковая передача: токены, tool calls, обновления состояния |
| **Human-in-the-loop** | Interrupts для approvals, правок, подтверждений |
| **Multi-agent** | Subgraphs, параллельные агенты, общее/изолированное состояние |
| **Production** | FastAPI интеграция, Postgres checkpointing, горизонтальное масштабирование |

## Use Cases

- **Customer support agents**: Durable multi-step взаимодействие с клиентом
- **Code review pipelines**: Автоматический анализ PR с человеческим подтверждением
- **Research agents**: Длительный сбор и анализ информации с промежуточными approvals
- **Data processing pipelines**: Пошаговая обработка данных с контролем состояния
- **Safety-critical agents**: Обязательные approvals перед опасными действиями

## Сравнение с другими orchestration-фреймворками

| Критерий | LangGraph | OpenAI Agents SDK | AutoGen/MAF | CrewAI |
|----------|-----------|-------------------|-------------|--------|
| **Модель** | Stateful graph | Agent orchestration | Event-driven | Role-based crews |
| **Состояние** | Строгая типизация | SDK-managed | Событийное | Crew state |
| **HITL** | Встроенный | Guardrails | Через события | HITL triggers |
| **Production** | LangGraph Cloud, Postgres | OpenAI hosted | .NET/Python | Self-hosted |
| **Open source** | MIT | MIT | MIT (MAF) | MIT |

## Отзывы и критика

### Сильные стороны:
- Лучший выбор для stateful long-running агентов
- Durable execution с checkpointing — надёжное восстановление
- Строгая типизация состояния снижает ошибки
- Интеграция с [LangSmith](../observability/langsmith.md) для observability
- Зрелая экосистема [LangChain](langchain.md)

### Слабые стороны:
- Кривая обучения: нужно проектировать граф и состояние
- Избыточен для простых сценариев
- Зависимость от [LangChain](langchain.md)-экосистемы
- LangGraph Cloud — дополнительная стоимость
- Меньше «магии из коробки» по сравнению с [CrewAI](crewai.md)

## Связи

- [Anthropic (Claude)](../../tools/platforms/anthropic.md) — Claude Code как альтернативный подход к агентам
- [OpenAI](../../tools/platforms/openai.md) — Agents SDK как альтернатива для OpenAI-стека
- [AutoGen / MAF](../frameworks/autogen.md) — event-driven multi-agent альтернатива
- [CrewAI](../frameworks/crewai.md) — роль-ориентированная multi-agent альтернатива
- [Исследование фреймворков](../agent-frameworks-research.md) — LangGraph в карте выбора
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — LangGraph как реализация orchestration в harness
- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) — LangGraph для оркестрации

*Добавлено: 2026-06-29*
