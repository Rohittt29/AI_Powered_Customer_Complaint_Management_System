"""
Root conftest.py – Shared pytest fixtures for the entire backend test suite.
Provides mock database sessions, test client, and patched settings
so tests run without a live PostgreSQL or Groq API key.
"""
import os
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

# Patch environment variables BEFORE any app code is imported
os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")
os.environ.setdefault("GROQ_API_KEY", "test-key-not-real")
os.environ.setdefault("ENVIRONMENT", "test")

from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.fixture
def mock_db():
    """Provide a mocked database session for unit tests."""
    session = MagicMock()
    session.commit = MagicMock()
    session.rollback = MagicMock()
    session.close = MagicMock()
    return session


@pytest.fixture
async def async_client():
    """
    Provide an async HTTP client wired to the FastAPI test app.
    Overrides get_db and get_current_user so no real DB or auth is needed.
    """
    from app.api.deps import get_db, get_current_user

    def _override_db():
        yield MagicMock()

    def _override_user():
        return {"user_id": "test-user", "role": "QA_Executive"}

    app.dependency_overrides[get_db] = _override_db
    app.dependency_overrides[get_current_user] = _override_user

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client

    app.dependency_overrides.clear()
