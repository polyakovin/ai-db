# Карта знаний

Эта карта показывает, где искать информацию и какой файл является источником истины для каждого типа знания.

## Принцип структуры

- `README.md` — короткий вход в проект и правила работы.
- `navigation/` — карта, backlog, служебная навигация.
- `concepts/` — базовые понятия и архитектурные строительные блоки.
- `patterns/` — повторяемые решения и правила проектирования.
- `tools/` — модели, SDK, фреймворки, платформы, runtime.
- `practices/` — прикладные workflow, recipes и how-to.
- `cases/` — практические сценарии внедрения и разборы.
- `comparisons/` — матрицы выбора и сравнительные обзоры.
- `sources/` — статьи, переводы, курсы и обработанные источники.
- `sources/` — provenance: внешние курсы, репозитории, каналы, документация.
- `meta/` — шаблоны и проектные skills.

Порядок разделов фиксируется этой картой и `README.md`. В именах папок не используем числовые префиксы: все пользовательские папки и Markdown-файлы называются на английском в `kebab-case`.

## Быстрый поиск по вопросу

| Если нужно | Идите сюда |
|---|---|
| Понять, в каком порядке изучать тему | [Learning path](learning-path.md) |
| Развести assistant, workflow, agent и multi-agent | [Таксономия AI-агентов](../concepts/agent-taxonomy.md) |
| Понять, из чего состоит агентная система | [Компоненты agent-системы](../concepts/agent-system-components.md) |
| Спроектировать harness вокруг агента | [Agent Harness](../concepts/agent-harness.md) |
| Разобрать основной цикл агента | [Execution loop агента](../concepts/agent-execution-loop.md) |
| Спроектировать контекст и память | [Context engineering](../concepts/context-engineering.md) |
| Подключить tools или MCP | [Tool use, function calling и MCP](../concepts/tool-use-and-mcp.md) |
| Проверить безопасность agentic-системы | [Безопасность агентных систем](../concepts/agent-security.md) |
| Оформить правила или skill для агента | [Skills и правила для агентов](../patterns/agent-skills-and-rules.md) |
| Организовать работу с код-агентом | [Работа с код-агентами](../practices/working-with-coding-agents.md) |
| Настроить evals и production gates | [Evaluations для AI-агентов](../practices/agent-evaluations.md) |
| Выбрать agent framework | [Исследование фреймворков](../tools/agent-frameworks-research.md) |
| Выбрать модель для агентного сценария | [Модельная карта для AI-агентов](../tools/agent-model-map.md) |
| Выбрать embedding-модель | [Модели для эмбеддингов](../tools/embedding-models.md) |
| Найти воспроизводимый рецепт | [Воспроизводимые рецепты AI-агентов](../practices/reproducible-agent-recipes.md) |
| Найти обработанные внешние источники | [Источники — Обзор](../sources/overview.md) |
| Посмотреть backlog | [Backlog](backlog.md) |

## Правило против дублей

Одна мысль должна иметь один основной дом:

- концепция живёт в `concepts/`;
- паттерн — в `patterns/`;
- инструкция к действию — в `practices/`;
- сведения о внешнем источнике — в `sources/`;
- обзор только ссылается и кратко объясняет, куда идти.

Если новая заметка повторяет существующую, нужно не копировать текст, а поставить ссылку на canonical note.
