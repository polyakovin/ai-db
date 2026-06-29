---
title: Semantic Kernel
url: https://learn.microsoft.com/en-us/semantic-kernel/overview/
type: url
category: tools
tags: [framework, microsoft, enterprise, dotnet, python, orchestration]
added: 2026-06-29
status: new
---

# Semantic Kernel

Semantic Kernel (SK) — легковесный open-source development kit от Microsoft для построения AI-агентов и интеграции моделей в C#, Python и Java. Выступает как enterprise middleware: предоставляет plugin-архитектуру, telemetry, filters и глубокую интеграцию с Microsoft-стеком (Azure, .NET, [OpenAI](../platforms/openai.md)). С апреля 2026 года объединён с [AutoGen](autogen.md) в **Microsoft Agent Framework (MAF)**, но сохраняет идентичность как enterprise integration layer.

## Ключевые возможности

- **Plugin system** — интеграция моделей с существующим кодом и API через плагины: native (C#/Python), REST (OpenAPI), Azure.
- **Multi-language** — C# (first-class), Python, Java.
- **Orchestration** — управление AI workflows: plan generation, function calling, agent orchestration.
- **Enterprise middleware** — filters, telemetry, Azure integration, authentication policies.
- **Memory** — векторная память (Azure Cognitive Search, Qdrant, [Pinecone](../vector-dbs/pinecone.md), Redis).
- **Agent Framework** — RC (март 2025), часть MAF с апреля 2026.

## Архитектура

```
Semantic Kernel
├── Kernel (оркестратор)
├── AI Services ([OpenAI](../platforms/openai.md), Azure OpenAI, HuggingFace, etc.)
├── Plugins (native functions, REST APIs, Azure services)
├── Memory (vector stores, retrieval)
├── Filters (pre/post обработка)
├── Telemetry (OpenTelemetry, Azure Monitor)
└── Planner (генерация планов выполнения)
```

## MAF-интеграция (апрель 2026)

После объединения с [AutoGen](autogen.md):
- SK стал enterprise integration layer в MAF
- [AutoGen](autogen.md) — event-driven orchestration layer
- Единая платформа с LTS, stable APIs для .NET и Python

## Когда применять

| Сценарий | Почему Semantic Kernel |
|----------|----------------------|
| **Enterprise .NET стек** | First-class C# поддержка, Azure-интеграция |
| **Microsoft-экосистема** | Visual Studio, Azure, Copilot stack |
| **Plugin-heavy architecture** | Интеграция с существующими enterprise API |
| **Middleware requirements** | Filters, telemetry, policies из коробки |
| **Hybrid C#/Python команды** | Оба языка поддерживаются как first-class |

## Когда НЕ применять

- Быстрый Python-прототип — [CrewAI](crewai.md) или [LangGraph](langgraph.md) проще
- RAG-first агенты — [LlamaIndex](llamaindex.md) специализированнее
- Чисто Python-стека — семантика SK избыточна
- Low-code requirements — [Dify](dify.md)/Flowise

## Open Source статус

- **Semantic Kernel** — MIT license, GitHub: `microsoft/semantic-kernel` (27K+ звёзд)
- **MAF** — MIT license (после слияния)
- Интеграция с Azure AI Services — managed (платный)

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Plugin-based tools** | Функции, REST API, Azure-сервисы как инструменты агента |
| **Planning** | Автоматическая генерация планов выполнения из цели |
| **Function calling** | Модель выбирает и вызывает функции через плагины |
| **Memory** | Векторная память с Azure Cognitive Search/Pinecone/Qdrant/Redis |
| **Filters** | Pre/post-processing: logging, safety, transformation |
| **Telemetry** | OpenTelemetry, Azure Monitor, кастомные метрики |
| **Multi-agent** | Через MAF: event-driven оркестрация с AutoGen |

## Сравнение с аналогами

| Критерий | Semantic Kernel | LangChain | LlamaIndex | OpenAI Agents SDK |
|----------|---------------|-----------|------------|-------------------|
| **Языки** | C#, Python, Java | Python, JS | Python, TS | Python, Node.js |
| **Enterprise** | Microsoft-first | Model-agnostic | Model-agnostic | OpenAI-first |
| **Plugins** | Нативные + REST | Tools/Chains | Tools | Hosted tools |
| **Planning** | Встроенный Planner | LangGraph | Workflows | Agents SDK |
| **Memory** | Vector stores | Retrievers | Встроенный RAG | File Search |

## Use Cases

- **Enterprise automation**: интеграция AI-агентов с существующими .NET/Azure сервисами
- **Business process agents**: планирование и выполнение многошаговых бизнес-процессов
- **API orchestration**: агент, вызывающий REST API через плагины
- **Hybrid teams**: смешанные C#/Python команды с общей агентной платформой
- **Regulated industries**: enterprise middleware с аудитом и политиками

## Отзывы и критика

### Сильные стороны:
- Единственный production-фреймворк с first-class C# поддержкой
- Глубокая Azure-интеграция
- Plugin-архитектура для enterprise API
- MAF-интеграция для multi-agent сценариев
- Microsoft LTS и поддержка

### Слабые стороны:
- Меньше adoption в Python-only сообществе
- Сложнее для быстрого прототипа, чем [CrewAI](../frameworks/crewai.md)
- Заточен под Microsoft-стек
- Меньше community tutorials и примеров
- Слияние с [AutoGen](autogen.md) — период нестабильности API

## Связи

- [AutoGen / MAF](../frameworks/autogen.md) — объединённая платформа
- [LangGraph](../frameworks/langgraph.md) — альтернативный orchestration-фреймворк
- [Исследование фреймворков](../agent-frameworks-research.md) — Semantic Kernel в карте выбора
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — SK как middleware layer в harness
- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) — MAF для оркестрации

*Добавлено: 2026-06-29*
