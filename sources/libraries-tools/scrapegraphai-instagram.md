---
title: ScrapeGraphAI — easy.ai.life Instagram Reel
url: https://www.instagram.com/easy.ai.life/
type: url
category: sources
tags: [scrapegraphai, web-scraping, llm-extraction, instagram]
added: 2026-07-26
status: used
---

# ScrapeGraphAI — easy.ai.life Instagram Reel

Скриншот Instagram Reel от `easy.ai.life`, переданный пользователем как `IMG_2458.PNG`. Видимая формулировка описывает ScrapeGraphAI как «бесплатную нейросеть для парсинга любых …».

Точный permalink ролика в скриншоте отсутствует, поэтому `url` ведёт на профиль автора. Технические и коммерческие утверждения дополнительно проверены по репозиторию, документации API и live pricing продукта.

## Что подтвердилось

- ScrapeGraphAI действительно предоставляет open-source Python-фреймворк под MIT для LLM-based extraction из веб-страниц и локальных HTML, XML, JSON и Markdown.
- Self-hosted библиотека использует собственную LLM-конфигурацию и Playwright; поддерживаются API-модели и локальные модели через Ollama.
- Отдельный managed API предоставляет `scrape`, `extract`, `search`, `crawl`, `monitor` и `history`.
- Hosted API использует credit-based billing; free plan на дату проверки содержит 500 разовых, а не ежемесячных кредитов.

## Что требует оговорки

- «Бесплатный» относится к лицензии open-source кода. Пользователь оплачивает или обслуживает LLM, браузеры, proxies, compute и масштабирование; managed API является платным после стартового лимита.
- «Для любых сайтов» не является гарантией: остаются авторизация, anti-bot, CAPTCHA, JavaScript, rate limits, robots/TOS и изменения DOM.
- LLM extraction недетерминирована. Результат требует schema validation, evidence/provenance и eval-набора на целевых страницах.
- Open-source пакет собирает usage telemetry; README документирует opt-out через `SCRAPEGRAPHAI_TELEMETRY_ENABLED=false`.

## Источники проверки

- [Open-source repository](https://github.com/ScrapeGraphAI/Scrapegraph-ai) — архитектура, MIT license, model/browser configuration, telemetry и граница self-hosted/managed.
- [ScrapeGraphAI API v2](https://docs.scrapegraphai.com/api-reference/introduction) — актуальные endpoints и deprecation v1.
- [ScrapeGraphAI pricing](https://scrapegraphai.com/) — live plans, credits и rate limits на дату проверки.

## Интеграция в базу

Факты о продукте перенесены в [canonical-заметку ScrapeGraphAI](../../tools/agent-tools/scrapegraphai.md). Архитектурное место LLM extraction зафиксировано в [автоматизации сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md).

## Статус

Добавлено и интегрировано: 2026-07-26.
