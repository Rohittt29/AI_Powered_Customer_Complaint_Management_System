from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from typing import Any, Dict

from app.schemas.common import GenericSuccessResponse
from app.services.chat_service import ChatService
from app.api.deps import get_db, get_current_user

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponseData(BaseModel):
    assistant_message: str
    complaint_state: Dict[str, Any]
    risk_assessment: Dict[str, Any]

@router.post("", response_model=GenericSuccessResponse[ChatResponseData], status_code=status.HTTP_200_OK)
async def send_chat_message(
    request: ChatRequest,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Send conversational input to the AI Copilot.
    This is the primary endpoint used by the frontend.
    """
    # Delegate to service
    result = await ChatService.process_message(db, request.session_id, request.message)
    
    return GenericSuccessResponse(
        success=True,
        message="Message processed successfully.",
        data=ChatResponseData(**result)
    )
