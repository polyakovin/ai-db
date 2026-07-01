---
title: File System Tools for Agents
url: https://github.com
type: url
category: tools
tags: [filesystem, files, agents, tools, io]
added: 2026-07-01
status: new
---

# File System Tools for Agents

Инструменты для работы с файловой системой в AI-агентах — чтение, запись, навигация, поиск файлов, управление директориями.

## Обзор

Работа с файлами — базовая способность для coding agents, automation workflows и data processing. Агентные инструменты файловой системы предоставляют:

- **Read/Write** — чтение и запись файлов
- **Navigation** — листинг директорий, переходы
- **Search** — поиск файлов по имени, содержимому, паттернам
- **Manipulation** — copy, move, delete, rename
- **Permissions** — управление правами доступа
- **Safety** — sandbox, ограничения на запись

## Ключевые инструменты

### Native File System (OS-level)

| Параметр | Значение |
|----------|----------|
| **API** | Python `os`, `pathlib`, `shutil` |
| **Доступ** | Полный доступ к FS (ограничен правами процесса) |
| **Цены** | Встроено в Python/Node.js |
| **Open Source** | N/A (стандартная библиотека) |

**Возможности:**
- Прямой доступ к файловой системе через стандартные библиотеки
- Полная kontrolь над операциями
- Требует явной реализации safety checks

**Пример (Python):**
```python
from pathlib import Path

# Read
content = Path("file.txt").read_text()

# Write
Path("output.txt").write_text("Hello, World!")

# List directory
files = list(Path(".").glob("*.py"))

# Navigate
parent = Path(__file__).parent.parent
```

### Claude Code File System

| Параметр | Значение |
|----------|----------|
| **URL** | https://claude.ai/code |
| **API** | Built-in tool (Claude Code) |
| **Модели** | Claude Sonnet/Opus |
| **Цены** | Через Claude Code subscription |
| **Open Source** | Нет |

**Возможности:**
- Built-in file read/write/edit tools
- Multi-file editing с context awareness
- Git integration (diff, commit, push)
- Safety prompts для destructive operations
- Workspace-aware (понимает структуру проекта)

**Пример использования:**
```
Claude, read src/main.py and fix the bug in line 42
Create a new file tests/test_auth.py with unit tests
Search for all TODO comments in the codebase
```

### OpenAI Codex CLI / Agents SDK

| Параметр | Значение |
|----------|----------|
| **URL** | https://github.com/openai/codex |
| **API** | CLI + Python SDK |
| **Модели** | GPT-4o, o3, Codex |
| **Цены** | API pricing |
| **Open Source** | Да (CLI) |

**Возможности:**
- File system access через sandbox
- Shell command execution
- Git operations
- Approval workflow для sensitive operations
- Session persistence

### LangChain File Tools

| Параметр | Значение |
|----------|----------|
| **URL** | https://python.langchain.com/ |
| **API** | Python SDK |
| **Модели** | Model-agnostic |
| **Цены** | Open Source |
| **Open Source** | Да (MIT) |

**Возможности:**
- `FileManagementTool` — read, write, list, delete
- `DirectoryFileManagement` — работа с директориями
- Интеграция с agent loops
- Customizable file filters

**Пример:**
```python
from langchain.agents import Tool
from langchain_community.tools.file_management import ReadFileTool

read_file = ReadFileTool()
content = read_file.run({"file_path": "data/config.yaml"})
```

### Superfile / E2B File System

| Параметр | Значение |
|----------|----------|
| **URL** | https://e2b.dev/ |
| **API** | Python/JS SDK |
| **Модели** | N/A (sandbox infrastructure) |
| **Цены** | Free tier → Paid от $20/мес |
| **Open Source** | SDK — да, infrastructure — нет |

**Возможности:**
- Isolated sandbox для file operations
- Pre-configured environments (Python, Node, etc.)
- Secure execution (no host FS access)
- Multi-file operations
- Session persistence и resume

## Когда использовать

| Сценарий | Рекомендуемый инструмент |
|----------|-------------------------|
| **Coding agent (local)** | Native FS + safety wrapper |
| **Claude Code workflow** | Built-in Claude Code tools |
| **OpenAI agent** | Codex CLI / Agents SDK |
| **LangChain agent** | LangChain File Tools |
| **Sandboxed execution** | E2B File System |
| **Production safety** | E2B или custom sandbox |

## Безопасность и ограничения

- **Sandbox boundary** — никогда не давать полный доступ к host FS
- **Write restrictions** — ограничивать запись critical directories
- **Path traversal** — валидация путей (`../`, absolute paths)
- **File size limits** — защита от чтения огромных файлов
- **Symlink attacks** — проверка на symbolic links
- **Permissions** — запуск от non-privileged user

### Пример safety wrapper (Python)
```python
from pathlib import Path

class SafeFileReader:
    def __init__(self, allowed_root: str):
        self.root = Path(allowed_root).resolve()
    
    def read(self, relative_path: str) -> str:
        file_path = (self.root / relative_path).resolve()
        # Prevent path traversal
        if not str(file_path).startswith(str(self.root)):
            raise ValueError("Path traversal detected!")
        return file_path.read_text()
```

## Интеграция с агентами

### LangChain Agent
```python
from langchain.agents import initialize_agent, Tool
from langchain_community.tools.file_management import (
    ReadFileTool, WriteFileTool, ListDirectoryTool
)

tools = [
    ReadFileTool(),
    WriteFileTool(),
    ListDirectoryTool()
]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
```

### Custom Tool (OpenAI Functions)
```python
import json
from openai import OpenAI

client = OpenAI()

tools = [{
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Read contents of a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {"type": "string"}
            },
            "required": ["file_path"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Read src/main.py"}],
    tools=tools
)
```

## Связи

- [Code Execution](code-execution.md) — запуск кода с file I/O
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — интеграция file tools в harness
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — file operations в coding workflows

---

*Добавлено: 2026-07-01*
