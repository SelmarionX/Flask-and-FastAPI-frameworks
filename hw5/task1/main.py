from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    status: str


tasks = []


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks")
def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    task_index = next((i for i, t in enumerate(tasks) if t.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_index] = task
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_index = next((i for i, t in enumerate(tasks) if t.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_index]
    return {"detail": "Task deleted"}
