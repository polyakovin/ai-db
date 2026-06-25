---
name: agent-harness-generator
description: Создать агентскую обвязку (harness) для нового проекта по принципам ai-db
type: skill
---

# Скилл: Генерация агентской обвязки (Agent Harness)

## Назначение
Создаёт полную рабочую обвязку вокруг AI-агента для нового проекта: файловую структуру, system prompt, правила, память, инструменты, hooks, sandbox, subagents, наблюдаемость и CI — на основе принципов из базы знаний `ai-db`.

## Когда применять
- Ты создаёшь новый проект, в котором будет работать AI-агент.
- Нужно быстро развернуть минимальный, но полный harness, а не писать всё вручную.
- Нужно, чтобы агент имел: rules, skills, hooks, память, subagents, sandbox и наблюдаемость.

## Алгоритм

### 1. Определить профиль проекта
Уточни у пользователя (или в контексте):

| Параметр | Пример |
|----------|--------|
| Название проекта | `my-agent-project` |
| Тип агента | coding / research / RAG / support / browser / SQL |
| Язык/стек | Python / TypeScript / Go |
| Git-репозиторий | Да / Нет |
| Нужен UI | Да / Нет |
| Нужны subagents | Да / Нет |
| Нужен CI/CD | GitHub Actions / GitLab CI / Нет |
| Внешняя ссылка на ai-db | URL репозитория или локальный путь |

### 2. Создать файловую структуру harness

Создай следующую структуру в корне проекта (все директории — `mkdir -p`):

```
<project>/
├── .hermes/                    # Harness: правила и память агента
│   ├── rules/                  # agent system rules (проектные правила)
│   │   └── project-rules.md    #    — стабильные правила поведения
│   ├── memory/                 # память проекта
│   │   └── project-memory.md   #    — предпочтения, решения, conventions
│   ├── skills/                 # модульные навыки для агента
│   │   ├── tdd.md              #    — test-driven development
│   │   ├── debug.md            #    — systematic debugging
│   │   └── review.md           #    — code review workflow
│   ├── sandbox/                # политики безопасности
│   │   └── security-policy.md  #    — allowlist, approvals, границы
│   ├── observability/          # логирование и traces
│   │   └── audit-log.md        #    — шаблон audit-записей
│   └── subagents/              # правила делегирования (если нужны)
│       └── subagent-rules.md   #    — как и когда использовать subagents
├── AGENTS.md                   # Точка входа для агента
├── SKILL.md                    # Проектные skill-правила (для Hermes)
├── .githooks/                  # Hooks: автоматические проверки
│   └── pre-commit              #    — перед каждым коммитом
├── scripts/                    # Утилиты и валидаторы
│   ├── lint.sh                 #    — линтеры
│   ├── test.sh                 #    — запуск тестов
│   └── validate.sh             #    — проверка состояния проекта
├── plan/                       # Файловая рабочая память агента
│   ├── current.md              #    — текущий план задачи
│   ├── evidence/               #    — промежуточные findings
│   └── decisions.md            #    — принятые решения и rationale
├── tests/                      # Eval set
│   └── ...                     #    — по типу проекта
├── .github/                    # CI (если GitHub)
│   └── workflows/
│       └── ci.yml
└── README.md                   # Точка входа для человека
```

### 3. Создать AGENTS.md

Создай `AGENTS.md` в корне проекта — точку входа для агента. Заполни все `<...>` плейсхолдеры под профиль проекта.

