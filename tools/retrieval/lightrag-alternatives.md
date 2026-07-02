# Аналоги LightRAG

Актуально на 2026-07-02. Эта заметка сравнивает инструменты, которые можно рассматривать как альтернативы или соседние решения к [LightRAG](lightrag.md): graph-based RAG, knowledge-graph retrieval, production RAG engines и agent memory systems.

## Что считать аналогом

[LightRAG](lightrag.md) полезен там, где обычный vector search теряет связи между сущностями. Поэтому аналогами считаются не только прямые GraphRAG-библиотеки, но и решения, которые закрывают похожую задачу: строят knowledge graph, делают multi-hop retrieval, соединяют graph traversal с embeddings или дают production-обвязку вокруг RAG.

## Карта выбора

| Инструмент | Класс | Когда смотреть | Осторожно |
|---|---|---|---|
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | canonical GraphRAG pipeline | Global questions, sensemaking, тематические обзоры больших корпусов | Индексация дорогая; GitHub README прямо предупреждает начинать с малого |
| [Fast GraphRAG](https://github.com/circlemind-ai/fast-graphrag) | lightweight GraphRAG | Нужен быстрый, promptable, incremental graph retrieval с меньшей стоимостью | Меньше зрелости, чем у крупных фреймворков; часть value уходит в managed service |
| [nano-graphrag](https://github.com/gusye1234/nano-graphrag) | minimal GraphRAG implementation | Обучение, прототип, кастомизация core pipeline | Не полная замена Microsoft GraphRAG; часть возможностей упрощена |
| [MiniRAG](https://github.com/HKUDS/MiniRAG) | lightweight RAG для small models | On-device/edge сценарии, small open-source language models, ограниченный storage | Ближе к исследовательскому проекту; основан на идеях LightRAG |
| [LlamaIndex PropertyGraphIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/) | framework-native graph index | Уже используется [LlamaIndex](../frameworks/llamaindex.md), нужны custom extractors/retrievers | Придется самому собрать production pipeline и storage decisions |
| [Neo4j GraphRAG for Python](https://neo4j.com/docs/neo4j-graphrag-python/current/) | graph database-first RAG package | Есть Neo4j/Aura, нужен Cypher, property graph и controlled graph storage | Привязка к Neo4j-стеку; graph schema становится частью продукта |
| [AWS GraphRAG Toolkit](https://github.com/awslabs/graphrag-toolkit) | cloud graph toolkit | AWS/Neptune/OpenSearch, BYOKG, enterprise graph-enhanced GenAI | AWS-centric архитектура; меньше community adoption, чем у популярных RAG-фреймворков |
| [R2R](https://github.com/SciPhi-AI/R2R) | production RAG API | Нужны REST API, hybrid search, multimodal ingestion, document management и knowledge graphs | Не graph-first инструмент; сложнее, если нужен только легкий library layer |
| [RAGFlow](https://github.com/infiniflow/ragflow) | RAG engine + agent platform | Нужен UI/workflow для enterprise document RAG и agent templates | Больше platform, чем библиотека; graph retrieval не главный фокус |
| [Cognee](https://github.com/topoteretes/cognee) | agent memory + knowledge graph | Долгосрочная память агентов, cross-session recall, self-hosted knowledge graph | Не прямой replacement для document QA; memory semantics важнее RAG benchmark |
| [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | research memory/RAG framework | Multi-hop retrieval, associativity, memory experiments | Исследовательский stack; production hardening придется делать отдельно |
| [RAG-Anything](https://github.com/HKUDS/RAG-Anything) | multimodal extension | PDFs, Office docs, images, tables, formulas, cross-modal knowledge graph | Это скорее расширение LightRAG-семейства, а не независимая альтернатива |

## Рекомендации

- Нужен ближайший по духу open-source GraphRAG без тяжелой платформы: [Fast GraphRAG](https://github.com/circlemind-ai/fast-graphrag) или [nano-graphrag](https://github.com/gusye1234/nano-graphrag).
- Нужен production-ready knowledge-heavy agent в существующем Python stack: [LlamaIndex](../frameworks/llamaindex.md) + PropertyGraphIndex.
- Нужен graph database как источник истины: [Neo4j GraphRAG for Python](https://neo4j.com/docs/neo4j-graphrag-python/current/) или [AWS GraphRAG Toolkit](https://github.com/awslabs/graphrag-toolkit).
- Нужна document platform с API, пользователями и ingestion lifecycle: [R2R](https://github.com/SciPhi-AI/R2R) или [RAGFlow](https://github.com/infiniflow/ragflow).
- Нужна долговременная память для агентов, а не только Q&A по документам: [Cognee](https://github.com/topoteretes/cognee) или [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG).
- Нужны мультимодальные документы: [RAG-Anything](https://github.com/HKUDS/RAG-Anything) или RAGFlow, если важен UI/workflow слой.

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

- [LightRAG GitHub](https://github.com/HKUDS/LightRAG)
- [LightRAG paper](https://arxiv.org/abs/2410.05779)
- [Microsoft GraphRAG docs](https://microsoft.github.io/graphrag/)
- [Microsoft GraphRAG repository](https://github.com/microsoft/graphrag)
- [LlamaIndex PropertyGraphIndex docs](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/)
- [Neo4j GraphRAG for Python docs](https://neo4j.com/docs/neo4j-graphrag-python/current/)
- [RAGFlow repository](https://github.com/infiniflow/ragflow)
- [R2R repository](https://github.com/SciPhi-AI/R2R)
- [Cognee repository](https://github.com/topoteretes/cognee)
- [HippoRAG repository](https://github.com/OSU-NLP-Group/HippoRAG)
- [AWS GraphRAG Toolkit](https://github.com/awslabs/graphrag-toolkit)

## Связанные заметки

- [LightRAG](lightrag.md) - canonical-страница инструмента.
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md) - общий retrieval pipeline.
- [LlamaIndex](../frameworks/llamaindex.md) - RAG-first framework для knowledge-heavy агентов.
- [Ререйкеры](../embeddings/rerankers.md) - усиление retrieval без graph layer.
- [Модели для эмбеддингов](../embeddings/OVERVIEW.md) - embedding layer для RAG.
