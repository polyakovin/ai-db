---
title: Omi
url: https://omi.me/
type: url
category: tools
tags: [personal-ai, wearable, transcription, memory, open-source, integrations]
added: 2026-07-26
status: verified
---

# Omi

Omi — open-source платформа персонального AI для захвата разговоров и экранного контекста с телефона, компьютера или носимого устройства. Она расшифровывает поток, формирует summaries и action items, сохраняет поисковую память и даёт chat-интерфейс поверх накопленного контекста.

Носимый pendant — один из способов ввода, а не обязательное условие: мобильное и desktop-приложения можно использовать без отдельного устройства.

## Архитектурная роль

Omi закрывает контур `capture → transcription → structured conversation → memory/action items → retrieval/action`. Это не провайдер фундаментальной модели и не универсальный agent runtime, а слой персонального контекста и интеграций, который можно подключать к другим приложениям и AI-ассистентам.

| Слой | Что входит |
|---|---|
| **Capture** | Omi wearable, Omi Glass, мобильное и desktop-приложения |
| **Processing** | live transcription, разделение реплик, summaries, action items и события |
| **Memory** | разговоры, извлечённые факты, семантический поиск и персонализированный chat |
| **Extensions** | Omi Apps, Developer API, MCP, CLI, SDK и webhooks |

## Developer-интерфейсы

- **Developer API** предоставляет scoped-доступ к memories, conversations, folders и action items.
- **MCP server** позволяет совместимому AI-ассистенту читать и изменять данные Omi через tools.
- **CLI** даёт JSON-friendly команды для shell scripts, CI и [agent harness](../../patterns/architecture-design/agent-harness.md).
- **Omi Apps** поддерживают prompt-based расширения и серверные integrations.
- **Webhooks** могут получать созданные memories, real-time transcript и raw audio; chat tools позволяют расширениям выполнять внешние действия.

API keys следует разделять по интеграциям и выдавать им минимальные scopes. Подключение app или webhook расширяет data boundary: внешний сервис может получить полный transcript, summary, action items и metadata.

## Open Source и развёртывание

Официальный monorepo опубликован под MIT License и включает hardware/firmware, мобильное и desktop-приложения, backend и SDK. Можно использовать управляемое облако Omi или разворачивать собственный backend.

Self-hosting даёт больше контроля, но не делает обработку автоматически локальной: нужно отдельно проверить настройки speech-to-text, LLM, vector storage, authentication и telemetry, а также полный маршрут данных до внешних провайдеров.

## Приватность и правовые ограничения

По действующей privacy policy облачный сервис хранит transcripts, summaries, metadata, memories и tasks. Raw audio заявлен как поток для непосредственной обработки без дальнейшего хранения; исключение — опциональный speech sample для распознавания голоса. Эти условия нужно перепроверять перед загрузкой чувствительных данных.

Постоянная запись затрагивает не только владельца устройства, но и собеседников. Пользователь отвечает за необходимые уведомления и согласия по законам своей юрисдикции. Для корпоративного применения дополнительно нужны retention policy, access review, правила удаления и оценка каждого установленного integration app.

## Когда рассматривать

Omi подходит для:

- автоматической фиксации встреч и разговоров;
- извлечения решений, задач и событий;
- поиска по персональной истории и контекстных напоминаний;
- построения voice-first integrations и персональных агентов поверх API, MCP или webhooks;
- экспериментов с открытым wearable-to-agent stack.

Платформа не подходит для незаметной записи людей, emergency-сценариев или среды со строгим on-prem требованием, пока локальный deployment и все внешние зависимости не проверены end-to-end.

## Доступ

Начать можно с mobile, desktop или web app без покупки hardware. У hosted-сервиса есть ограниченный и платный usage tiers, а устройства продаются отдельно; актуальные лимиты, цены и региональную доступность нужно проверять на сайте и в приложении.

## Связи

- [Персистентная память агента](../../patterns/advanced/agent-memory-patterns.md) — извлечение, хранение и управление долговременными фактами.
- [Data governance и compliance](../../patterns/architecture-design/data-governance-compliance.md) — consent, retention, access и удаление разговорных данных.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — подключение Omi к внешним AI-ассистентам и agent workflows.
- [Omi — официальные материалы](../../sources/libraries-tools/omi.md) — provenance и границы верификации.

*Проверено: 2026-07-26*
