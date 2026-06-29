---
title: Flowise
url: https://flowiseai.com/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Flowise

Low-code LLM app builder: drag-and-drop цепочки, RAG, агенты, чат-интерфейсы. Построен на [LangChain](langchain.md) и [LangGraph](langgraph.md).

## Ключевые возможности

- Drag-and-drop интерфейс для построения LLM-цепочек
- Визуальный конструктор агентов с tool calling
- Встроенный чат-интерфейс для тестирования
- RAG: загрузка документов, чанкинг, эмбеддинги, векторные БД
- Мульти-агентные workflow (через [[langgraph.md|LangGraph]])
- API endpoint для каждого потока
- Встроенная аналитика использования
- Рынок шаблонов (marketplace)

## Модели / Продукты

- Flowise (open-source, Apache 2.0)
- Flowise Cloud (managed)

## Цены и доступ

- **Open Source:** да, [Apache 2.0](https://github.com/FlowiseAI/Flowise)
- Бесплатно для self-hosted
- Cloud: бесплатный тир, платные от $20/мес

## Агентные возможности

- Визуальное построение ReAct-агентов с tool calling
- Multi-agent оркестрация через [[langgraph.md|LangGraph]]
- Human-in-the-loop узлы
- Credential management для API-ключей
- Автоматическая генерация API для агентов

## Open Source статус

**Полностью Open Source** (Apache 2.0).

## Use Cases

- Быстрое прототипирование RAG-агента без кода
- Чат-боты с knowledge base для поддержки
- Low-code автоматизация для не-разработчиков
- Обучение: визуализация agentic workflows

## Отзывы и критика

- Плюсы: порог входа нулевой, визуальное построение, интеграция с [[langchain.md|LangChain]]
- Минусы: не для сложной кастомной логики, vendor lock-in на [[langchain.md|LangChain]]-экосистему

## Связи

- [LangChain](langchain.md) — базовый фреймворк
- [LangGraph](langgraph.md) — мульти-агентная оркестрация
- [Dify](dify.md) — low-code альтернатива
- [Исследование фреймворков](../agent-frameworks-research.md)

*Добавлено: 2026-06-29*