```markdown
# AGENTS.md — правила для AI-агента

## Проект
- **Название:** <project-name>
- **Тип агента:** <type>
- **Язык:** <language>
- **Цель:** <одно предложение>

## Как агент работает

1. **Перед началом** — прочитай `plan/current.md`, загрузи skill, проверь git status.
2. **Выполняй** — минимальными порциями, каждая с проверкой.
3. **Пиши evidence** — результаты и наблюдения в `plan/evidence/`.
4. **Фиксируй решения** — важные выборы, причины, альтернативы в `plan/decisions.md`.
5. **Проверяй** — тесты, линтеры, валидацию после каждого meaningful изменения.
6. **Commit** — atomic, message с ссылкой на задачу.

## Ограничения (STOP)
- Не изменяй файлы вне scope задачи.
- Не пиши speculative код «на будущее».
- Не удаляй dead code, который не ты создал (если не указано иное).
- Если не уверен — запиши вопрос в `plan/decisions.md` с confidence score.
- Destructive actions (deploy, write, delete) требуют подтверждения.

## Инструменты
- <список инструментов, e.g.: shell, filesystem, git, browser>
- <если MCP — перечислить серверы>
- <если subagents — правила из `.hermes/subagents/subagent-rules.md`>

## Проверки
| Тип | Команда |
|-----|---------|
| Линтер | `scripts/lint.sh` |
| Тесты | `scripts/test.sh` |
| Валидация | `scripts/validate.sh` |

## Память проекта
- **System rules:** `.hermes/rules/project-rules.md`
- **Project memory:** `.hermes/memory/project-memory.md`
- **Work plan:** `plan/current.md`
- **Decisions:** `plan/decisions.md`
- **Security policy:** `.hermes/sandbox/security-policy.md`
- **Audit log:** `.hermes/observability/audit-log.md`

## Связанные материалы
- [Agent Harness — ai-db](../../concepts/agent-harness.md)
- [Работа с код-агентами — ai-db](../../practices/working-with-coding-agents.md)
- [Skills и правила — ai-db](../../patterns/agent-skills-and-rules.md)
- [Безопасность агентных систем — ai-db](../../concepts/agent-security.md)
- [Multi-agent orchestration — ai-db](../../concepts/multi-agent-orchestration.md)
```

### 4. Создать базовые правила (.hermes/rules/project-rules.md)

На основе разделов концепций ai-db: Agent Harness, Skills и правила, Execution loop, Context engineering.

```markdown
# Project Rules для AI-агента

Стабильные правила, которые агент **всегда** применяет.

## Принципы
- **Think before coding:** явно назвать предположения, неоднозначности и tradeoffs.
- **Simplicity first:** не добавлять speculative flexibility.
- **Surgical changes:** менять только то, что связано с задачей.
- **Goal-driven execution:** команды → проверяемые критерии успеха.

## Рабочий цикл
1. Уточнить цель и scope.
2. Сделать план (≤ 5 шагов).
3. Выполнить маленькими порциями.
4. Проверить (тесты, линтеры, валидация).
5. Зафиксировать след (commit + evidence).

## Стоп-критерии
- Успех: критерии выполнены, есть evidence.
- Блокировка: не хватает данных, доступа или решения человека.
- Unsafe: action нарушает policy.
- Budget: превышен лимит попыток/времени.
- Repeated failure: одинаковая ошибка > 2 раз.

## Tool policy
- Все destructive actions — с подтверждением.
- Секреты — вне контекста (env vars, vault).
- Результаты tool calls — структурированно, source+date.
- Каждый tool call логируется в `.hermes/observability/audit-log.md`.
```

### 5. Создать project-memory.md (.hermes/memory/project-memory.md)

```markdown
# Project Memory — <project-name>

## Основное
- **Название:** <project-name>
- **Тип:** <project-type>
- **Создан:** <YYYY-MM-DD>
- **Язык/стек:** <language>

## Конвенции
- <convention 1>
- <convention 2>

## Принятые решения
| Дата | Решение | Причина | Альтернативы |
|------|---------|---------|--------------|
|      |         |         |              |

## Предпочтения
- <preference 1>
```

### 6. Создать security-policy (.hermes/sandbox/security-policy.md)

