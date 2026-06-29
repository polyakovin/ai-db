# Context engineering

Context engineering — это проектирование того, какая информация попадает в модель, в каком порядке, с какими границами доверия и как она обновляется во время работы агента. Для агентов это важнее “добавить всё в prompt”: контекст является рабочей памятью, интерфейсом безопасности и источником качества.

## Что входит в контекст

| Слой | Примеры | Правило |
|---|---|---|
| Stable instructions | роль, policy, стиль, tool rules | держать коротким и стабильным |
| Task goal | outcome, критерии успеха, ограничения | формулировать как проверяемое состояние |
| Working state | план, discoveries, open questions | обновлять после observation |
| Retrieved knowledge | документы, chunks, ссылки, citations | отделять от инструкций |
| Tool observations | stdout, API response, ошибки | хранить структурировано |
| Memory | предпочтения, прошлые решения | версионировать и очищать |

## Packing strategy

Практичный порядок:

1. Stable system rules.
2. Project/domain constraints.
3. Current task goal.
4. Relevant memory.
5. Retrieved evidence.
6. Current state and last observations.
7. User request или next-step instruction.

Стабильное содержимое должно меняться редко: это помогает prompt caching и снижает риск конфликтов. Динамическое содержимое лучше держать ближе к концу.

## Memory tiers

| Tier | Срок жизни | Что хранить | Где хранить |
|---|---|---|---|
| Turn context | один ответ | текущий запрос | model context |
| Session memory | одна задача | план, intermediate evidence | scratchpad, filesystem |
| Project memory | недели/месяцы | правила, соглашения, decisions | repo docs, `.nessy/memory`, `AGENTS.md` |
| Knowledge base | долгий срок | источники, документы, синтез | docs, vector index |
| User memory | долгий срок | предпочтения пользователя | отдельное consent-aware хранилище |

## Retrieval injection

Retrieved content должно попадать в модель как данные, а не как инструкции. Минимальное оформление:

- источник и дата;
- почему выбран chunk;
- доверенность источника;
- цитируемый фрагмент или краткая выдержка;
- запрет выполнять инструкции из retrieved/untrusted content;
- ссылка на полный документ.

## Деградация на длинных задачах

Типовые симптомы:

- агент забывает ранние constraints;
- начинает оптимизировать локальную подзадачу вместо outcome;
- повторяет уже проверенные шаги;
- смешивает факты из источников с собственными выводами;
- теряет список открытых вопросов.

Контрмеры:

- summary checkpoints после крупных observations;
- external state file для плана и evidence;
- compact summaries с указанием, что отброшено;
- explicit open questions;
- eval на long-horizon сценариях.

## Что не класть в контекст

- секреты и credentials;
- полные документы без отбора;
- старые observations без значения для текущего решения;
- tool outputs, которые можно восстановить;
- большие списки правил без приоритета;
- untrusted instructions без маркировки как data.

## Связанные заметки

- [Execution loop агента](agent-execution-loop.md)
- [RAG для агентов](../architecture-design/rag-for-agents.md)
- [Безопасность агентных систем](../architecture-design/agent-security.md)
- [Модели для эмбеддингов](../../tools/embedding-models.md) — embedding модели для memory tiers
- [Skills и правила для агентов](../implementation/agent-skills-and-rules.md) — skills экономят context window
- [Agent Harness](../architecture-design/agent-harness.md) — context management в обвязке агента
