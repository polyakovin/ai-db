# Concepts — overview

Раздел посвящён тому, как устроены AI-агенты изнутри: от базовых компонентов до сложных многоагентных систем. Здесь собираются материалы о структурных решениях, циклах работы, управлении памятью и состоянием.

## Материалы

- [Таксономия AI-агентов](agent-taxonomy.md) — assistant, workflow, agent, autonomous agent, multi-agent system
- [Паттерны работы с AI-агентами](agent-system-components.md) — карта компонентов agent-системы
- [Agent Harness](agent-harness.md) — рабочая обвязка вокруг агента: tools, skills, memory, filesystem, sandbox, subagents
- [Execution loop агента](agent-execution-loop.md) — state, planning, action, observation, retries и stop criteria
- [Context engineering](context-engineering.md) — packing, memory tiers, retrieval injection и context budget
- [Tool use, function calling и MCP](tool-use-and-mcp.md) — tool schema, permissions, approvals и MCP
- [Безопасность агентных систем](agent-security.md) — prompt injection, sandbox, secrets, audit и approvals
- [RAG для AI-агентов](rag-for-agents.md) — retrieval как часть state, grounding и evals
- [Multi-agent orchestration](multi-agent-orchestration.md) — роли, shared state, supervisor/worker и anti-patterns

## Как устроен раздел

Каждая заметка внутри раздела раскрывает конкретный архитектурный аспект и содержит ссылки на релевантные статьи, паттерны или практические кейсы из других разделов хранилища.

---

*Последнее обновление: 24.06.2026*
