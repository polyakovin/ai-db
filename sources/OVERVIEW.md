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
- [OpenClaw ≠ магия — hands-on гайд на Habr](tutorials-courses/openclaw-habr-guide.md) — self-hosting, реальные use cases, эксплуатационные ограничения и безопасность

## 🔵 Libraries & Tools

*Инструментарий для сборки агентов: библиотеки, фреймворки, SDK.*

- [DeerFlow Documentation and Repository](libraries-tools/deerflow-docs.md) — open-source long-horizon agent harness, SDK/App, skills, sandbox, memory и subagents
- [LightRAG](libraries-tools/lightrag.md) — simple and fast RAG с графами знаний, multimodal support
- [Koog Documentation](libraries-tools/koog-docs.md) — Kotlin/Java agent framework, graph strategies, persistence и integrations
- [Pydantic AI Documentation](libraries-tools/pydantic-ai-docs.md) — typed Python agents, structured output, tools, evals и harness
- [LangGraph Documentation](libraries-tools/langgraph-docs.md) — stateful orchestration, durable execution, persistence и HITL
- [Langflow Documentation](libraries-tools/langflow-docs.md) — visual flows, agents, custom components, API и MCP
- [LightRAG Alternatives Research](libraries-tools/lightrag-alternatives.md) — provenance для обзора GraphRAG/RAG-аналогов
- [LangChain Deep Agents](libraries-tools/langchain-deep-agents.md) — harness, filesystem, subagents, context management, sandbox boundary
- [Superpowers](libraries-tools/superpowers.md) — skills workflow, TDD, systematic debugging, review loops
- [Ponytail](libraries-tools/ponytail.md) — YAGNI/reuse-first ruleset и skills для coding agents
- [ECC](libraries-tools/ecc.md) — harness OS, memory persistence, hooks, verification loops, security
- [Claude Science](libraries-tools/claude-science.md) — AI workbench для научных агентов, provenance, reviewer loop, compute orchestration
- [OpenScience](libraries-tools/openscience.md) — open-source AI workbench для scientific agents, local workspace, skills, MCP и scientific connectors
- [Perplexity AI](libraries-tools/perplexity.md) — AI-поиск с агентными возможностями
- [Model Context Protocol Docs](libraries-tools/model-context-protocol-docs.md) — стандарт подключения AI-приложений к внешним системам
- [Agent2Agent (A2A) Protocol](libraries-tools/a2a-protocol.md) — протокол коммуникации и interoperability между агентами
- [Agent Communication Protocol (ACP)](libraries-tools/agent-communication-protocol.md) — IBM/BeeAI REST-first протокол, merged into A2A
- [AionUi](libraries-tools/aionui.md) — desktop UI для multi-agent coworking и remote operator control
- [OpenAI Tools Docs](libraries-tools/openai-tools-docs.md) — hosted tools: web search, file search, MCP/connectors
- [LlamaIndex Data Connectors and Ingestion Pipeline](libraries-tools/llamaindex-data-connectors.md) — connectors, ingestion transformations, cache, vector-store insertion
- [LangChain Document Loaders](libraries-tools/langchain-document-loaders.md) — единый loader-интерфейс для внешних источников
- [Firecrawl Crawl Docs](libraries-tools/firecrawl-crawl-docs.md) — recursive crawl, sitemap discovery, clean markdown, webhooks
- [Airbyte Connectors Docs](libraries-tools/airbyte-connectors-docs.md) — source/destination connectors для data replication
- [Unstructured Docs](libraries-tools/unstructured-docs.md) — parsing, chunking и ingestion неструктурированных документов
- [Multica](libraries-tools/multica.md) — project management layer для human + agent teams, task lifecycle, runtimes, skills
- [Runable](libraries-tools/runable.md) — artifact-first AI-платформа с sandbox, skills, memory, plan approval и мультимодальными результатами
- [Agent Skills specification and authoring guidance](libraries-tools/agent-skills-specification.md) — progressive disclosure, структура skills и deferred tool discovery
- [Arena AI](libraries-tools/arena-ai.md) — human-preference leaderboard, Battle Mode, rank spread и privacy boundary
- [Qwen Studio](libraries-tools/qwen-studio.md) — официальный consumer-интерфейс моделей Qwen
- [NotebookLM](libraries-tools/notebooklm.md) — source-grounded research, citations и Studio-артефакты
- [Google Gemini App](libraries-tools/google-gemini-app.md) — официальный web/mobile интерфейс Gemini
- [MarkItDown](libraries-tools/markitdown.md) — конвертация документов в Markdown для LLM pipelines
- [Hermes Agent — русскоязычный обзор](libraries-tools/hermes-agent-ru.md) — установка, memory, skills, tools и delegation
- [LFM2.5-8B-A1B and LocalCowork](libraries-tools/localcowork-lfm2-5.md) — локальный desktop-агент, компактная MoE-модель и масштабирование MCP tool surface

