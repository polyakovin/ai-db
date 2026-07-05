---
title: Know Your Unknowns — Thariq Shihipar
url: https://thariqs.github.io/html-effectiveness/unknowns/
type: url
category: sources
tags: [thariq, claude-code, anthropic, html-artifacts, unknowns, planning, code-review, prototyping]
added: 2026-07-05
status: processed
---

# Know Your Unknowns — Thariq Shihipar

**Название:** «Know your unknowns — examples»
**Автор:** Thariq Shihipar (`@trq212`), инженер Claude Code в Anthropic
**Платформа:** X Article + GitHub Pages (`thariqs.github.io/html-effectiveness/unknowns/`)
**Контекст:** Companion-материал к посту «The Unreasonable Effectiveness of HTML» (8M+ views на X, также опубликован в блоге Claude)

## Результаты обзора

### Главный тезис

**Карта — это не территория; разрыв между ними — твои неизвестные.** Статья предлагает 11 самостоятельных HTML-артефактов для обнаружения неизвестных на каждом этапе разработки: до, во время и после реализации.

### Структура

| Этап | Артефактов | Назначение |
|------|-----------|------------|
| **Pre-implementation** | 8 демо | Дешевле всего найти unknown до написания кода |
| **During implementation** | 1 демо | Лог отклонений от плана, который ведёт Claude |
| **Post-implementation** | 2 демо | Питч-документ и квиз перед мержем |

### 11 артефактов

01. **Blindspot pass** — Claude сканирует незнакомый auth-модуль и выдаёт 7 карт неизвестных с исправлениями
02. **Teach me my unknowns** — интерактивный explainer по color-grading (словарная лестница, live before/after)
03. **Four design directions** — четыре radically разных варианта UI одной очереди (ops console, editorial, kanban, terminal)
04. **Mock before you wire** — clickable throwaway mock тулбара с тремя вариантами размещения
05. **Brainstorm the intervention** — 10 привязанных к коду интервенций по churn
06. **The interview** — Claude интервьюирует вас по feature, сортируя вопросы по architectural blast radius
07. **Point at a reference** — семантическая карта porting Rust → TypeScript
08. **The tweakable plan** — план имплементации, сортированный по вероятности изменений
09. **Implementation notes** — лог Claude за 3-часовую сборку с каждым отклонением от плана
10. **The buy-in doc** — ship-it pitch с анимированным демо и пред-ответами на возражения ревьюеров
11. **Change quiz** — merge-readiness report с 6 вопросами; неверный ответ → указывает на пропущенную секцию

### Формат

Каждый артефакт — самодостаточный `.html` файл. На странице показан точный промпт (сверху) и результат, который Claude произвёл (снизу). Формат HTML выбран потому что:
- **Пространственная структура** — визуальные размещения несут информацию, которую текст сплющивает
- **Интерактивность** — слайдеры, чекбоксы, кликабельные прототипы
- **Evidence** — визуальные доказательства, а не текстовые описания

## Релевантность для ai-db

Статья напрямую связана с паттерном **HTML-артефактов как формата коммуникации с AI-агентами** — ключевая практика, которая перекликается с:

- **HTML форматом для планов и спецификаций** — альтернатива Markdown, дающая richer feedback loop
- **Прототипированием до кода** — throwaway моки как инструмент редукции неопределённости
- **Рефлексией агента** — implementation notes как deviation log
- **Техникой «слепых пятен»** — systematic scan для unknown unknowns

## Связи

- [The Unreasonable Effectiveness of HTML] *(если будет создана)*
- [Claude Code 101](../tutorials-courses/claude-code-101.md) — практика работы с Claude Code
- [Agent Skills and Rules](../../patterns/implementation/agent-skills-and-rules.md) — системный подход к качеству промптов
- [AI Foundations](../tutorials-courses/ai-foundations.md) — Claude ecosystem как среда разработки
- [Harness Engineering — OpenAI](../research-production/harness-engineering-openai.md) — обвязка агентов как детерминированная ценность

*Добавлено: 2026-07-05 (на основе анализа X Article и GitHub Pages)*
