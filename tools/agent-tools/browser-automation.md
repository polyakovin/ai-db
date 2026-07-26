---
title: Browser Automation for Agents
url: https://github.com/browser-use/browser-use
type: url
category: tools
tags: [browser, automation, playwright, agents, tools]
added: 2026-07-01
status: verified
---

# Browser Automation for Agents

Инструменты для управления браузером в AI-агентах — автоматизация веб-взаимодействий: навигация, клики, заполнение форм, скриншоты, извлечение данных.

## Обзор

Браузерная автоматизация позволяет агентам выполнять задачи, требующие взаимодействия с веб-сайтами:

- **Web scraping** — извлечение данных с динамических страниц
- **Form filling** — автоматическое заполнение форм
- **Navigation** — переходы по ссылкам, back/forward, history
- **Authentication** — login/logout, session management
- **Visual verification** — скриншоты, visual regression
- **Multi-step workflows** — checkout, booking, data entry

## Ключевые инструменты

### Browser-use

| Параметр | Значение |
|----------|----------|
| **URL** | https://browser-use.com/ |
| **GitHub** | https://github.com/browser-use/browser-use |
| **API** | Python SDK |
| **Модели** | Model-agnostic (OpenAI, Anthropic, Ollama, etc.) |
| **Цены** | Open Source (MIT) |
| **Open Source** | Да |

**Возможности:**
- LLM-powered browser control (агент сам решает, куда кликать)
- Built on Playwright — поддержка Chrome, Firefox, Safari
- Natural language commands: "найди cheapest flights to Tokyo"
- Self-correcting — агент видит ошибки и исправляется
- Screenshot + DOM state для контекста LLM
- Интеграция с [LangChain](../frameworks/langchain.md), [LlamaIndex](../frameworks/llamaindex.md)

**Пример использования:**
```python
from browser_use import Agent

agent = Agent(
    task="Find cheapest flight from NYC to London in March",
    llm=model,
    browser_context=context
)
result = await agent.run()
```

### Playwright

| Параметр | Значение |
|----------|----------|
| **URL** | https://playwright.dev/ |
| **GitHub** | https://github.com/microsoft/playwright |
| **API** | Python, JS/TS, Java, .NET |
| **Модели** | N/A (browser automation library) |
| **Цены** | Open Source (Apache 2.0) |
| **Open Source** | Да |

**Возможности:**
- Кросс-браузер: Chromium, Firefox, WebKit
- Кросс-платформенный: Windows, Linux, macOS
- Headless и headful режимы
- Mobile emulation (iOS, Android)
- Network interception, geolocation, permissions
- Auto-wait, smart assertions
- Trace viewer для debugging

**Пример (Python):**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    page.click("button#submit")
    browser.close()
