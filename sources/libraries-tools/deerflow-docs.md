---
title: DeerFlow Documentation and Repository
url: https://deerflow.tech/en/docs
type: url
category: sources
tags: [deerflow, agent-harness, long-horizon, multi-agent, sandbox, skills, memory, open-source]
added: 2026-07-23
status: used
---

# DeerFlow Documentation and Repository

Набор официальных источников DeerFlow: документация Harness/App, основной GitHub-репозиторий и release notes. Материалы использованы для canonical-обзора архитектуры, возможностей, deployment и security boundaries.

## Проверенные страницы

- **Documentation:** https://deerflow.tech/en/docs
- **Core concepts:** https://deerflow.tech/en/docs/introduction/core-concepts
- **Harness vs App:** https://deerflow.tech/en/docs/introduction/harness-vs-app
- **Design principles:** https://deerflow.tech/en/docs/harness/design-principles
- **Sandbox:** https://deerflow.tech/en/docs/harness/sandbox
- **Subagents:** https://deerflow.tech/en/docs/harness/subagents
- **Memory:** https://deerflow.tech/en/docs/harness/memory
- **Deployment:** https://deerflow.tech/en/docs/application/deployment-guide
- **Repository:** https://github.com/bytedance/deer-flow
- **Release v2.0.0:** https://github.com/bytedance/deer-flow/releases/tag/v2.0.0
- **Backend package metadata:** https://github.com/bytedance/deer-flow/blob/main/backend/pyproject.toml
- **Security policy:** https://github.com/bytedance/deer-flow/blob/main/SECURITY.md
- **NVD CVE-2026-34430:** https://nvd.nist.gov/vuln/detail/CVE-2026-34430
- **LocalSandbox fix:** https://github.com/bytedance/deer-flow/commit/92c7a20cb74addc3038d2131da78f2e239ef542e

## Что проверено

- Граница между переиспользуемым Harness и готовым App.
- Переход от deep-research framework 1.x к полностью переписанному general-purpose harness 2.x.
- Состав runtime: lead agent, middleware, tools, skills, sandbox, memory, subagents и context management.
- Варианты sandbox и предупреждения о host access в LocalSandbox.
- Исправленная уязвимость CVE-2026-34430 в старых версиях LocalSandbox bash tool.
- Deployment paths, persistence, authentication и production isolation.
- MIT license, tagged release `v2.0.0` и расхождение между release tag и версией активной ветки.

Устойчивые сведения и рекомендации перенесены в [canonical-страницу DeerFlow](../../tools/frameworks/deerflow.md).

## Ограничения источников

- Документация, README и release notes принадлежат самому проекту: они надёжны для API, конфигурации и заявленного дизайна, но не доказывают качество результатов.
- Репозиторий активно развивается, поэтому `main`, documentation и последний tagged release могут описывать разные snapshots.
- Ранние issue reports до stable release не использованы как доказательство текущих дефектов.
- Найдены обзоры и feature comparisons, но не воспроизводимый benchmark актуальной ветки 2.x против других harnesses; оценка ограничена архитектурой и документированными capabilities.

## Связи

- [DeerFlow](../../tools/frameworks/deerflow.md) — canonical-страница инструмента
- [Исследование фреймворков](../../tools/agent-frameworks-research.md) — карта выбора
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — архитектурный контекст
- [Progressive disclosure](../../patterns/implementation/progressive-disclosure-for-agents.md) — skills и deferred tool discovery
- [Безопасность агентных систем](../../patterns/architecture-design/agent-security.md) — sandbox и permissions

## Статус

Проверено и интегрировано: 2026-07-23.