## 🟡 Engineering Patterns

*Практические эксперименты и архитектурные решения: BitGN, Codex, Plan-REPL.*

- [BitGN Arena — Insights](engineering-patterns/bitgn-arena-insights.md) — архитектурные инсайты
- [BitGN Codex CLI — Rules Evolution](engineering-patterns/bitgn-codex-cli-rules-evolution.md)
- [BitGN Codex on Rails](engineering-patterns/bitgn-codex-on-rails.md)
- [BitGN Filesystem Agent](engineering-patterns/bitgn-filesystem-agent.md)
- [BitGN Operation Pangolin](engineering-patterns/bitgn-operation-pangolin.md)
- [BitGN Plan-REPL Agent](engineering-patterns/bitgn-plan-repl-agent.md)
- [Know Your Unknowns — Thariq](engineering-patterns/thariq-html-unknowns.md) — 11 HTML-артефактов для обнаружения неопределённостей до/во время/после имплементации

## 🟠 Research & Production

*Исследования, production-практики, хардкорные доклады.*

- [Demystifying evals for AI agents — Anthropic](research-production/demystifying-evals-for-ai-agents.md) — outcome-first grading, capability/regression suites, повторные trials и lifecycle eval-набора
- [Harness Engineering — OpenAI](research-production/harness-engineering-openai.md) — Open AI/Anthropic подходы к обвязке агентов
- [Andrej Karpathy Skills](research-production/andrej-karpathy-skills.md) — think before coding, simplicity, surgical changes, goal-driven execution
- [Sber AI-Disrupt PDLC](research-production/sber-ai-disrupt-pdlc.md) — enterprise-агенты: двухпетлевая модель, Intent Loop, IDP, Skills, MCP/A2A, 98/2 обвязка
- [Large Language Models Do Not Always Need Readable Language (BabelTele)](research-production/large-language-models-do-not-always.md) — модельно-ориентированное сжатие контекста между LLM/агентами
- [Semantic Compression With Large Language Models](research-production/semantic-compression-with-llms.md) — исследование о компрессии и восстановлении смысла как раннем фундаменте для model-native форматов

---

## Сводная таблица

