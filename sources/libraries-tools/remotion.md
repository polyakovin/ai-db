# Remotion

**Source:** [remotion.dev](https://www.remotion.dev/)  
**GitHub:** [remotion-dev/remotion](https://github.com/remotion-dev/remotion)  
**License:** Специальная (требуется коммерческая лицензия в некоторых случаях)  

---

## Что это

Фреймворк для **программного создания видео с помощью React**. Видео описывается как React-компоненты — сцена, анимация, слои, композиции.

## Ключевые особенности

### Основной фреймворк
- Видео = React-компоненты: `<Composition>`, `<Sequence>`, кастомные `<Scene>`
- Каждый кадр — это React-рендер, анимации через CSS/JS, всё реактивно
- TypeScript из коробки

### Remotion Studio
- Визуальный редактор для сборки и превью композиций
- Timeline, перемотка, предпросмотр в реальном времени
- Hot-reload при изменении кода

### Rendering
- Локальный рендер (через Chrome/Chromium)
- **Lambda** — serverless рендер на AWS Lambda (масштабируется, платишь за CPU)
- **Player** — интерактивный проигрыватель Remotion-видео прямо в браузере (не рендерит, а проигрывает в реальном времени)
- **Recorder** — запись экрана/вкладки через браузер

### AI-интеграция
- Специальный раздел документации [по работе с AI coding agents](https://www.remotion.dev/docs/ai/coding-agents)
- MCP-сервер для Remotion
- System prompt для агентов, которые пишут Remotion-видео
- Just-in-time compilation — создание видео на лету через AI
- Prompt a video — текстовый промпт → готовое видео

### Экосистема
- **Templates** — стартеры для соцсетей, слайд-шоу, заголовков, повторяемых видео
- **Showcase** — продукты построенные на Remotion: audiograms, captioning tools, year-in-review генераторы
- **Editor Starter** (платный) — полноценный редактор с timeline, canvas, загрузкой ассетов

## Use Cases

| Сценарий | Как |
|----------|-----|
| Социальные видео | Слайд-шоу, заголовки, динамическая графика |
| Captioning | Автоматические субтитры, синхронизация с аудио |
| Data-видео | Дашборды, чарты, демо продукта — анимированные |
| Year-in-review | Персонализированные видео (GitHub Unwrapped и др.) |
| AI-генерация | Текстовый запрос → готовое видео через агента |

## Relevance для ai-db

Полезен как:
- Референс программного видеопроизводства с React
- Пример интеграции AI coding agents в production workflow (MCP, system prompt, JIT compilation)
- Serverless rendering pipeline (Lambda)
- Экосистема template'ов и Editor Starter как продукт поверх фреймворка
- Remotion Skill для агентов — можно адаптировать под свои workflow
