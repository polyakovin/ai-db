---
title: Ollama
url: https://ollama.ai/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Ollama

Локальный запуск LLM: скачай модель и запусти одной командой. Де-факто стандарт для локального инференса open-weight моделей.

## Ключевые возможности

- Одна команда: `ollama run llama3.2` — модель скачивается и запускается
- Поддержка GPU-акселерации (CUDA, Metal, ROCm)
- REST API (совместимый с [[../platforms/openai.md|OpenAI]] chat completions)
- Modelfile — кастомизация моделей (системный промпт, параметры, temperature)
- Multimodal модели (изображения на вход)
- Контекстная память между запросами
- Модели в один клик: Llama, Mistral, Gemma, Qwen, [[../platforms/deepseek.md|DeepSeek]], Phi, Command R+

## Модели / Продукты

- 100+ готовых моделей в реестре
- Кастомные модели через Modelfile
- Интеграция с [[../frameworks/langchain.md|LangChain]], [[../frameworks/llamaindex.md|LlamaIndex]], библиотеками Python/JS

## Цены и доступ

- **Open Source:** да, [MIT-лицензия](https://github.com/ollama/ollama)
- Полностью бесплатно (несёшь только затраты на железо)

## Агентные возможности

- API для tool calling через [[../platforms/openai.md|OpenAI]]-совместимый интерфейс
- Можно использовать как бэкенд для coding-агентов (через [[../platforms/openai.md|OpenAI]]-compatible endpoint)
- Локальный инференс — нет задержек сети и privacy-рисков
- Ограниченная поддержка function calling (зависит от модели)

## Open Source статус

**Полностью Open Source** (MIT). Модели в реестре — open weights (разные лицензии).

## Use Cases

- Локальный деплой coding-агента без облачных API
- RAG с локальной LLM (privacy-first)
- Эксперименты с open-weight моделями
- Edge-устройства (Raspberry Pi, ноутбуки)
- CI/CD: локальный инференс без интернета

## Отзывы и критика

- Плюсы: простота, скорость, огромный каталог моделей, open source
- Минусы: требует GPU для больших моделей; function calling ограничен

## Связи

- [OpenAI](../platforms/openai.md) — OpenAI-совместимый API
- [vLLM](vllm.md) — production-инференс (альтернатива Ollama)
- [Hugging Face](../hosting/huggingface.md) — источник моделей
- [Модельная карта](../agent-model-map.md)

*Добавлено: 2026-06-29*
