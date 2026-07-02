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
- [Автоматизация сбора внешнего контекста](architecture-design/external-context-collection.md) — connectors, crawl, ingestion, provenance, freshness
- [Data governance и compliance](architecture-design/data-governance-compliance.md)

## 🟡 Implementation — как реализовать

*Конкретные техники: skills, evaluations, оркестрация, [работа с код-агентами](implementation/working-with-coding-agents.md).*

- [Skills и правила для агентов](implementation/agent-skills-and-rules.md) — модульные инструкции, проектные правила, проверяемые workflow
- [Evaluations для агентов](implementation/agent-evaluations.md) — evals и production gates
- [Оценка ответов LLM](implementation/llm-response-evaluation.md) — способы оценки final answer, rubrics и LLM-as-judge
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
| 🔵 Architecture & Design | 6 | Проектные блоки |
| 🟡 Implementation | 5 | Техники сборки |
| 🟠 Production & Operations | 2 | Эксплуатация |
| 🔴 Advanced / Pro-Tips | 4 | Pro-tips |

---

## Learning path: от нуля до production

Рекомендуемый порядок погружения — от базовой таксономии до production-эксплуатации.

### 🟢 Уровень 0: карта предметной области

*Цель: перестать смешивать чат-бота, workflow и автономного агента.*

1. Прочитать [таксономию агентов](fundamentals/agent-taxonomy.md).
2. Посмотреть [компоненты agent-системы](architecture-design/agent-system-components.md).
3. Понять роль [agent harness](architecture-design/agent-harness.md).

Ожидаемый результат: можно объяснить, где заканчивается обычный assistant и где начинается agentic system.

### 🟢 Уровень 1: базовая механика

*Цель: понять, как агент принимает решения и взаимодействует с внешним миром.*

1. Прочитать [execution loop агента](fundamentals/agent-execution-loop.md).
2. Прочитать [tool use, function calling и MCP](fundamentals/tool-use-and-mcp.md).
3. Прочитать [context engineering](fundamentals/context-engineering.md).

Ожидаемый результат: можно нарисовать цикл `state → plan → action → observation → stop`, объяснить роль tools и назвать риски длинного контекста.

### 🟡 Уровень 2: рабочие правила и паттерны

*Цель: научиться управлять поведением агента через проверяемые правила, а не надежду на "хорошую модель".*

1. Прочитать [skills и правила для агентов](implementation/agent-skills-and-rules.md).
2. Изучить [антипаттерны агентных систем](advanced/agent-antipatterns.md).
3. Для coding-сценариев прочитать [работу с код-агентами](implementation/working-with-coding-agents.md).

Ожидаемый результат: можно сформулировать задачу агенту как цель, ограничения, критерии успеха и проверку.

### 🔵 Уровень 3: безопасность и качество

*Цель: не выпускать агента в среду, где он может делать дорогие или опасные вещи без контроля.*

1. Прочитать [безопасность агентных систем](architecture-design/agent-security.md).
2. Прочитать [evaluations для агентов](implementation/agent-evaluations.md).
3. Прочитать [оценку ответов LLM](implementation/llm-response-evaluation.md).

Ожидаемый результат: у каждого tool call есть граница доверия, у каждого workflow есть eval, у каждого ответа есть критерии качества, у каждого инцидента есть trace.

### 🟠 Уровень 4: production

*Цель: перейти от прототипа к системе, которую можно эксплуатировать.*

1. Прочитать [production operations](production-operations/production-operations.md).
2. Прочитать [human-in-the-loop UX](production-operations/human-in-the-loop-ux.md).
3. Прочитать [RAG для агентов](architecture-design/rag-for-agents.md).
4. Прочитать [автоматизацию сбора внешнего контекста](architecture-design/external-context-collection.md).
5. Прочитать [multi-agent orchestration](implementation/multi-agent-orchestration.md).

Ожидаемый результат: понятно, как агент деплоится, наблюдается, ограничивается, эскалирует решения человеку и восстанавливается после ошибок.

### 🔴 Уровень 5: выбор стека и кейсы

*Цель: выбрать инструменты под задачу, а не под хайп.*

1. Выбрать один из [воспроизводимых рецептов](advanced/reproducible-agent-recipes.md).
2. Посмотреть [карту кейсов](advanced/agent-use-cases.md).

Ожидаемый результат: можно выбрать модель, фреймворк, eval и deploy-подход под конкретный use case.

### Минимальный практический проект

Чтобы закрепить маршрут, соберите маленького research/RAG-агента:

1. Индексирует 10–20 документов.
2. Делает hybrid retrieval.
3. Использует 2–3 tools с явными permissions.
4. Возвращает ответ с источниками.
5. Имеет 20 eval-вопросов.
6. Логирует trace каждого запуска.
7. Требует approval для действия с внешним side effect.

Если этот проект проходит evals и понятен по trace, база для более сложных агентов уже есть.

---

*Последнее обновление: 02.07.2026*
