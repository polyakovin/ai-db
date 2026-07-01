---
title: API Clients for Agents
url: https://github.com
type: url
category: tools
tags: [api, http, rest, agents, tools, integration]
added: 2026-07-01
status: new
---

# API Clients for Agents

HTTP-клиенты для AI-агентов — инструменты для вызова внешних API, REST endpoints, GraphQL, gRPC и других веб-сервисов.

## Обзор

Интеграция с внешними сервисами — ключевая способность агентов для automation workflows. API клиенты позволяют агентам:

- **REST/GraphQL calls** — запросы к веб-сервисам
- **Authentication** — OAuth, API keys, JWT tokens
- **Request/Response handling** — headers, body, query params
- **Error handling** — retry logic, timeout, rate limiting
- **Data parsing** — JSON, XML, YAML, protobuf
- **Webhooks** — incoming/outgoing callbacks

## Ключевые инструменты

### Native HTTP Libraries

| Параметр | Значение |
|----------|----------|
| **API** | Python `requests`, `httpx`, `urllib` |
| **Доступ** | Полный HTTP/HTTPS доступ |
| **Цены** | Встроено / Open Source |
| **Open Source** | Да |

**Возможности:**
- Прямой доступ к HTTP API через стандартные библиотеки
- Полная kontrolь над запросами
- Требует явной реализации error handling, auth, retry

**Пример (Python httpx):**
```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get(
        "https://api.example.com/users",
        headers={"Authorization": "Bearer TOKEN"},
        params={"limit": 10}
    )
    data = response.json()
```

### LangChain API Tools

| Параметр | Значение |
|----------|----------|
| **URL** | https://python.langchain.com/ |
| **API** | Python SDK |
| **Модели** | Model-agnostic |
| **Цены** | Open Source |
| **Open Source** | Да (MIT) |

**Возможности:**
- `RequestsGetTool`, `RequestsPostTool`, etc. — HTTP методы
- `APIOperation` — спецификация OpenAPI/Swagger
- `OpenAPITool` — авто-генерация tools из спецификации
- Интеграция с agent loops

**Пример:**
```python
from langchain_community.tools.requests.tool import RequestsGetTool

requests_get = RequestsGetTool()
result = requests_get.run({"url": "https://api.github.com/events"})
```

### OpenAI Actions / GPTs

| Параметр | Значение |
|----------|----------|
| **URL** | https://platform.openai.com/docs/actions |
| **API** | OpenAI API |
| **Модели** | GPT-4o, o3 |
| **Цены** | Через OpenAI API |
| **Open Source** | Нет |

**Возможности:**
- Custom Actions для ChatGPT/GPTs
- OpenAPI schema-based tool definitions
- Automatic parameter extraction from natural language
- Built-in authentication (OAuth, API key)
- Response parsing и formatting

### Zapier AI Actions

| Параметр | Значение |
|----------|----------|
| **URL** | https://nla.zapier.com/ |
| **API** | REST API |
| **Модели** | NLA (Natural Language API) |
| **Цены** | Free tier → Paid |
| **Open Source** | Нет |

**Возможности:**
- 5,000+ готовых интеграций (Google, Slack, Salesforce, etc.)
- Natural language → API calls
- No-code setup
- OAuth handling
- Response formatting для LLM

**Пример:**
```python
import requests

ZAPIER_NLA_API_KEY = "..."
ZAPIER_NLA_ACTION_ID = "..."

response = requests.post(
    f"https://actions.zapier.com/api/v1/exposed/{ZAPIER_NLA_ACTION_ID}/execute/",
    headers={"X-API-Key": ZAPIER_NLA_API_KEY},
    data={"instructions": "Send email to team@example.com with subject 'Update'"}
)
```

### Apify Actors

| Параметр | Значение |
|----------|----------|
| **URL** | https://apify.com/ |
| **API** | REST API, Python/JS SDK |
| **Модели** | N/A (cloud automation platform) |
| **Цены** | Free tier ($5 credit) → Paid от $49/мес |
| **Open Source** | SDK — да, platform — нет |

**Возможности:**
- 3,000+ pre-built web automation actors
- Web scraping, data extraction, API wrappers
- Cloud execution (serverless)
- Scheduled runs
- Dataset storage и export

### Postman API Client

| Параметр | Значение |
|----------|----------|
| **URL** | https://www.postman.com/ |
| **API** | Postman API, CLI |
| **Модели** | N/A |
| **Цены** | Free tier → Paid от $12/мес |
| **Open Source** | Нет |

**Возможности:**
- API development и testing
- Collection sharing
- Environment variables
- Pre-request scripts (JavaScript)
- Test assertions
- Mock servers

## Когда использовать

| Сценарий | Рекомендуемый инструмент |
|----------|-------------------------|
| **Custom API integration** | Native httpx/requests + wrapper |
| **LangChain agent** | LangChain API Tools |
| **OpenAI GPTs** | OpenAI Actions |
| **No-code integrations** | Zapier AI Actions |
| **Web scraping APIs** | Apify Actors |
| **API development** | Postman |

## Безопасность и ограничения

- **API key exposure** — хранить в secrets manager, не в коде
- **Rate limiting** — соблюдать лимиты внешних API
- **Input validation** — санитизация user input перед вызовом API
- **Response parsing** — обработка ошибок, unexpected formats
- **Timeout** — защита от hanging requests
- **Retry logic** — exponential backoff для transient failures
- **Circuit breaker** — отключение при persistent failures

### Пример безопасного wrapper
```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

class SafeAPIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = 30.0
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential())
    async def get(self, endpoint: str, params: dict = None) -> dict:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}/{endpoint}",
                headers={"Authorization": f"Bearer {self.api_key}"},
                params=params
            )
            response.raise_for_status()
            return response.json()
```

## Интеграция с агентами

### LangChain Agent
```python
from langchain.agents import initialize_agent
from langchain_community.tools.requests.tool import RequestsGetTool
from langchain_openai import ChatOpenAI

tools = [RequestsGetTool()]
llm = ChatOpenAI(model="gpt-4o")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
agent.run("Get current weather from https://api.weather.com/current")
```

### OpenAI Functions
```python
from openai import OpenAI
import httpx

client = OpenAI()

async def call_weather_api(city: str) -> str:
    async with httpx.AsyncClient() as http_client:
        resp = await http_client.get(
            f"https://api.weather.com/current?city={city}"
        )
        return resp.json()["description"]

tools = [{
    "type": "function",
    "function": {
        "name": "call_weather_api",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]
```

## Связи

- [Web Search](web-search.md) — search APIs для research
- [Function Calling](function-calling.md) — механизм вызова API через LLM
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — интеграция API tools в harness

---

*Добавлено: 2026-07-01*
