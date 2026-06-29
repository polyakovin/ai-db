---
title: Google Gemini
url: https://gemini.google.com/
type: url
category: tools
tags: [llm, multimodal, platform, agent, computer-use, open-source]
added: 2026-06-29
status: new
---

# Google Gemini

Семейство мультимодальных LLM от Google DeepMind — флагманская AI-платформа Google, встроенная в Workspace, Chrome, Android, Search и доступная через API.

## Модельное семейство (июнь 2026)

Google поддерживает три активных поколения моделей:

| Модель | Статус | Особенности |
|--------|--------|-------------|
| **Gemini 3.5 Flash** | GA (май 2026) | Сильнейшая agentic/coding Flash-модель, $1.50/$9 per 1M токенов, 1M контекст, 76.2% Terminal-Bench 2.1, бьёт Gemini 3.1 Pro по coding и agentic бенчмаркам |
| **Gemini 3.1 Pro Preview** | Preview | Флагманская модель (paid-only), 2M контекст |
| **Gemini 3 Flash** | GA | Frontier-class производительность по цене Flash, 1M контекст |
| **Gemini 3.1 Flash-Lite** | GA | Самая дешёвая модель семейства |
| **Gemini 2.5 Pro** | GA | Предыдущий флагман, Computer Use model (UI-агент) |
| **Gemini 2.5 Flash / Flash-Lite** | GA | Стабильные модели предыдущего поколения |
| **Gemini Computer Use** | Preview | Специализированная модель для управления UI (клики, заполнение форм, навигация) |

## Агентные возможности

Gemini активно развивается в сторону AI-агентов:

| Возможность | Описание |
|-------------|----------|
| **Computer Use** | Модель для построения агентов, управляющих браузером/десктопом через скриншоты и UI-действия (клики, скролл, ввод). Gemini 3.5 Flash — рекомендуемая модель |
| **Gemini CLI** | Open-source терминальный агент для разработки (ReAct loop, MCP-серверы, GitHub Actions, checkpointing). Поддержка Gemini 3 моделей. Бесплатный доступ с личным Google-аккаунтом |
| **Gemini Code Assist** | AI-ассистент в VS Code + Gemini CLI для командной разработки (Free, Standard, Enterprise) |
| **Interactions API** | Server-side history management (аналог OpenAI Responses API, beta) |
| **Agentic Vision** | Апдейт для Gemini 2.5 Flash (январь 2026) — усиление работы с «трудным» визуальным контентом |
| **Antigravity Agent Preview** | Экспериментальный агент Google |

## Интеграция в экосистему Google

- **Gemini App** — потребительское приложение (Gemini 3 Flash, 32K контекст, до 30 запросов/день, 5 Deep Research отчётов/месяц)
- **Workspace** — Docs, Sheets, Slides, Gmail, Drive («Help me create», генерация по данным из Gmail/Chat/Drive)
- **Google Search** — AI Mode в поиске
- **Android** — системная интеграция
- **API** — Google AI Studio, Vertex AI, Gemini API

## Платформа для разработки

- Бесплатный API для Gemini 3.5 Flash, 3 Flash, 2.5 Flash (rate limits + data usage for improvement)
- Gemini 3.1 Pro Preview — paid-only
- Gemini CLI — open source на GitHub (`google-gemini/gemini-cli`)
- MCP-серверы, Extensions, headless JSON output
- Поддержка grounding (Google Maps, web search)

## Релевантность для базы знаний

Gemini — ключевой игрок в AI-агентной экосистеме:
- Computer Use — прямой конкурент Claude Computer Use и OpenAI CUA
- Gemini CLI — альтернатива Claude Code, OpenAI Codex CLI и OpenCode
- Open-source агентная платформа с MCP-расширяемостью
- Бесплатный доступ к frontier-моделям для инди-разработчиков

## Связи

- [[perplexity.md|Perplexity AI]] — альтернативная AI-платформа с агентными возможностями
- [[../patterns/architecture-design/agent-harness.md|Agent Harness]] — Computer Use как вариант построения UI-агента
- [[../patterns/implementation/working-with-coding-agents.md|Работа с код-агентами]] — Gemini CLI как coding agent
- [[agent-frameworks-research.md|Исследование фреймворков]] — контекст: Gemini API vs OpenAI/Anthropic

*Добавлено: 2026-06-29*
