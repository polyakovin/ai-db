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

## Always-on персональные агенты

Ассистент, постоянно подключённый к мессенджерам, web, памяти и shell, имеет больший attack surface, чем интерактивный coding agent. Для такого deployment:

1. Использовать отдельный непривилегированный host/container и не монтировать лишние пользовательские каталоги.
2. Разделять credentials по интеграциям, ограничивать scopes и иметь быстрый revoke path.
3. Не открывать control plane в публичную сеть без authentication, TLS и явной необходимости.
4. Считать email, chat, web pages, documents и community skills недоверенным вводом.
5. Проверять source и diff каждого skill/plugin; автоматический malware scan не ловит все prompt-injection и intent-manipulation атаки.
6. Регулярно обновлять runtime и запускать доступный security audit.
7. Ограничивать число шагов, wall-clock time, token/cost budget и повторные ошибки tools.

Практические симптомы неверных границ — самостоятельное изменение конфигурации после вопроса, runaway loops, silent background work и потеря контроля над token budget — зафиксированы в [hands-on гайде по OpenClaw](../../sources/tutorials-courses/openclaw-habr-guide.md).

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
- [OpenClaw](../../tools/platforms/openclaw.md) — self-hosted always-on агент как reference threat model
