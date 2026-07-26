---
title: LFM2.5-8B-A1B and LocalCowork
url: https://www.liquid.ai/blog/lfm2-5-8b-a1b
type: url
category: sources
tags: [local-ai, desktop-agent, mcp, tool-calling, mixture-of-experts]
added: 2026-07-26
status: used
---

# LFM2.5-8B-A1B and LocalCowork

Официальный анонс Liquid AI о модели LFM2.5-8B-A1B и переводе open-source desktop-агента LocalCowork на более компактную локальную модель.

## Проверенные источники

- **Анонс модели и обновления LocalCowork:** https://www.liquid.ai/blog/lfm2-5-8b-a1b
- **Model card:** https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- **GGUF и инструкция для llama.cpp:** https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF
- **LFM Open License 1.0:** https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
- **Код LocalCowork:** https://github.com/Liquid4All/cookbook/tree/main/examples/localcowork
- **Предыдущий LocalCowork benchmark:** https://www.liquid.ai/blog/no-cloud-tool-calling-agents-consumer-hardware-lfm2-24b-a2b

## Что подтверждено

- В мае 2026 года демонстрация LocalCowork перешла на LFM2.5-8B-A1B.
- В анонсе задействованы 67 инструментов в 13 MCP-серверах на одном ноутбуке, без облака и API-ключей.
- Модель имеет 8,3B параметров всего и 1,5B активных, context window 128K и отдельные GGUF, MLX и ONNX варианты.
- Код LocalCowork опубликован под MIT; модель использует отдельную LFM Open License 1.0.

## Расхождения и границы доверия

- На 2026-07-26 README LocalCowork всё ещё описывает прежнюю LFM2-24B-A2B конфигурацию, старый benchmark и download-команды. Новый анонс подтверждает смену модели, но репозиторий нельзя считать полностью обновлённой инструкцией по запуску LFM2.5 без проверки текущего config.
- Число около 5 GB на переданном скриншоте согласуется с заявлением блога «менее 6 GB» на протестированных laptop-конфигурациях, но не является гарантированным footprint для всех квантизаций и context lengths.
- Производительность и benchmark опубликованы самим вендором; независимая оценка в этот обзор не входила.
- Формулировка анонса «open-weight» не означает неограниченную коммерческую лицензию: Section 5 запрещает коммерческое использование организациям с годовой выручкой от $10 млн без отдельного соглашения.

## Практическая ценность

Материал показывает, что для интерактивного локального агента важны не только общие benchmark модели, но и latency выбора инструмента, размер tool surface, память на целевом устройстве, audit trail и human correction loop. Репозиторий дополнительно демонстрирует curated tool set и planner/router схему для масштабирования каталога инструментов.

## Связи

- [LocalCowork](../../tools/platforms/localcowork.md) — canonical-страница desktop-агента.
- [LFM2.5-8B-A1B](../../tools/models/lfm2-5-8b-a1b.md) — canonical-страница модели.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — перенесённый вывод о масштабировании tool surface.

## Статус

Добавлено и интегрировано: 2026-07-26.
