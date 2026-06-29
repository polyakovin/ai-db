# Human-in-the-loop UX

Human-in-the-loop нужен не потому, что агент “плохой”, а потому что часть решений требует человеческой ответственности, контекста или доверия. Хороший UX делает участие человека точным и редким: подтверждать нужно именно риск, а не каждый шаг.

## Точки участия человека

| Момент | Когда нужен человек | UI/UX форма |
|---|---|---|
| Clarification | цель неоднозначна | короткий вопрос |
| Confirmation | side effect обратим, но важен | preview + approve |
| Approval | действие рискованное | explicit approval с evidence |
| Handoff | агент не может продолжить | очередь/тикет человеку |
| Review | результат влияет на клиента/деньги | diff, citations, audit |
| Feedback | улучшение evals | thumbs, labels, correction |

## Что показывать в approval

Approval screen должен включать:

- что агент собирается сделать;
- какие аргументы будут переданы tool;
- откуда взялись факты;
- expected side effect;
- confidence и known risks;
- rollback path;
- альтернативы: approve, edit, reject, ask follow-up.

## Clarification vs guessing

Агент должен спрашивать, если:

- есть несколько несовместимых трактовок;
- действие нельзя безопасно откатить;
- не хватает обязательного параметра;
- пользователь просит “сделай всё”, но scope не определён;
- есть конфликт между policy и request.

Но агент не должен спрашивать о том, что можно безопасно обнаружить через read-only tool.

## Trust design

Пользователь доверяет агенту, если видит:

- trace ключевых действий;
- citations;
- diff перед изменением;
- возможность отмены;
- ясные границы автономности;
- отсутствие скрытых side effects.

## Anti-patterns

- approval fatigue: спрашивать на каждом шаге;
- vague confirmation: “вы уверены?” без деталей;
- hidden automation: агент действует до preview;
- no edit path: можно только approve/reject;
- no ownership: непонятно, кто отвечает за ошибку.

## Связанные заметки

- [Безопасность агентных систем](../architecture-design/agent-security.md)
- [Production operations](production-operations.md)
- [Работа с код-агентами](../implementation/working-with-coding-agents.md)
- [Agent Harness](../architecture-design/agent-harness.md) — approvals и UX агента
- [Антипаттерны агентных систем](../advanced/agent-antipatterns.md) — последствия для UX
