---
title: LFM2.5-8B-A1B
url: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
type: url
category: tools
tags: [llm, mixture-of-experts, local-ai, tool-calling, edge, open-weight]
added: 2026-07-26
status: verified
---

# LFM2.5-8B-A1B

LFM2.5-8B-A1B — reasoning-tuned text-only модель Liquid AI для локальных ассистентов, function calling и agentic workflow. Это sparse Mixture-of-Experts модель: общий объём задаёт качество и размер весов, а на каждом токене активируется только часть параметров.

## Характеристики

| Параметр | Значение |
|---|---|
| Параметры | 8,3B всего / 1,5B активных |
| Архитектура | 24 слоя: 18 double-gated LIV convolution + 6 GQA |
| Training budget | 38T токенов |
| Context window | 128K токенов |
| Модальность | Только текст |
| Языки | 10, включая английский, китайский, японский и основные европейские языки |
| Tool use | Function calling, structured outputs, multi-turn tool loop |

Модель использует ChatML-подобный шаблон. Нативный function calling возвращает Python-подобные вызовы между специальными токенами; JSON-формат нужно явно задать в system prompt, если harness ожидает строгий JSON.

## Форматы и runtime

- основной checkpoint — Transformers, [vLLM](../inference/vllm.md) и SGLang;
- GGUF — llama.cpp, [Ollama](../inference/ollama.md), LM Studio и совместимые runtime;
- MLX — Apple Silicon;
- ONNX — cross-platform inference.

Официальные материалы позиционируют модель для tool use, structured outputs, multilingual assistants и on-device workflow. Карточка модели отдельно предупреждает, что она не оптимальна для тяжёлого программирования и knowledge-intensive вопросов без retrieval.

## Память и производительность

Скриншот анонса указывает около 5 GB, а официальный блог сообщает менее 6 GB на протестированных laptop-конфигурациях. Это характеристика конкретной квантизации и runtime, а не универсальный размер: фактическая память зависит от формата весов, quantization, context length, KV cache и backend.

Liquid AI также публикует benchmark instruction following, math и tool use, но результаты self-reported. Перед выбором модели нужно проверить:

- точность выбора на собственных tool schemas;
- корректность аргументов и JSON/function-call формата;
- p50/p95 latency на целевом устройстве;
- память на реальной длине контекста;
- multi-step completion отдельно от single-step dispatch.

## Лицензия

Веса доступны по LFM Open License 1.0, а не по OSI-approved open-source лицензии. Лицензия разрешает использование, модификацию и распространение, но коммерческое использование разрешено только физическим лицам и организациям с годовой выручкой ниже $10 млн. Организациям, достигшим порога, требуется отдельное соглашение с Liquid AI.

## Когда рассматривать

- локальный персональный ассистент;
- privacy-sensitive tool-calling agent;
- быстрый router/dispatcher на consumer hardware;
- offline или edge deployment;
- self-hosted baseline для agent evals.

Для long-horizon autonomy, сложного coding и knowledge-heavy задач модель нужно сравнивать с более крупными моделями и усиливать retrieval, verifier или human-in-the-loop контуром.

## Связи

- [LocalCowork](../platforms/localcowork.md) — полностью локальная desktop-демонстрация модели.
- [Модельная карта для AI-агентов](../agent-model-map.md) — критерии выбора и evals.
- [Tool use, function calling и MCP](../../patterns/fundamentals/tool-use-and-mcp.md) — требования к tool contract и dispatch.
- [Официальный анонс и репозиторий](../../sources/libraries-tools/localcowork-lfm2-5.md) — provenance материала.

*Проверено: 2026-07-26*
