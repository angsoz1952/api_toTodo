from fastapi import APIRouter, Depends, status, HTTPException
from schemas.task import TaskCreate, TaskResponse
from database import get_db
from service.task_service import TaskService
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/create", response_model= TaskResponse, status_code=status.HTTP_201_CREATED, description="Cria uma nova tarefa")
def create_task(task: TaskCreate, db: Session =  Depends(get_db)):
    task = TaskService.create_task(task, db)
    return task


@router.get("/", response_model= List[TaskResponse], status_code=status.HTTP_200_OK, description="Lista todas as tarefas")
def list_all( db: Session =  Depends(get_db)):
    return TaskService.list_all(db)


@router.get("/{task_id}", response_model= TaskResponse, status_code=status.HTTP_200_OK, description="Obtém uma tarefa pelo ID")
def get_task_by_id(task_id: int, db: Session =  Depends(get_db)):
    task = TaskService.get_task_by_id(task_id, db)
    return task
     

@router.delete("/{task_id}", status_code=status.HTTP_200_OK, description="Deleta uma tarefa pelo ID")
def delete_task(task_id: int, db: Session =  Depends(get_db)):
    result = TaskService.delete_task(task_id, db)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Tarefa deletada com sucesso", "task": result}


@router.put("/{task_id}", response_model= TaskResponse, status_code=status.HTTP_200_OK, description="Atualiza uma tarefa pelo ID")
def update_task(task_id: int, updates: TaskCreate, db: Session =  Depends(get_db)):

    task = TaskService.get_task_by_id(task_id, db)
    
    updated_task = TaskService.update_task(task, db, updates.dict(exclude_unset=True))
    return updated_task