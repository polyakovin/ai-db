---
title: Model Context Protocol Docs
url: https://modelcontextprotocol.io/docs/getting-started/intro
type: url
category: sources
tags: [mcp, connectors, tools, context, protocol]
added: 2026-07-02
status: verified
---

# Model Context Protocol Docs

Официальная документация MCP как открытого стандарта подключения AI-приложений к внешним системам.

## Описание

- **Основные темы:** MCP clients/servers, подключение data sources, tools и workflows.
- **Практическая ценность:** задаёт общий интерфейс для доступа агента к внешним источникам без N×M набора одноразовых интеграций.
- **Relevance:** базовый протокол для слоя automated context collection, особенно когда один источник должен быть доступен нескольким agent clients.

## Связи

- [Автоматизация сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md)
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md)

## Статус

Добавлено: 2026-07-02

## Верификация

- **Дата:** 2026-07-08
- **Метод:** web_extract — https://modelcontextprotocol.io/docs/getting-started/intro
- **Результат:** Официальная документация MCP подтверждена. Описан как открытый стандарт для подключения AI-приложений к внешним системам (USB-C для AI). Содержание заметки соответствует.
