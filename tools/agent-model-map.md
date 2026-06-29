# Модельная карта для AI-агентов

Актуально на 2026-06-24. Для агентов модель выбирается не только по “умности”, а по способности работать с tools, долгим контекстом, reasoning budget, multimodal input, кодом, latency и ценой.

## Критерии выбора

| Критерий | Что проверить evals |
|---|---|
| Reasoning | multi-step planning, устойчивость к конфликтам инструкций |
| Tool calling | правильный tool, корректные аргументы, low invalid-call rate |
| Long context | не теряет ранние constraints и citations |
| Multimodal | понимает скриншоты, документы, видео/аудио при необходимости |
| Code | repo navigation, tests, patch quality, minimal diff |
| Cost/latency | p95 latency, token cost, reasoning effort |
| Reliability | variance между запусками, recovery после tool errors |
| Safety | отказ от unsafe side effects и injection resistance |

## Provider families

| Семейство | Когда рассматривать |
|---|---|
| OpenAI GPT-5.5 / GPT-5 series | tool-heavy, reasoning, structured outputs, Responses API, hosted tools |
| Anthropic Claude Fable/Opus/Sonnet/Haiku | long-horizon agentic work, coding, large context, strong writing/analysis |
| Google Gemini | multimodal input, Google ecosystem, long context, tools/computer use |
| Mistral | European provider, latency/cost-sensitive apps, open/enterprise options |
| Open/self-hosted models | data control, cost predictability, offline/private deployments |

## Default decision tree

1. Если нужен provider-hosted agent stack и tools: начать с OpenAI GPT-5.5 через Responses API.
2. Если главный сценарий — coding/repo work: сравнить Claude Opus/Sonnet, OpenAI GPT-5.5 и coding-specific eval.
3. Если нужны multimodal документы/изображения/аудио: проверить Gemini и OpenAI multimodal модели на собственных данных.
4. Если важны privacy/data residency/cost: добавить self-hosted baseline.
5. Если latency важнее reasoning: брать smaller/fast model и проверять escalation к сильной модели.
6. Для production не выбирать модель без task-specific eval.

## Reasoning effort

[OpenAI](platforms/openai.md) docs для GPT-5.5 рекомендуют Responses API для reasoning/tool-calling/multi-turn use cases и настройку `reasoning.effort`. Balanced стартовая точка — medium, но для latency-sensitive задач стоит проверять low, а high/xhigh оставлять для сложных асинхронных агентных задач.

Практическое правило: reasoning effort — это не ручка “сделай лучше”, а budget. Его меняют только после evals.

## Model routing

Для production agents часто нужна маршрутизация:

- fast model для классификации и extraction;
- reasoning model для планирования и сложных tool decisions;
- code-strong model для repo changes;
- vision/multimodal model для screenshots/PDF;
- fallback model при rate limits;
- human handoff при high-risk или low-confidence.

## Что фиксировать в run metadata

- provider;
- model id или pinned snapshot;
- reasoning effort;
- prompt version;
- tool schema version;
- retrieval index version;
- context window usage;
- input/output tokens;
- cost;
- latency;
- eval suite version.

## Primary sources

- [OpenAI latest model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Anthropic models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Google Gemini models](https://ai.google.dev/gemini-api/docs/models)
- [Mistral models overview](https://docs.mistral.ai/models/overview)

## Связанные заметки

- [Модели для эмбеддингов](embedding-models.md)
- [Evaluations для агентов](../patterns/implementation/agent-evaluations.md)
- [Исследование фреймворков](agent-frameworks-research.md)
- [OpenAI](platforms/openai.md) — GPT-5.5 в карте моделей
- [Anthropic (Claude)](platforms/anthropic.md) — Claude модели в карте
- [Google Gemini](gemini.md) — Gemini model family в карте
- [Mistral AI](platforms/mistral.md) — Mistral модели в карте
- [DeepSeek](platforms/deepseek.md) — DeepSeek модели в карте
- [Qwen (Alibaba)](platforms/qwen.md) — Qwen модели в карте
- [MiMo Code](models/mimo-code.md) — MiMo модели в карте
- [Z.ai](platforms/z-ai.md) — open-weight модели GLM
