# Ресурсы

Коллекция ключевых статей, исследований и переводов по теме AI-агентов. Раздел организован по типам источников: от туториалов до research.

---

## 🟢 Tutorials & Courses

*Обучающие материалы: курсы, воркшопы, плейлисты.*

- [Claude Code 101](tutorials-courses/claude-code-101.md) — CLI-agent workflow, постановка задач и проверка
- [OpenAI Academy](tutorials-courses/openai-academy.md) — structured agent work, workflow checkpoints
- [AI Foundations](tutorials-courses/ai-foundations.md) — Claude ecosystem, Projects как memory, Skills
- [Zinho Automates](tutorials-courses/zinho-automates.md) — end-to-end automation, Scheduled Tasks, Skills
- [Teacher's Tech](tutorials-courses/teachers-tech.md) — chat → build → agentic, типичные ошибки новичков

## 🔵 Libraries & Tools

*Инструментарий для сборки агентов: библиотеки, фреймворки, SDK.*

- [LangChain Deep Agents](libraries-tools/langchain-deep-agents.md) — harness, filesystem, subagents, context management, sandbox boundary
- [Superpowers](libraries-tools/superpowers.md) — skills workflow, TDD, systematic debugging, review loops
- [ECC](libraries-tools/ecc.md) — harness OS, memory persistence, hooks, verification loops, security
- [Perplexity AI](libraries-tools/perplexity.md) — AI-поиск с агентными возможностями

## 🟡 Engineering Patterns

*Практические эксперименты и архитектурные решения: BitGN, Codex, Plan-REPL.*

- [BitGN Arena — Insights](engineering-patterns/bitgn-arena-insights.md) — архитектурные инсайты
- [BitGN Codex CLI — Rules Evolution](engineering-patterns/bitgn-codex-cli-rules-evolution.md)
- [BitGN Codex on Rails](engineering-patterns/bitgn-codex-on-rails.md)
- [BitGN Filesystem Agent](engineering-patterns/bitgn-filesystem-agent.md)
- [BitGN Operation Pangolin](engineering-patterns/bitgn-operation-pangolin.md)
- [BitGN Plan-REPL Agent](engineering-patterns/bitgn-plan-repl-agent.md)

## 🟠 Research & Production

*Исследования, production-практики, хардкорные доклады.*

- [Harness Engineering — OpenAI](research-production/harness-engineering-openai.md) — Open AI/Anthropic подходы к обвязке агентов
- [Andrej Karpathy Skills](research-production/andrej-karpathy-skills.md) — think before coding, simplicity, surgical changes, goal-driven execution

---

## Сводная таблица

| Источник | Категория | Куда перенесено |
|----------|-----------|-----------------|
| [OpenAI Academy](tutorials-courses/openai-academy.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [AI Foundations](tutorials-courses/ai-foundations.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md) |
| [Zinho Automates](tutorials-courses/zinho-automates.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md) |
| [Teacher's Tech](tutorials-courses/teachers-tech.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [LangChain Deep Agents](libraries-tools/langchain-deep-agents.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| [Claude Code 101](tutorials-courses/claude-code-101.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Superpowers](libraries-tools/superpowers.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [ECC](libraries-tools/ecc.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [OpenMontage](libraries-tools/openmontage.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Perplexity AI](libraries-tools/perplexity.md) | 🔵 Libraries | [Perplexity (tools)](../tools/platforms/perplexity.md) — canonical |
| [Andrej Karpathy Skills](research-production/andrej-karpathy-skills.md) | 🟠 Research | [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |

---

## Как добавлять

При добавлении нового источника — создавай файл в подходящей подпапке и добавляй строку в сводную таблицу.

### Single Source of Truth для всей базы

Каждая сущность имеет единственную canonical страницу. Ниже — где что живёт и шаблон для каждого типа.

#### Инструменты, платформы, модели → `tools/`

Структура страницы инструмента:
```markdown
---
title: <Название>
url: <официальная ссылка>
type: url
category: tools
tags: []
added: <YYYY-MM-DD>
status: new
---

# <Название>

Краткое описание.

## Ключевые возможности

## Модели / Продукты

## Цены и доступ

## Агентные возможности

## Open Source статус

## Use Cases

## Отзывы и критика

## Связи

- [[../../patterns/...|...]] — какие паттерны используют этот инструмент
```

**Правила:**
- Все ссылки на инструмент из patterns, sources и других tools ведут на его страницу (Single Source of Truth)
- Страница инструмента не дублирует контент patterns, а даёт факты о самом инструменте
- Инструменты появляются как отдельные страницы до того, как на них начнут ссылаться из patterns
- Если инструмент уже есть в `sources/libraries-tools/`, он тоже должен появиться в `tools/` с фокусом на факты (sources остаётся как provenance-заметка про источник знаний)

#### Архитектурные паттерны → `patterns/`

Каноническая страница паттерна — единственное место, где описано **решение** (проблема → архитектура → когда применять). Все остальные заметки ссылаются на него.

Структура:
```markdown
# <Название паттерна>

## Проблема

## Решение

## Когда применять / Когда не применять

## Связанные паттерны

- [[../../tools/...|...]] — какие инструменты реализуют этот паттерн
```

#### Источники → `sources/`

Каноническая страница источника — provenance: что это, автор, дата, relevance. Не содержит пересказа содержания на уровне паттернов.

Структура — существующий шаблон `meta/templates/source.md`:
```yaml
---
title: <название>
url: <ссылка>
type: url
category: sources
tags: []
added: <YYYY-MM-DD>
status: new
---
```

Тело: описание, обзор ресурса, Связи (ссылки на patterns, куда перенесена выжимка).

#### Практические workflow → `patterns/implementation/`

Структура (по шаблону skills):
- Когда использовать
- Алгоритм
- Проверка результата
- Частые ошибки
- Связанные инструменты (ссылки на `tools/`)
- Связанные паттерны (ссылки на `patterns/`)

*Последнее обновление: 29.06.2026*
