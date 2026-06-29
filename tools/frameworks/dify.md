---
title: Dify
url: https://dify.ai/
type: url
category: tools
tags: [low-code, platform, agents, rag, open-source, workflow]
added: 2026-06-29
status: new
---

# Dify

Dify — open-source low-code платформа для разработки LLM-приложений и AI-агентов. Предоставляет визуальный интерфейс для построения agentic workflows, RAG-пайплайнов, интеграций и observability. Ориентирована на быстрое прототипирование и production-ready развёртывание агентных систем без глубокого программирования.

## Ключевые возможности

- **Agentic workflows** — визуальное построение агентов: serial и parallel execution, branching, conditions, loops.
- **Knowledge (RAG)** — first-class поддержка retrieval: загрузка документов, индексация, поиск, citations.
- **Plugins** — расширение возможностей агентов через плагины.
- **Observability** — встроенные мониторинг, трассировка и логирование.
- Multi-model — поддержка [OpenAI](../platforms/openai.md), [Anthropic](../platforms/anthropic.md), [Gemini](../gemini.md), [Mistral](../platforms/mistral.md), open-source моделей.
- **Publish** — деплой агентов как API endpoints, веб-приложений, ботов.
- **Enterprise features** — RBAC, audit logs, versioning, environments.

## Сравнение с другими low-code платформами

| Критерий | Dify | Flowise | LangFlow |
|----------|------|---------|----------|
| **Модель** | Agentic workflows + Knowledge | Визуальный builder | Визуальный graph builder |
| **RAG** | First-class | Средний | Средний |
| **Логика** | if/else, branching, for | Ограниченная | Средняя |
| **Плагины** | Да | Меньше | Через LangChain |
| **Production** | RBAC, audit, versioning | Нужно достраивать | Нужно достраивать |

## Когда применять

| Сценарий | Почему Dify |
|----------|-------------|
| **Быстрый прототип** | Визуальный интерфейс, drag-and-drop, минимум кода |
| **Internal tools** | Быстрое создание инструментов для команды |
| **Business automations** | Визуальные workflow для бизнес-процессов |
| **Knowledge bots** | RAG-first: быстрый бот по документации |
| **Non-engineering teams** | Доступно для построения агентов без программирования |

## Когда НЕ применять

- Сложные production агенты — limited low-code abstraction
- Тонкий контроль над состоянием — [LangGraph](../frameworks/langgraph.md)
- Coding-first workflow — [Claude Code](../platforms/anthropic.md)/Codex CLI
- Нужна полная гибкость кода — пишите на Python + LangChain

## Open Source статус

- **Dify** — open source (Apache 2.0 license), GitHub: `langgenius/dify`
- **Dify Cloud** — managed хостинг (платный)
- **Enterprise** — self-hosted с дополнительными фичами

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Visual workflow builder** | Создание agentic workflows через UI: serial, parallel, branching, conditions |
| **Knowledge/RAG** | Загрузка документов, индексация, retrieval, citations |
| **Tools** | API calls, webhooks, code execution, плагины |
| **Memory** | Conversation memory, persistent context |
| **HITL** | Approvals, корректировки в workflow |
| **Multi-agent** | Параллельное выполнение, координация через workflow |

## Use Cases

- **Customer support bots**: быстрое создание RAG-бота по базе знаний
- **Internal tools**: автоматизация рутинных операций команды
- **Content generation pipelines**: создание, рецензирование, публикация
- **Prototyping**: быстрая проверка идей до полноценной разработки
- **Educational agents**: создание обучающих ботов без программирования

## Отзывы и критика

### Сильные стороны:
- Быстрый старт — визуальный интерфейс, минимум кода
- Комплексная логика: if/else, branching, for — больше, чем у конкурентов
- First-class RAG: загрузка, индексация, поиск
- Open source с возможностью self-host
- Enterprise features (RBAC, audit, versioning)

### Слабые стороны:
- Low-code абстракция ограничивает сложные сценарии
- Production governance нужно проверять отдельно
- Меньше контроля, чем в коде
- Vendor lock-in (даже open source — сложно мигрировать с визуального workflow на код)
- Не для масштабных multi-agent production систем

## Связи

- [[../agent-frameworks-research.md|Исследование фреймворков]] — Dify в карте выбора (low-code слой)
- [[../frameworks/langgraph.md|LangGraph]] — альтернатива для сложной оркестрации в коде
- [[../frameworks/crewai.md|CrewAI]] — кодовая альтернатива для multi-agent
- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — Dify как визуальная реализация harness
- [[../../patterns/implementation/working-with-coding-agents.md|Работа с код-агентами]] — отличие низкокодового подхода

*Добавлено: 2026-06-29*
