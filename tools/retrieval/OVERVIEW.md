# Retrieval tools — overview

Раздел для RAG, GraphRAG, knowledge-graph retrieval, production RAG engines и agent memory systems. Факты по инструментам живут на отдельных страницах; сравнительные заметки только помогают выбрать направление.

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

## Сравнения

- [Аналоги LightRAG](lightrag-alternatives.md) — карта выбора по классам инструментов
