---
title: Agent Communication Protocol (ACP)
url: https://agentcommunicationprotocol.dev/
type: url
category: sources
tags: [acp, a2a, agent-protocol, interoperability, multi-agent, beeai, open-source]
added: 2026-07-05
status: new
---

# Agent Communication Protocol (ACP)

Official documentation for Agent Communication Protocol (ACP), the IBM/BeeAI-originated open protocol for communication between AI agents, applications, and humans.

## Official links

- **Documentation:** https://agentcommunicationprotocol.dev/
- **GitHub:** https://github.com/i-am-bee/acp
- **ACP and A2A:** https://agentcommunicationprotocol.dev/about/mcp-and-a2a
- **Merge announcement:** https://github.com/orgs/i-am-bee/discussions/5

## Overview

- **Format:** documentation site, OpenAPI specification, Python SDK, TypeScript SDK, examples, and migration guidance.
- **Core idea:** agents from different frameworks can communicate through a standardized RESTful API with multimodal messages, agent discovery, sessions, and long-running runs.
- **Protocol surface:** REST endpoints such as agent discovery, run creation, run status, run events, cancellation, and resume for paused runs.
- **Data exchange:** message parts use MIME types, so text, JSON, files, images, media, and custom binary formats can share one message structure.
- **Runtime patterns:** supports synchronous, asynchronous, streaming, stateful, and stateless interaction patterns.
- **Current status:** ACP is now part of Agent2Agent (A2A) under the Linux Foundation. The ACP repository is archived, active ACP development is winding down, and users are directed toward A2A migration paths.

## Relationship to A2A

ACP and [Agent2Agent (A2A) Protocol](a2a-protocol.md) are not the same specification:

- ACP came from IBM/BeeAI and was REST/OpenAPI-first.
- A2A came from Google and is now the active Linux Foundation agent-to-agent interoperability standard.
- The ACP team announced that ACP is merging into A2A and that ACP assets and expertise will contribute to A2A.
- For new architecture notes, prefer A2A as the current protocol name; mention ACP only as a legacy/provenance source or migration context.

## Relevance for ai-db

Useful as:

- Historical context for the A2A standardization path.
- Reference for REST-first agent communication, agent discovery, runs, sessions, pause/resume, and multimodal message parts.
- Migration context for BeeAI and older ACP-compatible agents.
- A caution against treating every "ACP" mention as a current standalone A2A alternative.

## Status

Added: 2026-07-05

## Links

- [Agent2Agent (A2A) Protocol](a2a-protocol.md) - current protocol home for agent-to-agent interoperability after the ACP merge.
- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) - agent role coordination and handoffs.
- [Робастная multi-agent среда](../../patterns/architecture-design/robust-multi-agent-environment.md) - A2A as a scoped external-agent transaction.
