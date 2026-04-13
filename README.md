# 🚀 Agentic Task Logger

## 📌 Description

A simple one-button agentic application that logs user actions into a database via a backend API.

This project demonstrates a minimal full-stack architecture where a frontend interacts with a backend service, which then persists data in a database.

* Frontend: Streamlit
* Backend: FastAPI
* Database: SQLite
* Deployment: Docker Compose

---

## ▶️ Run the App

To run the application locally using Docker:

```bash
docker-compose up --build
```

Once running, open your browser and go to:

http://localhost:8501

Click the button to trigger a request to the backend and store a log entry.

---

## 🏗️ Architecture

The system follows a simple client-server architecture:

Frontend (Streamlit)
→ sends POST request
→ Backend (FastAPI)
→ stores data in SQLite database

### Components:

* **Frontend**: Provides a UI with a single button
* **Backend**: Exposes an API endpoint (`/log`)
* **Database**: Stores logs with timestamps

---

## 🔌 API Endpoints

### POST `/log`

* Triggered when the button is clicked
* Saves a log entry to the database

### GET `/logs` (Optional Extension)

```python
@app.get("/logs")
def get_logs():
    return logs
```

* Returns all stored logs
* Useful for debugging and traceability

---

## 🤖 Agentic Development Approach

This project was developed using a collaboration between a human developer and AI agents.

### Human Responsibilities

* Defined the project idea and architecture
* Guided development direction
* Validated outputs and debugging

### AI Agent Responsibilities

* Generated backend code using FastAPI
* Generated frontend UI using Streamlit
* Assisted with Docker containerization
* Helped debug networking and integration issues

### Asynchronous Development

* Tasks were iteratively generated and refined using AI
* Frontend and backend were developed in parallel
* Continuous testing ensured integration worked correctly

### Alignment Strategy

* Incremental development (build → test → refine)
* Validation through logs and UI feedback
* Ensured end-to-end functionality (button → API → database)

---

## ⚙️ Optimization

The application was designed with the following considerations:

* **Performance**: Lightweight FastAPI backend ensures fast API responses
* **Development Time**: Reduced significantly using AI-assisted coding
* **Cost**: Minimal (uses local environment and open-source tools)
* **Accuracy**: Verified through API responses and stored logs
* **Usability**: Simple and intuitive one-button interface
* **Security**: Runs locally (can be extended with authentication)
* **Scalability**: Containerized using Docker for easy scaling
* **Maintainability**: Clear separation between frontend and backend
* **Traceability**: Logs stored in database for tracking actions

---

## 🐳 Containerization

This project is fully containerized using Docker.

* `docker-compose.yml` orchestrates frontend and backend services
* Services communicate via Docker network (using service names, e.g., `backend`)
* Ensures consistent environment across systems

---

## 📁 Project Structure

```
agentic-task-logger/
│
├── backend/          # FastAPI backend
├── frontend/         # Streamlit frontend
├── agents/           # (optional AI-related logic)
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── tasks.db          # SQLite database
```

---

## 🚀 Future Improvements

* Add a UI to display logs
* Implement authentication
* Deploy to cloud (AWS, GCP, Azure)
* Add more agent-based automation features

---

## 👨‍💻 Author

Developed as part of the *Innovation and Complexity Management* course
Deggendorf Institute of Technology

---
