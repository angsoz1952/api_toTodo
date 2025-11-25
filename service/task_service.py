from repository.task_repository import create_task_repository, list_all_repository, get_task_by_id_repository, delete_task_repository, update_task_repository
from schemas.task import TaskCreate
from sqlalchemy.orm import Session
from models.task import Task

class TaskService:

    @staticmethod
    def create_task(task: TaskCreate, db: Session):
        news_task = Task(
            title=task.title.upper(),
            description=task.description.capitalize(),
            done=task.done
        )
        return create_task_repository(news_task, db)


    @staticmethod
    def list_all(db: Session):
        return  list_all_repository(db) 


    @staticmethod
    def get_task_by_id(task_id: int, db: Session):
        return get_task_by_id_repository(task_id, db)


    @staticmethod
    def delete_task(task_id: int, db: Session):
        task = get_task_by_id_repository(task_id, db)
        return delete_task_repository(task, db)


    @staticmethod
    def update_task(task: Task, db: Session, updates = {}):
        return update_task_repository(task, db, updates)


