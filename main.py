from sqlalchemy import create_engine, Column, Integer, Boolean, String
import os
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from typing import List

#confi database
DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)
Base = declarative_base()


#Models
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    done = Column(Boolean, default=False)

db_path = os.path.join(os.path.dirname(__file__), "database.db")
if not os.path.exists(db_path):
    # Cria o arquivo SQLite e as tabelas somente se o arquivo não existir
    Base.metadata.create_all(bind=engine)


## Schemas
class TaskCreate(BaseModel):
    title: str
    description: str | None
    done: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    done: bool

    class Config: 
        from_attributes = True 


## injet depend - sessão banco
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

## FASTAPI

app = FastAPI(
    title= "API de Tarefas",
    description="Api simpes para apreender fundamento de designer de API",
    version="1.0.0"
)


@app.post("/task", response_model= TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session =  Depends(get_db)):

    # criando ums instância da class Taks com os dados recebido
    new_task = Task (
        title = task.title,
        description = task.description,
        done = task.done
    )

    # Adiconando na sessão do banco
    db.add(new_task)

    # salva no banco
    db.commit()
    
    #Atualiza o objeto com o id gerado pelo banco
    db.refresh(new_task)

    # retorna a tarefa criada
    return new_task


#Criado nosso get
@app.get("/", response_model= List[TaskResponse])
def list_all( db: Session =  Depends(get_db)):

    # realziando select * na tabela task

    tasks = db.query(Task).all()
    
    return tasks
