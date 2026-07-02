---
title: Agent2Agent (A2A) Protocol
url: https://github.com/a2aproject/A2A
type: url
category: sources
tags: [a2a, agent-protocol, interoperability, multi-agent, mcp, open-source]
added: 2026-07-02
status: new
---

# Agent2Agent (A2A) Protocol

Official GitHub repository for Agent2Agent (A2A), an open protocol for communication and interoperability between opaque agentic applications.

## Official links

- **GitHub:** https://github.com/a2aproject/A2A
- **Documentation:** https://a2a-protocol.org/
- **Specification:** https://a2a-protocol.org/latest/specification/

## Overview

- **Format:** open-source protocol repository, documentation, specification, SDK links, samples.
- **Core idea:** agents built by different teams, frameworks, and servers can discover each other, communicate, and collaborate without exposing internal state, memory, or tools.
- **Protocol surface:** JSON-RPC 2.0 over HTTP(S), Agent Cards for discovery, synchronous request/response, streaming via SSE, and asynchronous push notifications.
- **Data exchange:** text, files, and structured JSON data.
- **SDK ecosystem:** Python, Go, JavaScript, Java, .NET, and Rust SDKs are linked from the repository.
- **Governance and license:** open-source project under the Linux Foundation, contributed by Google, licensed under Apache 2.0.

## Key observations

- A2A targets agent-to-agent collaboration, while MCP targets agent-to-tool/context connectivity; the two protocols are complementary rather than substitutes.
- Agent Cards are the central discovery primitive: they describe capabilities and connection information before collaboration starts.
- The protocol is useful for multi-agent systems where agents remain opaque services rather than shared in-process components.
- The repository is a strong provenance source for interoperability patterns, enterprise agent communication, and standardizing long-running collaboration between agents.

## Relevance for ai-db

Useful as:

- Reference for multi-agent interoperability and agent-to-agent coordination.
- Protocol-level complement to MCP in agent architectures.
- Source for discovery, capability negotiation, task lifecycle, streaming, and push-notification patterns.
- Open-source specification and SDK entry point for future practical experiments with A2A servers and clients.

## Status

Added: 2026-07-02

## Links

- [Multi-agent orchestration](../../patterns/implementation/multi-agent-orchestration.md) - agent-to-agent coordination and role separation.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) - A2A as a complement to MCP, not a replacement for tool access.
- [Безопасность агентных систем](../../patterns/architecture-design/agent-security.md) - opacity, trust boundaries, and permission design for agent collaboration.
