---
title: Mistral AI
url: https://mistral.ai/
type: url
category: tools
tags: [llm, platform, european, coding, agent, api, open-source]
added: 2026-06-29
status: new
---

# Mistral AI

Mistral AI — французская AI-компания (основана в 2023 году), европейский лидер в разработке LLM. Предоставляет семейство моделей от lightweight (Ministral) до флагманских (Large, Medium), с фокусом на эффективность, latency, открытость и enterprise-интеграцию. Платформа Le Chat — потребительский AI-ассистент с агентными возможностями и Pro-подпиской.

## Ключевые возможности

- **Mistral API** — доступ к моделям через REST API с поддержкой function calling, structured outputs, prompt caching.
- **Le Chat** — потребительский AI-ассистент: чат, агенты (Vibe), coding, поиск, Canvas.
- **Vibe** — агентная платформа в Le Chat: автономное выполнение задач, remote agents.
- **Le Chat Pro** ($14.99/мес) — расширенные возможности, агенты, большие лимиты.
- **Open models** — Ministral, Mistral 3, Small 4, Devstral 2 — open-weight модели для self-hosting.
- **Specialist models** — Codestral (code), Voxtral (speech), OCR, Moderation, Leanstral (embedding).

## Модели (июнь 2026)

### Generalist models

| Модель | Статус | Цена API (input/output за 1M токенов) | Особенности |
|--------|--------|--------------------------------------|-------------|
| **Mistral Large 3** | GA (декабрь 2025) | $0.50 / $1.50 | Флагман: reasoning, coding, multilingual, 256K контекст |
| **Mistral Medium 3.5** | GA (апрель 2026) | $1.50 / $7.50 | Dense 128B: agentic workflows, coding, multi-step reasoning |
| **Mistral Small 4** | GA (март 2026) | $0.15 / $0.60 | Unified hybrid: instruct + reasoning + coding в одной модели |
| **Ministral 3 14B** | Open | — | Лучшая в классе text + vision, сравнима с Mistral Small 3.2 |
| **Ministral 3 8B** | Open | — | Эффективная text + vision модель |
| **Ministral 3 3B** | Open | — | Tiny model с vision capabilities |

### Specialist models

| Модель | Назначение | Цена API |
|--------|-----------|----------|
| **Codestral** | Code generation, code agents, fill-in-the-middle | $0.30 / $0.90 |
| **Devstral 2** | Open-source agentic coding (MIT) | Open-weight |
| **Voxtral TTS** | Text-to-speech | — |
| **Voxtral Mini Transcribe** | Speech-to-text | — |
| **OCR 4.0 / OCR 3** | Document OCR | — |
| **Mistral Moderation** | Content moderation | — |
| **Leanstral** | Embedding model | — |

### Previous/Labs:
- Mistral 3 (декабрь 2025, open-weight)
- Magistral Medium (enterprise, $2.00/$5.00)
- Nemo ($0.02/MTok input — самая дешёвая)

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Vibe (Le Chat)** | Агентная платформа: автономное выполнение задач, remote agents, workflow automation |
| **Function calling** | OpenAI-совместимый формат |
| **Tool use** | Structured outputs, parallel function calling |
| **Coding agents** | Codestral + Devstral 2 — open-source agentic coding |
| **Remote agents (Medium 3.5)** | Агенты для длительных автономных задач |

## Open Source статус

- **Open models**: Ministral 3, Mistral 3, Small 4 — open-weight (Apache 2.0 / Mistral Research License)
- **Devstral 2**: open-source agentic coding (MIT)
- **Large 3, Medium 3.5**: доступны только через API (закрытые)
- **Codestral**: закрытая, но доступна в Le Chat Pro
- **Voxtral Mini Transcribe Realtime**: open-weight

## Цены и доступ

### API (июнь 2026)
| Модель | Input/MTok | Output/MTok |
|--------|-----------|-------------|
| Mistral Large 3 | $0.50 | $1.50 |
| Mistral Medium 3.5 | $1.50 | $7.50 |
| Mistral Small 4 | $0.15 | $0.60 |
| Codestral | $0.30 | $0.90 |
| Nemo | $0.02 | — |

### Le Chat
- **Free**: базовые модели, ограниченные запросы
- **Pro** ($14.99/мес): Large 3, Codestral, Vibe agents, Canvas, file uploads
- **Enterprise**: отдельные соглашения

### Сравнение цен с конкурентами
| Провайдер | Флагманская модель | Input/Output | 
|-----------|-------------------|--------------|
| Mistral | Large 3 | $0.50/$1.50 |
| OpenAI | GPT-5.5 | ~$2.50/$10 |
| Anthropic | Opus 4.8 | $5/$25 |
| DeepSeek | V4 Flash | $0.14/$0.28 |

## Use Cases

- **European data residency**: GDPR-совместимые AI-решения на европейских серверах
- **Cost-sensitive production**: Mistral Large 3 в 5-30× дешевле Opus/GPT-5.5
- **Coding agents**: Devstral 2 для open-source agentic coding
- **Enterprise RAG**: Ministral для self-hosted retrieval
- **Multilingual apps**: Сильная поддержка европейских языков
- **Speech interfaces**: Voxtral TTS + Transcribe

## Отзывы и критика

### Сильные стороны:
- Европейский провайдер (GDPR, data residency)
- Отличное соотношение цена/качество (Large 3: $0.50/$1.50)
- Open-weight модели для self-hosting
- Широкий спектр специализированных моделей (code, speech, OCR)
- Le Chat Pro — доступный потребительский тариф ($14.99/мес)

### Слабые стороны:
- Уступает frontier-моделям (GPT-5.5, Opus 4.8) на сложных reasoning задачах
- Меньше adoption, чем OpenAI/Anthropic
- Нет managed agent stack как у OpenAI
- Vibe (агенты) — новее и менее зрело, чем Claude Cowork
- Меньше community content

## Связи

- [[../../tools/platforms/anthropic.md|Anthropic (Claude)]] — конкурент по frontier-моделям
- [[../../tools/platforms/openai.md|OpenAI]] — конкурент по API и агентам
- [[../platforms/deepseek.md|DeepSeek]] — конкурент по цене и open-weight
- [[../agent-model-map.md|Модельная карта]] — Mistral в карте моделей
- [[../agent-frameworks-research.md|Исследование фреймворков]] — Mistral как API-провайдер

*Добавлено: 2026-06-29*
