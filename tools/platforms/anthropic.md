---
title: Anthropic (Claude)
url: https://www.anthropic.com/
type: url
category: tools
tags: [llm, platform, agent, coding, computer-use, claude-code, cowork]
added: 2026-06-29
status: new
---

# Anthropic (Claude)

Anthropic — американская AI-компания, создатель семейства моделей Claude и платформы для безопасных AI-агентов. Основана в 2021 году бывшими сотрудниками [OpenAI](openai.md). Флагманское направление — Claude: мультимодальные LLM, coding agents (Claude Code), enterprise-агенты (Cowork) и API. Оценка компании — $380 млрд (февраль 2026).

## Ключевые возможности

- **Claude API** — доступ к семейству моделей через REST API с поддержкой extended thinking, tool use, computer use, prompt caching (90% скидка на кешированные чтения) и batch processing (50% скидка).
- **Claude Code** — терминальный coding agent для разработки: работа с репозиториями, MCP-серверы, approvals, команды, agent teams, scheduled tasks.
- **Claude Cowork** — enterprise AI-агент для knowledge workers: автономное выполнение задач на компьютере, плагины, connectors (Google Drive, Slack), scheduled tasks, Dispatch (удалённый запуск с телефона).
- **Computer Use** — управление десктопом/браузером через скриншоты и UI-действия (клики, скролл, ввод текста).
- **Extended Thinking** — chain-of-thought reasoning для сложных задач (доступно для Opus и Sonnet).
- **Agent Teams** — multi-agent workflows с изолированными контекстами и оркестрацией.

## Модели (июнь 2026)

| Модель | Статус | Цена API (input/output за 1M токенов) | Особенности |
|--------|--------|--------------------------------------|-------------|
| **Claude Opus 4.8** | GA (май 2026) | $5 / $25 | Флагман: adaptive thinking, Fast Mode (3× дешевле), лучшая coding-модель, 1M контекст |
| **Claude Opus 4.7** | GA | $5 / $25 | Vision + long-horizon agents |
| **Claude Sonnet 4.6** | GA | $3 / $15 | Рекомендуемый по умолчанию: strong coding + agent capabilities, 1M контекст |
| **Claude Haiku 4.5** | GA | $1 / $5 | Самая быстрая и дешёвая модель семейства |

### Модели предыдущего поколения (доступны по pinned version ID):
- Claude Opus 4.5 (стабильная, предыдущее поколение)
- Claude Sonnet 4.5 (рекомендуемая по умолчанию в некоторых вариантах)
- Claude Sonnet 4.0 (отдельное long-context ценообразование >200K токенов)

## Агентные возможности

| Возможность | Описание |
|-------------|----------|
| **Claude Code** | Терминальный coding agent: работа с репозиториями, plan mode, code generation, тестирование, approvals. Поддерживает agent teams, scheduled tasks, MCP-серверы. Код Cowork был написан Claude Code целиком |
| **Claude Cowork** | Enterprise AI-агент для офисных работников: автономное выполнение задач, плагины, интеграции |
| **Computer Use** | Управление GUI через скриншоты: клики, скролл, заполнение форм, навигация |
| **Agent Teams** | Мультиагентная оркестрация с изолированными контекстами |
| **Dispatch** | Удалённый запуск задач с мобильного телефона |
| **Scheduled Tasks** | Автоматические ежедневные workflow |
| **Projects** | Рабочие пространства с персистентным контекстом и правилами |
| **Skills** | Переиспользуемые инструкции для агентов (аналог skills в Claude Code) |

## Open Source статус

- **Закрытые модели** — Claude Opus, Sonnet, Haiku доступны только через API (Anthropic) или облачных провайдеров (AWS Bedrock, Google Vertex AI).
- **Claude Code и Cowork** — проприетарные, но Claude Code CLI бесплатен для использования с API-ключом.
- **MCP (Model Context Protocol)** — открытый стандарт для подключения AI-приложений к внешним системам, разработан Anthropic. Apache 2.0 лицензия.

## Цены и доступ

### API
- Haiku 4.5: $1/$5 за 1M токенов (самая доступная)
- Sonnet 4.6: $3/$15 за 1M токенов
- Opus 4.8: $5/$25 за 1M токенов (стандартный режим), Fast Mode — в 3× дешевле
- Prompt caching: 90% скидка на кешированные чтения
- Batch API: 50% скидка (обработка в течение 24 часов)
- Extended thinking: добавляет стоимость reasoning-токенов

### Подписки Claude
- **Max** ($100-200/мес): доступ к Opus через Claude Code, Agent Teams, 300M+ токенов/месяц
- **Pro** ($20/мес): Sonnet, базовые возможности
- **Free**: Haiku, ограниченные запросы

## Use Cases

- **Coding Agent**: Claude Code для терминальной разработки, plan mode с Opus, выполнение с Sonnet
- **Enterprise Automation**: Claude Cowork для офисных задач, плагины, scheduled workflows
- **Long-Horizon Agents**: 1M токенов контекст, durable execution, approvals
- **Computer Use**: UI-автоматизация, тестирование, scraping
- **Research & Analysis**: Extended thinking для сложных аналитических задач

## Отзывы и критика

### Сильные стороны:
- Лучшая в индустрии модель для coding (Opus 4.8 на SWE-bench Pro 69.2%)
- Claude Code — золотой стандарт coding agents
- 90% скидка на prompt caching (выше, чем у [OpenAI](openai.md))
- Самый сильный контекст: 1M токенов с высоким retrieval quality (78.3% на MRCR v2)
- Cowork — первый enterprise-grade AI-агент для non-developers

### Слабые стороны:
- Самые высокие цены среди frontier-провайдеров (Opus $25/MTok output)
- Закрытые модели — нельзя self-host
- Extended thinking увеличивает стоимость и latency
- Конкуренция со стороны open-weight моделей ([GLM-5.2](../platforms/z-ai.md), [DeepSeek](deepseek.md) V4) растёт

## Связи

- [[gemini.md|Google Gemini]] — прямой конкурент по моделям и агентным возможностям
- [[perplexity.md|Perplexity AI]] — альтернативная AI-платформа
- [[../platforms/openai.md|OpenAI]] — главный конкурент
- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — Claude Code как реализация coding harness
- [[../../patterns/implementation/working-with-coding-agents.md|Работа с код-агентами]] — практический workflow с Claude Code
- [[../agent-frameworks-research.md|Исследование фреймворков]] — Claude Code в карте выбора
- [[../agent-model-map.md|Модельная карта]] — Claude модели в карте

*Добавлено: 2026-06-29*
