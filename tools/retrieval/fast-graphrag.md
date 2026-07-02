---
title: Fast GraphRAG
url: https://github.com/circlemind-ai/fast-graphrag
type: url
category: tools
tags: [rag, graphrag, knowledge-graph, retrieval, python, open-source]
added: 2026-07-02
status: new
---

# Fast GraphRAG

Fast GraphRAG - lightweight GraphRAG-библиотека для promptable, interpretable и incremental graph retrieval. Позиционируется как более быстрый и дешевый graph-based RAG слой.

## Ключевые возможности

- Domain-specific graph construction через domain prompt, example queries и entity types.
- Incremental updates для меняющихся корпусов.
- PageRank-based graph exploration.
- Async Python API.
- Возможность получать references к использованной информации.

## Когда применять

- Нужен GraphRAG-подход без тяжелой [Microsoft GraphRAG](microsoft-graphrag.md) pipeline.
- Важны incremental updates и низкая стоимость индексации.
- Команда хочет быстро встроить graph retrieval в свой Python pipeline.

## Когда не применять

- Нужна максимально зрелая enterprise-платформа с UI, users и RBAC.
- Требуется строгий graph database как system of record.
- Нужны широкие community summaries уровня [Microsoft GraphRAG](microsoft-graphrag.md).

## Open Source статус

- Репозиторий: [circlemind-ai/fast-graphrag](https://github.com/circlemind-ai/fast-graphrag)
- Пакет: `fast-graphrag`
- Лицензия: MIT
- Есть managed service от Circlemind.

## Связи

- [LightRAG](lightrag.md) - близкая lightweight GraphRAG-альтернатива.
- [nano-graphrag](nano-graphrag.md) - минимальная GraphRAG-реализация.
- [Retrieval tools overview](OVERVIEW.md) - карта выбора.
