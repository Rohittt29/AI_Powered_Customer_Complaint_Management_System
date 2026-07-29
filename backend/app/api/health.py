from fastapi import APIRouter, status
from pydantic import BaseModel

from app.schemas.common import GenericSuccessResponse
from app.core.config import settings

router = APIRouter()

class HealthCheckResponse(BaseModel):
    status: str
    version: str

@router.get("", response_model=HealthCheckResponse, status_code=status.HTTP_200_OK)
async def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return HealthCheckResponse(status="UP", version=settings.VERSION)
