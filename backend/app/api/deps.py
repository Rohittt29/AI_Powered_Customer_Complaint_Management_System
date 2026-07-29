from typing import Generator
from fastapi import Depends, HTTPException, status
from app.core.config import settings

def get_db() -> Generator:
    """
    Dependency for getting database sessions.
    TODO: Implement SQLAlchemy sessionmaker yield in Module 2/DB.
    """
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
    yield None

def get_current_user():
    """
    Dependency for extracting the current authenticated user.
    TODO: Implement JWT validation and RBAC.
    """
    return {"user_id": "system", "role": "QA_Executive"}

def get_config():
    """
    Dependency for accessing application configuration.
    """
    return settings
