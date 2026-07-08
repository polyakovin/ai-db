---
title: LangChain Document Loaders
url: https://docs.langchain.com/oss/python/integrations/document_loaders
type: url
category: sources
tags: [langchain, document-loaders, ingestion, integrations]
added: 2026-07-02
status: verified
---

# LangChain Document Loaders

Официальная документация LangChain по document loader integrations.

## Описание

- **Основные темы:** единый loader-интерфейс, `load()`, `lazy_load()`, loaders для productivity tools, webpages, PDFs, cloud providers и common file types.
- **Практическая ценность:** показывает, как стандартизировать чтение внешних источников в единый формат документов.
- **Relevance:** useful reference для ingestion слоя, когда нужно быстро подключать разные source adapters.

## Связи

- [Автоматизация сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md)
- [LangChain](../../tools/frameworks/langchain.md) — canonical-страница инструмента

## Статус

Добавлено: 2026-07-02

## Верификация

- **Дата:** 2026-07-08
- **Метод:** web_extract — https://docs.langchain.com/oss/python/integrations/document_loaders
- **Результат:** Документация LangChain Document Loaders подтверждена. Поддерживает load()/lazy_load() интерфейс, множество интеграций. Содержание заметки соответствует.
