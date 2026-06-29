---
title: CrewAI
url: https://docs.crewai.com/
type: url
category: tools
tags: [framework, multi-agent, python, orchestration, open-source]
added: 2026-06-29
status: new
---

# CrewAI

CrewAI — фреймворк для роль-ориентированной multi-agent автоматизации. Строится вокруг концепции «crew» (экипажа) AI-агентов с ролями, задачами и инструментами. Поддерживает Flows (событийно-ориентированные workflow), memory, knowledge, guardrails, observability и HITL triggers. Хороший выбор для быстрой ролевой multi-agent автоматизации, где роли действительно независимы.

## Ключевые возможности

- **Crews** — экипажи AI-агентов с определёнными ролями, целями и инструментами.
- **Tasks** — задачи с описанием, ожидаемым результатом, контекстом и зависимостями.
- **Flows** — событийно-ориентированная оркестрация (v0.4, январь 2026): асинхронная архитектура для сотен параллельных агентов.
- **Memory** — кратковременная (session), долговременная (persistent), shared memory между агентами.
- **Knowledge** — встроенная поддержка RAG и retrieval для агентов.
- **Guardrails** — проверки input/output, safety filters.
- **Observability** — встроенное tracing, логирование, метрики.
- **HITL triggers** — остановка выполнения для человеческого подтверждения.

## Архитектура (v0.4, январь 2026)

```
Crew
├── Agents (роли: researcher, writer, reviewer)
├── Tasks (цели, ожидаемый результат, контекст)
├── Tools (функции, API, браузер)
├── Memory (short-term, long-term, shared)
├── Knowledge (RAG)
├── Flows (event-driven оркестрация)
└── Guardrails (проверки)
```

Асинхронная архитектура v0.4 позволяет запускать сотни параллельных агентных диалогов.

## Когда применять

| Сценарий | Почему CrewAI |
|----------|--------------|
| **Role-based automation** | Агенты с чёткими ролями: researcher → writer → reviewer |
| **Быстрый multi-agent прототип** | Минимальный boilerplate, декларативный синтаксис |
| **Content generation pipelines** | Многошаговая генерация контента с проверками |
| **Task decomposition** | Разбивка задач на роли, параллельное выполнение |

## Когда НЕ применять

- Сложный stateful orchestration — LangGraph сильнее
- Enterprise .NET-стек — MAF (AutoGen + Semantic Kernel)
- RAG-first агенты — LlamaIndex специализированнее
- Production без evals — CrewAI требует собственных проверок качества

## Open Source статус

- **CrewAI** — open source (MIT license), GitHub: `crewAIInc/crewAI`
- **Enterprise** — платный tier с дополнительными возможностями
- Активное сообщество, частые релизы

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Role-based agents** | Каждый агент — роль с экспертизой: researcher, writer, reviewer, coder |
| **Task delegation** | Агенты могут делегировать задачи друг другу |
| **Flow orchestration** | Event-driven workflow (v0.4) для асинхронной оркестрации |
| **Memory** | Short-term (session), long-term (persistent), shared между агентами |
| **Knowledge** | Встроенный RAG: retrieval из документов, баз знаний |
| **Guardrails** | Input/output validation, safety checks |
| **HITL** | Human-in-the-loop triggers для approvals |
| **Observability** | Tracing, логирование, интеграция с LangSmith/Arize |

## Сравнение с аналогами

| Критерий | CrewAI | LangGraph | AutoGen/MAF | OpenAI Agents SDK |
|----------|--------|-----------|-------------|-------------------|
| **Модель** | Role-based crews | Stateful graph | Event-driven | Agent orchestration |
| **Простота** | Высокая | Средняя | Средняя | Средняя |
| **Асинхронность** | Да (v0.4) | Streaming | Нативная | Да |
| **Memory** | Встроенная | Checkpoints | Через plugins | SDK-managed |
| **RAG** | Knowledge system | LangChain retrievers | Через plugins | File Search |

## Use Cases

- **Content creation**: researcher → writer → editor → publisher
- **Customer support triage**: classifier → responder → escalate
- **Code review teams**: reviewer → fixer → tester
- **Research automation**: collector → analyst → report writer
- **Marketing automation**: strategist → copywriter → designer agent

## Отзывы и критика

### Сильные стороны:
- Минимальный boilerplate — быстрый старт
- Интуитивная ролевая модель (легко объяснить бизнесу)
- Встроенная memory и knowledge из коробки
- Flow-оркестрация (v0.4) для асинхронных сценариев
- Активное сообщество

### Слабые стороны:
- Роли могут плодиться без реальной нужды («over-engineering ролей»)
- Меньше контроля над состоянием, чем в LangGraph
- Evals нужно делать самостоятельно
- Не для enterprise .NET (MAF сильнее)
- Для простого single-agent — избыточен

## Связи

- [[../frameworks/langgraph.md|LangGraph]] — альтернативный orchestration-фреймворк
- [[../frameworks/autogen.md|AutoGen / MAF]] — альтернативный multi-agent фреймворк
- [[../agent-frameworks-research.md|Исследование фреймворков]] — CrewAI в карте выбора
- [[../../patterns/implementation/multi-agent-orchestration.md|Multi-agent orchestration]] — CrewAI для оркестрации
- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — CrewAI в сравнении с harness-подходом

*Добавлено: 2026-06-29*
