# API de Tarefas

> Aplicação mínima em FastAPI

Resumo
- Código principal em `main.py` — contém modelos SQLAlchemy, schemas Pydantic, dependência de sessão e dois endpoints:
  - `POST /task` — cria uma nova tarefa (recebe `TaskCreate`, retorna `TaskResponse`, status 201)
  - `GET /` — lista todas as tarefas (retorna `List[TaskResponse]`)
- Banco: SQLite local (`database.db`) criado automaticamente por SQLAlchemy.

Dependências
- Ver `requirements.txt` (FastAPI, SQLAlchemy, Pydantic, Uvicorn etc.).

Instalação (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Executando localmente
```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
# A API ficará disponível em http://127.0.0.1:8000
```

Notas de implementação (pontos importantes para contributors/IA)
- Arquivo único: `main.py` contém toda a lógica (models, schemas, endpoints). Expanda em módulos se a app crescer.
- A sessão do banco é fornecida por `get_db()` e usada via `Depends(get_db)` nos endpoints — mantenha esse padrão ao adicionar endpoints que acessam o DB.
- Schema `TaskResponse` usa `Config.from_attributes = True` para permitir retorno direto de instâncias SQLAlchemy.
- O banco é `sqlite:///./database.db` com `connect_args={"check_same_thread": False}`; cuidado com concorrência em produção.

Endereços úteis
- Código: `main.py`
- Dependências: `requirements.txt`