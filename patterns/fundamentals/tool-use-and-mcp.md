# Tool use, function calling и MCP

Tools превращают модель из генератора текста в участника системы, который может читать данные, запускать действия и менять внешнее состояние. Поэтому tool use — это не только API-интеграция, но и контракт безопасности.

## Function calling

Function calling полезен, когда модель должна выбрать одну из заранее описанных функций и вернуть структурированные аргументы. Хороший tool contract содержит:

- название, отражающее действие;
- описание, когда tool использовать и когда не использовать;
- JSON schema входных параметров;
- side effects;
- идемпотентность;
- ошибки и retry policy;
- требования approval;
- формат observation.

[OpenAI](../../tools/platforms/openai.md) рекомендует помещать большую часть tool-specific guidance в описания tools, а не раздувать общий prompt. См. официальные страницы [Function calling](https://developers.openai.com/api/docs/guides/function-calling) и [Using tools](https://developers.openai.com/api/docs/guides/tools).

## MCP

MCP — открытый стандарт подключения AI-приложений к внешним системам: файлам, базам, search, workflow и специализированным prompts. Официальная документация описывает MCP как стандартный порт между AI-приложением и внешними системами: [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro).

Практическая роль MCP:

- уменьшает число одноразовых интеграций;
- отделяет client от server;
- позволяет переиспользовать один tool server в разных agent clients;
- делает capabilities явными;
- требует отдельной security модели для permissions и trust boundary.

## Tool schema checklist

Перед добавлением tool проверьте:

1. Может ли действие быть read-only.
2. Какие параметры обязательны.
3. Можно ли безопасно повторить вызов.
4. Есть ли dry-run режим.
5. Какие ошибки возвращаются структурировано.
6. Какие действия требуют approval.
7. Что попадёт в logs.
8. Как ограничить доступ по scope.

Если каталог schemas становится большим, применяйте [progressive disclosure](../implementation/progressive-disclosure-for-agents.md): держите частые и критичные tools в стартовом контексте, остальные находите и раскрывайте по запросу. Deferred loading уменьшает контекстный шум, но не заменяет permission и approval.

## Масштабирование большой tool surface

Количество подключённых MCP-серверов не равно количеству схем, которые нужно одновременно отправлять модели. Чем больше похожих tools видит модель, тем выше риск sibling confusion, лишний расход контекста и сложнее cross-server переходы.

Практический pipeline:

1. Соберите eval-набор для single-step выбора, аргументов и multi-step цепочек.
2. Оставьте небольшой curated default set из наиболее надёжных инструментов.
3. Для длинного хвоста находите релевантные schemas через metadata или retrieval и передавайте модели только top-K.
4. При сложном запросе разделите planning, выбор одного инструмента и synthesis результата.
5. Для write и destructive действий ставьте approval после выбора инструмента, но до исполнения.

[LocalCowork](../../tools/platforms/localcowork.md) — полезный reference: репозиторий содержит 75 tools, но стартует с проверенным подмножеством, а для расширенного каталога предлагает planner/router pipeline. Это архитектурная гипотеза, которую нужно подтвердить собственными evals, а не готовая гарантия качества.

## Permissions

Минимальные уровни:

| Уровень | Пример | Требование |
|---|---|---|
| Read-only | поиск, чтение файла | логирование |
| Low-risk write | создание черновика | rollback или review |
| External side effect | отправка email, webhook | confirmation |
| Destructive | delete, payment, prod deploy | explicit approval и audit |
| Privileged | secrets, admin APIs | отдельный policy gate |

## Fallback и retry

Retry не должен быть автоматическим для всего. Безопасный retry возможен, если:

- tool идемпотентен;
- ошибка временная;
- аргументы не меняют смысл действия;
- лимит попыток мал;
- observation сохраняется.

Если ошибка связана с permissions, schema или policy, retry должен остановиться и вернуть blocked state.

## Связанные заметки

- [Безопасность агентных систем](../architecture-design/agent-security.md)
- [Agent Harness](../architecture-design/agent-harness.md)
- [Production operations](../production-operations/production-operations.md)
- [Skills и правила для агентов](../implementation/agent-skills-and-rules.md) — skills как специализированные инструкции tool use
- [Работа с код-агентами](../implementation/working-with-coding-agents.md) — инструменты код-агента
- [Multi-agent orchestration](../implementation/multi-agent-orchestration.md) — MCP для межагентной коммуникации
- [OpenAI](../../tools/platforms/openai.md) — Responses API как tool use implementation
- [Anthropic (Claude)](../../tools/platforms/anthropic.md) — MCP-серверы в Claude Code
- [LangGraph](../../tools/frameworks/langgraph.md) — tool calling в LangGraph
- [Progressive disclosure для AI-агентов](../implementation/progressive-disclosure-for-agents.md) — deferred discovery больших каталогов tools
- [LocalCowork](../../tools/platforms/localcowork.md) — локальный MCP-agent с curated tool set и planner/router pipeline
