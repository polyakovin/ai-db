---
title: DeerFlow
url: https://deerflow.tech/en/docs
type: url
category: tools
tags: [framework, harness, agents, long-horizon, multi-agent, sandbox, skills, memory, python, open-source]
added: 2026-07-23
status: verified
---

# DeerFlow

DeerFlow — open-source harness для long-horizon AI-агентов из репозитория ByteDance. Версия 2.x объединяет переиспользуемый Python SDK/runtime и готовое reference-приложение: lead agent планирует работу, вызывает инструменты, делегирует подзадачи, использует sandbox и возвращает проверяемые артефакты.

DeerFlow 2.0 — полная переработка проекта без общего кода с исходной веткой 1.x. Ветка 1.x сохраняет прежний deep-research framework, а активная ветка 2.x развивает универсальный agent harness поверх [LangGraph](langgraph.md) и [LangChain](langchain.md).

## Два слоя

| Слой | Роль |
|---|---|
| **DeerFlow Harness** | Python SDK и runtime для собственных agent systems: lead agent, middleware, tools, skills, sandbox, memory, subagents и context management |
| **DeerFlow App** | Готовое self-hosted приложение поверх Harness: web workspace, threads, agents, authentication, Gateway API, TUI, scheduled tasks и messaging channels |

Harness подходит для встраивания в собственный продукт. App — для запуска готового рабочего пространства и как reference-реализация production-обвязки.

## Архитектура

| Компонент | Реализация |
|---|---|
| Lead Agent | Центральный агент с tool routing; поведение собирается цепочкой middleware |
| Orchestration | [LangGraph](langgraph.md) обеспечивает stateful runtime, checkpoints и threads; [LangChain](langchain.md) — model/tool integrations |
| Skills | Пакеты с `SKILL.md`, инструкциями и ресурсами; содержимое загружается по запросу, поддерживаются `allowed-tools` |
| Tools и MCP | Встроенные filesystem/shell/web tools, отложенное раскрытие схем и подключаемые MCP servers |
| Sandbox | LocalSandbox, контейнерный AIO Sandbox или отдельный Kubernetes Pod через provisioner |
| Subagents | Изолированный контекст, параллельное выполнение и отдельные лимиты времени/turns |
| Memory | Структурированные summary и facts между сессиями, раздельные области памяти пользователей и custom agents |
| Context management | Summarization, ручная compaction, scoped context подагентов и filesystem как внешняя рабочая память |
| Artifacts | Файлы, отчёты, код, графики, web pages и другие результаты в thread-scoped workspace |
| Operations | LangSmith/Langfuse/Monocle tracing, audit middleware, SQLite/PostgreSQL storage и scheduled tasks |

## Ключевые возможности

- **Long-horizon execution** — планирование и повторяющийся agent loop для задач от минут до часов.
- **Progressive skills** — research, data analysis, slides, web pages, image/video generation и собственные skills подгружаются только при необходимости.
- **Delegation** — встроенные general-purpose и bash subagents; custom agents также можно использовать как workers.
- **Model portability** — конфигурация через LangChain providers, OpenAI-compatible endpoints, Responses API и vLLM.
- **Несколько интерфейсов** — web application, Gateway API, embedded `DeerFlowClient`, terminal workbench и messaging channels.
- **Session goals** — thread-scoped критерий завершения с автоматическими продолжениями, typed blockers и no-progress breaker.
- **Stateful workspace** — threads, загруженные файлы, outputs, memory и checkpoints сохраняются между запусками.
- **Extensibility** — skills, tools, MCP servers, middleware, custom agents, sandbox providers и storage backends.

## Когда применять

| Сценарий | Почему DeerFlow |
|---|---|
| Self-hosted general-purpose agent | Уже есть runtime, UI, workspace, memory, tools и deployment path |
| Deep research с артефактами | Web tools, files, subagents, context compaction и report-oriented skills |
| Data analysis и content workflows | Sandbox позволяет запускать код и собирать файлы, графики, slides и web artifacts |
| Собственный long-horizon agent product | Harness можно встроить как Python SDK без полного web stack |
| Эксперименты с agent harness | Компоненты собраны в наблюдаемую middleware-архитектуру и доступны в исходном коде |

## Когда не применять

