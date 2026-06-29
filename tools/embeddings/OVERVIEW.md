# Эмбеддинги и ререйкинг — Overview

Раздел охватывает выбор embedding-моделей для RAG, памяти и семантического поиска, а также ререйкеры — модели второго этапа ранжирования для повышения precision retrieval.

## Модели для эмбеддингов

Актуально на 2026-06-24. Эмбеддинг-модель превращает текст, изображение или другой объект в вектор, который можно искать по близости. Для AI-агентов это базовый слой RAG, памяти, дедупликации, маршрутизации задач и семантической классификации.

### Что выбирать по умолчанию

[OpenAI](../platforms/openai.md) `text-embedding-3-small` — базовый выбор для недорогого production RAG, если стек уже на [OpenAI](../platforms/openai.md).
- **[OpenAI](../platforms/openai.md) `text-embedding-3-large`
- **Voyage `voyage-4` / `voyage-4-large`** — сильный выбор для retrieval-first систем, длинного контекста, мультиязычного поиска и доменных вариантов.
- **Google `gemini-embedding-2`** — когда нужны мультимодальные эмбеддинги: текст, изображения, видео, аудио, PDF в одном пространстве.
- **[[cohere.md|Cohere]] `embed-v4.0`** — хороший managed-вариант для смешанных text/image/PDF сценариев и enterprise-стека [[cohere.md|Cohere]].
- **BAAI `bge-m3`** — open-source вариант для self-hosted RAG, гибридного dense/sparse/multi-vector retrieval и языков, включая русский.
- **[Jina](rerankers.md) `jina-embeddings-v4`** — open/source-friendly вариант для длинного контекста, мультиязычности и мультимодального поиска.

### Сравнение моделей

| Модель | Тип | Размерность | Контекст | Сильные стороны | Когда брать |
|---|---|---:|---:|---|---|
| OpenAI `text-embedding-3-small` | API | 1536, можно уменьшать | 8192 токенов | цена/качество, простая интеграция | стандартный RAG, поиск по документам, память агента |
| OpenAI `text-embedding-3-large` | API | 3072, можно уменьшать | 8192 токенов | выше качество, гибкое сокращение размерности | точность важнее стоимости и размера индекса |
| Voyage `voyage-4-large` | API | 1024 default, 256/512/2048 | 32000 токенов | retrieval quality, длинные документы, совместимость 4-й серии | production retrieval и мультиязычный RAG |
| Voyage `voyage-code-3` | API | 1024 default, 256/512/2048 | 32000 токенов | кодовый retrieval | поиск по codebase, devtools, coding agents |
| Google `gemini-embedding-2` | API | 128-3072, рекомендуемые 768/1536/3072 | 8192 токена | мультимодальность, авто-нормализация урезанных векторов | поиск по PDF, изображениям, видео, аудио и тексту |
| Cohere `embed-v4.0` | API | 256/512/1024/1536 default | 128000 токенов | text/image/PDF, разные similarity metrics | enterprise RAG, документы с визуальной структурой |
| BAAI `bge-m3` | open weights | 1024 | 8192 токена | dense + sparse + multi-vector, 100+ языков | self-hosted, гибридный поиск, контроль данных |
| `multilingual-e5-large-instruct` | open weights | 1024 | 512 токенов | сильный multilingual baseline, instruction queries | локальный мультиязычный retrieval с короткими чанками |
| [Jina](rerankers.md) `jina-embeddings-v4` | API / models | зависит от режима | 32000 токенов | text+image, long context, 89 языков | мультимодальный поиск и длинные документы |

### Практические правила выбора

1. **Не смешивать embedding spaces** — векторы разных моделей нельзя корректно сравнивать напрямую.
2. **Размерность — это цена индекса** — большая размерность повышает требования к памяти и latency.
3. **Для RAG качество retrieval важнее «общего рейтинга»** — проверяйте на своих данных.
4. **Для русского и мультиязычия нужны отдельные evals** — не полагайтесь на English-only результаты.
5. **Агентам часто нужен hybrid retrieval** — BM25 + dense + reranker.

## Ререйкеры

Ререйкеры — модели второго этапа ранжирования, которые уточняют результаты поиска, переоценивая query-document пары с полным контекстом обоих. Типичный пайплайн: vector search возвращает top-100 кандидатов → reranker переоценивает и возвращает top-10 для LLM.

### Как работает reranking

```
1. Vector DB: retrieval (top-100 candidates)
2. Reranker: cross-encoder scoring (query, document)
3. Final: top-10 для LLM контекста
```

### Модели (июнь 2026)

Managed/API:
- **Cohere Rerank 4** — 100+ языков, SOTA качество
- **Voyage Rerank** — интеграция с Voyage embeddings

Open-source:
- **BGE-Reranker-v2-m3** — multilingual, самый популярный open-source reranker
- **Jina Reranker v2** — multimodal, в 6× быстрее v1, в 15× быстрее BGE-v2-m3
- **FlashRank** — ultra-lightweight для edge устройств

### Выбор reranker

| Сценарий | Рекомендация |
|----------|-------------|
| Managed, высокое качество | Cohere Rerank 4 |
| Open-source, multilingual | BGE-Reranker-v2-m3 |
| Multimodal (text + image) | Jina Reranker v2 |
| Self-hosting, контроль | BGE-Reranker-v2-m3 / zerank |

## Связанные темы

- [[../OVERVIEW.md|Инструменты — Обзор]]
- [[../../patterns/architecture-design/rag-for-agents.md|RAG для AI-агентов]] — retrieval как часть состояния агента
- [[../../patterns/fundamentals/context-engineering.md|Context engineering]] — memory tiers и retrieval injection
- [[../../patterns/implementation/agent-evaluations.md|Evaluations для агентов]] — качество retrieval
- [[../../patterns/advanced/reproducible-agent-recipes.md|Воспроизводимые рецепты]] — векторные базы и реранкеры
- [Cohere](cohere.md) — enterprise-платформа для эмбеддингов и ререйкинга
- [Ререйкеры](rerankers.md) — подробный обзор ререйкеров
