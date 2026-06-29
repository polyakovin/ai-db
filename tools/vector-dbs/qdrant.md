---
title: Qdrant
url: https://qdrant.tech/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Qdrant

Векторная БД для production: фильтрация, гибридный поиск, high availability. Написана на Rust, API-first.

## Ключевые возможности

- Гибридный поиск: dense (векторный) + sparse (BM25) в одном запросе
- Фильтрация по payload (метаданным) с богатым синтаксисом
- Квантование векторов для экономии памяти (до 30×)
- Шардирование и репликация для high availability
- On-disk индексация для больших коллекций
- REST API и gRPC
- Клиенты: Python, Rust, Go, JS, Java
- Multitenancy из коробки

## Модели / Продукты

- Qdrant (open-source, Apache 2.0)
- Qdrant Cloud (managed сервис)
- Qdrant Hybrid Cloud (on-prem + cloud)

## Цены и доступ

- **Open Source:** да, [Apache 2.0](https://github.com/qdrant/qdrant)
- Бесплатно для self-hosted
- Cloud: бесплатный тир (1GB, 1 cluster), платные от $25/мес

## Агентные возможности

- Точный retrieval с фильтрацией (агент ищет «только документы за последнюю неделю с рейтингом > 4»)
- HyDE (гипотетический документ) и multi-vector retrieval
- Рекомендации для агентов: «найди похожие кейсы»
- Изоляция tenant'ов для multi-agent SaaS

## Open Source статус

**Полностью Open Source** (Apache 2.0). Cloud — managed сервис.

## Use Cases

- Production RAG с миллионами документов
- E-commerce рекомендации
- Enterprise search с фильтрацией
- Multi-tenant агентные платформы

## Отзывы и критика

- Плюсы: лучшая производительность среди open-source векторных БД, гибридный поиск, Rust-основа
- Минусы: сложнее в настройке чем [[chroma.md|Chroma]], меньше интеграций чем [[pinecone.md|Pinecone]]

## Связи

- [Chroma](chroma.md) — более простая альтернатива
- [Pinecone](pinecone.md) — serverless альтернатива
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md)
- [Модели для эмбеддингов](../embedding-models.md)

*Добавлено: 2026-06-29*
