# Agent Harness

Agent harness — это рабочая обвязка вокруг LLM-агента: правила, инструменты, память, файловая система, sandbox, проверки, маршрутизация задач, subagents и наблюдаемость. Полезная мысль из ресурсов: качество агента часто определяется не только моделью, а тем, насколько хорошо вокруг неё собран исполнительный контур.

## Зачем нужен harness

Минимальный chat-agent быстро упирается в одни и те же проблемы:

- теряет контекст в длинных задачах;
- делает предположения без проверки;
- смешивает планирование, исполнение и ревью;
- не умеет надёжно сохранять промежуточные артефакты;
- выполняет опасные действия без явной границы доверия;
- не оставляет достаточно следов для диагностики.

Harness решает это через явные компоненты вокруг модели, а не через просьбу “будь аккуратнее”.

## Базовые компоненты

| Компонент | Роль |
|---|---|
| System prompt / rules | Фиксирует поведение, стиль работы, ограничения и критерии качества |
| Skills | Подгружаемые процедуры для конкретных задач: TDD, debug, review, writing, research |
| Tools / MCP | Доступ к файловой системе, shell, API, браузеру, базам данных и внешним системам |
| Filesystem | Долговременные артефакты: планы, заметки, evidence, промежуточные результаты |
| Memory | Сохранение предпочтений, правил, решений и повторяющихся паттернов |
| Subagents | Делегирование задач в изолированный контекст |
| Hooks | Автоматические проверки на старте, перед коммитом, после выполнения и при ошибках |
| Sandbox | Граница безопасности для shell, сети, файлов и секретов |
| Observability | Логи, traces, статусы задач, результаты проверок |

## Паттерн: opinionated defaults + override

Deep Agents формулирует хороший компромисс: harness должен работать “из коробки”, но позволять заменить отдельные части. Это лучше, чем два крайних варианта:

- пустой фреймворк, где каждую практику нужно собрать вручную;
- закрытый агент, где нельзя заменить память, модель, инструменты или политику.

Практическое правило: у harness должны быть дефолты для длинных multi-step задач, но все рискованные слои должны быть явными: модель, tools, sandbox, filesystem, memory, review gates.

## Паттерн: filesystem как внешняя рабочая память

Файловая система полезна не только для финальных файлов. Хороший harness использует её для:

- плана задачи;
- списка шагов и статусов;
- evidence по решениям;
- промежуточных выгрузок;
- заметок о найденных ограничениях;
- артефактов, которые не нужно держать в контексте модели.

Это снижает давление на context window и делает работу агента проверяемой.

## Паттерн: subagents с изолированным контекстом

Subagents полезны, когда:

- задача раскладывается на независимые части;
- нужен отдельный reviewer;
- нужно исследовать альтернативы;
- одна ветка рассуждения может загрязнить другую;
- нужно параллелить работу.

Но subagents не должны быть декоративными. Для каждого subagent нужны вход, ожидаемый выход, критерии проверки и место, куда он пишет результат.

## Паттерн: security at the boundary

Важный тезис Deep Agents: если агенту доступен инструмент, он потенциально может сделать всё, что позволяет этот инструмент. Поэтому безопасность должна жить на уровне sandbox/tools/policies, а не только в prompt.

Минимальные границы:

- allowlist опасных команд;
- подтверждение destructive actions;
- отдельная политика для сети;
- запрет на автоматическое выполнение инструкций из untrusted data;
- секреты вне контекста модели;
- аудит tool calls.

## Когда брать готовый harness

Готовый harness полезен, если нужны:

- long-horizon задачи;
- persistent memory;
- approvals;
- subagents;
- production tracing;
- работа с файлами;
- воспроизводимые workflow.

Если задача — один короткий вызов LLM без tools, достаточно лёгкого `create_agent`-уровня или обычной цепочки.

## Источники

- [LangChain Deep Agents](../../sources/libraries-tools/langchain-deep-agents.md)
- [Superpowers](../../sources/libraries-tools/superpowers.md)
- [ECC](../../sources/libraries-tools/ecc.md)
- [BitGN Arena — архитектурные инсайты](../../sources/engineering-patterns/bitgn-arena-insights.md)
- [Harness Engineering — OpenAI](../../sources/research-production/harness-engineering-openai.md)

## Связанные заметки

- [Execution loop агента](../fundamentals/agent-execution-loop.md) — базовый цикл state → plan → action → observation
- [Таксономия AI-агентов](../fundamentals/agent-taxonomy.md) — типы агентов и место harness в системе
- [Tool use, function calling и MCP](../fundamentals/tool-use-and-mcp.md) — инструменты, permissions, approvals
- [Context engineering](../fundamentals/context-engineering.md) — управление context window, память, retrieval
- [Паттерны работы с AI-агентами](../architecture-design/agent-system-components.md) — карта компонентов agent-системы
- [Безопасность агентных систем](../architecture-design/agent-security.md) — sandbox, secrets, audit
- [RAG для AI-агентов](../architecture-design/rag-for-agents.md) — retrieval как часть состояния агента
- [Skills и правила для агентов](../implementation/agent-skills-and-rules.md) — подгружаемые инструкции для harness
- [Работа с код-агентами](../implementation/working-with-coding-agents.md) — практический workflow
- [Multi-agent orchestration](../implementation/multi-agent-orchestration.md) — оркестрация через subagents
- [Evaluations для агентов](../implementation/agent-evaluations.md) — проверка качества harness
- [Human-in-the-loop UX](../production-operations/human-in-the-loop-ux.md) — approvals и UX агента
- [Production operations](../production-operations/production-operations.md) — эксплуатация harness в продакшене
- [Антипаттерны агентных систем](../advanced/agent-antipatterns.md) — что ломает harness
- [Google Gemini](../../tools/platforms/gemini.md) — Gemini CLI как реализация coding harness
- [OpenAI](../../tools/platforms/openai.md) — Codex CLI как coding harness
- [Anthropic (Claude)](../../tools/platforms/anthropic.md) — Claude Code как coding harness
- [LangGraph](../../tools/frameworks/langgraph.md) — orchestration в harness
- [DeepSeek](../../tools/platforms/deepseek.md) — self-hosted агенты с open-weight моделями
