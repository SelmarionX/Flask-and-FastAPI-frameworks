from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Создаем список задач
tasks = []


# Модель Task
class Task(BaseModel):
    id: int
    title: str
    description: str
    done: bool


# Получить список задач
@app.get("/tasks")
async def get_tasks():
    return tasks


# Создать новую задачу
@app.post("/tasks")
async def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task


# Получить задачу по id
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Обновить задачу по id
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Удалить задачу по id
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
