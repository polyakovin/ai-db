---
title: LightRAG
url: https://github.com/hkuds/lightrag
type: url
category: sources
tags: [rag, knowledge-graph, retrieval, open-source, python]
added: 2026-07-01
status: new
---

# LightRAG

Simple and Fast Retrieval-Augmented Generation с использованием графов знаний.

## Описание

LightRAG — это RAG-система, которая объединяет традиционный векторный поиск с графами знаний для улучшения качества извлечения информации. Проект позиционируется как простая и быстрая альтернатива сложным RAG-решениям.

## Обзор ресурса

- **Автор:** HKUDS (Hong Kong University of Data Science)
- **Лицензия:** MIT
- **Статус:** Активный проект (2026); 13K+ GitHub stars
- **Позиционирование:** Simple and Fast RAG с графами знаний — баланс между точностью и производительностью
- **Доступ:** SDK (Python) + PyPI package (`lightrag-hku`) + WebUI
- **Ключевые особенности:**
  - Graph-based retrieval + vector search
  - Поддержка multimodal документов (через RAG-Anything integration)
  - 4 стратегии чанкинга: `Fix`, `Recursive`, `Vector`, `Paragraph`
  - Role-specific LLM configuration (EXTRACT, QUERY, KEYWORDS, VLM)
  - Интеграция с OpenSearch, Neo4J, PostgreSQL, MongoDB
  - Reranker support для mixed queries
  - RAGAS evaluation + Langfuse tracing
  - Document deletion с автоматическим KG regeneration
- **Relevance:** Практический пример production-ready RAG с графами знаний; модель-агностик

## Ключевые возможности

- **Graph + Vector Retrieval:** Комбинирует структурные знания (графы) с семантическим поиском (векторы)
- **Multimodal Support:** Обработка PDF, изображений, таблиц, формул через MinerU/Docling
- **Scalability:** Оптимизировано для больших датасетов
- **Storage Backends:** Neo4J, PostgreSQL, MongoDB, OpenSearch, local storage
- **Evaluation Built-in:** RAGAS metrics для context precision
- **Citation Support:** Source attribution для enhanced traceability

## Связи

- [LightRAG](../../tools/retrieval/lightrag.md) — canonical-страница инструмента
- [Retrieval tools overview](../../tools/retrieval/OVERVIEW.md) — соседние retrieval-решения
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md) — архитектурный контекст
- [RAG-Anything](../../tools/retrieval/rag-anything.md) — multimodal RAG от той же команды
- [MiniRAG](../../tools/retrieval/minirag.md) — облегчённая версия от той же команды
- [VideoRAG](https://github.com/HKUDS/VideoRAG) — RAG для длинных видео-контекстов
