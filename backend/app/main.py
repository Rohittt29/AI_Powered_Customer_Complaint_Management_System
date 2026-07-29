"""
FastAPI Application Entry Point.
Configures the application factory with middleware, routers, and OpenAPI docs.
"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.security import (
    SecurityHeadersMiddleware,
    RateLimitMiddleware,
    RequestSizeLimitMiddleware,
)

# Configure structured logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# --- OpenAPI Metadata ---
TAGS_METADATA = [
    {"name": "Complaints", "description": "CRUD operations for pharmaceutical complaints."},
    {"name": "Copilot", "description": "AI Copilot conversational interface powered by LangGraph + Groq."},
    {"name": "Upload", "description": "Upload PDF documents for OCR extraction."},
    {"name": "Risk Assessment", "description": "AI-generated pharmaceutical risk profiling."},
    {"name": "Health", "description": "System health, readiness, and liveness checks."},
]


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=(
            "# AI-Powered Customer Complaint Management System\n\n"
            "An enterprise-grade QMS platform that uses **LangGraph** orchestration, "
            "**Groq LLM** inference, and a **React** frontend to automate "
            "pharmaceutical complaint intake, risk assessment, and resolution.\n\n"
            "## Key Capabilities\n"
            "- Natural language complaint intake via AI Copilot\n"
            "- Automated PDF/OCR document extraction\n"
            "- Real-time pharmaceutical risk assessment\n"
            "- Multi-agent LangGraph workflow orchestration\n"
        ),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        openapi_tags=TAGS_METADATA,
        contact={"name": "QMS AI Team", "email": "support@qms-ai.dev"},
        license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    )

    # --- Middleware Stack (order matters: outermost runs first) ---
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(RequestSizeLimitMiddleware)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://localhost:80"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # --- Routers ---
    from app.api import complaint, chat, upload, risk, health

    app.include_router(complaint.router, prefix="/api/v1/complaints", tags=["Complaints"])
    app.include_router(chat.router, prefix="/api/v1/chat", tags=["Copilot"])
    app.include_router(upload.router, prefix="/api/v1/upload", tags=["Upload"])
    app.include_router(risk.router, prefix="/api/v1/risk", tags=["Risk Assessment"])
    app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

    logger.info(f"Application '{settings.PROJECT_NAME}' v{settings.VERSION} started [{settings.ENVIRONMENT}]")
    return app


app = create_app()
