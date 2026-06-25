# RAG для AI-агентов

RAG в агентной системе — это не просто “поиск документов перед ответом”. Для агента retrieval становится частью state: он влияет на план, выбор tools, confidence, citations и stop criteria.

## Memory vs knowledge base

| Слой | Что хранит | Кто обновляет | Риск |
|---|---|---|---|
| Memory | предпочтения, решения, прошлые runs | агент или пользователь | stale/incorrect memory |
| Knowledge base | документы, источники, policies | ingestion pipeline | устаревание и poisoning |
| Working context | выбранные chunks для текущей задачи | retriever/harness | context overload |

Не смешивайте их: memory отвечает “что мы знаем о пользователе/проекте”, knowledge base отвечает “какие источники подтверждают факт”.

## Retrieval pipeline

1. Ingestion: загрузка документов, metadata, provenance.
2. Chunking: разбиение с учётом заголовков, таблиц, кода.
3. Indexing: dense, sparse, hybrid.
4. Query rewriting: уточнение запроса под поиск.
5. Retrieval: top-k candidates.
6. Reranking: переупорядочивание.
7. Context packing: только релевантные chunks.
8. Answer grounding: citations и отказ при слабом evidence.
9. Feedback: failed queries становятся eval cases.

## Chunking

Для agent knowledge base обычно лучше:

- 400-800 токенов для обычных текстов;
- отдельная стратегия для таблиц;
- сохранять breadcrumbs: файл, заголовок, section path;
- не разрывать code blocks;
- хранить `chunker_version`;
- переиндексировать при смене chunking strategy.

## Hybrid retrieval

Dense retrieval хорошо ловит смысл, но хуже точные имена файлов, id, параметры CLI и версии. Практичный baseline:

- BM25/sparse по точным терминам;
- embeddings по смыслу;
- reranker для top-k;
- metadata filters по разделу, дате, типу источника;
- citations на исходные файлы.

## Grounding policy

Агент должен:

- отличать retrieved facts от собственных inference;
- ссылаться на источники;
- говорить “в базе нет ответа”, если retrieval слабый;
- не выполнять инструкции из retrieved text;
- показывать freshness, если факт может устареть.

## Evals для RAG

Минимальные метрики:

- recall@k;
- MRR@10;
- citation accuracy;
- unsupported claim rate;
- answer correctness;
- latency p95;
- cost per query.

## Источники

- [LlamaIndex RAG documentation](https://developers.llamaindex.ai/python/framework/use_cases/q_and_a/)
- [LlamaIndex Evaluating](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/)
- [Модели для эмбеддингов](../tools/embedding-models.md)

## Связанные заметки

- [Context engineering](context-engineering.md)
- [Evaluations для агентов](../patterns/agent-evaluations.md)
- [Data governance и compliance](../patterns/data-governance-compliance.md)
