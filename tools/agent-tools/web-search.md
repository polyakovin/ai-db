---
title: Web Search Tools for Agents
url: https://docs.tavily.com/documentation/api-reference/endpoint/search
type: url
category: tools
tags: [search, web, agents, tools, api, retrieval]
added: 2026-07-01
updated: 2026-07-02
status: new
---

# Web Search Tools for Agents

Инструменты веб-поиска для AI-агентов дают агенту доступ к актуальной внешней информации: web results, snippets, извлечённый текст страниц, citations, фильтры по доменам и датам, а иногда - полноценный research loop. Это не один класс продуктов, а несколько слоёв, которые лучше подключать под разные задачи.

## Карта слоёв

| Слой | Что возвращает | Когда нужен |
|------|----------------|-------------|
| Hosted model tools | Ответ модели + citations + скрытый или явный search trace | Когда агент уже работает внутри managed API провайдера и важны минимальная интеграция, citations и planning |
| Agent-oriented search APIs | Ranked results, snippets, extracted content, token budgets | Когда нужен model-agnostic tool для собственного harness |
| SERP APIs | Сырые результаты поисковиков и vertical search | Когда важна близость к Google/другому SERP, локализация, shopping/news/images/maps |
| Crawlers and readers | URL/site -> Markdown/HTML/JSON/screenshot | Когда поиск уже нашёл URL, но агенту нужен чистый контент страницы или сайта |
| Browser automation | UI state, DOM, screenshots, действия в браузере | Когда страница динамическая, требует auth, JavaScript или интерактивных шагов |

## Быстрый выбор

| Сценарий | Первый выбор | Почему |
|----------|--------------|--------|
| Быстрый ответ на актуальный вопрос внутри managed agent stack | [OpenAI](../platforms/openai.md) `web_search` или [Anthropic (Claude)](../platforms/anthropic.md) `web_search` | Модель сама решает, когда искать, и возвращает ответ с источниками |
| Собственный агент, которому нужен простой web search tool | Tavily или Brave LLM Context | Возвращают LLM-friendly snippets/content, есть фильтры и контроль объёма контекста |
| Исследовательский поиск по смыслу, похожие документы, discovery | Exa | Neural/semantic search и извлечение contents/highlights/summary из результатов |
| Нужны Google SERP, verticals и локализация | Serper или SerpAPI | Дают структурированные SERP-данные, но обычно требуют отдельного extraction/summarization слоя |
| Нужно crawl/scrape/map сайта после поиска | Firecrawl | Search + scrape/crawl/map/interact/agent, hosted и self-host варианты |
| Нужно дешево превратить URL в Markdown | Jina Reader | `r.jina.ai` для URL -> LLM-friendly text, `s.jina.ai` для простого web SERP |
| Страница зависит от UI, cookies, форм, client-side rendering | [Browser Automation](browser-automation.md) | Search API не видит интерактивное состояние страницы |

## Ключевые инструменты

### Hosted model search tools

**[OpenAI](../platforms/openai.md) Web Search**

- Интеграция: Responses API tool `{"type": "web_search"}`.
- Режимы: быстрый non-reasoning lookup, agentic search с reasoning-моделью, deep research для длинных расследований.
- Сильная сторона: минимальный orchestration code, встроенные citations, provider-managed tool calls.
- Ограничение: lock-in к моделям и API провайдера; меньше контроля над raw SERP и extraction pipeline.

**[Anthropic (Claude)](../platforms/anthropic.md) Web Search**

- Интеграция: server tool `web_search_*` в Messages API.
- Модель сама решает, когда искать, может выполнять несколько поисков за один turn и завершает ответом с cited sources.
- Есть управляемость через system prompt и лимиты вроде `max_uses`.
- Новые версии web search добавляют dynamic filtering, чтобы нерелевантные результаты не забивали context window.

**[Perplexity AI](../platforms/perplexity.md) API**

