async function createProject() {
    const data = {
        id: parseInt(document.getElementById("projectId").value),
        name: document.getElementById("projectName").value,
        description: document.getElementById("projectDesc").value
    };
    const res = await fetch("/projects/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    alert("Project created!");
}

async function createTask() {
    const data = {
        id: parseInt(document.getElementById("taskId").value),
        project_id: parseInt(document.getElementById("taskProjectId").value),
        title: document.getElementById("taskTitle").value,
        status: document.getElementById("taskStatus").value
    };
    const res = await fetch("/tasks/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    alert("Task created!");
}

async function getTasks() {
    const projectId = document.getElementById("getTasksProjectId").value;
    const res = await fetch(`/projects/${projectId}/tasks/`);
    const tasks = await res.json();
    document.getElementById("tasksResult").textContent = JSON.stringify(tasks, null, 2);
}

async function getRecommendation() {
    const res = await fetch("/recommendations/");
    const data = await res.json();
    document.getElementById("recommendationResult").textContent = JSON.stringify(data, null, 2);
}
