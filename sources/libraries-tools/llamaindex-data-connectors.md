---
title: LlamaIndex Data Connectors and Ingestion Pipeline
url: https://developers.llamaindex.ai/python/framework/module_guides/loading/connector/
type: url
category: sources
tags: [llamaindex, rag, ingestion, connectors, document-loaders]
added: 2026-07-02
status: verified
---

# LlamaIndex Data Connectors and Ingestion Pipeline

Официальная документация LlamaIndex по data connectors, LlamaHub и ingestion pipeline.

## Описание

- **Основные темы:** Readers/data connectors, преобразование источников в Document, ingestion transformations, cache, vector-store insertion, dedup/document management.
- **Практическая ценность:** reference для построения self-managed RAG ingestion pipeline с разными внешними источниками.
- **Relevance:** даёт реализацию паттерна "source → document → transformation → index".

## Связи

- [Автоматизация сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md)
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md)
- [LlamaIndex](../../tools/frameworks/llamaindex.md) — canonical-страница инструмента

## Статус

Добавлено: 2026-07-02

## Верификация

- **Дата:** 2026-07-08
- **Метод:** web_extract — https://developers.llamaindex.ai/python/framework/module_guides/loading/connector/
- **Результат:** Документация LlamaIndex по Data Connectors (LlamaHub) подтверждена. Читабельна, содержит описание reader-интерфейса, примеры использования. Содержание заметки соответствует.
