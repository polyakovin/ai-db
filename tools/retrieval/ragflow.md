---
title: RAGFlow
url: https://github.com/infiniflow/ragflow
type: url
category: tools
tags: [rag, retrieval, document-ai, agents, platform, open-source]
added: 2026-07-02
status: new
---

# RAGFlow

RAGFlow - open-source RAG engine, который совмещает document understanding, context engine и agent templates. Он ближе к платформе для enterprise document RAG, чем к минимальной GraphRAG-библиотеке.

## Ключевые возможности

- Document parsing и RAG workflow.
- Context engine для retrieval-слоя.
- Agent templates.
- UI и developer/user guides.
- Self-hosted open-source deployment.

## Когда применять

- Нужна платформа для document-heavy RAG с UI.
- Важны ingestion workflow, templates и быстрый internal tool setup.
- Команда хочет меньше писать glue code вокруг RAG.

## Когда не применять

- Нужен только lightweight GraphRAG library.
- Retrieval должен быть полностью custom и embedded в существующий код.
- Graph traversal является главным differentiated layer.

## Open Source статус

- Репозиторий: [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- Лицензия: Apache-2.0
- Документация: [RAGFlow docs](https://ragflow.io/docs/)

## Связи

- [R2R](r2r.md) - production RAG API альтернатива.
- [LightRAG](lightrag.md) - graph + vector RAG library.
- [RAG-Anything](rag-anything.md) - multimodal RAG framework.
