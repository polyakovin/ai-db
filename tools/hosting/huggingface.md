---
title: Hugging Face
url: https://huggingface.co/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Hugging Face

Платформа для ML-моделей, датасетов и демо-приложений. Крупнейший хаб open-source AI: 500K+ моделей, библиотеки Transformers, Diffusers, Datasets.

## Ключевые возможности

- **Model Hub** — 500K+ моделей: LLM, embeddings, vision, audio
- **Datasets** — 100K+ датасетов
- **Spaces** — хостинг [Gradio](gradio.md) и Streamlit демо
- **Transformers** — библиотека для загрузки и инференса любой модели
- **Diffusers** — генерация изображений (Stable Diffusion, FLUX)
- **TGI (Text Generation Inference)** — production serving LLM
- **Inference API/Endpoints** — managed inference
- **AutoTrain** — no-code fine-tuning

## Модели / Продукты

- Transformers (Python library, Apache 2.0)
- Diffusers (image generation, Apache 2.0)
- TGI (inference server, Apache 2.0)
- Inference API (платный managed сервис)
- Spaces (бесплатные/платные демо)

## Цены и доступ

- **Open Source:** библиотеки — да (Apache 2.0)
- **Hub:** бесплатно для публичных моделей/датасетов
- **PRO:** $9/мес (больше storage)
- **Inference API:** от $0.06/час

## Агентные возможности

- Загрузка и запуск open-weight LLM для agent-бэкенда
- Spaces для демонстрации агентов
- Интеграция с [LangChain](../frameworks/langchain.md), [LlamaIndex](../frameworks/llamaindex.md) и другими framework'ами через модельную экосистему
- TGI для production serving agent-моделей

## Open Source статус

**Частично.** Библиотеки — Apache 2.0. Hub — proprietary платформа, но с открытым API.

## Use Cases

- Поиск и сравнение open-weight моделей для агентов
- Демонстрация агентов через Spaces
- Fine-tuning моделей под агентные задачи
- Production serving через TGI

## Отзывы и критика

- Плюсы: крупнейшая ML-экосистема, стандартизация форматов моделей
- Минусы: фрагментация библиотек, сложный поиск качественных моделей среди 500K+

## Связи

- [Gradio](gradio.md) — демо через Spaces
- [Ollama](../inference/ollama.md) — локальный инференс HF-моделей
- [Модельная карта](../agent-model-map.md)
- [vLLM](../inference/vllm.md) — production serving

*Добавлено: 2026-06-29*
