# Production operations для агентных систем

Production agent — это сервис с недетерминированным planner внутри. Его нужно эксплуатировать как distributed system: с лимитами, очередями, trace, rollback, incident response и контролем стоимости.

## Deployment topologies

| Топология | Когда брать | Риски |
|---|---|---|
| Synchronous API | короткие запросы до нескольких секунд | timeout и UX ожидания |
| Background job | long-running research/coding tasks | retries, idempotency, state storage |
| Event-driven agent | inbox, webhook, cron | runaway automation |
| Human approval queue | high-risk side effects | задержки и ownership |
| Multi-service harness | enterprise production | сложность observability |

## Runtime limits

Минимально задайте:

- max wall-clock time;
- max model calls;
- max tool calls;
- max tokens/cost;
- allowed tools;
- allowed network/file scopes;
- retry budget;
- queue timeout;
- concurrency limit.

## State and resumability

Long-running агент должен переживать:

- timeout;
- transient API failure;
- process restart;
- human approval delay;
- partial tool failure.

Для этого state должен храниться вне model context: run DB, task file, workflow engine или durable queue.

## Rollback и kill switch

Для каждого side effect:

- знать, можно ли откатить;
- сохранять before/after state;
- иметь manual override;
- иметь global disable для tool или agent version;
- уметь остановить новые runs и дать текущим завершиться безопасно.

## Cost controls

Контролируйте:

- model choice по классу задач;
- reasoning effort;
- prompt caching;
- retrieval top-k;
- max output;
- batch/flex/priority modes;
- per-user и per-tenant budgets;
- alerts по аномалиям.

## Release checklist

Перед production:

1. Eval suite зелёный.
2. Prompt/model/tool versions зафиксированы.
3. Observability включена.
4. Approvals проверены.
5. Secrets не попадают в context/logs.
6. Rate limits и budgets заданы.
7. Incident playbook существует.
8. Rollback протестирован.

## Источники

- [OpenAI production best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Связанные заметки

- [Agent Harness](../concepts/agent-harness.md)
- [Observability и debugging](../tools/agent-observability-debugging.md)
- [Безопасность агентных систем](../concepts/agent-security.md)
