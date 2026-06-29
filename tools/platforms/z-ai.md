---
name: Z.ai
type: AI Platform
url: https://z.ai/
status: verified
---

# Z.ai

**Z.ai** (ранее Zhipu AI / 智谱AI, официально Knowledge Atlas Technology Joint Stock Co., Ltd.) — китайская AI-компания, разрабатывающая семейство моделей GLM (General Language Model). Основана в 2019 году как spin-off из Университета Цинхуа (основатели: Tang Jie, Li Juanzi; CEO: Zhang Peng). Один из «AI Tigers» Китая; третий по величине LLM-игрок по версии IDC. В январе 2025 года добавлена в Entity List США (санкции). 8 января 2026 года провела IPO на Гонконгской фондовой бирже (SEHK: 2513) — первая крупная китайская LLM-компания, вышедшая на биржу.

## Ключевые возможности

- **Семейство моделей GLM** — языковые модели от GLM-4 до GLM-5.2. Все модели с июля 2025 — под лицензией MIT.
- **GLM-5.2** (июнь 2026) — флагман: 753B параметров (40B активных, MoE), 1M-token контекстное окно, архитектурная инновация IndexShare (снижение FLOPs в 2.9× на 1M контексте). Лучшая open-weight модель на Intelligence Index v4.1 (51 балл).
- **Vision Language Models** — GLM-4.5V, GLM-4.6V, GLM-5V Turbo (мультимодальный агентный foundation model)
- **Video Generation** — CogVideoX-3 (0.20$/видео через API), «Ying» (текст-в-видео, 6-сек клипы за ~30 сек, запущен июль 2024)
- **Image Generation** — CogView-4 ($0.01/изображение), GLM-Image ($0.015/изображение)
- **Audio** — GLM-ASR-2512 (распознавание речи, $0.03/MTok ≈ $0.0024/мин)
- **Назначение:** AI-агент для управления смартфоном через голосовые команды и интерпретацию экрана (тапы, свайпы, ввод текста) — аналог [Computer Use](anthropic.md) от [Anthropic](anthropic.md)
- **AutoGLM Rumination (沉思)** — агент для deep research: поиск, планирование путешествий, написание отчётов
- **Coding Plan** — подписка с эндпоинтом, оптимизированным для кодинга; совместимость с [Claude Code](anthropic.md), OpenClaw, Cline, Kilo Code, Roo Code, Cursor, Continue.dev и др. (20+ инструментов)
- **Z Code** — GUI-IDE с multi-agent коллаборацией, SSH, мобильным запуском задач
- **[Anthropic](anthropic.md)-совместимый endpoint** — `api.z.ai/api/anthropic` — drop-in замена Claude в [Claude Code](anthropic.md)
- **Open Source** — модели открыты под лицензией MIT с июля 2025 (без региональных ограничений)

## Хронология релизов моделей

| Дата | Модель | Ключевые характеристики |
|------|--------|------------------------|
| Авг 2024 | GLM-4-Plus | Проприетарная |
| Окт 2024 | GLM-4-Voice | End-to-end speech LLM |
| Июл 2025 | GLM-4.5 / GLM-4.5-Air | MIT, 355B параметров |
| Авг 2025 | GLM-4.5V | VLM, 106B |
| Сен 2025 | GLM-4.6 | FP8/Int4 на чипах Cambricon; 200K контекст |
| Дек 2025 | GLM-4.6V / GLM-4.7 | Vision + флагманский кодинг |
| Фев 2026 | GLM-5 | 744B (40B активных), MIT, agentic engineering |
| Мар 2026 | GLM-5.1 | Улучшенный long-horizon coding, MIT |
| Июн 2026 | GLM-5.2 | 753B, 1M контекст, IndexShare, MIT |

## Архитектурные инновации (GLM-5.2)

- **IndexShare для DSA (Deep Sparse Attention):** один «indexer» на каждые 4 transformer-слоя; снижение per-token FLOPs в 2.9× на 1M контексте без потери качества.
- **Mixture of Experts (MoE):** ~40B активных параметров из 753B (5.4% активации).
- **Multi-Token Prediction (MTP):** увеличение acceptance length для speculative decoding на +20% (до 5.47 токенов).
- **Flexible Thinking Modes:** три уровня `reasoning_effort` — none / high (~95% качества за ~50% стоимости) / max (полное качество).

## Бенчмарки (GLM-5.2 — Июнь 2026)

### Long-Horizon Coding

