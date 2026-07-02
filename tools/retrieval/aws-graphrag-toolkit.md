---
title: AWS GraphRAG Toolkit
url: https://github.com/awslabs/graphrag-toolkit
type: url
category: tools
tags: [rag, graphrag, knowledge-graph, aws, retrieval, open-source]
added: 2026-07-02
status: new
---

# AWS GraphRAG Toolkit

AWS GraphRAG Toolkit - набор Python tools для graph-enhanced GenAI applications. Основной акцент: hierarchical lexical graph, BYOKG-RAG и AWS graph/search infrastructure.

## Ключевые возможности

- Lexical Graph для построения hierarchical graph из unstructured data.
- Question-answering strategies поверх graph.
- BYOKG-RAG для question answering over custom knowledge graphs.
- Интеграция с AWS-экосистемой: Neptune, OpenSearch и related workshops.
- Отдельные packages и examples для graph-enhanced retrieval.

## Когда применять

- Проект уже в AWS и использует Neptune/OpenSearch.
- Есть bring-your-own knowledge graph сценарий.
- Нужен enterprise graph-enhanced GenAI pipeline.

## Когда не применять

- Нужен маленький локальный Python library без cloud assumptions.
- Команда не использует AWS graph/search stack.
- Нужна популярная community-first GraphRAG библиотека.

## Open Source статус

- Репозиторий: [awslabs/graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)
- Лицензия: Apache-2.0
- Документация: [GraphRAG Toolkit docs](https://awslabs.github.io/graphrag-toolkit/)

## Связи

- [Neo4j GraphRAG for Python](neo4j-graphrag-python.md) - graph database-first альтернатива вне AWS.
- [Microsoft GraphRAG](microsoft-graphrag.md) - research-oriented GraphRAG pipeline.
- [LightRAG](lightrag.md) - lightweight self-hosted альтернатива.
