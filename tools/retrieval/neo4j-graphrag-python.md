---
title: Neo4j GraphRAG for Python
url: https://neo4j.com/docs/neo4j-graphrag-python/current/
type: url
category: tools
tags: [rag, graphrag, knowledge-graph, graph-database, retrieval, python]
added: 2026-07-02
status: new
---

# Neo4j GraphRAG for Python

Neo4j GraphRAG for Python - first-party Python package с GraphRAG features для Neo4j. Подходит, когда graph database является не побочным индексом, а центральным storage/query слоем.

## Ключевые возможности

- Vector indexes и vector retrieval внутри Neo4j.
- Knowledge Graph Builder и pipeline components.
- LLM provider extras: Ollama, [OpenAI](../platforms/openai.md), Google, Cohere, Anthropic, MistralAI.
- External retrievers для Weaviate, Pinecone и [Qdrant](../vector-dbs/qdrant.md).
- Совместимость с Neo4j Aura и Neo4j 5.18+.

## Когда применять

- Knowledge graph уже хранится в Neo4j или Aura.
- Нужны Cypher, property graph model и контролируемая graph schema.
- Требуется совместить vector search и graph traversal в одном graph-DB стеке.

## Когда не применять

- Нужен database-agnostic lightweight RAG слой.
- Команда не готова поддерживать graph schema и Cypher queries.
- Документы простые и хорошо ищутся через vector DB + reranker.

## Open Source статус

- Документация: [GraphRAG for Python](https://neo4j.com/docs/neo4j-graphrag-python/current/)
- Пакет: `neo4j-graphrag`
- Это renamed continuation of `neo4j-genai`.

## Связи

- [LlamaIndex PropertyGraphIndex](llamaindex-property-graph-index.md) - framework-native вариант с Neo4j integration.
- [AWS GraphRAG Toolkit](aws-graphrag-toolkit.md) - cloud graph toolkit.
- [LightRAG](lightrag.md) - database-agnostic lightweight альтернатива.