| Бенчмарк | GLM-5.2 | Claude Opus 4.8 | GPT-5.5 |
|----------|---------|-----------------|---------|
| FrontierSWE | 74.4 | 75.1 | 72.6 |
| PostTrainBench | 34.3 | 37.2 | 28.4 |
| SWE-Marathon | 13.0 | 26.0 | 12.0 |

### Стандартный кодинг

| Бенчмарк | GLM-5.2 | GLM-5.1 | Claude Opus 4.8 | GPT-5.5 |
|----------|---------|---------|-----------------|---------|
| Terminal-Bench 2.1 | 81.0 | 63.5 | 85.0 | 84.0 |
| SWE-bench Pro | 62.1 | 58.4 | 69.2 | 58.6 |

### Рассуждение (Reasoning)

| Бенчмарк | GLM-5.2 | DeepSeek V4 Pro | Qwen3.7-Max | Claude Opus 4.8 |
|----------|---------|-----------------|-------------|-----------------|
| HLE | 40.5 | 37.7 | 41.4 | 49.8 |
| HLE w/ Tools | 54.7 | 48.2 | 53.5 | 57.9 |
| AIME 2026 | 99.2 | 94.6 | 97.0 | 95.7 |
| GPQA-Diamond | 91.2 | 90.1 | 90.0 | 93.6 |

### Агентность

| Бенчмарк | GLM-5.2 | Claude Opus 4.8 | GPT-5.5 | DeepSeek V4 Pro |
|----------|---------|-----------------|---------|-----------------|
| MCP-Atlas Public | 76.8 | 77.8 | 75.3 | 73.6 |
| Tool-Decathlon | 48.2 | 59.9 | 55.6 | 52.8 |

> **Intelligence Index v4.1 (Artificial Analysis):** GLM-5.2 = **51** — лучшая open-weight модель; опережает MiniMax-M3 (44), [DeepSeek](deepseek.md) V4 Pro (44), Kimi K2.6 (43).

## Сравнение с конкурентами (Июнь 2026)

| Характеристика | GLM-5.2 | [DeepSeek](deepseek.md) V4 Pro | [Qwen](qwen.md)3.6-35B-A3B |
|---------------|---------|-----------------|-----------------|
| Параметры (всего) | 753B (MoE) | 1.6T (MoE) | 35B (MoE) |
| Активных параметров | 40B | 49B | **3B** |
| Контекстное окно | 1M | 1M | ~128K |
| Лицензия | MIT | MIT | Apache 2.0 |
| Самостоятельный хостинг | Multi-GPU сервер | Multi-GPU сервер | **Одна 24GB GPU** |
| SWE-bench Pro | **62.1** | 55.4 | — |
| Terminal-Bench 2.x | **81.0** (2.1) | 67.9 (2.0) | — |
| Цена API (input/output $/MTok) | $1.40 / $4.40 | **$0.435 / $0.87** | $0.325 / $1.95 |

**Выводы:**
- **GLM-5.2:** лучшие показатели на SWE-bench Pro и Terminal-Bench среди open-weight; MIT; широкая экосистема интеграций
- **[DeepSeek](deepseek.md) V4 Pro:** самая низкая цена API; лучший на SWE-bench Verified (80.6%); 384K output
- **[Qwen](qwen.md)3.6-35B-A3B:** феноменальная эффективность (3B активных = 73.4 SWE-bench Verified); запуск на одной GPU

## AutoGLM — AI-агент для смартфонов

- **Релиз:** 31 марта 2025 (AutoGLM 沉思); декабрь 2025 — open-source (AutoGLM-Phone-9B)
- **Возможности:** полноценное управление смартфоном — интерпретация экрана, симуляция тапов/свайпов/ввода текста
- **Задачи:** заказ еды (Meituan), покупка билетов, навигация (Google Maps), работа с WeChat, Taobao и др.
- **Бенчмарки (arXiv 2411.00820):** Web: VAB-WebArena-Lite 55.2% (59.1% со второй попыткой), OpenTable 96.2%; Android: AndroidLab 36.2%, китайские приложения 89.7%
- **Open Source:** модель AutoGLM-Phone-9B доступна на [[../huggingface.md|Hugging Face]] и ModelScope; фреймворк Open-AutoGLM на GitHub
- **Контекст:** Z.ai заявляет, что работа над «phone use» велась с апреля 2023 (32 месяца разработки)

## Цены API (официальные, Z.ai — Июнь 2026)

### Текстовые модели (за 1M токенов)

