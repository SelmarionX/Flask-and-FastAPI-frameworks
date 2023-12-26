from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


tasks: List[Task] = []


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"сообщение": "Задача создана успешно"}


@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    for i, t in enumerate(tasks):
        if t.id == id:
            tasks[i] = task
            return {"сообщение": "Задача обновлена успешно"}
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete("/tasks/{id}")
def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task.id == id:
            del tasks[i]
            return {"сообщение": "Задача удалена успешно"}
    raise HTTPException(status_code=404, detail="Задача не найдена")