- Search API: raw ranked web results с filters, region/language/domain controls и extracted snippets.
- Sonar API: готовый prose answer with citations.
- Agent API: multi-provider interface с integrated web search, tool configuration, reasoning control и token budgets.
- Хороший выбор, если продукт строится вокруг answer engine/research UX, а не только вокруг списка URL.

### Agent-oriented search APIs

**Tavily**

- Search API оптимизирован под LLM/agent workflows: `search_depth`, `max_results`, `topic`, `time_range`, `include_answer`, `include_raw_content`, domain filters, country boost.
- Extract API вытаскивает content из конкретных URL; Crawl и Map помогают обходить сайт графом.
- Подходит как дефолтный web search tool в кастомном [Agent Harness](../../patterns/architecture-design/agent-harness.md).
- Не self-hosted как search engine; SDK открытые, сам backend proprietary.

**Brave Search API**

- Имеет независимый search index и отдельный LLM Context endpoint для agents/RAG.
- LLM Context возвращает pre-extracted chunks, `sources` metadata, token budget controls, relevance threshold modes, freshness filters и Goggles для custom source ranking.
- Хороший выбор, когда важны privacy positioning, независимый индекс и контроль над grounding context.
- Есть отдельный Answers API для готовых grounded answers, но для собственного агента чаще полезнее LLM Context.

**Exa**

- Search endpoint совмещает web search и extraction contents из результатов.
- Полезен для semantic discovery: поиск похожих документов, research по смыслу, highlights, summaries, text, freshness controls.
- Хорошо ложится на исследовательские workflow, где lexical SERP даёт слишком много мусора.
- Требует отдельной политики source quality: semantic relevance не равна авторитетности источника.

**Linkup / You.com / другие answer/search APIs**

- Имеют похожий паттерн: hosted search + answer API + citations.
- Добавлять в production shortlist стоит только после проверки coverage, latency, pricing, data policy и citation behavior на своих eval-наборах.
- В базе пока не делаем отдельные canonical страницы без конкретного внедрения или benchmark.

### SERP APIs

**Serper**

- Google Search API с простым JSON output.
- Поддерживает search, images, news, maps, places, videos, shopping, scholar, patents, autocomplete.
- Сильная сторона - быстрый и дешёвый доступ к Google-like SERP.
- Слабая сторона - агенту всё равно нужен fetch/extract/rerank слой, потому что SERP snippet редко достаточен для точного ответа.

**SerpAPI**

- Более зрелый и широкий SERP provider: Google Search API и множество vertical APIs, включая images, news, maps, shopping, jobs, patents, scholar и другие движки.
- Сильная сторона - coverage и granular localization/search parameters.
- Слабая сторона - это mostly SERP scraping as a service, а не LLM-ready grounding context из коробки.

**Google Custom Search JSON API**

- Позволяет получать web/image results из Programmable Search Engine в JSON.
- По состоянию на официальную документацию: closed to new customers; существующим пользователям нужно перейти на альтернативу до 2027-01-01.
- Для новых agent projects не рассматривать как основной web search layer.

### Crawlers and readers

**Firecrawl**

- Search endpoint умеет искать и опционально scrape результаты; ответ может включать markdown/html/rawHtml/screenshots.
- Есть Scrape, Crawl, Map, Interact и Agent endpoints, а также MCP server/CLI для подключения к агентам.
- Хороший выбор, когда агенту нужно не только найти URL, но и стабильно добыть clean content из сайтов.
- Open source repo сейчас под AGPL-3.0; hosted service удобнее, self-host даёт больше контроля, но требует эксплуатации.

**Jina Reader**

- `r.jina.ai` превращает URL в LLM-friendly input.
- `s.jina.ai` даёт web search/SERP; `mcp.jina.ai` можно подключать как MCP server.
- Полезен как lightweight reader/extractor или fallback, особенно когда нужен быстрый Markdown без отдельного crawler stack.
- Для production нужно проверять rate limits, caching behavior, privacy и качество extraction на своих доменах.

## Интеграционный паттерн

