---
title: RAG-Anything
url: https://github.com/HKUDS/RAG-Anything
type: url
category: tools
tags: [rag, multimodal, knowledge-graph, retrieval, documents, open-source]
added: 2026-07-02
status: new
---

# RAG-Anything

RAG-Anything - multimodal RAG framework от HKUDS, построенный вокруг [LightRAG](lightrag.md). Он расширяет RAG на PDFs, Office documents, images, tables, equations и cross-modal knowledge graph retrieval.

## Ключевые возможности

- End-to-end multimodal document processing pipeline.
- Universal document support: PDF, Office docs, images и structured content.
- Specialized processors для images, tables и mathematical equations.
- Multimodal knowledge graph и cross-modal relationships.
- Vector-graph fusion retrieval.
- MinerU, Docling/PaddleOCR-oriented parsing paths.

## Когда применять

- Корпус состоит из сложных мультимодальных документов.
- Важны таблицы, формулы, диаграммы и изображения.
- Уже подходит [LightRAG](lightrag.md), но нужен multimodal ingestion/retrieval layer.

## Когда не применять

- Корпус преимущественно plain text.
- Не нужен heavy document parsing layer.
- Нужна независимая альтернатива, а не расширение [LightRAG](lightrag.md)-семейства.

## Open Source статус

- Репозиторий: [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)
- Пакет: `raganything`
- Лицензия: MIT

## Связи

- [LightRAG](lightrag.md) - базовый graph + vector retrieval слой.
- [MiniRAG](minirag.md) - lightweight ветка HKUDS RAG-экосистемы.
- [RAGFlow](ragflow.md) - platform-oriented document RAG альтернатива.
