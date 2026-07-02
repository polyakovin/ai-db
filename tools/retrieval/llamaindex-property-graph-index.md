---
title: LlamaIndex PropertyGraphIndex
url: https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/
type: url
category: tools
tags: [rag, graphrag, property-graph, retrieval, llamaindex, python]
added: 2026-07-02
status: new
---

# LlamaIndex PropertyGraphIndex

LlamaIndex PropertyGraphIndex - graph indexing компонент внутри [LlamaIndex](../frameworks/llamaindex.md). Он строит property graph из документов, поддерживает graph/vector stores и дает retrievers для graph-aware retrieval.

## Ключевые возможности

- Graph construction через configurable `kg_extractors`.
- Retrieval через graph paths, vector context, synonyms и text-to-Cypher.
- Поддержка existing graph store и optional vector store.
- Интеграции с Neo4j, Nebula, Qdrant и другими storage слоями через [LlamaIndex](../frameworks/llamaindex.md).
- Можно расширять extractors и retrievers.

## Когда применять

- В проекте уже используется [LlamaIndex](../frameworks/llamaindex.md).
- Нужен graph-aware retrieval как часть broader RAG/agent pipeline.
- Важна гибкость кастомных extractors, retrievers и storage backends.

## Когда не применять

- Нужна готовая standalone GraphRAG-система с WebUI.
- Команда не хочет сама проектировать ingestion, evals и operations.
- Важнее graph database-first подход с явной schema и Cypher governance.

## Open Source статус

- Документация: [Using a Property Graph Index](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/)
- Родительский фреймворк: [LlamaIndex](../frameworks/llamaindex.md)
- Лицензия следует open-source ядру [LlamaIndex](../frameworks/llamaindex.md).

## Связи

- [LlamaIndex](../frameworks/llamaindex.md) - canonical-страница фреймворка.
- [Neo4j GraphRAG for Python](neo4j-graphrag-python.md) - graph database-first альтернатива.
- [LightRAG](lightrag.md) - standalone lightweight GraphRAG.
