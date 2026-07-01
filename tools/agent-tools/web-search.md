---
title: Web Search Tools for Agents
url: https://github.com/mendableai
type: url
category: tools
tags: [search, web, agents, tools, api]
added: 2026-07-01
status: new
---

# Web Search Tools for Agents

Инструменты веб-поиска для AI-агентов — специализированные API и сервисы для поиска информации в интернете, извлечения контента и исследования тем.

## Обзор

Веб-поиск — критически важный инструмент для агентов, работающих с актуальной информацией. В отличие от обычных поисковых API, агентные инструменты оптимизированы для:

- **Query reformulation** — автоматическое уточнение запросов
- **Result summarization** — сжатие найденного в контекст для LLM
- **Source attribution** — цитирование источников
- **Multi-step research** — последовательные поисковые запросы

## Ключевые сервисы

### Tavily AI

| Параметр | Значение |
|----------|----------|
| **URL** | https://tavily.com/ |
| **API** | REST API, Python/JS SDK |
| **Модели** | Собственный search-движок |
| **Цены** | Free tier (1K запросов/мес) → Paid от $29/мес |
| **Open Source** | SDK — да, движок — нет |

**Возможности:**
- Search API, оптимизированный для LLM-агентов
- Автоматическая фильтрация нерелевантного контента
- Извлечение основного текста страниц (content extraction)
- Поддержка query parameters: depth, topics, domains
- Интеграция с LangChain, LlamaIndex, AutoGen

**Пример использования (Python):**
```python
from tavily import TavilyClient

tavily = TavilyClient(api_key="...")
response = tavily.search(query="best Python frameworks for agents")
# response['results'] → [{title, content, url, score}, ...]
```

### Exa AI

| Параметр | Значение |
|----------|----------|
| **URL** | https://exa.ai/ |
| **API** | REST API, Python SDK |
| **Модели** | Neural search engine |
| **Цены** | Free tier (1K запросов) → Paid от $99/мес |
| **Open Source** | SDK — да, движок — нет |

**Возможности:**
- Semantic search по веб-контенту
- Find similar pages (похожие документы)
- Content extraction с разметкой
- Авторефераты найденных страниц
- Specialized для research workflows

### Serper / SerpAPI

| Параметр | Значение |
|----------|----------|
| **URL** | https://serper.dev/ | https://serpapi.com/ |
| **API** | REST API, SDK для всех языков |
| **Модели** | Google Search API wrapper |
| **Цены** | Free tier (100-1K запросов) → Paid от $50/мес |
| **Open Source** | Нет |

**Возможности:**
- Прямой доступ к Google Search results
- Поддержка image, video, news, shopping search
- Location targeting, language settings
- Structured JSON responses
- High rate limits для production

### Firecrawl

| Параметр | Значение |
|----------|----------|
| **URL** | https://www.firecrawl.dev/ |
| **API** | REST API, Python/JS SDK |
| **Модели** | Web crawler + LLM extraction |
| **Цены** | Free tier (500 кредитов) → Paid от $16/мес |
| **Open Source** | Да (MIT) |

**Возможности:**
- Crawling целых сайтов с настройкой глубины
- LLM-based content extraction
- Map mode (обнаружение всех URL на домене)
- Markdown output для LLM-friendly формата
- Self-hosted опция

### Jina Reader

| Параметр | Значение |
|----------|----------|
| **URL** | https://jina.ai/reader/ |
| **API** | REST API (`r.jina.ai/http://...`) |
| **Модели** | LLM-powered reader |
| **Цены** | Free tier (1M токенов/мес) → Paid |
| **Open Source** | Частично |

**Возможности:**
- URL → clean markdown (text + images + links)
- Bypass paywalls и anti-bot защиту
- Screenshot capture
- Multi-language support
- Простой API: `GET https://r.jina.ai/<URL>`

## Когда использовать

| Сценарий | Рекомендуемый инструмент |
|----------|-------------------------|
| **Agent research workflow** | Tavily (оптимизирован для агентов) |
| **Semantic search по контенту** | Exa (neural search) |
| **Google Search results** | Serper/SerpAPI (прямой доступ) |
| **Full site crawling** | Firecrawl (crawler + extraction) |
| **Simple URL → text** | Jina Reader (бесплатно, быстро) |
| **Self-hosted requirement** | Firecrawl (open source) |

## Интеграция с фреймворками

### LangChain
```python
from langchain_community.tools import TavilySearchResults
search = TavilySearchResults(k=5)
```

### LlamaIndex
```python
from llama_index.tools.tavily_research import TavilyToolSpec
```

### AutoGen
```python
from autogen.agentchat.contrib.capabilities import WebSearchTool
```

## Безопасность и ограничения

- **Rate limiting** — все сервисы лимитируют запросы
- **Content filtering** — могут пропускать нежелательный контент
- **API key exposure** — не хранить ключи в коде агента
- **Citation accuracy** — проверять источники для критичных данных
- **Cost control** — мониторить usage для paid tiers

## Связи

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — интеграция search tools в harness
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — research workflow для код-задач
- [Browser Automation](browser-automation.md) — альтернатива для dynamic content
- [Perplexity AI](../platforms/perplexity.md) — consumer-grade search agent

---

*Добавлено: 2026-07-01*
