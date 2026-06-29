# TODO.md — Аудит cross-reference связей в ai-db

Дата аудита: 2026-06-29. Файлов: 90 .md. Все существующие ссылки валидны — `validate-vault.sh` проходит.

**Обновление 29.06.2026 (рефакторинг):**
- ✅ README.md: `bash` → `python3`, добавлен раздел «Canonical Map», исправлена ссылка на meta/
- ✅ AGENTS.md: обновлены команды проверок, добавлены все 3 шага pre-commit
- ✅ meta/scripts/*.sh: `bash validate-vault.sh` → `python3 validate-vault.sh`
- ✅ meta/decisions.md: создан лог решений
- ✅ .gitignore: добавлены `__pycache__/`, `*.pyc`, `*.pyo`
- ✅ meta/project-rules.md: исправлен путь audit-log, `overview.md` → `OVERVIEW.md`
- ✅ validate-canonical-refs.sh: заменён на тонкую обёртку над .py
- ✅ 12 stub-страниц (codex-cli, cursor, langchain, langsmith, cohere, ollama, vllm, gradio, huggingface, chroma, qdrant, flowise): добавлен контент
- ✅ canonical-map.json: перегенерирован (35 записей, все с валидными путями)

---

## A. Недостающие секции «Связанные заметки» / «См. также»

### A1. P0 — Ключевые заметки БЕЗ секции cross-reference (только «Источники»)

Эти три файла — ядро базы — не содержат секции «Связанные заметки» и потому не ссылаются на другие patterns/tools:

1. **`patterns/architecture-design/agent-harness.md`**
   - Добавить `## Связанные заметки` после `## Источники` (строка 99).
   - Должен ссылаться на:
     - `../fundamentals/agent-taxonomy.md` — таксономия агентов
     - `../fundamentals/agent-execution-loop.md` — execution loop
     - `../fundamentals/context-engineering.md` — context packing, memory tiers
     - `../fundamentals/tool-use-and-mcp.md` — tools, MCP, permissions
     - `../architecture-design/agent-security.md` — security at the boundary, sandbox
     - `../architecture-design/agent-system-components.md` — карта компонентов
     - `../implementation/agent-skills-and-rules.md` — skills
     - `../implementation/working-with-coding-agents.md` — coding agent workflow
     - `../implementation/multi-agent-orchestration.md` — subagents, orchestration
     - `../implementation/agent-evaluations.md` — evals как часть harness
     - `../production-operations/production-operations.md` — production deployment
     - `../production-operations/human-in-the-loop-ux.md` — approvals, HITL
     - `../../tools/observability/OVERVIEW.md` — observability
     - `../../tools/agent-frameworks-research.md` — выбор фреймворка
     - `../../tools/agent-model-map.md` — выбор модели
     - `../../sources/libraries-tools/openmontage.md` — agent-first архитектура

2. **`patterns/implementation/agent-skills-and-rules.md`**
   - Добавить `## Связанные заметки` после `## Источники` (строка 91).
   - Должен ссылаться на:
     - `../architecture-design/agent-harness.md` — где живут skills
     - `../architecture-design/agent-system-components.md` — компоненты системы
     - `../fundamentals/context-engineering.md` — контекст, куда skills подгружаются
     - `../fundamentals/agent-execution-loop.md` — skills как часть loop
     - `working-with-coding-agents.md` — практическое применение
     - `agent-evaluations.md` — проверка качества skills
     - `../advanced/agent-antipatterns.md` — вредные skills
     - `../../tools/agent-frameworks-research.md` — фреймворки с поддержкой skills
     - `../../sources/libraries-tools/openmontage.md` — stage director skills

3. **`patterns/implementation/working-with-coding-agents.md`**
   - Добавить `## Связанные заметки` после `## Источники` (строка 87).
   - Должен ссылаться на:
     - `../architecture-design/agent-harness.md` — harness вокруг coding agent
     - `../architecture-design/agent-security.md` — approval, sandbox, destructive actions
     - `../fundamentals/agent-execution-loop.md` — verification loop ↔ execution loop
     - `../fundamentals/context-engineering.md` — project memory, AGENTS.md
     - `agent-skills-and-rules.md` — skills для coding
     - `agent-evaluations.md` — проверки: тесты, линтеры
     - `multi-agent-orchestration.md` — subagents для review
     - `../production-operations/human-in-the-loop-ux.md` — когда спросить
     - `../advanced/agent-antipatterns.md` — over-agentification, weak evals
     - `../advanced/reproducible-agent-recipes.md` — coding agent recipe
     - `../../tools/agent-frameworks-research.md` — Claude Code, Codex
     - `../../tools/agent-model-map.md` — выбор coding-модели
     - `../../sources/libraries-tools/openmontage.md` — coding agent оркестрация

---

### A2. P1 — Заметки БЕЗ cross-reference секции (sources без «Связи»)

Следующие источники не содержат секции cross-reference (ни «Связи», ни «См. также», ни «Связанные заметки»):

4. **`sources/tutorials-courses/claude-code-101.md`**
   - Добавить `## Связи` после `## Статус` (строка 37).
   - Ссылаться на:
     - `../../patterns/implementation/working-with-coding-agents.md`
     - `../../tools/agent-frameworks-research.md`

5. **`sources/tutorials-courses/openai-academy.md`**
   - Добавить `## Связи` после `## Синтез` (строка 63).
   - Ссылаться на:
     - `../../patterns/implementation/working-with-coding-agents.md`
     - `../../patterns/implementation/agent-skills-and-rules.md`
     - `../../patterns/implementation/agent-evaluations.md`

6. **`sources/tutorials-courses/ai-foundations.md`**
   - Добавить `## Связи` после `## Синтез` (строка 51).
   - Ссылаться на:
     - `../../patterns/implementation/working-with-coding-agents.md`
     - `../../patterns/implementation/agent-skills-and-rules.md`
     - `../../tools/agent-frameworks-research.md`

7. **`sources/tutorials-courses/teachers-tech.md`**
   - Добавить `## Связи` после `## Синтез` (строка 49).
   - Ссылаться на:
     - `../../patterns/implementation/working-with-coding-agents.md`

8. **`sources/tutorials-courses/zinho-automates.md`**
   - Добавить `## Связи` после `## Синтез` (строка 53).
   - Ссылаться на:
     - `../../patterns/implementation/working-with-coding-agents.md`
     - `../../patterns/implementation/agent-skills-and-rules.md`

9. **`sources/libraries-tools/langchain-deep-agents.md`**
   - Добавить `## Связи` после `## Статус` (строка 35).
   - Ссылаться на:
     - `../../patterns/architecture-design/agent-harness.md`
     - `../../patterns/implementation/multi-agent-orchestration.md`
     - `../../tools/agent-frameworks-research.md`

10. **`sources/libraries-tools/superpowers.md`**
    - Добавить `## Связи` после `## Статус` (строка 38).
    - Ссылаться на:
      - `../../patterns/architecture-design/agent-harness.md`
      - `../../patterns/implementation/agent-skills-and-rules.md`
      - `../../patterns/implementation/working-with-coding-agents.md`
      - `openmontage.md` — похожая архитектура (skills + tools)

11. **`sources/libraries-tools/ecc.md`**
    - Добавить `## Связи` после `## Статус` (строка 37).
    - Ссылаться на:
      - `../../patterns/architecture-design/agent-harness.md`
      - `../../patterns/implementation/agent-skills-and-rules.md`
      - `../../patterns/implementation/working-with-coding-agents.md`
      - `../../patterns/implementation/multi-agent-orchestration.md`

12. **`sources/research-production/andrej-karpathy-skills.md`**
    - Добавить `## Связи` после `## Синтез` (строка 31).
    - Ссылаться на:
      - `../../patterns/implementation/agent-skills-and-rules.md`
      - `../../patterns/implementation/working-with-coding-agents.md`

---

### A3. P1 — Patterns без cross-reference секции

13. **`patterns/advanced/agent-use-cases.md`**
    - Добавить `## Связанные заметки` после последнего кейса (строка 135).
    - Ссылаться на:
      - `../architecture-design/agent-harness.md`
      - `../architecture-design/agent-security.md`
      - `../architecture-design/rag-for-agents.md`
      - `../implementation/agent-evaluations.md`
      - `../implementation/working-with-coding-agents.md`
      - `../production-operations/production-operations.md`
      - `reproducible-agent-recipes.md`
      - `../../tools/agent-frameworks-research.md`
      - `../../tools/agent-model-map.md`

---

### A4. P2 — Инструменты с неполными или отсутствующими секциями

14. **`tools/embeddings/OVERVIEW.md`** — Секция «Связанные темы» (строка 90) содержит текст без реальных ссылок:
    - `Векторные базы данных` → заменить на реальную ссылку, когда заметка появится, или оформить как будущую тему
    - `RAG и агенты` → сделать ссылкой на `../patterns/architecture-design/rag-for-agents.md`
    - `Evaluations` → сделать ссылкой на `../patterns/implementation/agent-evaluations.md`
    - `Реранкеры` → оформить как тему (заметки пока нет)
    - Добавить ссылку на `agent-model-map.md`
    - Добавить ссылку на `../patterns/fundamentals/context-engineering.md` — retrieval injection

15. **`tools/comparisons.md`** — Нет секции «Связанные заметки»:
    - Добавить `## Связанные заметки` после `## Как устроен раздел` (строка 14).
    - Ссылаться на:
      - `../patterns/advanced/agent-antipatterns.md`
      - `../patterns/production-operations/production-operations.md`

16. **`tools/OVERVIEW.md`** — Нет секции «Связанные заметки»:
    - Добавить `## Связанные разделы` после `## Как устроен раздел` (строка 18).
    - Ссылаться на:
      - `../patterns/OVERVIEW.md` — паттерны
      - `../sources/OVERVIEW.md` — источники

---

## B. Нарушения bidirectional (A ссылается на B, но B не ссылается на A)

### B1. Patterns → Tools (обратные ссылки отсутствуют)

| Файл A (ссылается на) | Файл B (нет обратной ссылки) | Что добавить в B |
|---|---|---|
| `tools/platforms/perplexity.md` → Agent Harness | `patterns/architecture-design/agent-harness.md` | Ссылку на `../../tools/platforms/perplexity.md` |
| `tools/platforms/perplexity.md` → Работа с код-агентами | `patterns/implementation/working-with-coding-agents.md` | Ссылку на `../../tools/platforms/perplexity.md` |
| `tools/platforms/perplexity.md` → Исследование фреймворков | `tools/agent-frameworks-research.md` | Уже есть в обратную? Проверить — нет. Добавить ссылку на `perplexity.md` |
| `tools/platforms/gemini.md` → Agent Harness | `patterns/architecture-design/agent-harness.md` | Ссылку на `../../tools/platforms/gemini.md` |
| `tools/platforms/gemini.md` → Работа с код-агентами | `patterns/implementation/working-with-coding-agents.md` | Ссылку на `../../tools/platforms/gemini.md` |
| `tools/platforms/gemini.md` → Исследование фреймворков | `tools/agent-frameworks-research.md` | Добавить ссылку на `gemini.md` |
| `tools/platforms/gemini.md` → Perplexity | `tools/platforms/perplexity.md` | Уже есть! ✓ |
| `tools/platforms/z-ai.md` → tools/OVERVIEW | `tools/OVERVIEW.md` | Уже есть! ✓ |
| `tools/models/mimo-code.md` → tools/OVERVIEW | `tools/OVERVIEW.md` | Уже есть! ✓ |
| `tools/agent-frameworks-research.md` → Multi-agent orchestration | `patterns/implementation/multi-agent-orchestration.md` | Уже есть! ✓ |
| `tools/agent-frameworks-research.md` → Production operations | `patterns/production-operations/production-operations.md` | Уже есть! ✓ |
| `tools/agent-model-map.md` → Evaluations | `patterns/implementation/agent-evaluations.md` | Ссылку на `../../tools/agent-model-map.md` |
| `tools/agent-model-map.md` → Исследование фреймворков | `tools/agent-frameworks-research.md` | Уже есть! ✓ |
| `tools/observability/OVERVIEW.md` → Evaluations | `patterns/implementation/agent-evaluations.md` | Уже есть! ✓ |
| `tools/observability/OVERVIEW.md` → Execution loop | `patterns/fundamentals/agent-execution-loop.md` | Ссылку на `../../tools/observability/OVERVIEW.md` |

### B2. Sources → Patterns (обратные ссылки отсутствуют)

| Файл A (ссылается на) | Файл B (нет обратной ссылки) | Что добавить в B |
|---|---|---|
| `sources/libraries-tools/openmontage.md` → Agent Harness | `patterns/architecture-design/agent-harness.md` | Ссылку на `../../sources/libraries-tools/openmontage.md` |
| `sources/libraries-tools/openmontage.md` → Работа с код-агентами | `patterns/implementation/working-with-coding-agents.md` | Ссылку на `../../sources/libraries-tools/openmontage.md` |
| `sources/libraries-tools/openmontage.md` → Skills и правила | `patterns/implementation/agent-skills-and-rules.md` | Ссылку на `../../sources/libraries-tools/openmontage.md` |
| `sources/libraries-tools/openmontage.md` → Исследование фреймворков | `tools/agent-frameworks-research.md` | Ссылку на `../sources/libraries-tools/openmontage.md` |
| `sources/libraries-tools/openmontage.md` → Superpowers | `sources/libraries-tools/superpowers.md` | Ссылку на `openmontage.md` (см. A2.10) |
| `sources/research-production/harness-engineering-openai.md` → (только текстовые упоминания, не ссылки) | `patterns/architecture-design/agent-harness.md` | Уже есть! ✓ |

### B3. Sources → Sources (между собой)

| Файл A → B | Файл B → A | Статус |
|---|---|---|
| `bitgn-arena-insights` → все 5 bitgn-файлов | Все bitgn-файлы → `bitgn-arena-insights` | ✓ (у всех есть) |
| `bitgn-codex-on-rails` → `bitgn-operation-pangolin` | `bitgn-operation-pangolin` → `bitgn-codex-on-rails` | ✗ НЕТ обратной ссылки! Добавить в `bitgn-operation-pangolin.md` |
| `bitgn-codex-on-rails` → `bitgn-codex-cli-rules-evolution` | `bitgn-codex-cli-rules-evolution` → `bitgn-codex-on-rails` | ✓ |
| `bitgn-filesystem-agent` → `bitgn-operation-pangolin` | `bitgn-operation-pangolin` → `bitgn-filesystem-agent` | ✗ НЕТ обратной ссылки! |
| `bitgn-filesystem-agent` → `bitgn-codex-on-rails` | `bitgn-codex-on-rails` → `bitgn-filesystem-agent` | ✗ НЕТ обратной ссылки! Добавить в `bitgn-codex-on-rails.md` |
| `bitgn-filesystem-agent` → `bitgn-codex-cli-rules-evolution` | `bitgn-codex-cli-rules-evolution` → `bitgn-filesystem-agent` | ✗ НЕТ обратной ссылки! Добавить в `bitgn-codex-cli-rules-evolution.md` |
| `bitgn-plan-repl-agent` → `bitgn-operation-pangolin` | `bitgn-operation-pangolin` → `bitgn-plan-repl-agent` | ✗ НЕТ обратной ссылки! |
| `bitgn-plan-repl-agent` → `bitgn-codex-on-rails` | `bitgn-codex-on-rails` → `bitgn-plan-repl-agent` | ✗ НЕТ обратной ссылки! Добавить в `bitgn-codex-on-rails.md` |
| `bitgn-plan-repl-agent` → `bitgn-codex-cli-rules-evolution` | `bitgn-codex-cli-rules-evolution` → `bitgn-plan-repl-agent` | ✗ НЕТ обратной ссылки! Добавить в `bitgn-codex-cli-rules-evolution.md` |

### B4. Patterns → Patterns (недостающие обратные ссылки)

| Файл A (ссылается) → Файл B | Файл B → A | Статус |
|---|---|---|
| `agent-taxonomy` → `agent-harness` | `agent-harness` → `agent-taxonomy` | ✗ Добавить (см. A1.1) |
| `agent-taxonomy` → `agent-execution-loop` | `agent-execution-loop` → `agent-taxonomy` | ✗ Добавить в `agent-execution-loop.md` |
| `agent-taxonomy` → `agent-antipatterns` | `agent-antipatterns` → `agent-taxonomy` | ✓ |
| `agent-execution-loop` → `agent-harness` | `agent-harness` → `agent-execution-loop` | ✗ Добавить (см. A1.1) |
| `agent-execution-loop` → `context-engineering` | `context-engineering` → `agent-execution-loop` | ✓ |
| `agent-execution-loop` → `production-operations` | `production-operations` → `agent-execution-loop` | ✗ Добавить в `production-operations.md` |
| `context-engineering` → `agent-execution-loop` | `agent-execution-loop` → `context-engineering` | ✓ |
| `context-engineering` → `rag-for-agents` | `rag-for-agents` → `context-engineering` | ✓ |
| `context-engineering` → `agent-security` | `agent-security` → `context-engineering` | ✗ Добавить в `agent-security.md` |
| `tool-use-and-mcp` → `agent-security` | `agent-security` → `tool-use-and-mcp` | ✓ |
| `tool-use-and-mcp` → `agent-harness` | `agent-harness` → `tool-use-and-mcp` | ✗ Добавить (см. A1.1) |
| `tool-use-and-mcp` → `production-operations` | `production-operations` → `tool-use-and-mcp` | ✗ Добавить в `production-operations.md` |
| `agent-security` → `tool-use-and-mcp` | `tool-use-and-mcp` → `agent-security` | ✓ |
| `agent-security` → `production-operations` | `production-operations` → `agent-security` | ✓ |
| `agent-security` → `data-governance-compliance` | `data-governance-compliance` → `agent-security` | ✓ |
| `rag-for-agents` → `context-engineering` | `context-engineering` → `rag-for-agents` | ✓ |
| `rag-for-agents` → `agent-evaluations` | `agent-evaluations` → `rag-for-agents` | ✓ |
| `rag-for-agents` → `data-governance-compliance` | `data-governance-compliance` → `rag-for-agents` | ✓ |
| `data-governance-compliance` → `agent-security` | `agent-security` → `data-governance-compliance` | ✓ |
| `data-governance-compliance` → `rag-for-agents` | `rag-for-agents` → `data-governance-compliance` | ✓ |
| `data-governance-compliance` → `production-operations` | `production-operations` → `data-governance-compliance` | ✗ Добавить в `production-operations.md` |
| `agent-evaluations` → `agent-observability-debugging` | `agent-observability-debugging` → `agent-evaluations` | ✓ |
| `agent-evaluations` → `production-operations` | `production-operations` → `agent-evaluations` | ✗ Добавить в `production-operations.md` |
| `agent-evaluations` → `rag-for-agents` | `rag-for-agents` → `agent-evaluations` | ✓ |
| `multi-agent-orchestration` → `agent-harness` | `agent-harness` → `multi-agent-orchestration` | ✗ Добавить (см. A1.1) |
| `multi-agent-orchestration` → `agent-execution-loop` | `agent-execution-loop` → `multi-agent-orchestration` | ✗ Добавить в `agent-execution-loop.md` |
| `multi-agent-orchestration` → `agent-frameworks-research` | `agent-frameworks-research` → `multi-agent-orchestration` | ✓ |
| `production-operations` → `agent-harness` | `agent-harness` → `production-operations` | ✗ Добавить (см. A1.1) |
| `production-operations` → `agent-observability-debugging` | `agent-observability-debugging` → `production-operations` | ✗ Добавить в `observability/OVERVIEW.md` |
| `production-operations` → `agent-security` | `agent-security` → `production-operations` | ✓ |
| `human-in-the-loop-ux` → `agent-security` | `agent-security` → `human-in-the-loop-ux` | ✗ Добавить в `agent-security.md` |
| `human-in-the-loop-ux` → `production-operations` | `production-operations` → `human-in-the-loop-ux` | ✗ Добавить в `production-operations.md` |
| `human-in-the-loop-ux` → `working-with-coding-agents` | `working-with-coding-agents` → `human-in-the-loop-ux` | ✗ Добавить (см. A1.3) |
| `agent-antipatterns` → `agent-taxonomy` | `agent-taxonomy` → `agent-antipatterns` | ✓ |
| `agent-antipatterns` → `multi-agent-orchestration` | `multi-agent-orchestration` → `agent-antipatterns` | ✗ Добавить в `multi-agent-orchestration.md` |
| `agent-antipatterns` → `agent-security` | `agent-security` → `agent-antipatterns` | ✗ Добавить в `agent-security.md` |
| `reproducible-agent-recipes` → `agent-harness` | `agent-harness` → `reproducible-agent-recipes` | ✗ Добавить (см. A1.1) |
| `reproducible-agent-recipes` → `agent-evaluations` | `agent-evaluations` → `reproducible-agent-recipes` | ✗ Добавить в `agent-evaluations.md` |
| `reproducible-agent-recipes` → `production-operations` | `production-operations` → `reproducible-agent-recipes` | ✗ Добавить в `production-operations.md` |

### B5. Patterns/OVERVIEW → заметки ссылаются, но заметки → Patterns/OVERVIEW — не всегда

| Заметка | Ссылается на `patterns/OVERVIEW.md`? | Статус |
|---|---|---|
| Все patterns/*.md | Нет | ✗ Ни одна pattern-заметка не ссылается на `../OVERVIEW.md`. Опционально — добавить в каждую для навигации. |

---

## C. Отсутствующие темы (заметки, которые стоит создать)

1. **`patterns/fundamentals/security-foundations.md`** или расширить `agent-security.md`
   - Сейчас `agent-security.md` в Architecture & Design, но fundamentals касается security лишь косвенно.
   - Вариант: перенести базовые концепции безопасности в fundamentals, оставив в architecture-design продвинутые.

2. **`tools/embeddings/rerankers.md`** — заметка о реранкерах (Cohere Rerank, BGE-reranker, Jina Reranker).
   - Упоминается в `embeddings/OVERVIEW.md` как «Реранкеры» без ссылки.
   - Связана с RAG, retrieval pipeline.

3. **`patterns/architecture-design/mcp-deep-dive.md`** или расширить `tool-use-and-mcp.md`
   - MCP активно используется в bitgn-решениях (Codex-on-Rails), Gemini CLI, но отдельной архитектурной заметки нет.
   - Сейчас MCP описан в fundamentals как часть tool-use.

4. **`patterns/implementation/agent-memory-patterns.md`**
   - Memory упоминается везде (agent-harness, context-engineering, data-governance), но нет отдельной заметки.
   - Тема: persistent memory, types (episodic/semantic/procedural), TTL, consent, cleanup.

5. **`tools/platforms/anthropic.md`** / **`tools/platforms/openai.md`**
   - Сейчас есть только `z-ai.md` в platforms/. Нет отдельных заметок по Anthropic и OpenAI как платформам.
   - `gemini.md` и `perplexity.md` уже есть в tools/ (не в platforms/).

---

## D. Битые ссылки и проблемы форматирования

1. **`tools/embeddings/OVERVIEW.md`** строка 92–96 — «Связанные темы» содержит текст без ссылок:
   - `Векторные базы данных` — не ссылка
   - `RAG и агенты` — не ссылка
   - `Evaluations` — не ссылка
   - `Реранкеры` — не ссылка
   → Превратить в Markdown-ссылки (где есть целевые файлы) или явно пометить как будущие темы.

2. **`sources/engineering-patterns/bitgn-arena-insights.md`** строка 52–57 — «Связи с другими заметками» содержит текст без реальных ссылок:
   - `Harness Engineering` — не ссылка
   - `Plan-and-Execute` — не ссылка
   - `Guardrails` — не ссылка
   - `Agent-to-agent review` — не ссылка
   - `MCP-протокол` — не ссылка
   - `Codex CLI` — не ссылка
   → Превратить в ссылки на соответствующие patterns/sources.

3. **`sources/engineering-patterns/bitgn-codex-cli-rules-evolution.md`** строка 94–99 — «Связи» содержит текст без ссылок:
   - `Codex CLI` — не ссылка
   - `Agent-to-agent-review` — не ссылка
   - `Harness Engineering` — не ссылка
   - `Evaluations` — не ссылка
   - `Plan-and-Execute` — не ссылка
   → Превратить в ссылки.

4. **`sources/engineering-patterns/bitgn-codex-on-rails.md`** строка 190–195 — «Связи с другими заметками» содержит текст без ссылок:
   - `MCP-протокол` — не ссылка
   - `Guardrails` — не ссылка
   - `BitGN-Operation-Pangolin` — не ссылка
   - `Harness Engineering` — не ссылка
   - `Error-Recovery` — не ссылка
   - `Tool-Use-паттерны` — не ссылка
   → Превратить в ссылки.

5. **`sources/research-production/harness-engineering-openai.md`** строка 91–96 — «Связи с другими разделами» содержит текст без ссылок:
   - `Codex vs Hermes vs другие платформы` — не ссылка
   - `Plan-and-Execute паттерн` — не ссылка
   - `CI/CD с агентами` — не ссылка
   - `Как структурировать AGENTS.md` — не ссылка
   - `Agent-to-agent ревью` — не ссылка
   → Превратить в ссылки.

6. **`sources/engineering-patterns/bitgn-filesystem-agent.md`** строка 16 и 83 — смешанные реальные и текстовые ссылки:
   - Строка 16: `Plan-and-Execute`, `Human-in-the-Loop` — не ссылки
   - Строка 83: `Trust Boundaries` ссылается на bitgn-arena-insights ✓, но `Durable Memory через ФС` упоминает Pangolin → добавить ссылку.

7. **`sources/engineering-patterns/bitgn-operation-pangolin.md`** строка 16 и 86–89:
   - Строка 16: `Plan-and-Execute`, `Guardrails` — не ссылки
   - Строка 86: `Plan-and-Execute` — не ссылка
   - Строка 87: `Guardrails` — не ссылка
   - Строка 88: `Error Recovery` — не ссылка
   - Строка 89: `Агент с интерпретатором кода` — не ссылка

8. **`sources/engineering-patterns/bitgn-plan-repl-agent.md`** строка 136–142:
   - `Plan-and-Execute` — не ссылка
   - `OpenRouter` — не ссылка
   - `Guardrails` — не ссылка
   - `Evaluations` — не ссылка

---

## E. Сводка по приоритетам

### P0 — критичные (ключевые заметки без cross-reference):
- agent-harness.md — добавить «Связанные заметки» (16+ ссылок)
- agent-skills-and-rules.md — добавить «Связанные заметки» (9+ ссылок)
- working-with-coding-agents.md — добавить «Связанные заметки» (13+ ссылок)

### P1 — важные (отсутствуют секции):
- 9 sources без секции «Связи»
- agent-use-cases.md без «Связанные заметки»
- Недостающие bidirectional ссылки между bitgn-файлами и между patterns

### P2 — желательные (форматирование):
- embeddings/OVERVIEW.md — реальные ссылки вместо текста
- Несколько sources с текстовыми описаниями вместо ссылок
- comparisons.md и tools/OVERVIEW.md — добавить cross-reference

### P3 — новые заметки (расширение базы):
- rerankers.md, agent-memory-patterns.md, mcp-deep-dive.md, платформенные заметки

---

*Аудит завершён 2026-06-29. После внесения правок запустить `python3 meta/scripts/validate-vault.sh`.*
