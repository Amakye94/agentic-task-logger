from fastapi import FastAPI
from agents.logger_agent import process_event
from agents.analyzer_agent import analyze

app = FastAPI()

# In-memory storage (you already had something similar)
logs = []

@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}


@app.post("/log")
def log_event():
    # Step 1: Agent processes event
    processed_log = process_event("button_click")

    # Step 2: Second agent analyzes it
    insight = analyze(processed_log)

    # Step 3: Store everything
    log_entry = {
        "data": processed_log,
        "insight": insight
    }

    logs.append(log_entry)

    return {
        "message": "Logged with AI agents 🤖",
        "log": log_entry
    }


@app.get("/logs")
def get_logs():
    return logs

#(venv) PS C:\Users\amaky\OneDrive\Desktop\Agentic AI\agentic-ai-project\agentic-task-logger> streamlit run frontend/app.py