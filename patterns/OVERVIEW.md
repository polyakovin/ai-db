# Patterns — hierarchy

Всё, из чего строятся AI-агенты: от базовых архитектурных решений до продвинутых pro-tips и production-практик. Раздел организован по уровням зрелости — начинай с Fundamentals, углубляйся по мере освоения.

---

## 🟢 Fundamentals — базовые понятия

*С чего начать: что такое AI-агент, как он работает, из каких примитивов состоит.*

- [Таксономия AI-агентов](fundamentals/agent-taxonomy.md) — assistant → workflow → agent → autonomous agent → multi-agent system
- [Execution loop агента](fundamentals/agent-execution-loop.md) — state, planning, action, observation, retries, stop criteria
- [Context engineering](fundamentals/context-engineering.md) — packing, memory tiers, retrieval injection, context budget
- [Tool use, function calling и MCP](fundamentals/tool-use-and-mcp.md) — tool schema, permissions, approvals, MCP

## 🔵 Architecture & Design — как проектировать

*Архитектурные блоки: компоненты, безопасность, RAG, compliance.*

- [Паттерны работы с AI-агентами](architecture-design/agent-system-components.md) — карта компонентов agent-системы
- [Agent Harness](architecture-design/agent-harness.md) — рабочая обвязка: tools, skills, memory, filesystem, sandbox, subagents
- [Безопасность агентных систем](architecture-design/agent-security.md) — prompt injection, sandbox, secrets, audit, approvals
- [RAG для AI-агентов](architecture-design/rag-for-agents.md) — retrieval как часть state, grounding, evals
- [Data governance и compliance](architecture-design/data-governance-compliance.md)

## 🟡 Implementation — как реализовать

*Конкретные техники: skills, evaluations, оркестрация, работа с код-агентами.*

- [Skills и правила для агентов](implementation/agent-skills-and-rules.md) — модульные инструкции, проектные правила, проверяемые workflow
- [Evaluations для агентов](implementation/agent-evaluations.md) — evals и production gates
- [Multi-agent orchestration](implementation/multi-agent-orchestration.md) — роли, shared state, supervisor/worker, anti-patterns
- [Работа с код-агентами](implementation/working-with-coding-agents.md) — цикл постановки задачи, проверки, фиксации

## 🟠 Production & Operations — как запускать

*Жизнь после деплоя: эксплуатация, UX, сопровождение.*

- [Human-in-the-loop UX](production-operations/human-in-the-loop-ux.md)
- [Production operations](production-operations/production-operations.md) — эксплуатация в продакшене

## 🔴 Advanced / Pro-Tips — продвинутые паттерны

*Глубокий опыт: антипаттерны, воспроизводимость, карта кейсов.*

- [Антипаттерны агентных систем](advanced/agent-antipatterns.md) — over-agentification, blind tool execution, weak evals, hidden costs
- [Воспроизводимые рецепты](advanced/reproducible-agent-recipes.md)
- [Карта кейсов](advanced/agent-use-cases.md) — выбор архитектуры и evals под use case

---

## Как читать раздел

Каждая заметка раскрывает архитектурный аспект или инструментальный паттерн и содержит ссылки на смежные материалы. Паттерны описаны по схеме:

**Проблема → Решение → Псевдокод → Когда применять → Связанные паттерны**

Если ты только начинаешь — пройди 🟢 Fundamentals последовательно. Если ищешь конкретную технику — сразу переходи к 🟡 Implementation или 🔵 Architecture & Design. Для production-решений смотри 🟠, для глубокого рефакторинга — 🔴.

---

| Уровень | Файлов | Вход |
|---------|--------|------|
| 🟢 Fundamentals | 4 | Базовые примитивы |
| 🔵 Architecture & Design | 5 | Проектные блоки |
| 🟡 Implementation | 4 | Техники сборки |
| 🟠 Production & Operations | 2 | Эксплуатация |
| 🔴 Advanced / Pro-Tips | 3 | Pro-tips |

*Последнее обновление: 25.06.2026*
