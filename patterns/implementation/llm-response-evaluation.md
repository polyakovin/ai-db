# Оценка ответов LLM

Оценка ответа LLM нужна не для абстрактного рейтинга модели, а для решения: можно ли выпускать этот prompt, модель, RAG-пайплайн или UX в следующий этап. Хороший eval проверяет конкретный use case, фиксирует критерии качества и отделяет субъективное "нравится" от воспроизводимого результата.

## Что оценивать

| Критерий | Вопрос | Сигналы |
|---|---|---|
| Correctness | ответ фактически верен | совпадает с reference, нет выдуманных фактов |
| Completeness | покрыта ли задача целиком | все обязательные пункты раскрыты, нет пропусков |
| Instruction following | соблюдены ли ограничения | формат, язык, роль, запреты, порядок действий |
| Grounding | опирается ли ответ на evidence | claims подтверждены источниками, citations точные |
| Relevance | отвечает ли именно на запрос | нет ухода в соседнюю тему, нет лишней болтовни |
| Clarity | можно ли использовать ответ | понятная структура, конкретные next steps |
| Safety | нет ли вреда или policy breach | отказ там, где нужен отказ, нет утечки приватных данных |
| Calibration | признает ли модель неопределенность | не уверена без данных, просит источник или уточнение |
| Consistency | стабилен ли результат | похожее качество при повторных запусках и paraphrase |
| Cost/latency | можно ли масштабировать | приемлемые токены, latency, judge cost |

Не все критерии равны. Для юридического RAG важнее factuality, grounding и отказ при слабом evidence. Для creative writing больше весят стиль, соответствие tone of voice и полезность для пользователя.

## Способы оценки

| Метод | Когда применять | Ограничение |
|---|---|---|
| Deterministic checks | формат, JSON schema, exact match, обязательные фразы, запрет слов | плохо видит смысл |
| Reference-based metrics | классификация, QA, extraction, summarization с golden answer | слишком строг к допустимым формулировкам |
| Semantic similarity | paraphrase, ответы с несколькими валидными формами | может принять близкий, но неверный ответ |
| Rubric scoring | качество письма, объяснения, консультации, summary | требует хорошей шкалы и калибровки |
| Pairwise comparison | выбор между prompt/model версиями | нужен контроль order/position bias |
| LLM-as-judge | масштабная оценка сложных ответов | судья сам ошибается и имеет bias |
| Human review | high-risk домены, спорные критерии, calibration set | дорого и медленно |
| Adversarial evals | jailbreak, prompt injection, ambiguity, misleading context | не заменяет обычный regression set |
| Production feedback | thumbs, edits, escalations, support tickets | шумный сигнал, зависит от UX |

Практичный baseline: сначала deterministic checks для того, что можно проверить кодом, затем LLM-as-judge по явной rubric, затем human review на небольшой calibration set.

## Обзор бенчмарков для LLM

Не существует одного бенчмарка, покрывающего всё. Реальные evals комбинируют несколько тестов под свой use case.

| Категория | Что оценивает | Ключевые бенчмарки |
|---|---|---|
| Общие знания | Широкий кругозор, ответы из разных областей | MMLU, MMLU-Pro |
| Рассуждение | Логика, здравый смысл, выводы | HellaSwag, ARC, BIG-bench |
| Математика | Решение задач уровня school — olympiad | GSM8K, MATH, AIME |
| Генерация кода | Рабочий код по описанию, решение issues | HumanEval, MBPP, SWE-bench (Verified / Pro) |
| Tool calling | Вызов функций по документации, serial/parallel, multi-step | **BFCL** (Berkeley Function Calling Leaderboard) — AST-валидация вызовов |
| Agentic coding | Сквозное решение задач на реальных репозиториях | SWE-bench Verified (500 задач), SWE-bench Pro (contamination-resistant) |
| Правдивость | Склонность к галлюцинациям | TruthfulQA, SimpleQA |
| Мультимодальность | Понимание изображений, таблиц, схем | MMMU, MMMU-Pro, MathVista |
| Безопасность | Джейлбрейк, вредный контент, bias | HarmBench, ToxiGen, HEx-PHI, **AgentHarm** (multi-step agent safety) |
| Практический рейтинг | Качество в живом общении | Chatbot Arena (pairwise дуэли), LiveBench (contamination-free, ежемесячное обновление) |

**Ограничения.** Data contamination — данные бенчмарка попадают в обучающую выборку, цифры становятся бессмысленными. Saturation — модели проходят старый тест слишком хорошо, он перестаёт разделять. LiveBench решает первое частым обновлением задач; SWE-bench Pro — второе усложнением сценариев. Для **агентных** бенчмарков (tool calling, agentic coding, safety) есть отдельная заметка [Evaluations для агентов](agent-evaluations.md).

## Минимальный eval set

Для одного use case заведите 30-100 примеров:

