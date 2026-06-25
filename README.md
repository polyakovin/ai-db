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
| [meta](meta/skills/add-source.md) | Шаблоны и проектные skills |

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

Если новая заметка повторяет существующую, нужно поставить ссылку на canonical note, а не копировать текст.

## Как добавлять материалы

1. Определить тип материала: концепция, паттерн, инструмент, практика, кейс, сравнение, статья или источник.
2. Создать заметку в соответствующем разделе.
3. Добавить ссылку в `OVERVIEW.md` этого раздела.
4. Если материал пришёл из внешнего источника, добавить карточку в `sources/` по шаблону [source.md](meta/templates/source.md).
5. Запустить проверку:

```bash
bash meta/scripts/validate-vault.sh
```

## Проверки

В проекте есть единый валидатор:

```bash
bash meta/scripts/validate-vault.sh
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