| Модель | Input | Cached Input | Output |
|--------|-------|-------------|--------|
| GLM-5.2 | $1.40 | $0.26 | $4.40 |
| GLM-5.1 | $1.40 | $0.26 | $4.40 |
| GLM-5 | $1.00 | $0.20 | $3.20 |
| GLM-5-Turbo | $1.20 | $0.24 | $4.00 |
| GLM-4.7 | $0.60 | $0.11 | $2.20 |
| GLM-4.7-FlashX | $0.07 | $0.01 | $0.40 |
| GLM-4.6 | $0.60 | $0.11 | $2.20 |
| GLM-4.5 | $0.60 | $0.11 | $2.20 |
| GLM-4.5-Air | $0.20 | $0.03 | $1.10 |
| GLM-4.7-Flash | Бесплатно | Бесплатно | Бесплатно |
| GLM-4.5-Flash | Бесплатно | Бесплатно | Бесплатно |

### Vision-модели (за 1M токенов)

| Модель | Input | Output |
|--------|-------|--------|
| GLM-5V-Turbo | $1.20 | $4.00 |
| GLM-4.6V | $0.30 | $0.90 |
| GLM-4.5V | $0.60 | $1.80 |
| GLM-4.6V-Flash | Бесплатно | Бесплатно |

### Другие сервисы

| Сервис | Цена |
|--------|------|
| Web Search (built-in tool) | $0.01 / использование |
| CogView-4 (изображения) | $0.01 / изображение |
| GLM-Image | $0.015 / изображение |
| CogVideoX-3 (видео) | $0.20 / видео |
| GLM-ASR-2512 (аудио) | $0.03 / MTok (~$0.0024/мин) |

### Coding Plan (подписка)

| Тариф | Цена (мес.) | Квоты |
|-------|------------|-------|
| Lite | ~$10-18 | ~80 запросов / 5 часов |
| Pro | ~$30 | ~400 запросов / 5 часов |
| Max | ~$80 | ~1,600 запросов / 5 часов |
| Individual (годовая) | $12.60 | API токены + coding tools |

Все платные тарифы включают: GLM-5.2, GLM-5-Turbo, GLM-4.7, GLM-4.5-Air. Бесплатные модели: GLM-4.7-Flash, GLM-4.5-Flash, GLM-4.6V-Flash.

## Официальные ресурсы

