# DeepSeek GUI

**Source:** [deepseek-gui.com](https://www.deepseek-gui.com/)  
**GitHub:** [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI)  
**Latest version:** 0.2.4 (Jun 6, 2026)

---

## Что это

Локальный desktop workbench для DeepSeek, работающий поверх **Kun runtime** — собственного агентного движка. Замена простого чат-интерфейса на полноценную среду: Code, Write, внешние сообщения (Feishu/Lark), SDD-требования, планы, goals.

## Ключевые особенности

### Kun Runtime
- Локальный HTTP/SSE agent loop — один boundary для threads, events, approvals, usage
- **Cache-first оптимизация** — стабильные system prefixes + tool schemas → высокий cache hit
- Целевой cache hit rate: **90%+** на тёплых threads
- Progressive MCP discovery (3-step: `mcp_search` → `mcp_describe` → `mcp_call`)
- Telemetry через DeepSeek-native `prompt_cache_hit_tokens` / `prompt_cache_miss_tokens`

### Режимы

| Режим | Описание |
|-------|----------|
| **Code** | Projects, workspaces, plans, goals, visible file changes |
| **Write** | Markdown-редактор + превью + AI-полишинг inline |
| **Connect Phone** | Feishu/Lark интеграция, webhook/relay, scheduled tasks |

### SDD Workflow (Structured Requirement-Driven)
1. Draft — capture background, goals, acceptance criteria, images
2. Requirement AI заполняет gaps — ищет проект, задаёт вопросы
3. Executable plan → `.kunsdd/plan` Markdown artifact → synced todos in GUI

### Write / FIM (Inline Completion)
- Dual timer modes: short (650ms) и long (2800ms)
- Раздельные token budgets, acceptance rules, prompts
- RAG: BM25 + keyword boosts (без векторов), 30s TTL cache

## Доступность

- **macOS** (Apple Silicon / Intel) — DMG, ZIP
- **Windows** — EXE
- **Linux** — только сборка из исходников

## Relevance для ai-db

Полезен как:
- Референтс агентного runtime с cache-first архитектурой
- Пример локального MCP-ориентированного agent loop
- Реализация progressive tool discovery (альтернатива полной загрузке всех схем)
- Desktop UI для agent workflow (Code + Write + SDD)
