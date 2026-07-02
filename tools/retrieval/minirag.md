---
title: MiniRAG
url: https://github.com/HKUDS/MiniRAG
type: url
category: tools
tags: [rag, graphrag, small-language-models, retrieval, python, open-source]
added: 2026-07-02
status: new
---

# MiniRAG

MiniRAG - lightweight RAG-фреймворк от HKUDS для small/open-source language models. Он использует heterogeneous graph indexing и topology-enhanced retrieval, чтобы снижать требования к semantic understanding модели.

## Ключевые возможности

- Heterogeneous graph indexing: chunks и named entities в единой структуре.
- Lightweight topology-enhanced retrieval.
- Фокус на small language models и on-device сценариях.
- Поддержка нескольких graph backends.
- Research benchmark LiHua-World для lightweight RAG.

## Когда применять

- Нужен RAG для small/open-source models.
- Есть ограничения по storage, latency или deployment environment.
- Нужно сравнить [LightRAG](lightrag.md)-подход с более компактным вариантом.

## Когда не применять

- Нужна зрелая production-платформа с UI и lifecycle management.
- Используются сильные hosted LLMs и основная проблема не в ресурсоемкости.
- Нужна широкая экосистема integrations.

## Open Source статус

- Репозиторий: [HKUDS/MiniRAG](https://github.com/HKUDS/MiniRAG)
- Пакет: `minirag-hku`
- Лицензия: MIT
- Paper: [MiniRAG: Towards Extremely Simple Retrieval-Augmented Generation](https://arxiv.org/abs/2501.06713)

## Связи

- [LightRAG](lightrag.md) - базовая родственная система.
- [RAG-Anything](rag-anything.md) - multimodal ветка HKUDS RAG-экосистемы.
- [Retrieval tools overview](OVERVIEW.md) - карта выбора.
