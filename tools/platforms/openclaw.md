---
title: OpenClaw
url: https://openclaw.ai/
type: url
category: tools
tags: [personal-agent, self-hosted, gateway, skills, memory, automation]
added: 2026-07-26
status: verified
---

# OpenClaw

OpenClaw (ранее Clawdbot и Moltbot) — open-source local-first control plane для персонального AI-ассистента. Self-hosted gateway соединяет мессенджеры с моделью, stateful sessions, memory, tools и skills, поэтому агент может оставаться доступным и выполнять автоматизацию независимо от пользовательского ноутбука.

## Архитектурная роль

- **Gateway** поддерживает каналы и удалённый доступ к агенту.
- **Agent runtime** выбирает модель, ведёт сессию и вызывает инструменты.
- **Tools и skills** дают browser, web, shell, filesystem и интеграции.
- **Memory** сохраняет контекст между сессиями.
- **Sandbox backends** изолируют выполнение команд и работу с файлами.

OpenClaw — orchestration layer, а не одна конкретная LLM: модель и провайдер выбираются отдельно.

## Подходящие задачи

Практичный критерий из hands-on обзора: задача подходит OpenClaw, если её можно описать одним сообщением, заранее задать границы и затем оценить готовый outcome. Типичные сценарии — briefings, reminders, агрегация данных, расписания, triage и messaging-first автоматизация.

Задачи с постоянным визуальным контролем, частыми итерациями и review каждого промежуточного шага лучше выполнять в специализированном интерактивном инструменте или разбивать на этапы с approvals.

## Эксплуатация и безопасность

Always-on агент объединяет untrusted messages, web content, долговременную память и инструменты с side effects. Минимальный baseline:

1. Запускать на изолированном host или sandbox под непривилегированным пользователем.
2. Выдавать только необходимые tool permissions и отдельные scoped credentials.
3. Требовать preview/approval для внешних сообщений, платежей, удаления и изменения production.
4. Ограничивать токены, деньги, время и количество tool calls; останавливать runaway loops.
5. Проверять источник и содержимое skills, даже если registry показывает результаты автоматического scan.
6. Регулярно обновлять runtime и выполнять security audit.
7. Не трактовать вопрос о функции как разрешение установить, изменить или запустить её.

## Связи

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — gateway, tools, memory, skills и sandbox как части harness.
- [Безопасность агентных систем](../../patterns/architecture-design/agent-security.md) — least privilege, budgets и trust boundaries.
- [Human-in-the-loop UX](../../patterns/production-operations/human-in-the-loop-ux.md) — intent/action boundary и approvals.
- [Персистентная память агента](../../patterns/advanced/agent-memory-patterns.md) — memory как управляемое состояние.
- [Практический гайд по OpenClaw на Habr](../../sources/tutorials-courses/openclaw-habr-guide.md) — provenance hands-on выводов.
