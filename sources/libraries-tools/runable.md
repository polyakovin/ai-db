---
title: Runable
url: https://runable.com/
type: url
category: sources
tags: [ai-agent, artifacts, sandbox, skills, memory, no-code]
added: 2026-07-20
status: used
---

# Runable

Официальный сайт и документация Runable — источники о проприетарной AI-платформе, где один агент планирует, создаёт, редактирует и публикует сайты, презентации, отчёты, таблицы, изображения, видео и аудио.

## Проверенные страницы

- **Website:** https://runable.com/
- **Documentation:** https://docs.runable.com/
- **How the Agent Works:** https://docs.runable.com/how-the-agent-works
- **Modes:** https://docs.runable.com/agent-mode-vs-chat-mode-vs-plan-mode
- **Branching & Rollback:** https://docs.runable.com/branching-and-rollback
- **Plans & Credits:** https://docs.runable.com/quickstart-copied-2
- **Live Pricing:** https://runable.com/pricing
- **GitHub organization:** https://github.com/runablehq
- **Positive third-party review:** https://producthunter.co/runable-review/
- **Critical hands-on review:** https://future-stack-reviews.com/runable-ai-review/

## Что подтверждено

- Agent Mode получает изолированный sandbox для файлов, команд, пакетов и серверов.
- Plan Mode отделяет исследование и согласование `plan.md` от исполнения.
- Skills подгружают специализированные workflow, memory переносит пользовательские предпочтения между чатами.
- Checkpoints восстанавливают разговор, canvas и файлы; branching клонирует sandbox в независимый чат.
- RunClaw переносит того же агента в Telegram, Slack и Discord.
- Платформа создаёт web, office и media-артефакты и использует credit-based биллинг.

Устойчивые сведения о продукте перенесены в [canonical-заметку Runable](../../tools/platforms/runable.md).

## Практическая ценность для ai-db

Runable полезен как reference-реализация artifact-first agent harness для non-developer workflow:

- цель пользователя отделена от выбора инструментов;
- вопросы и plan approval уменьшают стоимость неверного исполнения;
- sandbox и checkpoints связывают разговор с состоянием артефакта;
- branching позволяет сравнивать варианты без потери исходной версии;
- direct manipulation дополняет prompt-based редактирование.

## Ограничения источников

- Сайт, документация и GitHub принадлежат самой компании; это надёжные источники для описания интерфейса, но не для оценки качества.
- На 2026-07-20 live pricing и документация расходятся по тарифам, лимитам и перечню моделей. Цены и model availability нельзя считать стабильными без проверки checkout.
- Заявления о 1.5M+ customers, результатах benchmark и 3k+ connectors не подтверждены независимыми источниками в рамках этого обзора.
- Независимый hands-on обзор Future Stack Reviews описывает credit friction, различие между рекламируемыми и нативными connectors и неработавшие Discord channel mentions; тест Discord проводился 2026-04-27 и не доказывает текущее состояние. У обзора есть affiliate disclosure, поэтому его выводы зафиксированы как наблюдения одного автора, а не как окончательная оценка продукта.

## Связи

- [Runable](../../tools/platforms/runable.md) — canonical-страница платформы.
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — skills, memory, sandbox и checkpoints.
- [Human-in-the-loop UX](../../patterns/production-operations/human-in-the-loop-ux.md) — clarifying questions и plan approval.
- [Skills и правила для агентов](../../patterns/implementation/agent-skills-and-rules.md) — автоматический и явный выбор skills.

## Статус

Добавлено и интегрировано: 2026-07-20.