| Источник | Категория | Куда перенесено |
|----------|-----------|-----------------|
| [DeerFlow Documentation and Repository](libraries-tools/deerflow-docs.md) | 🔵 Libraries | [DeerFlow](../tools/frameworks/deerflow.md), [Исследование фреймворков](../tools/agent-frameworks-research.md), [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| [Koog Documentation](libraries-tools/koog-docs.md) | 🔵 Libraries | [Koog](../tools/frameworks/koog.md), [Исследование фреймворков](../tools/agent-frameworks-research.md) |
| [Pydantic AI Documentation](libraries-tools/pydantic-ai-docs.md) | 🔵 Libraries | [Pydantic AI](../tools/frameworks/pydantic-ai.md), [Исследование фреймворков](../tools/agent-frameworks-research.md) |
| [LangGraph Documentation](libraries-tools/langgraph-docs.md) | 🔵 Libraries | [LangGraph](../tools/frameworks/langgraph.md), [Исследование фреймворков](../tools/agent-frameworks-research.md) |
| [Langflow Documentation](libraries-tools/langflow-docs.md) | 🔵 Libraries | [Langflow](../tools/frameworks/langflow.md), [Исследование фреймворков](../tools/agent-frameworks-research.md) |
| [OpenAI Academy](tutorials-courses/openai-academy.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [AI Foundations](tutorials-courses/ai-foundations.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md) |
| [Zinho Automates](tutorials-courses/zinho-automates.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md) |
| [Teacher's Tech](tutorials-courses/teachers-tech.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [LangChain Deep Agents](libraries-tools/langchain-deep-agents.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| [Claude Code 101](tutorials-courses/claude-code-101.md) | 🟢 Tutorials | [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Superpowers](libraries-tools/superpowers.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Ponytail](libraries-tools/ponytail.md) | 🔵 Libraries | [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md), [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| [ECC](libraries-tools/ecc.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [OpenMontage](libraries-tools/openmontage.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Claude Science](libraries-tools/claude-science.md) | 🔵 Libraries | [Anthropic (Claude)](../tools/platforms/anthropic.md) — canonical, [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| [OpenScience](libraries-tools/openscience.md) | 🔵 Libraries | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Tool use и MCP](../patterns/fundamentals/tool-use-and-mcp.md), [Воспроизводимые рецепты AI-агентов](../patterns/advanced/reproducible-agent-recipes.md) |
| [Perplexity AI](libraries-tools/perplexity.md) | 🔵 Libraries | [Perplexity (tools)](../tools/platforms/perplexity.md) — canonical |
| [Model Context Protocol Docs](libraries-tools/model-context-protocol-docs.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [Tool use и MCP](../patterns/fundamentals/tool-use-and-mcp.md) |
| [Agent2Agent (A2A) Protocol](libraries-tools/a2a-protocol.md) | 🔵 Libraries | [Робастная multi-agent среда](../patterns/architecture-design/robust-multi-agent-environment.md), [Multi-agent orchestration](../patterns/implementation/multi-agent-orchestration.md), [Tool use и MCP](../patterns/fundamentals/tool-use-and-mcp.md) |
| [Agent Communication Protocol (ACP)](libraries-tools/agent-communication-protocol.md) | 🔵 Libraries | [Agent2Agent (A2A) Protocol](libraries-tools/a2a-protocol.md), [Робастная multi-agent среда](../patterns/architecture-design/robust-multi-agent-environment.md), [Multi-agent orchestration](../patterns/implementation/multi-agent-orchestration.md) |
| [AionUi](libraries-tools/aionui.md) | 🔵 Libraries | [Робастная multi-agent среда](../patterns/architecture-design/robust-multi-agent-environment.md), [Agent Harness](../patterns/architecture-design/agent-harness.md) |
| [OpenAI Tools Docs](libraries-tools/openai-tools-docs.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [OpenAI](../tools/platforms/openai.md) |
| [LlamaIndex Data Connectors and Ingestion Pipeline](libraries-tools/llamaindex-data-connectors.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [LlamaIndex](../tools/frameworks/llamaindex.md) |
| [LangChain Document Loaders](libraries-tools/langchain-document-loaders.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [LangChain](../tools/frameworks/langchain.md) |
| [Firecrawl Crawl Docs](libraries-tools/firecrawl-crawl-docs.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [Web Search](../tools/agent-tools/web-search.md) |
| [Airbyte Connectors Docs](libraries-tools/airbyte-connectors-docs.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [Data governance и compliance](../patterns/architecture-design/data-governance-compliance.md) |
| [Unstructured Docs](libraries-tools/unstructured-docs.md) | 🔵 Libraries | [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md), [RAG для агентов](../patterns/architecture-design/rag-for-agents.md) |
| [LightRAG Alternatives Research](libraries-tools/lightrag-alternatives.md) | 🔵 Libraries | [LightRAG](../tools/retrieval/lightrag.md), [Retrieval tools overview](../tools/retrieval/OVERVIEW.md) |
| [Multica](libraries-tools/multica.md) | 🔵 Libraries | [Робастная multi-agent среда](../patterns/architecture-design/robust-multi-agent-environment.md), [Agent Harness](../patterns/architecture-design/agent-harness.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Runable](libraries-tools/runable.md) | 🔵 Libraries | [Runable (tools)](../tools/platforms/runable.md) — canonical, [Agent Harness](../patterns/architecture-design/agent-harness.md), [Human-in-the-loop UX](../patterns/production-operations/human-in-the-loop-ux.md) |
| [Agent Skills specification and authoring guidance](libraries-tools/agent-skills-specification.md) | 🔵 Libraries | [Progressive disclosure для AI-агентов](../patterns/implementation/progressive-disclosure-for-agents.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md) |
| [Demystifying evals for AI agents — Anthropic](research-production/demystifying-evals-for-ai-agents.md) | 🟠 Research | [Evaluations для AI-агентов](../patterns/implementation/agent-evaluations.md) |
| [Andrej Karpathy Skills](research-production/andrej-karpathy-skills.md) | 🟠 Research | [Skills и правила](../patterns/implementation/agent-skills-and-rules.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Sber AI-Disrupt PDLC](research-production/sber-ai-disrupt-pdlc.md) | 🟠 Research | [Agent Harness](../patterns/architecture-design/agent-harness.md), [Skills и правила](../patterns/implementation/agent-skills-and-rules.md) |
| [Large Language Models Do Not Always Need Readable Language (BabelTele)](research-production/large-language-models-do-not-always.md) | 🟠 Research | [Оценка ответов LLM](../patterns/implementation/llm-response-evaluation.md), [Работа с код-агентами](../patterns/implementation/working-with-coding-agents.md) |
| [Semantic Compression With Large Language Models](research-production/semantic-compression-with-llms.md) | 🟠 Research | [Агентная компрессия контекста](../patterns/advanced/agent-context-distillation.md), [Оценка ответов LLM](../patterns/implementation/llm-response-evaluation.md) |
| [Arena AI](libraries-tools/arena-ai.md) | 🔵 Libraries | [Arena AI (tools)](../tools/platforms/arena-ai.md), [Оценка ответов LLM](../patterns/implementation/llm-response-evaluation.md) |
| [Qwen Studio](libraries-tools/qwen-studio.md) | 🔵 Libraries | [Qwen (Alibaba)](../tools/platforms/qwen.md) — canonical |
| [OpenClaw ≠ магия — hands-on гайд на Habr](tutorials-courses/openclaw-habr-guide.md) | 🟢 Tutorials | [OpenClaw](../tools/platforms/openclaw.md), [Human-in-the-loop UX](../patterns/production-operations/human-in-the-loop-ux.md), [Безопасность агентных систем](../patterns/architecture-design/agent-security.md) |
| [NotebookLM](libraries-tools/notebooklm.md) | 🔵 Libraries | [NotebookLM (tools)](../tools/platforms/notebooklm.md), [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md) |
| [Google Gemini App](libraries-tools/google-gemini-app.md) | 🔵 Libraries | [Google Gemini](../tools/platforms/gemini.md) — canonical |
| [MarkItDown](libraries-tools/markitdown.md) | 🔵 Libraries | [MarkItDown (tools)](../tools/agent-tools/markitdown.md), [Автоматизация сбора внешнего контекста](../patterns/architecture-design/external-context-collection.md) |
| [Hermes Agent — русскоязычный обзор](libraries-tools/hermes-agent-ru.md) | 🔵 Libraries | [Hermes Agent (tools)](../tools/platforms/hermes-agent.md), [Робастная multi-agent среда](../patterns/architecture-design/robust-multi-agent-environment.md) |
| [LFM2.5-8B-A1B and LocalCowork](libraries-tools/localcowork-lfm2-5.md) | 🔵 Libraries | [LocalCowork](../tools/platforms/localcowork.md), [LFM2.5-8B-A1B](../tools/models/lfm2-5-8b-a1b.md), [Tool use и MCP](../patterns/fundamentals/tool-use-and-mcp.md) |

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

*Последнее обновление: 26.07.2026*
