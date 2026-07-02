---
title: nano-graphrag
url: https://github.com/gusye1234/nano-graphrag
type: url
category: tools
tags: [rag, graphrag, knowledge-graph, retrieval, python, open-source]
added: 2026-07-02
status: new
---

# nano-graphrag

nano-graphrag - небольшая, easy-to-hack реализация GraphRAG. Полезна как учебный и прототипный слой, когда хочется понимать и менять core pipeline.

## Ключевые возможности

- Local и global GraphRAG search.
- Incremental insert с дедупликацией по content hash.
- Async API.
- Поддержка naive RAG mode.
- Pluggable storage: KV, vector storage, graph storage.
- Встроенная поддержка NetworkX и Neo4j для graph storage.

## Когда применять

- Нужно изучить GraphRAG mechanics без большого framework.
- Нужен прототип с кастомными prompts, storage и chunking.
- Команда хочет быстро проверить идею на малом корпусе.

## Когда не применять

- Нужна production-платформа с governance, auth и UI.
- Нужны все возможности [Microsoft GraphRAG](microsoft-graphrag.md).
- Корпус большой и требует надежной операционной поддержки.

## Open Source статус

- Репозиторий: [gusye1234/nano-graphrag](https://github.com/gusye1234/nano-graphrag)
- Пакет: `nano-graphrag`
- Лицензия: MIT

## Связи

- [Microsoft GraphRAG](microsoft-graphrag.md) - исходная методологическая точка сравнения.
- [Fast GraphRAG](fast-graphrag.md) - соседняя lightweight реализация.
- [LightRAG](lightrag.md) - production-oriented lightweight GraphRAG.
