# Backlog — Новые темы для документирования

Найденные пробелы и тренды по результатам ночного аудита.

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

*Обновлено: 01.07.2026*
