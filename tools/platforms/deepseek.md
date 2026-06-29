---
title: DeepSeek
url: https://www.deepseek.com/
type: url
category: tools
tags: [llm, platform, open-source, coding, agent, api]
added: 2026-06-29
status: new
---

# DeepSeek

DeepSeek — китайская AI-компания, разработчик open-weight моделей семейства DeepSeek V. Известна сверхнизкими ценами API и открытыми весами моделей с frontier-производительностью. Флагманские модели: DeepSeek V4 Pro и V4 Flash (апрель 2026). Предоставляет [OpenAI](openai.md)-совместимый API и модель для самостоятельного хостинга.

## Ключевые возможности

- **DeepSeek V4 Pro** — флагманская модель: 1.6T параметров (MoE, 49B активных), 1M контекст, 384K output. Reasoning mode (Chain-of-Thought) для сложных задач.
- **DeepSeek V4 Flash** — экономичная модель: 1M контекст, $0.14/MTok input, $0.28/MTok output — одна из самых дешёвых frontier-моделей.
- **[OpenAI](openai.md)-совместимый API** — `api.deepseek.com`, drop-in замена [OpenAI](openai.md).
- **Open weights** — модели доступны для скачивания и self-hosting.
- **Context caching** — поддержка KV-cache для повторяющихся контекстов (снижение стоимости).
- **Agent integrations** — поддержка [Claude Code](anthropic.md), OpenCode и других coding agents.

## Модели (июнь 2026)

| Модель | Статус | Контекст | Цена API (input/output за 1M токенов) | Особенности |
|--------|--------|----------|--------------------------------------|-------------|
| **DeepSeek V4 Pro** | GA (апрель 2026) | 1M (384K output) | $0.88 / $3.48 (среднее с 50% cache hits) | Флагман: reasoning, coding, agents. Thinking mode для Chain-of-Thought |
| **DeepSeek V4 Pro (non-thinking)** | GA | 1M (384K output) | $0.88 / $3.48 | Быстрый режим без reasoning overhead |
| **DeepSeek V4 Flash** | GA (апрель 2026) | 1M (384K output) | $0.14 / $0.28 | Экономичная frontier-adjacent модель |
| **DeepSeek V4 Flash (thinking)** | GA | 1M (384K output) | $0.14 / $0.28 | Reasoning mode |
| **DeepSeek V3.2** | GA (декабрь 2025) | 164K | $0.23 / $0.34 | Предыдущее поколение, всё ещё competitive |
| **DeepSeek V3.2 Thinking** | GA | 164K | $0.23 / $0.34 | Reasoning mode для V3.2 |

### Примечания:
- `deepseek-chat` и `deepseek-reasoner` — legacy-алиасы для V4 Flash (non-thinking и thinking modes)
- DeepSeek V3.2 остаётся доступной для тех, кому нужна стабильная legacy-модель
- V4 Pro доступна только через API (не open-weight)

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Function calling** | OpenAI-совместимый формат, поддержка structured outputs |
| **Tool use** | Модели оптимизированы для agentic workloads и multi-step tool calling |
| **Reasoning** | Thinking mode (Chain-of-Thought) для сложных многошаговых задач |
| **Coding agents** | Совместимость с [Claude Code](anthropic.md), OpenCode, Cline и другими coding agents через OpenAI-совместимый endpoint |
| **MCP-интеграции** | Через совместимость с [Claude Code](anthropic.md) и другими платформами |

## Open Source статус

- **DeepSeek V3.2** — open-weight (веса доступны для скачивания)
- **DeepSeek V4 Flash** — open-weight
- **DeepSeek V4 Pro** — API-only (веса не публикуются)
- Лицензия: MIT-like (разрешён коммерческий использование и fine-tuning)
- Самостоятельный хостинг: требует multi-GPU сервер (MoE архитектура, 1.6T параметров для Pro)

## Цены и доступ

### API (июнь 2026)
| Модель | Input (cache miss) | Output | Примечание |
|--------|-------------------|--------|------------|
| V4 Flash | $0.14/MTok | $0.28/MTok | Cache hit: $0.0028/MTok |
| V4 Flash (thinking) | $0.14/MTok | $0.28/MTok | + reasoning токены |
| V4 Pro | $0.88/MTok | $3.48/MTok | Среднее с 50% cache hits |
| V4 Pro (thinking) | $0.88/MTok | $3.48/MTok | + reasoning токены |

### Сравнение цен с конкурентами
| Провайдер | Модель | Input/MTok | Output/MTok |
|-----------|--------|-----------|-------------|
| DeepSeek | V4 Flash | **$0.14** | **$0.28** |
| DeepSeek | V4 Pro | $0.88 | $3.48 |
| OpenAI | GPT-5.5 | ~$2.50 | ~$10 |
| Anthropic | Claude Opus 4.8 | $5 | $25 |
| Anthropic | Claude Haiku 4.5 | $1 | $5 |

**Вывод:** DeepSeek V4 Flash — самая дешёвая frontier-модель (в 35-100× дешевле GPT-5.5/Opus).

### Бесплатный tier
- Доступен через DeepSeek Chat (веб-интерфейс и мобильное приложение)
- Ограниченный API (регистрация с номером телефона)

## Use Cases

- **Бюджетные production-агенты**: V4 Flash для high-throughput сценариев при минимальной стоимости
- **Self-hosted агенты**: V3.2 или V4 Flash на собственных GPU — контроль данных и cost predictability
- **Coding assistants**: Через совместимость с [Claude Code](anthropic.md), OpenCode, Cline
- **Research/prototyping**: Быстрые и дешёвые итерации с frontier-качеством
- **Многоязычные сценарии**: Сильная поддержка китайского и английского

## Бенчмарки (апрель 2026)

| Бенчмарк | V4 Pro | V4 Flash |
|----------|--------|----------|
| Coding (non-thinking) | 65 | 61 |
| Coding (thinking) | 86 | 77 |
| SWE-bench Verified | **80.6%** | — |
| Math/Reasoning | competitive | competitive |

## Отзывы и критика

### Сильные стороны:
- Рекордно низкие цены API (V4 Flash: $0.14/$0.28 за 1M токенов)
- Open-weight модели для self-hosting
- [OpenAI](openai.md)-совместимый API — drop-in замена
- Сильные результаты на coding бенчмарках
- 1M контекстное окно

### Слабые стороны:
- Китайская компания — регуляторные риски (запреты в некоторых юрисдикциях, цензура)
- V4 Pro не открыта (API-only)
- Сообщество меньше, чем у [OpenAI](openai.md)/[Anthropic](anthropic.md)
- Проблемы с доступностью API при пиковых нагрузках
- Требования к регистрации (номер телефона) для бесплатного tier

## Связи

- [Anthropic (Claude)](../../tools/platforms/anthropic.md) — конкурент по frontier-моделям
- [OpenAI](../../tools/platforms/openai.md) — конкурент по API и coding agents
- [Z.ai (GLM)](../platforms/z-ai.md) — китайский open-weight конкурент
- [Google Gemini](gemini.md) — альтернативный провайдер
- [Модельная карта](../agent-model-map.md) — DeepSeek в карте моделей
- [Исследование фреймворков](../agent-frameworks-research.md) — DeepSeek как API-провайдер
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — self-hosted агенты с DeepSeek

*Добавлено: 2026-06-29*
