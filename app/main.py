from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from routers import task, user

app = FastAPI()
info_ed = ('<h2>Домашнее задание по теме "Миграции. Библиотека alembic."<br>'
           '<h3>Цель: усвоить новые правила структурирования проекта с использованием FastAPI.'
           '<br>Научиться создавать миграции и подтверждать их при помощи alembic.'
           '<br>Задача "Миграции alembic":'
           '<br>Студент Крылов Эдуард Васильевич'
           '<br>Дата: 06.12.2024г.</h3>')


# python -m uvicorn main:app
# Get
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


@app.get("/info", response_class=HTMLResponse)
async def info():
    return info_ed


app.include_router(task.router)
app.include_router(user.router)
# python -m uvicorn main:app
