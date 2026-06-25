# Evaluations для AI-агентов

Eval для агента проверяет не один ответ модели, а весь workflow: выбор tools, обработку ошибок, качество retrieved evidence, соблюдение policy, стоимость и способность остановиться.

## Что измерять

| Уровень | Вопрос | Метрики |
|---|---|---|
| Task success | решена ли задача | pass rate, exact outcome, human score |
| Tool use | правильно ли выбран tool | tool precision/recall, invalid calls |
| Grounding | опирается ли ответ на источники | citation accuracy, unsupported claims |
| Safety | соблюдены ли policy и approvals | unsafe actions, approval bypasses |
| Reliability | стабилен ли результат | regression rate, variance, retry success |
| Cost/latency | можно ли это эксплуатировать | token cost, p95 latency, tool count |

## Минимальный eval set

Для нового агента заведите 30-100 сценариев:

- happy path;
- edge cases;
- missing data;
- prompt injection в retrieved/inbox content;
- tool failure;
- ambiguous user request;
- destructive action без approval;
- long context;
- negative cases, где агент должен сказать “не знаю” или “нужен человек”.

## Структура тест-кейса

```yaml
id: support-refund-approval-001
goal: подготовить ответ клиенту по возврату
inputs:
  user_request: ...
  retrieved_docs: ...
expected:
  outcome: draft_created
  must_include: [policy citation, next step]
  must_not_call: [refund_payment]
  requires_approval: true
metrics:
  - task_success
  - policy_compliance
  - citation_accuracy
```

## Graders

Используйте несколько типов проверок:

- deterministic checks: JSON schema, наличие citations, запрет конкретного tool;
- reference checks: сравнение с golden answer;
- LLM-as-judge: полезно для качества, но требует calibration;
- human review: для спорных кейсов и high-risk доменов;
- replay checks: прогон старых traces после изменения prompt/model/tool schema.

## Regression workflow

1. Любой баг или инцидент становится eval case.
2. Перед изменением prompt/model/tool schema запускается baseline.
3. После изменения сравниваются pass rate, cost, latency, unsafe actions.
4. Если качество выросло, но cost/latency неприемлемы, изменение не считается готовым.
5. В production уходит только версия с зафиксированным eval report.

## Особенности agent evals

Обычные QA-evals часто пропускают важное:

- агент мог дать правильный финальный ответ, но вызвать опасный tool;
- агент мог получить правильный источник, но не процитировать его;
- агент мог решить задачу только из-за случайного порядка retrieved chunks;
- агент мог исчерпать бюджет, хотя answer выглядит хорошо.

Поэтому сохраняйте полный run trace и оценивайте path, а не только final answer.

## Источники

- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI Agents SDK: evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)
- [LlamaIndex Evaluating](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/)

## Связанные заметки

- [Observability и debugging](../tools/agent-observability-debugging.md)
- [Production operations](production-operations.md)
- [RAG для агентов](../patterns/rag-for-agents.md)
