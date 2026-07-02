# Автоматизация сбора внешнего контекста

Автоматизация сбора внешнего контекста — это слой между внешними системами и [Context engineering](../fundamentals/context-engineering.md). Его задача не в том, чтобы "дать агенту интернет", а в том, чтобы регулярно и безопасно превращать внешние источники в проверяемые evidence units: с provenance, свежестью, правами доступа и понятной границей доверия.

## Проблема

Ручной сбор контекста не масштабируется: пользователь копирует ссылки, агент заново ищет одно и то же, источники устаревают, а факты из публичного web, SaaS, файлов, тикетов и баз данных смешиваются в одном prompt. Для agentic-системы это быстро создаёт четыре риска:

- stale context — агент опирается на старые данные;
- context overload — в модель попадает слишком много нерелевантного текста;
- source poisoning — внешний документ содержит инструкции или вредный контент;
- privacy leak — приватные данные уходят в неподходящий tool, индекс или лог.

## Решение

Выделить отдельный context collection pipeline:

1. Вести registry источников: owner, URL/API, scope, trust tier, TTL, разрешённые действия.
2. Собирать данные через самый узкий безопасный канал: API/connector перед crawler, crawler перед browser agent.
3. Парсить и нормализовать контент в единый формат `Document`/`EvidenceUnit`.
4. Добавлять metadata: источник, дата получения, hash, parser version, permissions scope, freshness.
5. Дедуплицировать и версионировать изменения.
6. Индексировать только пригодные chunks для [RAG для AI-агентов](rag-for-agents.md).
7. Передавать в модель только выбранные chunks как данные, а не как инструкции.
8. Проверять pipeline evals: recall, citation accuracy, freshness, leakage, cost.

```text
source registry
  -> acquisition job
  -> parser / extractor
  -> policy + metadata
  -> dedup / version store
  -> chunking + index
  -> retrieval
  -> context packing
  -> answer / action with citations
```

## Карта возможностей

| Возможность | Что автоматизирует | Когда выбирать | Главный риск |
|-------------|--------------------|----------------|--------------|
| Hosted web search | Поиск свежих публичных фактов, новостей, ссылок, citations | Разовые research-задачи и discovery | Неполное покрытие, нестабильные результаты |
| Targeted crawl/scrape | Обход сайта, sitemap, docs, HTML/PDF, clean markdown | Регулярная индексация внешней документации | robots/TOS, rate limits, nondeterminism |
| SaaS/workspace connectors | Google Drive, Slack, Notion, GitHub, CRM, tickets | Корпоративный knowledge context | OAuth scopes, PII, смешение tenants |
| MCP servers | Единый tool-интерфейс к внешним системам | Когда один connector нужен разным agent clients | prompt injection, tool poisoning, доверие к серверу |
| Document loaders | Приведение разных источников к формату `Document` | RAG-pipeline с разнородными источниками | Разный уровень качества community loaders |
| ETL/ELT connectors | Инкрементальная репликация из API, DB, warehouse | Аналитический или операционный контекст | Утечка raw data, неверный sync mode |
| Webhooks/events | Push-сбор новых тикетов, PR, инцидентов, сообщений | Низкая задержка и freshness | Дубли, ordering, replay attacks |
| Document parsing/OCR | PDF, DOCX, slides, images, tables, scanned docs | Контекст из файлов и legacy-документов | Ошибки layout/table extraction |
| Browser/computer agents | UI-only источники без API | Last resort для закрытых веб-интерфейсов | Хрупкость, side effects, prompt injection на странице |
| Human-curated source inbox | Отбор и подтверждение источников человеком | Высокая цена ошибки или спорные источники | Медленнее, требует ownership |

## Уровни автоматизации

| Уровень | Механика | Пример результата |
|---------|----------|-------------------|
| On-demand | Агент ищет/читает источник только под текущую задачу | Короткий report с цитатами |
| Scheduled pull | Cron/queue периодически обновляет sources | Актуальный индекс внешней документации |
| Event-driven push | Webhook запускает ingestion при изменении | Новый тикет или PR сразу попадает в retrieval |
| Continuous monitoring | Pipeline отслеживает diff, freshness и alerting | Сигнал, что policy изменилась и evals надо обновить |
| Agentic acquisition | Агент сам планирует поиск, выбирает источники и просит approvals | Deep research с воспроизводимым source log |

Практичный baseline: discovery делать on-demand через search, стабильные источники переводить в scheduled pull, а operational events принимать через webhooks.

