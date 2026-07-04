# Backlog — Новые темы для документирования

Найденные пробелы и тренды по результатам ночного аудита.
*Обновлено: 02.07.2026*

## 🔴 High Priority

### 1. MCP 2026-07-28 RC — Breaking Changes
- **Stateless protocol core** — убран `initialize`/`initialized` handshake и `Mcp-Session-Id`. Протокольная версия, client info и capabilities передаются в `_meta` на каждом запросе.
- **Extensions стали first-class** — формальный процесс (SEP-2133): reverse-DNS IDs, делегированные мейнтенеры, версионируются независимо от spec.
- **MCP Apps** (SEP-1865) — server-rendered HTML UIs в sandboxed iframe.
- **Tasks** — graduated из experimental в extension (SEP-2663), stateless lifecycle.
- **JSON Schema 2020-12** для `inputSchema`/`outputSchema` — full поддержка с `oneOf`, `anyOf`, `$ref`, `$defs`.
- **Authorization hardening** — 6 SEPs: mix-up attack mitigation, OIDC `application_type`, refresh tokens, scope accumulation.
- **Deprecated:** Roots, Sampling, Logging (annotation-only, 12+ months notice).
- **Governance:** Feature Lifecycle Policy (SEP-2577) — Active → Deprecated → Removed.
- Источник: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate

### 2. A2A Protocol — v1.0 Stable, Enterprise Production
- **150+ организаций**, интеграция в Google Cloud, Microsoft Copilot Studio, Azure AI Foundry, Amazon Bedrock AgentCore.
- **A2A v1.0** — стабильный релиз (апрель 2026), signed Agent Cards, Agent Payments Protocol (AP2).
- **A2A + MCP взаимодополняемость** — MCP для tool access, A2A для agent coordination.
- Источник: https://rapidclaw.dev/blog/a2a-protocol-complete-guide-2026

### 3. Agent Protocol Ecosystem Map 2026
- **Четыре протокола, один стек:** MCP (97M downloads) → A2A (50+ partners) → ACP (IBM/Linux Foundation) → UCP (Google).
- **Enterprise agent stack 2026 использует все四个** — MCP для инструментов, A2A для координации, ACP/UCP для commerce.
- Источник: https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp

## 🟡 Medium Priority

### 4. Agent Evaluation 2026 — Production Reality
- **Провал статических бенчмарков:** UC Berkeley — 8 ведущих бенчмарков (SWE-bench, WebArena, OSWorld, GAIA) не отражают production-реальность.
- **Три уровня оценки:** end-to-end (task completion rate), trajectory-level (tool calls, reasoning), component-level.
- **Ключевые метрики:** task completion rate, human override rate, step efficiency, tool correctness.
- **Новые инструменты:** LangSmith, Braintrust, DeepEval, Phoenix, τ2-Bench, GDPval, Agent-SafetyBench.
- **METR approach:** "как долго задача должна быть, чтобы агент успевал в 50% случаев"
- Источник: https://www.morphllm.com/ai-agent-evaluation

### 5. Production Failures — 88% не доходят до production
- **7 паттернов провала:** scoping, data infra, security architecture, integration approach, cost modeling, governance, org dynamics.
- **Agent reliability cliff** — деградация при масштабировании multi-agent.
- **Реальные инциденты:** 195M записей через Claude Code (Mexico gov breach), zero-click prompt injection в M365 Copilot (CVE 9.3).
- Источник: https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework

### 6. Google ADK (Agent Development Kit)
- Open-source (Apache 2.0), model-agnostic, multi-language (Python, TypeScript, Go, Java).
- Hierarchical multi-agent, A2A-native, OpenTelemetry, встроенные evaluation tools.
- Прямой конкурент LangGraph, OpenAI Agents SDK, Claude Agent SDK.
- Источник: https://www.infoworld.com/article/4153857/hands-on-with-the-google-agent-development-kit.html

### 7. Anthropic Agentic Coding Trends 2026
- **8 трендов:** от single AI assistants к coordinated agent teams, autonomous runs часами/днями.
- **Rakuten case study:** Claude Code — 12.5M LOC codebase, 7 часов автономно, 99.9% accuracy.
- **60% работы с AI, но только 0–20% полного делегирования.**
- **Engineers → orchestrators** вместо writers.
- Источник: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf

### 8. MCP Security — NSA Guidelines
- **NSA AISC Cybersecurity Information Sheet** (May 2026) — Security Design Considerations for MCP.
- **Confused deputy** — главная архитектурная уязвимость MCP.
- **MCP Gateways** — централизованная аутентификация, tool-level permissions, audit trails.
- Источник: https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/

## 🟢 Lower Priority

### 9. Hermes Agent v0.14–v0.17 (2026)
- v0.14 (The Surface Release): desktop app, browser admin panel, remote gateway.
- v0.17 (The Reach Release): multi-agent Kanban, persistent /goal, Checkpoints v2, i18n locales.
- Skills system maturity, MCP integration, 60+ tools, 22 messaging platforms.
- NVIDIA RTX / DGX Spark support.
- 57K+ GitHub stars, growing faster than OpenClaw at same stage.
- Источник: https://hermesatlas.com/reports/state-of-hermes-april-2026

