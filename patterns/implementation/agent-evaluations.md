# Evaluations для AI-агентов

Eval для агента проверяет не один ответ модели, а весь workflow: достигнутый outcome, выбор tools, обработку ошибок, качество retrieved evidence, соблюдение policy, стоимость и способность остановиться. Если нужно оценить только final answer, смотри отдельную заметку [Оценка ответов LLM](llm-response-evaluation.md).

Оценивать нужно связку model + [agent harness](../architecture-design/agent-harness.md): инструкции, tools, orchestration и окружение влияют на результат не меньше самой модели.

## Из чего состоит agent eval

| Элемент | Что означает |
|---|---|
| Task / test case | входные данные и явно заданные критерии успеха |
| Trial | одна попытка выполнить task; для недетерминированного агента нужны повторные trials |
| Grader | кодовая, model-based или human-проверка одного аспекта результата |
| Transcript / trace / trajectory | полный ход trial: сообщения, reasoning, tool calls и промежуточные результаты |
| Outcome | конечное состояние среды: созданная запись, изменённый файл, проведённый возврат |
| Evaluation harness | инфраструктура, которая запускает trials, изолирует окружение, хранит traces, вызывает graders и агрегирует метрики |
| Evaluation suite | набор tasks для общей capability или поведения |

Не путайте evaluation harness с [agent harness](../architecture-design/agent-harness.md): первый тестирует, второй даёт модели возможность действовать.

## Что измерять

| Уровень | Вопрос | Метрики |
|---|---|---|
| Task success | решена ли задача | pass rate, exact outcome, human score |
| Tool use | правильно ли выбран tool | tool precision/recall, invalid calls |
| Grounding | опирается ли ответ на источники | citation accuracy, unsupported claims |
| Safety | соблюдены ли policy и approvals | unsafe actions, approval bypasses |
| Reliability | стабилен ли результат | regression rate, variance, retry success |
| Cost/latency | можно ли это эксплуатировать | token cost, p95 latency, tool count |

## Capability и regression suites

Эти наборы решают разные задачи и требуют разных ожиданий:

| Suite | Главный вопрос | Нормальный baseline | Как использовать |
|---|---|---|---|
| Capability / quality | что агент пока умеет и где предел | намеренно невысокий pass rate | улучшать prompts, tools, harness и модель; добавлять более сложные задачи при насыщении |
| Regression | не сломалось ли то, что уже работало | близко к 100% | запускать на каждое значимое изменение и блокировать подтверждённый откат |

Стабильно решаемые capability tasks переводите в regression suite. Eval с почти 100% полезен против откатов, но перестаёт показывать рост возможностей.

## Минимальный eval set

Начните с 20-50 простых сценариев: ручных проверок команды, продуктовых требований, багов и обращений пользователей. На ранней стадии этого обычно достаточно, чтобы заметить крупные изменения; по мере зрелости расширяйте набор и повышайте сложность.

Включите:

- happy path;
- edge cases;
- missing data;
- prompt injection в retrieved/inbox content;
- tool failure;
- ambiguous user request;
- destructive action без approval;
- long context;
- negative cases, где агент должен сказать “не знаю” или “нужен человек”.

Набор должен быть сбалансированным: проверяйте и случаи, где поведение должно сработать, и случаи, где оно неуместно. Например, eval для web search обязан ловить как undertriggering, так и overtriggering.

Каждый task должен:

- одинаково трактоваться двумя domain experts;
- сообщать всё, что проверяет grader, включая пути, форматы и ограничения;
- иметь reference solution, которая доказывает решаемость задачи и корректность graders;
- запускаться из чистого, воспроизводимого состояния.

Если сильный агент получает 0% после множества trials, сначала ищите неоднозначность task, ошибку grader или ограничение harness, а не делайте вывод о capability модели.

## Структура тест-кейса

```yaml
id: support-refund-approval-001
goal: подготовить ответ клиенту по возврату
trials: 5
inputs:
  user_request: ...
  retrieved_docs: ...
expected:
  outcome: draft_created
  must_include: [policy citation, next step]
  must_not_call: [refund_payment]
  requires_approval: true
graders:
  - type: state_check
    expect: {draft_status: created}
  - type: deterministic
    checks: [policy_compliance, citation_accuracy]
  - type: llm_rubric
    rubric: support-quality.md
tracked_metrics: [task_success, token_cost, latency, tool_count]
```

## Graders

Комбинируйте типы проверок, выбирая самый простой надёжный grader для каждого критерия:

| Тип | Подходит для | Ограничения |
|---|---|---|
| Code-based | unit tests, schema, static analysis, state и tool-policy checks | дёшев и воспроизводим, но хрупок к валидным вариациям |
| Model-based | rubric scoring, natural-language assertions, pairwise comparison, открытые ответы | масштабируется и видит нюансы, но недетерминирован и требует human calibration |
| Human | expert review, spot checks, high-risk и субъективные случаи | лучший эталон для спорного качества, но дорог и медленен |

