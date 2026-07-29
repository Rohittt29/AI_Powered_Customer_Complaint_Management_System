# AI Powered Customer Complaint Management System

## Overview

A modern, production‑ready web application that enables businesses to capture, classify, and resolve customer complaints using AI. The system consists of:

- **FastAPI backend** (Python) with a PostgreSQL database, Pydantic schemas, and LangChain/LangGraph orchestration.
- **AI agents & tools** that handle complaint extraction, sentiment analysis, routing, and response generation.
- **React frontend** (TypeScript, Vite, Tailwind CSS, Shadcn UI) with Redux Toolkit for state management.
- **CI/CD pipeline** (GitHub Actions) that runs unit, integration, and end‑to‑end tests and builds Docker images.
- **Docker Compose** for easy local development and production deployment behind Nginx.

The architecture follows a clean, decoupled design – the UI never talks directly to the LLM; all AI logic lives in reusable tooling layers accessed via the backend.

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI, Pydantic, SQLAlchemy, PostgreSQL, LangChain, LangGraph |
| **AI** | Groq (Gemma model), custom AI tools & agents |
| **Frontend** | React, TypeScript, Vite, Tailwind CSS, Shadcn UI, Redux Toolkit |
| **Testing** | Pytest, Vitest, React Testing Library, Playwright |
| **CI/CD** | GitHub Actions |
| **Containerisation** | Docker, Docker Compose, Nginx |

---

## Getting Started (Local Development)

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd AI_Powered_Customer_Complaint_Management_System
   ```

2. **Create a `.env` file** in the project root (or copy from `.env.example`). Required variables:
   ```
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=qms_db
   GROQ_API_KEY=your-groq-key
   SECRET_KEY=changeme
   LOG_LEVEL=debug
   ```

3. **Start services with Docker Compose (dev profile)**
   ```bash
   docker compose --profile dev up --build
   ```
   - Backend will be reachable at `http://localhost:8000`
   - Frontend will be reachable at `http://localhost`

4. **Run the test suite**
   ```bash
   # Backend tests
   cd backend && pytest

   # Frontend unit tests
   cd ../frontend && npx vitest run

   # End‑to‑end UI tests
   npx playwright test
   ```

---

## Scripts

- **`backend/scripts/seed_data.py`** – populates the database with sample complaint categories and users.
- **`frontend/src/api/axios.ts`** – centralised Axios instance with interceptors for auth & error handling.
- **`frontend/src/store.ts`** – configures Redux Toolkit store with slices for complaints, chat, UI state.

---

## Architecture Highlights

- **AI Tools Layer**: Reusable functions (`complaint_extraction`, `sentiment_analysis`, …) that encapsulate business logic. Agents invoke tools; tools invoke the LLM via the Groq provider.
- **LangGraph Workflow**: Orchestrates multi‑step AI processing, ensuring deterministic state transitions.
- **Middleware**: Structured JSON logging, rate‑limiting, secure headers, and correlation IDs for observability.
- **Testing Pyramid**: Unit → Integration → End‑to‑End, guaranteeing confidence at every level.

---

## License

MIT © 2026 Rohit Kumar
