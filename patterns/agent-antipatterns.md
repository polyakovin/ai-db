# Антипаттерны агентных систем

Антипаттерн — это повторяемое решение, которое выглядит агентным, но ухудшает качество, безопасность или стоимость.

## Over-agentification

Симптом: команда строит агента там, где достаточно deterministic workflow.

Проверка:

- Нужен ли динамический выбор tools?
- Меняется ли план после observation?
- Есть ли неизвестная среда?

Если нет, делайте workflow.

## Blind tool execution

Симптом: модель может вызвать любой tool с любыми аргументами.

Контрмера:

- scoped tools;
- schema validation;
- approval для side effects;
- audit log;
- deny-by-default для опасных действий.

## Prompt-only safety

Симптом: безопасность описана только словами “не делай X”.

Контрмера: policy enforcement вне модели: sandbox, permissions, secrets isolation, output validation.

## Weak evals

Симптом: агент “работает на демо”, но нет regression suite.

Контрмера:

- golden set;
- adversarial cases;
- tool failure cases;
- replay traces;
- cost/latency gates.

## Hidden costs

Симптом: прототип хороший, production счёт неприятный.

Контрмера:

- budget на run;
- model routing;
- prompt caching;
- token metrics;
- stop criteria.

## Prompt leakage

Симптом: system prompt или internal policies появляются в ответе.

Контрмера:

- не хранить секреты в prompt;
- считать system prompt не секретом, а control surface;
- проверять leakage evals;
- отделять public policy от private configuration.

## Memory pollution

Симптом: агент сохраняет случайные или неверные выводы как долговременную память.

Контрмера:

- memory write approval;
- provenance;
- TTL;
- user-visible memory edit/delete;
- eval на stale memory.

## Role soup

Симптом: “researcher”, “planner”, “critic”, “executor” существуют, но делают одно и то же.

Контрмера:

- у каждой роли свой input/output;
- разные permissions;
- owner итогового решения;
- лимит межагентных вызовов.

## Связанные заметки

- [Таксономия AI-агентов](../patterns/agent-taxonomy.md)
- [Multi-agent orchestration](../patterns/multi-agent-orchestration.md)
- [Безопасность агентных систем](../patterns/agent-security.md)
