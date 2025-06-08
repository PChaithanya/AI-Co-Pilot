from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

projects = []
tasks = []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/create-project")
async def create_project(id: int = Form(...), name: str = Form(...), description: str = Form(...)):
    projects.append({"id": id, "name": name, "description": description})
    return RedirectResponse("/", status_code=303)

@app.post("/create-task")
async def create_task(id: int = Form(...), project_id: int = Form(...), title: str = Form(...), status: str = Form(...)):
    tasks.append({"id": id, "project_id": project_id, "title": title, "status": status})
    return RedirectResponse("/", status_code=303)

@app.get("/get-tasks")
async def get_tasks(project_id: int):
    result = [t for t in tasks if t["project_id"] == project_id]
    return result

@app.get("/get-recommendation")
async def recommendation():
    pending = len([t for t in tasks if t["status"] != "Done"])
    return {"pending_tasks": pending, "recommendation": "Complete pending tasks to stay on track."}

if __name__ == "__main__":
    uvicorn.run("run:app", reload=True)
