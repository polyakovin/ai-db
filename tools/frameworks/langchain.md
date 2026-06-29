---
title: LangChain
url: https://www.langchain.com/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# LangChain

Фреймворк для создания LLM-приложений и агентов. Chains, RAG, инструменты, интеграции. Самый распространённый open-source фреймворк (~134K GitHub stars, 1000+ интеграций).

## Ключевые возможности

- **Model I/O** — унифицированный интерфейс к 100+ LLM-провайдерам
- **Chains** — композиция вызовов: последовательные, параллельные, условные
- **Retrieval (RAG)** — загрузка, чанкинг, эмбеддинги, векторные БД
- **Agents** — ReAct-агенты с tool calling (встроенная архитектура `create_agent`)
- **Memory** — persistence диалогов и состояния
- **Callbacks** — tracing, логирование, стриминг
- **[[langgraph.md|LangGraph]]** — stateful оркестрация для multi-agent систем (отдельный пакет)
- **[[../langsmith.md|LangSmith]]** — observability и evaluation (отдельный продукт)
- **Deep Agents** — long-running агенты с filesystem, sandbox, subagents

## Модели / Продукты

- LangChain (open-source ядро, MIT)
- [[langgraph.md|LangGraph]] (оркестрация, MIT)
- [[../langsmith.md|LangSmith]] (observability, proprietary)
- Deep Agents (long-running агенты)

## Цены и доступ

- **Open Source:** да, [MIT-лицензия](https://github.com/langchain-ai/langchain)
- Бесплатно (framework)
- [[../langsmith.md|LangSmith]]: бесплатный Developer-план (5K traces/мес), Plus $39/мес/seat

## Агентные возможности

- Tool calling через стандартизированный интерфейс
- ReAct-архитектура из коробки
- Multi-agent оркестрация через [[langgraph.md|LangGraph]]
- Persistence, checkpointing, rewind, human-in-the-loop
- Deep Agents для long-running задач с filesystem

## Open Source статус

**Полностью Open Source** (MIT). [[langgraph.md|LangGraph]] тоже MIT. [[../langsmith.md|LangSmith]] — proprietary SaaS.

## Use Cases

- Быстрое прототипирование RAG-приложений
- Чат-боты с memory и tool calling
- Enterprise multi-agent системы (через [[langgraph.md|LangGraph]])
- Data extraction pipelines
- Агенты с доступом к базам данных и API

## Отзывы и критика

- Плюсы: широчайшая экосистема, 1000+ интеграций, зрелая документация
- Минусы: высокий порог входа, много абстракций, breaking changes между версиями

## Связи

- [LangGraph](langgraph.md) — stateful оркестрация
- [LangSmith](../langsmith.md) — observability
- [Исследование фреймворков](../agent-frameworks-research.md)
- [Agent Harness](../../patterns/architecture-design/agent-harness.md)

*Добавлено: 2026-06-29*
