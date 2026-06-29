---
title: OpenMontage
url: https://github.com/calesthio/OpenMontage
type: url
category: sources
tags: [video-production, agentic, pipeline, open-source]
added: 2026-06-29
status: processed
---

# OpenMontage — Agentic Video Production System

- **GitHub:** [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)
- **License:** GNU AGPLv3
- **Статус:** #1 на GitHub Trending, Repository of the Day

## Описание

Первая open-source система видеопроизводства, управляемая AI-агентом. AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex) оркестрирует полный пайплайн: исследование, сценарий, генерация ассетов, монтаж, финальный рендер — всё по текстовым промптам.

**Ключевое отличие:** умеет делать не только слайд-шоу из картинок, но и настоящее видео из реальных motion-клипов (бесплатные стоковые архивы + открытые источники).

## Архитектура

```
agent (Claude/Cursor/...) → pipeline manifest (YAML) → stage director skills (Markdown) → Python tools → schema validation → render (Remotion/FFmpeg) → self-review
```

Трёхслойная архитектура знаний:
1. `tools/` + `pipeline_defs/` — что существует (48 Python-тулов + YAML-манифесты)
2. `skills/` — как использовать (per-pipeline stage directors, creative techniques)
3. `.agents/skills/` — как это работает (внешние технологические knowledge packs)

12 пайплайнов, каждый по цепочке: `research → proposal → script → scene_plan → assets → edit → compose`

## Пайплайны

| Пайплайн | Назначение |
|----------|-----------|
| Animated Explainer | Research + narration + visuals + music |
| Animation | Motion graphics, kinetic typography |
| Avatar Spokesperson | Avatar-driven presenter |
| Cinematic | Trailer, teaser, mood edits |
| Clip Factory | Batch коротких клипов из длинного источника |
| Documentary Montage | Тематический монтаж из бесплатных архивов |
| Hybrid | Source footage + AI support visuals |
| Localization & Dub | Субтитры, дубляж, перевод |
| Podcast Repurpose | Хайлайты подкаста → видео |
| Screen Demo | Screen recordings |
| Talking Head | Footage-led speaker |

## Бесплатный путь (Zero API Keys)

| Возможность | Бесплатный инструмент |
|------------|----------------------|
| Narration | Piper TTS (offline) |
| Open footage | Archive.org + NASA + Wikimedia Commons |
| Stock | Pexels + Unsplash + Pixabay |
| Composition | Remotion (React) + HyperFrames (HTML/GSAP) |
| Post-production | FFmpeg |
| Subtitles | Word-level auto-captions |

## Примеры с себестоимостью

- **"THE LAST BANANA"** — 60s Pixar-style short. 6 Kling v3 clips, Chirp3-HD narration, music. → **$1.33**
- **"VOID — Neural Interface"** — product ad, single API key (OpenAI). → **$0.69**
- **"Afternoon in Candyland"** — 12 FLUX images, crossfade, camera motion, particles. → **$0.15**

## Что интересно для ai-db

- **Agent-first архитектура**: агент читает YAML-манифест (pipeline_defs/) → stage director skills (Markdown) → вызывает Python-тулы — весь оркестрационный слой декларативный и читаемый.
- **Self-review цикл**: pre-compose validation + post-render self-review (ffprobe, frame extraction, audio analysis).
- **Scored provider selection** — 7-мерная оценка провайдеров (cost, quality, speed).
- **Resumable checkpoints** — JSON с логом решений, можно перезапустить пайплайн с любой стадии.
- **12 production pipelines** — готовые конструкции для видеопроизводства агентами.

## Связи с другими разделами

- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — обвязка вокруг агента, частью которой является OpenMontage
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — оркестрация агента для видеопроизводства
- [Skills и правила для агентов](../../patterns/implementation/agent-skills-and-rules.md) — слой stage director skills
- [Исследование фреймворков](../../tools/agent-frameworks-research.md) — сравнение подходов к оркестрации
- [Superpowers](../../sources/libraries-tools/superpowers.md) — похожая архитектура (skills + Python tools)

## Обзор ресурса

- **Автор:** Calesthio (calesthioailabs) — разработчик open-source AI-инструментов, также автор Crucix
- **Лицензия:** GNU AGPLv3
- **Статус:** #1 GitHub Trending, Repository of the Day (июнь 2026); активное развитие
- **Масштаб:** 12 production pipelines, 52+ tools, 500+ agent skills
- **Поддерживаемые AI-ассистенты:** Claude Code, Cursor, Copilot, Windsurf, Codex
- **YouTube:** @OpenMontage — каждое видео включает полный промпт, пайплайн, тулы и стоимость
- **Уникальность:** Первая open-source система, делающая полноценное видео (не только слайд-шоу) из реальных motion-клипов через AI-агента
- **Relevance:** Эталонная реализация agent-first архитектуры и агентного видеопроизводства

*Добавлено: 2026-06-29*
