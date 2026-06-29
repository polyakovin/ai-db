# Observability и debugging для AI-агентов

Observability для агента отвечает на вопрос: почему агент сделал именно это действие и как воспроизвести run. Без trace агент превращается в недетерминированный black box.

## Что логировать

| Сигнал | Пример | Зачем |
|---|---|---|
| Trace | run -> steps -> tool calls | восстановить путь решения |
| Spans | model call, retrieval, tool call | найти latency/cost bottleneck |
| Logs | structured events | расследовать ошибки |
| Metrics | pass rate, p95, cost, token usage | управлять production |
| Artifacts | prompts, retrieved chunks, outputs | replay и evals |

OpenTelemetry задаёт общий язык traces/spans/logs/metrics, а агентные платформы вроде [[langsmith.md|LangSmith]] и Phoenix добавляют LLM-specific представления run, prompt, retrieval и tool calls.

## Минимальная trace-схема

```yaml
run_id: ...
agent_version: ...
model: ...
input_summary: ...
steps:
  - type: model_call
    prompt_hash: ...
    output_summary: ...
    tokens: ...
  - type: tool_call
    tool: search_docs
    args_redacted: ...
    observation_summary: ...
  - type: approval
    decision: approved
outcome: success|blocked|failed
```

## Failure taxonomy

Классифицируйте провалы так, чтобы из них рождались evals:

- instruction conflict;
- missing context;
- retrieval miss;
- hallucinated source;
- wrong tool;
- invalid tool args;
- permission denied;
- unsafe action attempted;
- budget exceeded;
- human handoff needed;
- flaky external dependency.

## Debugging workflow

1. Найти failing run по `run_id`.
2. Сравнить goal, retrieved context и tool list.
3. Посмотреть первый шаг, где state разошёлся с expected path.
4. Отнести ошибку к failure taxonomy.
5. Создать regression eval.
6. Исправлять минимальный слой: prompt, retrieval, tool schema, policy или product UX.
7. Перепроверить old + new evals.

## Redaction

Observability не должна превращаться в утечку данных. Редактируйте:

- secrets;
- access tokens;
- PII;
- confidential documents;
- raw customer messages там, где достаточно summary;
- tool args, содержащие приватные id.

## Инструменты

| Инструмент | Когда полезен |
|---|---|
| OpenTelemetry | общий стандарт instrumentation и экспорт traces/logs/metrics |
| LangSmith | tracing/evals/debugging для LangChain/LangGraph и LLM apps |
| Arize Phoenix | open-source observability/evals для LLM/RAG traces |
| Provider dashboards | usage, latency, model-level errors |
| Custom audit DB | regulated workflows и approvals |

## Источники

- [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- [LangSmith observability quickstart](https://docs.langchain.com/langsmith/observability-quickstart)
- [Arize Phoenix docs](https://arize.com/docs/phoenix)

## Связанные заметки

- [Evaluations для агентов](../patterns/implementation/agent-evaluations.md)
- [Execution loop агента](../patterns/fundamentals/agent-execution-loop.md)
- [Production operations](../patterns/production-operations/production-operations.md)
- [Agent Harness](../patterns/architecture-design/agent-harness.md) — observability как компонент обвязки
