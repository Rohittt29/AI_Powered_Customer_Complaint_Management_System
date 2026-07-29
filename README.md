# AI-Powered Customer Complaint Management System

This is the AI-Powered Customer Complaint Management System for a Pharmaceutical Quality Management System (QMS).

## Architecture

The system is designed with an AI-First workflow using a layered architecture:

- **Frontend:** React 19, Redux Toolkit, Tailwind CSS, TypeScript
- **Backend:** FastAPI, Python 3.12+
- **AI Orchestration:** LangGraph, LangChain, Groq (Gemma2-9B-IT)
- **Database:** PostgreSQL / MySQL (managed via SQLAlchemy)

## Setup Instructions

### Environment Variables

Copy `.env.example` to `.env` and fill in your configuration:

```bash
cp .env.example .env
```

Make sure to provide your `GROQ_API_KEY`.

### Running via Docker Compose

The easiest way to run the entire stack is using Docker Compose:

```bash
docker-compose up --build
```

- Frontend: http://localhost:80
- Backend API Docs: http://localhost:8000/api/docs

### Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
# Activate venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Features

- Conversational AI Copilot for Logging Complaints
- AI-assisted Pharmaceutical Risk Assessment
- Document Upload and OCR Parsing
- Complaint Modification via Natural Language
- Scalable LangGraph state management
