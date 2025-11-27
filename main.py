from fastapi import FastAPI
from api import tasks_api, user_api

app = FastAPI(
    title= "API de Tarefas",
    description="Api simpes para apreender fundamento de designer de API",
    version="1.0.0"
)

app.include_router(tasks_api.router)
app.include_router(user_api.router)