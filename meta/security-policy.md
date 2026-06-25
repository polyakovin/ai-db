# Security Policy

## Tool allowlist
- Разрешены: shell (non-destructive), filesystem (read/write в scope проекта), git, web_search, web_extract.
- Запрещены: rm -rf без подтверждения, curl | bash, eval на непроверенном вводе.

## Approval gates
- Destructive actions (удаление файлов, перезапись истории git) → подтверждение пользователя.
- Deploy на production-сервер → подтверждение.
- Изменение секретов в конфигах → подтверждение.

## Secrets
- Секреты только в env vars или vault — НИКОГДА в контексте модели.
- Не читать и не логировать secrets.

## Audit
- Каждый tool call логируется: timestamp, tool, результат.
- Лог ведётся в `meta/observability/audit-log.md`.
