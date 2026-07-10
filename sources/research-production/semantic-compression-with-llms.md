---
title: Semantic Compression With Large Language Models
url: https://arxiv.org/abs/2304.12512
type: url
category: sources
tags: [llm, compression, context, benchmarks, agents]
added: 2026-07-06
status: verified
---

# Semantic Compression With Large Language Models

Исследование о том, как LLM могут сжимать текст, сохранять его смысл и использовать сжатые представления для reasoning без полного восстановления исходного текста.

## Описание

- Проблема: рост длины задач и контекста снижает стоимость и скорость агентных пайплайнов.
- Ключевая идея: использовать компрессию как промежуточное состояние, а не терять информацию до критических деталей.
- В статье рассматриваются метрики качества сжатия и восстановительной точности.

## Обзор ресурса

- Важен для темы контекстного budget в агентных системах и для сравнения с подходом `BabelTele`.
- Помогает обосновать, когда компрессия снижает стоимость контекста без критической потери semantic fidelity.
- Рекомендуется как baseline для сравнения новых model-native форматов в multi-step research/coding пайплайнах.

## Связи

- [Per-context memory patterns](../../patterns/advanced/agent-memory-patterns.md) — как компрессия меняет глубину хранения.
- [Агентная компрессия контекста (BabelTele)](../../patterns/advanced/agent-context-distillation.md) — практическая модель уплотнения между шагами.
|- [Оценка ответов LLM](../../patterns/implementation/llm-response-evaluation.md) — оценка качества декомпрессии.

## Верификация

- **Дата:** 2026-07-10
- **Метод:** открыт arXiv abstract по URL https://arxiv.org/abs/2304.12512
- **Результат:** страница доступна, статья опубликована в cs.AI, имеет DOI 10.48550/arXiv.2304.12512. Описание и relevance, указанные в заметке, соответствуют содержанию abstract.

