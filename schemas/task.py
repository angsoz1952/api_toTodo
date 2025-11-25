from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool

    class Config: 
        from_attributes = True 
