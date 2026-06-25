# Execution loop агента

Execution loop — это повторяемый цикл, в котором агент видит состояние, выбирает действие, получает observation и решает, продолжать ли работу. Качество агента определяется не красотой prompt, а тем, насколько этот loop ограничен, наблюдаем и проверяем.

## Базовая форма

```text
goal -> state -> plan -> action -> observation -> update state -> stop or continue
```

Минимальные элементы:

- `goal` — ожидаемый outcome и критерии успеха;
- `state` — текущие факты, память, ограничения, доступные tools;
- `plan` — ближайшие шаги, а не обязательно полный долгосрочный план;
- `action` — tool call, вопрос человеку, запись в файл, финальный ответ;
- `observation` — результат действия, ошибка или новое внешнее состояние;
- `stop criteria` — условия завершения, эскалации или отказа.

## Роли внутри loop

| Слой | Ответственность |
|---|---|
| Модель | интерпретировать цель, выбирать следующий шаг, формировать аргументы |
| Harness | хранить state, вызывать tools, применять permissions, управлять retries |
| Tools | выполнять ограниченные операции и возвращать структурированные observations |
| Evals | проверять, что loop приводит к правильному outcome |
| Observability | сохранять trace, входы, выходы, tool calls и ошибки |

## Stop criteria

Без stop criteria агент склонен либо останавливаться слишком рано, либо продолжать бессмысленно. Минимальный набор:

- success: критерии выполнены и есть evidence;
- blocked: не хватает данных, доступа или решения человека;
- unsafe: действие нарушает policy или permissions;
- budget exceeded: лимит времени, токенов, стоимости, tool calls;
- low confidence: агент не может доказать, что результат корректен;
- repeated failure: одинаковая ошибка повторилась больше допустимого числа раз.

## Failure modes

| Ошибка | Симптом | Контрмера |
|---|---|---|
| Tool drift | агент выбирает неподходящий tool | улучшить descriptions и routing evals |
| Hidden state | важное решение осталось только в контексте | писать state/evidence во внешнее хранилище |
| Infinite loop | повторяются одни и те же действия | loop budget и repeated-failure detector |
| Premature final | агент отвечает без проверки | required verification gate |
| Unsafe side effect | tool вызван без approval | policy enforcement вне модели |
| Context decay | агент забывает constraints | context packing и summary checkpoints |

## Практический шаблон задачи

Перед запуском long-running агента задайте:

1. Outcome: что должно быть истинно в конце.
2. Scope: какие системы и файлы можно трогать.
3. Evidence: чем подтверждается результат.
4. Stop: когда остановиться или спросить.
5. Budget: лимит времени, стоимости и tool calls.
6. Review: какие действия требуют человека.

## Связанные заметки

- [Agent Harness](agent-harness.md)
- [Context engineering](context-engineering.md)
- [Production operations](../practices/production-operations.md)
