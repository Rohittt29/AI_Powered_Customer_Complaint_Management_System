from fastapi import APIRouter, Depends, UploadFile, File, status
from pydantic import BaseModel
from typing import Any, Dict

from app.schemas.common import GenericSuccessResponse
from app.services.upload_service import UploadService
from app.api.deps import get_db, get_current_user

router = APIRouter()

class UploadResponseData(BaseModel):
    status: str
    complaint_state: Dict[str, Any]

@router.post("", response_model=GenericSuccessResponse[UploadResponseData], status_code=status.HTTP_200_OK)
async def upload_complaint_document(
    file: UploadFile = File(...),
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Upload a complaint document (PDF) for automated extraction.
    """
    # Delegate to service
    result = await UploadService.process_document(db, file)
    
    return GenericSuccessResponse(
        success=True,
        message="Document uploaded and processed successfully.",
        data=UploadResponseData(**result)
    )
