# AI-агенты: база знаний по практическому применению

База знаний о практическом применении AI-агентов: архитектура, паттерны, инструменты, рабочие процессы, кейсы, сравнения и источники. Главная цель структуры — быстро находить нужную заметку и не дублировать одно и то же знание в разных местах.

## С чего начать

- [Patterns OVERVIEW](patterns/OVERVIEW.md) — оглавление раздела с learning path.
- [Таксономия AI-агентов](patterns/fundamentals/agent-taxonomy.md) — assistant, workflow, agent, autonomous agent, multi-agent system.
- [Agent Harness](patterns/architecture-design/agent-harness.md) — из чего состоит рабочая обвязка вокруг агента.
- [Skills и правила для агентов](patterns/implementation/agent-skills-and-rules.md) — как оформлять переиспользуемые инструкции.
- [Работа с код-агентами](patterns/implementation/working-with-coding-agents.md) — цикл постановки задачи, проверки и фиксации результата.
- [Исследование фреймворков](tools/agent-frameworks-research.md) — выбор OpenAI/Anthropic/LangGraph/AutoGen/CrewAI/LlamaIndex/low-code стека.

## Структура

| Раздел | Роль |
|---|---|
| [patterns](patterns/OVERVIEW.md) | Архитектурные блоки, проектные решения, workflow, recipes, learning path, case-карта, how-to |
| [tools](tools/OVERVIEW.md) | Модели, SDK, платформы, runtime |
| [sources](sources/OVERVIEW.md) | Статьи, переводы, курсы, обработанные источники и provenance |
| [meta](meta/project-rules.md) | Шаблоны и проектные skills |

## Правило именования

- Пользовательские папки и Markdown-файлы называем строго на английском в `kebab-case`: `agent-harness.md`, `working-with-coding-agents.md`.
- Для обзорных страниц используем единое имя `OVERVIEW.md`.
- Служебные dot-файлы и файлы инструментов могут сохранять стандартные имена экосистемы: `.gitignore`, `.gitlab-ci.yml`, `.githooks/pre-commit`.
- Порядок разделов задаётся этой таблицей, а не числовыми префиксами в названиях папок.

## Правило против дублей

Одна мысль должна иметь один основной дом:

- архитектура, паттерн или решение — в `patterns/`;
- инструмент или модель — в `tools/`;
- инструкция к действию — в `patterns/`;
- внешний источник — в `sources/`;
- overview-файлы только навигируют и кратко объясняют, куда идти.

### Single Source of Truth

Каждая сущность в базе знаний имеет **единственную canonical страницу**, где живут её факты. Все остальные заметки **только ссылаются** на эту страницу — никогда не дублируют её содержание.

| Сущность | Где canonical страница | Что содержит |
|----------|-----------------------|-------------|
| Инструмент, платформа, провайдер, модель | `tools/` (или `tools/models/`, `tools/platforms/`) | Факты: возможности, модели, цены, Open Source статус, агентные фичи, use cases |
| Архитектурный паттерн, компонент, решение | `patterns/` | Проблема → Решение → Когда применять → Связанные паттерны |
| Внешний источник (статья, курс, видео) | `sources/` (provenance) | Что это, откуда, автор, дата, relevance, обзор ресурса |
| Практический workflow, рецепт, how-to | `patterns/implementation/` или `patterns/production-operations/` | Пошаговый алгоритм, проверка, частые ошибки |

**Как это работает на практике:**

1. Если нужно описать Claude Code — факты о нём пишутся один раз в `tools/platforms/anthropic.md` или `tools/claude-code.md`
2. Если `patterns/implementation/working-with-coding-agents.md` описывает workflow с Claude Code — он **ссылается** на страницу Claude Code, а не копирует цены/модели
3. Если `patterns/advanced/agent-antipatterns.md` упоминает ошибки Claude Code — он **ссылается** на страницу Claude Code
4. Если меняется цена Claude Code — правка в одном месте

**Проверка:** найди любую информацию в двух разных заметках. Если она одна и та же — это дубль, который нужно заменить ссылкой на canonical страницу.

Подробный шаблон для инструментов — в [[sources/OVERVIEW.md#правило-инструменты-и-платформы--отдельные-страницы|sources/OVERVIEW → шаблон]].

Если новая заметка повторяет существующую, нужно поставить ссылку на canonical note, а не копировать текст.

## Как добавлять материалы

1. Определить тип материала: концепция, паттерн, инструмент, практика, кейс, сравнение, статья или источник.
2. Создать заметку в соответствующем разделе.
3. Добавить ссылку в `OVERVIEW.md` этого раздела.
4. Если материал пришёл из внешнего источника, добавить карточку в `sources/` по шаблону [source.md](meta/templates/source.md).
5. Запустить проверку:

```bash
python3 meta/scripts/validate-vault.sh
```

## Проверки

В проекте есть три уровня валидации:

1. **Валидация vault** (битые ссылки, frontmatter):
```bash
python3 meta/scripts/validate-vault.sh
```

2. **Canonical cross-reference** (bare mentions → wiki-links):
```bash
python3 meta/scripts/validate-canonical-refs.py
```

3. **Регенерация canonical-map.json** (из tools/ структуры):
```bash
python3 meta/scripts/generate-canonical-map.py
```

Он проверяет:

- локальные Markdown-ссылки;
- наличие frontmatter у заметок в `sources/`;
- обязательные поля `title`, `url`, `type`, `category`, `tags`, `added`, `status`.

Все три проверки подключены в локальный pre-commit hook [.githooks/pre-commit](.githooks/pre-commit).

## Canonical Map

Проект использует единый реестр технологий — [meta/canonical-map.json](meta/canonical-map.json). Он генерируется автоматически:

```bash
python3 meta/scripts/generate-canonical-map.py
```

Скрипт сканирует все `.md` файлы в `tools/`, извлекает название из frontmatter `title:` или h1, и создаёт JSON-маппинг `{slug: {name, path}}`. Map используется:

- **validate-canonical-refs.py** — проверяет, что все упоминания технологий в `patterns/` и `tools/` оформлены как wiki-ссылки на canonical страницу
- **pre-commit hook** — автоматически регенерирует map и запускает проверку перед каждым коммитом

### Правила ссылок на canonical страницы

1. Каждый инструмент/платформа имеет **одну** canonical страницу в `tools/`
2. Все остальные заметки **только ссылаются** на canonical страницу, не дублируя факты
3. Ссылки оформляются относительным путём от файла к canonical странице (например, `../../tools/perplexity.md`)
4. Bare mentions (текстовые упоминания без ссылок) недопустимы — их ловит `validate-canonical-refs.py`

## Рабочие правила

- Связи между заметками делаем Markdown-ссылками на существующие файлы.
- Списки в обзорных страницах должны быть ссылками, если материал уже создан.
- Не оставляем битые ссылки как “заглушки”.
- После каждого изменения запускаем релевантные проверки, коммитим и пушим результат.
