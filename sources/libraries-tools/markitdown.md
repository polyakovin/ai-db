---
title: MarkItDown — репозиторий Microsoft
url: https://github.com/microsoft/markitdown
type: url
category: sources
tags: [markitdown, document-conversion, markdown, ingestion, python]
added: 2026-07-26
status: used
---

# MarkItDown — репозиторий Microsoft

Официальный репозиторий open-source Python-утилиты Microsoft для преобразования документов и других файлов в Markdown для LLM и text-analysis pipelines.

## Что подтверждено

- Поддерживаются CLI и Python API.
- Конвертеры покрывают office files, PDF, изображения, аудио, HTML, text formats, archives, EPUB и YouTube URL.
- Dependencies разбиты по format-specific extras.
- Есть plugin architecture; плагины отключены по умолчанию.
- Цель — сохранить структуру и смысл для машинной обработки, а не обеспечить high-fidelity визуальное воспроизведение.
- Процесс конвертации имеет доступ к тем же filesystem и network resources, что и текущий процесс.

Устойчивые сведения перенесены в [canonical-заметку MarkItDown](../../tools/agent-tools/markitdown.md) и [pipeline сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md).

## Ограничения источника

- Качество извлечения зависит от формата, структуры документа, OCR и optional dependencies.
- Cloud-конвертеры Azure имеют отдельные условия, стоимость и privacy boundary.
- GitHub README описывает возможности проекта, но не заменяет eval на собственном наборе документов.

## Статус

Добавлено и интегрировано: 2026-07-26.