### 10. Agentic Payments — AP2 & X42
- **AP2** (Google + Coinbase, Sep 2025): signed Intent → Cart → Payment Mandates.
- **X42** (stripe MPP) — competing protocol.
- A2A x402 extension for crypto payments.
- **Adyen Agentic** (June 2026) — merchant integration layer.
- Источник: https://eco.com/support/en/articles/15192002-ap2-protocol-explained

### 11. AI Agent Frameworks Landscape 2026
- **7+ фреймворков:** LangChain, CrewAI, Microsoft Agent Framework, LlamaIndex Workflows, Google ADK, OpenAI Agents SDK, Mastra.
- **Microsoft Agent Framework** — unified successor to AutoGen + Semantic Kernel (GA 1.0 April 2026).
- **Mastra** — TypeScript-first production framework.
- Источник: https://www.langchain.com/resources/ai-agent-frameworks

### 12. MCP Cheat Sheet & Best Practices
- MCP is NOT a REST API wrapper — это UI для non-human user.
- 6 best practices от Phil Schmid: описание инструментов, error handling, stateless design.
- WebMCP — W3C Browser AI Tool API (регулирует JS-функции как AI-callable tools).
- Website: https://www.webfuse.com/mcp-cheat-sheet

### 13. Agent Skills — SKILL.md Spec Maturity
- Официальная спецификация SKILL.md от Agent Skills community.
- Progressive disclosure, directory conventions, authoring patterns, output-quality evals.
- Связано с Hermes Agent skills system.
- Источник: https://www.webfuse.com/mcp-cheat-sheet (agent skills section)

---

## Технические проблемы базы

- **validate-vault.sh** имеет `#!/usr/bin/env python3` shebang — работает при запуске через `python3`, но сломан при прямом запуске (из-за неверного shebang для файла с `.sh` расширением). Нужен рефакторинг: либо переименовать в `.py`, либо исправить shebang на `#!/usr/bin/env python3` (уже стоит — проблема в том что shell не умеет запускать python скрипты напрямую без правильного shebang на всех системах).
- **pre-commit hook** корректно вызывает скрипты через `python3`, поэтому CI не страдает.

## TODO из предыдущего аудита (29.06.2026)

**P0 — критичные (всё ещё не сделано):**
- agent-harness.md — добавить «Связанные заметки» (16+ ссылок)
- agent-skills-and-rules.md — добавить «Связанные заметки» (9+ ссылок)
- working-with-coding-agents.md — добавить «Связанные заметки» (13+ ссылок)

**P1 — всё ещё открыто:**
- 9 sources без секции «Связи»
- agent-use-cases.md без «Связанные заметки»
- Множество bidirectional ссылок между bitgn-файлами

**P3 — новые заметки (расширение базы):**
- rerankers.md, agent-memory-patterns.md, mcp-deep-dive.md, платформенные заметки

---

## 🔴 NEW — High Priority (02.07.2026)

### 14. MCP 2026-07-28 RC — Deep Dive Impact
- **Stateless core is production-ready now** — no sessions, no handshake. Load-balanced MCP servers without sticky sessions.
- **MCP Apps (SEP-1865)** — server-rendered HTML in sandboxed iframes; tools declare UI templates ahead of time for security review.
- **Tasks graduates to extension (SEP-2663)** — breaking change for anyone using experimental Tasks API.
- **JSON Schema 2020-12** — full support for `oneOf`, `anyOf`, `$ref`, `$defs` in inputSchema/outputSchema.
- **Roots, Sampling, Logging deprecated** — annotation-only, 12+ months notice.
- **Authorization hardening** — six SEPs (iss validation, application_type, refresh tokens, scope accumulation).
- **Enterprise-Managed Authorization (EMA)** — zero-touch OAuth for MCP, SOC 2 Type II audited gateways.
- Источник: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate

### 15. MCP Gateways — Enterprise Production Pattern
- **MCPX** (Lunar.dev), **Docker MCP Gateway**, **Microsoft MCP Gateway**, **IBM ContextForge**, **MCPJungle**, **Obot**, **MintMCP** (SOC 2 Type II), **Bifrost** (Maxim AI).
- 80% of Fortune 500 have active AI agents; 28% have MCP servers in production.
- Pattern: agent → MCP Gateway → MCP Servers (auth, RBAC, audit, rate limiting, tool filtering).
- Источник: https://www.truefoundry.com/blog/best-mcp-gateways

### 16. Microsoft Agent Framework 1.0 — Unified AutoGen + Semantic Kernel
- **GA April 2026** — production-ready unified SDK for Python and .NET.
- Workflows: graph-based with type-safe routing, checkpointing, human-in-the-loop.
- Migration paths from Semantic Kernel and AutoGen documented.
- Прямой конкурент LangGraph, OpenAI Agents SDK, Google ADK.
- Источник: https://devblogs.microsoft.com/agent-framework/

