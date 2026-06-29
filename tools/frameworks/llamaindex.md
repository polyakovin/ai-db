---
title: LlamaIndex
url: https://www.llamaindex.ai/
type: url
category: tools
tags: [framework, rag, agents, knowledge, python, open-source]
added: 2026-06-29
status: new
---

# LlamaIndex

LlamaIndex — фреймворк для построения контекстно-осведомлённых AI-агентов, выросший из RAG-библиотеки в полноценную агентную платформу. Особенно силён для knowledge-heavy агентов: RAG, indexing, retrieval, agents over data, structured extraction с human-in-the-loop и evaluation.

## Ключевые возможности

- **Workflows** — событийно-ориентированная оркестрация multi-agent систем на Python и TypeScript (без domain-specific language).
- **Agents** — агенты, работающие с данными: retrieval, querying, structured extraction, multi-step reasoning.
- **RAG/Indexing** — богатая экосистема индексации: парсинг документов, чанкинг, embedding, retrieval.
- **Data connectors** — интеграция с 160+ источниками данных: файлы, базы, API, облачные хранилища.
- **Human-in-the-loop** — встроенные паузы для approvals и корректировок.
- **Multi-agent patterns** — шаблоны для координации нескольких агентов.
- **Tracing/Evaluation** — встроенная observability и evals.

## Когда применять

| Сценарий | Почему LlamaIndex |
|----------|-------------------|
| **Knowledge-heavy агенты** | RAG-first: retrieval, indexing, data connectors из коробки |
| **Агенты над документами** | Парсинг PDF, DOCX, таблиц, кода — автоматически |
| **Structured extraction** | Извлечение структурированных данных из неструктурированного текста |
| **Data pipeline agents** | Агенты как часть data pipeline с retrieval и трансформацией |
| **Multi-modal retrieval** | Поиск по тексту, изображениям, таблицам |

## Когда НЕ применять

- Stateful durable execution — [LangGraph](../frameworks/langgraph.md) сильнее
- Role-based multi-agent без данных — [CrewAI](../frameworks/crewai.md) проще
- Enterprise .NET — [Semantic Kernel](../frameworks/semantic-kernel.md)/MAF
- Tool-heavy workflows без RAG — [OpenAI Agents SDK](../platforms/openai.md)

## Open Source статус

- **LlamaIndex** — open source (MIT license), GitHub: `run-llama/llama_index`
- **LlamaCloud** — managed service (платный) для индексации и парсинга
- Активное сообщество, частые релизы

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Agents over data** | Агенты запрашивают, анализируют и синтезируют данные из индексов |
| **Workflow orchestration** | Event-driven оркестрация multi-agent workflows (Python/TS) |
| **Tool calling** | Агенты используют любые инструменты (API, функции, другие агенты) |
| **RAG** | Встроенный retrieval augmented generation с гибкими пайплайнами |
| **Memory** | Conversation memory, persistent agent state |
| **HITL** | Pause/resume для approvals, корректировок |
| **Observability** | Tracing, evals, интеграция с Arize/LangSmith |
| **Structured outputs** | Извлечение структурированных данных с citations |

## Сравнение с аналогами

| Критерий | LlamaIndex | LangChain/LangGraph | OpenAI Agents SDK |
|----------|-----------|-------------------|-------------------|
| **RAG** | First-class | Retrievers | File Search |
| **Data connectors** | 160+ | Меньше | Только File Search |
| **Indexing** | Встроенный | Через библиотеки | Нет |
| **Orchestration** | Workflows | LangGraph | Agents SDK |
| **Structured extraction** | Сильный | Средний | Structured Outputs |

## Use Cases

- **Document Q&A agents**: агент, отвечающий на вопросы по корпоративной документации
- **Research agents**: retrieval + synthesis по научным статьям
- **Data extraction pipelines**: извлечение структурированных данных из документов
- **Multi-modal retrieval**: поиск по тексту, таблицам, изображениям
- **Knowledge base agents**: база знаний компании как retrieval-источник

## Отзывы и критика

### Сильные стороны:
- Лучший в классе для RAG и knowledge-heavy агентов
- 160+ data connectors — широчайшая интеграция
- Workflows: event-driven оркестрация без domain-specific языка
- Активное open-source сообщество
- Хорошая документация и примеры

### Слабые стороны:
- Слабее в non-RAG сценариях (orchestration без данных)
- Оркестрация требует дополнительного уровня (Workflows моложе [LangGraph](langgraph.md))
- Меньше adoption в enterprise .NET
- LlamaCloud — дополнительная стоимость для managed парсинга

## Связи

- [LangGraph](../frameworks/langgraph.md) — альтернативный orchestration-фреймворк (RAG через retrievers)
- [Исследование фреймворков](../agent-frameworks-research.md) — LlamaIndex в карте выбора
- [RAG для агентов](../../patterns/architecture-design/rag-for-agents.md) — LlamaIndex как RAG-реализация
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — LlamaIndex Workflows как orchestration
- [Модели для эмбеддингов](../embeddings/OVERVIEW.md) — эмбеддинги для LlamaIndex retrieval
- [Модельная карта](../agent-model-map.md) — выбор модели для LlamaIndex агентов

*Добавлено: 2026-06-29*
