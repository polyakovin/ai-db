---
title: Demystifying evals for AI agents
url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
type: url
category: sources
tags: [anthropic, agents, evals, graders, reliability, production]
added: 2026-07-22
status: used
---

# Demystifying evals for AI agents

- **Источник:** Anthropic Engineering, 9 января 2026
- **Авторы:** Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe
- **Оригинал:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

## Что это

Практическое руководство Anthropic по оценке coding, conversational, research и computer-use агентов. Материал опирается на внутреннюю работу Anthropic и опыт команд, внедряющих агентов, и описывает общий словарь evals, типы graders, метрики недетерминированности и путь от первых tasks до обслуживаемого production-набора.

## Устойчивые выводы

- Agent eval должен разделять task, trial, grader, transcript, outcome, evaluation harness и evaluation suite.
- Capability и regression suites отвечают на разные вопросы: первая показывает пространство для роста, вторая защищает уже достигнутое качество.
- Начальный набор можно строить из 20-50 реальных ручных проверок, багов и пользовательских обращений, не дожидаясь сотен cases.
- Tasks должны быть однозначными, сбалансированными позитивными и негативными примерами и иметь рабочее reference solution.
- Надёжная оценка сочетает deterministic, model-based и human graders; LLM judges требуют регулярной калибровки с экспертами.
- Предпочтительно оценивать outcome, сохраняя trace для safety checks и диагностики, а не фиксировать единственно допустимый порядок действий.
- Нестабильность измеряется повторными trials: `pass@k` отражает шанс хотя бы одного успеха, а `pass^k` — последовательную надёжность.
- Eval-окружение должно изолировать trials, исключать shared state и отделять infrastructure flakiness от ошибок агента.
- Suites требуют владельца, чтения transcripts, пополнения реальными failures и обновления при насыщении.
- Offline evals дополняют, но не заменяют production monitoring, A/B tests, user feedback и human review.

## Ограничения источника

Это engineering guidance, а не формальный стандарт. Авторы прямо отмечают, что практика agent evals быстро развивается; конкретные размеры наборов, число trials и сочетание graders нужно адаптировать к риску, зрелости продукта и стоимости ошибки.

## Интеграция в vault

- [Evaluations для AI-агентов](../../patterns/implementation/agent-evaluations.md) — добавлены терминология, capability/regression suites, outcome-first grading, повторные trials, изоляция среды и lifecycle eval-набора.

## Статус

Добавлено и интегрировано: 2026-07-22.