### 17. Agent Protocol Ecosystem 2026 — Six Protocols
- **MCP** (tools), **A2A** (agent coordination), **ACP** (commerce), **UCP** (Google commerce), **AG-UI** (agent→UI), **AP2/X42** (payments).
- Enterprise agent stack uses all four: MCP → A2A → ACP/UCP.
- Источник: https://www.mindstudio.ai/blog/six-agent-protocols-ai-builders-2026

### 18. Production Failure Framework — 7 Patterns
- Verified: **88% never reach production**; avg direct cost $340K/project failure.
- 7 failure patterns: scope creep, data quality, security blockers, integration complexity, cost overruns, governance gaps, org resistance.
- Patterns 1+2 cause 61% of failures.
- Upfront prevention ($50K) reduces expected cost from $572K to $147.5K.
- Источник: https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework

## 🟡 NEW — Medium Priority (02.07.2026)

### 19. Agent Evaluation 2026 — Three-Layer Framework
- Three levels: end-to-end (task completion rate), trajectory-level (tool calls, reasoning), component-level (individual tools).
- **Task completion rate** and **human override rate** are the two most important metrics.
- Top platforms: Maxim AI, LangSmith, Braintrust, DeepEval, Phoenix.
- **METR approach**: "how long should a task be for 50% agent success rate".
- Источник: https://www.morphllm.com/ai-agent-evaluation

### 20. OpenAI Codex CLI 2026 — GPT-5.5 Agentic Coding
- 4M developers/week; Rust-based; runs locally; MCP support; sandbox execution.
- 4× fewer tokens per task vs Claude Code (independent tests).
- Skills catalog, sandboxes (macOS, Linux, Windows), execpolicy rules, plugins.
- Источник: https://tosea.ai/blog/openai-codex-complete-guide-2026

### 21. Google ADK (Agent Development Kit)
- Open-source Apache 2.0; model-agnostic; multi-language (Python, TypeScript, Go, Java).
- Hierarchical multi-agent, A2A-native, OpenTelemetry, built-in evaluation tools.
- Источник: https://www.infoworld.com/article/4153857/

### 22. Hermes Agent — v0.17.0 "The Reach Release" (June 19, 2026)
- Multi-agent Kanban, persistent `/goal`, Checkpoints v2, i18n locales.
- Background agents, WhatsApp integration, image editing, automation templates.
- 60+ tools, 22 messaging platforms, NVIDIA RTX/DGX Spark support.
- Hermes Desktop v0.15.2 (native macOS/Windows/Linux GUI) bundled with v0.15.2.
- 180K+ GitHub stars.
- Источник: https://medium.com/codetodeploy/hermes-v0-17-7-new-features

### 23. Anthropic Agentic Coding Trends 2026
- 8 trends: from single AI assistants to coordinated agent teams; autonomous runs hours/days.
- Rakuten case study: Claude Code → 12.5M LOC codebase, 7 hours autonomous, 99.9% accuracy.
- 60% work with AI, but only 0–20% full delegation.
- Engineers → orchestrators instead of writers.
- Источник: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf

### 24. smolagents — Hugging Face Agent Framework
- New framework in JetBrains' 2026 top list; lightweight, open-source.
- Missing from ai-db tools/ directory.

## 🟢 Lower Priority — Issues & Improvements (02.07.2026)

### 25. pre-commit hook check
- The `.githooks/pre-commit` is NOT auto-enabled. Developers must run `git config core.hooksPath .githooks` after clone.
- This should be documented in README.md.

### 26. validate-vault.sh — rename to .py
- Has `#!/usr/bin/env python3` shebang but `.sh` extension — works via `python3` call but breaks direct execution.
- Rename to `validate-vault.py` and update references in `.githooks/pre-commit`, `AGENTS.md`, `README.md`.

### 27. tool-use-and-mcp.md — Outdated on MCP version
- Содержит общие принципы, но не упоминает MCP 2026-07-28 RC (stateless core, extensions, deprecations).
- Нужно обновить с учётом последней спецификации.

### 28. No "Related notes" section in three key files
- backlog.md(P0) отмечает, что три ключевых файла (agent-harness.md, agent-skills-and-rules.md, working-with-coding-agents.md) не имеют «Связанные заметки» — всё ещё актуально.

### 29. Agent Frameworks — Missing entries
- **Google ADK** — нет в tools/frameworks/
- **smolagents** (Hugging Face) — нет в tools/frameworks/
- **Mastra** (TypeScript-first) — нет в tools/frameworks/
- **OpenAI Agents SDK** — упоминается в references, но нет canonical страницы в tools/
- **Haystack** (deepset) — упоминается в исследованиях, нет в tools/

### 30. Sources — Missing entries for new research
- MCP 2026-07-28 RC official blog post
- Digital Applied — 88% Production Failure Framework
- Digital Applied — Agent Protocol Ecosystem Map 2026
- MorphLLM — AI Agent Evaluation 2026
- JetBrains — Top Agentic Frameworks 2026
- NVIDIA Blog — Hermes on RTX/DGX Spark
- WorkOS — Everything about MCP in 2026
- The New Stack — MCP growing pains for production

---

*Обновлено: 02.07.2026*
