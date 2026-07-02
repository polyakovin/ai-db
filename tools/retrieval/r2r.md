---
title: R2R
url: https://github.com/SciPhi-AI/R2R
type: url
category: tools
tags: [rag, retrieval, knowledge-graph, api, multimodal, open-source]
added: 2026-07-02
status: new
---

# R2R

R2R - production-oriented AI retrieval system с REST API. Это не чистый GraphRAG clone, а RAG platform layer: ingestion, hybrid search, knowledge graphs, document management и agentic retrieval.

## Ключевые возможности

- RESTful API и Python/JavaScript SDK.
- Multimodal ingestion.
- Hybrid search: semantic + keyword search.
- Automatic entity and relationship extraction.
- Agentic RAG и Deep Research API.
- User/access management и document lifecycle.

## Когда применять

- Нужен production API для RAG-продукта.
- Важны document management, users, collections и auth.
- Graph retrieval нужен как часть broader retrieval platform.

## Когда не применять

- Нужен легкий library layer внутри существующего backend.
- Требуется именно graph-first retrieval algorithm.
- Не нужен platform/server слой.

## Open Source статус

- Репозиторий: [SciPhi-AI/R2R](https://github.com/SciPhi-AI/R2R)
- Пакет: `r2r`
- Лицензия: MIT

## Связи

- [RAGFlow](ragflow.md) - соседняя RAG platform с UI/workflow акцентом.
- [LightRAG](lightrag.md) - graph-first lightweight library.
- [Аналоги LightRAG](lightrag-alternatives.md) - карта выбора.
