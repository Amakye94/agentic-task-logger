from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# simple in-memory "database"
logs = []

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

@app.post("/log")
def log_action():
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "message": "Button clicked"
    }
    logs.append(log_entry)
    return {"status": "saved", "data": log_entry}

@app.get("/logs")
def get_logs():
    return logs

#(venv) PS C:\Users\amaky\OneDrive\Desktop\Agentic AI\agentic-ai-project\agentic-task-logger> streamlit run frontend/app.py