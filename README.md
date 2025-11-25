# API de Tarefas

Uma API REST para gerenciamento de tarefas (todo list) construída com FastAPI e SQLAlchemy.

## Funcionalidades

- Criar, listar, obter, atualizar e deletar tarefas.
- Banco de dados SQLite local.
- Estrutura modular: API, modelos, repositório, serviços e schemas.

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação FastAPI.
- `database.py`: Configuração do banco de dados.
- `api/tasks_api.py`: Endpoints da API para tarefas.
- `models/task.py`: Modelo SQLAlchemy para Task.
- `schemas/task.py`: Schemas Pydantic para TaskCreate e TaskResponse.
- `repository/task_repository.py`: Funções de acesso ao banco.
- `service/task_service.py`: Lógica de negócio.
- `requirements.txt`: Dependências Python.

## Dependências

Verifique `requirements.txt` para as bibliotecas necessárias (FastAPI, SQLAlchemy, Pydantic, Uvicorn, etc.).

## Instalação (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Executando Localmente

```powershell
fastapi dev main.py
# A API ficará disponível em http://127.0.0.1:8000
# Documentação automática em http://127.0.0.1:8000/docs
```

## Endpoints

- `POST /tasks/create`: Cria uma nova tarefa (status 201).
- `GET /tasks/`: Lista todas as tarefas.
- `GET /tasks/{task_id}`: Obtém uma tarefa pelo ID.
- `PUT /tasks/{task_id}`: Atualiza uma tarefa pelo ID.
- `DELETE /tasks/{task_id}`: Deleta uma tarefa pelo ID (retorna mensagem e tarefa deletada).

## Notas de Implementação

- A sessão do banco é gerenciada por `get_db()` em `database.py`.
- Use `Depends(get_db)` nos endpoints que acessam o banco.
- Schemas usam `Config.from_attributes = True` para conversão de objetos SQLAlchemy.
- Banco: SQLite (`sqlite:///./database.db`).

## Endereços Úteis

- Código principal: `main.py`
- Dependências: `requirements.txt`
- Documentação FastAPI: `/docs` ou `/redoc`
