# Безопасность агентных систем

Агентная безопасность строится вокруг простой идеи: если агент может вызвать tool, он потенциально может сделать всё, что позволяет этот tool. Prompt не является достаточной границей безопасности; границы должны жить в harness, permissions, sandbox, audit и product policy.

## Главные угрозы

| Угроза | Что происходит | Контрмера |
|---|---|---|
| Prompt injection | untrusted content пытается изменить инструкции | маркировать данные как data, не как instructions |
| Sensitive disclosure | модель раскрывает секреты или PII | не помещать секреты в контекст, redaction, DLP |
| Excessive agency | агент получает слишком широкие права | least privilege, approvals, scoped tools |
| Improper output handling | вывод модели исполняется без проверки | schema validation, escaping, sandbox |
| Data poisoning | knowledge base или embeddings загрязнены | provenance, ingestion review, evals |
| Tool misuse | выбран неверный tool или опасные аргументы | policy gate, typed schema, dry-run |
| Unbounded consumption | runaway loop тратит деньги и квоты | budgets, rate limits, stop criteria |

OWASP Top 10 for LLM Applications 2025 отдельно выделяет prompt injection, sensitive information disclosure, excessive agency, vector/embedding weaknesses и unbounded consumption: [OWASP Gen AI Security Project](https://genai.owasp.org/llm-top-10/).

## Trust boundary

Разделяйте:

- trusted system instructions;
- project rules;
- user instruction;
- retrieved documents;
- inbox/email/web content;
- tool observations;
- generated output.

Документы, письма, страницы браузера и API-ответы не должны становиться инструкциями для агента. Они являются данными, даже если внутри написано “ignore previous instructions”.

## Minimum viable security

Для любого агента с tools:

1. Tool allowlist.
2. Approval для destructive и external side effects.
3. Sandbox для shell, browser, code execution.
4. Секреты вне model context.
5. Structured logging всех tool calls.
6. Бюджеты на токены, время, деньги и количество действий.
7. Red-team набор prompt injection примеров.
8. Incident path: как остановить агента и отозвать доступы.

## Human approval

Approval нужен не “для всего”, а для действий, где ошибка дорога:

- отправка сообщений от имени пользователя;
- изменение production данных;
- платежи и заказы;
- удаление файлов;
- деплой;
- доступ к секретам;
- юридически значимые решения.

Approval screen должен показывать не только “да/нет”, но и: действие, аргументы, источник решения, expected side effect, rollback path.

## Audit log

Минимальный audit record:

- run id;
- user/request id;
- model и версия;
- tool name;
- arguments после redaction;
- approval status;
- observation summary;
- cost/latency;
- итоговый outcome.

## Связанные заметки

- [Tool use, function calling и MCP](../fundamentals/tool-use-and-mcp.md)
- [Production operations](../production-operations/production-operations.md)
- [Data governance и compliance](../architecture-design/data-governance-compliance.md)
