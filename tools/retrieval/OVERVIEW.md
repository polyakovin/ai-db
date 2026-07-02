# Retrieval tools — overview

Раздел для RAG, GraphRAG, knowledge-graph retrieval, production RAG engines и agent memory systems. Факты по инструментам живут на отдельных страницах; overview помогает выбрать направление.

## Карта выбора

- Ближайший по духу open-source GraphRAG без тяжелой платформы: [Fast GraphRAG](fast-graphrag.md) или [nano-graphrag](nano-graphrag.md).
- Production-ready knowledge-heavy agent в существующем Python stack: [LlamaIndex](../frameworks/llamaindex.md) + [LlamaIndex PropertyGraphIndex](llamaindex-property-graph-index.md).
- Graph database как источник истины: [Neo4j GraphRAG for Python](neo4j-graphrag-python.md) или [AWS GraphRAG Toolkit](aws-graphrag-toolkit.md).
- Document platform с API, пользователями и ingestion lifecycle: [R2R](r2r.md) или [RAGFlow](ragflow.md).
- Долговременная память для агентов: [Cognee](cognee.md) или [HippoRAG](hipporag.md).
- Мультимодальные документы: [RAG-Anything](rag-anything.md) или [RAGFlow](ragflow.md), если важен UI/workflow слой.

## Baseline перед GraphRAG

Перед внедрением graph-based RAG сравните его с более дешевым baseline: dense embeddings + BM25/sparse retrieval, metadata filters, reranker, citations и eval cases для single-hop, multi-hop, summary и adversarial queries. Graph layer оправдан, если baseline стабильно ломается на вопросах о связях между сущностями, темах всего корпуса, изменениях вокруг сущности или цепочках зависимостей.

## GraphRAG и graph retrieval

- [LightRAG](lightrag.md) — graph + vector RAG для multi-hop retrieval и knowledge graph контекста
- [Microsoft GraphRAG](microsoft-graphrag.md) — graph-based RAG pipeline для local/global search и corpus sensemaking
- [Fast GraphRAG](fast-graphrag.md) — lightweight GraphRAG с incremental updates и PageRank-based exploration
- [nano-graphrag](nano-graphrag.md) — минимальная easy-to-hack GraphRAG implementation
- [MiniRAG](minirag.md) — lightweight RAG для small/open-source language models
- [LlamaIndex PropertyGraphIndex](llamaindex-property-graph-index.md) — graph index компонент внутри [LlamaIndex](../frameworks/llamaindex.md)
- [Neo4j GraphRAG for Python](neo4j-graphrag-python.md) — first-party GraphRAG package для Neo4j
- [AWS GraphRAG Toolkit](aws-graphrag-toolkit.md) — AWS-oriented graph-enhanced GenAI toolkit

## Production RAG engines

- [R2R](r2r.md) — production RAG API с hybrid search, knowledge graphs и document management
- [RAGFlow](ragflow.md) — RAG engine + agent platform для document-heavy workflows

## Agent memory и multimodal RAG

- [Cognee](cognee.md) — AI memory platform для persistent agent memory
- [HippoRAG](hipporag.md) — research memory/RAG framework с knowledge graphs и Personalized PageRank
- [RAG-Anything](rag-anything.md) — multimodal RAG framework поверх [LightRAG](lightrag.md)
