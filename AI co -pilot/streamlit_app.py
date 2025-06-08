import streamlit as st
import requests

st.title("🧠 AI Project Management Co-Pilot")

st.header("Create Project")
proj_id = st.text_input("Project ID")
proj_name = st.text_input("Project Name")
proj_desc = st.text_input("Description")

if st.button("Create Project"):
    response = requests.post("http://127.0.0.1:8000/create-project", data={
        "id": proj_id,
        "name": proj_name,
        "description": proj_desc
    })
    st.success("✅ Project Created!")

st.header("Create Task")
task_id = st.text_input("Task ID")
task_proj_id = st.text_input("Project ID for Task")
task_title = st.text_input("Task Title")
task_status = st.selectbox("Status", ["To-Do", "In Progress", "Done"])

if st.button("Create Task"):
    response = requests.post("http://127.0.0.1:8000/create-task", data={
        "id": task_id,
        "project_id": task_proj_id,
        "title": task_title,
        "status": task_status
    })
    st.success("✅ Task Created!")

st.header("Get Tasks for a Project")
lookup_id = st.text_input("Enter Project ID to View Tasks")
if st.button("Get Tasks"):
    res = requests.get(f"http://127.0.0.1:8000/get-tasks?project_id={lookup_id}")
    if res.status_code == 200:
        st.json(res.json())

st.header("AI Recommendation")
if st.button("Get Recommendation"):
    res = requests.get("http://127.0.0.1:8000/get-recommendation")
    if res.status_code == 200:
        result = res.json()
        st.write("🔍 Pending Tasks:", result["pending_tasks"])
        st.success("📌 " + result["recommendation"])
