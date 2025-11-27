from sqlalchemy.orm import Session
from schemas.task import TaskCreate
from models.task import Task
from database import get_db

def create_task_repository(task: TaskCreate, db: Session):

    # Adiconando na sessão do banco
    db.add(task)

    # salva no banco
    db.commit()
    
    #Atualiza o objeto com o id gerado pelo banco
    db.refresh(task)

    # retorna a tarefa criada
    return task

def list_all_repository(db: Session, user_id: int):

    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    
    return tasks
    
def get_task_by_id_repository(task_id: int,  db: Session, user_id: int):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    return task

def delete_task_repository(task, db: Session):
    if not task:
        return None

    db.delete(task)
    db.commit()

    return task


def update_task_repository(task: Task, db: Session, updates = {}):

    for key, value in updates.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task 