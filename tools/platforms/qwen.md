---
title: Qwen (Alibaba)
url: https://qwenlm.github.io/
type: url
category: tools
tags: [llm, platform, chinese, open-source, coding, agent, multimodal]
added: 2026-06-29
status: new
---

# Qwen (Alibaba)

Qwen — семейство AI-моделей от Alibaba Cloud (Qwen Team), один из ведущих китайских разработчиков LLM. Отличается феноменальной эффективностью (Qwen3.6-35B-A3B: 3B активных параметров, 73.4% SWE-bench Verified) и сильным соотношением цена/качество. Новейшие модели (Qwen3.7-Max, Qwen3.7-Plus) доступны только через API — Alibaba переходит к закрытой модели распространения.

## Ключевые возможности

- **Qwen3.7-Max** (май 2026) — флагманская API-only модель: agent frontier, coding, office tasks, long-horizon автономное исполнение (до 35 часов).
- **Qwen3.7-Plus** (июнь 2026) — мультимодальная (текст + видео + изображения), на 60% дешевле Max, $0.40/$1.60 за 1M токенов.
- **Qwen3.6-35B-A3B** — open-weight чудо эффективности: 3B активных параметров из 35B, запуск на одной 24GB GPU, 73.4% SWE-bench Verified.
- **Qwen3.6-Max Preview** — 262K контекст, сильный reasoning.
- **Qwen Chat** — потребительский интерфейс.

## Модели (июнь 2026)

| Модель | Статус | Контекст | Цена API (input/output за 1M токенов) | Особенности |
|--------|--------|----------|--------------------------------------|-------------|
| **Qwen3.7-Max** | API-only (май 2026) | ~128K | $2.50 / $7.50 (Alibaba Cloud) | Флагман: agent frontier, автономная работа до 35ч, поддержка Claude Code |
| **Qwen3.7-Plus** | API-only (июнь 2026) | ~128K | $0.40 / $1.60 | Мультимодальная: текст + видео + изображения, 60% дешевле Max |
| **Qwen3.6-Max Preview** | API | 262K | $1.04 / $6.24 (OpenRouter) | Сильный reasoning, конкурент GPT-5.4 |
| **Qwen3.6-35B-A3B** | Open-weight | ~128K | $0.325 / $1.95 (API) | Эффективность: 3B активных, одна 24GB GPU |
| **Qwen3-Max Preview** | API | 262K | $1.20 / $6.00 | Предыдущее поколение Max |

### Важное изменение (июнь 2026):
Alibaba переходит к закрытой модели распространения для новых релизов. Qwen3.7-Max и Qwen3.7-Plus — **API-only**, веса не публикуются. Это отход от предыдущей open-source стратегии Qwen, что вызвало разочарование сообщества (включая крупных пользователей типа Airbnb).

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Long-horizon agents** | Qwen3.7-Max: автономное исполнение до 35 часов |
| **Coding** | Сильные результаты на SWE-bench Verified (73.4% у Qwen3.6-35B) |
| **External harness** | Поддержка Claude Code через совместимый API |
| **Office & productivity** | Автоматизация офисных задач, работа с документами |
| **Multimodal agents** | Qwen3.7-Plus: видео + изображения + текст |
| **Reasoning** | Extended thinking для сложных задач |

## Open Source статус

| Период | Стратегия |
|--------|-----------|
| **До июня 2026** | Open-weight модели: Qwen, Qwen2.5, Qwen3 (включая Qwen3.6-35B-A3B) |
| **С июня 2026** | Закрытая стратегия: Qwen3.7-Max и Qwen3.7-Plus — API-only |

### Доступные open-weight модели:
- Qwen3.6-35B-A3B (Apache 2.0)
- Qwen2.5 семейство (разные размеры, Apache 2.0)
- Qwen2.5-Coder (специализация на коде)
- Более старые Qwen3 модели

## Цены и доступ

### API (Alibaba Cloud Model Studio)
| Модель | Input/MTok | Output/MTok |
|--------|-----------|-------------|
| Qwen3.7-Max | $2.50 | $7.50 |
| Qwen3.7-Plus | $0.40 | $1.60 |
| Qwen3.6-Max Preview | $1.04 | $6.24 |
| Qwen3.6-35B-A3B | $0.325 | $1.95 |

### Через OpenRouter:
- Qwen3.7-Max: $1.25/$3.75
- Qwen3.6-Max Preview: $1.04/$6.24

### Qwen Chat
- Бесплатный доступ к базовым моделям
- Платные tier для расширенных лимитов

## Бенчмарки

| Бенчмарк | Qwen3.7-Max | Qwen3.6-35B-A3B | GPT-5.5 |
|----------|-------------|-----------------|---------|
| SWE-bench Verified | ~78% (оценка) | 73.4% | ~73% |
| Coding | Сильный | Отличный для размера | Сильный |
| Reasoning | Competitive | Competitive | Лидер |

## Use Cases

- **Coding agents**: Qwen3.7-Max через Claude Code или как API для coding agents
- **Бюджетные production агенты**: Qwen3.7-Plus ($0.40/$1.60) для high-throughput
- **Self-hosted coding**: Qwen3.6-35B-A3B на одной GPU — рекордная эффективность
- **Office automation**: Документы, таблицы, презентации
- **Мультимодальные агенты**: Qwen3.7-Plus для видео + изображения + текст
- **Китайский рынок**: Нативная поддержка китайского языка, локальное развёртывание

## Отзывы и критика

### Сильные стороны:
- Рекордная эффективность: Qwen3.6-35B-A3B (3B активных = 73.4% SWE-bench)
- Qwen3.7-Plus: мультимодальность по низкой цене ($0.40/$1.60)
- Длительное автономное исполнение (до 35 часов для Qwen3.7-Max)
- Сильные результаты на coding бенчмарках
- Популярность среди self-hosted сообщества

### Слабые стороны:
- Закрытие новых моделей (Qwen3.7) — отход от open-source
- Китайская компания — регуляторные риски, цензура
- Меньше adoption на западе, чем OpenAI/Anthropic/DeepSeek
- Меньше community tooling и документации на английском
- Разочарование open-source сообщества (Airbnb и другие)

## Связи

- [[../../tools/platforms/anthropic.md|Anthropic (Claude)]] — совместимость с Claude Code как external harness
- [[../../tools/platforms/openai.md|OpenAI]] — конкурент по agentic coding
- [[../platforms/deepseek.md|DeepSeek]] — китайский конкурент (open-weight vs closed)
- [[../platforms/z-ai.md|Z.ai (GLM)]] — китайский конкурент (open-weight MIT)
- [[../agent-model-map.md|Модельная карта]] — Qwen в карте моделей

*Добавлено: 2026-06-29*
