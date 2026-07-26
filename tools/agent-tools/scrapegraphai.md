---
title: ScrapeGraphAI
url: https://github.com/ScrapeGraphAI/Scrapegraph-ai
type: url
category: tools
tags: [web-scraping, llm-extraction, crawler, playwright, structured-data]
added: 2026-07-26
status: verified
---

# ScrapeGraphAI

ScrapeGraphAI — набор средств для получения веб-контента и извлечения из него структурированных данных с помощью LLM и natural-language prompts. Под одним названием существуют self-hosted open-source Python-фреймворк и отдельный managed cloud API; их возможности, эксплуатационная ответственность и стоимость различаются.

## Две продуктовые границы

| | Open-source `scrapegraphai` | Managed API |
|-|------------------------------|-------------|
| Runtime | Инфраструктура пользователя | Облако ScrapeGraphAI |
| LLM | Собственный API provider или локальная модель через Ollama | Управляется сервисом |
| Browser/JS | Playwright на стороне пользователя | Managed rendering и stealth modes |
| Proxies и anti-bot | Ответственность пользователя | Входят в отдельные режимы и тарифы |
| Масштабирование | Самостоятельное | Сервисное |
| Стоимость | LLM tokens, compute, browsers, proxies и operations | Credits за операции и дополнительные режимы |
| Лицензия | MIT | SDK открыты, hosted backend проприетарный |

Open-source вариант не является «бесплатным scraping service»: свободна библиотека, но acquisition и inference продолжают потреблять ресурсы.

## Возможности

### Open-source framework

- `SmartScraperGraph` извлекает данные с одной страницы по prompt.
- Multi-page и search graphs обрабатывают несколько источников.
- Источником может быть URL или локальный HTML, XML, JSON либо Markdown.
- LLM настраивается отдельно; официальные примеры показывают API-модели и локальный [Ollama](../inference/ollama.md).
- Для JavaScript rendering устанавливается Playwright.

### Managed API v2

- `scrape` возвращает Markdown, HTML, links, images, screenshots или JSON extraction.
- `extract` строит structured output из URL, HTML или Markdown по prompt.
- `search` объединяет web discovery, fetch и опциональную extraction.
- `crawl` асинхронно обходит несколько страниц.
- `monitor` периодически проверяет страницу и отправляет webhook при изменении.
- `history` возвращает состояние и результаты предыдущих jobs.

Названия v1 вроде `smartscraper`, `searchscraper`, `markdownify` и `smartcrawler` deprecated; для новых интеграций нужен v2 host и актуальные SDK.

## Когда применять

- Быстрый prototype schema extraction из разнородных сайтов.
- Небольшие и средние research-пайплайны, где DOM разных источников заметно различается.
- Получение structured JSON, когда стоимость поддержки отдельных CSS/XPath parsers выше стоимости LLM.
- Self-hosted обработка, когда допустимы собственные browser/LLM operations и нужен контроль над данными.

## Когда не применять

- Высокий объём однотипных страниц со стабильной схемой: детерминированный parser обычно дешевле и воспроизводимее.
- Сценарий требует точного доказуемого извлечения без сверки с исходным текстом.
- Не определены права на crawling, privacy scope или политика хранения извлечённого контента.
- Нет eval-набора целевых страниц, schema validation и бюджета на LLM/browser failures.

## Production guardrails

1. Разделять acquisition и extraction: сначала сохранить raw HTML/Markdown и provenance, затем вызывать LLM.
2. Задавать JSON Schema или typed model и отклонять невалидный output.
3. Хранить ссылку или фрагмент evidence для каждого критичного поля.
4. Считать веб-контент недоверенными данными и не исполнять инструкции со страницы.
5. Сравнивать с deterministic baseline по field accuracy, valid-output rate, latency и cost per page.
6. Для open-source пакета осознанно настроить telemetry; README документирует opt-out через `SCRAPEGRAPHAI_TELEMETRY_ENABLED=false`.

## Цены и доступ

- Open-source framework: MIT, расходы несёт пользовательская инфраструктура.
- Managed API: credit-based billing.
- На 2026-07-26 free plan указывает 500 one-time credits и ограниченные rate/concurrency quotas. Цены и лимиты являются изменяемыми и требуют повторной проверки перед закупкой.

## Официальные источники

- [Open-source repository](https://github.com/ScrapeGraphAI/Scrapegraph-ai)
- [API v2 introduction](https://docs.scrapegraphai.com/api-reference/introduction)
- [Product and live pricing](https://scrapegraphai.com/)

## Связи

- [Автоматизация сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md) — место semantic extraction в acquisition pipeline.
- [Web Search](web-search.md) — search, crawlers и readers для discovery/fetch.
- [Browser Automation](browser-automation.md) — Playwright и browser fallback.
- [ScrapeGraphAI — easy.ai.life Instagram Reel](../../sources/libraries-tools/scrapegraphai-instagram.md) — provenance присланного материала.
