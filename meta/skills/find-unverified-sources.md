# find-unverified-sources

Проверка базы знаний на источники, помеченные как unverified.

## Когда использовать

- При пуле изменений — проверить, не просочились ли новые unverified источники
- Перед аудитом vault
- После добавления нового источника

## Как искать

Поле статуса может называться по-разному. Искать **оба паттерна**:

```bash
# Pattern 1: status-based
rg -l 'status:\s*unverified' sources/ tools/ patterns/

# Pattern 2: provenance-based (старая конвенция)
rg -l 'provenance:\s*(draft|unverified)' sources/ tools/ patterns/
```

Или через Hermes tools:

```
search_files(path="sources/", pattern="status:\\s*unverified")
search_files(path="sources/", pattern="provenance:\\s*(draft|unverified)")
```

Повторить для `patterns/` и `tools/`.

## Типичные ошибки

1. **Искать только одно поле.** Файл может использовать `status:` вместо `provenance:` и наоборот.
2. **Искать по всему проекту.** Ограничь `sources/`, `tools/`, `patterns/` — в `meta/` и README unverified не бывает.

## Проверка

- [ ] Найдены все файлы с `status: unverified`
- [ ] Найдены все файлы с `provenance: draft|unverified`
- [ ] Каждый найденный файл или верифицирован, или заведена задача
