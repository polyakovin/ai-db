# Поддержка качества контекста для AI-агентов

Качество контекста - это способность базы знаний, базы данных и retrieval-слоя давать агенту релевантные, свежие, проверяемые и разрешенные данные в форме, пригодной для решения задачи. Для агента плохой контекст опасен не меньше плохой модели: он приводит к уверенным ошибкам, неверным tool calls, утечкам и повторению устаревших решений.

Эта заметка соединяет [Context engineering](../fundamentals/context-engineering.md), [RAG для AI-агентов](rag-for-agents.md), [Автоматизацию сбора внешнего контекста](external-context-collection.md), [Data governance и compliance](data-governance-compliance.md) и [Evaluations для агентов](../implementation/agent-evaluations.md) в одну операционную рамку.

## Что считать качественным контекстом

| Измерение | Вопрос | Минимальная проверка |
|-----------|--------|----------------------|
| Relevance | Помогает ли фрагмент решить текущую задачу | retrieval evals, human spot-check |
| Correctness | Факт верен и не искажен парсером | citation backcheck, source comparison |
| Freshness | Данные не устарели для сценария | `freshness_ttl`, `last_verified_at`, stale warnings |
| Completeness | Достаточно ли данных для решения | coverage tests, missing-source cases |
| Consistency | Нет ли конфликтов между источниками | canonical owner, conflict queue |
| Granularity | Фрагмент достаточно мал для prompt, но не теряет смысл | chunk evals, section breadcrumbs |
| Retrievability | Агент может найти нужное по смыслу и точному идентификатору | hybrid search, metadata filters |
| Provenance | Понятно, откуда факт и кто за него отвечает | source id, owner, hash, citation |
| Permissions | Агент и пользователь имеют право видеть данные | access policy, row/document-level filters |
| Actionability | Контекст говорит, что делать дальше или где проверить | runbooks, examples, linked tools |

## Knowledge base vs database vs index

| Слой | Что хранит | Главный риск | Как поддерживать качество |
|------|------------|--------------|---------------------------|
| Knowledge base | Документы, решения, политики, how-to, FAQ | Дубли, устаревшие страницы, неясный owner | atomic notes, canonical pages, ревью, broken-link checks |
| Operational database | Сущности, статусы, события, транзакции | Schema drift, stale replicas, неверные join-логики | data contracts, read-only views, semantic layer, freshness metrics |
| Analytics warehouse | Агрегаты, отчеты, исторические срезы | Несовпадение с source-of-record | lineage, snapshot date, metric definitions |
| Vector/semantic index | Производное представление документов и записей | Индекс стал источником истины, stale embeddings | source hash, index version, reindex policy, retrieval evals |
| Agent memory | Предпочтения, решения, прошлые runs | Неверная или чувствительная память переживает задачу | TTL, provenance, user-visible edit/delete, cleanup |

Правило: source-of-truth остается в базе знаний или базе данных, а индекс является ускорителем доступа. Если факт изменился в источнике, но не переиндексирован, агент должен видеть stale warning или не использовать этот chunk.

## Карта подходов

| Подход | Что дает | Когда применять | Риск без контроля |
|--------|----------|-----------------|-------------------|
| Source registry | Явный список источников, owners, TTL, trust tier | Любая долгоживущая база контекста | Никто не отвечает за устаревание |
| Canonical pages | Один основной дом для факта или решения | Базы знаний, docs, policy | Дубли расходятся и retrieval путает агента |
| Data contracts | Стабильные схемы и правила изменения данных | БД, API, event streams | Агент строит действия на сломанной семантике |
| Metadata contract | Единые поля для provenance, freshness, permissions | Ingestion и RAG | Нельзя объяснить, почему факт попал в ответ |
| Curated ingestion | Человек или policy допускает источник в индекс | High-risk домены | Poisoning и legal/privacy ошибки |
| Automated validation | Линтеры, broken links, schema checks, duplicate checks | Markdown vault, docs, structured data | Ошибки обнаруживаются только в ответах агента |
| Hybrid retrieval | Dense + sparse + filters + rerank | Смешаны смысловые запросы и точные id | Агент не находит нужный файл, id или policy |
| Context packing | Отбор и порядок evidence перед моделью | Длинные документы и multi-step tasks | Context overload и конфликт инструкций |
| Retrieval evals | Проверка recall, citations, unsupported claims | Production RAG и agents over data | Улучшения индекса ломают реальные сценарии |
| Observability | Trace: запрос, retrieved chunks, answer, tool calls | Production и спорные решения | Невозможно объяснить ошибку |
| Feedback loop | Баги, missed retrieval и human corrections становятся test cases | Живая база знаний | Одни и те же ошибки повторяются |

