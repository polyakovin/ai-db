---
title: Omi — официальный сайт, документация и репозиторий
url: https://omi.me/
type: url
category: sources
tags: [omi, personal-ai, wearable, transcription, memory, open-source]
added: 2026-07-26
status: used
---

# Omi — официальный сайт, документация и репозиторий

Набор первичных источников о платформе Omi: носимых устройствах, приложениях, conversation memory, developer-интерфейсах, открытом коде и правилах обработки данных.

## Проверенные материалы

- **Website:** https://omi.me/
- **Product overview:** https://help.omi.me/en/articles/13135007-overview
- **Documentation introduction:** https://docs.omi.me/doc/get_started/introduction
- **GitHub repository:** https://github.com/BasedHardware/omi
- **Developer API:** https://docs.omi.me/doc/developer/api/overview
- **Omi Apps:** https://docs.omi.me/doc/developer/apps/Introduction
- **Integration Apps and webhooks:** https://docs.omi.me/doc/developer/apps/Integrations
- **MCP:** https://docs.omi.me/doc/developer/mcp/introduction
- **CLI:** https://docs.omi.me/doc/developer/cli/introduction
- **Privacy Policy:** https://help.omi.me/en/articles/13162549-omi-privacy-policy
- **Terms and recording laws:** https://www.omi.me/pages/terms-of-service

## Что подтверждено

- Omi работает через mobile, desktop и web apps; wearable hardware для базового сценария не обязателен.
- Платформа превращает разговоры в transcripts, summaries, memories и action items и предоставляет chat поверх накопленного контекста.
- Расширения получают доступ через prompt-based apps, webhooks, Developer API, MCP, CLI и SDK.
- Monorepo включает hardware/firmware, приложения, backend и SDK и опубликован под MIT License.
- Официально поддерживаются hosted cloud и self-hosted deployment.
- Согласно текущей privacy policy, structured conversation data хранится в backend, а raw audio после непосредственной обработки не сохраняется, кроме опционального voice sample.
- Terms возлагают на пользователя обязанность соблюдать применимые recording, wiretap, privacy и consent laws.

Устойчивые сведения перенесены в [canonical-заметку Omi](../../tools/platforms/omi.md).

## Практическая ценность для ai-db

Omi показывает полный wearable-to-agent контур: постоянный capture становится структурированным context store, а API, MCP и event-driven webhooks превращают память в доступный для агентов tool surface. Одновременно платформа подчёркивает, что ambient AI требует явного управления consent, retention, scopes и сторонними получателями данных.

## Ограничения источников

- Все проверенные материалы принадлежат Omi; они подтверждают заявленную архитектуру и интерфейсы, но не точность transcription, качество summaries или надёжность hardware.
- MIT License относится к содержимому открытого репозитория; условия управляемого cloud-сервиса и продаваемых устройств регулируются отдельно.
- Pricing, usage limits, battery life, integrations и продуктовая комплектация меняются, поэтому числовые значения не перенесены в canonical-заметку.
- Наличие self-hosted backend не доказывает полностью локальную обработку: конкретный deployment нужно проверять на обращения к STT, LLM, vector storage и telemetry providers.
- Правила записи разговоров зависят от юрисдикции и организационной policy; product documentation не заменяет юридическую проверку.

## Связи

- [Omi](../../tools/platforms/omi.md) — canonical-страница платформы.
- [Персистентная память агента](../../patterns/advanced/agent-memory-patterns.md) — память и lifecycle извлечённых фактов.
- [Data governance и compliance](../../patterns/architecture-design/data-governance-compliance.md) — consent, retention, access и third-party sharing.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — developer surfaces для agent integrations.

## Статус

Добавлено и интегрировано: 2026-07-26.
