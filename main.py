from fastapi import FastAPI
from api import tasks_api

app = FastAPI(
    title= "API de Tarefas",
    description="Api simpes para apreender fundamento de designer de API",
    version="1.0.0"
)

app.include_router(tasks_api.router)