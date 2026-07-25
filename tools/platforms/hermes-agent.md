---
title: Hermes Agent
url: https://hermes-agent.nousresearch.com/
type: url
category: tools
tags: [agent-harness, self-hosted, skills, memory, delegation, open-source]
added: 2026-07-26
status: verified
---

# Hermes Agent

Hermes Agent — open-source MIT-licensed [agent harness](../../patterns/architecture-design/agent-harness.md) от Nous Research. Он работает локально или на пользовательской инфраструктуре, поддерживает разные model providers и объединяет CLI, messaging gateway, tools, skills, persistent memory, delegation и автоматизацию.

## Ключевые возможности

- Toolsets для файлов, terminal, web, browser, code execution, vision, memory и delegation.
- Messaging gateway и CLI для доступа к одному агенту из разных интерфейсов.
- MCP servers как дополнительный источник динамически подключаемых tools.
- Subagents и task delegation.
- Scheduled jobs и always-on deployment.
- Локальные, container, SSH и облачные execution backends.

## Memory и skills

Встроенная память разделяет короткие устойчивые сведения:

- `MEMORY.md` — факты об окружении, проектах, соглашениях и найденных рабочих приёмах;
- `USER.md` — предпочтения и профиль пользователя.

Размер встроенной памяти ограничен, чтобы она оставалась курированной и всегда помещалась в system context. Более длинные процедуры хранятся в skills и загружаются по progressive disclosure. Агент может создавать и обновлять skills после успешных или исправленных workflow, но production-настройка должна оставлять human review для self-modification.

## Когда применять

Hermes Agent подходит как self-hosted general-purpose harness для:

- персонального ассистента с памятью;
- исследовательских и coding-задач с tools;
- автоматизации через мессенджеры;
- делегирования изолированным subagents;
- воспроизводимых процедур, сохранённых как skills.

## Ограничения

- Возможности зависят от включённых toolsets, провайдера модели и выбранного execution backend.
- Local-first не означает автоматически безопасный: секреты, shell, browser и messaging требуют least privilege, sandbox и audit.
- Автоматическое изменение memory и skills нуждается в лимитах, provenance и review.
- Для установки и актуального поведения источником истины служат официальный репозиторий и документация Nous Research; сторонние локализации могут отставать.

## Связи

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — архитектурная роль Hermes Agent.
- [Робастная multi-agent среда](../../patterns/architecture-design/robust-multi-agent-environment.md) — пример execution worker с delegation.
- [Персистентная память агента](../../patterns/advanced/agent-memory-patterns.md) — bounded memory и user profile.
- [Skills и правила для агентов](../../patterns/implementation/agent-skills-and-rules.md) — progressive disclosure и процедурная память.
- [Hermes Agent — русскоязычный обзор](../../sources/libraries-tools/hermes-agent-ru.md) — provenance переданного материала.
