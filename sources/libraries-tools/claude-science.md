---
title: Claude Science
url: https://www.anthropic.com/news/claude-science-ai-workbench
type: url
category: sources
tags: [anthropic, claude, science, ai-workbench, agents, provenance, mcp]
added: 2026-07-02
status: processed
---

# Claude Science

Официальный анонс и продуктовая страница Anthropic про Claude Science — beta-приложение для научных команд, где Claude работает как AI workbench: анализирует литературу и данные, запускает пайплайны, управляет вычислениями и сохраняет provenance результатов.

## Официальные ссылки

- **Announcement:** https://www.anthropic.com/news/claude-science-ai-workbench
- **Product page:** https://claude.com/product/claude-science

## Обзор ресурса

- **Источник:** Anthropic, 30 июня 2026
- **Формат:** продуктовый анонс + landing page
- **Темы:** scientific agents, reproducible artifacts, reviewer agent, scientific renderers, MCP/connectors, reusable skills, HPC/Modal compute orchestration
- **Практическая ценность:** показывает, как generalist agent, specialist agents, reviewer loop, domain tools, compute access и artifact provenance собираются в единый исследовательский harness
- **Доступ:** beta для Claude Pro, Max, Team и Enterprise; macOS и Linux; Team/Enterprise требуют включения администратором

## Ключевые наблюдения

- Claude Science — не новая модель, а приложение и рабочая среда вокруг Claude models.
- Каждый научный артефакт привязан к коду, окружению, описанию действий и истории диалога, что делает результат воспроизводимым и проверяемым.
- Reviewer agent проверяет citations, calculations и соответствие figures исходному коду.
- Workbench умеет работать с локальными и удаленными вычислениями: laptop, Linux box, HPC login node, Slurm over SSH, Modal.
- Domain setup включает genomics, single-cell, proteomics, structural biology, cheminformatics и доступ к 60+ научным базам и инструментам.
- Пайплайны можно сохранять как reusable skills, а лабораторные системы подключать через connectors.

## Статус

Обработано: 2026-07-02

## Связи

- [Anthropic (Claude)](../../tools/platforms/anthropic.md) — canonical-страница платформы и продуктовых фактов
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — Claude Science как domain-specific harness
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — connectors, MCP и domain tools
- [Воспроизводимые рецепты AI-агентов](../../patterns/advanced/reproducible-agent-recipes.md) — provenance и reproducible artifacts
