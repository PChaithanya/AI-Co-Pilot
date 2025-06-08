import streamlit as st
import requests

st.set_page_config(page_title="AI Project Management Co-Pilot", layout="centered")

API_URL = "http://127.0.0.1:8000"

# --- PAGE NAVIGATION ---
page = st.sidebar.radio("Navigation", ["Create Project", "Project Created"])

if page == "Create Project":
    st.title("🚀 AI Project Management Co-Pilot")

    st.header("Create Project")
    proj_id = st.text_input("Project ID")
    proj_name = st.text_input("Project Name")
    proj_desc = st.text_input("Description")

    if st.button("Create"):
        payload = {
            "project_id": int(proj_id),
            "name": proj_name,
            "description": proj_desc
        }
        response = requests.post(f"{API_URL}/projects", json=payload)
        if response.status_code == 200:
            st.success("✅ Project Created Successfully!")
            st.session_state['page'] = "Project Created"
            st.experimental_rerun()
        else:
            st.error("❌ Failed to create project.")

elif page == "Project Created":
    st.header("✅ Project Created Successfully")
    st.write("You can now create tasks or view project details.")
