# Воспроизводимые рецепты AI-агентов

Эта заметка задаёт минимальные рецепты, которые можно превратить в отдельные проекты или подробные how-to. Каждый рецепт фиксирует цель, компоненты, проверки и production-gates.

## Общий шаблон

Для каждого рецепта:

1. Определить outcome и boundaries.
2. Выбрать модель и tools.
3. Задать state schema.
4. Добавить eval set.
5. Включить tracing.
6. Ограничить permissions.
7. Проверить failure cases.

## RAG agent

Цель: отвечать по базе документов с citations.

Компоненты:

- ingestion pipeline;
- chunker;
- hybrid retrieval;
- reranker;
- answer generator;
- citation checker;
- eval set с negative queries.

Проверки:

- recall@5;
- citation accuracy;
- unsupported claim rate;
- freshness;
- latency p95.

Связано: [RAG для агентов](../concepts/rag-for-agents.md).

## SQL agent

Цель: отвечать на вопросы по данным через безопасные SQL-запросы.

Компоненты:

- schema introspection;
- read-only DB role;
- query planner;
- SQL validator;
- row limit;
- result summarizer;
- audit log.

Проверки:

- запрет write queries;
- correct aggregation;
- SQL injection cases;
- timeout handling;
- “данных недостаточно” cases.

## Browser agent

Цель: выполнять web tasks с ограниченными side effects.

Компоненты:

- browser sandbox;
- URL allowlist/denylist;
- page summarizer;
- form-fill approval;
- screenshot trace;
- download quarantine.

Проверки:

- prompt injection на странице;
- невозможность доступа к localhost/secrets;
- confirmation перед отправкой формы;
- trace каждого action.

## Coding agent

Цель: менять кодовую базу по задаче и проходить проверки.

Компоненты:

- repo reader;
- patch tool;
- test runner;
- diff reviewer;
- branch/commit workflow;
- project memory/rules.

Проверки:

- minimal diff;
- tests/lint;
- no unrelated rewrites;
- review of risky changes;
- commit + push policy.

Связано: [Работа с код-агентами](working-with-coding-agents.md).

## Support agent

Цель: готовить ответы клиентам и выполнять безопасные support actions.

Компоненты:

- customer context retrieval;
- policy retrieval;
- response drafter;
- escalation classifier;
- CRM tool;
- approval для refunds/credits/account changes.

Проверки:

- policy citation;
- tone;
- privacy boundaries;
- hallucination prevention;
- correct escalation.

## Research agent

Цель: собирать информацию, отделять факты от выводов и отдавать report с источниками.

Компоненты:

- source search;
- primary-source preference;
- note taking;
- claim extraction;
- contradiction handling;
- citation formatter.

Проверки:

- source quality;
- date awareness;
- no unsupported claims;
- clear assumptions;
- reproducible source list.

## Связанные заметки

- [Agent Harness](../concepts/agent-harness.md)
- [Evaluations для агентов](agent-evaluations.md)
- [Production operations](production-operations.md)