- Нужен небольшой типизированный Python agent loop без UI, memory и sandbox — [Pydantic AI](pydantic-ai.md) даст меньшую operational surface.
- Нужен полностью явный deterministic graph/state machine — используйте [LangGraph](langgraph.md) напрямую и проектируйте nodes, edges и side effects.
- Нужен визуальный low-code builder для быстрого demo — [Dify](dify.md) или [Langflow](langflow.md) проще для non-engineering команды.
- Нельзя безопасно изолировать выполнение команд и файлов — capabilities DeerFlow будут слишком привилегированными для такого окружения.
- Нужен managed SaaS без self-hosting и эксплуатации — self-hosted App потребует управления моделями, storage, authentication, sandbox и обновлениями.

## Установка и deployment

- Рекомендуемый старт из репозитория: setup wizard `make setup`, диагностика `make doctor`.
- Backend требует Python 3.12 или новее; полный App также использует frontend на TypeScript/Next.js.
- Доступны local development, Docker Compose и production-вариант с Kubernetes-managed sandboxes.
- Для воспроизводимого production deployment следует закреплять Git tag или commit: tagged release и активная ветка `main` могут расходиться.
- Inference не входит в лицензию или runtime: нужны credentials выбранного LLM provider либо собственный совместимый endpoint.
- Для сложных задач проект рекомендует модели с большим контекстом, reasoning и надёжным tool calling.

## Версии и Open Source статус

- **Лицензия:** MIT.
- **Последний GitHub release на 2026-07-23:** `v2.0.0`, опубликован 2026-06-25.
- **Активная разработка:** package metadata ветки `main` уже указывает `2.1.0`, поэтому возможности документации и `main` могут опережать последний tag.
- **Legacy:** исходный deep-research код поддерживается отдельно в ветке 1.x; 2.x не является backward-compatible обновлением.

## Безопасность

- `LocalSandboxProvider` выполняет файловые операции на host и **не даёт контейнерной изоляции**. Shell по умолчанию отключён, но file tools всё равно сохраняют доступ к разрешённой рабочей области.
- **CVE-2026-34430:** версии до commit `92c7a20` позволяли обойти regex-защиту bash tool и выйти за границы LocalSandbox с выполнением команд на host. Используйте commit `92c7a20` или более новый и не считайте локальный provider security boundary.
- Для multi-user и untrusted deployments нужен контейнерный sandbox; для production проект рекомендует отдельные Kubernetes Pods через provisioner.
- Публичный deployment требует authentication, сильного secret, network isolation/allowlist, TLS/reverse proxy и минимальных mounts.
- Skills, MCP tools, model prompts, uploads и generated commands образуют единую trust boundary; разрешения нужно ограничивать на уровне tool policy и sandbox.
- Tracing может сохранять prompts, tool arguments и model responses целиком, поэтому remote exporters следует считать внешним получателем данных.
- Перед обновлением persistent deployment нужны backup и проверка migrations; ветка 2.x активно меняется.

## Сильные стороны и ограничения

**Сильные стороны:** полноценный open-source harness вместо набора разрозненных библиотек; единая модель SDK + reference App; skills с progressive loading; subagents и context isolation; несколько sandbox modes; memory, artifacts, tracing и deployment guidance из коробки.

**Ограничения:** большая operational surface; безопасность зависит от выбранного sandbox и конфигурации; качество и стоимость long-horizon runs зависят от модели; `main` развивается быстрее tagged releases; сравнительные независимые benchmarks качества Harness в проверенных материалах не представлены.

## Связи

- [Официальные материалы DeerFlow](../../sources/libraries-tools/deerflow-docs.md) — provenance для этой страницы
- [LangGraph](langgraph.md) — stateful orchestration runtime в основе DeerFlow
- [LangChain](langchain.md) — model и tool integrations
- [Исследование фреймворков](../agent-frameworks-research.md) — место DeerFlow в карте выбора
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — архитектурный слой, который реализует DeerFlow
- [Progressive disclosure](../../patterns/implementation/progressive-disclosure-for-agents.md) — загрузка skills и deferred tool schemas по запросу
- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) — lead agent и subagents
- [Безопасность агентных систем](../../patterns/architecture-design/agent-security.md) — sandbox, permissions и trust boundaries

*Добавлено: 2026-07-23*