```markdown
# Security Policy

## Tool allowlist
- Разрешены: shell (non-destructive), filesystem (read/write в scope), git, browser (read-only)
- Запрещены: rm -rf, curl | bash, eval, exec на непроверенном вводе

## Approval gates
- Destructive actions → подтверждение пользователя
- Deploy → подтверждение
- Изменение production-данных → подтверждение
- Удаление файлов → подтверждение

## Secrets
- Секреты только в env vars или vault — НИКОГДА в контексте модели.

## Audit
- Каждый tool call логируется: timestamp, tool, arguments (redacted), результат, cost.
- Лог ведётся в `.hermes/observability/audit-log.md`.
```

### 7. Создать pre-commit hook (.githooks/pre-commit)

```bash
#!/usr/bin/env bash
# Pre-commit hook: запускает проверки перед коммитом
set -euo pipefail

echo "🔍 Pre-commit checks..."

# 1. Линтер
if [ -f scripts/lint.sh ]; then
  bash scripts/lint.sh || { echo "❌ Lint failed"; exit 1; }
fi

# 2. Тесты
if [ -f scripts/test.sh ]; then
  bash scripts/test.sh || { echo "❌ Tests failed"; exit 1; }
elif [ -f Makefile ]; then
  make test || { echo "❌ Tests failed"; exit 1; }
fi

# 3. Валидация
if [ -f scripts/validate.sh ]; then
  bash scripts/validate.sh || { echo "❌ Validation failed"; exit 1; }
fi

echo "✅ All checks passed"
```

### 8. Создать начальный план (plan/current.md)

```markdown
# Текущий план

## Цель
<что должно быть истинно в конце>

## Шаги
- [ ] Шаг 1: <описание> → проверка: <как проверить>
- [ ] Шаг 2: <описание> → проверка: <как проверить>
- ...

## Открытые вопросы
- <вопрос> — <статус>

## Evidence
Ссылки на файлы в `plan/evidence/`
```

### 9. Создать CI (в зависимости от выбора)

**GitHub Actions** — `.github/workflows/ci.yml`:
```yaml
name: CI
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: scripts/lint.sh
      - run: scripts/test.sh
      - run: scripts/validate.sh
```

**GitLab CI** — `.gitlab-ci.yml`:
```yaml
stages:
  - check

check:
  stage: check
  image: ubuntu:latest
  script:
    - bash scripts/lint.sh
    - bash scripts/test.sh
    - bash scripts/validate.sh
```

### 10. Создать правила subagents (если нужны)

Если в профиле `subagents: Да`, создай `.hermes/subagents/subagent-rules.md`:

```markdown
# Subagent Rules

## Когда использовать subagent
- Задача раскладывается на независимые части.
- Нужен отдельный reviewer.
- Нужно исследовать альтернативы без загрязнения контекста.
- Нужно параллелить работу.

## Правила делегирования
- Каждый subagent получает: цель, scope, ожидаемый выход, критерии проверки.
- Subagent пишет результат в `plan/evidence/<subagent-name>.md`.
- Subagent НЕ модифицирует файлы вне своего scope.
- Родительский агент проверяет результат subagent перед использованием.

## Бюджет
- Максимум <N> subagents параллельно.
- Лимит попыток на subagent: <M>.
```

### 11. Сгенерировать базовые skills

Для каждого skill в `.hermes/skills/` создай минимальный каркас.

**tdd.md:**
```markdown
# TDD Workflow

## Когда использовать
Перед реализацией любой функции или исправлением бага.

## Алгоритм
1. Напиши failing test.
2. Запусти — убедись, что он падает.
3. Напиши минимальный код для прохождения.
4. Запусти — убедись, что проходит.
5. Refactor при необходимости.
6. Commit.

## Проверка
- test(s) проходят
- coverage не уменьшился
```

