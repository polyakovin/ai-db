---
title: HippoRAG
url: https://github.com/OSU-NLP-Group/HippoRAG
type: url
category: tools
tags: [memory, rag, knowledge-graph, retrieval, research, open-source]
added: 2026-07-02
status: new
---

# HippoRAG

HippoRAG - research framework для RAG + knowledge graphs + Personalized PageRank, вдохновленный long-term memory. Версия HippoRAG 2 позиционируется как переход от RAG к memory framework.

## Ключевые возможности

- OpenIE-based graph construction.
- Retrieval и QA modes.
- Personalized PageRank-inspired retrieval.
- Фокус на associativity, multi-hop retrieval и sense-making.
- Поддержка hosted и local/[vLLM](../inference/vllm.md) deployments.

## Когда применять

- Нужно исследовать memory-like retrieval и multi-hop associativity.
- Важны experiments, benchmarks и retrieval/QA evaluation.
- Команда готова дорабатывать production hardening самостоятельно.

## Когда не применять

- Нужна готовая enterprise RAG platform.
- Требуется простой document ingestion UI.
- Нужна low-ops библиотека для быстрого production deployment.

## Open Source статус

- Репозиторий: [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG)
- Пакет: `hipporag`
- Лицензия: MIT
- Papers: [HippoRAG](https://arxiv.org/abs/2405.14831), [HippoRAG 2](https://arxiv.org/abs/2502.14802)

## Связи

- [Cognee](cognee.md) - product-oriented agent memory platform.
- [Fast GraphRAG](fast-graphrag.md) - использует PageRank-based graph exploration.
- [LightRAG](lightrag.md) - graph + vector retrieval baseline.
