---
title: NotebookLM
url: https://notebooklm.google.com/
type: url
category: tools
tags: [research, source-grounding, citations, documents, google]
added: 2026-07-26
status: verified
---

# NotebookLM

NotebookLM — исследовательский ассистент Google для работы с ограниченным пользователем корпусом источников. Внутри NotebookLM ответы чата grounding-ятся выбранными материалами и сопровождаются inline citations, по которым можно перейти к исходному фрагменту.

## Ключевые возможности

- Импорт PDF, DOCX, PPTX, Markdown, CSV, ePub, изображений, аудио, веб-страниц, публичных YouTube-видео и файлов Google Drive.
- Включение и исключение отдельных источников из контекста конкретного запроса.
- Ответы, обзоры источников и преобразование материалов в briefings, study guides, mind maps, audio/video overviews и другие Studio-артефакты.
- Поиск материалов в web и Drive; Deep Research может подготовить отчёт и набор источников для импорта.
- Синхронизация поддерживаемых файлов Google Drive и интеграция notebooks с Gemini Apps.

## Ограничения импорта

- Для веб-страницы импортируется основной текст, но не вложенные страницы, изображения или встроенное видео.
- Для YouTube используется доступная текстовая расшифровка.
- Комментарии и сноски Google-файлов могут не импортироваться.
- Citation подтверждает соответствие источнику, но не истинность самого источника; важные выводы всё равно требуют проверки provenance и качества материалов.

## Когда применять

NotebookLM подходит для:

- исследования закрытого набора документов;
- сравнения нескольких источников с быстрым переходом к цитатам;
- подготовки учебных и обзорных материалов;
- source-grounded Q&A без построения собственного RAG pipeline.

Для автоматизированного production-ingestion, собственных access policies, versioning и retrieval evals нужен отдельный pipeline.

## Приватность

Google указывает, что данные NotebookLM не используются для обучения продукта без отправки feedback. Для подходящих Workspace и Education аккаунтов uploads, queries и responses не проходят human review и не используются для обучения AI-моделей. Перед загрузкой чувствительных данных всё равно нужно сверять условия конкретного типа аккаунта и policy организации.

## Связи

- [Google Gemini](gemini.md) — экосистема моделей и интеграция notebooks с Gemini Apps.
- [Автоматизация сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md) — отличие интерактивного notebook от production ingestion.
- [RAG для AI-агентов](../../patterns/architecture-design/rag-for-agents.md) — grounding на выбранном корпусе.
- [NotebookLM — официальный продукт и справка](../../sources/libraries-tools/notebooklm.md) — provenance.
