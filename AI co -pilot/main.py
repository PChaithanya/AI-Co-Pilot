from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

projects = []
tasks = []

class Project(BaseModel):
    project_id: int
    name: str
    description: str

class Task(BaseModel):
    task_id: int
    project_id: int
    title: str
    status: str

@app.get("/")
def root():
    return {"message": "Welcome to the AI Co-Pilot API!"}

@app.post("/projects")
def create_project(project: Project):
    projects.append(project)
    return {"message": "Project created", "project": project}

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task created", "task": task}

@app.get("/projects")
def get_projects():
    return projects

@app.get("/tasks/{project_id}")
def get_tasks_by_project(project_id: int):
    return [task for task in tasks if task.project_id == project_id]
