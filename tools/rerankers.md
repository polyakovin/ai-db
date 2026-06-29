---
title: Ререйкеры (Rerankers)
url: https://localaimaster.com/blog/reranking-cross-encoders-guide
type: url
category: tools
tags: [rerankers, rag, retrieval, cross-encoder, ranking]
added: 2026-06-29
status: new
---

# Ререйкеры (Rerankers)

Ререйкеры — модели второго этапа ранжирования, которые уточняют результаты поиска, переоценивая query-document пары с полным контекстом обоих. Типичный пайплайн: vector search возвращает top-100 кандидатов → reranker переоценивает и возвращает top-10 для LLM. Критический компонент production RAG-систем для повышения precision.

## Как работает reranking

```
1. Vector DB: retrieval (top-100 candidates)
2. Reranker: cross-encoder scoring (query, document)
3. Final: top-10 для LLM контекста
```

## Модели (июнь 2026)

### Managed/API

| Ререйкер | Провайдер | Особенности |
|----------|-----------|-------------|
| **Cohere Rerank 4** | Cohere (API) | 100+ языков, state-of-the-art качество, managed |
| **Voyage Rerank** | Voyage AI (API) | Интеграция с Voyage embeddings |

### Open-source / Open-weight

| Ререйкер | Тип | Особенности |
|----------|-----|-------------|
| **BGE-Reranker-v2-m3** | Cross-encoder (BAAI) | Multilingual (100+ языков), open-weight, самый популярный open-source reranker |
| **BGE-Reranker-v2-Gemma** | Cross-encoder (BAAI) | На базе Gemma, высокое качество, тяжелее |
| **Jina Reranker v2** | Cross-encoder (Jina AI) | 100+ языков, multimodal (text + image), в 6× быстрее v1, в 15× быстрее BGE-v2-m3 |
| **mxbai-rerank** | Cross-encoder (Mixedbread) | Хорошее качество, open-weight |
| **ZeroEntropy zerank** | Cross-encoder | Self-hosted альтернатива Cohere |
| **FlashRank** | Ultra-lightweight | Минимальная latency, для edge устройств |

### ColBERT
- **ColBERT** — late-interaction модель: не pure cross-encoder, а token-level interaction
- Компромисс между скоростью bi-encoder и качеством cross-encoder
- ColQwen, ColBERT-v2, PLAID

## Сравнение: bi-encoder vs cross-encoder vs ColBERT

| Тип | Скорость | Качество | Использование |
|-----|---------|----------|---------------|
| **Bi-encoder** (embeddings) | Быстрый (cosine similarity) | Базовое | Первый этап: retrieval top-k |
| **Cross-encoder** (reranker) | Медленный (полное взаимодействие) | Высокое | Второй этап: rerank top-k |
| **ColBERT** (late interaction) | Средний | Высокое | Компромисс скорость/качество |

## Выбор reranker

### По сценарию

| Сценарий | Рекомендация |
|----------|-------------|
| **Managed, высокое качество** | Cohere Rerank 4 |
| **Open-source, multilingual** | BGE-Reranker-v2-m3 |
| **Multimodal (text + image)** | Jina Reranker v2 |
| **Максимальная скорость** | Jina Reranker v2 или FlashRank |
| **Self-hosting, контроль** | BGE-Reranker-v2-m3 / zerank |
| **Domain-specific** | Fine-tune BGE-Reranker на своих данных |

### Практические правила

1. **Не rerank всё**: только top-k из vector retrieval
2. **Мониторь latency**: cross-encoder добавляет задержку
3. **Fine-tune для домена**: domain-specific данные дают значительный прирост
4. **Проверяй recall@k vs NDCG@k**: reranker улучшает NDCG, но может снизить recall
5. **Кешируй результаты**: повторяющиеся запросы не должны переоцениваться

## Производительность

| Ререйкер | Относительная скорость | Качество |
|----------|----------------------|----------|
| Jina Reranker v2 | **15× быстрее** BGE-v2-m3 | Высокое |
| BGE-Reranker-v2-m3 | Базовая | Стандарт open-source |
| BGE-Reranker-v2-Gemma | Медленнее | Очень высокое |
| Cohere Rerank 4 | API latency | SOTA |
| FlashRank | **Максимальная** | Приемлемое |

## Интеграция

### Python
```python
# BGE-Reranker
from sentence_transformers import CrossEncoder
model = CrossEncoder('BAAI/bge-reranker-v2-m3')
scores = model.predict([(query, doc) for doc in candidates])

# Cohere Rerank
import cohere
co = cohere.Client(api_key)
results = co.rerank(query=query, documents=candidates, model='rerank-english-v3.0')
```

### С фреймворками
- **LangChain**: `CohereRerank`, `BGERerank`
- **LlamaIndex**: `CohereRerank`, `BGERerank`, `JinaRerank`
- **Haystack**: `CohereRanker`, `SentenceTransformersDiversityRanker`

## Use Cases

- **RAG precision boost**: повышение точности retrieval для LLM
- **Hybrid retrieval**: dense + sparse → reranker → LLM
- **Multilingual search**: BGE/Jina для 100+ языков
- **Multimodal RAG**: Jina Reranker v2 для text + image
- **Domain-specific search**: fine-tuned reranker на отраслевых данных

## Отзывы и критика

### Сильные стороны:
- Значительное улучшение precision в RAG
- BGE-Reranker-v2-m3 — зрелый open-source стандарт
- Jina Reranker v2 — лучшая скорость в классе
- Cohere Rerank 4 — SOTA качество без self-hosting

### Слабые стороны:
- Добавляет latency (особенно медленные cross-encoders)
- Нужен отдельный сервис или модель
- Fine-tuning требует размеченных данных
- Для простых сценариев может быть избыточным

## Связи

- [[../../tools/embedding-models.md|Модели для эмбеддингов]] — первый этап retrieval
- [[../vector-dbs/pinecone.md|Pinecone]] — векторная БД для первого этапа
- [[../../patterns/architecture-design/rag-for-agents.md|RAG для агентов]] — reranker как компонент RAG
- [[../../patterns/advanced/reproducible-agent-recipes.md|Воспроизводимые рецепты]] — RAG agent с reranker
- [[../agent-observability-debugging.md|Observability и debugging]] — tracing retrieval pipeline

*Добавлено: 2026-06-29*
