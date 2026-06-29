# Tools — overview

Раздел охватывает фреймворки, библиотеки, SDK, платформы и утилиты для создания, отладки и развёртывания AI-агентов. Цель — дать практический обзор доступного инструментария и помочь с выбором под конкретную задачу.

## Платформы и провайдеры

- [Anthropic (Claude)](platforms/anthropic.md) — Claude API, Claude Code, Claude Cowork, Computer Use, Opus/Sonnet/Haiku
- [OpenAI](platforms/openai.md) — GPT-5.5, Responses API, Agents SDK, Codex CLI, Realtime API
- [Google Gemini](platforms/gemini.md) — семейство мультимодальных LLM, платформа с Computer Use, Gemini CLI, API
- [Mistral AI](platforms/mistral.md) — европейский провайдер: Large 3, Medium 3.5, Small 4, Codestral, Le Chat
- [DeepSeek](platforms/deepseek.md) — open-weight модели V4 Pro/Flash, сверхнизкие цены API
- [Qwen (Alibaba)](platforms/qwen.md) — Qwen3.7-Max/Plus, Qwen3.6-35B-A3B, open-weight → API-only переход
- [Z.ai (GLM)](platforms/z-ai.md) — GLM-5.2, open-weight MIT, Anthropic-совместимый API, AutoGLM

## Модели

- [MiMo Code](models/mimo-code.md) — кодовый AI-ассистент и семейство моделей от Xiaomi

## Фреймворки

- [LangGraph](frameworks/langgraph.md) — stateful orchestration runtime для long-running агентов
- [AutoGen / MAF](frameworks/autogen.md) — event-driven multi-agent фреймворк (Microsoft Agent Framework)
- [CrewAI](frameworks/crewai.md) — роль-ориентированная multi-agent автоматизация
- [Semantic Kernel](frameworks/semantic-kernel.md) — enterprise middleware для AI-агентов (.NET/Python/Java)
- [LlamaIndex](frameworks/llamaindex.md) — фреймворк для knowledge-heavy агентов и RAG
- [Dify](frameworks/dify.md) — low-code платформа для построения agentic workflows

## Поиск и retrieval

- [Perplexity AI](platforms/perplexity.md) — AI-поисковая платформа с агентными возможностями (Computer, Spaces, Workflows)
- [Pinecone](vector-dbs/pinecone.md) — serverless векторная база данных для RAG
- [Ререйкеры](embeddings/rerankers.md) — Cohere Rerank, BGE, Jina — второй этап ранжирования для RAG

## Другие инструменты

- [Модели для эмбеддингов](embeddings/OVERVIEW.md) — выбор embedding-модели для RAG, памяти и семантического поиска
- [Observability и debugging](observability/OVERVIEW.md) — traces, spans, logs, metrics, run replay и failure taxonomy

## Исследования и сравнения

- [Исследование фреймворков для AI-агентов](agent-frameworks-research.md) — OpenAI, Anthropic, LangGraph, AutoGen, Semantic Kernel, CrewAI, LlamaIndex и low-code
- [Модельная карта для AI-агентов](agent-model-map.md) — reasoning, tool calling, long context, multimodal, code, cost/latency
- [Сравнение платформ](comparisons.md) — сравнительный анализ фреймворков, моделей и платформ

## Как устроен раздел

Каждая заметка — это обзор конкретного инструмента или категории инструментов, с примерами кода, таблицами сравнения и рекомендациями по выбору. Перекрёстные ссылки ведут к паттернам и практическим кейсам.

### Single Source of Truth

Каждый инструмент/платформа имеет **единственную canonical страницу** в `tools/` (или подпапках). Все остальные заметки (patterns, sources) **только ссылаются** на эти страницы — никогда не дублируют факты.

---

*Последнее обновление: 29.06.2026*
