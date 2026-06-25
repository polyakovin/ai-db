# Карта кейсов AI-агентов

Кейсы нужны не как вдохновляющий список, а как способ связать use case с архитектурой, рисками, evals и production gates.

## Матрица кейсов

| Кейс | Ценность | Архитектура | Главные риски | Evals |
|---|---|---|---|---|
| Support agent | быстрее ответы и triage | RAG + CRM tools + HITL | privacy, wrong policy, refund mistakes | policy QA, escalation accuracy |
| Coding workflow | скорость разработки | coding agent + tests + review gates | unrelated changes, insecure code | tests, diff review, vuln scan |
| Data analyst | self-serve аналитика | SQL agent + semantic layer | SQL injection, wrong aggregation | query correctness, read-only |
| Back-office automation | меньше ручных операций | workflow + tools + approvals | side effects, audit gaps | process completion, approval checks |
| Research assistant | faster synthesis | search + notes + citations | stale sources, hallucinations | citation accuracy, source quality |
| Personal second brain | память и навигация | retrieval + user memory | privacy, stale memory | retrieval quality, consent checks |

## Шаблон кейса

```markdown
# <case>

## Контекст
Кто пользователь, какая задача, почему agentic system нужна.

## Outcome
Какой результат считается успехом.

## Архитектура
Модель, tools, memory/RAG, approvals, observability.

## Риски
Security, privacy, quality, cost, legal.

## Evals
Набор тестов и метрик.

## Production gates
Что должно быть готово до запуска.
```

## Support agent

MVP:

- ищет policy;
- предлагает draft;
- классифицирует escalation;
- не выполняет refunds без approval.

Production gates:

- PII redaction;
- audit log;
- policy freshness;
- human review для sensitive cases.

## Coding workflow

MVP:

- читает задачу;
- строит план;
- меняет код минимальным diff;
- запускает тесты;
- готовит summary.

Production gates:

- branch isolation;
- pre-commit hooks;
- secret scanning;
- reviewer handoff.

## Data analyst

MVP:

- понимает schema;
- генерирует read-only SQL;
- объясняет результат;
- показывает query.

Production gates:

- row limits;
- SQL allowlist;
- semantic layer;
- protected columns.

## Back-office automation

MVP:

- принимает structured request;
- проверяет policy;
- создаёт draft действия;
- просит approval.

Production gates:

- idempotency keys;
- rollback;
- queue monitoring;
- audit export.

## Research assistant

MVP:

- ищет primary sources;
- пишет notes;
- отделяет facts от inference;
- возвращает report с links.

Production gates:

- source quality rubric;
- date handling;
- contradiction notes;
- citation checks.

## Personal second brain

MVP:

- индексирует заметки;
- отвечает с ссылками;
- предлагает related notes;
- сохраняет preferences только с consent.

Production gates:

- memory edit/delete;
- private scopes;
- freshness labels;
- retrieval evals.
