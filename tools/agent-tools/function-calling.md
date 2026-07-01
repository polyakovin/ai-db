---
title: Function Calling for Agents
url: https://platform.openai.com/docs/guides/function-calling
type: url
category: tools
tags: [function-calling, tool-calling, agents, llm, api]
added: 2026-07-01
status: new
---

# Function Calling for Agents

Механизм вызова функций через LLM — способ позволить языковой модели выбирать и вызывать внешние инструменты/API на основе natural language запросов.

## Обзор

Function calling (tool calling) — фундаментальный механизм для AI-агентов. Он позволяет LLM:

- **Понимать намерения** — извлекать параметры из natural language
- **Выбирать инструменты** — определять, какую функцию вызвать
- **Форматировать вызовы** — генерировать structured arguments
- **Интерпретировать результаты** — использовать return values для ответов

## Основные провайдеры

### OpenAI Function Calling

| Параметр | Значение |
|----------|----------|
| **URL** | https://platform.openai.com/docs/guides/function-calling |
| **API** | Chat Completions API |
| **Модели** | GPT-3.5-Turbo, GPT-4o, o1, o3 |
| **Цены** | Standard API pricing |
| **Open Source** | Нет |

**Возможности:**
- JSON Schema для описания функций
- Parallel function calls (multiple tools за один вызов)
- Strict mode (валидация аргументов)
- Function results в контексте ответа
- Vision + function calling (GPT-4o)

**Пример:**
```python
from openai import OpenAI

client = OpenAI()

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name, e.g. 'London'"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"]
                }
            },
            "required": ["location"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in London?"}],
    tools=tools
)

# response.choices[0].message.tool_calls
# → [{"name": "get_weather", "arguments": {"location": "London"}}]
```

### Anthropic Tool Use

| Параметр | Значение |
|----------|----------|
| **URL** | https://docs.anthropic.com/claude/docs/tool-use |
| **API** | Messages API |
| **Модели** | Claude 3+ (Haiku, Sonnet, Opus) |
| **Цены** | Standard API pricing |
| **Open Source** | Нет |

**Возможности:**
- XML-based tool format
- Multi-turn tool conversations
- Parallel tool calls
- Custom tool schemas
- Image + tool calling

**Пример:**
```python
from anthropic import Anthropic

client = Anthropic()

tools = [{
    "name": "get_weather",
    "description": "Get current weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
    }
}]

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather in London?"}],
    tools=tools
)

# response.content → [{"type": "tool_use", "name": "get_weather", ...}]
```

### Google Gemini Function Calling

| Параметр | Значение |
|----------|----------|
| **URL** | https://ai.google.dev/docs/function_calling |
| **API** | Gemini API |
| **Модели** | Gemini 1.5 Pro/Flash, Gemini 2.0 |
| **Цены** | Free tier → Paid |
| **Open Source** | Нет |

**Возможности:**
- JSON Schema function definitions
- Multi-modal function calling (text + images)
- Function response integration
- Streaming function calls

### Ollama / Local Models

| Параметр | Значение |
|----------|----------|
| **URL** | https://ollama.com/ |
| **API** | Ollama API |
| **Модели** | Llama 3, Mistral, Qwen, etc. |
| **Цены** | Free (self-hosted) |
| **Open Source** | Да |

**Возможности:**
- Local model execution
- Custom function calling format
- No API costs
- Full data privacy

## Паттерны использования

### Single Tool Call
```
User: "What's the weather in Tokyo?"
LLM → tool_call: get_weather(location="Tokyo")
Tool → {"temp": 22, "condition": "sunny"}
LLM → "It's 22°C and sunny in Tokyo!"
```

### Parallel Tool Calls
```
User: "Compare weather in Tokyo and Osaka"
LLM → [
  tool_call: get_weather(location="Tokyo"),
  tool_call: get_weather(location="Osaka")
]
Tools → [{"temp": 22}, {"temp": 19}]
LLM → "Tokyo: 22°C, Osaka: 19°C. Tokyo is warmer."
```

### Multi-Turn Tool Conversation
```
User: "Book a flight to Paris"
LLM → tool_call: search_flights(destination="Paris")
Tool → [{"flight": "AF123", "price": 450}, ...]
LLM → "Found flights. Which one?"
User: "The cheapest one"
LLM → tool_call: book_flight(flight_id="AF123")
```

## Безопасность и ограничения

- **Tool injection** — валидация function names и arguments
- **Parameter sanitization** — защита от SQL injection, command injection
- **Rate limiting** — лимиты на вызовы инструментов
- **Timeout** — защита от hanging tool calls
- **Authorization** — проверка прав на вызов инструментов
- **Audit logging** — логирование всех tool calls

### Пример validation wrapper
```python
from pydantic import BaseModel, validator

class WeatherToolArgs(BaseModel):
    location: str
    unit: str = "celsius"
    
    @validator("location")
    def validate_location(cls, v):
        if len(v) > 100:
            raise ValueError("Location too long")
        if not v.replace(" ", "").isalnum():
            raise ValueError("Invalid characters")
        return v

def safe_call_weather(args: dict) -> dict:
    validated = WeatherToolArgs(**args)
    return call_weather_api(validated.location, validated.unit)
```

## Интеграция с фреймворками

### LangChain
```python
from langchain.agents import tool

@tool
def get_weather(location: str, unit: str = "celsius") -> str:
    """Get current weather for a location"""
    return call_weather_api(location, unit)

tools = [get_weather]
```

### LlamaIndex
```python
from llama_index.core.tools import FunctionTool

def get_weather(location: str, unit: str = "celsius") -> str:
    return call_weather_api(location, unit)

tool = FunctionTool.from_defaults(
    fn=get_weather,
    name="get_weather",
    description="Get current weather for a location"
)
```

## Связи

- [API Clients](api-clients.md) — HTTP-клиенты для вызова API
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — интеграция function calling в harness
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — tool calling для coding tasks

---

*Добавлено: 2026-07-01*
