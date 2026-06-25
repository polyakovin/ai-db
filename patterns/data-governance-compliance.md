# Data governance и compliance для AI-агентов

Агенты работают с контекстом, tools и памятью, поэтому governance должен покрывать не только model provider, но и весь путь данных: ingestion, retrieval, prompt, tool calls, logs, evals, memory и deletion.

## Что считать данными

- user prompts;
- retrieved documents;
- tool inputs/outputs;
- model outputs;
- traces;
- eval datasets;
- memory records;
- uploaded files;
- screenshots/browser state;
- generated artifacts.

## Классификация данных

| Класс | Примеры | Требования |
|---|---|---|
| Public | docs, public webpages | provenance |
| Internal | process docs, code, tickets | access control |
| Confidential | contracts, financial data | encryption, audit |
| PII | email, phone, HR records | minimization, retention |
| Secrets | tokens, keys, credentials | never in model context |
| Regulated | health, finance, legal | policy + legal review |

## Minimum governance checklist

1. Data inventory: какие данные видит агент.
2. Purpose limitation: зачем данные используются.
3. Access control: кто и какой tool может читать/писать.
4. Retention: сколько хранить prompts, traces, memory.
5. Deletion: как удалить user memory и artifacts.
6. Redaction: что убрать из logs/evals.
7. Provider review: какие данные уходят во внешний API.
8. Auditability: кто сделал действие и почему.
9. Human approval: где требуется человек.
10. Incident response: что делать при утечке или неверном действии.

## Memory governance

Memory особенно рискованна, потому что переживает одну сессию. Нужны:

- явное основание для записи;
- provenance;
- user-visible edit/delete;
- TTL для временных фактов;
- запрет на запись sensitive data без policy;
- periodic cleanup;
- evals на stale/incorrect memory.

## Evals и privacy

Eval datasets часто копируют реальные prompts. Перед сохранением:

- удалить PII;
- заменить реальные ids синтетическими;
- не включать secrets;
- пометить источник данных;
- ограничить доступ;
- хранить consent/legal basis, если требуется.

## Standards и ориентиры

- NIST AI RMF помогает управлять рисками для людей, организаций и общества.
- ISO/IEC 42001 задаёт рамку AI management system.
- Для персональных данных применяются локальные privacy laws и договоры обработки данных.

Primary sources:

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001](https://www.iso.org/standard/42001)

## Связанные заметки

- [Безопасность агентных систем](../patterns/agent-security.md)
- [RAG для агентов](../patterns/rag-for-agents.md)
- [Production operations](production-operations.md)
