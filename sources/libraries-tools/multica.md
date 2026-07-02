---
title: Multica
url: https://multica.ai/
type: url
category: sources
tags: [agent-management, coding-agents, project-management, skills, runtimes, open-source]
added: 2026-07-02
status: new
---

# Multica

Multica - open-source platform for managing human + agent teams. It turns coding agents into first-class teammates: agents can be assigned issues, report progress, raise blockers, update statuses, comment, and reuse team skills.

## Official links

- **Website:** https://multica.ai/
- **Docs:** https://multica.ai/docs
- **Changelog:** https://multica.ai/changelog
- **GitHub:** https://github.com/multica-ai/multica

## Overview

- **Format:** product website, docs, changelog, open-source repository.
- **Core idea:** project management layer for human + AI agent collaboration.
- **Supported agent runtimes:** local daemon detects installed coding tools and registers them as runtimes.
- **Execution model:** agent work runs on the user's machine or self-hosted infrastructure; Multica coordinates task state and events.
- **Task lifecycle:** enqueue, claim, start, complete/fail, blocker reporting, and real-time progress streaming.
- **Skills model:** reusable capability definitions that can be shared across the team and attached to agents.
- **Deployment:** hosted cloud, desktop app, and self-hosted backend.
- **License:** modified Apache 2.0 with additional commercial hosting and frontend attribution restrictions.

## Key observations

- Multica treats agents as project-board participants rather than prompt-response tools.
- The platform separates coordination from execution: server state, comments, issues, and events live in Multica, while agent execution happens through local or self-hosted runtimes.
- Runtime management is a core product surface: online/offline status, usage charts, CLI detection, and multiple machines are part of the operating model.
- Skills are positioned as a compounding team asset, not only as per-agent prompt snippets.
- The source is useful as a practical reference for multi-agent work management, task lifecycle design, and human-agent collaboration UX.

## Relevance for ai-db

Useful as:

- Reference for agent project management and human-agent work queues.
- Example of first-class agent identity in boards, comments, assignees, and activity timelines.
- Runtime orchestration pattern for local coding agents.
- Skills library pattern for reusable operational capabilities.
- Open-source implementation of a managed agents platform.

## Status

Added: 2026-07-02

## Links

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) - Multica as a management layer around agent execution.
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) - task assignment, progress reporting, and review loops.
- [Skills и правила для агентов](../../patterns/implementation/agent-skills-and-rules.md) - reusable skills as shared agent capabilities.