Практическое правило: deterministic graders там, где возможно; model-based там, где нужна семантика; human review — для калибровки и сложных решений. Для составной задачи используйте несколько graders и partial credit, если частичный успех действительно полезен.

Model-based grader делите на отдельные измерения с ясными rubrics. Разрешайте ответ `unknown`, когда evidence недостаточно, и регулярно сравнивайте оценки с domain experts.

## Outcome важнее жёстко заданного path

Сохраняйте полный trace, но не требуйте без необходимости конкретный порядок tool calls: агент может найти корректный путь, которого автор eval не предусмотрел.

Приоритет проверки:

1. Проверить реальный outcome в среде, а не заявление агента об успехе.
2. Проверить обязательные safety, policy и authorization invariants по trace.
3. Оценить качество взаимодействия, groundedness и полноту через rubrics.
4. Собирать turns, tool calls, tokens, cost и latency как диагностические метрики.

Точное следование path оправдано только тогда, когда сам путь является требованием: например, identity verification перед финансовым действием. В остальных случаях trace нужен прежде всего для объяснения провала, поиска grader bugs и выявления неэффективности.

## Недетерминированность и повторные trials

Один запуск не показывает надёжность агента. Выполняйте несколько независимых trials и выбирайте метрику под продуктовый контракт. Если вероятность успеха одного trial равна `p`, то при независимых попытках:

- `pass@k = 1 - (1 - p)^k` — вероятность хотя бы одного успеха за `k` попыток; подходит, когда допустимо предложить несколько решений;
- `pass^k = p^k` — вероятность успеха во всех `k` попытках; подходит для customer-facing действий, где важна стабильность каждого запуска.

Всегда фиксируйте число trials и доверительный интервал или хотя бы размер выборки рядом с агрегированным score. Не сравнивайте варианты по единичным прогонам.

## Стабильное eval-окружение

Eval должен воспроизводить production-поведение агента, не добавляя собственный шум:

- начинайте каждый trial с чистого состояния;
- не переиспользуйте файлы, кэш, историю или данные предыдущих trials;
- фиксируйте versions модели, prompts, tools, dependencies и fixtures;
- отслеживайте infrastructure failures отдельно от agent failures;
- не допускайте общей нехватки ресурсов, создающей коррелированные ошибки.

Shared state способен как занизить score из-за flakiness, так и завысить его через leakage между попытками.

## Regression workflow

1. До реализации capability сформулировать её как tasks и success criteria.
2. Любой баг, инцидент или повторяемая ручная проверка превращается в eval case.
3. Перед изменением prompt/model/tool schema запустить baseline.
4. После изменения сравнить success, reliability, cost, latency и unsafe actions на нескольких trials.
5. Прочитать выборку успешных и проваленных transcripts: провал должен быть справедливым и объяснимым.
6. Если качество выросло, но cost/latency неприемлемы, изменение не считать готовым.
7. В production отправлять только версию с зафиксированным eval report.
8. Назначить владельца suite, принимать tasks от product/domain experts и пересматривать насыщенные или устаревшие evals.

## Особенности agent evals

Обычные QA-evals часто пропускают важное:

- агент мог дать правильный финальный ответ, но вызвать опасный tool;
- агент мог получить правильный источник, но не процитировать его;
- агент мог решить задачу только из-за случайного порядка retrieved chunks;
- агент мог исчерпать бюджет, хотя answer выглядит хорошо.

Поэтому проверяйте outcome и обязательные invariants, сохраняйте полный run trace и регулярно читайте transcripts. Score нельзя принимать за истину, пока команда не убедилась, что tasks однозначны, graders справедливы, среда стабильна, а harness не ограничивает валидные решения.

## Не ограничиваться offline evals

Автоматические evals — первая линия до релиза и в CI, а не полная картина production-качества. Дополняйте их:

- production monitoring для drift и неизвестных failure modes;
- A/B tests для реальных продуктовых outcomes;
- user feedback и bug reports как источник новых tasks;
- регулярным manual transcript review;
- systematic human studies для high-risk или субъективных задач и калибровки model-based graders.

Ни один слой не ловит все ошибки. Надёжный контур соединяет воспроизводимые offline evals, production-сигналы и периодический human review.

## Источники

- [Demystifying evals for AI agents — Anthropic](../../sources/research-production/demystifying-evals-for-ai-agents.md)
- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI Agents SDK: evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)
- [LlamaIndex Evaluating](https://developers.llamaindex.ai/python/framework/module_guides/evaluating/)

## Связанные заметки

- [Observability и debugging](../../tools/observability/OVERVIEW.md)
- [Оценка ответов LLM](llm-response-evaluation.md)
- [Production operations](../production-operations/production-operations.md)
- [RAG для агентов](../architecture-design/rag-for-agents.md)
