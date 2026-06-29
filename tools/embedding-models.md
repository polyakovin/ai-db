# Модели для эмбеддингов

Актуально на 2026-06-24. Эмбеддинг-модель превращает текст, изображение или другой объект в вектор, который можно искать по близости. Для AI-агентов это базовый слой RAG, памяти, дедупликации, маршрутизации задач и семантической классификации.

## Что выбирать по умолчанию

[OpenAI](platforms/openai.md) `text-embedding-3-small` — базовый выбор для недорогого production RAG, если стек уже на [OpenAI](platforms/openai.md).
- **[OpenAI](platforms/openai.md) `text-embedding-3-large`
- **Voyage `voyage-4` / `voyage-4-large`** — сильный выбор для retrieval-first систем, длинного контекста, мультиязычного поиска и доменных вариантов.
- **Google `gemini-embedding-2`** — когда нужны мультимодальные эмбеддинги: текст, изображения, видео, аудио, PDF в одном пространстве.
- **[[cohere.md|Cohere]] `embed-v4.0`** — хороший managed-вариант для смешанных text/image/PDF сценариев и enterprise-стека [[cohere.md|Cohere]].
- **BAAI `bge-m3`** — open-source вариант для self-hosted RAG, гибридного dense/sparse/multi-vector retrieval и языков, включая русский.
- **[Jina](rerankers.md) `jina-embeddings-v4`** — open/source-friendly вариант для длинного контекста, мультиязычности и мультимодального поиска.

## Сравнение моделей

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

## Практические правила выбора

### 1. Не смешивать embedding spaces

Векторы разных моделей нельзя корректно сравнивать напрямую. При смене модели нужно переиндексировать весь корпус. Это особенно важно при миграции между версиями вроде `gemini-embedding-001` и `gemini-embedding-2`, где поставщик прямо указывает несовместимость пространств.

### 2. Размерность — это цена индекса

Большая размерность повышает требования к памяти, диску, скорости индексации и latency ANN-поиска. Если модель поддерживает Matryoshka/truncation-подход, сначала тестируйте 768 или 1024 измерения, а не берите максимум автоматически.

### 3. Для RAG качество retrieval важнее “общего рейтинга”

MTEB полезен как sanity check, но production RAG нужно проверять на собственных вопросах, чанках и критериях: recall@k, nDCG@k, доля ответов с правильным источником, latency, стоимость индексации.

### 4. Для русского и мультиязычия нужны отдельные evals

Не полагайтесь на English-only результаты. Для русскоязычной базы стоит отдельно измерить:

- поиск русского запроса по русским документам;
- поиск русского запроса по английским документам;
- смешанные документы с кодом, таблицами и транслитерацией;
- имена продуктов, аббревиатуры, CLI-команды и ошибки.

### 5. Агентам часто нужен hybrid retrieval

Для рабочих баз знаний dense-поиск хорошо ловит смысл, но хуже точные имена файлов, команды, id, версии и параметры. Практичный baseline:

1. BM25 или sparse retrieval для точных совпадений.
2. Dense embedding retrieval для семантики.
3. Reranker для финального top-k.
4. Логирование “почему этот источник выбран”, чтобы улучшать чанкинг и запросы.

## Рекомендации для этого vault

Для текущей базы знаний по AI-агентам лучше начать с такого плана:

1. **Baseline:** `text-embedding-3-small` или `bge-m3`.
2. **Chunking:** 400-800 токенов, overlap 80-120 токенов, отдельная обработка таблиц.
3. **Hybrid:** добавить BM25 по заголовкам, путям файлов и точным терминам.
4. **Eval set:** 30-50 вопросов по разделам `articles`, `sources`, `patterns`, `tools`.
5. **Метрики:** recall@5, MRR@10, доля ответов с правильным файлом-источником, latency p95.
6. **Миграция:** хранить `embedding_model`, `embedding_dimension`, `chunker_version` рядом с каждым чанком.

## Минимальный eval-чеклист

- Запросы с точными именами: `Codex-on-Rails`, `BGE-M3`, `MCP`, `AGENTS.md`.
- Запросы с переформулировкой: “как агенту не выполнить инструкцию из inbox”.
- Запросы на сравнение: “чем Pangolin отличается от Plan-REPL”.
- Cross-language: русский вопрос по англоязычному названию источника.
- Негативные запросы: вопрос, на который в базе ещё нет ответа.

## Источники

- [OpenAI Embeddings docs](https://developers.openai.com/api/docs/guides/embeddings) — `text-embedding-3-small`, `text-embedding-3-large`, размерности, MTEB и max input.
- [Voyage AI Text Embeddings](https://docs.voyageai.com/docs/embeddings) — линейка `voyage-4`, `voyage-code-3`, доменные модели, размерности и `input_type`.
- [Google Gemini API Embeddings](https://ai.google.dev/gemini-api/docs/embeddings) — `gemini-embedding-2`, мультимодальность, размерности, migration notes.
- [Cohere Embed docs](https://docs.cohere.com/docs/cohere-embed) — `embed-v4.0`, multimodal input, размерности и контекст.
- [BAAI/bge-m3 model card](https://huggingface.co/BAAI/bge-m3) — multilingual, dense/sparse/multi-vector, 8192 tokens.
- [intfloat/multilingual-e5-large-instruct model card](https://huggingface.co/intfloat/multilingual-e5-large-instruct) — 94 languages, 1024-dimensional embeddings.
- [Jina Embeddings docs](https://jina.ai/embeddings/) — `jina-embeddings-v4`, 89 languages, 32K context, multimodal retrieval.

## Связанные темы

- [[../tools/OVERVIEW.md|Инструменты — Обзор]]
- [[../patterns/architecture-design/rag-for-agents.md|RAG для AI-агентов]] — retrieval как часть состояния агента
- [[../patterns/fundamentals/context-engineering.md|Context engineering]] — memory tiers и retrieval injection
- [[../patterns/implementation/agent-evaluations.md|Evaluations для агентов]] — качество retrieval
- [[../patterns/advanced/reproducible-agent-recipes.md|Воспроизводимые рецепты]] — векторные базы и реранкеры