- happy path;
- edge cases и редкие форматы входа;
- ambiguous prompts, где правильный ответ - уточнить;
- negative cases, где нужно отказать или сказать "не знаю";
- known failure cases из багов и пользовательских жалоб;
- paraphrase одного и того же запроса;
- stale, conflicting или insufficient context;
- safety/privacy cases;
- examples с ожидаемым кратким и ожидаемым подробным ответом.

Каждый инцидент в production должен становиться новым eval case, иначе ошибка вернется после смены prompt, модели или retrieval.

## Структура тест-кейса

```yaml
id: qa-grounding-001
task: answer_question_with_sources
input:
  user_question: "Какие документы нужны для возврата?"
  context:
    - source_id: refund-policy-v3
      text: "..."
expected:
  must_include:
    - список обязательных документов
    - ссылка на refund-policy-v3
  must_not_include:
    - неподтвержденные сроки
  should_refuse_if:
    - context_is_missing
metrics:
  - correctness
  - grounding
  - citation_accuracy
  - instruction_following
grader:
  type: rubric
  pass_threshold: 0.8
```

## Rubric для LLM-судьи

LLM-судья должен получать не просьбу "оцени качество", а проверяемую шкалу:

```text
Оцени candidate answer по входному question, reference и retrieved evidence.

Верни JSON:
{
  "correctness": 0..5,
  "grounding": 0..5,
  "instruction_following": 0..5,
  "unsupported_claims": ["..."],
  "missing_requirements": ["..."],
  "pass": true|false
}

Правила:
- Ставь 0 за факт, который противоречит reference.
- Не награждай за красивый стиль, если ответ не grounded.
- Если evidence недостаточно, правильный ответ должен явно сказать об этом.
- Не учитывай длину ответа как самостоятельный плюс.
```

Для pairwise comparison скрывайте названия моделей, перемешивайте порядок A/B и прогоняйте часть примеров в обратном порядке. Иначе судья может предпочитать первый, более длинный или стилистически знакомый ответ.

## На что обращать внимание

### Factuality и hallucinations

Проверяйте каждое существенное утверждение: оно есть в reference/evidence, выводится из него или является неподтвержденной догадкой. Отдельно считайте unsupported claim rate.

### Grounding и citations

Цитата должна подтверждать именно тот claim, рядом с которым стоит. Плохой RAG-ответ часто выглядит уверенно, но ссылается на источник, где нужного факта нет.

### Instruction conflicts

Ответ может быть фактически верным, но нарушать формат, язык, tone, JSON schema, privacy rule или запрет на раскрытие внутренней логики. Такие нарушения лучше проверять отдельными graders.

### Refusal quality

Отказ оценивается не только по факту отказа. Хороший отказ кратко объясняет границу, не раскрывает опасные детали и предлагает безопасную альтернативу.

### Robustness

Прогоняйте paraphrase, длинный контекст, misleading context, prompt injection и пустые данные. Если качество держится только на одном аккуратном prompt, eval слишком слабый.

### Judge reliability

LLM-as-judge нужно калибровать на human labels. Следите за agreement с людьми, variance между запусками, bias к длине, позиции, стилю и ответам той же модельной семьи.

## Частые ошибки

- Оценивать только средний score без разбора failed cases.
- Смешивать разные критерии в один мутный "quality".
- Делать golden answer слишком узким для open-ended задачи.
- Использовать того же LLM-судью, под которого оптимизируется prompt, без human calibration.
- Не фиксировать версии prompt, модели, retrieval index и judge rubric.
- Убирать неудобные edge cases из eval set ради красивого pass rate.
- Считать production thumbs полноценной заменой offline evals.

## Минимальный workflow

1. Определить use case и критерии успеха.
2. Собрать eval set из реальных, синтетических и негативных кейсов.
3. Разделить graders: deterministic, semantic, rubric, human.
4. Зафиксировать baseline для текущего prompt/model.
5. Менять только одну крупную переменную за раз.
6. Сравнивать score, failed cases, cost, latency и safety failures.
7. Добавлять каждый новый bug как regression case.

## Источники

- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI Graders](https://developers.openai.com/api/docs/guides/graders)
- [Anthropic: Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Google Cloud: Gen AI evaluation service overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview)
- [Berkeley Function Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html) — бенчмарк для оценки ability LLM вызывать функции (tools): serial/parallel calls, AST-валидация, multi-turn, multiple programming languages. V3 добавляет multi-step и stateful сценарии. Использует AST evaluation method — не просто exact match, а проверка AST-дерева вызова.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217)

## Связанные заметки

- [Evaluations для агентов](agent-evaluations.md) - оценка всего workflow, tools и trace
- [RAG для AI-агентов](../architecture-design/rag-for-agents.md) - retrieval, grounding и citations
- [Context engineering](../fundamentals/context-engineering.md) - что попадает в prompt и как это влияет на качество
- [Human-in-the-loop UX](../production-operations/human-in-the-loop-ux.md) - human review, feedback и escalation
- [Антипаттерны агентных систем](../advanced/agent-antipatterns.md) - weak evals и другие ошибки
