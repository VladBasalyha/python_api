from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    task_name: str
    priority: str
    date: Union[str, None] = None


@app.get("/")
def read_root():
    return {"Завдання": "API для керування завданнями"}


@app.get("/tasks/{task_id}")
def read_item(task_id: int, task: Union[str, None] = "Поки немає завдань"):
    return {"task_id": task_id, "task": task}


# @app.put("/tasks/{task_id}", response_model=Task)
# def update_item(task_id: int, task: Task):
#     return {"task_name": task.task, "task_id": task_id}
    