## Metadata contract

Каждая единица контекста должна иметь минимальный контракт:

```yaml
source_id: vendor-docs
source_type: web|api|file|db|event|browser
origin: https://example.com/docs/page
owner: team-or-person
fetched_at: 2026-07-02T10:00:00Z
content_hash: sha256:...
parser_version: html-v3
trust_tier: official|partner|community|user|untrusted
permissions_scope: read:docs
freshness_ttl: 7d
pii_class: none|internal|sensitive
license_policy: allowed|restricted|unknown
instruction_boundary: external_data_not_instructions
citation: page title / section / line
```

Без этого [Agent Harness](agent-harness.md) не сможет объяснить, почему chunk попал в контекст, когда он устарел и кому разрешено его видеть.

## Политика выбора источников

1. Official API или managed connector предпочтительнее scraping.
2. Read-only token предпочтительнее full-access OAuth.
3. Incremental sync предпочтительнее полной переиндексации.
4. Public web search годится для discovery, но повторяемые workflows требуют сохранённого source log.
5. Browser agent — fallback, если нет API, export или crawler-friendly endpoint.
6. External content всегда маркируется как data, а инструкции внутри него игнорируются.
7. Источник с неизвестной лицензией или privacy scope не попадает в long-term index.
8. Высокорисковые источники проходят human review до попадания в production retrieval.

## Псевдокод

```python
for source in source_registry.due(now):
    raw_items = acquire(source)
    for raw in raw_items:
        parsed = parse(raw, parser=source.parser)
        evidence = normalize(parsed, metadata={
            "source_id": source.id,
            "origin": raw.origin,
            "fetched_at": now,
            "trust_tier": source.trust_tier,
            "permissions_scope": source.scope,
        })
        if policy.rejects(evidence):
            audit.log("rejected", evidence.metadata)
            continue
        if store.has_same_hash(evidence):
            continue
        store.upsert_version(evidence)
        chunks = chunk(evidence)
        retrieval_index.upsert(chunks)
        eval_queue.add(source.id, evidence.version)
```

## Evals

Минимальный набор проверок:

- source coverage: нужные документы реально попали в индекс;
- freshness: просроченные chunks не используются без warning;
- citation accuracy: ссылка ведёт к исходному evidence;
- duplicate rate: crawler не раздувает индекс одинаковыми страницами;
- unsupported claim rate: модель не делает выводы без evidence;
- prompt injection resistance: инструкции из внешнего текста не выполняются;
- privacy leakage: приватные chunks не доступны не тем пользователям;
- ingestion cost/latency: обновление укладывается в budget.

## Когда не применять

- Источник нельзя легально или договорно индексировать.
- Данные слишком чувствительные для выбранного хранилища или модели.
- Нет owner, который отвечает за freshness и access policy.
- Контекст нужен один раз и дешевле сделать ручной verified lookup.
- Ошибка retrieval приведёт к действию с внешним side effect без approval.

## Источники и provenance

- [Model Context Protocol docs](../../sources/libraries-tools/model-context-protocol-docs.md)
- [OpenAI Tools docs](../../sources/libraries-tools/openai-tools-docs.md)
- [LlamaIndex Data Connectors and Ingestion Pipeline](../../sources/libraries-tools/llamaindex-data-connectors.md)
- [LangChain Document Loaders](../../sources/libraries-tools/langchain-document-loaders.md)
- [Firecrawl Crawl docs](../../sources/libraries-tools/firecrawl-crawl-docs.md)
- [Airbyte Connectors docs](../../sources/libraries-tools/airbyte-connectors-docs.md)
- [Unstructured docs](../../sources/libraries-tools/unstructured-docs.md)

## Связанные заметки

- [Context engineering](../fundamentals/context-engineering.md)
- [RAG для AI-агентов](rag-for-agents.md)
- [Tool use, function calling и MCP](../fundamentals/tool-use-and-mcp.md)
- [Безопасность агентных систем](agent-security.md)
- [Data governance и compliance](data-governance-compliance.md)
- [Evaluations для агентов](../implementation/agent-evaluations.md)
- [Production operations](../production-operations/production-operations.md)
- [LlamaIndex](../../tools/frameworks/llamaindex.md) — data connectors и ingestion как реализация pipeline
- [LangChain](../../tools/frameworks/langchain.md) — document loaders и интеграции
- [OpenAI](../../tools/platforms/openai.md) — hosted web/file search и MCP tools
