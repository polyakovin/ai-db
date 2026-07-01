---
title: Code Execution for Agents
url: https://e2b.dev/
type: url
category: tools
tags: [code-execution, sandbox, agents, tools, runtime]
added: 2026-07-01
status: new
---

# Code Execution for Agents

Инструменты для выполнения кода в AI-агентах — sandboxed runtime для запуска Python, JavaScript, SQL и других языков программирования.

## Обзор

Выполнение кода — критическая способность для coding agents, data analysis, и automated testing. Агентные инструменты code execution предоставляют:

- **Sandboxed runtime** — изолированное выполнение (без доступа к host system)
- **Multi-language support** — Python, JavaScript, SQL, R, etc.
- **Package management** — установка зависимостей
- **I/O isolation** — контролируемый доступ к файлам, сети
- **Timeout & resource limits** — защита от infinite loops, DoS
- **Result capture** — stdout, stderr, return values

## Ключевые инструменты

### E2B

| Параметр | Значение |
|----------|----------|
| **URL** | https://e2b.dev/ |
| **GitHub** | https://github.com/e2b-dev/e2b |
| **API** | Python, JS/TS SDK |
| **Модели** | N/A (sandbox infrastructure) |
| **Цены** | Free tier (500 часов/мес) → Paid от $20/мес |
| **Open Source** | SDK — да, infrastructure — нет |

**Возможности:**
- Cloud sandbox environment для выполнения кода
- Pre-built templates (Python, Node.js, Go, Rust, etc.)
- Custom sandbox templates (Dockerfile-based)
- File system access (isolated)
- Network access control
- Session persistence (до 15 мин idle)
- Real-time stdout/stderr streaming

**Пример (Python):**
```python
from e2b import Sandbox

sandbox = Sandbox(template="python")
execution = sandbox.run_code("print('Hello, World!')")
print(execution.logs.stdout)  # Hello, World!
```

### Jupyter Kernel

| Параметр | Значение |
|----------|----------|
| **URL** | https://jupyter.org/ |
| **GitHub** | https://github.com/jupyter/jupyter |
| **API** | WebSocket (Jupyter Protocol) |
| **Модели** | N/A |
| **Цены** | Open Source (BSD) |
| **Open Source** | Да |

**Возможности:**
- Interactive code execution (cell-based)
- Rich output (HTML, images, plots, LaTeX)
- Stateful sessions (переменные сохраняются между ячейками)
- Multi-language kernels (Python, R, Julia, etc.)
- Magic commands (%timeit, %load, %run)

**Интеграция с агентами:**
```python
import jupyter_client

km, kc = jupyter_client.manager.start_new_kernel(kernel_name="python3")
kc.execute("x = 42")
kc.execute("print(x)")  # 42
```

### Docker Sandbox

| Параметр | Значение |
|----------|----------|
| **URL** | https://www.docker.com/ |
| **GitHub** | https://github.com/docker/cli |
| **API** | CLI, Python (docker-py), Go |
| **Модели** | N/A |
| **Цены** | Open Source (Apache 2.0) |
| **Open Source** | Да |

**Возможности:**
- Full OS-level isolation
- Custom images для любых языков/зависимостей
- Resource limits (CPU, memory, disk)
- Network isolation
- Volume mounts для file I/O
- Ephemeral containers (auto-cleanup)

**Пример:**
```python
import docker

client = docker.from_env()
container = client.containers.run(
    "python:3.11-slim",
    command="python -c 'print(42)'",
    remove=True,
    mem_limit="512m",
    cpu_quota=50000
)
```

### Google Cloud Run / Cloud Functions

| Параметр | Значение |
|----------|----------|
| **URL** | https://cloud.google.com/run |
| **API** | REST, gRPC, Python/Go SDK |
| **Модели** | N/A |
| **Цены** | Pay-per-use ($0.0000025/vCPU-second) |
| **Open Source** | Нет |

**Возможности:**
- Serverless code execution
- Auto-scaling (0 to N instances)
- HTTP-triggered execution
- Custom containers
- Built-in monitoring и logging

### Replit Ghostwriter / Repl.it API

| Параметр | Значение |
|----------|----------|
| **URL** | https://replit.com/ |
| **API** | REST, WebSocket |
| **Модели** | Ghostwriter (AI assistant) |
| **Цены** | Free tier → Paid от $7/мес |
| **Open Source** | Нет |

**Возможности:**
- Cloud IDE с execution environment
- Multi-language support (50+ языков)
- Real-time collaboration
- AI-powered code completion (Ghostwriter)
- Deploy hosting

### LangChain Code Tools

| Параметр | Значение |
|----------|----------|
| **URL** | https://python.langchain.com/ |
| **API** | Python SDK |
| **Модели** | Model-agnostic |
| **Цены** | Open Source |
| **Open Source** | Да (MIT) |

**Возможности:**
- `PythonREPLTool` — выполнение Python кода
- `PythonAstREPLTool` — безопасный AST-based REPL
- `JupyterTool` — интеграция с Jupyter kernels
- Интеграция с agent loops

**Пример:**
```python
from langchain_experimental.tools import PythonREPLTool

repl = PythonREPLTool()
result = repl.run("print(2 + 2)")  # 4
```

## Когда использовать

| Сценарий | Рекомендуемый инструмент |
|----------|-------------------------|
| **Cloud sandbox для агентов** | E2B (built for AI agents) |
| **Data analysis / notebooks** | Jupyter Kernel |
| **Full OS isolation** | Docker Sandbox |
| **Serverless production** | Cloud Run / Cloud Functions |
| **LangChain agent** | LangChain PythonREPLTool |
| **Educational / collaborative** | Replit |

## Безопасность и ограничения

- **Sandbox escape** — главная угроза (CVE в runtime, kernel exploits)
- **Resource exhaustion** — лимиты CPU, memory, disk, time
- **Network access** — блокировать outbound по умолчанию
- **File system** — isolated FS, no host access
- **Secrets management** — не передавать credentials в sandbox
- **Audit logging** — логировать все выполнения для forensics

### Пример безопасного wrapper (Python AST)
```python
import ast
import operator

SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def safe_eval(expr: str) -> float:
    tree = ast.parse(expr, mode="eval")
    # Только whitelist операций
    # Запрет импортов, вызовов функций, доступа к атрибутам
    # ...
```

## Интеграция с агентами

### E2B + OpenAI Agent
```python
from e2b import Sandbox
from openai import OpenAI

client = OpenAI()
sandbox = Sandbox(template="python")

def execute_code(code: str) -> str:
    result = sandbox.run_code(code)
    return "".join(result.logs.stdout)

tools = [{
    "type": "function",
    "function": {
        "name": "execute_python",
        "description": "Execute Python code in sandbox",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Python code to execute"}
            },
            "required": ["code"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Calculate factorial of 10"}],
    tools=tools
)
```

### LangChain Agent
```python
from langchain.agents import initialize_agent
from langchain_experimental.tools import PythonREPLTool
from langchain_openai import ChatOpenAI

tools = [PythonREPLTool()]
llm = ChatOpenAI(model="gpt-4o")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
agent.run("What is 25 * 47?")
```

## Связи

- [File System](file-system.md) — file I/O в sandboxed code
- [Browser Automation](browser-automation.md) — web-based code execution
- [Agent Harness](../../patterns/architecture-design/agent-harness.md) — интеграция code execution tools
- [Работа с код-агентами](../../patterns/implementation/working-with-coding-agents.md) — code execution в coding workflows

---

*Добавлено: 2026-07-01*
