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

if not os.path.exists("./database.db"):
    from models.task import Task
    # Cria o arquivo SQLite e as tabelas somente se o arquivo não existir
    Base.metadata.create_all(bind=engine)
