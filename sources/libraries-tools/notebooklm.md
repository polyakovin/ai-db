---
title: NotebookLM — официальный продукт и справка
url: https://notebooklm.google.com/
type: url
category: sources
tags: [notebooklm, research, source-grounding, citations, google]
added: 2026-07-26
status: used
---

# NotebookLM — официальный продукт и справка

Официальный сервис NotebookLM и справочные материалы Google о source-grounded research, поддерживаемых типах источников, citations, Studio-артефактах и data handling.

## Проверенные материалы

- **Product:** https://notebooklm.google.com/
- **Learn about NotebookLM:** https://support.google.com/notebooklm/answer/16164461
- **Add or discover sources:** https://support.google.com/notebooklm/answer/16215270
- **Use chat:** https://support.google.com/notebooklm/answer/16179559
- **FAQ:** https://support.google.com/notebooklm/answer/16269187

## Практическая ценность

NotebookLM — готовый вариант для Q&A и синтеза по ограниченному корпусу без самостоятельной сборки RAG pipeline. Inline citations упрощают переход от ответа к evidence, а Studio превращает те же источники в обзоры и учебные артефакты.

Критично учитывать семантику импорта: web URL обычно даёт текст страницы, YouTube — transcript, а часть структуры Google-файлов может быть потеряна. Citation доказывает связь с импортированным текстом, но не качество исходного источника.

Сведения перенесены в [canonical-заметку NotebookLM](../../tools/platforms/notebooklm.md).

## Ограничения источника

- Product page требует Google Account и почти не раскрывает возможности без входа; факты проверены по Google Help.
- Limits и premium features меняются, поэтому числовые квоты не фиксируются как устойчивые знания.
- Data handling различается для personal, Workspace и Education accounts.

## Статус

Добавлено и интегрировано: 2026-07-26.
