# AI-агенты: база знаний по практическому применению

> Obsidian Vault · Git-репозиторий · Русский язык
> Версия: 0.1.0 · Обновлено: 2026-06-24

База знаний о практическом применении AI-агентов: архитектура, паттерны, инструменты, рабочие процессы, кейсы, сравнения и источники. Главная цель структуры — быстро находить нужную заметку и не дублировать одно и то же знание в разных местах.

## С чего начать

- [Карта знаний](navigation/knowledge-map.md) — главный маршрут по vault.
- [Learning path](navigation/learning-path.md) — порядок погружения от базовой таксономии до production.
- [Таксономия AI-агентов](concepts/agent-taxonomy.md) — assistant, workflow, agent, autonomous agent, multi-agent system.
- [Agent Harness](concepts/agent-harness.md) — из чего состоит рабочая обвязка вокруг агента.
- [Skills и правила для агентов](patterns/agent-skills-and-rules.md) — как оформлять переиспользуемые инструкции.
- [Работа с код-агентами](practices/working-with-coding-agents.md) — цикл постановки задачи, проверки и фиксации результата.
- [Исследование фреймворков](tools/agent-frameworks-research.md) — выбор OpenAI/Anthropic/LangGraph/AutoGen/CrewAI/LlamaIndex/low-code стека.

## Структура

| Раздел | Роль |
|---|---|
| [navigation](navigation/knowledge-map.md) | Карта vault, backlog, правила поиска |
| [concepts](concepts/overview.md) | Базовые понятия и архитектурные блоки |
| [patterns](patterns/overview.md) | Повторяемые проектные решения |
| [tools](tools/overview.md) | Модели, SDK, платформы, runtime |
| [practices](practices/recipes.md) | Workflow, recipes, практические инструкции |
| [cases](cases/overview.md) | Сценарии внедрения и разборы |
| [comparisons](comparisons/overview.md) | Матрицы выбора и сравнительные обзоры |
| [articles](articles/overview.md) | Переводы, конспекты, аналитика статей |
| [sources](sources/overview.md) | Внешние курсы, каналы, репозитории, provenance |
| [meta](meta/skills/add-source.md) | Шаблоны и проектные skills |

## Правило именования

- Пользовательские папки и Markdown-файлы называем строго на английском в `kebab-case`: `agent-harness.md`, `working-with-coding-agents.md`.
- Для обзорных страниц используем единое имя `overview.md`.
- Служебные dot-файлы и файлы инструментов могут сохранять стандартные имена экосистемы: `.gitignore`, `.gitlab-ci.yml`, `.githooks/pre-commit`.
- Порядок разделов задаётся этой таблицей и [картой знаний](navigation/knowledge-map.md), а не числовыми префиксами в названиях папок.

## Правило против дублей

Одна мысль должна иметь один основной дом:

- концепция живёт в `concepts/`;
- паттерн — в `patterns/`;
- инструмент или модель — в `tools/`;
- инструкция к действию — в `practices/`;
- внешний источник — в `sources/`;
- overview-файлы только навигируют и кратко объясняют, куда идти.

Если новая заметка повторяет существующую, нужно поставить ссылку на canonical note, а не копировать текст.

## Как добавлять материалы

1. Определить тип материала: концепция, паттерн, инструмент, практика, кейс, сравнение, статья или источник.
2. Создать заметку в соответствующем разделе.
3. Добавить ссылку в `overview.md` этого раздела.
4. Если материал пришёл из внешнего источника, добавить карточку в `sources/` по шаблону [source.md](meta/templates/source.md).
5. Запустить проверку:

```bash
bash scripts/validate-vault.sh
```

## Проверки

В проекте есть единый валидатор:

```bash
bash scripts/validate-vault.sh
```

Он проверяет:

- локальные Markdown-ссылки;
- наличие frontmatter у заметок в `sources/`;
- обязательные поля `title`, `url`, `type`, `category`, `tags`, `added`, `status`.

Та же проверка подключена в локальный pre-commit hook [.githooks/pre-commit](.githooks/pre-commit).

## Рабочие правила

- Связи между заметками делаем Markdown-ссылками на существующие файлы.
- Списки в обзорных страницах должны быть ссылками, если материал уже создан.
- Не оставляем битые ссылки как “заглушки”.
- После каждого изменения запускаем релевантные проверки, коммитим и пушим результат.
