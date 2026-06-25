# Карта знаний

Эта карта показывает, где искать информацию и какой файл является источником истины для каждого типа знания.

## Принцип структуры

- `README.md` — короткий вход в проект и правила работы.
- `navigation/` — карта, learning path, служебная навигация.
- `concepts/` — удалён, всё в patterns/.
- `patterns/` — повторяемые решения, workflow, recipes, case-карта и how-to.
- `tools/` — модели, SDK, фреймворки, платформы, runtime, сравнения.
- `sources/` — статьи, переводы, курсы, обработанные источники и provenance.
- `meta/` — шаблоны и проектные skills.

Порядок разделов фиксируется этой картой и `README.md`. В именах папок не используем числовые префиксы: все пользовательские папки и Markdown-файлы называются на английском в `kebab-case`.

## Быстрый поиск по вопросу

| Если нужно | Идите сюда |
|---|---|
| Понять, в каком порядке изучать тему | [Learning path](learning-path.md) |
| Развести assistant, workflow, agent и multi-agent | [Таксономия AI-агентов](../patterns/fundamentals/agent-taxonomy.md) |
| Понять, из чего состоит агентная система | [Компоненты agent-системы](../patterns/architecture-design/agent-system-components.md) |
| Спроектировать harness вокруг агента | [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| Разобрать основной цикл агента | [Execution loop агента](../patterns/fundamentals/agent-execution-loop.md) |
| Спроектировать контекст и память | [Context engineering](../patterns/fundamentals/context-engineering.md) |
| Подключить tools или MCP | [Tool use, function calling и MCP](../patterns/fundamentals/tool-use-and-mcp.md) |
| Проверить безопасность agentic-системы | [Безопасность агентных систем](../patterns/architecture-design/agent-security.md) |
| Оформить правила или skill для агента | [Skills и правила для агентов](../patterns/implementation/agent-skills-and-rules.md) |
| Организовать работу с код-агентом | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| Настроить evals и production gates | [Evaluations для AI-агентов](../patterns/implementation/agent-evaluations.md) |
| Выбрать agent framework | [Исследование фреймворков](../tools/agent-frameworks-research.md) |
| Выбрать модель для агентного сценария | [Модельная карта для AI-агентов](../tools/agent-model-map.md) |
| Выбрать embedding-модель | [Модели для эмбеддингов](../tools/embedding-models.md) |
| Найти воспроизводимый рецепт | [Воспроизводимые рецепты AI-агентов](../patterns/advanced/reproducible-agent-recipes.md) |
| Выбрать архитектуру и evals под use case | [Карта кейсов AI-агентов](../patterns/advanced/agent-use-cases.md) |
| Найти обработанные внешние источники | [Источники — Обзор](../sources/OVERVIEW.md) |
|| Оценить картину целиком | [Learning path](learning-path.md) |

## Правило против дублей

Одна мысль должна иметь один основной дом:

- концепция живёт в `concepts/`;
- паттерн — в `patterns/`;
- инструкция к действию — в `practices/`;
- сведения о внешнем источнике — в `sources/`;
- обзор только ссылается и кратко объясняет, куда идти.

Если новая заметка повторяет существующую, нужно не копировать текст, а поставить ссылку на canonical note.
