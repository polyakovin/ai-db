# Лог решений

| Дата | Решение | Причина | Альтернативы |
|------|---------|---------|--------------|
| 2026-06-24 | Ветка master вместо main | HEAD ремоута — master | main |
| 2026-06-24 | Файловая структура harness (meta/, AGENTS.md) в корне | Единая точка входа для агента | Разнести по проекту |
| 2026-06-24 | validate-vault.sh как Python-скрипт (не Bash) | Надёжный парсинг Markdown, кроссплатформенность | Bash с grep/sed |
| 2026-06-29 | validate-canonical-refs.py как Python-скрипт | Сложная логика: исключение frontmatter, кодовых блоков, таблиц | Bash-эвристики |
| 2026-06-29 | Три уровня проверок в pre-commit (generate map → validate vault → check bare mentions) | Полная автоматизация; нельзя закоммитить битые ссылки или bare mentions | Ручной запуск каждого шага |
| 2026-06-29 | canonical-map.json генерируется из tools/ структуры | Единый источник истины, не требует ручной синхронизации | Ручное ведение JSON |
| 2026-07-02 | Обзор автоматизации сбора внешнего контекста размещён в `patterns/architecture-design/` | Тема описывает архитектурный pipeline и governance, а не отдельный инструмент; provenance вынесен в `sources/` | Новый top-level раздел; каталог инструментов в `tools/` |
| 2026-07-02 | Оценка ответов LLM вынесена в отдельную implementation-заметку | `agent-evaluations.md` описывает workflow-level evals, а final answer требует собственных criteria, rubrics и judge workflow | Расширить `agent-evaluations.md` одним длинным разделом |
| 2026-07-02 | Поисковые сервисы для агентов описаны в `tools/agent-tools/web-search.md` как категорийный обзор | Задача была на обзор выбора; отдельные canonical-страницы по Tavily/Exa/Serper/Brave/Firecrawl стоит создавать только при внедрении или отдельном benchmark | Создать отдельную страницу на каждый search provider сразу |
| 2026-07-02 | Claude Science добавлен как source + раздел в canonical-странице Anthropic | Это продукт Anthropic вокруг Claude, а не отдельная модель; отдельная tool-страница преждевременна без глубокой оценки продукта | Создать `tools/platforms/claude-science.md` |
| 2026-07-02 | Обзор поддержки качества контекста размещён в `patterns/architecture-design/` | Тема связывает базы знаний, БД, retrieval, governance и evals как архитектурную операционную практику для агентов | Расширить только `context-engineering.md` или `rag-for-agents.md` |
| 2026-07-02 | LightRAG вынесен в canonical `tools/retrieval/lightrag.md`, а аналоги описаны категорийным обзором `tools/retrieval/lightrag-alternatives.md` | LightRAG уже был source-карточкой, но факты об инструменте должны жить в `tools/`; аналоги нужны как карта выбора, а не как набор преждевременных canonical-страниц | Оставить LightRAG только в `sources/`; создать отдельную tool-страницу для каждого аналога сразу |
