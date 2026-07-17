---
title: Langflow
url: https://docs.langflow.org/
type: url
category: tools
tags: [framework, low-code, visual-builder, agents, python, mcp, open-source]
added: 2026-07-17
status: new
---

# Langflow

Langflow — open-source Python-фреймворк с визуальным редактором для AI-приложений, agents и workflows. Он позволяет собирать flow из компонентов, тестировать его в playground, расширять Python-кодом и публиковать как API или MCP tools без привязки к одному LLM provider или vector store.

## Ключевые возможности

- **Visual flow builder** — graph editor для моделей, prompts, agents, tools, retrieval и data stores.
- **Agent component** — tool-calling agent; другие components, flows, agents и MCP servers можно подключать как tools.
- **Multi-agent composition** — один agent можно использовать как tool другого в пределах flow.
- **MCP client и server** — подключение внешних MCP servers и публикация flows как tools собственного MCP server.
- **Custom components** — расширение стандартной библиотеки Python-компонентами.
- **Playground** — интерактивное тестирование и пошаговая отладка flow.
- **Serving** — запуск flow через API, container deployment и экспорт конфигурации.
- **Model и storage integrations** — выбор LLM, embedding provider и vector store на уровне компонентов.

## Когда применять

| Сценарий | Почему Langflow |
|---|---|
| Быстрый прототип | Flow собирается визуально и сразу проверяется в playground |
| Совместная работа с non-engineers | Граф показывает data flow и tool connections без чтения всего кода |
| Internal AI tools | Flow можно опубликовать как API или MCP tool |
| RAG proof of concept | Готовые components связывают loaders, embeddings, stores и agent |
| Переход от low-code к Python | Custom components позволяют точечно заменить визуальный блок кодом |

## Когда не применять

- Нужен низкоуровневый durable runtime с явным checkpointing и replay — [LangGraph](langgraph.md) специализированнее.
- Workflow должен проходить обычный code review, статический анализ и unit tests целиком как код — визуальное представление добавит отдельный artifact lifecycle.
- Требуется строгая application-level multi-tenant isolation — её нужно проектировать на уровне инфраструктуры и deployment, а не считать свойством flow builder.
- Задача решается коротким типизированным Python agent loop — [Pydantic AI](pydantic-ai.md) может быть проще.

## Агентные возможности

| Возможность | Реализация |
|---|---|
| Tool calling | Components и flows подключаются к Agent component как tools |
| Multi-agent | Agent-as-tool композиция |
| MCP | Client для внешних servers и server для публикации flows |
| RAG | Loaders, embeddings, vector stores и retrieval components |
| Testing | Playground и пошаговый просмотр выполнения |
| Deployment | API, containers и отдельный runtime deployment |
| Extensibility | Python custom components |

## Open Source статус и безопасность

- Langflow распространяется по лицензии MIT; основной репозиторий — `langflow-ai/langflow`.
- Доступны Python package, container deployment и desktop distribution.
- При shared или public deployment нужно отключить automatic login, задать собственный secret key, включить authentication и поставить Langflow за защищённым reverse proxy.
- Credentials провайдеров и права MCP/API endpoints требуют отдельного управления; визуальный builder не устраняет эти риски.

## Сильные стороны и ограничения

**Сильные стороны:** быстрый визуальный feedback loop, Python extensibility, широкий набор компонентов, API и двусторонняя MCP-интеграция.

**Ограничения:** сложный flow труднее diff/review/test, чем code-first workflow; production governance и tenant isolation нужно достраивать; перенос логики в другой runtime может потребовать ручной реализации.

## Связи

- [Официальная документация Langflow](../../sources/libraries-tools/langflow-docs.md) — provenance для этой страницы
- [Исследование фреймворков](../agent-frameworks-research.md) — Langflow в low-code карте
- [Dify](dify.md) — альтернативная low-code платформа
- [Flowise](flowise.md) — альтернативный visual builder
- [LangGraph](langgraph.md) — code-first runtime для stateful orchestration
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — MCP client/server и agent tools

*Добавлено: 2026-07-17*
