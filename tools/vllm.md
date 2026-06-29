---
title: vLLM
url: https://github.com/vllm-project/vllm
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# vLLM

High-throughput LLM inference engine для production: PagedAttention, tensor parallelism, continuous batching. Стандарт для serving open-weight моделей.

## Ключевые возможности

- **PagedAttention** — управление KV-кэшем как виртуальной памятью (до 24× эффективнее)
- **Continuous batching** — динамическое досоставление batch'ей без ожидания
- **Tensor parallelism** — распределение модели по нескольким GPU
- **Quantization** — AWQ, GPTQ, FP8, INT8 для экономии VRAM
- **[[platforms/openai.md|OpenAI]]-совместимый API** — drop-in замена для любого кода, работающего с [[platforms/openai.md|OpenAI]]
- **Multi-LoRA** — serving нескольких fine-tuned адаптеров на одной модели
- **Speculative decoding** — ускорение через draft-модель
- **Prefix caching** — кэширование общих префиксов (system prompts)

## Модели / Продукты

- Поддержка 50+ архитектур (Llama, Mistral, Qwen, [[platforms/deepseek.md|DeepSeek]], Gemma, GPT-NeoX...)
- Совместимость с [[huggingface.md|Hugging Face]] моделями

## Цены и доступ

- **Open Source:** да, [Apache 2.0](https://github.com/vllm-project/vllm)
- Бесплатно (несёшь затраты на GPU/инфраструктуру)

## Агентные возможности

- [[platforms/openai.md|OpenAI]]-совместимый API — любой агентный фреймворк может использовать vLLM как бэкенд
- Поддержка tool calling (function calling) на уровне модели
- Prefix caching эффективен для agentic prompt'ов с повторяющимся system prompt
- Низкая latency critical для interactive agent loop

## Open Source статус

**Полностью Open Source** (Apache 2.0). Активное сообщество: 40K+ GitHub stars.

## Use Cases

- Production serving LLM для high-traffic агентов
- Multi-tenant SaaS: изоляция через Multi-LoRA
- Cost-efficient API для internal agent-систем (вместо [[platforms/openai.md|OpenAI]] API)
- Batch inference для офлайн-evaluations

## Отзывы и критика

- Плюсы: лучшая производительность среди open-source inference engines, активная разработка
- Минусы: сложная настройка для кластеров, требует выделенных GPU

## Связи

- [Ollama](ollama.md) — локальный инференс (проще, но менее производительный)
- [Hugging Face](huggingface.md) — источник моделей
- [OpenAI](platforms/openai.md) — OpenAI-совместимый API
- [Модельная карта](agent-model-map.md)

*Добавлено: 2026-06-29*