## Архитектурный lifecycle

```text
source registry
  -> acquisition / sync
  -> parse / normalize
  -> validate / classify
  -> version / deduplicate
  -> chunk / embed / index
  -> retrieve / rerank / filter
  -> context packing
  -> answer or action
  -> trace / feedback / eval case
```

На каждом шаге должен быть артефакт, который можно проверить: source record, parsed document, validation report, version id, chunk metadata, retrieval trace, eval result.

## Минимальный metadata contract

```yaml
context_id: policy-refund-v3#section-eligibility
source_type: doc|db|api|event|memory
source_uri: docs/refund-policy.md
canonical_owner: support-ops
trust_tier: official|internal|community|user|untrusted
fetched_at: 2026-07-02T10:00:00Z
last_verified_at: 2026-07-02T10:00:00Z
freshness_ttl: 30d
content_hash: sha256:...
schema_version: policy-doc-v2
chunker_version: heading-aware-v1
index_version: support-rag-2026-07-02
permissions_scope: support:read
pii_class: none|internal|sensitive
instruction_boundary: external_data_not_instructions
citation: Refund policy / Eligibility
```

Для записей из БД добавляйте `source_table`, `primary_key`, `snapshot_at`, `query_view` и `metric_definition`, если агент использует агрегаты.

## Подходы для базы знаний

### 1. Atomic notes

Одна заметка отвечает за одну мысль: паттерн, инструмент, решение, policy или источник. Это снижает дубли и помогает retrieval находить точный фрагмент, а не большую страницу со всем подряд.

Практики:

- использовать понятные английские file names в `kebab-case`;
- держать обзорные страницы как навигацию, а не как второй источник фактов;
- делать cross-links только на существующие страницы;
- указывать related notes в конце;
- запускать broken-link validation после meaningful changes.

### 2. Canonical ownership

У каждого факта должен быть основной дом и owner. Например, факты об инструменте живут в `tools/`, а workflow только ссылается на инструмент. Это особенно важно для агентов: retrieval может вернуть несколько версий одного факта, и модель выберет убедительную, а не правильную.

Практики:

- завести canonical page для повторно используемых сущностей;
- заменять дубли ссылками на canonical page;
- хранить decision log для архитектурных выборов;
- помечать спорные или устаревшие места как review items, а не оставлять silently stale.

### 3. Freshness workflow

Не весь контекст стареет одинаково. Правила проекта могут жить месяцами, pricing и API-поведение - днями, operational status - минутами.

Практики:

- назначать TTL по типу источника;
- выводить stale warning в retrieval result;
- иметь scheduled review для policy и runbooks;
- отделять historical notes от current policy;
- при обновлении источника запускать reindex и regression eval.

### 4. Curation queue

Автоматический импорт без отбора быстро превращает базу знаний в шум. Для production-агентов полезна очередь: candidate source -> policy checks -> human/owner approval -> ingestion -> eval.

Практики:

- reject по лицензии, privacy scope и неизвестному owner;
- сохранять rejected reason;
- high-risk источники допускать только после human review;
- превращать повторные missed answers в задачи на пополнение базы.

## Подходы для баз данных

### 1. Read-only semantic views

Агенту лучше давать не raw tables, а узкие read-only views или tools с доменными именами. View скрывает нестабильные join-детали, применяет permissions и возвращает поля, которые агент может объяснить.

Практики:

- отдельные views под agent use cases;
- описания колонок на языке домена;
- row-level и tenant-level filters до попадания в модель;
- запрет прямого доступа к sensitive columns;
- examples: хороший запрос, плохой запрос, expected result.

### 2. Schema cards

Схема БД сама по себе не объясняет смысл данных. Нужна карточка: назначение таблицы, owner, freshness, ключи, допустимые join paths, known caveats.

Минимальная карточка:

```yaml
dataset: support_tickets
owner: support-ops
source_of_record: yes
freshness_sla: 5m
primary_key: ticket_id
tenant_key: workspace_id
allowed_agent_views:
  - support_ticket_summary_v1
forbidden_fields:
  - customer_raw_email
known_caveats:
  - status changes can lag external helpdesk by 5 minutes
```

### 3. Query mediation

