---
title: LightRAG
url: https://github.com/HKUDS/LightRAG
type: url
category: tools
tags: [rag, graphrag, knowledge-graph, retrieval, python, open-source]
added: 2026-07-02
status: new
---

# LightRAG

LightRAG - open-source RAG-фреймворк, который объединяет graph-based retrieval и vector retrieval. Его смысл не в том, чтобы заменить обычный векторный поиск всегда, а в том, чтобы улучшать ответы на вопросы, где важны сущности, связи, multi-hop контекст и обновляемая база знаний.

## Ключевые возможности

- Graph + vector retrieval: извлечение по сущностям, отношениям и семантическим векторам.
- Dual-level retrieval: low-level факты и high-level связи/темы.
- Incremental update: добавление новых документов без полного пересоздания индекса.
- WebUI и API server для локальной эксплуатации.
- Поддержка storage backends: local, Neo4j, PostgreSQL, MongoDB, OpenSearch и другие варианты из экосистемы проекта.
- Reranker support, citations, RAGAS evaluation и Langfuse tracing.
- Multimodal extension через [RAG-Anything](https://github.com/HKUDS/RAG-Anything).

## Когда применять

| Сценарий | Почему LightRAG |
|---|---|
| Корпоративная база знаний с перекрестными связями | Граф помогает собирать контекст вокруг сущностей и отношений |
| Multi-hop вопросы | Retrieval может проходить через связанные сущности, а не только похожие chunks |
| Частые обновления корпуса | Incremental update снижает стоимость обновления индекса |
| Нужен self-hosted RAG без тяжелой платформы | Python package, WebUI и storage backends дают быстрый старт |

## Когда не применять

- Простые FAQ и локальные вопросы по одному документу: hybrid vector/BM25 + reranker обычно дешевле.
- Строгие графовые запросы по уже нормализованной БД: лучше смотреть в сторону graph database + Cypher/SPARQL pipeline.
- Большой корпус без бюджета на entity/relation extraction: graph indexing может стать основной стоимостью.
- Требуется готовый enterprise workflow с пользователями, RBAC, UI и document lifecycle: production RAG platforms могут быть практичнее.

## Open Source статус

- Репозиторий: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- Лицензия: MIT
- Пакет: `lightrag-hku`
- Исследовательская статья: [LightRAG: Simple and Fast Retrieval-Augmented Generation](https://arxiv.org/abs/2410.05779)

## Связи

- [Аналоги LightRAG](lightrag-alternatives.md) - сравнительная карта GraphRAG/RAG-инструментов.
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md) - архитектурный слой retrieval в агентной системе.
- [LlamaIndex](../frameworks/llamaindex.md) - framework-native альтернатива для knowledge-heavy агентов.
- [Ререйкеры](../embeddings/rerankers.md) - второй этап ранжирования для hybrid retrieval.
- [LightRAG source](../../sources/libraries-tools/lightrag.md) - provenance-карточка источника.

*Добавлено: 2026-07-02*