- [Z.ai](https://z.ai/) — международный сайт
- [Z.ai API Platform](https://z.ai/model-api) — платформа API
- [Документация](https://docs.z.ai/guides/overview/quick-start)
- [API Reference](https://docs.z.ai/api-reference/introduction)
- [Pricing](https://docs.z.ai/guides/overview/pricing)
- [GitHub (zai-org)](https://github.com/zai-org)
- [HuggingFace (zai-org)](https://huggingface.co/zai-org)
- [Coding Plan](https://z.ai/subscribe)
- [Wikipedia](https://en.wikipedia.org/wiki/Z.ai)
- [BigModel.cn](https://bigmodel.cn/) — китайская платформа
- [Z Code IDE](https://zcode.z.ai/)
- [arXiv: GLM-5 Technical Report](https://arxiv.org/abs/2602.15763)

## API и интеграции

- **API Base (PAAS):** `https://api.z.ai/api/paas/v4/`
- **Coding Plan API Base:** `https://api.z.ai/api/coding/paas/v4/`
- **Anthropic-совместимый endpoint:** `https://api.z.ai/api/anthropic` (drop-in замена [Claude](anthropic.md))
- Совместимость с 20+ AI-coding инструментами: [Claude Code](anthropic.md), OpenClaw, Cline, Kilo Code, Roo Code, Cursor, Continue.dev, Crush, Factory, Droid, OpenCode, Trae и др.
- Модели API: `glm-5.2`, `glm-5.1`, `glm-5`, `glm-5-turbo`, `glm-4.7`, `glm-4.6`, `glm-4.5`, `glm-4.5-air`, `glm-5v-turbo`, `glm-4.6v`, `glm-4.5v`
- MCP-серверы (включены в Coding Plan): Vision Analysis, Web Search, Web Reader, Zread
- Поддерживаемое железо для self-host: NVIDIA (H20/H100), Huawei Ascend, Moore Threads, Cambricon, Kunlun Chip, MetaX, Enflame, Hygon

## Позиционирование и стратегия

- **Open Source first:** флагманские модели открываются в день релиза (MIT), без региональных ограничений. Стратегия: open source → принятие в US (через Fireworks, Groq, self-host) → рост API-выручки (по модели [DeepSeek](deepseek.md)).
- **Рынки:** Китай (BigModel.cn), международный (z.ai). Крупнейшая база пользователей — Индия; наибольшая выручка — США (50% overseas revenue). Инференс-серверы в Сингапуре; тренировка — в Китае.
- **Инвесторы:** Alibaba, Tencent, Meituan, Ant Group, Xiaomi, HongShan, Prosperity7 (Саудовская Аравия). Оценка ~$3B (май 2024).
- **Сотрудники:** 800+ (2024); core research team: 100–200 чел.
- **Вызовы:** санкции США (Entity List с января 2025); compute shortage (февраль 2026 — падение акций на 23%); data wall для текущей архитектуры.

## Use Cases

- **Coding Agent ([Claude Code](anthropic.md)-совместимость):** автономная разработка, отладка, рефакторинг, long-horizon задачи (600+ итераций VectorDB оптимизации, 8-часовое построение Linux desktop)
- **Agentic Engineering:** multi-step tool use, function calling, MCP-интеграции
- **Office Automation:** генерация .docx, .pdf, .xlsx из текстовых описаний (PRD, финансовые отчёты, планы уроков)
- **Mobile Agent (AutoGLM):** заказ еды, покупка билетов, навигация — голосом
- **Deep Research (AutoGLM Rumination):** поиск, анализ, написание отчётов
- **Video Generation (CogVideoX-3/Ying):** создание видео из текста/изображений
- **Перевод (CN↔EN):** near-parity с [Gemini](../gemini.md) 2.5 Pro; специализация на китайских интернет-мемах, эмодзи, аббревиатурах
- **Mixed-language codebases:** преимущество в командах с китайско-английским кодом

## Отзывы и критика

- **Сильные стороны:** лучшая open-weight модель по бенчмаркам (Июнь 2026); MIT-лицензия без ограничений; [Anthropic](anthropic.md)-совместимый API для бесшовной замены [Claude](anthropic.md); конкурентоспособная цена ($1.40/$4.40 за 1M токенов vs $5/$25 у Opus); широкий набор моделей (текст, vision, видео, аудио, агенты).
- **Слабые стороны:** высокие требования к самостоятельному хостингу (1.51 TB в BF16); throttling при пиковых нагрузках; отсутствие нативной IDE-интеграции (только через third-party); региональные риски (китайская компания под санкциями США); эффективный контекст ~60–100K (по собственному признанию в ChinaTalk), несмотря на заявленный 1M.
- **Simon Willison (Июнь 2026):** «GLM-5.2 is probably the most powerful text-only open weights LLM».
- **Vibe Coding Blog:** «The flat-rate Coding Plan tiers remain Zhipu's strongest value proposition».
- **Разработчики (Reddit r/LocalLLaMA):** GLM-4.6 показал сильные результаты в тестах на кодинг против [DeepSeek](deepseek.md) V3.2-Exp и [Qwen](qwen.md)3.

## Верификация

- **Дата:** 2026-06-29
- **Метод:** Открытие z.ai, Wikipedia, официальной документации, блогов Z.ai (GLM-5, GLM-5.1, GLM-5.2), страницы цен API, ChinaTalk, независимых обзоров (Vibe Coding, Flowtivity, Developers Digest, llm-stats.com), Artificial Analysis, Reddit.
- **Источники:** [Wikipedia](https://en.wikipedia.org/wiki/Z.ai), [z.ai](https://z.ai/), [Z.ai Docs](https://docs.z.ai/), [Z.ai Blog — GLM-5.2](https://z.ai/blog/glm-5.2), [Z.ai Blog — GLM-5.1](https://z.ai/blog/glm-5.1), [Z.ai Blog — GLM-5](https://z.ai/blog/glm-5), [ChinaTalk — The Z.ai Playbook](https://www.chinatalk.media/p/the-zai-playbook), [Developers Digest](https://www.developersdigest.tech/blog/glm-5-2-vs-deepseek-v4-vs-qwen3-open-weights-coding-showdown), [llm-stats.com](https://llm-stats.com/models/glm-5.2)
- **Статус изменён:** `verified` → `verified` (расширено)

## См. также

- [[../../tools/OVERVIEW.md|tools/OVERVIEW.md]] — обзор инструментов и платформ
- [[../../tools/agent-model-map.md|Модельная карта]] — open-weight модели в карте
- [[../../patterns/implementation/working-with-coding-agents.md|Работа с код-агентами]] — Claude Code с Z.ai backend
- [[../../patterns/architecture-design/agent-harness.md|Agent Harness]] — coding harness с открытыми моделями
