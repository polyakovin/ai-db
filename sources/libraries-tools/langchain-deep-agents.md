---
title: LangChain Deep Agents
url: https://github.com/langchain-ai/deep-agents
type: url
category: sources
tags: [langchain, agents, harness, open-source]
added: 2026-06-24
status: processed
---

# LangChain Deep Agents

Open-source agent harness для долгосрочных задач и multi-agent оркестрации.

## Описание

Проект полезен как пример практической обвязки вокруг агента: управление задачами, контекстом, инструментами и координацией подзадач.

## Обзор ресурса

- **Автор:** LangChain (langchain-ai)
- **Лицензия:** MIT
- **Статус:** Активный проект (2026); часть экосистемы LangChain (134K+ GitHub stars)
- **Позиционирование:** Opinionated agent harness поверх `create_agent` в LangGraph — batteries-included: planning tool, filesystem backend, sub-agents, context management, skills
- **Доступ:** SDK (Python) + CLI (Deep Agents Code — аналог Claude Code/Cursor, model-agnostic)
- **Отличие от LangChain `create_agent`:** Deep Agents — более высокоуровневый harness с предустановленными компонентами; `create_agent` — минимальный
- **Relevance:** Ключевой open-source референс для архитектуры agent harness; модель-агностик

## Синтез

Основная выжимка перенесена в [обзор источников](../OVERVIEW.md) и связанные проектные заметки.

## Статус

Обработано: 2026-06-24

## Связи

- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — ключевой источник для концепции harness
- [[../../patterns/implementation/multi-agent-orchestration.md|Multi-agent orchestration]] — subagents и оркестрация
- [[../../patterns/implementation/agent-evaluations.md|Evaluations для агентов]] — проверка качества harness
