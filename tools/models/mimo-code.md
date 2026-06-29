---
name: MiMo Code
vendor: Xiaomi
type: Code LLM / Agentic Coding Harness
url: https://mimo.xiaomi.com/zh/mimocode
github: https://github.com/XiaomiMiMo/MiMo-Code
license: MIT (+ Use Restrictions)
updated: 2026-06-29
---

# MiMo Code

Кодовый AI-ассистент и семейство моделей от Xiaomi. Терминальный (terminal-native) инструмент для разработки с открытым исходным кодом, построенный на форке OpenCode. Включает персистентную память, Compose-режим, голосовое управление и систему самообучения (`/dream`).

## Модели семейства MiMo

### MiMo-V2.5-Pro (флагман, апрель 2026)
- **Архитектура:** Mixture of Experts (MoE)
- **Всего параметров:** 1.02T (триллион)
- **Активных параметров на токен:** 42B
- **Контекстное окно:** 1M токенов (базовая версия 256K)
- **Претрейн:** 27 трлн токенов
- **Лицензия:** MIT (коммерческое использование, файнтюн)
- **HuggingFace:** `XiaomiMiMo/MiMo-V2.5-Pro`
- **Особенности:** нативное мультимодальное восприятие (изображения, видео, аудио, текст), агентное исполнение

### MiMo-V2.5 (апрель 2026)
- **Архитектура:** MoE, ~310B total / 15B active
- **Контекстное окно:** 1M токенов
- **Цена (API):** $0.14/M input (cache miss), $0.28/M output
- **Особенности:** омнимодальная модель, сопоставима по производительности с [Claude Sonnet](../platforms/anthropic.md) 4.6, встроена в MiMo Code бесплатно (limited time)

