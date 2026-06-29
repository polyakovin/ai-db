---
title: Chroma
url: https://www.trychroma.com/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Chroma

Open-source векторная БД для RAG и semantic search. Простая, встраиваемая, AI-native — создана специально для LLM-приложений.

## Ключевые возможности

- Встраивается прямо в Python-приложение (без отдельного сервера)
- Автоматический выбор embedding-функции ([[../platforms/openai.md|OpenAI]], [[../cohere.md|Cohere]], [[../huggingface.md|Hugging Face]], Sentence Transformers)
- Два режима: in-memory (для прототипов) и persistent (для продакшена)
- Metadata filtering
- Режим клиент-сервер для team deployments
- Интеграция с [[../frameworks/langchain.md|LangChain]], [[../frameworks/llamaindex.md|LlamaIndex]], [[../platforms/openai.md|OpenAI]]
- Автоматическое обновление эмбеддингов при изменении документов

## Модели / Продукты

- Chroma Core (open-source, Apache 2.0)
- Chroma Cloud (managed сервис)

## Цены и доступ

- **Open Source:** да, [Apache 2.0](https://github.com/chroma-core/chroma)
- Бесплатно для self-hosted
- Cloud: бесплатный тир (ограниченный storage), платные от $0.35/GB/мес

## Агентные возможности

- Memory backend для агентов (хранение контекста между сессиями)
- Retrieval для RAG-агентов
- Быстрая индексация на лету для исследовательских агентов
- Metadata filtering для multi-tenant агентов

## Open Source статус

**Полностью Open Source** (Apache 2.0). Cloud — managed сервис.

## Use Cases

- RAG-агент с embedding-based retrieval
- Memory store для диалоговых агентов
- Прототипирование: поднял за 3 строки кода
- Small-to-medium scale (сотни тысяч документов)

## Отзывы и критика

- Плюсы: экстремальная простота, AI-native, отличная документация
- Минусы: не для high-scale (> миллиона документов), меньше фич чем у [[qdrant.md|Qdrant]]/[[pinecone.md|Pinecone]]

## Связи

- [Qdrant](qdrant.md) — production-grade альтернатива
- [Pinecone](pinecone.md) — serverless альтернатива
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md)
- [Модели для эмбеддингов](../embedding-models.md)

*Добавлено: 2026-06-29*
