from database import Base
from sqlalchemy import Column, Integer, Boolean, String


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    done = Column(Boolean, default=False)
