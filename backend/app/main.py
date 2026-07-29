import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="AI-Powered Customer Complaint Management System API",
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Restrict this in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from app.api import complaint, chat, upload, risk, health

    app.include_router(complaint.router, prefix="/api/v1/complaints", tags=["Complaints"])
    app.include_router(chat.router, prefix="/api/v1/chat", tags=["Copilot"])
    app.include_router(upload.router, prefix="/api/v1/upload", tags=["Upload"])
    app.include_router(risk.router, prefix="/api/v1/risk", tags=["Risk Assessment"])
    app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

    return app

app = create_app()
