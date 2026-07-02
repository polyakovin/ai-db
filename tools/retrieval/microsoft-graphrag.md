---
title: Microsoft GraphRAG
url: https://github.com/microsoft/graphrag
type: url
category: tools
tags: [rag, graphrag, knowledge-graph, retrieval, microsoft, open-source]
added: 2026-07-02
status: new
---

# Microsoft GraphRAG

Microsoft GraphRAG - open-source pipeline для graph-based RAG: извлекает knowledge graph из текста, строит community hierarchy, генерирует summaries и использует их для local/global retrieval.

## Ключевые возможности

- Indexing pipeline для извлечения сущностей, отношений и community summaries.
- Local search для вопросов вокруг конкретных сущностей.
- Global search для "sensemaking" вопросов по всему корпусу.
- CLI и Python package.
- Research lineage от Microsoft Research GraphRAG.

## Когда применять

- Нужно отвечать на широкие вопросы по корпусу: темы, конфликты, тенденции, обзор.
- Корпус содержит много связанных сущностей и narrative/private data.
- Команда готова платить за дорогую offline indexing фазу.

## Когда не применять

- Нужен самый простой self-hosted RAG слой без сложной индексации.
- Корпус часто обновляется малыми порциями и нет бюджета на graph refresh.
- Вопросы в основном локальные и хорошо решаются hybrid search + reranker.

## Open Source статус

- Репозиторий: [microsoft/graphrag](https://github.com/microsoft/graphrag)
- Документация: [GraphRAG docs](https://microsoft.github.io/graphrag/)
- Лицензия: MIT

## Связи

- [LightRAG](lightrag.md) - более lightweight альтернатива с фокусом на graph + vector retrieval.
- [Аналоги LightRAG](lightrag-alternatives.md) - карта выбора.
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md) - общий retrieval pipeline.
