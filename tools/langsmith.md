---
title: LangSmith
url: https://smith.langchain.com/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# LangSmith

Платформа для observability, tracing, evaluation и тестирования LLM-приложений от создателей [LangChain](frameworks/langchain.md). Работает с любым LLM-фреймворком.

## Ключевые возможности

- **Tracing** — end-to-end трассировка цепочек вызовов (chain, retriever, tool, LLM)
- **Evaluation** — автоматизированное тестирование: regression evals, pairwise comparison, custom graders
- **Monitoring** — real-time метрики: latency, cost, token usage, error rates
- **Prompt Management** — версионирование и A/B-тестирование промптов
- **Datasets** — создание и управление eval-датасетами
- **Feedback** — сбор пользовательских оценок (thumbs up/down, custom metrics)
- **Playground** — интерактивное тестирование цепочек и агентов
- **Hub** — реестр промптов и сниппетов

## Модели / Продукты

- LangSmith Platform (SaaS + self-hosted Enterprise)
- SDK: Python, TypeScript
- Интеграция одной строкой: `LANGCHAIN_TRACING_V2=true`

## Цены и доступ

- **Open Source:** нет (proprietary SaaS)
- **Developer:** бесплатно (5K traces/мес, 14 дней retention, 1 seat)
- **Plus:** $39/мес/seat (10K traces, 400 дней retention, 3 workspaces)
- **Enterprise:** custom pricing (self-hosting, SSO, compliance)

## Агентные возможности

- Tracing agentic workflows с вложенными вызовами
- Evaluation агентов: tool selection accuracy, task completion rate
- Отладка agentic loop: визуализация plan → action → observation
- Cost tracking по под-агентам и tool calls

## Open Source статус

**Proprietary.** Ядро [[frameworks/langchain.md|LangChain]] — open source (MIT), но LangSmith — закрытая платформа.

## Use Cases

- Отладка production-агентов: почему агент выбрал не тот tool?
- Regression testing: не сломал ли новый промпт старые кейсы?
- Cost monitoring: какой под-агент тратит больше всего токенов?
- Prompt engineering: A/B-тестирование через datasets
- Compliance: полный trace для аудита решений агента

## Отзывы и критика

- Плюсы: глубокая интеграция с [[frameworks/langchain.md|LangChain]], rich tracing, зрелые evals
- Минусы: платный на масштабе, vendor lock-in для [[frameworks/langchain.md|LangChain]]-экосистемы

## Связи

- [LangChain](frameworks/langchain.md) — основной фреймворк
- [LangGraph](frameworks/langgraph.md) — оркестрация
- [Evaluations для агентов](../patterns/implementation/agent-evaluations.md)
- [Observability и debugging](agent-observability-debugging.md)

*Добавлено: 2026-06-29*
