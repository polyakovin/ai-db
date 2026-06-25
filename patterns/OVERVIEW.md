# Patterns & Concepts — overview

Всё, из чего строятся AI-агенты: от базовых архитектурных решений до проверенных шаблонов взаимодействия.

## Архитектурные блоки (concepts)

- [Таксономия AI-агентов](agent-taxonomy.md) — assistant, workflow, agent, autonomous agent, multi-agent system
- [Паттерны работы с AI-агентами](agent-system-components.md) — карта компонентов agent-системы
- [Agent Harness](agent-harness.md) — рабочая обвязка вокруг агента: tools, skills, memory, filesystem, sandbox, subagents
- [Execution loop агента](agent-execution-loop.md) — state, planning, action, observation, retries и stop criteria
- [Context engineering](context-engineering.md) — packing, memory tiers, retrieval injection и context budget
- [Tool use, function calling и MCP](tool-use-and-mcp.md) — tool schema, permissions, approvals и MCP
- [Безопасность агентных систем](agent-security.md) — prompt injection, sandbox, secrets, audit и approvals
- [RAG для AI-агентов](rag-for-agents.md) — retrieval как часть state, grounding и evals
- [Multi-agent orchestration](multi-agent-orchestration.md) — роли, shared state, supervisor/worker и anti-patterns

## Проектировочные паттерны (patterns)

- [Skills и правила для агентов](agent-skills-and-rules.md) — модульные инструкции, проектные правила и проверяемые workflow
- [Антипаттерны агентных систем](agent-antipatterns.md) — over-agentification, blind tool execution, weak evals и hidden costs
- [Evaluations для агентов](agent-evaluations.md) — evals и production gates
- [Data governance и compliance](data-governance-compliance.md)
- [Human-in-the-loop UX](human-in-the-loop-ux.md)
- [Production operations](production-operations.md) — эксплуатация в продакшене
- [Работа с код-агентами](working-with-coding-agents.md) — цикл постановки задачи, проверки и фиксации
- [Воспроизводимые рецепты](reproducible-agent-recipes.md)
- [Карта кейсов](agent-use-cases.md) — выбор архитектуры и evals под use case

## Как устроен раздел

Каждая заметка раскрывает архитектурный аспект или инструментальный паттерн и содержит ссылки на смежные материалы. Паттерны описаны по схеме: проблема → решение → псевдокод → когда применять → связанные паттерны.

---

*Последнее обновление: 25.06.2026*
