---
title: Web scraping stack — harsh.times Instagram Reel
url: https://www.instagram.com/harsh.times/
type: url
category: sources
tags: [web-scraping, browser-automation, anti-bot, python, instagram]
added: 2026-07-26
status: used
---

# Web scraping stack — harsh.times Instagram Reel

Скриншот Instagram Reel от `harsh.times`, переданный пользователем как `IMG_2301.PNG`. В ролике девять технологий представлены как единый конвейер для поиска, скрытого сбора, параллельной обработки и экспорта веб-данных.

Точный permalink ролика в скриншоте отсутствует, поэтому `url` ведёт на профиль автора. Это ограничивает воспроизводимость provenance: содержание ниже зафиксировано по присланному изображению, а технические утверждения проверены по официальной документации.

## Утверждения из материала

| Элемент | Формулировка ролика | Результат проверки |
|---------|---------------------|--------------------|
| RSS | быстрый поиск постов | Подходит для инкрементального получения публикаций из доступных feeds, но не является универсальным поиском |
| CloakBrowser | подмена цифрового отпечатка | Проект патчит Chromium и browser fingerprint; его benchmark-заявления принадлежат самому проекту |
| SeleniumBase | автоматическое решение капч | UC/CDP modes содержат anti-detection и CAPTCHA helpers, но не гарантируют прохождение защиты |
| CDP | скрытое управление браузером | CDP — штатный протокол управления и инспекции Chromium; stealth появляется только в дополнительных реализациях |
| curl_cffi | имитация сетевого отпечатка | Поддерживает browser-like TLS/HTTP2/HTTP3 fingerprints; не подменяет IP и JavaScript fingerprint |
| asyncio | запуск тысяч потоков | Планирует корутины и tasks, а не тысячи OS threads; concurrency должна быть ограничена |
| Redis | хранение сессионных cookies | Возможен как краткоживущий session/cache store с TTL, ACL и TLS; cookies нужно считать секретами |
| JSON | скоростная фильтрация данных | JSON — формат данных; фильтрацию и schema validation выполняет код или специализированные библиотеки |
| openpyxl | создание финальных таблиц | Подходит для XLSX-экспорта, но не заменяет основное хранилище больших наборов данных |

## Источники проверки

- [CloakBrowser repository](https://github.com/CloakHQ/CloakBrowser) — архитектура, лицензирование wrapper/binary и ограничения anti-detection.
- [SeleniumBase UC Mode](https://seleniumbase.github.io/help_docs/uc_mode/) и [CDP Mode](https://seleniumbase.github.io/examples/cdp_mode/ReadMe/) — режимы anti-detection и CAPTCHA helpers.
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) — назначение CDP.
- [curl_cffi documentation](https://curl-cffi.readthedocs.io/en/stable/) — fingerprints, async API, HTTP/2, HTTP/3 и proxies.
- [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) — корутины, tasks и cooperative scheduling.
- [Redis security](https://redis.io/docs/latest/operate/oss_and_stack/management/security/) — trusted environment, ACL и TLS.
- [openpyxl documentation](https://openpyxl.readthedocs.io/en/stable/tutorial.html) — чтение и запись XLSX.

## Интеграция в базу

Материал полезен не как готовый stack, а как пример смешения независимых слоёв: discovery, transport, browser automation, concurrency, session state, data format и export. Устойчивые выводы перенесены в:

- [Автоматизацию сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md) — правильная декомпозиция pipeline.
- [Browser Automation](../../tools/agent-tools/browser-automation.md) — CDP, SeleniumBase, CloakBrowser и границы stealth-подходов.
- [API Clients](../../tools/agent-tools/api-clients.md) — место curl_cffi среди HTTP-клиентов.

## Статус

Добавлено и интегрировано: 2026-07-26.