### MiMo-V2-Flash (январь 2026, обновление февраль 2026)
- **Архитектура:** MoE, 309B total / 15B active
- **Гибридное внимание:** Sliding Window Attention (SWA) + Global Attention (5:1), окно 128 токенов
- **Контекст:** 32K native → 256K extended
- **Претрейн:** 27 трлн токенов с Multi-Token Prediction (MTP)
- **Посттренинг:** Multi-Teacher On-Policy Distillation (MOPD)
- **Спекулятивное декодирование:** до 3.6× acceptance length, 2.6× ускорение
- **Лицензия:** MIT (open-weight)
- **arXiv:** [2601.02780v2](https://arxiv.org/html/2601.02780v2)
- **SWE-Bench Verified (Thinking):** 78.6% (v2-flash-0204)
- **Tool Calling Accuracy (Thinking):** 97.0%

### MiMo-7B (май 2025) — исследовательская серия
- **Параметры:** 7B, обучена с нуля (from scratch)
- **Претрейн:** 25 трлн токенов, с Multi-Token Prediction (MTP)
- **Посттренинг:** Base → SFT → RL (Reinforcement Learning)
- **MiMo-7B-RL-0530:** превосходит [DeepSeek](../platforms/deepseek.md) R1 (79.8) на AIME24 (80.1)
- **MATH500:** 97.2 (MiMo-7B-RL-0530)
- **LiveCodeBench v5:** 60.9 (MiMo-7B-RL-0530)
- **Релиз:** GitHub [xiaomimimo/mimo](https://github.com/xiaomimimo/mimo), HuggingFace `XiaomiMiMo/MiMo-7B-*`
- **Лицензия:** открытая (open-source)

## Бенчмарки MiMo Code (V0.1.0, июнь 2026)

Сравнение MiMo Code vs [Claude Code](../platforms/anthropic.md) (одинаковая модель MiMo-V2.5-Pro):

| Benchmark | MiMo Code | Claude Code |
|-----------|-----------|-------------|
| **SWE-bench Verified** | **82%** | 79% |
| **SWE-bench Pro** | **62%** | 57% |
| **Terminal Bench 2** | **73%** | 68% |

### A/B тестирование (576 разработчиков, 474 репозитория, 1213 пар):
- Задачи до 200 шагов: ~50/50 с [Claude Code](../platforms/anthropic.md)
- Задачи свыше 200 шагов: MiMo Code побеждает в >65% случаев

### Бенчмарки моделей:

| Бенчмарк | V2.5-Pro | V2-Flash (0204) | Claude Opus 4.6 |
|----------|----------|-----------------|-----------------|
| SWE-Bench Verified (Thinking) | — | 78.6% | — |
| SWE-Bench Verified (Non-Thinking) | — | 73.7% | — |
| Arena-Hard Hard Prompt (Thinking) | — | 60.6 | — |
| Tool Call Success (Thinking) | — | 97.0% | — |
| ClawEval (agentic) | 63.8% | — | — |

## Ключевые архитектурные особенности

### Персистентная память (Persistent Memory)
- **4-слойная система:** project memory (`MEMORY.md`), session checkpoints, scratch notes, per-task progress logs
- **Индексирование:** SQLite FTS5 (полнотекстовый поиск)
- **Checkpoint-writer subagent:** Независимый субагент сохраняет состояние, пока основной агент работает
- **Автовосстановление:** При переполнении контекстного окна среда восстанавливается из структурированных чекпоинтов

### Compose Mode
- Активация по клавише **Tab**
- Полный цикл: дизайн → планирование → кодирование → тестирование → ревью → готовый продукт
- Спецификация-ориентированная разработка (specs-driven)

### Самообучение
- **`/dream`** — запускается каждые ~7 дней, анализирует историю сессий, дедуплицирует, сжимает в долговременную память
- **`/distill`** — извлекает повторяемые рабочие процессы из прошлых сессий

### Multi-Agent система
| Агент | Назначение |
|-------|-----------|
| **build** (по умолчанию) | Полный доступ к инструментам для разработки |
| **plan** | Read-only режим для анализа и проектирования |
| **compose** | Оркестрация spec-driven разработки |

- Субагенты создаются автоматически, работают параллельно
- Goal/Stop Condition — независимый judge-model для предотвращения преждевременных остановок при автономной работе

### Голосовое управление
- Распознавание: MiMo-V2.5-ASR + TenVAD
- Режимы: диктовка кода, голосовые команды ("send", "execute")
- Поддержка: китайский, английский, диалекты (кантонский, миньнань, сычуаньский, у)

## Цены и API-доступ

### MiMo Code (инструмент)
- **MiMo-V2.5:** бесплатно (limited time), встроен в MiMo Code Auto channel
- **MiMo-V2.5-Pro:** $1.00/M input (≤256K), $3.00/M output (≤256K); $2.00/$6.00 (>256K)
- **Token Plan:** годовые пакеты токенов на platform.xiaomimimo.com

### API (Pay-as-you-go, международные цены)
| Модель | Input (Cache Miss) | Output |
|--------|-------------------|--------|
| `mimo-v2.5-pro` | $0.435/M | $0.87/M |
| `mimo-v2.5` | $0.14/M | $0.28/M |
| `mimo-v2.5-asr` | $0.074/час | — |

### OpenRouter
- `xiaomi/mimo-v2-pro`: $1/M input, $3/M output
- `xiaomi/mimo-v2-omni`: $0.40/M input, $2.00/M output

### Интеграции
- **Kilo Code:** VS Code, JetBrains, [[../ides/cursor.md|Cursor]], Windsurf, Trae — MiMo-V2-Flash, MiMo-V2.5, MiMo-V2.5-Pro
- **[Claude Code](../platforms/anthropic.md):** совместимость через [Anthropic](../platforms/anthropic.md)-compatible API endpoint
- **OpenCode:** основа форка, все возможности OpenCode сохранены
- **OpenRouter:** API-доступ ко всем моделям
- **MCP:** поддержка Model Context Protocol (импорт из [Claude Code](../platforms/anthropic.md))

## Open Source статус

| Компонент | Лицензия | Репозиторий |
|-----------|----------|-------------|
| MiMo Code (агент) | MIT (+ Use Restrictions) | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) |
| MiMo-V2.5-Pro (модель) | MIT (open-weight) | [HuggingFace](https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro) |
| MiMo-V2-Flash (модель) | MIT (open-weight) | [GitHub](https://github.com/xiaomimimo/MiMo-V2-Flash) |
| MiMo-7B (модель) | Открытая | [GitHub](https://github.com/xiaomimimo/mimo) / HF |

- MiMo Code основан на форке [OpenCode](https://github.com/anomalyco/opencode)
- Полный код агента открыт под MIT
- Веса моделей доступны на HuggingFace и ModelScope
- Действуют Use Restrictions на использование сервисов Xiaomi MiMo

## Use Cases

1. **Автономная разработка:** полный цикл от идеи до production-кода (301+ коммитов в тестах)
2. **Длинные multi-step задачи:** наилучшие результаты при 200+ шаговых сценариях
3. **Code review и багфиксинг:** SWE-bench Pro 62% (выше GPT-5.5 с 58.6%)
4. **Кросс-модальная разработка:** работа с изображениями, аудио, видео в контексте кода
5. **Спецификация-ориентированная разработка:** Compose mode для промышленного кода
6. **Локальный запуск:** open-weight модели для on-premise/air-gapped использования
7. **Голосовое программирование:** hands-free coding через ASR

## Отзывы и критика

### Положительные:
- Превосходит [Claude Code](../platforms/anthropic.md) на длинных задачах (200+ шагов)
- Значительно дешевле конкурентов: в 10-87× дешевле GPT-5.5 и [Claude Opus](../platforms/anthropic.md) 4.8
- Тратит на 40-60% меньше токенов на траекторию (против [Claude Opus](../platforms/anthropic.md) 4.6, [Gemini](../platforms/gemini.md) 3.1 Pro, GPT-5.4)
- Активное open-source сообщество, MIT лицензия

### Негативные:
- Жалобы на лимиты использования и «misleading marketing» Token Plan
- Проблемы с настройкой в OpenCode (требует доработки)
- По некоторым тестам уступает GLM 5.1
- Самостоятельные (self-reported) бенчмарки — требуется независимая верификация
- Не сравнивались напрямую с [Codex CLI](../platforms/openai.md) и [Gemini](../platforms/gemini.md) CLI

## Ключевые конкуренты
- [Claude Code](../platforms/anthropic.md) ([Anthropic](../platforms/anthropic.md)) — прямой бенчмарк-конкурент
- [OpenAI](../platforms/openai.md) [Codex CLI](../platforms/openai.md) + GPT-5.5
- GLM-5.1 / Kimi K2.6 (китайские open-source альтернативы)
- [DeepSeek](../platforms/deepseek.md) V3.2
- [Qwen](../platforms/qwen.md) (Alibaba)

## Ключевые даты
- **Май 2025:** Релиз MiMo-7B (исследовательская серия)
- **Январь 2026:** MiMo-V2-Flash, arXiv technical report
- **Февраль 2026:** MiMo-V2-Flash обновление (SWE-Bench 78.6%)
- **Март 2026:** MiMo-V2-Pro, MiMo-V2-Omni, MiMo-V2-TTS
- **Апрель 2026:** MiMo-V2.5 и MiMo-V2.5-Pro (1T параметров)
- **Июнь 2026:** MiMo Code V0.1.0 — терминальный AI coding assistant

## Ссылки
- [MiMo Code — официальная страница](https://mimo.xiaomi.com/zh/mimocode)
- [MiMo Code GitHub](https://github.com/XiaomiMiMo/MiMo-Code)
- [MiMo API Pricing](https://mimo.mi.com/docs/en-US/price/pay-as-you-go)
- [MiMo Token Plan](https://platform.xiaomimimo.com/token-plan)
- [MiMo Model Releases](https://mimo.mi.com/docs/en-US/updates/model)
- [MiMo-7B GitHub](https://github.com/xiaomimimo/mimo)
- [MiMo-V2-Flash arXiv](https://arxiv.org/html/2601.02780v2)
- [MiMo on HuggingFace](https://huggingface.co/XiaomiMiMo)
- [VentureBeat: MiMo Code beats Claude Code](https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks)
- [MiMo Coding Models on Kilo Code](https://kilo.ai/models/by/xiaomi)

## См. также
- [[../../tools/OVERVIEW.md|tools/OVERVIEW.md]] — обзор инструментов и моделей
- [[../../tools/agent-model-map.md|Модельная карта]] — MiMo модели в карте
- [[../../patterns/implementation/working-with-coding-agents.md|Работа с код-агентами]] — MiMo Code как coding agent
- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — MiMo Code как реализация harness
