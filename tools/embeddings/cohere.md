---
title: Cohere
url: https://cohere.com/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Cohere

Enterprise-платформа для эмбеддингов, ререйкинга и RAG. Известна моделями Command R/R+, Embed, Rerank.

## Ключевые возможности

- **Embed** — embedding-модели для semantic search (multilingual, сжатые)
- **Rerank** — второй этап ранжирования результатов retrieval (точность > плотность)
- **Command R/R+** — генеративные LLM с длинным контекстом (128K), оптимизированы для RAG и tool use
- **North** — корпоративная AI-платформа: поиск по документам, чат, агенты
- **Compass** — search & retrieval engine для enterprise-данных
- **Tool use** — function calling с несколькими шагами

## Модели / Продукты

- Command R+ (флагман, 128K контекст, tool use)
- Command R (базовая, RAG-оптимизированная)
- Embed v3 (multilingual embeddings)
- Rerank v3 (cross-encoder ререйкер)
- North (enterprise workspace)

## Цены и доступ

- **Open Source:** модели Command R/R+ — open weights (CC-BY-NC)
- **API:** pay-as-you-go, эмбеддинги дешевле многих конкурентов
- **Enterprise:** custom pricing через North

## Агентные возможности

- Tool use (function calling) с многошаговыми цепочками
- RAG с ререйкингом для точного retrieval
- North-агенты для enterprise search и автоматизации
- Меньше фокус на автономные multi-agent системы по сравнению с [LangGraph](../frameworks/langgraph.md)/AutoGen

## Open Source статус

**Частично.** Command R/R+ — open weights (CC-BY-NC, некоммерческая лицензия). Embed и Rerank — proprietary API.

## Use Cases

- Enterprise RAG: поиск по внутренним документам с ререйкингом
- Мультиязычный semantic search
- Чат-боты с точным retrieval
- Email/документооборот с AI-суммаризацией

## Отзывы и критика

- Плюсы: лучшие в классе ререйкеры, качественные multilingual embeddings, enterprise-friendly
- Минусы: модель R+ слабее GPT-5.5/Claude Opus для сложного reasoning; ограниченная агентная экосистема

## Связи

- [Ререйкеры](rerankers.md) — Cohere Rerank как ключевой игрок
- [Модели для эмбеддингов](OVERVIEW.md)
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md)
- [Исследование фреймворков](../agent-frameworks-research.md)

*Добавлено: 2026-06-29*
