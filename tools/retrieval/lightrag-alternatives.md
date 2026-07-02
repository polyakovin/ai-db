# Аналоги LightRAG

Актуально на 2026-07-02. Это не canonical-страница инструментов, а карта выбора вокруг [LightRAG](lightrag.md). Факты по каждой альтернативе вынесены в отдельные страницы в этой же папке.

## Что считать аналогом

[LightRAG](lightrag.md) полезен там, где обычный vector search теряет связи между сущностями. Поэтому аналогами считаются не только прямые GraphRAG-библиотеки, но и решения, которые закрывают похожую задачу: строят knowledge graph, делают multi-hop retrieval, соединяют graph traversal с embeddings или дают production-обвязку вокруг RAG.

## Карта выбора

| Инструмент | Класс | Когда смотреть | Осторожно |
|---|---|---|---|
| [Microsoft GraphRAG](microsoft-graphrag.md) | canonical GraphRAG pipeline | Global questions, sensemaking, тематические обзоры больших корпусов | Индексация дорогая; GitHub README прямо предупреждает начинать с малого |
| [Fast GraphRAG](fast-graphrag.md) | lightweight GraphRAG | Нужен быстрый, promptable, incremental graph retrieval с меньшей стоимостью | Меньше зрелости, чем у крупных фреймворков; часть value уходит в managed service |
| [nano-graphrag](nano-graphrag.md) | minimal GraphRAG implementation | Обучение, прототип, кастомизация core pipeline | Не полная замена Microsoft GraphRAG; часть возможностей упрощена |
| [MiniRAG](minirag.md) | lightweight RAG для small models | On-device/edge сценарии, small open-source language models, ограниченный storage | Ближе к исследовательскому проекту; основан на идеях LightRAG |
| [LlamaIndex PropertyGraphIndex](llamaindex-property-graph-index.md) | framework-native graph index | Уже используется [LlamaIndex](../frameworks/llamaindex.md), нужны custom extractors/retrievers | Придется самому собрать production pipeline и storage decisions |
| [Neo4j GraphRAG for Python](neo4j-graphrag-python.md) | graph database-first RAG package | Есть Neo4j/Aura, нужен Cypher, property graph и controlled graph storage | Привязка к Neo4j-стеку; graph schema становится частью продукта |
| [AWS GraphRAG Toolkit](aws-graphrag-toolkit.md) | cloud graph toolkit | AWS/Neptune/OpenSearch, BYOKG, enterprise graph-enhanced GenAI | AWS-centric архитектура; меньше community adoption, чем у популярных RAG-фреймворков |
| [R2R](r2r.md) | production RAG API | Нужны REST API, hybrid search, multimodal ingestion, document management и knowledge graphs | Не graph-first инструмент; сложнее, если нужен только легкий library layer |
| [RAGFlow](ragflow.md) | RAG engine + agent platform | Нужен UI/workflow для enterprise document RAG и agent templates | Больше platform, чем библиотека; graph retrieval не главный фокус |
| [Cognee](cognee.md) | agent memory + knowledge graph | Долгосрочная память агентов, cross-session recall, self-hosted knowledge graph | Не прямой replacement для document QA; memory semantics важнее RAG benchmark |
| [HippoRAG](hipporag.md) | research memory/RAG framework | Multi-hop retrieval, associativity, memory experiments | Исследовательский stack; production hardening придется делать отдельно |
| [RAG-Anything](rag-anything.md) | multimodal extension | PDFs, Office docs, images, tables, formulas, cross-modal knowledge graph | Это скорее расширение LightRAG-семейства, а не независимая альтернатива |

## Рекомендации

- Нужен ближайший по духу open-source GraphRAG без тяжелой платформы: [Fast GraphRAG](fast-graphrag.md) или [nano-graphrag](nano-graphrag.md).
- Нужен production-ready knowledge-heavy agent в существующем Python stack: [LlamaIndex](../frameworks/llamaindex.md) + [LlamaIndex PropertyGraphIndex](llamaindex-property-graph-index.md).
- Нужен graph database как источник истины: [Neo4j GraphRAG for Python](neo4j-graphrag-python.md) или [AWS GraphRAG Toolkit](aws-graphrag-toolkit.md).
- Нужна document platform с API, пользователями и ingestion lifecycle: [R2R](r2r.md) или [RAGFlow](ragflow.md).
- Нужна долговременная память для агентов, а не только Q&A по документам: [Cognee](cognee.md) или [HippoRAG](hipporag.md).
- Нужны мультимодальные документы: [RAG-Anything](rag-anything.md) или [RAGFlow](ragflow.md), если важен UI/workflow слой.

## Практический baseline

Перед внедрением graph-based RAG стоит сравнить его с более дешевым baseline:

1. Dense embeddings + BM25/sparse retrieval.
2. Metadata filters по источнику, дате, типу документа и tenant.
3. Reranker на top-k.
4. Строгие citations и отказ при слабом evidence.
5. Набор eval cases для single-hop, multi-hop, summary и adversarial queries.

Graph layer оправдан, если baseline стабильно ломается на вопросах вида "как связаны X и Y", "какие основные темы всего корпуса", "что изменилось вокруг сущности", "собери цепочку причин/зависимостей".

## Due diligence

Проверять перед выбором инструмента:

- Ingestion: форматы, chunking, document deletion, reindex strategy.
- Graph quality: entity resolution, relation schema, duplicate handling, provenance.
- Retrieval modes: local/global search, multi-hop traversal, vector-graph fusion.
- Cost: LLM calls на extraction, community summaries, reranking и refresh.
- Storage: local files, graph DB, vector DB, backups, migrations.
- Operations: API, auth, observability, evals, tracing, rate limits.
- Security: tenant isolation, prompt injection handling, access control на retrieved context.
- Model flexibility: local LLMs, [OpenAI](../platforms/openai.md)-compatible endpoints, embedding providers.

## Primary Sources

Primary sources вынесены на страницы конкретных инструментов. Provenance-карточка обзора: [LightRAG Alternatives Research](../../sources/libraries-tools/lightrag-alternatives.md).

## Связанные заметки

- [LightRAG](lightrag.md) - canonical-страница инструмента.
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md) - общий retrieval pipeline.
- [LlamaIndex](../frameworks/llamaindex.md) - RAG-first framework для knowledge-heavy агентов.
- [Ререйкеры](../embeddings/rerankers.md) - усиление retrieval без graph layer.
- [Модели для эмбеддингов](../embeddings/OVERVIEW.md) - embedding layer для RAG.