Для важных действий агент не должен сам сочинять произвольный SQL. Лучше использовать typed tools: `find_customer_orders`, `get_policy_by_region`, `summarize_ticket_history`. Это снижает риск неправильного join, утечки и дорогого запроса.

Практики:

- tool schema вместо raw query для повторяемых workflows;
- dry-run и explain для дорогих запросов;
- лимиты строк, времени и стоимости;
- audit log с user, purpose, query/tool, result size;
- отдельные mutation tools с approval и rollback policy.

### 4. Reconciliation

Если агент использует одновременно документы, БД и индекс, нужны проверки согласованности. Например, policy в базе знаний может противоречить текущим статусам в operational DB.

Практики:

- nightly checks между source-of-record и derived indexes;
- conflict queue с owner и severity;
- metric definitions рядом с агрегатами;
- запрет использовать устаревший snapshot без явной маркировки;
- tests для известных спорных кейсов.

## Agent-facing packaging

Контекст нужно отдавать агенту как evidence, а не как неразмеченный текст.

Хороший context packet:

```yaml
task: answer_refund_question
evidence:
  - id: policy-refund-v3#eligibility
    source: official policy
    freshness: fresh
    trust: official
    why_selected: semantic match + region filter
    instruction_boundary: data_only
    excerpt: ...
  - id: order-123#status
    source: order database
    freshness: 2m
    trust: source_of_record
    why_selected: exact order_id match
open_questions:
  - customer region is missing
must_not_do:
  - issue refund without approval
```

В packet должны попадать не только chunks, но и объяснение отбора: почему эти данные релевантны, насколько они свежие, есть ли ограничения и где требуется человек.

## Evals и метрики

| Область | Метрика | Что ловит |
|---------|---------|-----------|
| Retrieval | recall@k, MRR@10, nDCG | Нужный источник не найден или ранжируется низко |
| Grounding | citation accuracy, unsupported claim rate | Ответы без evidence |
| Freshness | stale chunk usage, TTL violations | Использование устаревших данных |
| Coverage | unanswered known questions, missing source rate | Пробелы в базе знаний |
| Consistency | duplicate/conflict rate | Несколько версий одного факта |
| Security | permission bypass, sensitive chunk exposure | Доступ не тем пользователям |
| Operations | ingestion latency, reindex time, cost per query | Система качества не масштабируется |

Практичный baseline: 30-100 representative questions, 10-20 negative cases, несколько prompt-injection документов, replay старых инцидентов и отдельный набор exact-id queries.

## Operational checklist

- Есть source registry с owner, TTL, trust tier и permissions.
- У ключевых фактов есть canonical page или source-of-record.
- Для БД есть read-only views/tools, а не прямой unrestricted access.
- Каждый chunk содержит source, hash, timestamp, permissions и citation.
- Индекс можно пересобрать из источников.
- Stale context маркируется или исключается.
- Retrieval evals запускаются при изменении chunking, embedding, filters или reranker.
- Trace сохраняет query, retrieved evidence, answer и tool calls.
- Human feedback превращается в backlog, source update или eval case.
- Удаление/retention распространяется на документы, индекс, logs, memory и eval datasets.

## Антипаттерны

- Считать vector index источником истины.
- Индексировать все документы без owner, TTL и permissions.
- Смешивать user memory, project policy и external docs в одном namespace.
- Хранить большие страницы, которые retrieval возвращает целиком.
- Давать агенту raw DB доступ без semantic layer и лимитов.
- Обновлять документы без reindex и regression eval.
- Оценивать только финальный ответ, не проверяя retrieved evidence и tool path.
- Лечить плохой retrieval увеличением `top_k` без анализа precision.

## Когда достаточно простого подхода

Если агент работает с маленьким repo или ручной curated папкой, можно начать с файловой базы знаний:

1. Atomic Markdown files.
2. `OVERVIEW.md` как карта.
3. Decision log.
4. Broken-link validation.
5. Search по файлам.
6. Ручной review устаревших страниц.

Векторный индекс, ETL и сложные evals стоит добавлять, когда появляются объем, частые обновления, разные access scopes или production-риски.

## Связанные заметки

- [Context engineering](../fundamentals/context-engineering.md)
- [RAG для AI-агентов](rag-for-agents.md)
- [Автоматизация сбора внешнего контекста](external-context-collection.md)
- [Data governance и compliance](data-governance-compliance.md)
- [Персистентная память агента](../advanced/agent-memory-patterns.md)
- [Evaluations для агентов](../implementation/agent-evaluations.md)
- [Production operations](../production-operations/production-operations.md)
