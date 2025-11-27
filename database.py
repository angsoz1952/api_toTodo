import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)
Base = declarative_base()

## injet depend - sessão banco
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

from models.task import Task
from models.user import User
# Cria as tabelas se não existirem
Base.metadata.create_all(bind=engine)
