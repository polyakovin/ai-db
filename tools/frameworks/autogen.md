---
title: AutoGen / Microsoft Agent Framework
url: https://github.com/microsoft/autogen
type: url
category: tools
tags: [framework, multi-agent, microsoft, orchestration, open-source, python]
added: 2026-06-29
status: new
---

# AutoGen / Microsoft Agent Framework (MAF)

AutoGen — open-source фреймворк от Microsoft Research для создания conversational и event-driven multi-agent систем. Исторически разделялся на AgentChat (high-level) и Core (low-level). В апреле 2026 года AutoGen и Semantic Kernel объединились в **Microsoft Agent Framework (MAF)** — единую production-ready платформу для .NET и Python с stable API и долгосрочной поддержкой.

## Ключевые возможности

- **AgentChat** — high-level API для быстрого создания conversational single/multi-agent приложений.
- **Core** — низкоуровневый event-driven runtime для построения сложных multi-agent систем.
- **Extensions** — расширения для observability, Studio (UI для визуализации и отладки).
- **Event-driven архитектура** — агенты общаются через события (messages, tool calls, state changes).
- **Multi-agent collaboration** — поддержка conversational patterns: round-robin, manager-worker, group chat.
- **Convergence с Semantic Kernel** (апрель 2026) → единый MAF: stable APIs, LTS, production-ready.

## MAF 1.0 (апрель 2026)

После слияния AutoGen и Semantic Kernel в Microsoft Agent Framework:

| Характеристика | MAF 1.0 |
|---------------|---------|
| **Дата GA** | 2 апреля 2026 |
| **Языки** | .NET, Python (оба first-class) |
| **API стабильность** | Stable APIs, LTS |
| **Модель** | Event-driven + middleware |
| **Enterprise** | Интеграция с Microsoft-стеком: Azure, plugins, telemetry |
| **Hosted** | Опционально: Azure Agent Service |

## Когда применять

| Сценарий | Почему AutoGen/MAF |
|----------|-------------------|
| **Conversational multi-agent** | AgentChat для round-robin/group chat между агентами |
| **Event-driven системы** | Core для сложной event-driven архитектуры |
| **Research/prototyping** | Быстрое прототипирование multi-agent collaboration |
| **Enterprise Microsoft стек** | MAF + .NET + Azure — нативная интеграция |
| **Middleware-архитектура** | Filters, plugins, telemetry встроены |

## Когда НЕ применять

- Простой single-agent — избыточно
- Stateful durable execution — [LangGraph](langgraph.md) сильнее
- Нужен быстрый MVP — [CrewAI](crewai.md)/[Dify](dify.md) быстрее
- Не-Microsoft стек — весомое преимущество MAF теряется

## Open Source статус

- **AutoGen** — MIT license (GitHub: `microsoft/autogen`)
- **Semantic Kernel** — MIT license (GitHub: `microsoft/semantic-kernel`)
- **MAF** — MIT license, единый репозиторий после слияния
- **AutoGen Studio** — open source UI для визуализации и отладки

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Conversational agents** | AgentChat: агенты общаются через сообщения, поддерживаются round-robin, group chat |
| **Event-driven execution** | Core: события — основа архитектуры, подписки, pub/sub |
| **Multi-agent patterns** | Manager-worker, group chat, hierarchical teams |
| **Middleware** | Filters, telemetry, plugins — enterprise integration layer |
| **Tools / Plugins** | Semantic Kernel plugin system: C#, Python, REST, OpenAPI |
| **Observability** | OpenTelemetry, Azure Monitor, кастомные sinks |
| **Human-in-the-loop** | Approvals через события, прерывания |

## Сравнение с аналогами

| Критерий | MAF (AutoGen+SK) | LangGraph | CrewAI | OpenAI Agents SDK |
|----------|-----------------|-----------|--------|-------------------|
| **Модель** | Event-driven + middleware | Stateful graph | Role-based crews | Agent orchestration |
| **Языки** | .NET + Python | Python | Python | Python/Node.js |
| **Сложность** | Средняя | Высокая | Низкая | Средняя |
| **Enterprise** | Microsoft-first | Model-agnostic | Self-contained | OpenAI-first |
| **HITL** | Через события | Встроенный | HITL triggers | Guardrails |

## Use Cases

- **Multi-agent research**: Conversational collaboration между агентами-исследователями
- **Enterprise automation**: .NET-интеграция с существующими enterprise-системами
- **Customer service**: Multi-agent round-robin обслуживание клиентов
- **Event-driven pipelines**: Асинхронная обработка событий несколькими агентами

## Отзывы и критика

### Сильные стороны:
- Единственный production-фреймворк с first-class поддержкой .NET и Python
- Слияние AutoGen и Semantic Kernel — единая платформа, stable API
- Event-driven архитектура хороша для асинхронных сценариев
- Глубокая интеграция с Microsoft-стеком (Azure, plugins, telemetry)
- AutoGen Studio для визуализации

### Слабые стороны:
- Слияние двух проектов может означать breaking changes и сложности миграции
- Меньше adoption, чем у LangGraph/CrewAI
- Event-driven модель сложнее для простых сценариев
- Заточен под Microsoft-экосистему (меньше ценности вне неё)
- Меньше community content и tutorials

## Связи

- [[../frameworks/langgraph.md|LangGraph]] — альтернативный orchestration-фреймворк
- [[../frameworks/crewai.md|CrewAI]] — более простая multi-agent альтернатива
- [[../frameworks/semantic-kernel.md|Semantic Kernel]] — часть MAF, enterprise middleware
- [[../agent-frameworks-research.md|Исследование фреймворков]] — AutoGen в карте выбора
- [[../../patterns/implementation/multi-agent-orchestration.md|Multi-agent orchestration]] — AutoGen для оркестрации
- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — MAF как реализация harness

*Добавлено: 2026-06-29*
