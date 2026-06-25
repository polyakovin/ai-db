# Multi-agent orchestration

Multi-agent система полезна, когда разные роли действительно улучшают качество, параллелизм или контроль. Она вредна, если несколько агентов просто пересказывают друг другу неопределённый контекст.

## Когда multi-agent оправдан

- независимые подзадачи можно выполнять параллельно;
- нужен отдельный reviewer или critic;
- роли требуют разных tools/permissions;
- нужна изоляция контекста;
- один агент генерирует, другой проверяет;
- есть supervisor, который агрегирует evidence и принимает stop decision.

## Базовые паттерны

| Паттерн | Как работает | Когда применять |
|---|---|---|
| Supervisor/worker | supervisor ставит задачи worker-агентам | research, coding, data analysis |
| Generator/critic | один создаёт, другой проверяет | code review, writing, QA |
| Debate | агенты предлагают разные решения | ambiguous strategy decisions |
| Router | классификатор выбирает specialist | support, triage |
| Pipeline | каждый агент отвечает за этап | extraction -> analysis -> report |
| Blackboard | агенты пишут в общее evidence-хранилище | long-running investigation |

## Shared state

Общее состояние должно быть:

- структурированным;
- append-only там, где важен audit;
- разделённым по ролям и permissions;
- с owner для каждого artifact;
- пригодным для replay.

Не стоит давать всем агентам один общий неструктурированный context: это быстро приводит к конфликтам и потере ответственности.

## Conflict resolution

Если агенты спорят, нужен deterministic resolver:

- ranking criteria;
- source priority;
- confidence threshold;
- human escalation;
- final decision owner.

Без resolver multi-agent превращается в дорогой brainstorming.

## Anti-patterns

- “больше агентов = умнее”;
- одинаковые агенты с разными именами;
- нет единого stop criteria;
- нет владельца итогового ответа;
- agents call each other без лимита;
- shared memory без provenance.

## Инструментальные опоры

- LangGraph: stateful graphs, persistence, human-in-the-loop.
- AutoGen: conversational single/multi-agent apps и event-driven Core.
- CrewAI: crews, tasks/processes, guardrails, memory, flows.
- OpenAI Agents SDK: handoffs, guardrails, tracing/evals.

## Связанные заметки

- [Agent Harness](agent-harness.md)
- [Execution loop агента](agent-execution-loop.md)
- [Исследование фреймворков](../tools/agent-frameworks-research.md)
