---
title: OpenScience
url: https://github.com/synthetic-sciences/openscience
type: url
category: sources
tags: [scientific-agents, ai-workbench, research, open-source, skills, mcp, provenance, compute]
added: 2026-07-06
status: verified
---

# OpenScience

OpenScience — open-source AI workbench для научных исследований от Synthetic Sciences. Пользователь задаёт исследовательскую цель, а агентная среда проходит research loop: читает литературу, формирует гипотезы, пишет и запускает код, выполняет эксперименты, обращается к научным базам и оформляет результат.

## Официальные ссылки

- **GitHub:** https://github.com/synthetic-sciences/openscience
- **Docs:** https://openscience.sh/docs
- **npm:** https://www.npmjs.com/package/@synsci/openscience
- **Releases:** https://github.com/synthetic-sciences/openscience/releases
- **Atlas:** https://app.syntheticsciences.ai

## Обзор ресурса

- **Автор:** Synthetic Sciences
- **Формат:** open-source репозиторий, CLI/browser workspace, документация, npm-пакет
- **Лицензия:** Apache-2.0
- **Темы:** scientific agents, research harness, domain skills, scientific database tools, MCP, local workspace, experiment provenance
- **Практическая ценность:** показывает, как собрать научного агента не как чат, а как рабочую среду с файлами, терминалом, редактором, LSP, scientific renderers, специализированными агентами и подключаемыми инструментами

## Ключевые наблюдения

- OpenScience запускается локально: CLI поднимает server и browser workspace на машине пользователя.
- Базовый агент `research` дополняется specialist-агентами `biology`, `physics`, `ml`, critique/literature-review sub-agents и read-only `plan` mode.
- Agent runtime вызывает shell, editor, LSP, MCP servers, scientific connectors и skills; модели маршрутизируются по запросам и могут приходить от разных провайдеров или локального inference.
- Scientific tool layer включает UniProt, PDB, Ensembl, ChEMBL, PubChem, arXiv, OpenAlex, Semantic Scholar и другие базы.
- Workspace хранит sessions, artifacts и provenance на диске; результаты можно шарить ссылками.
- Atlas — опциональная managed-платформа Synthetic Sciences для моделей, wallet, research graph и cloud compute; bring-your-own-key сценарий не требует аккаунта.
- Важная граница безопасности: агент не является sandboxed; permission system повышает прозрачность действий, но не заменяет контейнер или VM для изоляции.

## Relevance для ai-db

Полезен как:

- reference implementation для domain-specific research harness;
- пример AI workbench с научными коннекторами, skill packs и inline scientific renderers;
- пример локального agent runtime, где browser UI, terminal, file tree, editor и tool layer собраны в один исследовательский loop;
- источник паттернов для reproducible artifacts, provenance и experiment write-up;
- open-source альтернатива/соседний ориентир к Claude Science для научных агентов.

## Статус

Добавлено: 2026-07-06

## Верификация

- **Дата:** 2026-07-10
- **Метод:** открыт GitHub-репозиторий по URL https://github.com/synthetic-sciences/openscience
- **Результат:** репозиторий активен: 1.8k stars, 262 forks, 216 commits, 11 releases (latest v1.3.2 от 2026-07-09). Лицензия Apache-2.0. Основные языки: TypeScript (54.3%), Python (31.2%). Наличие ARCHITECTURE.md, AGENTS.md, CHANGELOG.md, CLAUDE.md подтверждает зрелость проекта. Вся информация в заметке соответствует реальному состоянию репозитория.

## Связи

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — OpenScience как domain-specific harness вокруг research agent.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — MCP servers, scientific connectors и agent tools.
- [Воспроизводимые рецепты AI-агентов](../../patterns/advanced/reproducible-agent-recipes.md) — provenance, artifacts, code и experiment write-up.
- [Claude Science](claude-science.md) — соседний reference point для scientific AI workbench.
