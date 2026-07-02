---
title: Cognee
url: https://github.com/topoteretes/cognee
type: url
category: tools
tags: [memory, rag, knowledge-graph, agents, retrieval, open-source]
added: 2026-07-02
status: new
---

# Cognee

Cognee - open-source AI memory platform для агентов. Он строит self-hosted knowledge graph и соединяет vector embeddings, graph reasoning и long-term memory across sessions.

## Ключевые возможности

- Persistent long-term memory for agents.
- Operations: `remember`, `recall`, `forget`, `improve`.
- Knowledge graph + vector search.
- Session memory с синхронизацией в permanent graph.
- Docker, local UI, API server и MCP-oriented integrations.
- Tenant isolation, traceability и OTEL-oriented observability claims.

## Когда применять

- Нужна память агента между сессиями.
- Важен "company brain" для нескольких агентов или рабочих поверхностей.
- Retrieval должен учитывать не только документы, но и accumulated interactions.

## Когда не применять

- Нужен обычный document Q&A по статическому корпусу.
- Memory semantics и lifecycle не нужны.
- Требуется минимальный GraphRAG algorithm без platform layer.

## Open Source статус

- Репозиторий: [topoteretes/cognee](https://github.com/topoteretes/cognee)
- Пакет: `cognee`
- Лицензия: Apache-2.0
- Документация: [Cognee docs](https://docs.cognee.ai/)

## Связи

- [HippoRAG](hipporag.md) - research memory/RAG framework.
- [LightRAG](lightrag.md) - document/knowledge GraphRAG baseline.
- [Agent memory patterns](../../patterns/advanced/agent-memory-patterns.md)