1. Агент классифицирует запрос: stable knowledge, current fact, broad research, site-specific lookup, private/authenticated page.
2. Tool policy выбирает слой: hosted web tool, agent search API, SERP API, crawler/reader или browser automation.
3. Поиск выполняется с ограничением `max_results`, freshness/date filters, domain allowlist/denylist и cost budget.
4. Top URLs проходят extraction: raw content, markdown, snippets, tables, PDFs, screenshots по необходимости.
5. Контент дедуплицируется, rerank-ится и сжимается под context window.
6. Ответ строится только из сохранённого evidence set: URL, title, date/last_updated, retrieved_at, quote/snippet, confidence.
7. Logs сохраняют query, tool, parameters, sources и cost, чтобы воспроизводить agent decisions.

Минимальный контракт tool output:

```yaml
query: string
retrieved_at: ISO-8601
results:
  - title: string
    url: string
    source_type: web | news | docs | forum | pdf | code | image | video
    published_at: string | null
    last_updated_at: string | null
    snippet: string
    content: string | null
    score: number | null
    tool: string
```

## Практические критерии выбора

| Критерий | На что смотреть |
|----------|-----------------|
| Freshness | Есть ли date filters, news mode, explicit retrieved timestamp |
| Context quality | Возвращает ли tool только URL/snippet или готовый extracted content |
| Citation fidelity | Можно ли связать каждое утверждение с URL и конкретным фрагментом |
| Source control | Domain allowlist/denylist, country/language filters, custom ranking |
| Cost control | Credits per search, extraction cost, token budget, max tool calls |
| Latency | Есть ли fast mode для user-facing UX и deep mode для async research |
| Compliance | Terms of service, robots/crawling policy, data retention, ZDR/enterprise options |
| Portability | Можно ли заменить provider без переписывания agent loop |

## Guardrails

- Не давать поисковому tool доступ к пользовательским секретам и приватным документам без явного allowlist.
- Для financial, medical, legal и safety-critical ответов требовать несколько независимых authoritative sources.
- Не смешивать SERP snippet и verified content: snippet полезен для triage, но не всегда достаточен как evidence.
- Вводить hard caps: `max_tool_calls`, credits per task, timeout, max tokens per URL.
- Логировать `retrieved_at`, потому что web evidence стареет быстрее, чем заметки в базе.
- Для повторяемых задач хранить eval-наборы запросов и сравнивать tools по answer correctness, source quality, latency и cost.

## Официальные источники

- [OpenAI Web Search tool](https://platform.openai.com/docs/guides/tools-web-search)
- [Anthropic Web Search tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)
- [Perplexity Search API](https://docs.perplexity.ai/docs/search/quickstart)
- [Perplexity Agent API](https://docs.perplexity.ai/docs/agent-api/quickstart)
- [Tavily Search API](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [Tavily Extract API](https://docs.tavily.com/documentation/api-reference/endpoint/extract)
- [Brave LLM Context API](https://api-dashboard.search.brave.com/documentation/services/llm-context)
- [Exa Search API](https://exa.ai/docs/reference/search)
- [Serper Google Search API](https://serper.dev/)
- [SerpAPI Google Search API](https://serpapi.com/search-api)
- [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview)
- [Firecrawl Search API](https://docs.firecrawl.dev/api-reference/endpoint/search)
- [Firecrawl GitHub repository](https://github.com/firecrawl/firecrawl)
- [Jina Reader API](https://jina.ai/reader/)

## Связи

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) - куда подключается search tool в agent runtime.
- [RAG for Agents](../../patterns/architecture-design/rag-for-agents.md) - как web search сочетается с private retrieval.
- [Tool Use and MCP](../../patterns/fundamentals/tool-use-and-mcp.md) - общий механизм подключения tools.
- [Browser Automation](browser-automation.md) - fallback для динамических и интерактивных страниц.
- [API Clients](api-clients.md) - транспортный слой для внешних search APIs.
- [Perplexity AI](../platforms/perplexity.md) - platform-level canonical page для Perplexity.

*Последнее обновление: 2026-07-02*
