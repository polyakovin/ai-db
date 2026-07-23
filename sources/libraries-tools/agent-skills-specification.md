---
title: Agent Skills specification and authoring guidance
url: https://agentskills.io/specification
type: url
category: sources
tags: [agent-skills, progressive-disclosure, context-engineering, skills]
added: 2026-07-23
status: used
---

# Agent Skills specification and authoring guidance

Набор первичных материалов об открытом формате Agent Skills и поэтапной загрузке инструкций и ресурсов.

## Проверенные материалы

- **Agent Skills overview:** https://agentskills.io/home
- **Agent Skills specification:** https://agentskills.io/specification
- **Skill authoring best practices:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Tool search tool:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
- **Репозиторий спецификации:** https://github.com/agentskills/agentskills

Доступ и проверка содержания: 2026-07-23.

## Что подтверждают источники

- Agent Skills используют три уровня progressive disclosure: metadata, полное тело активированного `SKILL.md`, дополнительные ресурсы по необходимости.
- Спецификация оценивает metadata примерно в 100 токенов и рекомендует держать инструкции активированного skill меньше 5 000 токенов.
- `description` должна объяснять, что делает skill и когда её применять, включая конкретные ключевые слова для discovery.
- Основной файл должен быть точкой входа и картой ресурсов; большие материалы выносятся в `references/`, `scripts/` и `assets/`.
- Authoring guidance рекомендует прямые ссылки на один уровень от `SKILL.md`, тематическое разбиение reference-файлов и содержание для длинных references.
- Deferred tool loading переносит тот же принцип на каталоги tools: в model context остаются search и небольшой eager-набор, полные schemas найденных tools раскрываются по запросу.

## Ограничения

- Точные token и line limits относятся к текущей спецификации и конкретным реализациям; это стартовые ориентиры, а не универсальные свойства всех моделей.
- Agent Skills описывают формат упаковки capabilities, но не задают общую permission model для каждого runtime.
- Заявленные эффекты tool search и его пороги относятся к реализации Claude API; общий паттерн требует собственных evals на используемой модели и каталоге.

## Интеграция в vault

- [Progressive disclosure для AI-агентов](../../patterns/implementation/progressive-disclosure-for-agents.md) — добавлены общая архитектура, применение к skills, tools, repository knowledge и RAG, failure modes и evals.
- [Skills и правила для агентов](../../patterns/implementation/agent-skills-and-rules.md) — добавлена связь с канонической практикой поэтапной загрузки.
- [Context engineering](../../patterns/fundamentals/context-engineering.md) — progressive disclosure добавлен как способ управлять context budget.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — добавлена связь с deferred tool discovery.

## Статус

Добавлено и интегрировано: 2026-07-23.
