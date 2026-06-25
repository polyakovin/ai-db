---
title: BitGN Arena — архитектурные инсайты с PAC1
url: https://bitgn.com/insights/
type: url
category: sources
tags: [bitgn, pac1, arena]
added: 2026-06-25
status: new
---

1|# BitGN Arena — архитектурные инсайты с PAC1
2|
**Источник:** https://bitgn.com/insights/  
**Челлендж:** PAC1 (Personal Agent Challenge) — детерминированная оценка агентов  
**Формат:** Публичные эксперименты, сотни агентов, слепая оценка (blind submission)

## Что это такое

BitGN Arena — бенчмарк, где агенты соревнуются на реальных задачах: обработка входящих, финансы, CRM, работа с документами, безопасность. Оценка — точность на PAC1, самый строгий лидерборд: один слепой сабмит, ранжирование по абсолютной точности.

## Ключевые инсайты

| Архитектура | Автор | Счёт | Ключевая идея |
|---|---|---|---|
| Operation Pangolin | Illia Dzivinskyi (Grammarly) | **92.0** (Ultimate #1) | Один инструмент — `execute_code` + строгий чеклист + REPL-цикл + durable memory |
| Codex-on-Rails | Igor Inozemtsev (Nevis) | **87.0** (Accuracy #1) | Frontier coding agent + MCP-мост + «рельсы» (валидация, trust boundaries, grounding) |
| Codex CLI + Rules Evolution | Maksim Popkov (Sber) | **84.0** | Разделение runtime и evolution-лупа; ~100 строк AGENTS.md; атомарные правки правил |
| Filesystem Agent | Azamat Yelmagambetov | **83.0** | Один сильный агент + классификатор сценариев + маленькие workflow-скиллы |
| Plan-REPL Agent | Grigory-T | **60.6** | Plan-and-REPL, typed step outputs — но упёрся в лимиты промпт-инжиниринга |

## Общие паттерны топ-решений

1. **Один сильный coding agent** — не мультиагент, а один LLM + жёсткие рельсы
2. **Минимум инструментов** — Pangolin: `execute_code` только; Codex-on-Rails: 6 vault-тулов
3. **Валидация вне модели** — grounding refs от рантайма, не от модели; синтаксическая проверка записей
4. **Trust boundaries** — inbox-данные как **data, not instructions**
5. **Strict completion contract** — `TaskResult` с outcome codes, не натуральный текст
6. **Эволюция через failure analysis** — не само-модификация, а отдельный loop для правок

## Связи с другими заметками

- Harness Engineering — тот же тренд: «один агент + лёгкая обвязка»
- Plan-and-Execute — Pangolin как REPL-реализация
- Guardrails — Codex-on-Rails и trust boundaries
- Agent-to-agent review — Rules Evolution как внешний loop
- MCP-протокол — Codex-on-Rails использует MCP как мост
- Codex CLI

---

*Добавлено: 2026-06-21*