**debug.md:**
```markdown
# Systematic Debugging

## Когда использовать
При любой ошибке в коде, тестах или инфраструктуре.

## Алгоритм
1. Воспроизведи ошибку.
2. Прочитай полный stack trace / лог ошибки.
3. Сформулируй гипотезу о причине.
4. Проверь гипотезу минимальным изоляционным тестом.
5. Напиши тест, ловящий баг.
6. Исправь.
7. Убедись, что тест проходит и старые тесты не сломаны.

## Проверка
- Ошибка не воспроизводится.
- тест на регрессию добавлен.
```

**review.md:**
```markdown
# Code Review Workflow

## Когда использовать
После завершения реализации, перед коммитом или после открытия PR.

## Алгоритм
1. Прочитай diff — каждая строка связана с задачей?
2. Проверь на минимальный diff: нет лишних форматирований, комментариев, рефакторинга.
3. Проверь на safety: нет ли секретов, опасных команд, необработанных input-ов.
4. Запусти тесты и линтер.
5. Если есть замечания — исправь или запиши в decisions.md.

## Проверка
- diff связан с задачей.
- tests pass.
- lint pass.
- Нет unsafe-изменений.
```

### 12. Настроить git hooks

```bash
git config core.hooksPath .githooks
```

## Проверка результата

После генерации:
- [ ] Вся структура создана (директории и файлы).
- [ ] `AGENTS.md` заполнен под проект — все `<...>` заменены.
- [ ] `.hermes/rules/project-rules.md` заполнен.
- [ ] `.hermes/memory/project-memory.md` не пустой (есть имя проекта и дата).
- [ ] `.hermes/sandbox/security-policy.md` создан.
- [ ] `.githooks/pre-commit` создан и executable (`chmod +x .githooks/pre-commit`).
- [ ] `git config core.hooksPath .githooks` выполнен.
- [ ] `plan/` содержит начальный план.
- [ ] `scripts/` содержит lint.sh, test.sh, validate.sh (хотя бы заглушки).
- [ ] `scripts/validate.sh` запускается и возвращает 0 (smoke test).
- [ ] Если нужен CI — заполнен (CI-файл выбранного типа).
- [ ] Если `subagents: Да` — созданы `.hermes/subagents/subagent-rules.md`.
- [ ] Все ссылки в AGENTS.md ведут на существующие файлы.
- [ ] `.hermes/skills/` не пустой (минимум 3 файла с содержимым).
- [ ] `README.md` обновлён (упоминание harness и AGENTS.md).

## Частые ошибки

- **Пустой AGENTS.md:** важно заполнить тип агента, инструменты и ограничения — иначе агент не знает границ.
- **Нет stop criteria:** агент будет работать бесконечно или останавливаться раньше времени.
- **Pre-commit без проверок:** создавать пустой hook бесполезно.
- **Память проекта не заполнена:** project-memory.md должен стартовать с имени проекта и базовых conventions.
- **План в AGENTS.md vs. plan/:** AGENTS.md говорит КАК работать, `plan/current.md` — ЧТО делать прямо сейчас. Не путать.
- **Security-policy только упомянут:** без actual allowlist и approval gates агент может выполнить опасное действие.
- **Subagents без правил:** если subagents разрешены, без правил делегирования они будут декоративными.
- **Плейсхолдеры не заменены:** все `<...>` в AGENTS.md и project-memory.md должны быть заменены на конкретные значения для проекта.

## Связанные материалы
- [ai-db: Agent Harness](../../concepts/agent-harness.md)
- [ai-db: Skills и правила](../../patterns/agent-skills-and-rules.md)
- [ai-db: Работа с код-агентами](../../practices/working-with-coding-agents.md)
- [ai-db: Execution loop](../../concepts/agent-execution-loop.md)
- [ai-db: Context engineering](../../concepts/context-engineering.md)
- [ai-db: Безопасность агентных систем](../../concepts/agent-security.md)
- [ai-db: Multi-agent orchestration](../../concepts/multi-agent-orchestration.md)
