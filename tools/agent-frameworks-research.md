# Исследование фреймворков для AI-агентов

Актуально на 2026-06-24. Эта заметка помогает выбрать стек для агентной системы. Она опирается на официальные страницы проектов, но рекомендации являются синтезом для этого vault.

## Карта выбора

| Стек | Сильная сторона | Когда брать | Осторожно |
|---|---|---|---|
| OpenAI Responses API + Agents SDK | hosted tools, tracing, guardrails, handoffs, evals | OpenAI-first production, tool-heavy workflows | завязка на provider surface |
| Anthropic Claude Code | coding-agent workflow в терминале/IDE | разработка, refactor, code review, repo tasks | не универсальный app framework |
| LangGraph | long-running stateful agents, persistence, HITL | сложные workflow и control over state | требует проектировать graph/state |
| AutoGen | conversational и event-driven multi-agent systems | research/prototyping multi-agent | сложность orchestration/debugging |
| Semantic Kernel | enterprise middleware, plugins, C#/Python/Java | Microsoft/.NET enterprise stack | меньше “готовой магии”, больше integration layer |
| CrewAI | crews, tasks, flows, guardrails, memory | быстрые role-based multi-agent automations | проверять evals, не плодить роли без нужды |
| LlamaIndex | RAG, knowledge agents, data connectors | knowledge-heavy agents | orchestration может потребовать внешнего runtime |
| Dify | low-code LLM apps/agents | быстрый prototype, internal tools | limits low-code abstraction |
| Flowise | visual builder for LLM flows | no/low-code experimentation | production governance нужно достраивать |
| LangFlow | visual graph builder | обучение, быстрые flow prototypes | сложные production agents требуют инженерного слоя |

## Разделение по слою

| Слой | Инструменты |
|---|---|
| Model/API runtime | OpenAI Responses API, Anthropic API, Gemini API, Mistral |
| Agent SDK | OpenAI Agents SDK, Semantic Kernel, LlamaIndex agents |
| Orchestration | LangGraph, AutoGen Core, CrewAI Flows |
| Knowledge/RAG | LlamaIndex, LangChain retrievers, vector DBs |
| Low-code builders | Dify, Flowise, LangFlow |
| Observability/evals | LangSmith, Phoenix, OpenAI Evals/Traces |

## OpenAI

OpenAI стоит брать, если нужен managed stack с Responses API, tools, structured outputs, tracing, evals и Agents SDK. Хорош для production-команд, которым важны provider-hosted capabilities и единая экосистема.

Primary sources:

- [OpenAI building agents track](https://developers.openai.com/tracks/building-agents)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI Responses API migration guide](https://developers.openai.com/api/docs/guides/migrate-to-responses)

## Anthropic Claude Code

Claude Code — не общий framework для embedding в backend, а готовый coding-agent surface: terminal/IDE workflow, работа с repo, commands, approvals и developer loop. Его стоит изучать как reference implementation для coding agents и human-in-the-loop инженерного UX.

Primary source:

- [Claude Code overview](https://code.claude.com/docs/en/overview)

## LangGraph

LangGraph — низкоуровневый orchestration runtime для long-running stateful agents. Официальные docs подчёркивают durable execution, streaming, human-in-the-loop, memory и production deployment. Хороший выбор, когда граф состояния важнее “быстрого агента за 10 строк”.

Primary source:

- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)

## AutoGen

AutoGen разделяет AgentChat, Core, Extensions и Studio. Полезен для conversational single/multi-agent applications, event-driven multi-agent systems, прототипирования и исследований multi-agent collaboration.

Primary source:

- [AutoGen documentation](https://microsoft.github.io/autogen/stable/)

## Semantic Kernel

Semantic Kernel — lightweight open-source development kit для AI agents и интеграции моделей в C#, Python, Java. Особенно уместен в enterprise/Microsoft среде, где нужны plugins, telemetry, filters и интеграция с существующими API.

Primary source:

- [Semantic Kernel overview](https://learn.microsoft.com/en-us/semantic-kernel/overview/)

## CrewAI

CrewAI фокусируется на collaborative agents, crews и flows. В docs заявлены guardrails, memory, knowledge, observability, human-in-the-loop triggers и deployment automations. Хорош для role-based automations, если роли действительно независимы.

Primary source:

- [CrewAI documentation](https://docs.crewai.com/)

## LlamaIndex

LlamaIndex особенно силён для knowledge-heavy агентов: RAG, indexing, agents over data, human-in-the-loop, multi-agent patterns, tracing/evaluation. Его стоит брать, когда главная сложность — данные, документы, retrieval и structured extraction.

Primary source:

- [LlamaIndex agents](https://developers.llamaindex.ai/python/framework/use_cases/agents/)

## Low-code: Dify, Flowise, LangFlow

Low-code платформы полезны для discovery, внутренних tools и быстрых demos. Их нельзя считать заменой production engineering: отдельно проверяйте permissions, versioning, evals, secrets, observability, rollback и exportability.

Primary sources:

- [Dify docs](https://docs.dify.ai/)
- [Flowise docs](https://docs.flowiseai.com/)
- [LangFlow docs](https://docs.langflow.org/)

## Рекомендации по выбору

- Нужен production OpenAI-first агент: OpenAI Responses API + Agents SDK.
- Нужен stateful graph с human interrupts: LangGraph.
- Нужен knowledge/RAG agent: LlamaIndex или LangGraph + RAG слой.
- Нужна .NET/enterprise интеграция: Semantic Kernel.
- Нужны role-based multi-agent prototypes: CrewAI или AutoGen.
- Нужно быстро показать идею non-engineering команде: Dify/Flowise/LangFlow.
- Нужен coding workflow по repo: Claude Code или Codex-like agent.

## Связанные заметки

- [Модельная карта для агентов](agent-model-map.md)
- [Multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [Production operations](../patterns/production-operations.md)
