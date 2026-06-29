---
title: Gradio
url: https://www.gradio.app/
type: url
category: tools
tags: []
added: 2026-06-29
status: new
---

# Gradio

Быстрое создание веб-интерфейсов для ML-моделей: чаты, демо, прототипы. Де-факто стандарт для демонстрации ML-моделей.

## Ключевые возможности

- Python-библиотека: `gradio.Interface(fn=model, inputs=..., outputs=...)`
- Компоненты: чат (Chatbot), текст, изображения, аудио, видео, файлы, датафреймы
- Blocks API — сложные layout'ы с состоянием и событиями
- Интеграция с [[huggingface.md|Hugging Face]] Spaces (один клик для деплоя)
- Аутентификация (OAuth, [[huggingface.md|Hugging Face]], BASIC)
- Стриминг ответов
- Очереди для обработки concurrent запросов
- Темы и кастомизация UI

## Модели / Продукты

- Gradio (open-source библиотека)
- [[huggingface.md|Hugging Face]] Spaces (хостинг Gradio-приложений)

## Цены и доступ

- **Open Source:** да, [Apache 2.0](https://github.com/gradio-app/gradio)
- Бесплатно (локальный запуск) + HF Spaces (бесплатный тир с ограниченными ресурсами)
- HF Spaces PRO: $9/мес за CPU, GPU от $0.40/час

## Агентные возможности

- Быстрые UI для agent prototyping: чат-интерфейс за 5 строк кода
- Стриминг tool calls и промежуточных шагов агента
- Демонстрация RAG-агентов с поиском и источниками
- Хостинг агентов как публичных демо на HF Spaces

## Open Source статус

**Полностью Open Source** (Apache 2.0). Приобретена [[huggingface.md|Hugging Face]] в 2021.

## Use Cases

- Демонстрация RAG-агента с источниками
- Чат-интерфейс для coding-агента
- A/B-тестирование разных моделей/промптов через UI
- Быстрые прототипы для stakeholders
- Обучающие демо ML-концепций

## Отзывы и критика

- Плюсы: экстремальная простота, интеграция с HF, богатые компоненты
- Минусы: не для production backend, ограниченная кастомизация без Blocks API

## Связи

- [Hugging Face](huggingface.md) — хостинг через Spaces
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — UI для демонстрации
- [Evaluations для агентов](../../patterns/implementation/agent-evaluations.md) — интерфейс для human evaluation

*Добавлено: 2026-06-29*