```

### Puppeteer

| Параметр | Значение |
|----------|----------|
| **URL** | https://pptr.dev/ |
| **GitHub** | https://github.com/puppeteer/puppeteer |
| **API** | Node.js, Python (pyppeteer) |
| **Модели** | N/A |
| **Цены** | Open Source (Apache 2.0) |
| **Open Source** | Да |

**Возможности:**
- Chrome/Chromium automation
- Screenshot, PDF generation
- Performance profiling
- Keyboard/mouse events
- Custom user agents

### Selenium

| Параметр | Значение |
|----------|----------|
| **URL** | https://www.selenium.dev/ |
| **GitHub** | https://github.com/SeleniumHQ/selenium |
| **API** | Python, Java, C#, Ruby, JS |
| **Модели** | N/A |
| **Цены** | Open Source (Apache 2.0) |
| **Open Source** | Да |

**Возможности:**
- Старейший инструмент браузерной автоматизации
- Поддержка всех основных браузеров
- WebDriver protocol стандарт
- Grid для распределённого тестирования
- Rich ecosystem и документация

**Недостатки:**
- Медленнее Playwright/Puppeteer
- Менее стабильный (flaky tests)
- Нет современных фич (auto-wait, trace viewer)

### crawl4ai

| Параметр | Значение |
|----------|----------|
| **URL** | https://github.com/unclecode/crawl4ai |
| **GitHub** | https://github.com/unclecode/crawl4ai |
| **API** | Python SDK |
| **Модели** | LLM-powered extraction |
| **Цены** | Open Source (Apache 2.0) |
| **Open Source** | Да |

**Возможности:**
- AI-powered web crawler для LLM
- JavaScript rendering (headless browser)
- LLM-based content extraction
- Markdown output
- Custom hooks для preprocessing
- Optimized для RAG и agent workflows

## CDP, stealth и anti-detection

Stealth-инструменты не образуют отдельный обязательный слой browser automation. Их следует рассматривать как специализированные реализации для собственных систем, тестовых стендов или сайтов, где автоматизация явно разрешена.

### Chrome DevTools Protocol

[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) позволяет инструментам инспектировать, отлаживать, профилировать и управлять Chromium. Сам CDP не является «скрытым управлением»: stealth-свойства возникают из поведения конкретного клиента, изменений browser fingerprint и способа генерации событий.

### SeleniumBase

[SeleniumBase UC Mode](https://seleniumbase.github.io/help_docs/uc_mode/) расширяет Selenium anti-detection методами, а [CDP Mode](https://seleniumbase.github.io/examples/cdp_mode/ReadMe/) может управлять браузером без WebDriver и предоставляет CAPTCHA helpers. Это не гарантия прохождения защиты: результат зависит от сайта, режима запуска, browser build, сети и изменений anti-bot provider.

### CloakBrowser

[CloakBrowser](https://github.com/CloakHQ/CloakBrowser) — patched Chromium с Playwright/Puppeteer-compatible wrapper и изменениями fingerprint на уровне browser source. На 2026-07-26:

- wrapper code опубликован под MIT, а готовый Chromium binary имеет отдельную лицензию без права redistribution;
- проект публикует signatures/attestations для проверки binary artifacts;
- заявления о прохождении detection tests являются self-reported benchmark проекта;
- документация прямо признаёт, что detection остаётся arms race и будущая обнаруживаемость возможна.

Для базового automation stack предпочтительнее обычный Playwright с rate limits, стабильными selectors, traces и разрешённым доступом. Stealth browser повышает supply-chain и maintenance surface и не заменяет authorization, robots/TOS policy или обработку блокировок.

## Когда использовать

| Сценарий | Рекомендуемый инструмент |
|----------|-------------------------|
| **LLM-controlled browser** | Browser-use (агент сам управляет) |
| **Scripted automation** | Playwright (надёжно, быстро) |
| **Chrome-only tasks** | Puppeteer (легковесный) |
| **Legacy integration** | Selenium (широкая поддержка) |
| **LLM content extraction** | crawl4ai (AI-powered crawler) |
| **Visual testing** | Playwright (trace viewer, screenshots) |

## Интеграция с агентами

### Browser-use + LLM
```python
from browser_use import Agent, Controller
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")
agent = Agent(
    task="Book a table at Italian restaurant for 2 at 7pm",
    llm=llm,
    controller=Controller()
)
result = await agent.run()
```

### Playwright + LangChain Tool
```python
from langchain.tools import tool
from playwright.async_api import async_playwright

@tool
async def scrape_website(url: str) -> str:
    """Scrape website content"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        content = await page.content()
        await browser.close()
        return content
```

## Безопасность и ограничения

- **Sandbox escape** — браузер может выполнять произвольный JS
- **Session hijacking** — защита cookies и tokens
- **Rate limiting** — сайты блокируют aggressive scraping
- **CAPTCHA** — многие сайты используют bot detection
- **Legal compliance** — проверка robots.txt, ToS
- **Resource usage** — браузеры потребляют много памяти/CPU
- **Anti-detection arms race** — stealth-патчи могут перестать работать после обновления browser или защиты
- **Binary supply chain** — сторонние Chromium builds нужно pin-ить и проверять signatures/attestations

## Связи

- [Web Search](web-search.md) — альтернатива для статичного контента
- [Code Execution](code-execution.md) — запуск browser scripts в sandbox
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — интеграция browser tools
- [Function Calling](function-calling.md) — механизм вызова browser actions
- [Web scraping stack — harsh.times Instagram Reel](../../sources/libraries-tools/web-scraping-stack-instagram.md) — provenance разбора CDP, SeleniumBase и CloakBrowser

---

*Добавлено: 2026-07-01. Обновлено: 2026-07-26.*
