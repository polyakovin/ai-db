---
title: MarkItDown
url: https://github.com/microsoft/markitdown
type: url
category: tools
tags: [document-conversion, markdown, ingestion, python, llm]
added: 2026-07-26
status: verified
---

# MarkItDown

MarkItDown — open-source Python-утилита Microsoft для преобразования файлов и внешних материалов в Markdown, ориентированный на LLM и text-analysis pipelines. Приоритет инструмента — сохранить полезную структуру документа, а не воспроизвести исходный layout с высокой визуальной точностью.

## Поддерживаемые источники

В базовую и опциональную поставку входят конвертеры для PDF, PowerPoint, Word, Excel, изображений, аудио, HTML, CSV, JSON, XML, ZIP, EPUB и YouTube URL. Доступность конкретного формата зависит от установленной группы optional dependencies.

## Интерфейсы

- CLI: `markitdown input.pdf -o output.md`
- Python API: `MarkItDown().convert(...)`
- Ввод через stream для встраивания в ingestion pipeline.
- Plugin architecture; сторонние плагины отключены по умолчанию и включаются явно.
- Опциональная интеграция с Azure Document Intelligence, Azure Content Understanding и LLM Vision для расширенного извлечения.

## Роль в agent pipeline

MarkItDown удобно использовать как parser/normalizer между acquisition и chunking:

```text
file or URL
  -> MarkItDown
  -> normalized Markdown + provenance metadata
  -> policy checks
  -> chunking / index
  -> agent context
```

Сам конвертер не решает provenance, access control, дедупликацию и retrieval quality. Эти metadata и проверки должен добавлять внешний ingestion pipeline.

## Ограничения и безопасность

- Результат нужно проверять на потерю таблиц, layout, формул, изображений и OCR-ошибки.
- Конвертация выполняется с правами текущего процесса: untrusted input требует изоляции и минимальных filesystem/network permissions.
- Следует выбирать наиболее узкий метод конвертации (`convert_stream`, `convert_local` и т. п.), а плагины включать только после проверки.
- Для документов, где важна визуальная идентичность, нужен render-based converter или ручная QA.

## Связи

- [Автоматизация сбора внешнего контекста](../../patterns/architecture-design/external-context-collection.md) — место нормализации документов в ingestion pipeline.
- [File System](file-system.md) — границы доступа к локальным файлам.
- [Code Execution](code-execution.md) — изоляция конвертации недоверенных документов.
- [MarkItDown — репозиторий Microsoft](../../sources/libraries-tools/markitdown.md) — provenance.
